"""Captura #77 Cardápio digital presencial e QR Code.

Rodar na pasta do manual:
  python capturar.py           # dump + todas as capturas
  python capturar.py dump      # só login + dump da API (não grava nada)
  python capturar.py admin     # card Presencial + parâmetros + garçom
  python capturar.py qr        # modais QR Geral e Mesa
  python capturar.py links     # Meus Links (presencial)
  python capturar.py public    # cardápio público ?tipo=p e visualização

NÃO clicar em switch do card Presencial: a tela grava sozinha.
Abrir modal de QR / Meus Links / Garçom é só leitura (fechar com ESC).
Gerar QR de mesa 1–6 é local, não grava no servidor.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

DIR = Path(__file__).resolve().parent
PURA = DIR / "imagens-puras"
PURA.mkdir(exist_ok=True)
STATE = Path("/tmp/beefood3-storage.json")
DUMP = Path("/tmp/beefood3-presencial-dump.json")

LOGIN_EMAIL = "contato@beefood.com.br"
LOGIN_SENHA = "1q2w3e4r"
WAIT = 5000
ADMIN = "https://beefood.app/cardapio-digital?tab=configuracoes&scrollTo=presencial"
MENU_P = "https://menu.beefood.com.br/beefood3/?tipo=p"
MENU_VIS = "https://cardapio.beefood.com.br/beefood3"
MENU_PRES = "https://presencial.beefood.com.br/beefood3"


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
    nps = page.locator('[role="dialog"]').filter(
        has_text="Como está sendo sua experiência"
    )
    if nps.count():
        try:
            nps.get_by_role("button", name="FECHAR").first.click(timeout=1500)
            page.wait_for_timeout(400)
        except Exception:
            page.keyboard.press("Escape")
            page.wait_for_timeout(400)
    for sel in ('button[aria-label="Dispensar"]',):
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
        else:
            t = page.locator('button:has-text("Alterar tema")')
            if t.count():
                t.first.click()
                page.wait_for_timeout(800)


def login(page):
    page.goto("https://beefood.app/login", wait_until="domcontentloaded")
    after_click(page, 2500)
    if "login" in page.url.lower():
        page.fill("input#emailOrWhatsapp", LOGIN_EMAIL)
        page.fill("input#password", LOGIN_SENHA)
        page.locator("button", has_text="ENTRAR").first.click()
        after_click(page, 9000)
    limpar_tela(page)
    tema_claro(page)


def shot(page, nome: str, locator=None, full: bool = False):
    dest = PURA / nome
    if locator is not None:
        locator.screenshot(path=str(dest), type="png")
    else:
        page.screenshot(path=str(dest), type="png", full_page=full)
    print("SHOT", nome, dest.stat().st_size)


def dump_apis(page) -> dict:
    found: dict = {}

    def on_resp(resp):
        u = resp.url
        method = resp.request.method
        try:
            if "cardapioDigital/configuracoes" in u and method == "GET":
                found["config"] = resp.json()
            elif "/cabecalho/" in u and method == "GET":
                found["cabecalho"] = resp.json()
            elif "garcomOpc" in u and method == "GET":
                found["garcom"] = resp.json()
            elif ("mesa" in u.lower() or "comanda" in u.lower()) and method == "GET":
                if "json" in (resp.headers.get("content-type") or ""):
                    found.setdefault("mesas_raw_urls", []).append(u)
        except Exception:
            pass

    page.on("response", on_resp)
    page.goto(ADMIN, wait_until="domcontentloaded")
    after_click(page, 7000)
    limpar_tela(page)
    tema_claro(page)

    cfg = found.get("config") or {}
    if isinstance(cfg, dict):
        print("=== CONFIG PRESENCIAL ===")
        for k in (
            "nomeFantasia",
            "linkAcesso",
            "qrCodePresencial",
            "presencialGarcomOpcoes",
            "pFechaConta",
            "pedidoSemCadastroPresencial",
            "pedSemCadPSimp",
            "solicitaEmailP",
            "solicitaNascimentoP",
            "consumoLocal",
            "abertoDelivery",
        ):
            print(f"  {k}: {cfg.get(k)}")

    cab = found.get("cabecalho")
    if cab:
        print("=== CABECALHO ===")
        rows = cab if isinstance(cab, list) else [cab]
        for r in rows[:3]:
            if isinstance(r, dict):
                print(
                    " ",
                    {
                        k: r.get(k)
                        for k in (
                            "linkAcesso",
                            "linkAcessoP",
                            "qrCodePresencial",
                            "presencialAberto",
                            "horarioAtendimentoPresencialAgora",
                        )
                    },
                )

    DUMP.write_text(json.dumps(found, indent=2, ensure_ascii=False, default=str))
    print("DUMP", DUMP)
    return found


def abrir_config(page):
    page.goto(ADMIN, wait_until="domcontentloaded")
    after_click(page, 7000)
    limpar_tela(page)
    tema_claro(page)
    after_click(page, 2000)
    page.keyboard.press("Escape")
    page.wait_for_timeout(400)


def card_presencial(page):
    titulo = page.get_by_text("Presencial (Mesas/Comandas)", exact=True)
    if titulo.count():
        titulo.first.scroll_into_view_if_needed()
        after_click(page, 2000)
        card = titulo.first.locator("xpath=ancestor::div[contains(@class,'rounded')][1]")
        return card
    return None


def admin_shots(page):
    abrir_config(page)
    shot(page, "00-admin-full.png")

    card = card_presencial(page)
    if card and card.count():
        try:
            shot(page, "01-card-presencial.png", card.first)
        except Exception as e:
            print("card shot fail", e)
            shot(page, "01-card-presencial.png")
    else:
        print("card Presencial não achado")
        shot(page, "01-card-presencial.png")

    shot(page, "01-onde-fica.png")

    # modal garçom: no sandbox o switch vem desligado. Liga só para o
    # print (02 + 03), abre o modal, fecha e restaura. Auto-save ~800 ms.
    garcom_lbl = page.locator("label", has_text="Habilitar opções do Garçom")
    restaurou_garcom = False
    if garcom_lbl.count():
        row = garcom_lbl.first.locator("xpath=ancestor::div[contains(@class,'flex')][1]")
        sw = row.locator('[role="switch"]')
        if sw.count() and sw.first.get_attribute("data-state") != "checked":
            sw.first.click()
            after_click(page, 2500)
            restaurou_garcom = True
            print("ligou garçom temporariamente")
    cad = page.get_by_text("Cadastro", exact=True)
    if cad.count():
        cad.first.scroll_into_view_if_needed()
        after_click(page, 2000)
    shot(page, "02-parametros.png")
    cfg_btn = page.locator("button", has_text="Configurar")
    if cfg_btn.count():
        cfg_btn.first.click()
        after_click(page, 4000)
        shot(page, "03-garcom-opcoes.png")
        page.keyboard.press("Escape")
        after_click(page, 1500)
    else:
        print("botão Configurar não achado (garçom desligado?)")
    if restaurou_garcom and garcom_lbl.count():
        row = garcom_lbl.first.locator("xpath=ancestor::div[contains(@class,'flex')][1]")
        sw = row.locator('[role="switch"]')
        if sw.count() and sw.first.get_attribute("data-state") == "checked":
            sw.first.click()
            after_click(page, 2500)
            print("restaurou garçom desligado")


def qr_shots(page):
    abrir_config(page)
    card = card_presencial(page)
    if card:
        card.first.scroll_into_view_if_needed()
        after_click(page, 2000)

    page.locator("button", has_text="QR Code Geral").first.click()
    after_click(page, 3000)
    shot(page, "04-qr-geral.png")
    page.keyboard.press("Escape")
    after_click(page, 1500)

    page.locator("button", has_text="QR Code Mesa").first.click()
    after_click(page, 2500)
    shot(page, "05-qr-mesa-vazio.png")
    # intervalo 1–6 (local, não grava)
    inputs = page.locator('div[role="dialog"] input[type="number"]')
    if inputs.count() >= 2:
        inputs.nth(0).fill("1")
        inputs.nth(1).fill("6")
    page.locator("button", has_text="Gerar QR Codes").first.click()
    after_click(page, 3000)
    shot(page, "05-qr-mesa.png")
    page.keyboard.press("Escape")
    after_click(page, 1500)

    page.locator("button", has_text="QR Code Comanda").first.click()
    after_click(page, 2500)
    shot(page, "05b-qr-comanda-vazio.png")
    page.keyboard.press("Escape")
    after_click(page, 1500)


def abrir_meus_links(page):
    page.goto("https://beefood.app/", wait_until="domcontentloaded")
    after_click(page, 5000)
    limpar_tela(page)
    tema_claro(page)
    btn = page.locator("button", has_text="Meus Links")
    if not btn.count():
        # sidebar colapsada? tenta o texto mesmo assim
        btn = page.get_by_text("Meus Links", exact=True)
    btn.first.click()
    after_click(page, 4000)
    limpar_tela(page)


def links_shots(page):
    abrir_meus_links(page)
    shot(page, "06-meus-links-topo.png")

    pres = page.get_by_text("Cardápios Presencial", exact=True)
    if pres.count():
        pres.first.scroll_into_view_if_needed()
        after_click(page, 2000)
    # o grupo presencial + o card de mesa/comanda
    shot(page, "06-meus-links.png")

    mesa_sel = page.locator('[role="dialog"], [data-state="open"]').locator(
        "button"
    ).filter(has_text="Sem mesa")
    # SelectTrigger mostra "Sem mesa" / "Mesa N"
    trigger = page.get_by_text("Sem mesa", exact=True)
    if trigger.count():
        trigger.first.click()
        after_click(page, 1500)
        shot(page, "07-meus-links-lista-mesa.png")
        # escolhe a primeira mesa numerada, se existir
        item = page.locator('[role="option"]').filter(has_text="Mesa").first
        if item.count():
            item.click()
            after_click(page, 2000)
            shot(page, "07-meus-links-mesa.png")
        else:
            page.keyboard.press("Escape")
            after_click(page, 800)
            print("nenhuma mesa no select")
    else:
        print("select Sem mesa não achado")

    # gerador
    ger = page.locator("button", has_text="Abrir Gerador de QR Codes")
    if ger.count():
        ger.first.click()
        after_click(page, 2500)
        shot(page, "08-gerador-passo1.png")
        # escolhe Mesas
        page.get_by_text("QR Codes de Mesas", exact=True).first.click()
        after_click(page, 2500)
        shot(page, "09-tipo-qr.png")
        # Cardápio Digital Presencial — pode abrir o gate da comanda
        page.get_by_text("Cardápio Digital Presencial", exact=True).first.click()
        after_click(page, 3000)
        shot(page, "09b-depois-tipo.png")
        # se o gate "Você usa Comanda" abriu, fotografar e responder Não
        if page.get_by_text("Você usa Comanda").count():
            shot(page, "09c-gate-comanda.png")
            page.get_by_text("Não, só Mesas", exact=True).first.click()
            after_click(page, 3000)
            shot(page, "09d-depois-gate.png")
        page.keyboard.press("Escape")
        after_click(page, 1000)
        page.keyboard.press("Escape")
        after_click(page, 800)
    else:
        print("gerador não achado")


def public_shots(browser):
    ctx = browser.new_context(
        viewport={"width": 390, "height": 844},
        device_scale_factor=2,
        is_mobile=True,
        has_touch=True,
        locale="pt-BR",
        timezone_id="America/Sao_Paulo",
    )
    page = ctx.new_page()

    page.goto(MENU_P, wait_until="domcontentloaded")
    after_click(page, 8000)
    shot(page, "10-cel-presencial-home.png")
    # segunda tela: rolar um pouco ou clicar em algo seguro (não Retirada)
    page.mouse.wheel(0, 400)
    after_click(page, 2000)
    shot(page, "10b-cel-presencial-lista.png")

    page.goto(MENU_VIS, wait_until="domcontentloaded")
    after_click(page, 7000)
    shot(page, "11-cel-visualizacao.png")

    page.goto(MENU_PRES, wait_until="domcontentloaded")
    after_click(page, 7000)
    shot(page, "12-cel-presencial-dominio.png")

    ctx.close()


def main():
    modo = sys.argv[1] if len(sys.argv) > 1 else "tudo"
    os.environ.setdefault("LANG", "pt_BR.UTF-8")
    os.environ.setdefault("LANGUAGE", "pt_BR")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"},
        )
        ctx_kwargs = dict(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=1.5,
            locale="pt-BR",
            timezone_id="America/Sao_Paulo",
        )
        if STATE.exists():
            ctx_kwargs["storage_state"] = str(STATE)
        ctx = browser.new_context(**ctx_kwargs)
        page = ctx.new_page()
        login(page)
        ctx.storage_state(path=str(STATE))

        if modo in ("tudo", "dump"):
            dump_apis(page)
        if modo in ("tudo", "admin"):
            admin_shots(page)
        if modo in ("tudo", "qr"):
            qr_shots(page)
        if modo in ("tudo", "links"):
            links_shots(page)
        if modo in ("tudo", "public"):
            public_shots(browser)

        ctx.close()
        browser.close()
    print("fim", modo)


if __name__ == "__main__":
    main()
