#!/usr/bin/env python3
"""Captura #121 — Totem de Autoatendimento: pôr no ar e configurar.

    python capturar.py                 # painel + aparelho
    python capturar.py aplicativos configuracao pagamentos aparencia cardapios download
    python capturar.py aparelho        # só as telas do totem (viewport 1080x1920)

O painel sai em 1440x900 com DPR 1.5 (2160x1350) e o totem em 1080x1920, que é a
resolução do aparelho. Depois de cada clique: spinner some e só então 5 s.

O aparelho é uma página web — a URL é a mesma que a aba Download entrega, com o
token da filial (sandbox descartável, pode ficar versionado).
"""
from __future__ import annotations

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
TOTEM_URL = ("https://totem.beefood.app/?empresaID=38311&filialID=39202"
             "&token=D3590976-63A1-4FDF-9721-0E054CBF3BB5")


# --------------------------------------------------------------- utilidades
def after_click(page, extra_ms: int = WAIT):
    for _ in range(30):
        ocupado = (page.locator("text=Carregando...").count()
                   or page.locator("text=Atualizando...").count()
                   or page.locator("text=Calculando").count())
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


def tema_claro(page):
    if "dark" in (page.locator("html").get_attribute("class") or ""):
        alvo = page.locator('span.sr-only:has-text("Alterar tema")')
        if alvo.count():
            alvo.first.locator("xpath=ancestor::button").first.click()
            page.wait_for_timeout(800)


def login(page, ctx):
    page.goto("https://beefood.app/", wait_until="domcontentloaded")
    after_click(page)
    if page.locator("input#emailOrWhatsapp").count():
        page.fill("input#emailOrWhatsapp", LOGIN_EMAIL)
        page.fill("input#password", LOGIN_SENHA)
        page.get_by_role("button", name="ENTRAR").click()
        after_click(page, 9000)
        ctx.storage_state(path=str(STATE))
    tema_claro(page)
    limpar(page)


def shot(page, nome: str):
    destino = PURA / nome
    page.screenshot(path=str(destino), type="png")
    print("SHOT", destino.name, destino.stat().st_size)


def texto_modal(page, limite: int = 900):
    dlg = page.locator('[role="dialog"]').last
    linhas = [l.strip() for l in (dlg.inner_text() or "").split("\n") if l.strip()]
    print("  modal:", " | ".join(linhas)[:limite])


# ----------------------------------------------------------------- o painel
def abrir_modal(page):
    page.goto("https://beefood.app/aplicativos", wait_until="domcontentloaded")
    after_click(page, 8000)
    limpar(page)
    page.get_by_text("Autoatendimento presencial", exact=False).first.click()
    after_click(page, 8000)
    limpar(page)


def aba(page, nome: str):
    """As abas do modal não são role=tab — são botões/divs com o texto da aba."""
    achou = page.evaluate("""(nome) => {
      const dlg = [...document.querySelectorAll('[role=dialog]')].pop();
      const ler = e => (e.innerText || '').replace(/\\s+/g, ' ').trim();
      const alvo = [...dlg.querySelectorAll('button,div,span,a')]
        .filter(e => ler(e) === nome && e.getBoundingClientRect().height < 60)
        .pop();
      if (!alvo) return false;
      alvo.click();
      return true;
    }""", nome)
    if not achou:
        raise RuntimeError(f"aba {nome!r} não encontrada")
    after_click(page, 4000)


def rolar_modal(page, fracao: float):
    """Rola o corpo do modal. fracao 0..1 do scrollHeight."""
    page.evaluate("""(fracao) => {
      const dlg = [...document.querySelectorAll('[role=dialog]')].pop();
      const alvo = [...dlg.querySelectorAll('*')]
        .filter(e => e.scrollHeight > e.clientHeight + 40)
        .sort((a, b) => b.scrollHeight - a.scrollHeight)[0] || dlg;
      alvo.scrollTop = (alvo.scrollHeight - alvo.clientHeight) * fracao;
    }""", fracao)
    page.wait_for_timeout(2500)


def cap_aplicativos(page):
    page.goto("https://beefood.app/aplicativos", wait_until="domcontentloaded")
    after_click(page, 8000)
    limpar(page)
    alvo = page.get_by_text("Autoatendimento presencial", exact=False).first
    alvo.scroll_into_view_if_needed()
    page.wait_for_timeout(2500)
    print("  card:", alvo.bounding_box())
    shot(page, "01-aplicativos-card-totem.png")


def cap_configuracao(page):
    abrir_modal(page)
    texto_modal(page)
    shot(page, "02-modal-configuracao-topo.png")
    rolar_modal(page, 0.45)
    shot(page, "03-modal-configuracao-meio.png")
    rolar_modal(page, 1.0)
    shot(page, "04-modal-configuracao-fim.png")


def cap_pagamentos(page):
    abrir_modal(page)
    aba(page, "Pagamentos")
    texto_modal(page)
    shot(page, "05-modal-pagamentos.png")


def cap_aparencia(page):
    abrir_modal(page)
    aba(page, "Aparência")
    texto_modal(page)
    shot(page, "06-modal-aparencia.png")


def cap_cardapios(page):
    abrir_modal(page)
    aba(page, "Cardápios")
    texto_modal(page)
    shot(page, "07-modal-cardapios.png")


def cap_download(page):
    abrir_modal(page)
    aba(page, "Download")
    texto_modal(page)
    shot(page, "08-modal-download.png")


def cap_setor_foto(page):
    """Cardápio → menu do setor → Editar: é onde a foto do setor é subida."""
    page.goto("https://beefood.app/cardapio?tab=produtos", wait_until="domcontentloaded")
    after_click(page, 8000)
    limpar(page)
    alvo = None
    for cand in page.locator('div[class*="group"]').all():
        txt = (cand.inner_text() or "").strip()
        if txt.startswith("Bebidas") and cand.locator("svg.lucide-ellipsis-vertical").count():
            alvo = cand
            break
    if alvo is None:
        raise RuntimeError("linha do setor Bebidas não encontrada")
    alvo.locator("button").filter(
        has=page.locator("svg.lucide-ellipsis-vertical")).first.click()
    after_click(page, 1500)
    page.get_by_role("menuitem", name="Editar").first.click()
    after_click(page, 6000)
    limpar(page)
    texto_modal(page, 400)
    shot(page, "12-painel-setor-foto.png")


PAINEL = {
    "aplicativos": cap_aplicativos,
    "configuracao": cap_configuracao,
    "pagamentos": cap_pagamentos,
    "aparencia": cap_aparencia,
    "cardapios": cap_cardapios,
    "download": cap_download,
    "setor": cap_setor_foto,
}


# ---------------------------------------------------------------- o aparelho
def tocar(pg, texto, minimo=0, obrigatorio=True):
    """Toca no botão cujo texto contém `texto`. `minimo` filtra por altura na tela."""
    rotulo = pg.evaluate("""([texto, minimo]) => {
      const ler = b => (b.innerText || '').replace(/\\s+/g, ' ').trim();
      const alvo = [...document.querySelectorAll('button')].find(b =>
        b.getBoundingClientRect().y >= minimo && ler(b).toUpperCase().includes(texto));
      if (!alvo) return null;
      alvo.click();
      return ler(alvo);
    }""", [texto.upper(), minimo])
    if rotulo is None and obrigatorio:
        raise SystemExit(f"ERRO: não achei {texto!r}")
    pg.wait_for_timeout(2500)
    return rotulo


def digitar(pg, texto):
    """O teclado do totem ignora click() por JS — precisa do clique real."""
    for c in texto:
        pg.get_by_role("button", name=c, exact=True).first.click(force=True)
        pg.wait_for_timeout(150)


def cap_aparelho(pg):
    pg.goto(TOTEM_URL, wait_until="networkidle", timeout=90000)
    pg.wait_for_timeout(12000)
    shot(pg, "09-totem-espera.png")
    tocar(pg, "FAÇA SEU PEDIDO")
    pg.wait_for_timeout(4000)
    shot(pg, "10-totem-cardapio-sem-foto-setor.png")


def main():
    pedidos = sys.argv[1:] or list(PAINEL) + ["aparelho"]
    with sync_playwright() as p:
        nav = p.chromium.launch(headless=True)
        if [x for x in pedidos if x in PAINEL]:
            ctx = nav.new_context(
                viewport={"width": 1440, "height": 900}, device_scale_factor=1.5,
                locale="pt-BR", timezone_id="America/Sao_Paulo",
                storage_state=str(STATE) if STATE.exists() else None)
            page = ctx.new_page()
            login(page, ctx)
            for nome in pedidos:
                if nome in PAINEL:
                    print("==", nome)
                    PAINEL[nome](page)
            ctx.storage_state(path=str(STATE))
            ctx.close()
        if "aparelho" in pedidos:
            print("== aparelho")
            ctx = nav.new_context(viewport={"width": 1080, "height": 1920},
                                  locale="pt-BR", service_workers="block")
            cap_aparelho(ctx.new_page())
            ctx.close()
        nav.close()
    print("rode o annotate.py para gerar imagens-tratadas")


if __name__ == "__main__":
    main()
