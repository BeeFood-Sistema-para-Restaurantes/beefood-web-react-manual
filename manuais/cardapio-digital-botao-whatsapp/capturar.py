"""Capturas do #128 — Botão de WhatsApp do Cardápio Digital.

Duas pontas, e por isso dois navegadores diferentes:

* o **painel**, em `https://beefood.app/cardapio-digital?tab=whatsapp`, com a conta
  BeeFood3 - Manual (viewport 1440x1100 em DPR 1.5 — a tela precisa de altura, porque o
  formulário tem a prévia ao lado e o cartão de formatos é alto);
* o **cardápio do cliente**, em `https://menu.beefood.com.br/beefood3`, no computador
  (1440x900 em DPR 1.5) e no celular (390x844 em DPR 2, com `is_mobile`).

Grava só em `imagens-puras/`. As setas são do `annotate.py`, e a margem clara em volta da
captura é montada lá, em memória: pura é o print, e só.

Três coisas que este manual aprendeu, e que estão no código abaixo:

* **A tela rola por dentro.** O conteúdo mora num `div` com `overflow-y-auto` de 2455 px, e
  `page.mouse.wheel` ou `window.scrollTo` não movem nada. Rolar é mexer no `scrollTop` desse
  `div` — é o que `rolar()` faz, e os três valores (0, 545, 1200) são as três telas do manual.
* **Medir pelo DOM, não no olho.** `medir()` imprime a caixa de cada alvo já convertida para
  pixel da pura (`getBoundingClientRect() * 1.5`). Numa tela de formulário é mais exato que a
  grade de frações, e é de lá que saem as coordenadas do `annotate.py`.
* **O cardápio do cliente guarda cache.** Depois de salvar a configuração, o botão levou
  alguns minutos para aparecer em `menu.beefood.com.br`. O script confere a presença de
  `a.be-wa__alvo` e avisa quando não acha, em vez de gravar um print sem botão.

Uso, de dentro da pasta do manual:

    python3 capturar.py            # painel e cardápio
    python3 capturar.py painel
    python3 capturar.py cardapio
    python3 capturar.py medir      # só imprime as caixas dos alvos, não grava nada
"""

import os
import sys

from playwright.sync_api import sync_playwright

DEST = "imagens-puras"
PAINEL = "https://beefood.app/cardapio-digital?tab=whatsapp"
MENU = "https://menu.beefood.com.br/beefood3"
STORE = "/tmp/beefood3-storage.json"
LOGIN = ("contato@beefood.com.br", "1q2w3e4r")

# O widget flutuante de suporte cobre o canto de baixo e entraria em toda imagem.
ESCONDER = "div.fixed.bottom-6 { display:none !important }"

# As três rolagens do formulário: topo, "Onde o botão aparece" e "Formato".
ROLAGENS = {"topo": 0, "onde": 545, "formato": 1200}


def esperar(page, extra=5000):
    """Spinner primeiro, cinco segundos depois. Regra da casa para toda captura."""
    for _ in range(30):
        ocupado = (page.locator("text=Carregando...").count()
                   or page.locator("text=Atualizando...").count()
                   or page.locator("text=Calculando").count())
        if not ocupado:
            break
        page.wait_for_timeout(1000)
    page.wait_for_timeout(extra)


def limpar(page):
    if page.locator('button[aria-label="Dispensar"]').count():
        page.locator('button[aria-label="Dispensar"]').first.click()
        page.wait_for_timeout(500)
    for _ in range(2):
        nps = page.locator('[role="dialog"]').filter(has_text="Como está sendo sua experiência")
        if nps.count():
            nps.locator('button:has-text("FECHAR (ESC)")').first.click()
            page.wait_for_timeout(800)
    page.add_style_tag(content=ESCONDER)


def rolar(page, quanto):
    page.evaluate(
        "y => { document.querySelector('div.min-h-0.flex-1.overflow-y-auto').scrollTop = y; }",
        quanto)
    page.wait_for_timeout(1200)


def logar(ctx):
    page = ctx.new_page()
    page.goto("https://beefood.app/login", wait_until="domcontentloaded")
    page.wait_for_timeout(3000)
    if page.locator("#emailOrWhatsapp").count():
        page.fill("#emailOrWhatsapp", LOGIN[0])
        page.fill("#password", LOGIN[1])
        page.click("button:has-text('ENTRAR')")
        page.wait_for_timeout(9000)
        ctx.storage_state(path=STORE)
    page.close()


def abrir_painel(p, altura=1100):
    navegador = p.chromium.launch(env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"})
    ctx = navegador.new_context(
        viewport={"width": 1440, "height": altura}, device_scale_factor=1.5,
        locale="pt-BR", timezone_id="America/Sao_Paulo",
        storage_state=STORE if os.path.exists(STORE) else None)
    if not os.path.exists(STORE):
        logar(ctx)
    page = ctx.new_page()
    page.goto(PAINEL, wait_until="domcontentloaded")
    esperar(page, 10000)
    limpar(page)
    return navegador, page


def painel():
    os.makedirs(DEST, exist_ok=True)
    with sync_playwright() as p:
        navegador, page = abrir_painel(p)
        rolar(page, ROLAGENS["topo"])
        page.screenshot(path=f"{DEST}/01-aba-botao-whatsapp.png")
        rolar(page, ROLAGENS["onde"])
        page.screenshot(path=f"{DEST}/03-onde-o-botao-aparece.png")
        rolar(page, ROLAGENS["formato"])
        page.screenshot(path=f"{DEST}/04-formato-do-botao.png")
        rolar(page, ROLAGENS["topo"])
        page.wait_for_timeout(1500)
        page.screenshot(path=f"{DEST}/05-previa-celular.png")
        page.locator("aside button:has-text('Computador')").first.click()
        page.wait_for_timeout(2500)
        page.screenshot(path=f"{DEST}/06-previa-computador.png")
        # devolve a prévia ao celular, que é como a tela abre
        page.locator("aside button:has-text('Celular')").first.click()
        page.wait_for_timeout(1500)
        print("painel: 5 capturas")
        navegador.close()


def cardapio():
    os.makedirs(DEST, exist_ok=True)
    telas = (("07-cardapio-computador", (1440, 900), False, 1.5),
             ("08-cardapio-celular", (390, 844), True, 2))
    with sync_playwright() as p:
        navegador = p.chromium.launch(env={**os.environ, "LANG": "pt_BR.UTF-8",
                                           "LANGUAGE": "pt_BR"})
        for nome, (largura, altura), celular, dpr in telas:
            ctx = navegador.new_context(
                viewport={"width": largura, "height": altura}, device_scale_factor=dpr,
                locale="pt-BR", timezone_id="America/Sao_Paulo",
                is_mobile=celular, has_touch=celular)
            page = ctx.new_page()
            page.goto(MENU, wait_until="domcontentloaded")
            page.wait_for_timeout(14000)
            alvo = page.locator("a.be-wa__alvo")
            if not alvo.count():
                print(f"ATENÇÃO {nome}: o botão não está no cardápio. Confira se a "
                      "configuração está ligada e espere o cache do cardápio virar.")
            else:
                print(nome, "caixa do botão (CSS):", alvo.first.bounding_box())
            page.screenshot(path=f"{DEST}/{nome}.png")
            ctx.close()
        navegador.close()


# Os alvos das setas, por rolagem. `texto` escolhe entre vários elementos do mesmo seletor.
ALVOS = {
    "topo": [
        ("menu_lateral", "button", "Botão WhatsApp"),
        ("chave_ligar", 'button[aria-label="Ligar Botão de WhatsApp"]', None),
        ("campo_fone", "#wpp-fone", None),
        ("campo_msg", "#wpp-msg", None),
        ("previa_toggle", "aside button", "Celular"),
        ("previa_chaves", "aside label", "Loja aberta"),
    ],
    "onde": [
        ("pos_flutuante", 'button[role="radio"]', "Flutuante sobre o cardápio"),
        ("disp_celular", "#wpp-disp-m", None),
        ("disp_computador", "#wpp-disp-d", None),
    ],
    "formato": [
        ("fmt_pilula", "button", "Pílula"),
        ("tamanho", 'input[aria-label="Tamanho do botão"]', None),
        ("texto_botao", "#wpp-rot", None),
        ("lado_tela", 'button[role="combobox"]', None),
        ("cor_verde", 'button[title="#25D366"]', None),
    ],
}

JS_MEDIR = """
(alvos) => {
  const caixa = (el) => { const b = el.getBoundingClientRect();
    return [Math.round(b.left * 1.5), Math.round(b.top * 1.5),
            Math.round(b.right * 1.5), Math.round(b.bottom * 1.5)]; };
  const saida = {};
  for (const [nome, seletor, texto] of alvos) {
    const lista = Array.from(document.querySelectorAll(seletor));
    const el = texto
      ? lista.find(e => ((e.innerText || e.getAttribute('aria-label') || '').trim()).includes(texto))
      : lista[0];
    saida[nome] = el ? caixa(el) : null;
  }
  return saida;
}
"""


def medir():
    """Imprime a caixa de cada alvo em pixel da pura. É a fonte do annotate.py."""
    with sync_playwright() as p:
        navegador, page = abrir_painel(p)
        for rolagem, alvos in ALVOS.items():
            rolar(page, ROLAGENS[rolagem])
            print(f"== rolagem {rolagem} ({ROLAGENS[rolagem]}) ==")
            for nome, caixa in page.evaluate(JS_MEDIR, alvos).items():
                print(f"   {nome:18} {caixa}")
        navegador.close()


if __name__ == "__main__":
    pedido = sys.argv[1] if len(sys.argv) > 1 else "tudo"
    if pedido == "medir":
        medir()
    else:
        if pedido in ("tudo", "painel"):
            painel()
        if pedido in ("tudo", "cardapio"):
            cardapio()
        print("pronto. Agora: python3 annotate.py")
