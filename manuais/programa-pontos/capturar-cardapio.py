"""Captura as telas do cardápio digital para o #126 — o que o cliente vê dos pontos.

Somente **leitura** do lado do restaurante: o roteiro monta uma sacola, resgata uma
recompensa e para antes de fechar o pedido. Nada é gravado na sandbox — o resgate só
consome pontos quando a venda nasce, e a venda não nasce aqui. O saldo que as imagens
mostram foi creditado pelo `cenario.py`.

Padrão de celular da casa: viewport **390x844** em DPR 2 (pura 780x1688), `is_mobile`,
`has_touch`, `locale="pt-BR"`, `timezone_id="America/Sao_Paulo"` e `LANG=pt_BR.UTF-8` no
processo — sem o `LANG` no ambiente do Chromium, campo de data e hora sai em AM/PM.

Quatro armadilhas deste cardápio, todas pagas em tentativa:

* **O botão do rodapé é `.v-bottom-navigation .v-btn`.** `get_by_text("Perfil")` acha o
  rótulo, mas o clique não navega: o Vuetify põe o texto dentro do botão, e é o botão que
  escuta. O mesmo vale para `CONTINUAR`, que fica dentro de `.v-btn`.
* **Perfil deslogado abre a tela de login, não o menu do perfil.** Depois de entrar, o
  cardápio volta para a home — é preciso tocar em *Perfil* **de novo** para ver o menu com
  *Programa de pontos*.
* **O telefone de teste entra sem código.** O servidor responde `motivo !== "O"` e o
  cliente pula a etapa do WhatsApp. É o que torna a captura do lado do cliente possível aqui.
* **A modalidade trava o avanço.** *Receber no seu endereço* exige endereço e abre o mapa;
  o caminho curto é **Retirar no estabelecimento**, dentro da sacola. O card
  *Programa de Pontos* só aparece **depois** dessa escolha.

E a que mais importa para o manual: a **faixa** e o **card do carrinho** só existem quando
`pontosAtivo` é verdadeiro e o cardápio **não** é presencial (`?tipo=p`). O banner do
computador, além disso, mora numa coluna que só existe em tela larga.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

SRC = Path(__file__).resolve().parent / "imagens-puras"
SRC.mkdir(exist_ok=True)

URL = "https://menu.beefood.com.br/beefood3"
TELEFONE = "15999998888"          # cliente Teste Manual, versionado na seção 5 da memória
PRODUTO = "/chicken-deluxe/"      # produto simples: nenhum grupo de opções obrigatório
RECOMPENSA = "R$ 10,00 de desconto"

CELULAR = {"width": 390, "height": 844}
COMPUTADOR = {"width": 1440, "height": 900}


def esperar(page, ms: int):
    page.wait_for_timeout(ms)


def tirar(page, nome: str, alvo=None):
    (alvo or page).screenshot(path=str(SRC / nome))
    print("PURA", nome)


def fechar_banner_cupom(page):
    """A faixa verde de cupons cobre o topo e não tem a ver com pontos."""
    x = page.locator("i.mdi-close")
    if x.count():
        x.first.click()
        esperar(page, 1500)


def entrar(page):
    page.locator(".v-bottom-navigation .v-btn").filter(has_text="Perfil").first.click()
    esperar(page, 5000)
    page.locator("input[type=tel]").first.fill(TELEFONE)
    page.locator(".v-btn").filter(has_text="CONTINUAR").first.click()
    esperar(page, 10000)


def abrir_navegador(p, viewport):
    b = p.chromium.launch(args=["--no-sandbox"],
                          env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"})
    ctx = b.new_context(viewport=viewport,
                        device_scale_factor=2 if viewport is CELULAR else 1.5,
                        is_mobile=viewport is CELULAR, has_touch=viewport is CELULAR,
                        locale="pt-BR", timezone_id="America/Sao_Paulo")
    return b, ctx, ctx.new_page()


def celular(p):
    b, ctx, page = abrir_navegador(p, CELULAR)
    try:
        page.goto(URL, wait_until="domcontentloaded")
        esperar(page, 11000)
        fechar_banner_cupom(page)

        # 11 — a porta de entrada do cliente: a faixa amarela e o selo de presente no produto
        tirar(page, "06-cardapio-faixa-pontos.png")

        entrar(page)

        # 12 — o menu do perfil, com o atalho do programa
        page.locator(".v-bottom-navigation .v-btn").filter(has_text="Perfil").first.click()
        esperar(page, 6000)
        tirar(page, "07-cardapio-perfil-programa-pontos.png")

        # 13 — o saldo e o extrato do cliente
        page.get_by_text("Programa de pontos", exact=False).first.click()
        esperar(page, 7000)
        tirar(page, "08-cardapio-meus-pontos.png")

        # 14 — a vitrine de recompensas, com o que falta para as que ainda não dão
        page.get_by_text("Ver o que você pode ganhar", exact=False).first.click()
        esperar(page, 6000)
        tirar(page, "09-cardapio-recompensas.png")
        page.keyboard.press("Escape")
        esperar(page, 2500)

        # sacola: um produto simples, retirada no balcão
        page.goto(URL + PRODUTO, wait_until="domcontentloaded")
        esperar(page, 8000)
        page.locator(".v-btn").filter(has_text="Adicionar").last.click()
        esperar(page, 7000)
        page.get_by_text("Ver sacola", exact=False).first.click()
        esperar(page, 9000)
        page.locator(".v-btn").filter(has_text="Continuar").last.click()
        esperar(page, 8000)
        page.get_by_text("Retirar no estabelecimento", exact=False).first.click()
        esperar(page, 4000)
        page.locator(".v-btn").filter(has_text="Continuar").last.click()
        esperar(page, 10000)

        # 15 — o cliente troca pontos por recompensa, dentro da sacola
        page.get_by_text("Programa de Pontos", exact=False).first.scroll_into_view_if_needed()
        esperar(page, 2500)
        tirar(page, "10-cardapio-trocar-pontos.png")

        # 16 — a recompensa aplicada: o desconto entra no total
        linha = page.get_by_text(RECOMPENSA, exact=False).first.locator(
            "xpath=ancestor::*[.//button or .//*[contains(@class,'v-btn')]][1]"
        )
        linha.locator(".v-btn, button").filter(has_text="RESGATAR").first.click()
        esperar(page, 8000)
        tirar(page, "11-cardapio-resgate-aplicado.png")
        print("RESUMO:", page.inner_text("body")[:40].replace("\n", " "))
        print("ATENÇÃO: o pedido NÃO foi fechado — o resgate só consome pontos na venda.")
    finally:
        ctx.close()
        b.close()


def computador(p):
    b, ctx, page = abrir_navegador(p, COMPUTADOR)
    try:
        page.goto(URL, wait_until="domcontentloaded")
        esperar(page, 12000)
        fechar_banner_cupom(page)
        banner = page.locator(".banner-pontos")
        print("banner-pontos no computador:", banner.count())
        if not banner.count():
            print("sem banner — nada a capturar")
            return
        banner.first.scroll_into_view_if_needed()
        esperar(page, 2500)
        # O banner mora na coluna da sacola, que só existe em tela larga. A imagem é uma
        # faixa de **largura inteira**: recortar perto do cartão tiraria a referência de
        # onde ele fica, e foi o que aconteceu na primeira tentativa — o nome da loja saía
        # cortado no meio.
        caixa = banner.first.bounding_box()
        page.screenshot(path=str(SRC / "12-banner-pontos-computador.png"), clip={
            "x": 0, "y": max(0, caixa["y"] - 170),
            "width": COMPUTADOR["width"],
            "height": caixa["height"] + 250,
        })
        print("PURA 12-banner-pontos-computador.png")
    finally:
        ctx.close()
        b.close()


def main():
    alvos = sys.argv[1:] or ["celular", "computador"]
    with sync_playwright() as p:
        if "celular" in alvos:
            celular(p)
        if "computador" in alvos:
            computador(p)


if __name__ == "__main__":
    main()
