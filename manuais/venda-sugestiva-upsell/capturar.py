#!/usr/bin/env python3
"""Captura #103 — Venda Sugestiva (UpSell) (produção, sandbox BeeFood3 / 38311).

    python capturar.py                 # todas as etapas do painel
    python capturar.py menu geral      # só algumas
    DRY=1 python capturar.py config    # não grava a configuração

Etapas do painel:
  menu     menu de ações da tela Cardápio (item Venda Sugestiva (UpSell))
  config   janela de escolha aberta pelos três pontinhos do produto (grava!)
  produto  item Venda Sugestiva no menu de três pontinhos do produto
  geral    janela geral (lista de produtos, selos e filtros)
  aba      aba Venda Sugestiva dentro do cadastro do produto
  limite   janela de escolha com 6 itens (aviso de limite)

Regra da MEMORIA-GERAL: depois de cada clique, espera o spinner sair e mais 5 s.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

DIR = Path(__file__).resolve().parent
PURA = DIR / "imagens-puras"
PURA.mkdir(exist_ok=True)
STATE = Path("/tmp/bf3-auth.json")
WAIT = 5000
LOGIN_EMAIL = "contato@beefood.com.br"
LOGIN_SENHA = "1q2w3e4r"
DRY = os.environ.get("DRY") == "1"

# Exemplo do manual: nomes únicos na base (ela tem 21 nomes repetidos)
PRODUTO = "Combo One Burger"
SUGERIDOS = [
    "Anéis de Cebola Empanada",
    "Milk Shake de Morango",
    "Brownie",
    "Pudim - Leite Condensado",
]
PRODUTO_CHEIO = "Combo Chicken Deluxe"  # já vem com 6 configurados


def after_click(page, extra_ms: int = WAIT):
    for _ in range(30):
        ocupado = (
            page.locator("text=Carregando...").count()
            or page.locator("text=Atualizando...").count()
            or page.locator("text=Carregando produtos...").count()
        )
        if not ocupado:
            break
        page.wait_for_timeout(1000)
    page.wait_for_timeout(extra_ms)


def limpar(page):
    page.add_style_tag(content="div.fixed.bottom-6 { display:none !important }")
    nps = page.locator('[role="dialog"]').filter(has_text="Como está sendo sua experiência")
    if nps.count():
        botao = nps.last.get_by_role("button", name="FECHAR")
        if botao.count():
            try:
                botao.click(timeout=1500)
                after_click(page)
            except Exception:
                pass
    dispensar = page.locator('button[aria-label="Dispensar"]')
    if dispensar.count():
        try:
            dispensar.first.click(timeout=1200)
            after_click(page)
        except Exception:
            pass


def tema_claro(page):
    classes = page.locator("html").get_attribute("class") or ""
    if "dark" in classes:
        alvo = page.locator('span.sr-only:has-text("Alterar tema")')
        if alvo.count():
            alvo.first.locator("xpath=ancestor::button").first.click()
            page.wait_for_timeout(800)


def login(page, contexto):
    page.goto("https://beefood.app/", wait_until="domcontentloaded")
    after_click(page)
    if page.locator("input#emailOrWhatsapp").count():
        page.fill("input#emailOrWhatsapp", LOGIN_EMAIL)
        page.fill("input#password", LOGIN_SENHA)
        page.get_by_role("button", name="ENTRAR").click()
        after_click(page, 9000)
        contexto.storage_state(path=str(STATE))
    tema_claro(page)
    limpar(page)


def shot(page, nome: str):
    destino = PURA / nome
    page.screenshot(path=str(destino), type="png")
    print("SHOT", destino.name, destino.stat().st_size)


def caixa(page, rotulo: str, seletor, indice: int = 0):
    """Caixa do elemento já na escala da imagem (device_scale 1.5)."""
    loc = seletor if hasattr(seletor, "nth") else page.locator(seletor)
    if not loc.count():
        print(f"  CAIXA {rotulo}: NÃO ENCONTRADA")
        return
    b = loc.nth(indice).bounding_box()
    if not b:
        print(f"  CAIXA {rotulo}: sem caixa")
        return
    f = 1.5
    print(
        f"  CAIXA {rotulo}: ({round(b['x'] * f)}, {round(b['y'] * f)}, "
        f"{round((b['x'] + b['width']) * f)}, {round((b['y'] + b['height']) * f)})"
    )


def abrir_cardapio(page):
    page.goto("https://beefood.app/cardapio?tab=produtos", wait_until="domcontentloaded")
    after_click(page, 9000)
    limpar(page)


def menu_pagina(page):
    """Abre o menu de ações do topo da página (três pontinhos)."""
    gatilho = page.locator("header, .flex").locator("button").filter(
        has=page.locator("svg.lucide-ellipsis-vertical")
    )
    gatilho.first.click()
    after_click(page, 2500)
    return page.locator('[role="menu"]').last


def abrir_menu_do_produto(page, nome: str):
    """Abre o menu de três pontinhos do card do produto.

    A grade é virtualizada e todos os cards têm o mesmo botão; o jeito estável é
    achar o título e pegar o ⋮ na mesma linha, à direita dele.
    """
    titulo = page.get_by_text(nome, exact=True).first
    titulo.scroll_into_view_if_needed()
    after_click(page, 1500)
    alvo_box = titulo.bounding_box()
    botoes = page.locator("button").filter(has=page.locator("svg.lucide-ellipsis-vertical"))
    melhor, melhor_dist = None, 1e9
    for i in range(botoes.count()):
        b = botoes.nth(i).bounding_box()
        if not b or b["x"] < alvo_box["x"]:
            continue
        dist = abs(b["y"] - alvo_box["y"])
        if dist < melhor_dist:
            melhor, melhor_dist = i, dist
    if melhor is None or melhor_dist > 40:
        raise RuntimeError(f"não achei o ⋮ do card {nome} (dist={melhor_dist})")
    botoes.nth(melhor).click()
    after_click(page, 2500)
    return page.locator('[role="menu"]').last


def dialogo(page, texto: str):
    return page.locator('[role="dialog"]').filter(has_text=texto).last


# ------------------------------------------------------------------ etapas


def cap_menu(page):
    """01 — menu de ações da tela Cardápio com o item Venda Sugestiva (UpSell)."""
    abrir_cardapio(page)
    menu = menu_pagina(page)
    print("MENU:", menu.inner_text().replace("\n", " | "))
    caixa(page, "item venda sugestiva", '[role="menuitem"]:has-text("Venda Sugestiva")')
    caixa(page, "menu inteiro", '[role="menu"]')
    caixa(
        page,
        "botao 3 pontinhos",
        page.locator("button").filter(has=page.locator("svg.lucide-ellipsis-vertical")),
    )
    shot(page, "01-menu-acoes.png")
    page.keyboard.press("Escape")
    page.wait_for_timeout(800)


def cap_produto(page):
    """04 — três pontinhos do produto, com o item Venda Sugestiva."""
    abrir_cardapio(page)
    menu = abrir_menu_do_produto(page, PRODUTO)
    print("MENU PRODUTO:", menu.inner_text().replace("\n", " | "))
    caixa(page, "item venda sugestiva", '[role="menuitem"]:has-text("Venda Sugestiva")')
    caixa(page, "menu do produto", '[role="menu"]')
    shot(page, "04-menu-produto.png")
    page.keyboard.press("Escape")
    page.wait_for_timeout(800)


def cap_config(page):
    """02/03 — janela de escolha: marca os sugeridos e salva."""
    abrir_cardapio(page)
    abrir_menu_do_produto(page, PRODUTO)
    page.locator('[role="menuitem"]:has-text("Venda Sugestiva")').first.click()
    after_click(page, 6000)

    dlg = dialogo(page, "Venda Sugestiva")
    print("titulo:", dlg.locator("h2, [role=heading]").first.inner_text())
    shot(page, "03a-janela-vazia.png")

    for nome in SUGERIDOS:
        linha = dlg.locator("label").filter(has_text=nome).first
        linha.scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        linha.click()
        after_click(page, 1500)
        print("  marcado:", nome)

    # rola a lista de volta ao topo para o print
    dlg.locator("label").first.scroll_into_view_if_needed()
    after_click(page, 2000)
    caixa(page, "faixa selecionados", dlg.locator("text=Selecionados"))
    caixa(page, "contador", dlg.locator("text=/^[0-9]+\\/6$/"))
    caixa(page, "busca", dlg.locator('input[placeholder*="Buscar"]'))
    caixa(page, "filtro setores", dlg.get_by_role("button", name="Todos os setores"))
    caixa(page, "salvar", dlg.get_by_role("button", name="SALVAR (F2)"))
    caixa(page, "cancelar", dlg.get_by_role("button", name="CANCELAR (ESC)"))
    caixa(page, "dialogo", dlg)
    shot(page, "03-janela-escolha.png")

    if DRY:
        print("  DRY: não salvou")
        page.keyboard.press("Escape")
        return
    dlg.get_by_role("button", name="SALVAR (F2)").click()
    after_click(page, 4000)
    print("  salvo. toast:", page.locator("[role=status], .toast").first.inner_text()[:120]
          if page.locator("[role=status], .toast").count() else "(sem toast visível)")
    shot(page, "03b-toast-salvo.png")


def cap_geral(page):
    """02 — janela geral: lista de produtos com selo Configurado e Sugere:."""
    abrir_cardapio(page)
    menu = menu_pagina(page)
    menu.locator('[role="menuitem"]:has-text("Venda Sugestiva")').first.click()
    after_click(page, 9000)
    dlg = dialogo(page, "Venda Sugestiva (UpSell)")
    # espera as fotos das sugestões carregarem
    for _ in range(10):
        if dlg.locator("text=Sugere:").count():
            break
        page.wait_for_timeout(2000)
    after_click(page, 4000)
    print("configurados:", dlg.get_by_role("button", name="Somente configurados").first.inner_text()
          if dlg.get_by_role("button", name="Somente configurados").count() else "?")
    caixa(page, "busca", dlg.locator('input[placeholder*="Buscar"]'))
    caixa(page, "filtro setores", dlg.get_by_role("button", name="Todos os setores"))
    caixa(page, "somente configurados", dlg.get_by_role("button", name="Somente configurados"))
    caixa(page, "linha do produto", dlg.locator("button").filter(has_text=PRODUTO))
    caixa(page, "selo configurado", dlg.locator("text=Configurado"))
    caixa(page, "faixa sugere", dlg.locator("text=Sugere:"))
    caixa(page, "fechar", dlg.get_by_role("button", name="FECHAR (ESC)"))
    caixa(page, "dialogo", dlg)
    shot(page, "02-janela-geral.png")
    page.keyboard.press("Escape")
    page.wait_for_timeout(800)


def cap_aba(page):
    """05 — aba Venda Sugestiva dentro do cadastro do produto."""
    abrir_cardapio(page)
    page.get_by_text(PRODUTO, exact=True).first.scroll_into_view_if_needed()
    after_click(page, 1500)
    page.get_by_text(PRODUTO, exact=True).first.click()
    after_click(page, 8000)
    dlg = dialogo(page, "Venda Sugestiva")
    aba = page.get_by_role("button", name="Venda Sugestiva")
    if not aba.count():
        aba = page.locator('button:has-text("Venda Sugestiva")')
    print("abas:", [t for t in page.locator('[role="tablist"] button, .tabs button').all_inner_texts()][:10])
    aba.last.click()
    after_click(page, 7000)
    dlg = page.locator('[role="dialog"]').last
    caixa(page, "aba venda sugestiva", aba, aba.count() - 1)
    caixa(page, "salvo automaticamente", dlg.locator("text=Salvo automaticamente"))
    caixa(page, "faixa selecionados", dlg.locator("text=Selecionados"))
    caixa(page, "busca", dlg.locator('input[placeholder*="Buscar"]'))
    caixa(page, "dialogo", dlg)
    shot(page, "05-aba-cadastro.png")
    page.keyboard.press("Escape")
    page.wait_for_timeout(1000)
    page.keyboard.press("Escape")


def cap_limite(page):
    """06 — janela de escolha com 6 marcados (aviso de limite)."""
    abrir_cardapio(page)
    abrir_menu_do_produto(page, PRODUTO_CHEIO)
    page.locator('[role="menuitem"]:has-text("Venda Sugestiva")').first.click()
    after_click(page, 7000)
    dlg = dialogo(page, "Venda Sugestiva")
    caixa(page, "aviso limite", dlg.locator("text=/Limite de 6/"))
    caixa(page, "contador", dlg.locator("text=/^6\\/6$/"))
    caixa(page, "dialogo", dlg)
    shot(page, "06-limite.png")
    page.keyboard.press("Escape")
    page.wait_for_timeout(800)


ETAPAS = {
    "menu": cap_menu,
    "config": cap_config,
    "produto": cap_produto,
    "geral": cap_geral,
    "aba": cap_aba,
    "limite": cap_limite,
}


def main():
    pedidas = sys.argv[1:] or list(ETAPAS)
    with sync_playwright() as p:
        nav = p.chromium.launch(env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"})
        ctx = nav.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=1.5,
            locale="pt-BR",
            timezone_id="America/Sao_Paulo",
            storage_state=str(STATE) if STATE.exists() else None,
        )
        page = ctx.new_page()
        login(page, ctx)
        for nome in pedidas:
            fn = ETAPAS.get(nome)
            if not fn:
                print("etapa desconhecida:", nome)
                continue
            print("==", nome)
            try:
                fn(page)
            except Exception as e:
                print("ERRO em", nome, str(e).split("\n")[0][:200])
                shot(page, f"erro-{nome}.png")
        ctx.close()
        nav.close()


if __name__ == "__main__":
    main()
