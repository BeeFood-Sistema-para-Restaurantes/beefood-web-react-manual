"""Sessão autenticada no painel da Natural Bot, usada pelas capturas do #134.

O acesso é de **homologação** (`hml-painel.naturalbot.com`), passado pelo dono na conversa.
O usuário fica aqui porque é descartável; a senha vem da variável `NB_SENHA`, porque o
painel é de um parceiro e este repositório é público:

    NB_SENHA='...' python3 capturar-naturalbot.py

O estado da sessão fica em `/tmp`, nunca na pasta do manual.

Detalhe do painel que vale para qualquer script: o menu da esquerda é todo de `<button>`,
inclusive os itens de segundo nível (Produtos, Lista de pedidos), e **Configurações** é um
texto simples. Depois de cada clique a tela monta em ~6 s, sem spinner com texto, então a
espera é por tempo mesmo.
"""

from __future__ import annotations

import os
from pathlib import Path

PAINEL = "https://hml-painel.naturalbot.com"
USUARIO = "beefood@beefood.com.br"
STATE = Path("/tmp/naturalbot-storage.json")
ESPERA = 6000


def esperar(page, ms: int = ESPERA):
    page.wait_for_timeout(ms)


def login(page):
    page.goto(f"{PAINEL}/login", wait_until="domcontentloaded")
    esperar(page, 5000)
    if "/login" not in page.url:
        return
    senha = os.environ.get("NB_SENHA")
    if not senha:
        raise RuntimeError("defina NB_SENHA com a senha do painel de homologação da Natural Bot")
    page.fill("input#email", USUARIO)
    page.fill("input#password", senha)
    page.get_by_role("button", name="Entrar").click()
    esperar(page, 10000)


def limpar_tela(page):
    """Esconde o widget de mensagens e o balão do robô, que ficam sobre o conteúdo."""
    page.add_style_tag(
        content="""
        div[class*="fixed"][class*="bottom"] { display: none !important }
        iframe[title*="chat" i], iframe[src*="chat" i] { display: none !important }
        """
    )
    esperar(page, 500)


def abrir(p, viewport=(1440, 900), escala=1.5):
    """Abre o navegador já logado no painel. Devolve (browser, context, page)."""
    browser = p.chromium.launch(env={**os.environ, "LANG": "pt_BR.UTF-8"})
    ctx = browser.new_context(
        viewport={"width": viewport[0], "height": viewport[1]},
        device_scale_factor=escala,
        locale="pt-BR",
        timezone_id="America/Sao_Paulo",
        storage_state=str(STATE) if STATE.exists() else None,
    )
    page = ctx.new_page()
    login(page)
    esperar(page, 3000)
    limpar_tela(page)
    ctx.storage_state(path=str(STATE))
    return browser, ctx, page


def menu(page, item: str, filho: str | None = None):
    """Clica num item do menu da esquerda e, se pedido, no item de segundo nível."""
    page.get_by_text(item, exact=True).first.click()
    esperar(page, 3000)
    if filho:
        page.get_by_role("button", name=filho).first.click()
        esperar(page, 10000)
    limpar_tela(page)


def card_integracao(page, nome: str):
    """O botão (Configurar/Editar) do card de uma integração na aba Integrações."""
    page.get_by_text(nome, exact=True).first.scroll_into_view_if_needed()
    esperar(page, 1500)
    return page.locator(
        "xpath=//*[normalize-space(text())='" + nome + "']"
        "/ancestor::div[.//button[normalize-space()='Editar' or normalize-space()='Configurar']][1]"
        "//button[normalize-space()='Editar' or normalize-space()='Configurar']"
    ).first
