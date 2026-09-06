"""Captura #83 Pedidos pelo chat (BeeBot).

1. Login e dashboard do bot.beefood (switch Pedido Chat).
2. Caminho no BeeFood: WhatsApp → Abrir Conversas.
3. Quatro mockups de WhatsApp (HTML) com o texto real da API validaFluxo.

Nao clica em switch. Lista de conversas e ofuscada (repositorio e publico).
"""
from __future__ import annotations

from pathlib import Path

from playwright.sync_api import sync_playwright

DIR = Path(__file__).resolve().parent
PURA = DIR / "imagens-puras"
PURA.mkdir(exist_ok=True)

LOGIN_EMAIL = "contato@beefood.com.br"
LOGIN_SENHA = "1q2w3e4r"
WAIT = 5000
STATE = Path("/tmp/beefood3-storage.json")


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


def limpar_beefood(page):
    page.add_style_tag(content="div.fixed.bottom-6 { display:none !important }")
    for sel in ('button[aria-label="Dispensar"]', 'button[aria-label="Fechar"]'):
        b = page.locator(sel)
        if b.count():
            try:
                b.first.click(timeout=1200)
                page.wait_for_timeout(300)
            except Exception:
                pass
    nps = page.locator('[role="dialog"]').filter(has_text="Como está sendo sua experiência")
    if nps.count():
        try:
            nps.locator("button").filter(has_text="FECHAR").first.click(timeout=1500)
            page.wait_for_timeout(400)
        except Exception:
            pass


def fechar_tour_bot(page):
    page.evaluate(
        """() => {
          const nodes = [...document.querySelectorAll('*')];
          const x = nodes.find(n => n.childNodes.length === 1 && n.textContent.trim() === '×');
          if (x) x.click();
        }"""
    )
    page.wait_for_timeout(500)
    try:
        page.keyboard.press("Escape")
    except Exception:
        pass
    page.wait_for_timeout(400)


def ofuscar_conversas(page):
    """Substitui nome/telefone reais da lista. Nao mexe no switch."""
    page.evaluate(
        """() => {
          const btns = [...document.querySelectorAll('button')];
          let n = 0;
          for (const b of btns) {
            const t = (b.innerText || '').trim();
            if (!t) continue;
            if (/^\\d{2}\\s*\\n?\\(?\\d/.test(t) || t.includes('Galli') || t.includes('Rafael') || t.includes('há ')) {
              const linhas = t.split('\\n').map(s => s.trim()).filter(Boolean);
              if (linhas.length >= 2) {
                n += 1;
                const fake = n === 1 ? 'Cliente' : 'Cliente ' + n;
                b.querySelectorAll('*').forEach(el => {
                  if (el.childNodes.length === 1 && el.childNodes[0].nodeType === 3) {
                    const v = el.textContent.trim();
                    if (/^\\(?\\d/.test(v) || /Galli|Rafael/i.test(v)) el.textContent = fake;
                    else if (/^\\(\\d{2}\\)/.test(v) || /^\\d{2}\\s/.test(v)) el.textContent = '(11) 9XXXX-000' + n;
                  }
                });
              }
            }
          }
        }"""
    )
    page.wait_for_timeout(300)


def cap_bot(page):
    page.goto("https://bot.beefood.com.br", wait_until="domcontentloaded")
    after_click(page, 3000)
    page.screenshot(path=str(PURA / "01-login-bot.png"), type="png")
    print("   -> 01-login-bot.png")

    page.fill("#usuario", LOGIN_EMAIL)
    page.fill("#senha", LOGIN_SENHA)
    page.locator("button", has_text="Entrar").first.click()
    after_click(page, 8000)
    fechar_tour_bot(page)
    after_click(page, WAIT)
    ofuscar_conversas(page)
    page.wait_for_timeout(800)

    # Confirma que Pedido Chat esta ligado (nao clica se ja estiver).
    sw = page.locator("#beeBotBeeChatPedido")
    estado = sw.get_attribute("data-state")
    print("   Pedido Chat data-state =", estado)
    if estado != "checked":
        raise RuntimeError("Pedido Chat veio desligado; nao religar daqui. Conferir no painel.")

    page.screenshot(path=str(PURA / "02-dashboard-bot.png"), type="png")
    print("   -> 02-dashboard-bot.png")

    # Recorte da coluna de switches (80 px) + um pouco da lista, sem o chat.
    box = page.locator("div.dark.w-\\[80px\\]").first.bounding_box()
    if not box:
        raise RuntimeError("nao achei a coluna de switches")
    page.screenshot(
        path=str(PURA / "02-pedido-chat.png"),
        type="png",
        clip={"x": 0, "y": 0, "width": min(420, 1440), "height": 900},
    )
    print("   -> 02-pedido-chat.png clip")


def login_beefood(page):
    page.goto("https://beefood.app/login", wait_until="domcontentloaded")
    after_click(page, 2500)
    if "login" in page.url.lower():
        page.fill("input#emailOrWhatsapp", LOGIN_EMAIL)
        page.fill("input#password", LOGIN_SENHA)
        page.locator("button", has_text="ENTRAR").first.click()
        after_click(page, 9000)
    limpar_beefood(page)
    cls = page.locator("html").get_attribute("class") or ""
    if "dark" in cls:
        alvo = page.locator('span.sr-only:has-text("Alterar tema")')
        if alvo.count():
            alvo.first.locator("xpath=ancestor::button").first.click()
            page.wait_for_timeout(800)


def cap_beefood_whatsapp(page):
    page.goto("https://beefood.app/whatsapp", wait_until="domcontentloaded")
    after_click(page, 8000)
    limpar_beefood(page)
    after_click(page, WAIT)
    page.screenshot(path=str(PURA / "00-beefood-whatsapp.png"), type="png")
    print("   -> 00-beefood-whatsapp.png")
    btn = page.locator("button", has_text="Abrir Conversas")
    print("   Abrir Conversas count =", btn.count())


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            env={**__import__("os").environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"},
        )
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=1.5,
            locale="pt-BR",
            timezone_id="America/Sao_Paulo",
        )
        page = context.new_page()
        page.set_default_timeout(30000)
        print("== bot.beefood ==")
        cap_bot(page)
        print("== beefood.app /whatsapp ==")
        login_beefood(page)
        cap_beefood_whatsapp(page)
        context.storage_state(path=str(STATE))
        browser.close()
    print("ok capturas painel")


if __name__ == "__main__":
    main()
