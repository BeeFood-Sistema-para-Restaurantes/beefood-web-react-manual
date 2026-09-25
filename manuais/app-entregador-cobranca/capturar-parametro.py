"""Fotografa o card **Delivery** de Configuração → Parâmetros, onde mora a chave nova.

As dezenove imagens deste manual são do aplicativo, e vieram prontas do dono. Esta é a única
capturada aqui, porque é a única tela **web**: o interruptor que decide se o entregador registra
pagamento.

**Somente leitura.** Parâmetros faz auto-save 500 ms depois do clique, sem botão Salvar — clicar
num interruptor "só para ver" já muda o ambiente do sandbox. Então o script lê `data-state` dos
dois interruptores do card, imprime, e não toca em nenhum.

    python capturar-parametro.py           # imprime o estado e captura
    python capturar-parametro.py --estado  # só imprime, não captura
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "painel-entregador"))

from playwright.sync_api import sync_playwright  # noqa: E402

from beefood import abrir, after_click, limpar_tela  # noqa: E402

PURAS = Path(__file__).resolve().parent / "imagens-puras"
CARD = "20-parametro-entregador-registra-pagamento.png"
CHAVES = ["Pagamento Automático Delivery", "Entregador registra pagamento"]


def forcar_tema_claro(page):
    """Grava o tema claro no `localStorage` do next-themes e recarrega.

    Ler `html.class` logo depois do `goto` corre com a hidratação e às vezes diz `light` numa
    tela que ainda vai virar escura — a lição do #120.
    """
    page.evaluate("() => localStorage.setItem('theme', 'light')")
    page.reload(wait_until="domcontentloaded")
    after_click(page, 7000)
    limpar_tela(page)
    classe = page.locator("html").get_attribute("class") or ""
    if "dark" in classe:
        raise RuntimeError("a tela continuou escura — o print não serve para o manual")


def interruptor_de(page, rotulo: str):
    """Sobe do texto do rótulo até o `[role=switch]` da mesma linha.

    Filtrar `div` por texto cai no elemento errado, porque o card inteiro contém o texto.
    """
    linha = page.locator("div.flex.items-center.justify-between").filter(has_text=rotulo)
    if not linha.count():
        raise RuntimeError(f"não achei a linha de {rotulo!r}")
    return linha.last.locator('[role="switch"]').last


def card_delivery(page):
    return page.locator("div.rounded-lg.border, div[class*='rounded-lg'][class*='border']").filter(
        has_text="Configurações de delivery"
    ).last


def main():
    so_estado = "--estado" in sys.argv
    PURAS.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser, ctx, page = abrir(p, "/parametros", claro=True, viewport=(1440, 1000))
        try:
            forcar_tema_claro(page)

            alvo = page.get_by_text("Entregador registra pagamento", exact=True).last
            alvo.scroll_into_view_if_needed()
            after_click(page, 2500)

            print("--- estado atual dos interruptores do card Delivery (sem tocar em nada)")
            for chave in CHAVES:
                sw = interruptor_de(page, chave)
                print(f"  {chave:38s} {sw.get_attribute('data-state')}")

            if so_estado:
                return

            card = card_delivery(page)
            caixa = card.bounding_box()
            if not caixa:
                raise RuntimeError("o card Delivery não tem caixa — a tela não terminou de montar")
            folga = 14
            page.screenshot(
                path=str(PURAS / CARD),
                clip={
                    "x": caixa["x"] - folga,
                    "y": caixa["y"] - folga,
                    "width": caixa["width"] + folga * 2,
                    "height": caixa["height"] + folga * 2,
                },
            )
            print("PURA", CARD)
        finally:
            ctx.close()
            browser.close()


if __name__ == "__main__":
    main()
