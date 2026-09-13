#!/usr/bin/env python3
"""Captura o Cupom Pedido de uma venda DELIVERY com bebida em destaque (#99).

    python capturar-delivery.py          # venda 936
    VENDA=957 python capturar-delivery.py

Padrão: venda 936 (02/09/2026, origem Cardápio Digital, R$ 37,05) —
Combo One Burger = One Burger + Batata frita + Coca Cola 350ml.
Reaproveita login, limpeza de tela e gancho do iframe do `capturar.py`.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from capturar import (  # noqa: E402
    STATE, after_click, instalar_gancho_cupom, limpar, limpar_cache_destaque,
    login, render_cupom, shot,
)
from playwright.sync_api import sync_playwright  # noqa: E402

ALVO = os.environ.get("VENDA", "936")


def main():
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
        for porta in ("http://localhost:1316/**", "http://localhost:1317/**",
                      "https://impressao.ngrok.app/**",
                      "https://impressao-cozinha.ngrok.app/**"):
            ctx.route(porta, lambda route: route.abort())
        page = ctx.new_page()
        login(page, ctx)

        page.goto("https://beefood.app/historico", wait_until="domcontentloaded")
        after_click(page, 8000)
        limpar(page)

        # A busca do histórico filtra por numeroPreVenda.
        page.locator('input[placeholder*="Buscar"]').first.fill(ALVO)
        after_click(page, 4000)

        alvo = None
        for tr in page.locator("table tbody tr").all():
            texto = (tr.inner_text() or "").replace("\n", " | ")
            if ALVO in texto:
                print("LINHA", texto[:220])
                alvo = tr
                break
        if alvo is None:
            raise RuntimeError(f"venda {ALVO} não encontrada na lista")

        botao = alvo.locator("button")
        (botao.first if botao.count() else alvo).click()
        after_click(page, 14000)
        limpar(page)

        limpar_cache_destaque(page)
        instalar_gancho_cupom(page)
        page.evaluate("() => { window.__cupomHTML = null; }")

        printer = page.locator('[role="dialog"] button').filter(
            has=page.locator("svg.lucide-printer"))
        if printer.count() == 0:
            printer = page.locator("button").filter(has=page.locator("svg.lucide-printer"))
        printer.first.click(force=True)

        html = None
        for _ in range(120):
            html = page.evaluate("() => window.__cupomHTML")
            if html:
                break
            page.wait_for_timeout(250)
        print("cupom delivery", "SIM" if html else "NAO", len(html or ""))
        if html:
            render_cupom(ctx, html, "07-cupom-delivery.png")
        else:
            print("body:", page.inner_text("body")[-600:])

        ctx.storage_state(path=str(STATE))
        browser.close()
    print("rode o annotate.py para regerar imagens-tratadas")


if __name__ == "__main__":
    main()
