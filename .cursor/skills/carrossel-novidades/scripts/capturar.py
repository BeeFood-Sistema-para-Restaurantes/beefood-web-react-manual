#!/usr/bin/env python3
"""Captura as telas que vão para dentro do carrossel.

Não reinventa a captura: aplica as regras que a `MEMORIA-GERAL.md` já provou nos
manuais (seções 3, 5 e 6) — espera o spinner sumir e **mais 5 segundos**, tema
claro, banner promocional fechado, widget de suporte escondido, pesquisa de NPS
dispensada com filtro pelo título (fechar por texto derruba o modal que você quer
fotografar). Leia aquelas seções antes de mexer aqui.

Diferença em relação ao manual: aqui o print não recebe seta nem número. Ele vai
entrar dentro de uma moldura de celular ou de navegador no slide, e seta em
miniatura de carrossel só suja a imagem. Anotação é trabalho do `annotate.py` do
manual.

Uso como CLI:
    python capturar.py <slug> --rota /cardapio --nome 02-cadastro
    python capturar.py <slug> --rota /cardapio-digital --dispositivo celular
    python capturar.py <slug> --url https://beefood.app/novidades --nome 01-pagina --publico
    python capturar.py <slug> --rota /pdv --nome 03-pdv --recorte 0.1,0.2,0.9,0.7

Uso como módulo, quando a tela exige cliques:
    import sys; sys.path.append(".cursor/skills/carrossel-novidades/scripts")
    from capturar import sessao, esperar, limpar

    with sessao() as pagina:
        pagina.goto("https://beefood.app/cardapio"); esperar(pagina)
        pagina.click("text=Produtos"); esperar(pagina)
        limpar(pagina)
        pagina.screenshot(path="carrosseis/<slug>/imagens-puras/02-produtos.png",
                          type="png")

Cupom impresso é caso especial: ele nasce dentro de um iframe que vai para a
impressora, então não dá para fotografar a tela. Use `ganchar_cupom` antes do
clique e `salvar_cupom` depois.

A saída é sempre `carrosseis/<slug>/imagens-puras/`. Print é matéria-prima:
o que o slide referencia é este arquivo, sem edição.
"""

from __future__ import annotations

import argparse
import contextlib
import os
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
CARROSSEIS = RAIZ / "carrosseis"
ESTADO = Path(os.environ.get("BEEFOOD_ESTADO", "/tmp/beefood-estado.json"))

BASE = "https://beefood.app"
# Conta sandbox dos manuais (MEMORIA-GERAL.md, seção 5). São credenciais
# descartáveis de uma empresa de testes; o dono já decidiu que podem ficar
# versionadas. Sobrescreva por variável de ambiente se precisar de outra conta.
LOGIN = os.environ.get("BEEFOOD_LOGIN", "contato@beefood.com.br")
SENHA = os.environ.get("BEEFOOD_SENHA", "1q2w3e4r")

# device_scale_factor alto para o print continuar legível depois de entrar
# reduzido na moldura do slide.
DISPOSITIVOS = {
    "painel": {"viewport": {"width": 1440, "height": 900}, "device_scale_factor": 2},
    "celular": {"viewport": {"width": 390, "height": 844}, "device_scale_factor": 3,
                "is_mobile": True, "has_touch": True},
}

OCUPADO = ("Carregando...", "Atualizando...", "Calculando")
ESPERA_FINAL = 5000


def esperar(pagina, espera_final: int = ESPERA_FINAL) -> None:
    """Espera o spinner sumir e só então conta 5 segundos.

    Regra permanente dos manuais, não é atalho: print cedo demais sai com painel
    vazio ou com "Atualizando..." no meio da tela.
    """
    for _ in range(30):
        ocupado = any(pagina.locator(f"text={t}").count() for t in OCUPADO)
        if not ocupado:
            break
        pagina.wait_for_timeout(1000)
    pagina.wait_for_timeout(espera_final)


def limpar(pagina) -> None:
    """Tira da frente o que não é a funcionalidade: banner, widget e NPS."""
    with contextlib.suppress(Exception):
        pagina.add_style_tag(content="div.fixed.bottom-6{display:none !important}")

    with contextlib.suppress(Exception):
        botao = pagina.locator('button[aria-label="Dispensar"]')
        if botao.count():
            botao.first.click()
            pagina.wait_for_timeout(600)

    # A pesquisa de NPS usa o MESMO texto de botão de vários modais do sistema.
    # Filtrar pelo título é obrigatório: sem isso a limpeza fecha o modal que
    # está sendo fotografado (quebrou duas rodadas de captura no manual #75).
    for _ in range(2):
        with contextlib.suppress(Exception):
            nps = pagina.locator('[role="dialog"]').filter(
                has_text="Como está sendo sua experiência")
            if not nps.count():
                break
            nps.first.locator('button:has-text("FECHAR")').first.click()
            pagina.wait_for_timeout(600)


@contextlib.contextmanager
def sessao(dispositivo: str = "painel", publico: bool = False):
    """Abre o Chromium já logado (ou anônimo, com `publico=True`).

    O `storage_state` é reaproveitado entre execuções porque o login leva ~12 s.
    Cuidado herdado dos manuais: estado salvo congela o `config_cache` do front —
    se você mexeu em permissão, apague o arquivo e logue de novo.
    """
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        # LANG no processo é o que faz campo de hora e data sair em 24 h.
        navegador = p.chromium.launch(
            env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"})
        opcoes = dict(DISPOSITIVOS[dispositivo],
                      locale="pt-BR", timezone_id="America/Sao_Paulo")

        if publico:
            ctx = navegador.new_context(**opcoes)
        else:
            if not ESTADO.is_file():
                _logar(navegador, opcoes)
            ctx = navegador.new_context(storage_state=str(ESTADO), **opcoes)

        pagina = ctx.new_page()
        try:
            yield pagina
        finally:
            navegador.close()


def _logar(navegador, opcoes: dict) -> None:
    ctx = navegador.new_context(**opcoes)
    pagina = ctx.new_page()
    pagina.goto(f"{BASE}/login", wait_until="domcontentloaded", timeout=90000)
    pagina.wait_for_timeout(4000)
    # Desde 2026-08 a tela tem um campo só para e-mail ou WhatsApp.
    pagina.fill("input#emailOrWhatsapp", LOGIN)
    pagina.fill("input#password", SENHA)
    pagina.click("button:has-text('ENTRAR')")
    pagina.wait_for_timeout(12000)
    if "/login" in pagina.url:
        raise SystemExit("ERRO: o login não passou — confira BEEFOOD_LOGIN/BEEFOOD_SENHA")
    ctx.storage_state(path=str(ESTADO))
    print(f"--> logado como {LOGIN}; sessão guardada em {ESTADO}")
    ctx.close()


def ganchar_cupom(pagina) -> None:
    """Prepara a página para interceptar o cupom antes de ele ir para a impressora.

    O sistema monta o cupom num iframe `beefood-print-frame` e chama `print()`
    nele. Em Chromium headless o diálogo de impressão trava a página e o HTML
    some junto. O truque é o mesmo do manual #99: observar o DOM, copiar o
    documento do iframe assim que ele tem conteúdo e neutralizar o `print()`.

    Chame antes do clique no botão de imprimir; depois, `salvar_cupom`.
    """
    pagina.evaluate(
        """() => {
          window.__cupomHTML = null;
          const pegar = () => {
            const f = document.getElementById('beefood-print-frame');
            if (!f) return;
            try {
              const doc = f.contentDocument;
              if (doc && doc.body && (doc.body.innerText || '').trim().length > 20) {
                window.__cupomHTML = doc.documentElement.outerHTML;
                if (f.contentWindow) f.contentWindow.print = () => {};
              }
            } catch (e) {}
          };
          new MutationObserver(pegar).observe(document.documentElement,
                                              {childList: true, subtree: true});
          setInterval(pegar, 40);
        }"""
    )


def salvar_cupom(pagina, destino: Path, largura: int = 600) -> str:
    """Fotografa o cupom interceptado por `ganchar_cupom` e devolve o texto dele.

    A bobina é estreita e alta: renderiza numa aba própria com `full_page`, então
    a imagem sai na altura do cupom e não na do viewport. O texto voltar é o que
    permite conferir no script se o destaque saiu nos itens certos.
    """
    html = None
    for _ in range(80):
        html = pagina.evaluate("() => window.__cupomHTML")
        if html:
            break
        pagina.wait_for_timeout(250)
    if not html:
        raise SystemExit("ERRO: o cupom não apareceu — o gancho foi instalado antes do clique?")

    aba = pagina.context.new_page()
    aba.set_viewport_size({"width": largura, "height": 1100})
    aba.set_content(html, wait_until="domcontentloaded")
    aba.wait_for_timeout(1500)
    destino.parent.mkdir(parents=True, exist_ok=True)
    aba.screenshot(path=str(destino), type="png", full_page=True)
    texto = aba.inner_text("body")
    aba.close()
    return texto


def recorte_em_px(recorte: str, largura: int, altura: int) -> dict:
    """`--recorte` vem em frações 0..1, como as coordenadas do annotate.py."""
    try:
        x0, y0, x1, y1 = (float(v) for v in recorte.split(","))
    except ValueError:
        raise SystemExit("ERRO: --recorte espera x0,y0,x1,y1 em frações (0..1)")
    return {"x": round(x0 * largura), "y": round(y0 * altura),
            "width": round((x1 - x0) * largura), "height": round((y1 - y0) * altura)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", help="pasta do carrossel em carrosseis/")
    ap.add_argument("--rota", help="rota do painel, ex.: /cardapio")
    ap.add_argument("--url", help="URL completa (usar com --publico)")
    ap.add_argument("--nome", help="nome do arquivo sem extensão")
    ap.add_argument("--dispositivo", default="painel", choices=list(DISPOSITIVOS))
    ap.add_argument("--publico", action="store_true",
                    help="não loga (página pública, cardápio, novidades)")
    ap.add_argument("--recorte", help="x0,y0,x1,y1 em frações de 0 a 1")
    ap.add_argument("--espera", type=int, default=ESPERA_FINAL,
                    help="ms depois do spinner (14000 no detalhe da venda)")
    args = ap.parse_args()

    if not args.rota and not args.url:
        sys.exit("ERRO: informe --rota ou --url")

    url = args.url or f"{BASE}{args.rota}"
    nome = args.nome or (args.rota or "captura").strip("/").replace("/", "-") or "home"
    destino = CARROSSEIS / args.slug / "imagens-puras"
    destino.mkdir(parents=True, exist_ok=True)
    arquivo = destino / f"{nome}.png"

    with sessao(args.dispositivo, args.publico) as pagina:
        pagina.goto(url, wait_until="domcontentloaded", timeout=90000)
        esperar(pagina, args.espera)
        limpar(pagina)
        opcoes = {"path": str(arquivo), "type": "png"}
        if args.recorte:
            v = DISPOSITIVOS[args.dispositivo]["viewport"]
            opcoes["clip"] = recorte_em_px(args.recorte, v["width"], v["height"])
        pagina.screenshot(**opcoes)

    from PIL import Image
    with Image.open(arquivo) as img:
        print(f"OK  {arquivo.relative_to(RAIZ)}  {img.width}x{img.height}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
