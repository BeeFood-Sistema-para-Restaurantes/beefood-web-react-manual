"""Captura #17 BeeFood Pixel Analytics — sandbox BeeFood3.

Rodar na pasta do manual:
  python capturar.py diag        # só imprime a API (sem print)
  python capturar.py             # diagnóstico + todas as capturas

Regra permanente: spinner some, depois 5 s, só então screenshot.
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

LOGIN_EMAIL = "contato@beefood.com.br"
LOGIN_SENHA = "1q2w3e4r"
WAIT = 5000
URL = "https://beefood.app/food-marketing/pixel-analytics"

# Período amplo: rastreio começou em 01/06/2026.
DATA_INI = "2026-06-01"
DATA_FIM = "2026-09-02"


def after_click(page, extra_ms: int = WAIT):
    for _ in range(40):
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
    page.add_style_tag(
        content="""
        div.fixed.bottom-6 { display:none !important }
        """
    )
    nps = page.locator('[role="dialog"]').filter(has_text="Como está sendo sua experiência")
    if nps.count():
        try:
            nps.locator("button").filter(has_text="FECHAR").first.click(timeout=1500)
            page.wait_for_timeout(400)
        except Exception:
            pass
    for sel in ('button[aria-label="Dispensar"]',):
        b = page.locator(sel)
        if b.count():
            try:
                b.first.click(timeout=1200)
                page.wait_for_timeout(300)
            except Exception:
                pass


def esconder_ao_vivo(page, esconder: bool):
    page.add_style_tag(
        content=(
            "div.fixed.bottom-4.right-4 { display:none !important }"
            if esconder
            else "div.fixed.bottom-4.right-4 { display:flex !important }"
        )
    )


def tema_claro(page):
    cls = page.locator("html").get_attribute("class") or ""
    if "dark" in cls:
        alvo = page.locator('span.sr-only:has-text("Alterar tema")')
        if alvo.count():
            alvo.first.locator("xpath=ancestor::button").first.click()
            page.wait_for_timeout(800)


def login(page):
    page.goto("https://beefood.app/login", wait_until="domcontentloaded")
    after_click(page, 2500)
    if "login" in page.url.lower():
        page.fill("input#emailOrWhatsapp", LOGIN_EMAIL)
        page.fill("input#password", LOGIN_SENHA)
        page.locator("button", has_text="ENTRAR").first.click()
        after_click(page, 9000)


def tirar(page, nome: str, full: bool = False):
    limpar_tela(page)
    page.screenshot(path=str(PURA / nome), type="png", full_page=full)
    print("   ->", nome, PURA / nome)


def diagnosticar(page):
    """Lê as respostas que a própria tela já faz (report.beetechapi.be)."""
    capturado = {"pixel": None, "aovivo": None, "seg": None}

    def on_response(resp):
        url = resp.url
        if "pixelAnalytics" in url and capturado["pixel"] is None:
            try:
                capturado["pixel"] = {"status": resp.status, "url": url, "json": resp.json()}
            except Exception as e:
                capturado["pixel"] = {"status": resp.status, "url": url, "erro": str(e)}
        elif "pixelAoVivo" in url and capturado["aovivo"] is None:
            try:
                capturado["aovivo"] = {"status": resp.status, "url": url, "json": resp.json()}
            except Exception as e:
                capturado["aovivo"] = {"status": resp.status, "url": url, "erro": str(e)}
        elif "pixelSegmentacao" in url and capturado["seg"] is None:
            try:
                capturado["seg"] = {"status": resp.status, "url": url, "json": resp.json()}
            except Exception as e:
                capturado["seg"] = {"status": resp.status, "url": url, "erro": str(e)}

    page.on("response", on_response)
    page.goto(URL, wait_until="domcontentloaded")
    after_click(page, 8000)

    pix = capturado["pixel"] or {}
    j = pix.get("json") or {}
    funil = j.get("funil") or []
    produtos = (j.get("produtos") or [])[:8]
    print("PIXEL_URL", pix.get("url"), "status", pix.get("status"))
    print("FUNIL_LINHAS", len(funil))
    print("FUNIL", json.dumps(funil, ensure_ascii=False, indent=2)[:4000])
    print("PRODUTOS", json.dumps(produtos, ensure_ascii=False, indent=2)[:2500])
    print("VISITANTES_DIA", len(j.get("visitantesDia") or []))
    print("EVOLUCAO_DIA", len(j.get("evolucaoDia") or []))
    print("DISPOSITIVOS", json.dumps(j.get("dispositivos") or [], ensure_ascii=False)[:1500])
    print("CUPOM", json.dumps(j.get("cupomCashback") or [], ensure_ascii=False)[:1500])

    vivo = capturado["aovivo"] or {}
    ev = (vivo.get("json") or {}).get("eventos") or []
    print("AOVIVO_URL", vivo.get("url"), "status", vivo.get("status"), "n", len(ev))
    print("AOVIVO", json.dumps(ev[:15], ensure_ascii=False, indent=2)[:3000])

    seg = capturado["seg"] or {}
    print("SEG_URL", seg.get("url"), "status", seg.get("status"))
    linhas = (seg.get("json") or {}).get("linhas") or []
    print("SEG", json.dumps(linhas[:12], ensure_ascii=False, indent=2)[:2500])
    print("TELA", page.inner_text("body")[:1500])
    return capturado


def gerar_visita_publica(page):
    """Abre o cardápio público para o ao vivo não ficar só com evento antigo."""
    page.goto("https://menu.beefood.com.br/beefood3", wait_until="domcontentloaded")
    after_click(page, 6000)
    print("   visita pública ok", page.url)


def abrir_pixel(page):
    page.goto(URL, wait_until="domcontentloaded")
    after_click(page, 6000)
    limpar_tela(page)
    tema_claro(page)
    # Garantir período amplo: o DateRangePicker já vem com 7 dias.
    # Se a tela tiver inputs de data, tentamos o atalho via recarregar
    # com o período já aplicado pelo próprio componente (padrão 7 dias).
    # Para o manual, 7 dias recentes + o diagnóstico de junho→hoje bastam.
    page.wait_for_selector("text=BeeFood Pixel Analytics", timeout=20000)
    after_click(page, 5000)


def cap_menu(page):
    page.goto("https://beefood.app/", wait_until="domcontentloaded")
    after_click(page, 4000)
    limpar_tela(page)
    tema_claro(page)
    # Abrir o grupo Food Marketing no menu se estiver fechado
    fm = page.locator("text=Food Marketing").first
    if fm.count():
        try:
            fm.click(timeout=2000)
            after_click(page, 1500)
        except Exception:
            pass
    esconder_ao_vivo(page, True)
    tirar(page, "01-menu-food-marketing.png")


def cap_filtros(page):
    abrir_pixel(page)
    esconder_ao_vivo(page, True)
    # Clip do topo (título + filtros). Screenshot da viewport já cobre.
    tirar(page, "02-filtros-topo.png")


def cap_funil_colunas(page):
    abrir_pixel(page)
    esconder_ao_vivo(page, True)
    # Modo colunas é o padrão. Clicar no botão se estiver no outro.
    btn = page.locator("button", has_text="Colunas")
    if btn.count():
        btn.first.click()
        after_click(page, 2000)
    tirar(page, "03-funil-colunas.png")


def cap_funil_classico(page):
    abrir_pixel(page)
    esconder_ao_vivo(page, True)
    btn = page.locator("button", has_text="Funil")
    if btn.count():
        btn.first.click()
        after_click(page, 2500)
    tirar(page, "04-funil-classico.png")
    # voltar para colunas para o resto
    page.locator("button", has_text="Colunas").first.click()
    after_click(page, 1000)


def cap_kpis(page):
    abrir_pixel(page)
    esconder_ao_vivo(page, True)
    alvo = page.get_by_text("Receita total", exact=True)
    if alvo.count():
        alvo.first.scroll_into_view_if_needed()
        after_click(page, 2000)
    tirar(page, "05-kpis-resumo.png")


def cap_aovivo(page):
    gerar_visita_publica(page)
    abrir_pixel(page)
    esconder_ao_vivo(page, False)
    # Abrir o painel (pílula "Ao vivo")
    pill = page.locator("button", has_text="Ao vivo")
    if pill.count():
        pill.last.click()
        after_click(page, 2000)
    tirar(page, "06-ao-vivo.png")


def cap_ajuda(page):
    abrir_pixel(page)
    esconder_ao_vivo(page, True)
    page.locator("button", has_text="Saiba como funciona").first.click()
    after_click(page, 2000)
    tirar(page, "07-como-funciona.png")
    page.keyboard.press("Escape")
    page.wait_for_timeout(800)


def cap_segmentacao(page):
    abrir_pixel(page)
    esconder_ao_vivo(page, True)
    alvo = page.get_by_text("Segmentação", exact=False)
    if alvo.count():
        alvo.first.scroll_into_view_if_needed()
        after_click(page, 3000)
    tirar(page, "08-segmentacao.png")


ETAPAS = {
    "visita": gerar_visita_publica,
    "menu": cap_menu,
    "filtros": cap_filtros,
    "funil": cap_funil_colunas,
    "classico": cap_funil_classico,
    "kpis": cap_kpis,
    "aovivo": cap_aovivo,
    "ajuda": cap_ajuda,
    "segmentacao": cap_segmentacao,
}


def main():
    pedidos = sys.argv[1:] or ["diag", *ETAPAS]
    with sync_playwright() as p:
        browser = p.chromium.launch(
            env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"}
        )
        args = dict(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=1.5,
            locale="pt-BR",
            timezone_id="America/Sao_Paulo",
        )
        if STATE.exists():
            args["storage_state"] = str(STATE)
        ctx = browser.new_context(**args)
        page = ctx.new_page()
        login(page)
        tema_claro(page)
        if "diag" in pedidos:
            print("== diag")
            diagnosticar(page)
            pedidos = [x for x in pedidos if x != "diag"]
        for nome in pedidos:
            if nome not in ETAPAS:
                print("etapa desconhecida:", nome)
                continue
            print("==", nome)
            ETAPAS[nome](page)
        ctx.storage_state(path=str(STATE))
        browser.close()


if __name__ == "__main__":
    main()
