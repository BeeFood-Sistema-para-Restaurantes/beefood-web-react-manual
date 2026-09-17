#!/usr/bin/env python3
"""Transforma um slide em vídeo, com a tela do mockup rodando de verdade.

Carrossel do Instagram aceita vídeo no lugar de uma imagem. Quando a novidade
**é** movimento — capa em vídeo, vitrine em vídeo —, a capa parada gasta o
melhor argumento da peça: o leitor tem de acreditar que aquilo se mexe.

O slide continua sendo o mesmo HTML, e o PNG entregue continua o mesmo. Este
script só põe o filme dentro da tela do aparelho:

1. renderiza o slide e **mede no DOM** a caixa da imagem que vai virar filme
   (`--alvo`, um seletor CSS dentro do slide);
2. abre o cardápio público com a nossa mídia injetada (o mesmo caminho do
   `capturar-cardapio.py`) e fotografa quadro a quadro, avançando o
   `currentTime` do `<video>` na mão — assim cada quadro é determinístico, e o
   carrossel do cardápio não gira sozinho no meio da filmagem;
3. costura os quadros por cima do PNG do slide com o FFmpeg.

A captura quadro a quadro é mais lenta que gravar a tela, e é o que dá quadro
limpo: gravação de página em Chromium headless sai com taxa irregular, e o zoom
lento do banner aparece aos trancos.

Uso:
    python filmar-slide.py carrosseis/<slug>/slides/01-capa.html \\
        --tomada pc-capa-video \\
        --conteudo carrosseis/<slug>/midias.json \\
        --saida carrosseis/<slug>/video/01-capa.mp4

Saída: MP4 H.264, 1080x1350, mudo (o cardápio toca `<video muted>`).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))

import renderizar  # noqa: E402

MARCA = renderizar.MARCA


def modulo_cardapio():
    """`capturar-cardapio.py` tem hífen no nome e não entra com `import`."""
    spec = importlib.util.spec_from_file_location(
        "capturar_cardapio", AQUI / "capturar-cardapio.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fundo_e_alvo(slide: Path, alvo: str, largura: int, altura: int,
                 fundo: Path) -> dict:
    """Guarda o PNG do slide e mede, no DOM, a caixa da imagem a ser filmada."""
    from playwright.sync_api import sync_playwright

    html = renderizar.documento(slide.read_text(encoding="utf-8"),
                                largura, altura, slide.parent, False,
                                MARCA["formato_padrao"])
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False,
                                     encoding="utf-8") as f:
        f.write(html)
        arquivo = Path(f.name)
    try:
        with sync_playwright() as p:
            navegador = p.chromium.launch()
            pagina = navegador.new_context(
                viewport={"width": largura, "height": altura},
                device_scale_factor=1, locale="pt-BR").new_page()
            pagina.goto(arquivo.as_uri(), wait_until="load")
            pagina.evaluate("document.fonts.ready")
            pagina.wait_for_timeout(300)
            caixa = pagina.evaluate(
                """(alvo) => {
                  const e = document.querySelector(alvo);
                  if (!e) throw new Error('não achei ' + alvo + ' no slide');
                  const c = e.getBoundingClientRect();
                  return {x: Math.round(c.x), y: Math.round(c.y),
                          w: Math.round(c.width), h: Math.round(c.height)};
                }""", alvo)
            pagina.screenshot(path=str(fundo), type="png")
            navegador.close()
    finally:
        arquivo.unlink(missing_ok=True)
    # Largura e altura ímpares quebram o yuv420p do H.264.
    caixa["w"] -= caixa["w"] % 2
    caixa["h"] -= caixa["h"] % 2
    return caixa


def parar_relogios(pagina) -> None:
    """Desliga os temporizadores da página, para o carrossel parar de girar.

    Cada quadro custa quase um segundo de relógio real, então 6 s de filme levam
    mais de um minuto de captura — e nesse tempo o carrossel do cardápio troca
    de mídia sozinho várias vezes. No filme isso sai como banner piscando.

    O vídeo não depende de temporizador aqui: quem manda no `currentTime` é o
    `congelar_video`, quadro a quadro. Então derrubar os `setTimeout` e
    `setInterval` pendentes congela o carrossel e deixa o vídeo andar.
    """
    pagina.evaluate("""() => {
        const ultimo = setTimeout(() => {}, 0);
        for (let i = 0; i <= ultimo; i++) { clearTimeout(i); clearInterval(i); }
    }""")


def filmar_cardapio(cd, args, pasta: Path, quadros: int) -> None:
    """Fotografa a tela do cardápio quadro a quadro, com o vídeo no tempo certo."""
    from playwright.sync_api import sync_playwright

    receita = cd.TOMADAS[args.tomada]
    conteudo = json.loads(Path(args.conteudo).read_text(encoding="utf-8"))
    banners = cd.montar_banners(conteudo)
    avisos = cd.montar_avisos(conteudo)
    biblioteca = Path(args.biblioteca)

    with sync_playwright() as p:
        navegador = p.chromium.launch(
            args=["--autoplay-policy=no-user-gesture-required"])
        ctx = navegador.new_context(
            locale="pt-BR", timezone_id="America/Sao_Paulo",
            service_workers="block", **cd.APARELHOS[receita["aparelho"]])
        ctx.route("**/validaDelivery**", lambda rota: rota.fulfill(
            status=200, content_type="application/json",
            body=cd.remendar_config(rota.fetch().text(), banners, avisos)))
        ctx.route(f"**/{cd.PASTA_FALSA}/*",
                  lambda rota: cd.responder_midia(rota, biblioteca))

        pagina = ctx.new_page()
        pagina.goto(args.url, wait_until="networkidle", timeout=120_000)
        pagina.wait_for_timeout(6000)
        cd.limpar(pagina)
        if receita.get("rolar"):
            cd.rolar_para(pagina, receita["rolar"])
        if receita.get("midia"):
            cd.ir_para_midia(pagina, *receita["midia"])
        parar_relogios(pagina)

        for i in range(quadros):
            cd.congelar_video(pagina, i / args.fps)
            pagina.screenshot(path=str(pasta / f"{i:04d}.png"), type="png")
        navegador.close()


def costurar(fundo: Path, quadros: Path, caixa: dict, destino: Path,
             fps: int) -> None:
    destino.parent.mkdir(parents=True, exist_ok=True)
    filtro = (f"[1:v]scale={caixa['w']}:{caixa['h']}[tela];"
              f"[0:v][tela]overlay={caixa['x']}:{caixa['y']}:shortest=1")
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error",
        "-loop", "1", "-i", str(fundo),
        "-framerate", str(fps), "-i", str(quadros / "%04d.png"),
        "-filter_complex", filtro,
        "-c:v", "libx264", "-profile:v", "high", "-crf", "18",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an",
        str(destino),
    ], check=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slide", type=lambda v: Path(v).resolve(),
                    help="o fragmento .html do slide")
    ap.add_argument("--alvo", default=".notebook__tela img, .celular__tela img",
                    help="seletor da imagem que vira filme")
    ap.add_argument("--tomada", required=True,
                    help="tomada do capturar-cardapio.py (ex.: pc-capa-video)")
    ap.add_argument("--conteudo", required=True, help="JSON das mídias")
    ap.add_argument("--biblioteca", default=str(SKILL / "assets" / "midia"))
    ap.add_argument("--url", default=None)
    ap.add_argument("--saida", required=True, type=Path)
    ap.add_argument("--segundos", type=float, default=6.0)
    ap.add_argument("--fps", type=int, default=15)
    args = ap.parse_args()

    cd = modulo_cardapio()
    args.url = args.url or cd.URL_PADRAO
    if args.tomada not in cd.TOMADAS:
        sys.exit(f"ERRO: tomada {args.tomada} não existe")

    largura, altura = MARCA["formatos"][MARCA["formato_padrao"]]
    quadros = int(args.segundos * args.fps)
    tmp = Path(tempfile.mkdtemp(prefix="filme-slide-"))
    try:
        fundo = tmp / "fundo.png"
        caixa = fundo_e_alvo(args.slide, args.alvo, largura, altura, fundo)
        print(f"--> tela do mockup em {caixa['x']},{caixa['y']} "
              f"({caixa['w']}x{caixa['h']})")

        pasta = tmp / "quadros"
        pasta.mkdir()
        filmar_cardapio(cd, args, pasta, quadros)
        costurar(fundo, pasta, caixa, args.saida, args.fps)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    tamanho = args.saida.stat().st_size / 1024
    print(f"OK  {args.saida}  {largura}x{altura}  "
          f"{args.segundos:g}s  {tamanho:.0f} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
