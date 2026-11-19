"""Captura as quatro telas do BeeFood para o #134 — ativação da Natural Bot.

A credencial é criada de verdade, como no #129: o diálogo **Credencial criada** só existe
depois de criar, e é nele que o `clientId` e o `clientSecret` aparecem lado a lado. A
diferença aqui é a lista de permissões — a Natural Bot pede **seis** acessos, e o diálogo
nasce com **todos** ligados, então o script desliga dez interruptores antes do print. O estado
inicial não é fotografado: o dono cortou a foto do "como ele abre", porque é a mesma tela.

O `clientId` e o `clientSecret` vão para `/tmp/manual-134-cred.json` (nunca para a pasta do
manual), de onde o `capturar-naturalbot.py` os lê para fotografar o formulário do parceiro
preenchido. Terminadas as capturas, `limpar-credencial.py` apaga essa credencial: o segredo que
aparece na imagem é, então, de uma credencial que não existe mais.

Uso, de dentro da pasta do manual:

    python3 capturar-beefood.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "painel-entregador"))

from playwright.sync_api import sync_playwright  # noqa: E402

from beefood import abrir, after_click, limpar_tela  # noqa: E402

SRC = Path(__file__).resolve().parent / "imagens-puras"
SRC.mkdir(exist_ok=True)
CRED = Path("/tmp/manual-134-cred.json")

# Os seis acessos que a tela da Natural Bot pede, na ordem em que ela os lista.
SEIS = ("store:read", "catalog:read", "orders:write", "orders:read", "webhook:read", "webhook:write")

# Recursos que saem inteiros (desligar o "Consultar" desliga o "Alterar" junto) e recursos
# que ficam, mas só para consultar.
FORA = ("customers", "coupons", "reviews", "stock", "drivers", "waiters", "cash-registers", "users")
SO_CONSULTAR = ("catalog", "store")


def salvar(page, nome: str):
    page.screenshot(path=str(SRC / nome))
    print("PURA", nome)


def switch(escopo, scope: str):
    """O interruptor da linha cujo nome em mono é este escopo."""
    return escopo.locator(f"xpath=.//code[normalize-space()='{scope}']/../label//button").first


def ligado(botao) -> bool:
    estado = botao.get_attribute("data-state") or botao.get_attribute("aria-checked") or ""
    return estado in ("checked", "true")


def deixar_so_os_seis(page, dialogo):
    for recurso in FORA:
        b = switch(dialogo, f"{recurso}:read")
        if ligado(b):
            b.click()
            page.wait_for_timeout(250)
    for recurso in SO_CONSULTAR:
        b = switch(dialogo, f"{recurso}:write")
        if ligado(b):
            b.click()
            page.wait_for_timeout(250)
    ligados = sorted(
        c.inner_text().strip()
        for c in dialogo.locator("code").all()
        if ":" in c.inner_text() and ligado(switch(dialogo, c.inner_text().strip()))
    )
    assert ligados == sorted(SEIS), f"escopos ligados fora do combinado: {ligados}"


with sync_playwright() as p:
    browser, ctx, page = abrir(p, "/aplicativos")
    limpar_tela(page)
    after_click(page, 3000)
    salvar(page, "01-aplicativos-api-aberta.png")

    # O painel lateral é alto: viewport maior para ele caber inteiro, como no #127 e no #129.
    page.set_viewport_size({"width": 1440, "height": 1300})
    after_click(page, 2000)

    page.get_by_text("API Aberta", exact=True).first.click()
    after_click(page, 8000)
    limpar_tela(page)
    salvar(page, "02-painel-credencial.png")

    page.get_by_role("button", name="CRIAR CREDENCIAL").click()
    after_click(page, 2500)
    nova = page.locator('[role="dialog"]').filter(has_text="Nova credencial adicional").last

    deixar_so_os_seis(page, nova)
    after_click(page, 1500)
    salvar(page, "03-nova-credencial-seis.png")

    nova.get_by_role("button", name="CRIAR").click()
    after_click(page, 9000)
    criada = page.locator('[role="dialog"]').filter(has_text="Credencial criada").last
    salvar(page, "04-credencial-criada.png")

    codes = [c.inner_text().strip() for c in criada.locator("code").all()]
    CRED.write_text(json.dumps({"clientId": codes[0], "clientSecret": codes[1]}))
    print("credencial criada:", codes[0], "- secret em", CRED)

    criada.get_by_role("button", name="FECHAR").click()
    after_click(page, 3000)

    ctx.close()
    browser.close()
