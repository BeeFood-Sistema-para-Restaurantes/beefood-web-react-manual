"""Faz um pedido de DELIVERY no cardápio público da sandbox e registra o que ele envia.

Serve a duas coisas do #120:

1. dar ao painel pedidos com origem **Cardápio Digital** de verdade (o
   `venda2/salvar` do painel grava sempre `origem = Manual`);
2. mostrar qual rota o cardápio usa e com que corpo — é ela que decide a origem,
   e é isso que o estudo do banco precisava responder.

    python pedido_cardapio.py            # um pedido
    python pedido_cardapio.py 3          # três pedidos seguidos

Combo de teste: One Burger + Batata frita + Coca 350ml. Telefone de teste
15999998888 (cliente Teste Manual). Modalidade **Entrega**, porque o painel só
mostra `tipoPedido = DELIVERY`.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = Path("/tmp/painel-entregador-pedidos")
OUT.mkdir(exist_ok=True)
MENU = "https://menu.beefood.com.br/beefood3"
TEL = "15999998888"
# A área de entrega da sandbox é por bairro e só tem o Centro cadastrado.
BAIRRO = "Centro"
RUA = "Rua Barão de Piratininga"
NUMERO = "120"
CEP = "18010250"

# Combos do cardápio da sandbox, alternados para os cartões não saírem iguais.
COMBOS = [
    ("Combo One Burger", "Batata frita", "Coca Cola 350ml"),
    ("Combo Crispy Bbq", "Batata frita com cheddar e bacon", "Coca Zero 350ml"),
    ("Combo Chicken Deluxe", "Anéis de Cebola Empanada", "Coca Cola 350ml"),
    ("Combo One Cheddar", "Batata frita", "Coca Zero 350ml"),
]


def after(page, ms=2500):
    page.wait_for_timeout(ms)


def shot(page, nome):
    page.screenshot(path=str(OUT / f"{nome}.png"), type="png")
    print("   shot", nome)


def dump(page, etapa, n=500):
    txt = page.inner_text("body")
    print(f"   [{etapa}]", txt[:n].replace("\n", " | "))
    return txt


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
    print("   opcao", name)


def click_continuar_rodape(page):
    btn = page.get_by_role("button", name="Continuar")
    if btn.count():
        alvo = btn.last
        try:
            alvo.scroll_into_view_if_needed()
        except Exception:
            pass
        after(page, 200)
        box = alvo.bounding_box()
        if box:
            page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
            after(page, 2200)
            return True
    vp = page.viewport_size or {"width": 390, "height": 844}
    page.mouse.click(vp["width"] / 2, vp["height"] - 90)
    after(page, 2200)
    return True


def click_texto_visivel(page, texto, exact=False):
    loc = page.get_by_text(texto, exact=exact)
    for i in range(loc.count()):
        el = loc.nth(i)
        try:
            if not el.is_visible():
                continue
            box = el.bounding_box()
            if not box or box["y"] < 50 or box["y"] > 800:
                continue
            page.mouse.click(box["x"] + min(40, box["width"] / 2), box["y"] + box["height"] / 2)
            after(page, 1800)
            print("   click", texto)
            return True
        except Exception:
            continue
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


def preencher_telefone(page):
    inp = page.locator("input[type=tel]").last
    if not inp.count():
        return False
    try:
        atual = inp.input_value() or ""
    except Exception:
        atual = ""
    if len("".join(c for c in atual if c.isdigit())) >= 10:
        return True
    box = inp.bounding_box()
    if box:
        page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
        after(page, 250)
    page.keyboard.type(TEL, delay=40)
    after(page, 600)
    print("   telefone", inp.input_value())
    return True


def dialogo(page, etapa: str, n: int = 1400) -> str:
    """O texto do diálogo ativo. `inner_text('body')` devolve o cardápio de trás."""
    txt = page.evaluate(
        """() => Array.from(document.querySelectorAll('.v-dialog__content--active .v-dialog'))
                     .map(d => d.innerText).join('\\n---\\n')"""
    )
    print(f"   [{etapa}]", (txt or "(sem dialog)").replace("\n", " | ")[:n])
    return txt or ""


def escolher_entrega(page, indice: int):
    """Modalidade *Receber no seu endereço* + endereço no bairro da área de entrega.

    A área de entrega da sandbox é **por bairro** e só tem o **Centro** cadastrado:
    buscar qualquer outro bairro devolve "Nenhum resultado encontrado".
    """
    texto_modalidade = dialogo(page, "modalidade")
    click_texto_visivel(page, "Receber no seu endereço")
    after(page, 800)

    # Do segundo pedido em diante o endereço já está salvo no cliente e a sacola
    # mostra "Trocar" em vez do convite para informar o endereço.
    if RUA.split()[-1] in texto_modalidade or "Trocar" in texto_modalidade:
        print("   endereço já salvo — segue direto")
        click_continuar_rodape(page)
        after(page, 2500)
        return True

    if not click_texto_visivel(page, "Clique aqui e informe o endereço"):
        return False
    after(page, 2500)

    campo = page.locator('input[placeholder="Digite seu Bairro"]').last
    if not campo.count():
        dialogo(page, "sem-campo-bairro")
        return False
    campo.click()
    page.keyboard.type(BAIRRO, delay=80)
    after(page, 4000)
    dialogo(page, "bairros")
    if not click_texto_visivel(page, BAIRRO, exact=True):
        return False
    after(page, 3000)
    shot(page, f"{indice}-endereco-campos")
    dialogo(page, "campos-endereco")

    # O formulário NOVO ENDEREÇO não usa placeholder: os rótulos são elementos
    # separados, então os campos vazios são preenchidos por posição —
    # 0 Endereço, 1 Número, 2 CEP (bairro, cidade e estado já vêm preenchidos).
    texto = page.locator(".v-dialog__content--active input:visible")
    editaveis = [
        texto.nth(i) for i in range(texto.count())
        if texto.nth(i).get_attribute("type") not in ("radio", "checkbox")
    ]
    for campo, valor in zip(editaveis, (RUA, NUMERO, CEP)):
        campo.click()
        page.keyboard.type(valor, delay=40)
        after(page, 400)
    print("   endereço preenchido:", [c.input_value() for c in editaveis])

    if not click_botao_nome(page, "Salvar endereço"):
        click_texto_visivel(page, "Salvar endereço")
    after(page, 3500)
    dialogo(page, "depois-endereco")
    click_continuar_rodape(page)
    after(page, 2500)
    return True


def fechar_upsell(page):
    """A venda sugestiva (#103) abre sozinha ao pôr item na sacola e tapa o 'Ver sacola'."""
    modal = page.locator(".modal-upsell")
    if not modal.count():
        return
    print("   upsell:", modal.first.inner_text().replace("\n", " | ")[:200])
    for seletor in (
        ".modal-upsell button:has-text('Não')",
        ".modal-upsell button:has-text('NÃO')",
        ".modal-upsell button:has-text('Continuar')",
        ".modal-upsell button:has-text('Fechar')",
        ".modal-upsell .v-icon",
        ".modal-upsell__fechar",
    ):
        alvo = page.locator(seletor)
        if alvo.count():
            try:
                alvo.last.click(timeout=2000)
                after(page, 1200)
                if not page.locator(".modal-upsell").count():
                    print("   upsell fechado por", seletor)
                    return
            except Exception:
                pass
    page.keyboard.press("Escape")
    after(page, 1000)
    print("   upsell ainda aberto?", bool(page.locator(".modal-upsell").count()))


def fluxo(page, indice: int):
    page.goto(MENU, wait_until="domcontentloaded")
    after(page, 7000)
    fechar_overlays(page)
    shot(page, f"{indice}-01-home")

    combo, acompanhamento, bebida = COMBOS[(indice - 1) % len(COMBOS)]
    print("   combo", combo, "+", acompanhamento, "+", bebida)
    page.get_by_text(combo, exact=True).first.scroll_into_view_if_needed()
    after(page, 400)
    page.get_by_text(combo, exact=True).first.click()
    after(page, 2500)
    page.wait_for_selector(".option-item", timeout=15000)
    pick_option(page, acompanhamento)
    pick_option(page, bebida)
    page.locator("button:has-text('Adicionar')").last.click()
    after(page, 3000)
    fechar_upsell(page)

    # Fechar a sugestão já deixa a sacola aberta; clicar em "Ver sacola" seria
    # intercept pointer events pelo próprio diálogo.
    if not page.locator(".cart-content-scroll").count():
        page.get_by_text("Ver sacola").first.click()
        after(page, 3500)
    shot(page, f"{indice}-02-sacola")

    click_continuar_rodape(page)
    after(page, 1200)
    preencher_telefone(page)
    click_continuar_rodape(page)
    after(page, 1800)

    if not escolher_entrega(page, indice):
        print("   NAO consegui escolher Entrega — parando antes de finalizar")
        shot(page, f"{indice}-erro-endereco")
        return False
    shot(page, f"{indice}-03-pagamento")
    dialogo(page, "pagamento")

    click_texto_visivel(page, "Outras formas de pagamento")
    after(page, 800)
    click_texto_visivel(page, "Dinheiro")
    after(page, 800)
    if not click_botao_nome(page, "NÃO QUERO TROCO"):
        click_texto_visivel(page, "NÃO QUERO TROCO")
    after(page, 1500)

    if not click_botao_nome(page, "Finalizar"):
        click_texto_visivel(page, "Finalizar")
    after(page, 6000)
    shot(page, f"{indice}-04-fim")
    txt = dump(page, "fim", 900)
    baixo = txt.lower()
    ok = any(x in baixo for x in (
        "detalhes do pedido", "pedido enviado para o restaurante",
        "pedido recebido", "recebemos o seu pedido",
    ))
    print("   resultado", "OK" if ok else "INDEFINIDO")
    return ok


def main():
    quantos = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    with sync_playwright() as p:
        browser = p.chromium.launch(env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"})
        for i in range(1, quantos + 1):
            print(f"== pedido {i}/{quantos}")
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

            # Registra o que o cardápio manda: é a rota que decide a origem do pedido.
            def on_request(req):
                if req.method in ("POST", "PUT") and "beetechapi" in req.url:
                    corpo = (req.post_data or "")[:1200]
                    print("   >>", req.method, req.url)
                    print("      ", corpo)

            page.on("request", on_request)
            try:
                fluxo(page, i)
            except Exception as e:
                print("ERRO", e)
                try:
                    shot(page, f"{i}-erro")
                    dump(page, "erro", 900)
                except Exception:
                    pass
            ctx.close()
        browser.close()


if __name__ == "__main__":
    main()
