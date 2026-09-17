#!/usr/bin/env python3
"""Fotografa os aparelhos que a skill sabe desenhar, um por um e numa folha só.

    python catalogo.py

Saída: `assets/catalogo/*.png` e `assets/catalogo/catalogo.png` (a folha).

Por que existe: o `base.css` sabe desenhar totem, tablet, celular, janela de
navegador e cupom, e cada um tem um jeito certo de aparecer — largura que cabe,
tela vazia ou tela desenhada, reto ou em 3D. Isso estava só escrito. Escolher
aparelho lendo texto custa uma rodada de render; escolher **olhando** custa um
arquivo aberto.

Cada peça aparece em dois estados, quando os dois existem:

- **só o aparelho**, para ver a carcaça e decidir a moldura;
- **com tela**, que é captura de verdade quando ela se lê reduzida, ou tela
  desenhada em CSS quando não se lê.

Rodar de novo depois de mexer no `base.css` é obrigatório: a folha é a prova de
que o aparelho continua lendo como aparelho. As medidas dos rótulos são as
larguras recomendadas em `references/mockups.md`.
"""

from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import renderizar as R  # noqa: E402

SKILL = Path(__file__).resolve().parent.parent
CATALOGO = SKILL / "assets" / "catalogo"

# Tela vazia: listrado claro, sem texto. Diz "aqui entra imagem" sem escrever
# nada dentro do aparelho — palavra em mockup de catálogo vira legenda falsa.
VAZIA = """
.vazia {
  width: 100%;
  height: 100%;
  background: repeating-linear-gradient(-45deg, #e9e9ec 0 12px, #f4f4f6 12px 24px);
}
"""

TELA_TOTEM = """
<div class="tela-totem" style="font-size: 19px">
  <div class="tela-totem__setores">
    <div class="tela-totem__marca-caixa"><span></span></div>
    <div class="tela-totem__setor tela-totem__setor--ativo">
      <img src="skill:fotos/foto-batata.png" alt=""><span>SIDES</span>
    </div>
    <div class="tela-totem__setor">
      <img src="skill:fotos/foto-smash.png" alt=""><span>BURGERS</span>
    </div>
    <div class="tela-totem__setor">
      <img src="skill:fotos/foto-brownie.png" alt=""><span>DESSERTS</span>
    </div>
    <div class="tela-totem__setor">
      <img src="skill:fotos/foto-shake.png" alt=""><span>MILKSHAKES</span>
    </div>
  </div>
  <div class="tela-totem__corpo">
    <div class="tela-totem__banner"><img src="skill:fotos/totem-banner-en.png" alt=""></div>
    <div class="tela-totem__rolagem">
      <div class="tela-totem__secao">Sides</div>
      <div class="tela-totem__grade">
        <div class="tela-totem__card">
          <img src="skill:fotos/foto-batata.png" alt="">
          <div><span>FRENCH FRIES</span><b>R$ 11,00</b></div>
        </div>
        <div class="tela-totem__card">
          <img src="skill:fotos/foto-cebola.png" alt="">
          <div><span>ONION RINGS</span><b>R$ 12,00</b></div>
        </div>
        <div class="tela-totem__card">
          <img src="skill:fotos/foto-mozza.png" alt="">
          <div><span>MOZZA STICKS</span><b>R$ 32,00</b></div>
        </div>
        <div class="tela-totem__card">
          <img src="skill:fotos/foto-batata-cheddar.png" alt="">
          <div><span>CHEDDAR &amp; BACON FRIES</span><b>R$ 18,00</b></div>
        </div>
      </div>
    </div>
    <div class="tela-totem__sacola"><i></i><span>Your bag is empty</span></div>
  </div>
</div>
"""

TELA_TOTEM_ESPERA = """
<div class="tela-totem tela-totem--espera" style="font-size: 20px">
  <div class="tela-totem__botao">START YOUR ORDER</div>
  <div class="tela-totem__idiomas">
    <span class="bandeira"><span>&#127463;&#127479;</span></span>
    <span class="bandeira bandeira--anel"><span>&#127482;&#127480;</span></span>
    <span class="bandeira"><span>&#127466;&#127480;</span></span>
  </div>
</div>
"""

TELA_TABLET = """
<div class="tela-tablet" style="font-size: 16px">
  <div class="tela-tablet__topo">
    <span class="tela-tablet__logo"></span>
    <span class="tela-tablet__busca"><i class="lupa"></i>SEARCH</span>
    <span class="tela-tablet__acao"><i></i>MY CART</span>
    <span class="tela-tablet__acao"><i></i>MY BILL</span>
  </div>
  <div class="tela-tablet__miolo">
    <div class="tela-tablet__atalhos">
      <div class="tela-tablet__atalho"><i></i>HIGHLIGHTS</div>
      <div class="tela-tablet__atalho tela-tablet__atalho--ativo"><i class="talher"></i>MENU</div>
      <div class="tela-tablet__atalho"><i class="sino"></i>RATE</div>
      <div class="tela-tablet__idiomas">
        <span class="bandeira bandeira--retangular"><span>&#127463;&#127479;</span></span>
        <span class="bandeira bandeira--retangular bandeira--anel"><span>&#127482;&#127480;</span></span>
        <span class="bandeira bandeira--retangular"><span>&#127466;&#127480;</span></span>
      </div>
    </div>
    <div class="tela-tablet__setores">
      <div class="tela-tablet__setor tela-tablet__setor--ativo">Burgers</div>
      <div class="tela-tablet__setor">Sides</div>
      <div class="tela-tablet__setor">Desserts</div>
    </div>
    <div class="tela-tablet__corpo">
      <div class="tela-tablet__faixa">Burgers avulsos</div>
      <div class="tela-tablet__item">
        <img src="skill:fotos/foto-melted.png" alt="">
        <div class="tela-tablet__texto">
          <span>MELTED</span>
          <small>Brioche bun, 100 g beef patty, melted cheddar cream and
            chopped bacon</small>
          <b>R$ 34,00</b>
        </div>
        <span class="tela-tablet__pedir">Order</span>
      </div>
      <div class="tela-tablet__item">
        <img src="skill:fotos/foto-tasty-bacon.png" alt="">
        <div class="tela-tablet__texto">
          <span>TASTY BACON</span>
          <small>Sesame brioche bun, cheddar cheese, smoked mayo and bacon
            slices</small>
          <b>R$ 30,00</b>
        </div>
        <span class="tela-tablet__pedir">Order</span>
      </div>
      <div class="tela-tablet__item">
        <img src="skill:fotos/foto-one-classic.png" alt="">
        <div class="tela-tablet__texto">
          <span>ONE CLASSIC</span>
          <small>Brioche bun, 100 g beef patty, lettuce, tomato, red onion and
            green mayo</small>
          <b>R$ 26,00</b>
        </div>
        <span class="tela-tablet__pedir">Order</span>
      </div>
    </div>
  </div>
</div>
"""

TELA_APP = """
<div class="tela-app" style="font-size: 22px">
  <div class="tela-app__barra"><span>20:41</span><span>Entregador</span></div>
  <div class="tela-app__topo">
    <div class="tela-app__titulo">Pedido #32</div>
    <div>Rua das Acácias, 120</div>
  </div>
  <div class="tela-app__corpo">
    <div class="tela-app__cartao">
      <div class="tela-app__linha"><span>1x Combo One</span><span>39,00</span></div>
      <div class="tela-app__linha tela-app__linha--destaque">
        <span>1x Coca 350ml</span><span></span>
      </div>
    </div>
    <div class="tela-app__aviso">Confira a bebida antes de sair</div>
    <div class="tela-app__botao">Sair para entrega</div>
  </div>
</div>
"""

TOTEM_CORPO = """
  <div class="totem__painel">
    <div class="totem__leitor"></div>
    <div class="totem__impressora"></div>
    <div class="totem__pinpad">
      <div class="totem__tecla"><span></span><span></span><span></span></div>
      <div class="totem__tecla"><span></span><span></span><span></span></div>
      <div class="totem__tecla"><span></span><span></span><span></span></div>
    </div>
  </div>
  <div class="totem__coluna"></div>
  <div class="totem__base"></div>
"""


def totem(dentro: str) -> str:
    return (f'<div class="totem" style="width: 420px; --coluna: 300px">'
            f'<div class="totem__tela">{dentro}</div>{TOTEM_CORPO}</div>')


def tablet(dentro: str) -> str:
    return (f'<div class="tablet" style="width: 880px">'
            f'<div class="tablet__tela">{dentro}</div>'
            f'<div class="tablet__suporte"></div></div>')


VAZIO = '<div class="vazia"></div>'

# (arquivo, rótulo, o que aparece embaixo dele na folha, fragmento)
PECAS: list[tuple[str, str, str, str]] = [
    ("totem", "Totem, só o aparelho",
     "420 px com texto ao lado; 400 sozinho",
     totem(VAZIO)),
    ("totem-com-captura", "Totem com captura",
     "totem-espera-en-720.png, da biblioteca",
     totem('<img src="skill:fotos/totem-espera-en-720.png" alt="">')),
    ("totem-com-cardapio", "Totem com tela desenhada",
     ".tela-totem, cardápio (19 px)",
     totem(TELA_TOTEM)),
    ("totem-com-espera", "Totem com espera desenhada",
     ".tela-totem--espera, quando não há captura",
     totem(TELA_TOTEM_ESPERA)),
    ("tablet", "Tablet, só o aparelho",
     "880 px sozinho; 660 dividindo a faixa",
     tablet(VAZIO)),
    ("tablet-com-cardapio", "Tablet com tela desenhada",
     ".tela-tablet, cardápio escuro (16 px)",
     tablet(TELA_TABLET)),
    ("celular", "Celular, só o aparelho",
     "660 px em sangria centralizada",
     f'<div class="celular" style="width: 660px"><div class="celular__tela">{VAZIO}</div></div>'),
    ("celular-3d", "Celular em 3D, com tela desenhada",
     "462 px, virado para dentro (.g3d--na-direita)",
     '<div class="cena3d"><div class="celular g3d g3d--na-direita" style="width: 462px">'
     f'<div class="celular__tela">{TELA_APP}</div></div></div>'),
    ("navegador", "Janela de navegador",
     "1120 px em sangria pela direita",
     '<div class="navegador" style="width: 1120px">'
     '<div class="navegador__barra"><span class="navegador__bolinha"></span>'
     '<span class="navegador__bolinha"></span><span class="navegador__bolinha"></span>'
     '<span class="navegador__url">beefood.app/cardapio/produtos</span></div>'
     '<div class="navegador__tela" style="aspect-ratio: 16 / 10">'
     f'{VAZIO}</div></div>'),
    ("cupom", "Cupom térmico desenhado",
     ".cupom + .rasgado, bobina de 80 mm",
     '<div class="cupom rasgado">'
     '<div class="cupom__linha"><span>1x Combo One</span><span>39,00</span></div>'
     '<div class="cupom__linha"><span>&bull; 1x Batata</span><span></span></div>'
     '<div class="cupom__linha cupom__linha--destaque">'
     '<span>&bull; 1x Coca 350ml</span><span></span></div>'
     '<div class="cupom__corte"></div>'
     '<div class="cupom__linha"><span>TOTAL</span><span>39,00</span></div></div>'),
]


def pagina(fragmento: str) -> str:
    """Mesma pilha de estilos do slide, num quadro que só tem a peça."""
    largura, altura = R.MARCA["formatos"][R.MARCA["formato_padrao"]]
    return f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<style>{R.face_das_fontes()}</style>
<style>:root{{--largura:{largura}px;--altura:{altura}px;
--logo:url('{R.LOGO_CLARO.as_uri()}');
--logo-escuro:url('{R.LOGO_ESCURO.as_uri()}');}}</style>
<style>{R.BASE_CSS.read_text(encoding="utf-8")}</style>
<style>
html, body {{ margin: 0; background: #faf9f8; font-family: 'Mulish', sans-serif; }}
/* Folga em volta para caber a sombra do aparelho, que sai da caixa dele. */
#peca {{ display: inline-block; padding: 80px; }}
{VAZIA}
</style>
</head><body><div id="peca">{R.resolver_skill(fragmento)}</div></body></html>"""


def fotografar() -> list[tuple[Path, str, str]]:
    from playwright.sync_api import sync_playwright

    CATALOGO.mkdir(parents=True, exist_ok=True)
    feitas: list[tuple[Path, str, str]] = []
    tmp = Path(tempfile.mkdtemp(prefix="catalogo-"))
    try:
        with sync_playwright() as p:
            navegador = p.chromium.launch()
            ctx = navegador.new_context(viewport={"width": 1400, "height": 1600},
                                        device_scale_factor=1, locale="pt-BR")
            aba = ctx.new_page()
            for arquivo, rotulo, nota, fragmento in PECAS:
                alvo = tmp / f"{arquivo}.html"
                alvo.write_text(pagina(fragmento), encoding="utf-8")
                aba.goto(alvo.as_uri(), wait_until="load")
                aba.evaluate("document.fonts.ready")
                aba.wait_for_timeout(300)
                png = CATALOGO / f"{arquivo}.png"
                aba.locator("#peca").screenshot(path=str(png), type="png")
                feitas.append((png, rotulo, nota))
                print(f"OK  {png.relative_to(SKILL)}")
            navegador.close()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return feitas


def folha(pecas: list[tuple[Path, str, str]], colunas: int = 4) -> Path:
    """Uma folha com todas as peças na mesma escala relativa, com rótulo."""
    from PIL import Image, ImageDraw, ImageFont

    celula, alto_rotulo, margem = 420, 76, 24
    linhas = -(-len(pecas) // colunas)
    larg = colunas * (celula + margem) + margem
    alt = linhas * (celula + alto_rotulo + margem) + margem
    folha_img = Image.new("RGB", (larg, alt), "#faf9f8")
    desenho = ImageDraw.Draw(folha_img)
    negrito = ImageFont.truetype(str(R.FONTES / "Mulish-700.ttf"), 20)
    leve = ImageFont.truetype(str(R.FONTES / "Mulish-400.ttf"), 17)

    for i, (png, rotulo, nota) in enumerate(pecas):
        col, lin = i % colunas, i // colunas
        x = margem + col * (celula + margem)
        y = margem + lin * (celula + alto_rotulo + margem)
        with Image.open(png) as im:
            im = im.convert("RGB")
            escala = min(celula / im.width, celula / im.height)
            mini = im.resize((max(1, round(im.width * escala)),
                              max(1, round(im.height * escala))), Image.LANCZOS)
        folha_img.paste(mini, (x + (celula - mini.width) // 2,
                               y + (celula - mini.height) // 2))
        desenho.text((x, y + celula + 10), rotulo, font=negrito, fill="#1e1e1e")
        desenho.text((x, y + celula + 38), nota, font=leve, fill="#6b6b6b")

    alvo = CATALOGO / "catalogo.png"
    folha_img.save(alvo)
    print(f"OK  {alvo.relative_to(SKILL)}  {folha_img.width}x{folha_img.height}")
    return alvo


if __name__ == "__main__":
    folha(fotografar())
