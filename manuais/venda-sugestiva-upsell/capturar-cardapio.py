#!/usr/bin/env python3
"""Captura #103 — a Venda Sugestiva no cardápio digital (celular 390×844, DPR 2).

    python capturar-cardapio.py delivery          # tira do delivery (sem pedir)
    python capturar-cardapio.py presencial        # tira do presencial (sem pedir)
    DRY=0 python capturar-cardapio.py pedido      # gera pedido de verdade (relatório)

O sandbox BeeFood3 é ambiente de teste: pode fechar pedido.
Combo One Burger sugere Anéis de Cebola Empanada, Milk Shake de Morango,
Brownie e Pudim - Leite Condensado (configurado no painel).
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

DIR = Path(__file__).resolve().parent
PURA = DIR / "imagens-puras"
PURA.mkdir(exist_ok=True)
MENU_D = "https://menu.beefood.com.br/beefood3"
MENU_P = "https://menu.beefood.com.br/beefood3/?tipo=p"
PRODUTO = "Combo One Burger"
SUGESTAO = "Milk Shake de Morango"
TEL = "15999998888"
DRY = os.environ.get("DRY", "1") == "1"


def after(page, ms=2500):
    page.wait_for_timeout(ms)


def shot(page, nome):
    destino = PURA / nome
    page.screenshot(path=str(destino), type="png")
    print("   SHOT", destino.name, destino.stat().st_size)


def fechar_overlays(page):
    page.keyboard.press("Escape")
    after(page, 300)
    page.evaluate(
        """() => {
          const textos = ['Dispensar', 'Agora não', 'Entendi'];
          for (const t of textos) {
            const el = Array.from(document.querySelectorAll('button, [role=button]'))
              .find(e => (e.innerText||'').trim() === t);
            if (el) el.click();
          }
        }"""
    )
    after(page, 400)


def escolher_obrigatorios(page):
    """Marca 1 opção nos grupos que ainda mostram OBRIGATÓRIO.

    O primeiro grupo do combo já vem pré-selecionado; clicar nele desmarca.
    """
    grupos = page.locator(".group-section")
    for i in range(grupos.count()):
        g = grupos.nth(i)
        cab = g.locator(".group-header").first
        if "OBRIGAT" not in cab.inner_text().upper():
            continue
        item = g.locator(".option-item").first
        if not item.count():
            continue
        item.scroll_into_view_if_needed()
        after(page, 500)
        b = item.bounding_box()
        if b:
            page.mouse.click(b["x"] + b["width"] - 18, b["y"] + b["height"] / 2)
            after(page, 700)
            print("   opção:", item.locator(".option-title-text").first.inner_text().strip())


def adicionar_produto(page, nome: str):
    alvo = page.get_by_text(nome, exact=True).first
    alvo.scroll_into_view_if_needed()
    after(page, 600)
    alvo.click()
    after(page, 3500)
    escolher_obrigatorios(page)
    botao = page.locator("button:has-text('Adicionar')").last
    print("   botão:", botao.inner_text().replace("\n", " "))
    botao.click()
    after(page, 4500)


def clicar_continuar(page):
    btn = page.get_by_role("button", name="Continuar")
    if not btn.count():
        return False
    alvo = btn.last
    try:
        alvo.scroll_into_view_if_needed()
    except Exception:
        pass
    b = alvo.bounding_box()
    if b:
        page.mouse.click(b["x"] + b["width"] / 2, b["y"] + b["height"] / 2)
        after(page, 2500)
        return True
    return False


def clicar_texto(page, texto, exact=False):
    loc = page.get_by_text(texto, exact=exact)
    for i in range(loc.count()):
        el = loc.nth(i)
        try:
            if not el.is_visible():
                continue
            b = el.bounding_box()
            if not b or b["y"] < 40 or b["y"] > 800:
                continue
            page.mouse.click(b["x"] + min(40, b["width"] / 2), b["y"] + b["height"] / 2)
            after(page, 1800)
            print("   clique:", texto)
            return True
        except Exception:
            continue
    return False


def fluxo_sugestao(page, url, prefixo, sugestao=SUGESTAO):
    """Adiciona o produto, fotografa a sugestão, aceita e fotografa a sacola."""
    page.goto(url, wait_until="domcontentloaded")
    after(page, 9000)
    fechar_overlays(page)

    adicionar_produto(page, PRODUTO)
    if not page.locator(".modal-upsell").count():
        raise RuntimeError("a janela de sugestão não abriu")
    print("   sugestão:", page.locator(".modal-upsell").first.inner_text().replace("\n", " | ")[:200])
    shot(page, f"{prefixo}-sugestao.png")

    page.locator(".modal-upsell").locator(f"text={sugestao}").first.click()
    after(page, 3500)
    shot(page, f"{prefixo}-produto-sugerido.png")

    page.locator("button:has-text('Adicionar')").last.click()
    after(page, 4000)

    if page.get_by_text("Ver sacola").count():
        page.get_by_text("Ver sacola").first.click()
    else:
        clicar_texto(page, "Ver sacola")
    after(page, 3500)
    shot(page, f"{prefixo}-sacola.png")
    print("   sacola:", page.locator(".v-dialog--active").first.inner_text().replace("\n", " | ")[:300]
          if page.locator(".v-dialog--active").count() else "")


def fechar_pedido_delivery(page, prefixo):
    """Sacola → WhatsApp → retirada → dinheiro → Finalizar."""
    clicar_continuar(page)
    after(page, 1500)
    inp = page.locator("input[type=tel]").last
    if inp.count():
        b = inp.bounding_box()
        if b:
            page.mouse.click(b["x"] + b["width"] / 2, b["y"] + b["height"] / 2)
            after(page, 300)
        page.keyboard.type(TEL, delay=40)
        after(page, 600)
    clicar_continuar(page)
    after(page, 1800)
    clicar_texto(page, "Retirar no estabelecimento")
    clicar_continuar(page)
    after(page, 1800)
    clicar_texto(page, "Outras formas de pagamento")
    after(page, 800)
    clicar_texto(page, "Dinheiro")
    after(page, 800)
    if not clicar_texto(page, "NÃO QUERO TROCO"):
        page.get_by_role("button", name="NÃO QUERO TROCO").last.click()
    after(page, 2000)
    if not clicar_texto(page, "Finalizar"):
        page.get_by_role("button", name="Finalizar").last.click()
    after(page, 6000)
    shot(page, f"{prefixo}-pedido-fim.png")
    txt = page.inner_text("body")[:600].replace("\n", " | ")
    print("   fim:", txt)


def contexto(nav):
    return nav.new_context(
        viewport={"width": 390, "height": 844},
        device_scale_factor=2,
        is_mobile=True,
        has_touch=True,
        locale="pt-BR",
        timezone_id="America/Sao_Paulo",
        extra_http_headers={"Accept-Language": "pt-BR,pt;q=0.9"},
    )


def main():
    etapas = sys.argv[1:] or ["delivery", "presencial"]
    with sync_playwright() as p:
        nav = p.chromium.launch(env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"})

        if "delivery" in etapas:
            print("== delivery")
            ctx = contexto(nav)
            page = ctx.new_page()
            fluxo_sugestao(page, MENU_D, "07-delivery")
            ctx.close()

        if "presencial" in etapas:
            print("== presencial")
            ctx = contexto(nav)
            page = ctx.new_page()
            # Brownie está oculto no cardápio digital (tabela Ocultar do #68) e,
            # por isso, nem aparece na janela de sugestão.
            fluxo_sugestao(page, MENU_P, "08-presencial", sugestao=SUGESTAO)
            ctx.close()

        if "pedido" in etapas:
            print("== pedido de verdade (delivery)")
            ctx = contexto(nav)
            page = ctx.new_page()
            page.on(
                "request",
                lambda r: Path("/tmp/post-pedido.json").write_text(r.post_data or "")
                if r.method == "POST" and "venda" in r.url.lower()
                else None,
            )
            fluxo_sugestao(page, MENU_D, "90-pedido")
            if DRY:
                print("   DRY: não fechou o pedido")
            else:
                fechar_pedido_delivery(page, "90-pedido")
            ctx.close()

        nav.close()


if __name__ == "__main__":
    main()
