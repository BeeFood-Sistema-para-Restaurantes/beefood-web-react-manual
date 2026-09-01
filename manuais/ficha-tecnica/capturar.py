"""Captura #72 Ficha Técnica — hamburgueria (sandbox BeeFood3).

Rodar na pasta do manual:
  python capturar.py             # tudo, na ordem
  python capturar.py insumos     # só a parte de insumo (01 a 03)
  python capturar.py ficha       # ficha do One Burger (04 a 06)
  python capturar.py outras      # adicionais e porção (07 a 09)
  python capturar.py estoque     # coluna Ficha Técnica (10)
  python capturar.py pdv         # venda no PDV (11)
  python capturar.py mov         # movimentações (12)
  python capturar.py editar      # editar/remover linha (13 e 14)
  python capturar.py receita     # insumo vindo de receita (15)

Regra permanente do projeto: depois de cada clique, esperar o spinner sumir e
só então contar 5 segundos antes do print.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

DIR = Path(__file__).resolve().parent
PURA = DIR / "imagens-puras"
PURA.mkdir(exist_ok=True)
STATE = Path("/tmp/beefood3-storage.json")

LOGIN_EMAIL = "contato@beefood.com.br"
LOGIN_SENHA = "1q2w3e4r"
WAIT = 5000

ONE_BURGER = "One Burger"


def after_click(page, extra_ms: int = WAIT):
    for _ in range(30):
        busy = (
            page.locator("text=Carregando...").count()
            or page.locator("text=Atualizando...").count()
            or page.locator("text=Calculando").count()
        )
        if not busy:
            break
        page.wait_for_timeout(1000)
    page.wait_for_timeout(extra_ms)


def limpar_tela(page):
    page.add_style_tag(content="div.fixed.bottom-6 { display:none !important }")
    for sel in ('button[aria-label="Dispensar"]', 'button[aria-label="Fechar"]'):
        b = page.locator(sel)
        if b.count():
            try:
                b.first.click(timeout=1200)
                page.wait_for_timeout(300)
            except Exception:
                pass


def tema_claro(page):
    cls = page.locator("html").get_attribute("class") or ""
    if "dark" in cls:
        alvo = page.locator('span.sr-only:has-text("Alterar tema")')
        if alvo.count():
            alvo.first.locator("xpath=ancestor::button").first.click()
            page.wait_for_timeout(800)


def login(page):
    page.goto("https://beefood.app/login", wait_until="domcontentloaded")
    after_click(page, 2500)
    if "login" in page.url.lower():
        page.fill("input#emailOrWhatsapp", LOGIN_EMAIL)
        page.fill("input#password", LOGIN_SENHA)
        page.locator("button", has_text="ENTRAR").first.click()
        after_click(page, 9000)


def tirar(page, nome: str):
    limpar_tela(page)
    page.screenshot(path=str(PURA / nome), type="png")
    print("   ->", nome)


def abrir_produto(page, nome: str, setor: str | None = None, aba: str | None = None,
                  marcador: str | None = None):
    """Abre o modal de um produto do Cardápio e, se pedido, troca de aba.

    A base do sandbox tem produtos com nome repetido (dois "One Burger", duas
    "Batata frita"). `marcador` é um texto que só existe no item certo — o
    ciclo abre um por um até encontrar.
    """
    page.goto("https://beefood.app/cardapio?tab=produtos", wait_until="domcontentloaded")
    after_click(page, 6000)
    limpar_tela(page)
    if setor:
        page.get_by_text(setor, exact=True).first.click()
        after_click(page, 4000)

    cartoes = page.get_by_text(nome, exact=True)
    for i in range(cartoes.count()):
        cartoes.nth(i).click()
        after_click(page, 6000)
        if aba:
            page.locator(f'button:has-text("{aba}")').first.click()
            after_click(page, 5000)
        if not marcador or marcador in page.locator('div[role="dialog"]').last.inner_text():
            return
        print(f"   (card {i} não é o certo, tentando o próximo)")
        fechar_modal(page)
    raise RuntimeError(f"não achei {nome} com o marcador {marcador!r}")


def abrir_complemento(page, nome: str, aba: str | None = None):
    page.goto("https://beefood.app/cardapio?tab=complementos", wait_until="domcontentloaded")
    after_click(page, 6000)
    limpar_tela(page)
    page.get_by_text(nome, exact=True).first.click()
    after_click(page, 6000)
    if aba:
        page.locator(f'button:has-text("{aba}")').first.click()
        after_click(page, 5000)


def fechar_modal(page):
    page.keyboard.press("Escape")
    page.wait_for_timeout(1500)


# ---------------------------------------------------------------- etapas


def cap_insumos(page):
    """01 lista de insumos · 02 cadastro do Alface · 03 aba Estoque do insumo."""
    page.goto("https://beefood.app/meu-estoque?tab=insumos", wait_until="domcontentloaded")
    after_click(page, 6000)
    tirar(page, "01-insumos-lista.png")

    page.locator('button:has-text("Insumo")').filter(has_not_text="Insumos").first.click()
    after_click(page, 4000)
    dlg = page.locator('div[role="dialog"]').last
    dlg.locator('input[placeholder="Nome do insumo"]').fill("Alface")
    page.wait_for_timeout(400)
    dlg.locator('input[placeholder="R$ 0,00"]').first.fill("8,00")
    page.wait_for_timeout(400)
    # Unidade
    dlg.locator('button[role="combobox"]').first.click()
    page.wait_for_timeout(800)
    page.get_by_text("KG - Quilograma", exact=True).first.click()
    after_click(page, 2500)
    tirar(page, "02-insumo-cadastro.png")

    dlg.locator('button:has-text("Estoque")').first.click()
    after_click(page, 3000)
    dlg.locator('button[role="switch"]').first.click()  # Controlar Estoque
    page.wait_for_timeout(1200)
    minimo = dlg.locator('input[placeholder="0"]').first
    minimo.fill("0.5")
    page.wait_for_timeout(800)
    tirar(page, "03-insumo-estoque.png")
    dlg.locator('button:has-text("SALVAR E SAIR (F2)")').first.click()
    after_click(page, 5000)


def cap_ficha(page):
    """04 adicionar insumo · 05 ficha completa · 06 custos na aba Produto."""
    abrir_produto(page, ONE_BURGER, "Burgers Avulsos (Só O Lanche)", "Ficha Técnica",
                  marcador="Blend bovino")
    dlg = page.locator('div[role="dialog"]').last

    dlg.locator('button:has-text("Buscar insumo...")').first.click()
    page.wait_for_timeout(1200)
    page.locator('input[placeholder="Digite para buscar..."]').fill("Alface")
    page.wait_for_timeout(1500)
    page.get_by_text("Alface", exact=True).last.click()
    page.wait_for_timeout(1200)
    dlg.locator('input[placeholder="0,0000"]').fill("0,01")
    page.wait_for_timeout(800)
    tirar(page, "04-ficha-adicionar.png")

    dlg.locator('button:has-text("Adicionar")').first.click()
    after_click(page, 5000)
    # depois de adicionar, o campo de busca reabre sozinho e tapa a tabela
    page.keyboard.press("Escape")
    page.wait_for_timeout(1500)
    tirar(page, "05-ficha-completa.png")

    page.locator('div[role="dialog"] button:has-text("Produto")').first.click()
    after_click(page, 4000)
    tirar(page, "06-produto-custos.png")


def cap_outras(page):
    """07 ficha do adicional Carne 100g · 08 Bacon · 09 porção Batata frita."""
    abrir_complemento(page, "Carne 100g", "Ficha Técnica")
    tirar(page, "07-ficha-adicional-carne.png")
    fechar_modal(page)

    abrir_complemento(page, "Bacon", "Ficha Técnica")
    tirar(page, "08-ficha-adicional-bacon.png")
    fechar_modal(page)

    abrir_produto(page, "Batata frita", "Acompanhamentos", "Ficha Técnica",
                  marcador="Batata congelada")
    tirar(page, "09-ficha-porcao.png")


def cap_estoque(page):
    """10 coluna Ficha Técnica na lista de produtos do estoque."""
    page.goto("https://beefood.app/meu-estoque?tab=produtos", wait_until="domcontentloaded")
    after_click(page, 6000)
    campo = page.locator('input[placeholder*="Buscar"]')
    if campo.count():
        campo.first.fill("One Burger")
        after_click(page, 3000)
    tirar(page, "10-estoque-coluna-ficha.png")


def cap_pdv(page):
    """11 One Burger com dois adicionais de carne no PDV."""
    page.goto("https://beefood.app/pdv", wait_until="domcontentloaded")
    after_click(page, 7000)
    limpar_tela(page)
    page.fill('input[placeholder="Digite algo para buscar..."]', ONE_BURGER)
    after_click(page, 3000)
    alvo = None
    for c in page.locator('div[class*="cursor-pointer"]').all():
        t = (c.inner_text() or "").strip()
        if t.startswith("COMBO") and ONE_BURGER in t and "Combo " not in t:
            alvo = c
            break
    alvo.click()
    after_click(page, 4000)
    dlg = page.locator('div[role="dialog"]').last
    linha = dlg.locator('div:has-text("Carne 100g")').last
    for _ in range(2):
        linha.click()
        page.wait_for_timeout(1200)
    # o modal rola sozinho ao selecionar opção: volta ao topo antes do print
    dlg.evaluate("el => el.querySelectorAll('*').forEach(x => x.scrollTop = 0)")
    page.wait_for_timeout(1500)
    tirar(page, "11-pdv-dois-adicionais.png")

    dlg.locator('button:has-text("Adicionar ao carrinho")').first.click()
    after_click(page, 4000)
    page.locator('button:has-text("Receber (F3)")').first.click()
    after_click(page, 6000)
    page.locator('button:has-text("Dinheiro")').first.click()
    after_click(page, 3000)
    page.locator('button:has-text("CONFIRMAR (ENTER/F1)")').first.click()
    after_click(page, 8000)
    print("   venda registrada")


def cap_mov(page):
    """12 movimentações geradas pela venda."""
    page.goto("https://beefood.app/movimentacoes", wait_until="domcontentloaded")
    after_click(page, 6000)
    limpar_tela(page)
    tirar(page, "12-movimentacoes-venda.png")


def cap_editar(page):
    """13 editar quantidade na linha · 14 diálogo de remoção."""
    abrir_produto(page, ONE_BURGER, "Burgers Avulsos (Só O Lanche)", "Ficha Técnica",
                  marcador="Blend bovino")
    dlg = page.locator('div[role="dialog"]').last
    linhas = dlg.locator("tbody tr")
    alvo = None
    for i in range(linhas.count()):
        if "Tomate" in linhas.nth(i).inner_text():
            alvo = linhas.nth(i)
            break
    alvo.locator("button").first.click()  # lápis
    page.wait_for_timeout(1500)
    tirar(page, "13-ficha-editar-linha.png")
    # ESC fecharia o modal inteiro: o X da própria linha é quem cancela a edição
    alvo.locator("button").last.click()
    page.wait_for_timeout(1500)

    alvo.locator("button").last.click()  # lixeira
    after_click(page, 2500)
    tirar(page, "14-ficha-remover.png")
    botao_nao = page.locator('button:has-text("Não")')
    if botao_nao.count():
        botao_nao.first.click()
    page.wait_for_timeout(1200)


def cap_receita(page):
    """15 insumo cujo custo vem de uma receita."""
    page.goto("https://beefood.app/meu-estoque?tab=insumos", wait_until="domcontentloaded")
    after_click(page, 6000)
    page.get_by_text("Maionese da casa (sache)", exact=True).first.click()
    after_click(page, 5000)
    tirar(page, "15-insumo-receita.png")


ETAPAS = {
    "insumos": cap_insumos,
    "ficha": cap_ficha,
    "outras": cap_outras,
    "estoque": cap_estoque,
    "pdv": cap_pdv,
    "mov": cap_mov,
    "editar": cap_editar,
    "receita": cap_receita,
}


def main():
    pedidos = sys.argv[1:] or list(ETAPAS)
    with sync_playwright() as p:
        browser = p.chromium.launch(
            env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"}
        )
        args = dict(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=1.5,
            locale="pt-BR",
            timezone_id="America/Sao_Paulo",
        )
        if STATE.exists():
            args["storage_state"] = str(STATE)
        ctx = browser.new_context(**args)
        page = ctx.new_page()
        login(page)
        tema_claro(page)
        for nome in pedidos:
            print("==", nome)
            ETAPAS[nome](page)
        ctx.storage_state(path=str(STATE))
        browser.close()


if __name__ == "__main__":
    main()
