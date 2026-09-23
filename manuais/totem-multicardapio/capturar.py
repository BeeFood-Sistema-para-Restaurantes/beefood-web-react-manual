#!/usr/bin/env python3
"""Captura #124 — Mais de um cardápio no totem.

    python3 capturar.py painel            # a aba Cardápios e o seletor do painel
    python3 capturar.py aparelho          # seletor, "ver todos" e o cardápio adicional
    python3 capturar.py ensaio            # monta o pedido misto e PARA no pagamento
    VALENDO=1 python3 capturar.py pedido  # fecha o pedido misto, em Dinheiro
    python3 capturar.py detalhe           # o pedido misto no painel

O pedido misto é a prova do manual: um item do cardápio adicional e um do
principal na mesma sacola, para mostrar que a venda é **uma só**. Como ele grava
de verdade, vale a técnica do ensaio (MEMORIA-GERAL, seção 7): `ensaio` percorre o
mesmo caminho e para antes do clique que grava, e o `pedido` só clica com
`VALENDO=1`.

O aparelho é uma página web: mesma URL da aba Download, com o token da filial
(sandbox descartável, pode ficar versionado). O seletor de cardápio e o teclado
numérico **ignoram `click()` por JavaScript** — os dois precisam de clique real.
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
ADICIONAL = "SUSHI"          # o cardápio adicional, como aparece no seletor
ITEM_ADICIONAL = "TEMAKI DE ATUM"   # sem grupo de opções: entra direto
ITEM_PRINCIPAL = "ONE BURGER"
TELEFONE = "15999998888"
MESA = "14"
ESCONDE_FLUTUANTE = """
  div.fixed.bottom-6, a[href*="wa.me"], iframe[title*="WhatsApp"] { display: none !important }
"""


# --------------------------------------------------------------- utilidades
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
    nps = page.locator('[role="dialog"]').filter(has_text="Como está sendo sua experiência")
    if nps.count():
        botao = nps.last.get_by_role("button", name="FECHAR")
        if botao.count():
            try:
                botao.click(timeout=1500)
                after_click(page)
            except Exception:
                pass


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


def texto_tela(pg, titulo, limite=700):
    linhas = [l.strip() for l in pg.locator("body").inner_text().split("\n") if l.strip()]
    junto = " | ".join(linhas)
    print(f"  {titulo}:", junto[:limite])
    return junto.upper()


# ----------------------------------------------------------------- o painel
def abrir_modal(page):
    page.goto("https://beefood.app/aplicativos", wait_until="domcontentloaded")
    after_click(page, 8000)
    limpar(page)
    page.get_by_text("Autoatendimento presencial", exact=False).first.click()
    after_click(page, 8000)
    limpar(page)


def aba(page, nome: str):
    achou = page.evaluate("""(nome) => {
      const dlg = [...document.querySelectorAll('[role=dialog]')].pop();
      const ler = e => (e.innerText || '').replace(/\\s+/g, ' ').trim();
      const alvo = [...dlg.querySelectorAll('button,div,span,a')]
        .filter(e => ler(e) === nome && e.getBoundingClientRect().height < 60)
        .pop();
      if (!alvo) return false;
      alvo.click();
      return true;
    }""", nome)
    if not achou:
        raise RuntimeError(f"aba {nome!r} não encontrada")
    after_click(page, 4000)


def cap_painel(page):
    """A aba Cardápios com a chave do cardápio adicional ligada, e o seletor de
    cardápio que o painel ganha quando existe mais de um."""
    abrir_modal(page)
    aba(page, "Cardápios")
    print("  switches:", page.evaluate("""() => {
      const dlg = [...document.querySelectorAll('[role=dialog]')].pop();
      return [...dlg.querySelectorAll('[role=switch]')].map(s => ({
        estado: s.getAttribute('data-state'),
        travado: s.hasAttribute('disabled'),
        linha: (s.closest('div.flex')?.innerText || '').replace(/\\s+/g,' ').trim()}));
    }"""))
    texto_tela(page, "aba Cardápios", 400)
    shot(page, "01-modal-cardapios-chave.png")

    page.keyboard.press("Escape")
    after_click(page, 3000)
    page.goto("https://beefood.app/cardapio-digital", wait_until="domcontentloaded")
    after_click(page, 12000)
    limpar(page)
    # troca para o cardápio adicional, senão a imagem não mostra a troca
    achou = page.evaluate("""(nome) => {
      const alvo = [...document.querySelectorAll('button')].find(b =>
        (b.getAttribute('title') || b.getAttribute('aria-label') ||
         b.querySelector('img')?.alt || '').toUpperCase().includes(nome));
      if (!alvo) return null;
      alvo.click();
      return alvo.getAttribute('title') || alvo.querySelector('img')?.alt || '?';
    }""", ADICIONAL)
    print("  chip clicado:", achou)
    after_click(page, 10000)
    limpar(page)
    print("  editando:", page.evaluate("""() => {
      const el = [...document.querySelectorAll('*')].filter(e =>
        (e.innerText || '').includes('EDITANDO CARDÁPIO') && e.children.length < 6);
      return el.slice(-1).map(e => (e.innerText||'').replace(/\\s+/g,' ').trim());
    }"""))
    shot(page, "07-painel-editando-cardapio.png")


def cap_detalhe(page):
    """O pedido misto no painel: dois itens, um de cada cardápio, numa venda só."""
    page.goto("https://beefood.app/delivery", wait_until="domcontentloaded")
    after_click(page, 10000)
    limpar(page)
    page.get_by_text("Totem", exact=False).first.click()
    after_click(page, 6000)
    # o card do pedido misto é o da mesa que ele usou: clicar no "Teste Manual"
    # solto abre o primeiro card da coluna, que é outro pedido
    achou = page.evaluate("""(mesa) => {
      const alvo = [...document.querySelectorAll('div')].filter(e => {
        const t = (e.innerText || '').replace(/\\s+/g, ' ');
        return t.includes('Mesa ' + mesa) && e.getBoundingClientRect().height < 200;
      })[0];
      if (!alvo) return false;
      alvo.click();
      return true;
    }""", MESA)
    if not achou:
        raise SystemExit(f"ERRO: não achei o card da mesa {MESA}")
    after_click(page, 9000)
    limpar(page)
    dlg = page.locator('[role="dialog"]').last
    if dlg.count():
        print("  card:", " | ".join(
            [l.strip() for l in (dlg.inner_text() or "").split("\n") if l.strip()])[:700])
    shot(page, "06-painel-pedido-misto.png")


PAINEL = {"painel": cap_painel, "detalhe": cap_detalhe}


# ---------------------------------------------------------------- o aparelho
def tocar(pg, texto, minimo=0, obrigatorio=True, real=False):
    """Acha o botão pelo texto. `real=True` usa o mouse: o seletor de cardápio é
    um motion.button e não responde a click() por JavaScript."""
    caixa = pg.evaluate("""([texto, minimo]) => {
      const ler = b => (b.innerText || '').replace(/\\s+/g, ' ').trim();
      const alvo = [...document.querySelectorAll('button')].find(b =>
        b.getBoundingClientRect().y >= minimo && ler(b).toUpperCase().includes(texto));
      if (!alvo) return null;
      const r = alvo.getBoundingClientRect();
      return {x: r.x + r.width / 2, y: r.y + r.height / 2, t: ler(alvo).slice(0, 60)};
    }""", [texto.upper(), minimo])
    if caixa is None:
        if obrigatorio:
            raise SystemExit(f"ERRO: não achei {texto!r}")
        return None
    if real:
        pg.mouse.click(caixa["x"], caixa["y"])
    else:
        pg.evaluate("""([texto, minimo]) => {
          const ler = b => (b.innerText || '').replace(/\\s+/g, ' ').trim();
          const alvo = [...document.querySelectorAll('button')].find(b =>
            b.getBoundingClientRect().y >= minimo && ler(b).toUpperCase().includes(texto));
          if (alvo) alvo.click();
        }""", [texto.upper(), minimo])
    pg.wait_for_timeout(3000)
    return caixa["t"]


def escolher(pg, nome):
    """Escolhe um cardápio DENTRO do seletor.

    Precisa ser escopado: o seletor é uma camada por cima do cardápio, e há
    produto com "sushi" no nome atrás dele — procurar no documento inteiro acha o
    cartão do produto e o clique morre na camada. O seletor é o único
    `[role=dialog]` com `aria-labelledby="menu-picker-title"`.
    """
    caixa = pg.evaluate("""(nome) => {
      const dlg = document.querySelector(
        '[role=dialog][aria-labelledby="menu-picker-title"]');
      if (!dlg) return null;
      const ler = b => (b.innerText || '').replace(/\\s+/g, ' ').trim();
      const alvo = [...dlg.querySelectorAll('button')].find(b =>
        ler(b).toUpperCase().includes(nome));
      if (!alvo) return null;
      const r = alvo.getBoundingClientRect();
      return {x: r.x + r.width / 2, y: r.y + r.height / 2, t: ler(alvo).slice(0, 60)};
    }""", nome.upper())
    if caixa is None:
        raise SystemExit(f"ERRO: {nome!r} não está no seletor de cardápio")
    pg.mouse.click(caixa["x"], caixa["y"])
    print(f"  escolhi {caixa['t']!r}")
    pg.wait_for_timeout(5000)
    esperar_imagens(pg)


def cartao(pg, nome):
    """Clica no cartão do produto: o texto do cartão começa com o nome e ele é
    baixo o bastante para não ser o cabeçalho do setor."""
    achou = pg.evaluate("""(nome) => {
      const alvo = [...document.querySelectorAll('div,article,li,button')].filter(e => {
        const t = (e.innerText || '').replace(/\\s+/g, ' ').trim().toUpperCase();
        return t.startsWith(nome + ' R$') && e.getBoundingClientRect().height < 400;
      }).pop();
      if (!alvo) return false;
      alvo.click();
      return true;
    }""", nome.upper())
    if not achou:
        raise SystemExit(f"ERRO: não achei o cartão de {nome!r}")
    pg.wait_for_timeout(4500)


def digitar(pg, texto):
    """O teclado numérico escuta evento de ponteiro: precisa de clique real."""
    for c in texto:
        pg.get_by_role("button", name=c, exact=True).first.click(force=True)
        pg.wait_for_timeout(150)


def esperar_imagens(pg, ms=25000):
    try:
        pg.wait_for_function(
            "() => [...document.images].every(i => i.complete && i.naturalWidth > 0)",
            timeout=ms)
    except Exception:
        print("  aviso: alguma imagem não terminou de carregar")
    pg.wait_for_timeout(2500)


def abrir_seletor(pg):
    pg.goto(TOTEM_URL, wait_until="networkidle", timeout=90000)
    pg.wait_for_timeout(16000)
    esperar_imagens(pg)
    tocar(pg, "FAÇA SEU PEDIDO", real=True)
    pg.wait_for_timeout(4000)
    esperar_imagens(pg)


def trocar(pg):
    """Reabre o seletor pelo botão Trocar do cabeçalho do cardápio."""
    tocar(pg, "TROCAR", real=True)
    pg.wait_for_timeout(4000)
    if not pg.locator('[role=dialog][aria-labelledby="menu-picker-title"]').count():
        raise SystemExit("ERRO: o Trocar não abriu o seletor de cardápio")


def adicionar_item(pg, nome):
    """Abre o cartão, vence os grupos de opções e volta com o item na sacola."""
    cartao(pg, nome)
    for _ in range(8):
        if tocar(pg, "ADICIONAR R$", 1400, obrigatorio=False):
            break
        if not tocar(pg, "PULAR", 1400, obrigatorio=False):
            raise SystemExit(f"ERRO: não consegui adicionar {nome!r}")
    pg.wait_for_timeout(3000)
    # a venda sugestiva entra depois de adicionar e segura a tela
    tocar(pg, "CONTINUAR SEM ADICIONAR", obrigatorio=False)
    pg.wait_for_timeout(2500)
    print(f"  {nome} na sacola")


def cap_aparelho(pg):
    """As três telas do cliente: o seletor, os dois cardápios juntos e o adicional
    sozinho."""
    abrir_seletor(pg)
    texto_tela(pg, "seletor")
    shot(pg, "02-totem-escolha-cardapio.png")

    escolher(pg, "VER TODOS OS CARDÁPIOS")
    # a coluna de setores é a prova do "ver todos": rolada até a emenda, ela mostra
    # os setores do cardápio adicional e os do principal na mesma lista. Sem isso a
    # imagem sai idêntica à do cardápio adicional sozinho.
    pg.mouse.move(120, 1000)
    for _ in range(6):
        pg.mouse.wheel(0, 200)
        pg.wait_for_timeout(400)
    pg.wait_for_timeout(2500)
    esperar_imagens(pg)
    texto_tela(pg, "todos os cardápios", 500)
    shot(pg, "03-totem-todos-cardapios.png")

    trocar(pg)
    escolher(pg, ADICIONAL)
    texto_tela(pg, "só o cardápio adicional", 500)
    shot(pg, "04-totem-cardapio-adicional.png")


def ate_o_pagamento(pg):
    """Sacola com um item de cada cardápio, e para na tela de pagamento."""
    abrir_seletor(pg)
    escolher(pg, ADICIONAL)
    adicionar_item(pg, ITEM_ADICIONAL)

    trocar(pg)
    escolher(pg, "CARDÁPIO PRINCIPAL")
    adicionar_item(pg, ITEM_PRINCIPAL)

    tocar(pg, "VER SACOLA", 1650, obrigatorio=False)
    pg.wait_for_timeout(3000)
    esperar_imagens(pg)
    corpo = texto_tela(pg, "sacola", 900)
    if ITEM_ADICIONAL not in corpo or ITEM_PRINCIPAL not in corpo:
        raise SystemExit("ERRO: a sacola não tem um item de cada cardápio")
    shot(pg, "05-totem-sacola-mista.png")

    tocar(pg, "CONTINUAR", 1650, obrigatorio=False)
    pg.wait_for_timeout(4000)
    digitar(pg, TELEFONE)
    tocar(pg, "CONFIRMAR", obrigatorio=False)
    pg.wait_for_timeout(7000)
    if "MESA" in texto_tela(pg, "apos telefone", 300) and \
            pg.get_by_role("button", name="1", exact=True).count():
        digitar(pg, MESA)
        tocar(pg, "CONFIRMAR", obrigatorio=False)
        pg.wait_for_timeout(6000)
    tocar(pg, "COMER AQUI", obrigatorio=False)
    pg.wait_for_timeout(3000)
    tocar(pg, "IR PARA PAGAMENTO")
    pg.wait_for_timeout(6000)
    esperar_imagens(pg)
    texto_tela(pg, "pagamento", 400)


def cap_ensaio(pg):
    ate_o_pagamento(pg)
    print("  ENSAIO: paro aqui. Nenhum pedido gravado.")


def cap_pedido(pg):
    ate_o_pagamento(pg)
    tocar(pg, "DINHEIRO")
    pg.wait_for_timeout(5000)
    corpo = texto_tela(pg, "dinheiro", 400)
    if os.environ.get("VALENDO") != "1":
        print("  SEM VALENDO=1: paro antes de gravar o pedido.")
        return
    if "SIM, VOU PAGAR" not in corpo:
        raise SystemExit("ERRO: a confirmação do dinheiro não apareceu — não gravo nada")
    print("  cliquei em", tocar(pg, "SIM, VOU PAGAR"))
    for i in range(1, 5):
        pg.wait_for_timeout(2500)
        texto_tela(pg, f"depois do clique {i}", 300)


APARELHO = {"aparelho": cap_aparelho, "ensaio": cap_ensaio, "pedido": cap_pedido}


def main():
    pedidos = sys.argv[1:] or ["painel", "aparelho"]
    with sync_playwright() as p:
        nav = p.chromium.launch(headless=True)
        for nome in pedidos:
            if nome in APARELHO:
                print("==", nome)
                ctx = nav.new_context(viewport={"width": 1080, "height": 1920},
                                      locale="pt-BR", timezone_id="America/Sao_Paulo",
                                      service_workers="block")
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
    print("rode o annotate.py para gerar imagens-tratadas")


if __name__ == "__main__":
    main()
