#!/usr/bin/env python3
"""Captura #122 — Cupom e cashback no totem.

    python3 capturar.py                  # painel (CRM) + aparelho
    python3 capturar.py cupons cupom cashback
    python3 capturar.py aparelho         # só as telas do totem

O painel sai em 1440x900 com DPR 1.5; o totem, em 1080x1920. O roteiro do
aparelho **para antes do pagamento** — nada é gravado. O teclado do totem ignora
click() por JS, então telefone e mesa são digitados com o clique real.
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
ESCONDE_FLUTUANTE = """
  div.fixed.bottom-6, a[href*="wa.me"], iframe[title*="WhatsApp"],
  #beefood-whatsapp-widget { display: none !important }
"""


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
    page.add_style_tag(content=ESCONDE_FLUTUANTE)
    page.evaluate("""() => {
      for (const e of document.querySelectorAll('div[class*="fixed"]')) {
        const r = e.getBoundingClientRect();
        if (r.width < 120 && r.height < 120 && r.bottom > innerHeight - 160)
          e.style.display = 'none';
      }
    }""")


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


# ------------------------------------------------------------------- painel
def cap_cupons(page):
    """A lista de cupons filtrada pelo canal Totem."""
    page.goto("https://beefood.app/cupom-desconto", wait_until="domcontentloaded")
    after_click(page, 9000)
    limpar(page)
    page.get_by_text("Todos os canais", exact=False).first.click()
    after_click(page, 2000)
    page.get_by_role("option", name="Totem", exact=False).first.click()
    after_click(page, 5000)
    limpar(page)
    cabeca = page.locator("text=cupom(ns)").first
    print("  filtro:", cabeca.inner_text() if cabeca.count() else "?")
    shot(page, "01-crm-cupons-canal-totem.png")


def cap_cupom(page):
    """O modal de um cupom: canais à esquerda, regras à direita."""
    page.goto("https://beefood.app/cupom-desconto", wait_until="domcontentloaded")
    after_click(page, 9000)
    limpar(page)
    page.get_by_text("SMS", exact=True).first.click()
    after_click(page, 6000)
    limpar(page)
    page.evaluate("""() => {
      const dlg = [...document.querySelectorAll('[role=dialog]')].pop();
      const ler = e => (e.innerText || '').replace(/\\s+/g, ' ').trim();
      const alvo = [...dlg.querySelectorAll('div,p,span,h3')]
        .filter(e => ler(e) === 'Canais de Visibilidade').pop();
      if (alvo) alvo.scrollIntoView({block: 'center'});
    }""")
    page.wait_for_timeout(3000)
    dlg = page.locator('[role="dialog"]').last
    print("  modal:", " | ".join(
        [l.strip() for l in (dlg.inner_text() or "").split("\n") if l.strip()])[:700])
    shot(page, "02-crm-cupom-canais-regras.png")
    page.keyboard.press("Escape")
    after_click(page, 2000)


def cap_cashback(page):
    page.goto("https://beefood.app/cashback", wait_until="domcontentloaded")
    after_click(page, 9000)
    limpar(page)
    alvo = page.get_by_text("Pedidos via Totem", exact=True).first
    alvo.scroll_into_view_if_needed()
    page.wait_for_timeout(2500)
    limpar(page)
    shot(page, "03-crm-cashback-modalidade-totem.png")


PAINEL = {"cupons": cap_cupons, "cupom": cap_cupom, "cashback": cap_cashback}


# ----------------------------------------------------------------- aparelho
def tocar(pg, texto, minimo=0, obrigatorio=True):
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
    for c in texto:
        pg.get_by_role("button", name=c, exact=True).first.click(force=True)
        pg.wait_for_timeout(150)


def esperar_imagens(pg, ms=12000):
    """O logotipo do cabeçalho do totem chega depois do texto — sem isto ele sai cortado."""
    try:
        pg.wait_for_function(
            "() => [...document.images].every(i => i.complete && i.naturalWidth > 0)",
            timeout=ms)
    except Exception:
        print("  aviso: alguma imagem não terminou de carregar")
    pg.wait_for_timeout(2500)


def resumo(pg, titulo):
    linhas = [l.strip() for l in pg.locator("body").inner_text().split("\n") if l.strip()]
    print(f"  {titulo}:", " | ".join(linhas)[:500])


def cap_aparelho(pg):
    pg.goto(TOTEM_URL, wait_until="networkidle", timeout=90000)
    pg.wait_for_timeout(9000)
    tocar(pg, "FAÇA SEU PEDIDO")
    pg.wait_for_timeout(4000)
    pg.evaluate("""() => {
      const alvo = [...document.querySelectorAll('div,article,li,button')].filter(e => {
        const t = (e.innerText || '').replace(/\\s+/g, ' ').trim().toUpperCase();
        return t.startsWith('ONE BURGER R$') && e.getBoundingClientRect().height < 400;
      }).pop();
      if (alvo) alvo.click();
    }""")
    pg.wait_for_timeout(4000)
    for _ in range(8):
        if tocar(pg, "ADICIONAR R$", 1650, obrigatorio=False):
            break
        if not tocar(pg, "PULAR", 1650, obrigatorio=False):
            break
    tocar(pg, "VER SACOLA", 1650, obrigatorio=False)
    tocar(pg, "CONTINUAR", 1650, obrigatorio=False)
    pg.wait_for_timeout(4000)
    esperar_imagens(pg)
    resumo(pg, "identificacao")
    shot(pg, "04-totem-identificacao-cashback.png")

    digitar(pg, "15999998888")
    tocar(pg, "CONFIRMAR", obrigatorio=False)
    pg.wait_for_timeout(7000)
    corpo = pg.locator("body").inner_text().upper()
    if "MESA" in corpo and pg.get_by_role("button", name="1", exact=True).count():
        digitar(pg, "12")
        tocar(pg, "CONFIRMAR", obrigatorio=False)
        pg.wait_for_timeout(6000)
    esperar_imagens(pg)
    resumo(pg, "confirmacao")
    shot(pg, "05-totem-confirmacao-cupom-cashback.png")

    tocar(pg, "CUPOM DE DESCONTO", 200)
    pg.wait_for_timeout(5000)
    esperar_imagens(pg)
    resumo(pg, "cupons")
    shot(pg, "06-totem-cupons-regras.png")


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
