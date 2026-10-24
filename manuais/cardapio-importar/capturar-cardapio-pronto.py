"""Captura o cardápio depois da importação do iFood — o resultado que o cliente vai conferir.

Idempotente: só abre telas e fotografa. Pode rodar quantas vezes quiser.

São as três telas onde a importação do iFood aparece de verdade:

* **Produtos**, com os setores que vieram da loja e os produtos com foto e preço;
* **Grupo de Opções**, que é onde os complementos do iFood (ponto da carne, adicionais) chegam;
* a ficha de um produto importado, para mostrar o que veio preenchido e o que falta revisar.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "painel-entregador"))

from playwright.sync_api import sync_playwright
from beefood import abrir, after_click, api_get, limpar_tela, sessao

AQUI = Path(__file__).resolve().parent
PURAS = AQUI / "imagens-puras"


def print_tela(page, nome, espera=8000):
    after_click(page, espera)
    limpar_tela(page)
    page.screenshot(path=str(PURAS / nome))
    print("gravado:", nome)


with sync_playwright() as p:
    browser, ctx, page = abrir(p, "/cardapio?tab=produtos", viewport=(1440, 900), escala=1.5)
    s = sessao(page)
    print("qtdProdutos:", api_get(page, f"/api/produto2/cardapio/qtdProdutos/{s['empresaID']}/{s['usuarioID']}"))
    print_tela(page, "06-produtos-importados.png")
    print("setores na tela:", page.locator("body").inner_text()[:400].replace("\n", " | "))

    page.goto("https://beefood.app/cardapio?tab=grupoOpcoes", wait_until="domcontentloaded")
    print_tela(page, "07-grupos-opcoes-importados.png")

    browser.close()
print("fim")
