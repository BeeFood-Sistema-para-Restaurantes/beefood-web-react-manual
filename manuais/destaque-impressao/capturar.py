#!/usr/bin/env python3
"""Captura #99 — Destaque na impressão (sandbox BeeFood3).

  python capturar.py            # tudo
  python capturar.py cadastro   # produto + complemento
  python capturar.py lote
  python capturar.py pedido     # PDV + detalhe + cupom + cozinha

Depois de cada clique: spinner some e só então 5 s.
NÃO processar o lote (só fotografar a etapa 2).
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


def shot(page, nome: str, full: bool = False):
    dest = PURA / nome
    page.screenshot(path=str(dest), type="png", full_page=full)
    print("SHOT", dest.name, dest.stat().st_size)


def fechar_modal(page):
    dlg = page.locator('div[role="dialog"]').last
    x = dlg.locator('button[aria-label="Fechar"], button:has-text("FECHAR")')
    if x.count():
        try:
            x.first.click(timeout=1500)
            after_click(page)
            return
        except Exception:
            pass
    page.keyboard.press("Escape")
    after_click(page)


def instalar_gancho_cupom(page):
    page.evaluate(
        """() => {
          window.__cupomHTML = null;
          const grab = () => {
            const f = document.getElementById('beefood-print-frame');
            if (!f) return;
            try {
              const doc = f.contentDocument;
              if (doc && doc.body && (doc.body.innerText || '').trim().length > 20) {
                window.__cupomHTML = doc.documentElement.outerHTML;
                if (f.contentWindow) f.contentWindow.print = () => {};
              }
            } catch (e) {}
          };
          new MutationObserver(grab).observe(document.documentElement, {childList:true, subtree:true});
          setInterval(grab, 40);
        }"""
    )


def render_cupom(context, html: str, nome: str):
    cupom = context.new_page()
    cupom.set_viewport_size({"width": 400, "height": 1100})
    cupom.set_content(html, wait_until="domcontentloaded")
    cupom.wait_for_timeout(1500)
    dest = PURA / nome
    cupom.screenshot(path=str(dest), type="png", full_page=True)
    print("SHOT", dest.name, dest.stat().st_size)
    print("TEXTO", dest.name, ":", cupom.inner_text("body")[:1800].replace("\n", " | "))
    cupom.close()


def limpar_cache_destaque(page):
    page.evaluate(
        """() => {
          const keys = [];
          for (let i = 0; i < localStorage.length; i++) {
            const k = localStorage.key(i);
            if (k && k.startsWith('beefood_destaque_impressao')) keys.push(k);
          }
          keys.forEach(k => localStorage.removeItem(k));
        }"""
    )


def cap_cadastro_produto(page):
    page.goto("https://beefood.app/cardapio?tab=produtos", wait_until="domcontentloaded")
    after_click(page, 6000)
    limpar(page)
    page.get_by_text("Bebidas", exact=True).first.click()
    after_click(page, 4000)
    page.get_by_text("Coca Cola 350ml", exact=True).first.click()
    after_click(page, 6000)
    sw = page.locator("#destaqueImpressao")
    if sw.count():
        sw.first.scroll_into_view_if_needed()
        page.wait_for_timeout(800)
        print("switch produto", sw.first.get_attribute("data-state"))
    else:
        print("SEM switch produto; dialog:", page.locator('div[role="dialog"]').last.inner_text()[:800])
    shot(page, "01-cadastro-produto.png")
    fechar_modal(page)


def cap_cadastro_complemento(page):
    page.goto("https://beefood.app/cardapio?tab=complementos", wait_until="domcontentloaded")
    after_click(page, 6000)
    limpar(page)
    page.get_by_text("Molho verde", exact=True).first.click()
    after_click(page, 6000)
    sw = page.locator("#destaqueImpressao")
    if sw.count():
        sw.first.scroll_into_view_if_needed()
        page.wait_for_timeout(800)
        print("switch complemento", sw.first.get_attribute("data-state"))
    else:
        print("SEM switch complemento")
    shot(page, "02-cadastro-complemento.png")
    fechar_modal(page)


def cap_lote(page):
    page.goto("https://beefood.app/cardapio?tab=produtos", wait_until="domcontentloaded")
    after_click(page, 6000)
    limpar(page)
    page.get_by_text("Bebidas", exact=True).first.click()
    after_click(page, 4000)
    page.get_by_role("button", name="Editar em Lote").click()
    after_click(page, 4000)
    page.get_by_role("button", name="PRÓXIMO").click()
    after_click(page, 3000)
    dlg = page.locator('div[role="dialog"]').last
    campo = dlg.get_by_text("Destaque na impressão", exact=True)
    if campo.count():
        campo.first.scroll_into_view_if_needed()
        page.wait_for_timeout(400)
        # marca o checkbox do campo (não processa)
        box = campo.first.locator("xpath=ancestor::div[contains(@class,'border')]").locator('[role="checkbox"]')
        if box.count() and box.first.get_attribute("data-state") != "checked":
            box.first.click()
            after_click(page, 2000)
        sw = campo.first.locator("xpath=ancestor::div[contains(@class,'border')]").locator('[role="switch"]')
        if sw.count() and sw.first.get_attribute("data-state") != "checked":
            sw.first.click()
            after_click(page, 2000)
        print("lote campo ok", "switch", sw.first.get_attribute("data-state") if sw.count() else "sem")
    else:
        print("SEM campo lote. dialog:", dlg.inner_text()[:1200])
    shot(page, "03-editar-lote.png")
    # fecha sem processar
    page.keyboard.press("Escape")
    after_click(page)
    if page.locator('div[role="dialog"]').count():
        page.keyboard.press("Escape")
        after_click(page)


def escolher_opcao(dlg, texto: str):
    alvo = dlg.get_by_text(texto, exact=True)
    if alvo.count() == 0:
        alvo = dlg.get_by_text(texto)
    if alvo.count() == 0:
        print("FALTA opcao", texto)
        return False
    alvo.first.scroll_into_view_if_needed()
    alvo.first.click()
    after_click(dlg.page if hasattr(dlg, "page") else alvo.page, 1500)
    return True


def clicar_card_pdv(page, nome: str, precisa_combo: bool = False):
    page.fill('input[placeholder="Digite algo para buscar..."]', nome)
    after_click(page, 3000)
    cards = page.locator('div[class*="cursor-pointer"]')
    escolhido = None
    for c in cards.all():
        t = (c.inner_text() or "").strip()
        if nome not in t:
            continue
        if precisa_combo and "COMBO" not in t.upper():
            continue
        if not precisa_combo and t.startswith("COMBO") and "Combo " in t and nome != t:
            # evita pegar "Combo X" quando buscamos o item simples
            pass
        escolhido = c
        print("CARD", t.replace("\n", " / ")[:160])
        if precisa_combo and "COMBO" in t.upper():
            break
    if escolhido is None:
        raise RuntimeError(f"não achei card {nome!r} combo={precisa_combo}")
    escolhido.click()
    after_click(page, 4000)


def cap_pedido(page, context):
    page.goto("https://beefood.app/pdv", wait_until="domcontentloaded")
    after_click(page, 7000)
    limpar(page)

    clicar_card_pdv(page, "Combo One Burger", precisa_combo=True)
    dlg = page.locator('div[role="dialog"]').last
    print("DIALOG combo:", dlg.inner_text()[:1500].replace("\n", " | "))
    for txt in ("Coca Cola 350ml", "Sem Maionese Verde"):
        ok = False
        loc = dlg.get_by_text(txt, exact=True)
        if loc.count():
            loc.first.scroll_into_view_if_needed()
            loc.first.click()
            after_click(page, 1500)
            ok = True
        print("opcao", txt, ok)
    add = dlg.locator('button:has-text("Adicionar ao carrinho")')
    if add.count() and add.first.is_disabled():
        print("carrinho desabilitado, tentando obrigatórios")
        for txt in ("One Burger", "Batata frita", "Batata"):
            loc = dlg.get_by_text(txt)
            if loc.count():
                loc.first.click()
                after_click(page, 1200)
                print("clique extra", txt)
    add.first.click()
    after_click(page, 4000)

    clicar_card_pdv(page, "Mozza Sticks + Molho", precisa_combo=True)
    dlg = page.locator('div[role="dialog"]').last
    print("DIALOG mozza:", dlg.inner_text()[:1200].replace("\n", " | "))
    loc = dlg.get_by_text("Molho verde", exact=True)
    if loc.count() == 0:
        loc = dlg.get_by_text("Molho Barbecue", exact=True)
    if loc.count():
        loc.first.click()
        after_click(page, 1500)
    dlg.locator('button:has-text("Adicionar ao carrinho")').first.click()
    after_click(page, 4000)

    page.locator('button:has-text("Receber (F3)")').first.click()
    after_click(page, 6000)
    page.locator('button:has-text("Dinheiro")').first.click()
    after_click(page, 3000)
    page.locator('button:has-text("CONFIRMAR")').first.click()
    after_click(page, 8000)
    print("venda registrada")

    page.goto("https://beefood.app/historico", wait_until="domcontentloaded")
    after_click(page, 6000)
    limpar(page)
    seletor = page.locator("button").filter(has_text="por página")
    if seletor.count():
        seletor.first.click()
        after_click(page, 1000)
        page.get_by_text("100", exact=True).first.click()
        after_click(page, 3000)
    row = page.locator("table tbody tr").first
    print("primeira linha:", row.inner_text()[:200].replace("\n", " | "))
    row.click()
    after_click(page, 14000)
    limpar(page)
    shot(page, "04-detalhe-venda.png")

    limpar_cache_destaque(page)
    instalar_gancho_cupom(page)

    printer = page.locator('[role="dialog"] button').filter(has=page.locator("svg.lucide-printer"))
    if printer.count() == 0:
        printer = page.locator("button").filter(has=page.locator("svg.lucide-printer"))
    print("printer", printer.count())
    page.evaluate("() => { window.__cupomHTML = null; }")
    printer.first.click()
    html = None
    for _ in range(80):
        html = page.evaluate("() => window.__cupomHTML")
        if html:
            break
        page.wait_for_timeout(250)
    print("cupom pedido", "SIM" if html else "NAO", len(html or ""))
    if html:
        render_cupom(context, html, "05-cupom-pedido.png")

    page.evaluate("() => { window.__cupomHTML = null; }")
    chef = page.locator('[role="dialog"] button').filter(has=page.locator("svg.lucide-chef-hat"))
    if chef.count() == 0:
        chef = page.locator("button").filter(has=page.locator("svg.lucide-chef-hat"))
    print("chef", chef.count())
    if chef.count():
        chef.first.click()
        after_click(page, 3000)
        # se abrir modal de reimpressão / escolha, confirma
        if page.get_by_role("button", name="IMPRIMIR").count():
            page.get_by_role("button", name="IMPRIMIR").last.click()
            after_click(page, 2000)
        if page.get_by_text("Todos os produtos já foram impressos").count():
            print("cozinha ja impressa — menu reimprimir")
            mais = page.locator('[role="dialog"] button').filter(has=page.locator("svg.lucide-ellipsis"))
            if mais.count() == 0:
                mais = page.locator('[role="dialog"]').get_by_text("Imprimir Cozinha")
            # tenta o dropdown de mais ações
            page.locator('[role="dialog"]').get_by_text("Imprimir Cozinha").first.click()
            after_click(page, 2000)
    html = None
    for _ in range(80):
        html = page.evaluate("() => window.__cupomHTML")
        if html:
            break
        page.wait_for_timeout(250)
    print("cupom cozinha", "SIM" if html else "NAO", len(html or ""))
    if html:
        render_cupom(context, html, "06-cupom-cozinha.png")
    else:
        print("body agora:", page.inner_text("body")[-800:])


ETAPAS = {
    "cadastro": lambda page, ctx: (cap_cadastro_produto(page), cap_cadastro_complemento(page)),
    "lote": lambda page, ctx: cap_lote(page),
    "pedido": cap_pedido,
}


def main():
    pedidos = sys.argv[1:] or ["cadastro", "lote", "pedido"]
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
        ctx.route("http://localhost:1316/**", lambda route: route.abort())
        ctx.route("http://localhost:1317/**", lambda route: route.abort())
        ctx.route("https://impressao.ngrok.app/**", lambda route: route.abort())
        ctx.route("https://impressao-cozinha.ngrok.app/**", lambda route: route.abort())
        page = ctx.new_page()
        login(page, ctx)
        for nome in pedidos:
            print("==", nome)
            ETAPAS[nome](page, ctx)
        ctx.storage_state(path=str(STATE))
        browser.close()


if __name__ == "__main__":
    main()
