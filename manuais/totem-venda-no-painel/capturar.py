#!/usr/bin/env python3
"""Captura #123 — O pedido do totem no painel.

    python3 capturar.py ensaio           # roda o pedido inteiro e PARA no pagamento
    VALENDO=1 python3 capturar.py pedido # fecha o pedido de verdade, em Dinheiro
    python3 capturar.py delivery historico desempenho

A técnica do ensaio (MEMORIA-GERAL, seção 7): `ensaio` percorre o mesmo caminho do
`pedido` e para antes do clique que grava. Sem `VALENDO=1`, o `pedido` também para —
o clique final só sai com a variável ligada, para não gravar venda por engano.

O pedido é pago em **Dinheiro** (a aba Pagamentos do totem tem Dinheiro ligado), que
é o único meio que fecha sem pinpad. A NFC-e está desligada no sandbox.
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
TOTEM_URL = ("https://totem.beefood.app/?empresaID=38311&filialID=39202"
             "&token=D3590976-63A1-4FDF-9721-0E054CBF3BB5")
TELEFONE = "15999998888"
MESA = "12"
ESCONDE_FLUTUANTE = """
  div.fixed.bottom-6, a[href*="wa.me"], iframe[title*="WhatsApp"] { display: none !important }
"""


def after_click(page, extra_ms: int = WAIT):
    for _ in range(30):
        ocupado = (page.locator("text=Carregando...").count()
                   or page.locator("text=Atualizando...").count()
                   or page.locator("text=Calculando").count())
        if not ocupado:
            break
        page.wait_for_timeout(1000)
    page.wait_for_timeout(extra_ms)


def limpar(page):
    page.add_style_tag(content=ESCONDE_FLUTUANTE)
    page.evaluate("""() => {
      for (const e of document.querySelectorAll('div[class*="fixed"]')) {
        const r = e.getBoundingClientRect();
        if (r.width < 120 && r.height < 120 && r.bottom > innerHeight - 160)
          e.style.display = 'none';
      }
    }""")


def tema_claro(page):
    if "dark" in (page.locator("html").get_attribute("class") or ""):
        alvo = page.locator('span.sr-only:has-text("Alterar tema")')
        if alvo.count():
            alvo.first.locator("xpath=ancestor::button").first.click()
            page.wait_for_timeout(800)


def login(page, ctx):
    page.goto("https://beefood.app/", wait_until="domcontentloaded")
    after_click(page)
    if page.locator("input#emailOrWhatsapp").count():
        page.fill("input#emailOrWhatsapp", LOGIN_EMAIL)
        page.fill("input#password", LOGIN_SENHA)
        page.get_by_role("button", name="ENTRAR").click()
        after_click(page, 9000)
        ctx.storage_state(path=str(STATE))
    tema_claro(page)
    limpar(page)


def shot(page, nome: str):
    destino = PURA / nome
    page.screenshot(path=str(destino), type="png")
    print("SHOT", destino.name, destino.stat().st_size)


# ----------------------------------------------------------------- o aparelho
def tocar(pg, texto, minimo=0, obrigatorio=True):
    rotulo = pg.evaluate("""([texto, minimo]) => {
      const ler = b => (b.innerText || '').replace(/\\s+/g, ' ').trim();
      const alvo = [...document.querySelectorAll('button')].find(b =>
        b.getBoundingClientRect().y >= minimo && ler(b).toUpperCase().includes(texto));
      if (!alvo) return null;
      alvo.click();
      return ler(alvo);
    }""", [texto.upper(), minimo])
    if rotulo is None and obrigatorio:
        raise SystemExit(f"ERRO: não achei {texto!r}")
    pg.wait_for_timeout(2500)
    return rotulo


def digitar(pg, texto):
    for c in texto:
        pg.get_by_role("button", name=c, exact=True).first.click(force=True)
        pg.wait_for_timeout(150)


def esperar_imagens(pg, ms=12000):
    try:
        pg.wait_for_function(
            "() => [...document.images].every(i => i.complete && i.naturalWidth > 0)",
            timeout=ms)
    except Exception:
        print("  aviso: alguma imagem não terminou de carregar")
    pg.wait_for_timeout(2500)


def texto_tela(pg, titulo):
    linhas = [l.strip() for l in pg.locator("body").inner_text().split("\n") if l.strip()]
    print(f"  {titulo}:", " | ".join(linhas)[:600])
    return " | ".join(linhas).upper()


def ate_o_pagamento(pg):
    """Monta o pedido, identifica o cliente e para na tela de pagamento."""
    pg.goto(TOTEM_URL, wait_until="networkidle", timeout=90000)
    pg.wait_for_timeout(9000)
    tocar(pg, "FAÇA SEU PEDIDO")
    pg.wait_for_timeout(4000)
    pg.evaluate("""() => {
      const alvo = [...document.querySelectorAll('div,article,li,button')].filter(e => {
        const t = (e.innerText || '').replace(/\\s+/g, ' ').trim().toUpperCase();
        return t.startsWith('ONE BURGER R$') && e.getBoundingClientRect().height < 400;
      }).pop();
      if (alvo) alvo.click();
    }""")
    pg.wait_for_timeout(4000)
    for _ in range(8):
        if tocar(pg, "ADICIONAR R$", 1650, obrigatorio=False):
            break
        if not tocar(pg, "PULAR", 1650, obrigatorio=False):
            break
    tocar(pg, "VER SACOLA", 1650, obrigatorio=False)
    tocar(pg, "CONTINUAR", 1650, obrigatorio=False)
    pg.wait_for_timeout(4000)
    digitar(pg, TELEFONE)
    tocar(pg, "CONFIRMAR", obrigatorio=False)
    pg.wait_for_timeout(7000)
    if "MESA" in texto_tela(pg, "apos telefone") and \
            pg.get_by_role("button", name="1", exact=True).count():
        digitar(pg, MESA)
        tocar(pg, "CONFIRMAR", obrigatorio=False)
        pg.wait_for_timeout(6000)
    tocar(pg, "COMER AQUI", obrigatorio=False)
    pg.wait_for_timeout(3000)
    tocar(pg, "IR PARA PAGAMENTO")
    pg.wait_for_timeout(6000)
    esperar_imagens(pg)
    texto_tela(pg, "pagamento")
    shot(pg, "01-totem-pagamento.png")


def cap_ensaio(pg):
    ate_o_pagamento(pg)
    print("  ENSAIO: paro aqui. Nenhum pedido gravado.")


def cap_pedido(pg):
    ate_o_pagamento(pg)
    tocar(pg, "DINHEIRO")
    pg.wait_for_timeout(5000)
    corpo = texto_tela(pg, "dinheiro")
    shot(pg, "02-totem-dinheiro.png")
    if os.environ.get("VALENDO") != "1":
        print("  SEM VALENDO=1: paro antes de gravar o pedido.")
        return
    if "SIM, VOU PAGAR" not in corpo:
        raise SystemExit("ERRO: a confirmação do dinheiro não apareceu — não gravo nada")
    print("  cliquei em", tocar(pg, "SIM, VOU PAGAR"))
    # a tela de sucesso fica poucos segundos no ar antes de voltar para a espera
    for i in range(1, 5):
        pg.wait_for_timeout(2500)
        texto_tela(pg, f"depois do clique {i}")
        shot(pg, f"03-totem-pedido-feito-{i}.png")


APARELHO = {"ensaio": cap_ensaio, "pedido": cap_pedido}


# ------------------------------------------------------------------- o painel
def cap_delivery(page):
    """Filtra pelo chip Totem: sem o filtro a tela mostra cliente de outros pedidos."""
    page.goto("https://beefood.app/delivery", wait_until="domcontentloaded")
    after_click(page, 10000)
    limpar(page)
    chip = page.get_by_text("Totem", exact=False).first
    print("  chip:", chip.inner_text())
    chip.click()
    after_click(page, 6000)
    limpar(page)
    shot(page, "04-painel-delivery-pedido-totem.png")


def cap_detalhe(page):
    """O card do pedido aberto: itens, mesa e origem."""
    page.goto("https://beefood.app/delivery", wait_until="domcontentloaded")
    after_click(page, 10000)
    limpar(page)
    page.get_by_text("Totem", exact=False).first.click()
    after_click(page, 6000)
    page.get_by_text("Teste Manual", exact=False).first.click()
    after_click(page, 8000)
    limpar(page)
    dlg = page.locator('[role="dialog"]').last
    if dlg.count():
        print("  modal:", " | ".join(
            [l.strip() for l in (dlg.inner_text() or "").split("\n") if l.strip()])[:600])
    shot(page, "05-painel-pedido-detalhe.png")


def cap_historico(page):
    """Histórico de Vendas → filtro Origem = Totem. O filtro evita mostrar cliente
    de outros pedidos na imagem, que é dado de terceiro em repositório público."""
    page.goto("https://beefood.app/historico", wait_until="domcontentloaded")
    after_click(page, 12000)
    limpar(page)
    page.locator("button:has(svg.lucide-funnel), button:has(svg.lucide-filter)").first.click()
    after_click(page, 4000)
    dlg = page.locator('[role="dialog"]').last
    dlg.get_by_text("Totem", exact=True).first.click()
    after_click(page, 2000)
    shot(page, "06-painel-historico-filtro-origem.png")
    dlg.get_by_text("APLICAR FILTROS", exact=False).first.click()
    after_click(page, 9000)
    limpar(page)
    linhas = page.locator("tbody tr").count()
    print("  linhas na lista:", linhas)
    shot(page, "07-painel-historico-lista-totem.png")


def cap_desempenho(page):
    """A tela Desempenho é um iframe de relatorios.beefood.com.br."""
    page.goto("https://beefood.app/desempenho", wait_until="domcontentloaded")
    after_click(page, 14000)
    limpar(page)
    quadro = page.frame_locator('iframe[src*="relatorios"]')
    quadro.get_by_text("Origem", exact=True).first.click()
    after_click(page, 12000)
    limpar(page)
    shot(page, "08-painel-desempenho-origem.png")
    quadro.get_by_text("Autoatendimento", exact=True).first.click()
    after_click(page, 9000)
    limpar(page)
    shot(page, "09-painel-desempenho-autoatendimento.png")


PAINEL = {"delivery": cap_delivery, "detalhe": cap_detalhe, "historico": cap_historico,
          "desempenho": cap_desempenho}


def main():
    pedidos = sys.argv[1:] or ["ensaio"]
    with sync_playwright() as p:
        nav = p.chromium.launch(headless=True)
        for nome in pedidos:
            if nome in APARELHO:
                print("==", nome)
                ctx = nav.new_context(viewport={"width": 1080, "height": 1920},
                                      locale="pt-BR", service_workers="block")
                APARELHO[nome](ctx.new_page())
                ctx.close()
        if [x for x in pedidos if x in PAINEL]:
            ctx = nav.new_context(
                viewport={"width": 1440, "height": 900}, device_scale_factor=1.5,
                locale="pt-BR", timezone_id="America/Sao_Paulo",
                storage_state=str(STATE) if STATE.exists() else None)
            page = ctx.new_page()
            login(page, ctx)
            for nome in pedidos:
                if nome in PAINEL:
                    print("==", nome)
                    PAINEL[nome](page)
            ctx.storage_state(path=str(STATE))
            ctx.close()
        nav.close()


if __name__ == "__main__":
    main()
