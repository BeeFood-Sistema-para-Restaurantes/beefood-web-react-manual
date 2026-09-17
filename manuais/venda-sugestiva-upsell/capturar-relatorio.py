#!/usr/bin/env python3
"""Captura #103 — relatório Desempenho → Delivery/Presencial → Sugestões.

    python capturar-relatorio.py delivery presencial

A tela de Desempenho é um iframe de `relatorios.beefood.com.br` dentro do painel;
as respostas de `relatorioSugestao` são impressas para conferência.
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
STATE = Path("/tmp/bf3-auth.json")
WAIT = 5000
LOGIN_EMAIL = "contato@beefood.com.br"
LOGIN_SENHA = "1q2w3e4r"


def after_click(page, extra_ms: int = WAIT):
    page.wait_for_timeout(extra_ms)


def limpar(page):
    page.add_style_tag(content="div.fixed.bottom-6 { display:none !important }")
    nps = page.locator('[role="dialog"]').filter(has_text="Como está sendo sua experiência")
    if nps.count():
        b = nps.last.get_by_role("button", name="FECHAR")
        if b.count():
            try:
                b.click(timeout=1500)
            except Exception:
                pass
    d = page.locator('button[aria-label="Dispensar"]')
    if d.count():
        try:
            d.first.click(timeout=1200)
        except Exception:
            pass


def login(page, ctx):
    page.goto("https://beefood.app/", wait_until="domcontentloaded")
    after_click(page)
    if page.locator("input#emailOrWhatsapp").count():
        page.fill("input#emailOrWhatsapp", LOGIN_EMAIL)
        page.fill("input#password", LOGIN_SENHA)
        page.get_by_role("button", name="ENTRAR").click()
        after_click(page, 9000)
        ctx.storage_state(path=str(STATE))
    classes = page.locator("html").get_attribute("class") or ""
    if "dark" in classes:
        alvo = page.locator('span.sr-only:has-text("Alterar tema")')
        if alvo.count():
            alvo.first.locator("xpath=ancestor::button").first.click()
            page.wait_for_timeout(800)
    limpar(page)


def frame_relatorios(page):
    for _ in range(20):
        for f in page.frames:
            if "relatorios.beefood.com.br" in (f.url or ""):
                return f
        page.wait_for_timeout(1500)
    raise RuntimeError("iframe de relatórios não carregou")


def periodo(page, f, preset: str):
    """Troca o intervalo do relatório por um dos atalhos do calendário."""
    botao = [t.strip() for t in f.locator("button").all_inner_texts() if "/2026" in t]
    if not botao:
        print("  não achei o botão de período")
        return
    f.get_by_role("button", name=botao[0]).first.click()
    page.wait_for_timeout(2500)
    f.get_by_role("button", name=preset, exact=True).first.click()
    page.wait_for_timeout(2500)
    confirmar = f.get_by_role("button", name="Confirmar")
    if confirmar.count():
        confirmar.first.click()
    page.wait_for_timeout(12000)
    print("  período:", [t.strip() for t in f.locator("button").all_inner_texts() if "/2026" in t])


def abrir(page, canal: str, arquivo: str, preset: str | None = None):
    page.goto("https://beefood.app/desempenho", wait_until="domcontentloaded")
    after_click(page, 12000)
    limpar(page)
    f = frame_relatorios(page)
    print("  frame:", f.url[:90])
    f.get_by_text(canal, exact=True).first.click()
    page.wait_for_timeout(6000)
    f.get_by_text("Sugestões", exact=True).first.click()
    page.wait_for_timeout(12000)
    if preset:
        periodo(page, f, preset)
    titulo = f.locator("h2").first.inner_text() if f.locator("h2").count() else "?"
    print("  título:", titulo)
    page.screenshot(path=str(PURA / arquivo), type="png")
    print("  SHOT", arquivo)

    # segunda foto: as listas de mais sugeridos, que ficam abaixo do gráfico.
    # O relatório rola DENTRO do iframe — `scroll_into_view_if_needed` não mexe nele.
    page.mouse.move(1000, 600)
    for _ in range(3):
        page.mouse.wheel(0, 220)
        page.wait_for_timeout(300)
    page.mouse.move(80, 700)  # tira o ponteiro do gráfico, senão o tooltip aparece no print
    page.wait_for_timeout(WAIT)
    rolado = arquivo.replace(".png", "-listas.png")
    page.screenshot(path=str(PURA / rolado), type="png")
    print("  SHOT", rolado)
    return f


def main():
    etapas = sys.argv[1:] or ["delivery"]
    with sync_playwright() as p:
        nav = p.chromium.launch(env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"})
        ctx = nav.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=1.5,
            locale="pt-BR",
            timezone_id="America/Sao_Paulo",
            storage_state=str(STATE) if STATE.exists() else None,
        )
        page = ctx.new_page()

        def on_resp(r):
            if "relatorioSugestao" in r.url:
                try:
                    dados = r.json()
                except Exception:
                    return
                n = len(dados) if isinstance(dados, list) else 0
                print("  relatorioSugestao", r.url.split("relatorioSugestao")[-1], "->", n, "linhas")
                if n:
                    Path(f"/tmp/sugestao-{r.url[-1]}.json").write_text(json.dumps(dados, ensure_ascii=False))
                    for x in dados[-6:]:
                        print("     ", x.get("dataVenda"), x.get("numeroPreVenda"), x.get("descricao"),
                              x.get("qtd"), x.get("vendaUnt"), "| origem:", x.get("origem"))

        page.on("response", on_resp)
        login(page, ctx)

        preset = os.environ.get("PERIODO") or None
        if "delivery" in etapas:
            print("== delivery")
            abrir(page, "Delivery", "09-relatorio-delivery.png", preset)
        if "presencial" in etapas:
            print("== presencial")
            abrir(page, "Presencial", "10-relatorio-presencial.png", preset)

        ctx.close()
        nav.close()


if __name__ == "__main__":
    main()
