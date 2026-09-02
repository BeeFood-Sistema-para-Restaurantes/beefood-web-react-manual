"""Gera visitas e pedidos no cardápio com URLs fake de anúncio.

Cada campanha usa um contexto Playwright novo (sessão/UTM isolados).
Combo One Burger + Batata frita + Coca 350ml = R$ 39.
Retirada + telefone 15999998888 + Dinheiro.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = Path("/tmp/pixel-pedidos")
OUT.mkdir(exist_ok=True)
MENU = "https://menu.beefood.com.br/beefood3"
TEL = "15999998888"

CAMPANHAS = [
    {
        "nome": "google-ads",
        "comprar": True,
        "url": (
            f"{MENU}?utm_source=google&utm_medium=cpc"
            "&utm_campaign=manual-google-ads"
            "&utm_content=anuncio-pesquisa-combo"
            "&utm_term=hamburguer+delivery+sorocaba"
            "&gclid=TwManualGclidGoogle001"
        ),
    },
    {
        "nome": "facebook-ads",
        "comprar": True,
        "url": (
            f"{MENU}?utm_source=facebook&utm_medium=paid"
            "&utm_campaign=manual-meta-feed"
            "&utm_content=criativo-combo-one"
            "&fbclid=TwManualFbclid001"
        ),
    },
    {
        "nome": "instagram-ads",
        "comprar": True,
        "url": (
            f"{MENU}?utm_source=instagram&utm_medium=paid"
            "&utm_campaign=manual-ig-stories"
            "&utm_content=stories-fim-de-semana"
        ),
    },
    {
        "nome": "tiktok-ads",
        "comprar": True,
        "url": (
            f"{MENU}?utm_source=tiktok&utm_medium=paid"
            "&utm_campaign=manual-tt-video"
            "&utm_content=video-lanche"
        ),
    },
    {
        "nome": "youtube-ads",
        "comprar": False,
        "url": (
            f"{MENU}?utm_source=youtube&utm_medium=cpc"
            "&utm_campaign=manual-yt-instream"
            "&utm_content=pre-roll-combo"
        ),
    },
    {
        "nome": "kwai-ads",
        "comprar": False,
        "url": (
            f"{MENU}?utm_source=kwai&utm_medium=paid"
            "&utm_campaign=manual-kwai-clip"
        ),
    },
]


def after(page, ms=2500):
    page.wait_for_timeout(ms)


def shot(page, nome):
    page.screenshot(path=str(OUT / f"{nome}.png"), type="png")
    print("   shot", nome)


def attrib(page):
    raw = page.evaluate("() => localStorage.getItem('beefood_pixel_attrib')")
    print("   attrib", (raw or "")[:280])
    return raw


def dump(page, etapa):
    txt = page.inner_text("body")
    print(f"   [{etapa}]", txt[:600].replace("\n", " | "))
    return txt


def pick_option(page, name):
    item = page.locator(".option-item").filter(
        has=page.locator(".option-title-text", has_text=name)
    ).first
    item.scroll_into_view_if_needed()
    after(page, 400)
    box = item.bounding_box()
    if not box:
        raise RuntimeError(f"sem box para {name}")
    page.mouse.click(box["x"] + box["width"] - 18, box["y"] + box["height"] / 2)
    after(page, 500)
    print("   pick", name)


def fechar_overlays(page):
    page.keyboard.press("Escape")
    after(page, 200)
    page.evaluate(
        """() => {
          const textos = ['Dispensar', 'Fechar', 'FECHAR', 'Agora não', 'Entendi'];
          for (const t of textos) {
            const el = Array.from(document.querySelectorAll('button, [role=button]'))
              .find(e => (e.innerText||'').trim() === t);
            if (el) el.click();
          }
        }"""
    )
    after(page, 300)


def click_continuar_rodape(page):
    """Clica o botão vermelho Continuar do rodapé (não o texto da home)."""
    btn = page.get_by_role("button", name="Continuar")
    n = btn.count()
    print("   continuar role count", n)
    if n:
        alvo = btn.last
        try:
            alvo.scroll_into_view_if_needed()
        except Exception:
            pass
        after(page, 200)
        box = alvo.bounding_box()
        print("   continuar box", box)
        if box:
            page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
            after(page, 2200)
            print("   click Continuar (mouse)")
            return True
        try:
            alvo.click(timeout=2500, force=True)
            after(page, 2200)
            print("   click Continuar (force)")
            return True
        except Exception as e:
            print("   click Continuar falhou", str(e).split("\n")[0][:120])
    # fallback: centro inferior do viewport
    vp = page.viewport_size or {"width": 390, "height": 844}
    page.mouse.click(vp["width"] / 2, vp["height"] - 90)
    after(page, 2200)
    print("   click Continuar (fallback y)")
    return True


def preencher_telefone(page):
    """O input visível é type=tel dentro do diálogo. input.first é um campo readonly da home."""
    inp = page.locator("input[type=tel]").last
    if not inp.count():
        print("   sem input tel")
        return False
    try:
        atual = (inp.input_value() or "")
    except Exception:
        atual = ""
    digits = "".join(c for c in atual if c.isdigit())
    if len(digits) >= 10:
        print("   tel já tinha", atual)
        return True
    box = inp.bounding_box()
    if box:
        page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
        after(page, 250)
    page.keyboard.type(TEL, delay=40)
    after(page, 500)
    print("   tel preenchido", inp.input_value())
    return True


def pedido_sucesso(texto: str) -> bool:
    t = texto.lower()
    if any(x in t for x in ("pedido recebido", "recebemos o seu pedido", "pedido confirmado", "pedido enviado")):
        return True
    if "nº" in t or "n°" in t:
        return True
    if "acompanhe" in t and "pedido" in t:
        return True
    return False


def click_texto_visivel(page, texto, exact=False):
    loc = page.get_by_text(texto, exact=exact)
    n = loc.count()
    for i in range(n):
        el = loc.nth(i)
        try:
            if not el.is_visible():
                continue
            box = el.bounding_box()
            if not box or box["y"] < 50 or box["y"] > 780:
                continue
            page.mouse.click(box["x"] + min(40, box["width"] / 2), box["y"] + box["height"] / 2)
            after(page, 1800)
            print("   click", texto)
            return True
        except Exception as e:
            print("   skip", texto, str(e).split("\n")[0][:80])
    return False


def click_botao_nome(page, nome):
    btn = page.get_by_role("button", name=nome)
    if not btn.count():
        return False
    box = btn.last.bounding_box()
    if not box:
        return False
    page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
    after(page, 2200)
    print("   click btn", nome)
    return True


def avancar_checkout(page, camp):
    """Sacola → WhatsApp → retirada → outras formas → dinheiro → sem troco → Finalizar."""
    click_continuar_rodape(page)
    after(page, 1200)
    shot(page, f"{camp['nome']}-04-whatsapp")

    preencher_telefone(page)
    click_continuar_rodape(page)
    after(page, 1500)
    shot(page, f"{camp['nome']}-05-modalidade")

    click_texto_visivel(page, "Retirar no estabelecimento")
    click_continuar_rodape(page)
    after(page, 1500)
    shot(page, f"{camp['nome']}-06-pagamento")

    click_texto_visivel(page, "Outras formas de pagamento")
    after(page, 800)
    click_texto_visivel(page, "Dinheiro")
    after(page, 800)
    shot(page, f"{camp['nome']}-07-troco")

    if not click_botao_nome(page, "NÃO QUERO TROCO"):
        click_texto_visivel(page, "NÃO QUERO TROCO")
    after(page, 1500)
    shot(page, f"{camp['nome']}-08-pag-ok")

    if not click_botao_nome(page, "Finalizar"):
        click_texto_visivel(page, "Finalizar")
    after(page, 5000)
    shot(page, f"{camp['nome']}-09-fim")

    vis = page.evaluate(
        """() => {
          const d = document.querySelector('.v-dialog--active, .v-dialog__content--active .v-dialog');
          return ((d && d.innerText) || document.body.innerText || '').slice(0, 1500);
        }"""
    )
    print("   FIM", (vis or "").replace("\n", " | ")[:800])
    ok = pedido_sucesso(vis or "")
    print("   resultado", "OK" if ok else "INDEFINIDO")
    return ok


def fluxo(page, camp):
    page.goto(camp["url"], wait_until="domcontentloaded")
    after(page, 7000)
    fechar_overlays(page)
    attrib(page)
    shot(page, f"{camp['nome']}-01-home")
    dump(page, "home")

    combo = page.get_by_text("Combo One Burger", exact=True)
    if not combo.count():
        # tenta o título parcial
        combo = page.locator("text=One Burger").first
        combo.scroll_into_view_if_needed()
        after(page, 400)
    else:
        combo.first.scroll_into_view_if_needed()
        after(page, 400)
    page.get_by_text("Combo One Burger", exact=True).first.click()
    after(page, 2500)
    page.wait_for_selector(".option-item", timeout=15000)
    pick_option(page, "Batata frita")
    pick_option(page, "Coca Cola 350ml")
    add = page.locator("button:has-text('Adicionar')").last
    print("   preco", add.inner_text().replace("\n", " "))
    add.click()
    after(page, 3000)
    shot(page, f"{camp['nome']}-02-add")

    if not camp["comprar"]:
        print("   parou no carrinho (sem pedido)")
        return True

    if not page.get_by_text("Ver sacola").count():
        raise RuntimeError("sacola não apareceu — combo não entrou")
    page.get_by_text("Ver sacola").first.click()
    after(page, 3500)
    shot(page, f"{camp['nome']}-03-sacola")
    dump(page, "sacola")

    return avancar_checkout(page, camp)


def main():
    nomes = sys.argv[1:] or [c["nome"] for c in CAMPANHAS]
    os.environ.setdefault("LANG", "pt_BR.UTF-8")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"}
        )
        resultados = {}
        for camp in CAMPANHAS:
            if camp["nome"] not in nomes:
                continue
            print("==", camp["nome"])
            ctx = browser.new_context(
                viewport={"width": 390, "height": 844},
                device_scale_factor=2,
                is_mobile=True,
                has_touch=True,
                locale="pt-BR",
                timezone_id="America/Sao_Paulo",
                extra_http_headers={"Accept-Language": "pt-BR,pt;q=0.9"},
            )
            page = ctx.new_page()
            try:
                resultados[camp["nome"]] = fluxo(page, camp)
            except Exception as e:
                print("ERRO", camp["nome"], e)
                resultados[camp["nome"]] = False
                try:
                    shot(page, f"{camp['nome']}-erro")
                    dump(page, "erro")
                except Exception:
                    pass
            ctx.close()
        browser.close()
        print("RESUMO", json.dumps(resultados, ensure_ascii=False))


if __name__ == "__main__":
    main()
