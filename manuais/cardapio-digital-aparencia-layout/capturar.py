"""Captura #71 Aparência e layout — painel + cardápio público.

Rodar na pasta do manual:
  python capturar.py           # tudo
  python capturar.py login     # só login + dump
  python capturar.py admin     # só painel
  python capturar.py public    # só cardápio (estado atual)
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

DIR = Path(__file__).resolve().parent
PURA = DIR / "imagens-puras"
PURA.mkdir(exist_ok=True)
STATE = Path("/tmp/beefood3-storage.json")
CFG_DUMP = Path("/tmp/beefood3-aparencia-config.json")

WAIT = 5000
LOGIN_EMAIL = "contato@beefood.com.br"
LOGIN_SENHA = "1q2w3e4r"
ADMIN = "https://beefood.app/cardapio-digital?tab=configuracoes"
MENU = "https://menu.beefood.com.br/beefood3"


def after_click(page, extra_ms=WAIT):
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


def hide_chrome(page):
    page.add_style_tag(
        content="div.fixed.bottom-6 { display:none !important }"
    )
    for sel in (
        'button[aria-label="Dispensar"]',
        'button[aria-label="Fechar"]',
    ):
        btn = page.locator(sel)
        if btn.count():
            try:
                btn.first.click(timeout=1500)
                page.wait_for_timeout(400)
            except Exception:
                pass


def ensure_light(page):
    html = page.locator("html")
    cls = html.get_attribute("class") or ""
    if "dark" in cls:
        t = page.locator('button:has-text("Alterar tema")')
        if t.count():
            t.first.click()
            page.wait_for_timeout(800)
        else:
            sr = page.locator('span.sr-only:has-text("Alterar tema")')
            if sr.count():
                sr.first.locator("xpath=ancestor::button").first.click()
                page.wait_for_timeout(800)


def login(page):
    page.goto("https://beefood.app/login", wait_until="domcontentloaded")
    after_click(page, 2000)
    if "login" not in page.url.lower():
        print("já logado", page.url)
        return
    page.fill("input#emailOrWhatsapp", LOGIN_EMAIL)
    page.fill("input#password", LOGIN_SENHA)
    page.locator("button", has_text="ENTRAR").first.click()
    after_click(page, 8000)
    print("login url", page.url)


def dump_config(page):
    found = {}

    def on_resp(resp):
        u = resp.url
        if "cardapioDigital/configuracoes" in u and resp.request.method == "GET":
            try:
                found["get"] = resp.json()
                found["url"] = u
            except Exception:
                pass

    page.on("response", on_resp)
    page.goto(ADMIN, wait_until="domcontentloaded")
    after_click(page, 6000)
    hide_chrome(page)
    ensure_light(page)
    after_click(page, 2000)
    if found.get("get"):
        CFG_DUMP.write_text(json.dumps(found["get"], indent=2, ensure_ascii=False))
        d = found["get"]
        if isinstance(d, dict) and "result" in d:
            d = d.get("result") or d
        # datasnap às vezes embrulha
        print("CONFIG KEYS", list(d.keys())[:40] if isinstance(d, dict) else type(d))
        for k in (
            "nomeFantasia",
            "corPrimaria",
            "corAcao",
            "logotipoS3Link",
            "fotoCapa",
            "layoutSetor",
            "layoutStepCarrinho",
            "exibirPromocoes",
            "abrirPromocoesAuto",
            "linkAcesso",
            "id",
            "deliveryCategoriaID",
        ):
            if isinstance(d, dict) and k in d:
                v = d[k]
                if isinstance(v, str) and len(v) > 80:
                    v = v[:80] + "…"
                print(f"  {k}: {v}")
    else:
        print("GET config não interceptado")
    return found


def shot(page, name, locator=None, full=False):
    dest = PURA / name
    if locator is not None:
        locator.screenshot(path=str(dest), type="png")
    else:
        page.screenshot(path=str(dest), type="png", full_page=full)
    print("SHOT", name, dest.stat().st_size)


def admin_shots(page):
    page.goto(ADMIN, wait_until="domcontentloaded")
    after_click(page, 6000)
    hide_chrome(page)
    ensure_light(page)
    after_click(page, 3000)

    # fecha possível toast
    page.keyboard.press("Escape")
    page.wait_for_timeout(400)

    shot(page, "00-admin-full.png", full=False)

    card = page.locator("text=Aparência").first.locator(
        "xpath=ancestor::div[contains(@class,'rounded')]"
    )
    if card.count():
        try:
            card.first.screenshot(path=str(PURA / "01-aparencia.png"), type="png")
            print("SHOT 01-aparencia via card")
        except Exception as e:
            print("card shot fail", e)
            shot(page, "01-aparencia.png")
    else:
        shot(page, "01-aparencia.png")

    # preview (capa/logo)
    prev = page.get_by_text("Preview do Cardápio")
    if prev.count():
        box = prev.first.locator("xpath=ancestor::div[contains(@class,'space-y-3')]")
        if box.count():
            try:
                box.first.screenshot(path=str(PURA / "02-preview.png"), type="png")
                print("SHOT 02-preview")
            except Exception as e:
                print("preview fail", e)

    # hover capa para mostrar overlay
    capa = page.locator('img[alt="Capa"]')
    if capa.count():
        capa.first.hover()
        page.wait_for_timeout(600)
        shot(page, "02b-preview-hover.png")

    # identidade + cores
    ident = page.get_by_text("Identidade", exact=True)
    if ident.count():
        ident.first.scroll_into_view_if_needed()
        after_click(page, 2000)
        shot(page, "03-identidade.png")

    # abrir modal cor do tema
    tema = page.get_by_text("Cor do Tema", exact=True)
    if tema.count():
        btn = tema.first.locator("xpath=following::button[1]")
        if btn.count():
            btn.first.click()
            after_click(page, 2000)
            shot(page, "03b-modal-cor-tema.png")
            page.keyboard.press("Escape")
            page.wait_for_timeout(800)

    # layout
    lay = page.get_by_text("Layout do cardápio", exact=True)
    if lay.count():
        # pega o heading da seção (uppercase pequeno) ou o label do seletor
        for loc in page.get_by_text("Layout do cardápio").all():
            try:
                loc.scroll_into_view_if_needed()
            except Exception:
                pass
        after_click(page, 2000)
        shot(page, "04-layout.png")

    # vitrine dropdown
    vit = page.get_by_text("Vitrine de Promoções", exact=True)
    if vit.count():
        vit.first.scroll_into_view_if_needed()
        after_click(page, 1500)
        trig = page.locator('[role="combobox"]').filter(
            has_text="promoções"
        )
        # o trigger mostra o label atual
        for txt in (
            "Deixar a aba disponível",
            "Destacar promoções",
            "Não mostrar promoções",
        ):
            t = page.get_by_role("combobox").filter(has_text=txt)
            if t.count():
                t.first.click()
                after_click(page, 1500)
                shot(page, "05-vitrine-aberta.png")
                page.keyboard.press("Escape")
                break
        else:
            # tenta qualquer combobox perto
            cbs = page.locator('[role="combobox"]')
            print("combobox count", cbs.count())
            if cbs.count():
                cbs.last.click()
                after_click(page, 1500)
                shot(page, "05-vitrine-aberta.png")
                page.keyboard.press("Escape")


def public_home(context, name="10-cel-home.png"):
    page = context.new_page()
    page.goto(MENU, wait_until="domcontentloaded")
    after_click(page, 6000)
    # fecha cupom / aviso se aparecer
    for label in ("Dispensar", "Fechar", "OK", "Entendi"):
        b = page.get_by_role("button", name=label)
        if b.count():
            try:
                b.first.click(timeout=1500)
                page.wait_for_timeout(500)
            except Exception:
                pass
    page.keyboard.press("Escape")
    page.wait_for_timeout(800)
    shot(page, name)
    # dump textos úteis
    print("PUBLIC TITLE", page.title())
    print("PUBLIC TXT", page.inner_text("body")[:400].replace("\n", " | "))
    page.close()
    return name


def public_explore(context):
    page = context.new_page()
    page.goto(MENU, wait_until="domcontentloaded")
    after_click(page, 6000)
    page.keyboard.press("Escape")
    page.wait_for_timeout(500)
    # links / botões visíveis
    texts = page.locator("body").inner_text()
    print("--- PUBLIC BODY (800) ---")
    print(texts[:800])
    # tenta achar setores / produtos
    for sel in (
        "text=Promoções",
        "text=Lanches",
        "text=X-Burger",
        "text=One Burger",
        "text=Milk Shake",
        "text=Escolha um setor",
        "text=Sobremesas",
    ):
        n = page.locator(sel).count()
        print(f"  loc {sel}: {n}")
    page.close()


def run(phase="all"):
    os.environ.setdefault("LANG", "pt_BR.UTF-8")
    os.environ.setdefault("LANGUAGE", "pt_BR")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"},
        )
        kwargs = dict(
            locale="pt-BR",
            timezone_id="America/Sao_Paulo",
            viewport={"width": 1440, "height": 900},
            device_scale_factor=1.5,
        )
        if STATE.exists() and phase != "login":
            kwargs["storage_state"] = str(STATE)
        context = browser.new_context(**kwargs)
        page = context.new_page()
        if phase in ("all", "login"):
            login(page)
            dump_config(page)
            context.storage_state(path=str(STATE))
            print("STATE", STATE)
        if phase in ("all", "admin"):
            if "login" in page.url.lower():
                login(page)
            admin_shots(page)
            context.storage_state(path=str(STATE))
        if phase in ("all", "public"):
            phone = browser.new_context(
                locale="pt-BR",
                timezone_id="America/Sao_Paulo",
                viewport={"width": 390, "height": 844},
                device_scale_factor=2,
                is_mobile=True,
                has_touch=True,
            )
            public_home(phone)
            public_explore(phone)
            phone.close()
        browser.close()


if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else "all")
