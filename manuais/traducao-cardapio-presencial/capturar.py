#!/usr/bin/env python3
"""Captura #100 — Tradução do cardápio presencial (sandbox BeeFood3).

  python capturar.py                 # tudo
  python capturar.py setor produto complemento grupo totem
  python capturar.py bebidas         # só limpa a tradução de teste do setor Bebidas

Depois de cada clique: spinner some e só então 5 s (regra da MEMORIA-GERAL).
As bandeiras só aparecem porque a conta tem totem (qtdAA=5) e tablet (qtdTablet=10).
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

# Textos usados no manual (mesmos itens nas 5 capturas)
TRAD = {
    "setor": {"en": "Sides", "es": "Guarniciones"},
    "produto_nome": {"en": "Breaded Onion Rings", "es": "Aros de cebolla empanizados"},
    "produto_desc": {
        "en": "Portion with 8 breaded onion rings",
        "es": "Porción con 8 aros de cebolla empanizados",
    },
    "complemento": {"en": "Green sauce", "es": "Salsa verde"},
    "grupo": {"en": "Choose a sauce", "es": "Elige una salsa"},
}


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


def limpar(page):
    page.add_style_tag(content="div.fixed.bottom-6 { display:none !important }")
    nps = page.locator('[role="dialog"]').filter(has_text="Como está sendo sua experiência")
    if nps.count():
        btn = nps.last.get_by_role("button", name="FECHAR")
        if btn.count():
            try:
                btn.click(timeout=1500)
                after_click(page)
            except Exception:
                pass
    disp = page.locator('button[aria-label="Dispensar"]')
    if disp.count():
        try:
            disp.first.click(timeout=1200)
            after_click(page)
        except Exception:
            pass


def tema_claro(page):
    cls = page.locator("html").get_attribute("class") or ""
    if "dark" in cls:
        alvo = page.locator('span.sr-only:has-text("Alterar tema")')
        if alvo.count():
            alvo.first.locator("xpath=ancestor::button").first.click()
            page.wait_for_timeout(800)


def login(page, context):
    page.goto("https://beefood.app/", wait_until="domcontentloaded")
    after_click(page)
    if page.locator("input#emailOrWhatsapp").count():
        page.fill("input#emailOrWhatsapp", LOGIN_EMAIL)
        page.fill("input#password", LOGIN_SENHA)
        page.get_by_role("button", name="ENTRAR").click()
        after_click(page, 9000)
        context.storage_state(path=str(STATE))
    tema_claro(page)
    limpar(page)


def shot(page, nome: str):
    dest = PURA / nome
    page.screenshot(path=str(dest), type="png")
    print("SHOT", dest.name, dest.stat().st_size)


def bandeira(page, idioma: str):
    """Clica na bandeira do modal aberto. idioma: Português | Inglês | Espanhol."""
    dlg = page.locator('[role="dialog"]').last
    btn = dlg.locator(f'button[aria-label="{idioma}"]')
    if btn.count() == 0:
        raise RuntimeError(f"bandeira {idioma} não encontrada")
    btn.first.scroll_into_view_if_needed()
    btn.first.click()
    page.wait_for_timeout(1200)
    print("bandeira", idioma, "ok")


def salvar_modal(page):
    """DRY=1 fotografa tudo e sai sem gravar (ensaio da MEMORIA-GERAL, seção 7)."""
    if os.environ.get("DRY") == "1":
        print("DRY: não salvou")
        fechar_modal(page)
        return
    dlg = page.locator('[role="dialog"]').last
    btn = dlg.locator('button:has-text("SALVAR E SAIR")')
    btn.first.click()
    after_click(page, 8000)


def fechar_modal(page):
    page.keyboard.press("Escape")
    after_click(page, 2000)
    if page.locator('[role="dialog"]').count():
        page.keyboard.press("Escape")
        after_click(page, 1500)


def abrir_setor(page, titulo: str):
    page.goto("https://beefood.app/cardapio?tab=produtos", wait_until="domcontentloaded")
    after_click(page, 7000)
    limpar(page)
    linha = page.locator("div").filter(has_text=titulo).last
    # a linha do setor tem o botão ⋮ (MoreVertical) → Editar
    alvo = None
    for cand in page.locator('div[class*="group"]').all():
        txt = (cand.inner_text() or "").strip()
        if txt.startswith(titulo) and cand.locator("svg.lucide-ellipsis-vertical").count():
            alvo = cand
            break
    if alvo is None:
        print("linha fallback:", (linha.inner_text() or "")[:120])
        alvo = linha
    alvo.locator("button").filter(has=page.locator("svg.lucide-ellipsis-vertical")).first.click()
    after_click(page, 1500)
    page.get_by_role("menuitem", name="Editar").first.click()
    after_click(page, 6000)
    limpar(page)


def cap_setor(page):
    abrir_setor(page, "Acompanhamentos")
    campo = page.locator("#titulo")
    campo.first.scroll_into_view_if_needed()
    page.wait_for_timeout(600)
    print("titulo pt:", campo.first.input_value())
    shot(page, "01-setor-bandeiras.png")

    bandeira(page, "Inglês")
    campo.first.fill(TRAD["setor"]["en"])
    page.wait_for_timeout(1200)
    shot(page, "02-setor-ingles.png")

    bandeira(page, "Espanhol")
    campo.first.fill(TRAD["setor"]["es"])
    page.wait_for_timeout(800)
    salvar_modal(page)
    print("setor salvo")


def cap_bebidas(page):
    """Troca a tradução de teste do setor Bebidas (Drinksx/Drinkles) por texto limpo."""
    abrir_setor(page, "Bebidas")
    campo = page.locator("#titulo")
    bandeira(page, "Inglês")
    campo.first.fill("Drinks")
    page.wait_for_timeout(600)
    bandeira(page, "Espanhol")
    campo.first.fill("Bebidas")
    page.wait_for_timeout(600)
    salvar_modal(page)
    print("bebidas ajustado")


def abrir_item(page, aba: str, nome: str, setor: str | None = None):
    """A aba do cardápio não tem campo de busca; a lista é virtualizada.
    Em Produtos, filtrar pelo setor deixa o item visível."""
    page.goto(f"https://beefood.app/cardapio?tab={aba}", wait_until="domcontentloaded")
    after_click(page, 8000)
    limpar(page)
    if setor:
        page.get_by_text(setor, exact=True).first.click()
        after_click(page, 5000)
    alvo = page.get_by_text(nome, exact=True)
    print("itens com", nome, ":", alvo.count())
    alvo.first.scroll_into_view_if_needed()
    alvo.first.click()
    after_click(page, 9000)
    limpar(page)


def cap_produto(page):
    abrir_item(page, "produtos", "Anéis de Cebola Empanada", setor="Acompanhamentos")
    nome = page.locator("#nome")
    desc = page.locator("#descricao")
    print("nome pt:", nome.first.input_value(), "| desc pt:", desc.first.input_value()[:60])

    bandeira(page, "Inglês")
    nome.first.fill(TRAD["produto_nome"]["en"])
    desc.first.fill(TRAD["produto_desc"]["en"])
    page.wait_for_timeout(1200)
    shot(page, "03-produto-ingles.png")

    bandeira(page, "Espanhol")
    nome.first.fill(TRAD["produto_nome"]["es"])
    desc.first.fill(TRAD["produto_desc"]["es"])
    page.wait_for_timeout(800)
    salvar_modal(page)
    print("produto salvo")


def cap_complemento(page):
    abrir_item(page, "complementos", "Molho verde")
    nome = page.locator("#nome")
    print("complemento pt:", nome.first.input_value())
    bandeira(page, "Inglês")
    nome.first.fill(TRAD["complemento"]["en"])
    page.wait_for_timeout(1200)
    shot(page, "04-complemento-ingles.png")
    bandeira(page, "Espanhol")
    nome.first.fill(TRAD["complemento"]["es"])
    page.wait_for_timeout(800)
    salvar_modal(page)
    print("complemento salvo")


def cap_grupo(page):
    abrir_item(page, "grupoOpcoes", "Escolha um molho")
    dlg = page.locator('[role="dialog"]').last
    campo = dlg.locator("#descricao")
    if campo.count() == 0:
        campo = dlg.locator("input").first
    print("grupo pt:", campo.first.input_value())
    bandeira(page, "Inglês")
    campo.first.fill(TRAD["grupo"]["en"])
    page.wait_for_timeout(1200)
    shot(page, "05-grupo-opcoes-ingles.png")
    bandeira(page, "Espanhol")
    campo.first.fill(TRAD["grupo"]["es"])
    page.wait_for_timeout(800)
    salvar_modal(page)
    print("grupo salvo")


def cap_totem(page):
    page.goto("https://beefood.app/aplicativos", wait_until="domcontentloaded")
    after_click(page, 8000)
    limpar(page)
    busca = page.locator('input[placeholder*="Buscar"], input[placeholder*="buscar"]')
    if busca.count():
        busca.first.fill("Totem")
        after_click(page, 3000)
    page.get_by_text("Totem", exact=False).first.click()
    after_click(page, 8000)
    limpar(page)
    dlg = page.locator('[role="dialog"]').last
    print("modal totem:", (dlg.inner_text() or "")[:200].replace("\n", " | "))
    alvo = dlg.get_by_text("Habilitar tradução", exact=True)
    if alvo.count() == 0:
        print("SEM grupo Idiomas. conteudo:", (dlg.inner_text() or "")[:1500])
        return
    alvo.first.evaluate("el => el.scrollIntoView({block:'center'})")
    page.wait_for_timeout(1500)
    box = alvo.first.locator("xpath=ancestor::label").locator('[role="checkbox"]')
    estado = box.first.get_attribute("data-state")
    print("habilitar traducao:", estado)
    if estado != "checked" and os.environ.get("DRY") != "1":
        alvo.first.click()
        after_click(page, 4000)
        print("agora:", box.first.get_attribute("data-state"))
    shot(page, "06-totem-idiomas.png")


ETAPAS = {
    "setor": cap_setor,
    "bebidas": cap_bebidas,
    "produto": cap_produto,
    "complemento": cap_complemento,
    "grupo": cap_grupo,
    "totem": cap_totem,
}


def main():
    pedidos = sys.argv[1:] or ["setor", "produto", "complemento", "grupo", "totem"]
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"},
        )
        kwargs = {
            "viewport": {"width": 1440, "height": 900},
            "device_scale_factor": 1.5,
            "locale": "pt-BR",
            "timezone_id": "America/Sao_Paulo",
        }
        if STATE.exists():
            kwargs["storage_state"] = str(STATE)
        ctx = browser.new_context(**kwargs)
        page = ctx.new_page()
        login(page, ctx)
        for nome in pedidos:
            print("==", nome)
            ETAPAS[nome](page)
        ctx.storage_state(path=str(STATE))
        browser.close()
    print("rode o annotate.py para gerar imagens-tratadas")


if __name__ == "__main__":
    main()
