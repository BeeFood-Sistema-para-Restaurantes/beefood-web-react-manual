"""Anota as sete capturas do #128 — Botão de WhatsApp do Cardápio Digital.

As coordenadas estão sempre em **pixel da captura pura**, inclusive nas recortadas:
`preparar()` converte. E elas não foram medidas no olho: o `capturar.py` imprime a caixa de
cada alvo lida do próprio DOM (`getBoundingClientRect() * 1.5`, que é o DPR da captura), e é
esse número que entra aqui. Numa tela de formulário, com campo colado em campo, medir pelo
DOM é mais rápido e mais exato do que a grade de frações da `MEMORIA-GERAL`.

Duas geometrias:

* **painel** (`forma()`): a coluna do formulário vive entre x=372 e x=1524 dos 2160 px. O
  recorte a isola e põe faixa clara **dos dois lados** — a da esquerda para quem aponta
  rótulo de campo, a da direita para a chave de ligar e para o seletor de formato, que
  encostam na borda direita do cartão. É a regra do #126: etiqueta na tira da direita mira a
  borda direita, senão a seta atravessa o rótulo inteiro.
* **cardápio do cliente**: entra inteiro, com faixa só à direita. O botão flutuante mora no
  canto inferior direito, e é de lá que a seta tem de chegar.

Nenhuma faixa é gravada na pura: tudo é montado em memória aqui dentro, senão rodar duas
vezes desloca todas as setas. Pura é o print, e só.
"""

import math
import os

from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

VERDE = (22, 150, 78)
BRANCO = (255, 255, 255)
A_LINHA = 235
A_ETIQ = 245
FAIXA = (255, 255, 255)

FONTES = [
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]

# A coluna do formulário na captura de 2160x1650, e a faixa onde moram as etiquetas.
FORM_X0, FORM_X1 = 340, 1540
MARGEM = 150
ESQ = FORM_X0 - MARGEM // 2          # 265
DIR = FORM_X1 + MARGEM // 2          # 1615

# A prévia (o aparelho desenhado à direita da tela) tem recorte próprio.
PREV_X0, PREV_X1 = 1545, 2160
ESQ_PREV = PREV_X0 - MARGEM // 2     # 1425
DIR_PREV = PREV_X1 + MARGEM // 2     # 2235


def font(sz):
    for caminho in FONTES:
        if os.path.exists(caminho):
            return ImageFont.truetype(caminho, sz)
    raise RuntimeError("nenhuma fonte bold encontrada")


def seta(d, x0, y0, x1, y1, w):
    cor = VERDE + (A_LINHA,)
    d.line([(x0, y0), (x1, y1)], fill=cor, width=w)
    ang = math.atan2(y1 - y0, x1 - x0)
    L = w * 4.0
    for s in (0.5, -0.5):
        d.line([(x1, y1), (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))],
               fill=cor, width=w)


def etiqueta(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 3, cy - r - 3, cx + r + 3, cy + r + 3], fill=BRANCO + (245,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=VERDE + (A_ETIQ,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
           t, fill=BRANCO, font=fnt)


def preparar(nome, corte, esquerda, direita):
    """Recorta e põe faixa clara de cada lado. Devolve a imagem e o deslocamento."""
    img = Image.open(os.path.join(SRC, nome)).convert("RGBA")
    dx = dy = 0
    if corte:
        img = img.crop(corte)
        dx, dy = -corte[0], -corte[1]
    if esquerda or direita:
        base = Image.new("RGBA", (img.width + esquerda + direita, img.height), FAIXA + (255,))
        base.paste(img, (esquerda, 0))
        img = base
        dx += esquerda
    return img, dx, dy


def annotate(nome, marcadores=(), corte=None, esquerda=0, direita=0, saida=None, r=None, w=None):
    img, dx, dy = preparar(nome, corte, esquerda, direita)
    W, H = img.size
    camada = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(camada)
    r = r or int(W * 0.0125)
    w = w or max(2, int(W * 0.0022))
    fnt = font(int(r * 1.25))
    for (num, ax, ay, bx, by) in marcadores:
        ax, bx = ax + dx, bx + dx
        ay, by = ay + dy, by + dy
        ang = math.atan2(ay - by, ax - bx)
        seta(d, bx + (r + 6) * math.cos(ang), by + (r + 6) * math.sin(ang), ax, ay, w)
        etiqueta(d, bx, by, r, num, fnt)
    Image.alpha_composite(img, camada).convert("RGB").save(os.path.join(OUT, saida or nome))
    print("OK", saida or nome, W, H, f"({len(marcadores)} seta(s))")


def forma(nome, marcadores=(), y0=170, y1=1180, **kw):
    """Coluna do formulário, recortada, com faixa clara dos dois lados."""
    annotate(nome, marcadores=marcadores, corte=(FORM_X0, y0, FORM_X1, y1),
             esquerda=MARGEM, direita=MARGEM, r=28, w=4, **kw)


# =====================================================================================
# Onde a configuração mora
# =====================================================================================

# 01 — a tela inteira, como contexto: o item no menu do Cardápio Digital e a aba no topo.
# Faixa dos dois lados, porque um alvo está na borda esquerda e o outro na direita.
annotate(
    "01-aba-botao-whatsapp.png",
    saida="01-onde-fica.png",
    esquerda=MARGEM, direita=MARGEM,
    marcadores=(
        (1, 10, 864, -MARGEM // 2, 864),          # menu lateral: Botão WhatsApp
        # A seta da aba chega pela linha de baixo: na altura do rótulo ela terminaria no
        # ícone de recarregar, que mora logo depois da última aba.
        (2, 2085, 172, 2160 + MARGEM // 2, 172),  # aba Botão WhatsApp, no topo
    ),
    r=30, w=5,
)

# 02 — ligar e dizer para onde a mensagem vai. Mesmo print da 01, recortado na coluna do
# formulário: a chave fica na borda direita do cartão, e por isso a etiqueta 1 vem da faixa
# da direita.
forma(
    "01-aba-botao-whatsapp.png",
    saida="02-ligar-e-telefone.png",
    y0=180, y1=985,
    marcadores=(
        (1, 1497, 240, DIR, 240),      # chave que liga o botão
        (2, 404, 609, ESQ, 609),       # telefone com DDI e DDD
        (3, 404, 800, ESQ, 800),       # mensagem que o cliente já encontra escrita
    ),
)

# =====================================================================================
# Onde o botão aparece, e com que cara
# =====================================================================================

forma(
    "03-onde-o-botao-aparece.png",
    y0=170, y1=1150,
    marcadores=(
        (1, 404, 300, ESQ, 300),       # posição: flutuante sobre o cardápio
        # Uma seta para as duas chaves, e não uma para cada: a linha de texto logo abaixo
        # atravessa a imagem inteira, e qualquer seta vinda de baixo cortaria essa frase.
        (2, 404, 1023, ESQ, 1023),     # celular e tablet / computador
    ),
)

forma(
    "04-formato-do-botao.png",
    y0=170, y1=1175,
    marcadores=(
        (1, 1497, 380, DIR, 380),      # formato: pílula
        (2, 404, 739, ESQ, 739),       # tamanho
        (3, 404, 904, ESQ, 904),       # texto do botão
        (4, 1497, 904, DIR, 904),      # lado da tela: direita
        (5, 404, 1061, ESQ, 1061),     # cor do botão
    ),
)

# 05 — a prévia, que é o que evita publicar para testar. Recorte no aparelho desenhado.
annotate(
    "05-previa-celular.png",
    saida="05-previa.png",
    corte=(PREV_X0, 180, PREV_X1, 1470),
    esquerda=MARGEM, direita=MARGEM,
    marcadores=(
        (1, 1679, 227, ESQ_PREV, 227),        # celular / computador
        (2, 2056, 1067, DIR_PREV, 1067),      # o botão desenhado na prévia
        (3, 1626, 1383, ESQ_PREV, 1383),      # loja aberta / com itens na sacola
    ),
    r=28, w=4,
)


# =====================================================================================
# Como fica no cardápio do cliente
# =====================================================================================

# 06 — computador: viewport 1440x900 em DPR 1.5. O botão encosta a 24 px da borda.
annotate(
    "07-cardapio-computador.png",
    saida="06-cardapio-computador.png",
    direita=MARGEM,
    marcadores=(
        (1, 2128, 1281, 2160 + MARGEM // 2, 1281),
    ),
    r=30, w=5,
)

# 07 — celular: viewport 390x844 em DPR 2. A faixa é mais estreita porque a imagem é também.
annotate(
    "08-cardapio-celular.png",
    saida="07-cardapio-celular.png",
    direita=120,
    marcadores=(
        (1, 752, 1508, 840, 1508),
    ),
    r=24, w=4,
)
