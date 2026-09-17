#!/usr/bin/env python3
"""Estúdio de mídia: gera o banner, o cartaz e o vídeo que o cliente subiria.

Existe por causa de uma novidade inteira: capa, vitrine e avisos do Cardápio
Digital aceitam **imagem e vídeo**. Para mostrar isso não dá para usar print de
loja de cliente nem foto solta — a arte É o assunto. Então a arte é nossa, feita
aqui, e entra no cardápio de exemplo pelo `capturar-cardapio.py`.

O que o sistema aceita (do manual de Capas e Destaques e do de Avisos):

| Peça  | Medida    | Arquivo                             |
|-------|-----------|-------------------------------------|
| capa  | 1920x580  | JPG/PNG/WEBP/GIF, ou MP4 H.264/WEBM |
| loja  | 1920x580  | idem (até 15 MB, sem áudio)         |
| aviso | 1080x1080 | só imagem                           |

Por que 1920x580 e não 16/9: o cardápio mostra o banner numa faixa com
`object-fit: cover` — ~4,1/1 no computador, ~2,6/1 no celular. Arte 16/9 chega
lá e perde metade da altura. A conta está no `arte.css`.

Vídeo sai **H.264, sem faixa de áudio**: é o que toca em Android e iPhone.
HEVC/H.265 dá tela preta no Android sem nem avisar erro, por isso o
`-c:v libx264` é fixo aqui.

Uso:
    python fazer-midia.py                      # tudo o que estiver no catálogo
    python fazer-midia.py --peca capa-chapa-smash
    python fazer-midia.py --listar

Entrada : assets/midia/artes/*.html  (fragmento de body + assets/midia/arte.css)
Saída   : assets/midia/*.jpg  *.png  *.mp4

A arte é fragmento de body, igual slide: o embrulho (fonte Mulish de disco,
`arte.css`, `skill:` resolvido) é deste script. Assim a mesma arte renderiza em
1920 para a imagem e em 2560 para o vídeo, sem reescrever medida nenhuma — tudo
na arte é `em` sobre a largura.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from renderizar import face_das_fontes, resolver_skill  # noqa: E402

SKILL = Path(__file__).resolve().parent.parent
MIDIA = SKILL / "assets" / "midia"
ARTES = MIDIA / "artes"
ARTE_CSS = MIDIA / "arte.css"

BANNER = (1920, 580)
AVISO = (1080, 1080)
# O vídeo é renderizado grande e reduzido pelo zoompan: assim o avanço de lente
# não amplia pixel, recorta pixel que já existe.
VIDEO_FONTE = (2560, 774)
VIDEO_SAIDA = (1280, 388)

# Catálogo: peça → (arte, medida, saída, vídeo?).
# `video` é (segundos, zoom final). Sem `video`, sai só imagem.
PECAS: dict[str, dict] = {
    "capa-combo-tasty": {"medida": BANNER, "saida": "banner-capa-combo.jpg",
                         "nota": "capa · imagem · TASTY BACON"},
    "capa-chapa-smash": {"medida": BANNER, "saida": "banner-capa-chapa.jpg",
                         "video": {"arquivo": "banner-capa-chapa.mp4",
                                   "segundos": 6, "zoom": 1.12},
                         "nota": "capa · vídeo · SMASH 2.0 na chapa"},
    "vitrine-batata-cheddar": {"medida": BANNER,
                               "saida": "banner-vitrine-batata.jpg",
                               "nota": "vitrine · imagem · batata com cheddar"},
    "vitrine-milk-shake": {"medida": BANNER, "saida": "banner-vitrine-shake.jpg",
                           "video": {"arquivo": "banner-vitrine-shake.mp4",
                                     "segundos": 6, "zoom": 1.1},
                           "nota": "vitrine · vídeo · milk shake"},
    "aviso-feriado": {"medida": AVISO, "saida": "aviso-feriado.png",
                      "nota": "aviso · fechados no feriado"},
    "aviso-horario": {"medida": AVISO, "saida": "aviso-horario.png",
                      "nota": "aviso · novo horário"},
    "aviso-so-delivery": {"medida": AVISO, "saida": "aviso-so-delivery.png",
                          "nota": "aviso · hoje só delivery"},
}


def documento(fragmento: str, largura: int, altura: int) -> str:
    """Embrulha a arte num HTML completo, com fonte de disco e `arte.css`."""
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<style>{face_das_fontes()}</style>
<style>:root{{--largura:{largura}px;--altura:{altura}px;}}</style>
<style>{ARTE_CSS.read_text(encoding="utf-8")}</style>
<style>html,body{{width:{largura}px;height:{altura}px;overflow:hidden;}}</style>
</head>
<body>
{resolver_skill(fragmento)}
</body>
</html>"""


def desenhar(pagina, arte: Path, largura: int, altura: int, destino: Path,
             tmp: Path) -> None:
    html = tmp / f"{arte.stem}-{largura}.html"
    html.write_text(documento(arte.read_text(encoding="utf-8"), largura, altura),
                    encoding="utf-8")
    pagina.set_viewport_size({"width": largura, "height": altura})
    pagina.goto(html.as_uri(), wait_until="load")
    pagina.evaluate("document.fonts.ready")
    pagina.wait_for_timeout(250)
    if destino.suffix == ".jpg":
        # Banner de cardápio é foto: JPG de qualidade alta pesa muito menos que
        # PNG e é o que o restaurante exportaria do celular dele.
        pagina.screenshot(path=str(destino), type="jpeg", quality=92)
    else:
        pagina.screenshot(path=str(destino), type="png")


def filmar(quadro: Path, destino: Path, segundos: int, zoom: float) -> None:
    """Monta o MP4 a partir de um quadro grande, com avanço lento de lente.

    Avanço de lente (o "Ken Burns") em vez de animação de texto: é o que uma
    cozinha consegue fazer com a foto que ela já tem, e é o que o sistema espera
    receber — vídeo curto, horizontal e mudo.
    """
    quadros = segundos * 25
    passo = (zoom - 1) / quadros
    largura, altura = VIDEO_SAIDA
    filtro = (
        f"zoompan=z='min(1+{passo:.6f}*on,{zoom})'"
        f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
        f":d=1:s={largura}x{altura}:fps=25,format=yuv420p"
    )
    comando = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-loop", "1", "-framerate", "25", "-t", str(segundos), "-i", str(quadro),
        "-vf", filtro,
        "-c:v", "libx264", "-preset", "slow", "-crf", "22",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        "-an",  # sem áudio: o cardápio toca mudo de propósito
        str(destino),
    ]
    subprocess.run(comando, check=True)


def fazer(pecas: list[str]) -> None:
    from playwright.sync_api import sync_playwright

    MIDIA.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix="midia-"))
    try:
        with sync_playwright() as p:
            navegador = p.chromium.launch()
            ctx = navegador.new_context(viewport={"width": 1920, "height": 1080},
                                        device_scale_factor=1, locale="pt-BR")
            pagina = ctx.new_page()
            for nome in pecas:
                receita = PECAS[nome]
                arte = ARTES / f"{nome}.html"
                if not arte.is_file():
                    sys.exit(f"ERRO: não achei a arte {arte}")
                largura, altura = receita["medida"]
                destino = MIDIA / receita["saida"]
                desenhar(pagina, arte, largura, altura, destino, tmp)
                print(f"OK  {destino.relative_to(SKILL)}  {largura}x{altura}")

                filme = receita.get("video")
                if filme:
                    grande = tmp / f"{nome}-grande.png"
                    desenhar(pagina, arte, *VIDEO_FONTE, grande, tmp)
                    mp4 = MIDIA / filme["arquivo"]
                    filmar(grande, mp4, filme["segundos"], filme["zoom"])
                    peso = mp4.stat().st_size / 1024
                    print(f"OK  {mp4.relative_to(SKILL)}  "
                          f"{VIDEO_SAIDA[0]}x{VIDEO_SAIDA[1]}  {peso:.0f} KB")
            navegador.close()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--peca", action="append", choices=sorted(PECAS),
                    help="só esta peça (pode repetir)")
    ap.add_argument("--listar", action="store_true", help="mostra o catálogo")
    args = ap.parse_args()

    if args.listar:
        for nome, receita in PECAS.items():
            tipo = "imagem + vídeo" if receita.get("video") else "imagem"
            print(f"{nome:26} {tipo:14} {receita['nota']}")
        return 0

    if not shutil.which("ffmpeg"):
        sys.exit("ERRO: ffmpeg não está instalado (é ele que monta o MP4)")

    fazer(args.peca or list(PECAS))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
