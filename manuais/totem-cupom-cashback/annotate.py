"""Anota os screenshots do #122 — Cupom e cashback no totem.

Coordenadas em pixels **da imagem já recortada** (o recorte entra antes das
setas). Cada seta sai de um espaço vazio e mira a borda do elemento, nunca o
meio do texto.

Três padrões de recorte:

- **Página do painel**: sai a barra de cima (o "Indique e ganhe!") e entra uma
  faixa branca no alto, onde ficam as etiquetas do menu lateral.
- **Modal do cupom**: recorta no modal e cola faixa branca — à esquerda quando a
  seta vem da margem, à direita quando o alvo é o interruptor no fim da linha.
- **Totem** (1080x1920): a barra de cima desenha o logotipo retangular da loja
  dentro de um espaço quadrado e ele sai cortado; onde ela não ensina nada, o
  recorte a deixa de fora.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
A_LINE = 235
A_BADGE = 245
FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def font(sz):
    for caminho in FONT_CANDIDATES:
        if os.path.exists(caminho):
            return ImageFont.truetype(caminho, sz)
    raise RuntimeError("nenhuma fonte bold encontrada")


def draw_arrow(d, x0, y0, x1, y1, w):
    col = GREEN + (A_LINE,)
    d.line([(x0, y0), (x1, y1)], fill=col, width=w)
    ang = math.atan2(y1 - y0, x1 - x0)
    L = w * 4.0
    for s in (0.5, -0.5):
        d.line([(x1, y1), (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))],
               fill=col, width=w)


def badge(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 3, cy - r - 3, cx + r + 3, cy + r + 3], fill=WHITE + (245,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN + (A_BADGE,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
           t, fill=WHITE, font=fnt)


def annotate(name, markers=(), ring=(), crop=None, pad_left=0, pad_top=0,
             pad_right=0, r=None, w=None, out_name=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    if crop:
        img = img.crop(crop)
    if pad_left or pad_top or pad_right:
        base = Image.new("RGBA",
                         (img.width + pad_left + pad_right, img.height + pad_top),
                         WHITE + (255,))
        base.paste(img, (pad_left, pad_top))
        img = base
    W, H = img.size
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = r or int(W * 0.0125)
    fnt = font(int(r * 1.25))
    w = w or max(2, int(W * 0.0022))
    for (x0, y0, x1, y1) in ring:
        d.rounded_rectangle([x0, y0, x1, y1], radius=int(r * 0.6),
                            outline=GREEN + (A_LINE,), width=w)
    for (num, tx, ty, bx, by) in markers:
        ang = math.atan2(ty - by, tx - bx)
        draw_arrow(d, bx + (r + 6) * math.cos(ang), by + (r + 6) * math.sin(ang),
                   tx, ty, w)
        badge(d, bx, by, r, num, fnt)
    Image.alpha_composite(img, overlay).convert("RGB").save(
        os.path.join(OUT, out_name or name))
    print("OK", out_name or name, W, H)


# Página do painel sem a barra de cima, com faixa branca no alto.
PAGINA = dict(crop=(0, 86, 2160, 1290), pad_top=110, r=27, w=4)
# O aparelho sem a barra de cima (o logotipo retangular sai cortado nela).
TOTEM = dict(crop=(0, 88, 1080, 1920), r=17, w=3)

# --- 01 A lista de cupons filtrada pelo canal Totem ------------------------
annotate("01-crm-cupons-canal-totem.png",
         markers=[(1, 295, 403, 295, 55),
                  (2, 1135, 329, 1290, 384),
                  (3, 760, 754, 880, 754)],
         **PAGINA)

# --- 02 O cupom: canal Totem à esquerda, regras à direita ------------------
# Modal de x=500 a x=1660 e de y=70 a y=1290. A faixa de 160 px à direita
# recebe as etiquetas dos interruptores, que ficam no fim de cada linha.
annotate("02-crm-cupom-canais-regras.png",
         crop=(500, 70, 1660, 1290), pad_right=160, r=25, w=4,
         markers=[(1, 445, 400, 445, 560),
                  (2, 1090, 540, 1240, 540),
                  (3, 1090, 690, 1240, 690)])

# --- 03 O cupom: configurações avançadas -----------------------------------
annotate("03-crm-cupom-avancadas.png",
         crop=(500, 70, 1660, 1290), pad_left=150, r=25, w=4,
         markers=[(1, 220, 268, 70, 268),
                  (2, 225, 575, 70, 575),
                  (3, 225, 825, 70, 825),
                  (4, 225, 957, 70, 957)])

# --- 04 Cashback: o programa e a modalidade Totem --------------------------
annotate("04-crm-cashback-modalidades.png",
         markers=[(1, 295, 456, 295, 55),
                  (2, 490, 434, 370, 434),
                  (3, 520, 729, 390, 729),
                  (4, 1240, 964, 1120, 964)],
         **PAGINA)

# --- 05 Cashback: o percentual que o totem anuncia -------------------------
annotate("05-crm-cashback-percentual.png",
         crop=(300, 620, 1990, 1350), r=25, w=4,
         markers=[(1, 1210, 92, 1100, 92),
                  (2, 1060, 350, 1150, 350),
                  (3, 705, 450, 530, 450)])

# --- 06 Totem: a identificação que oferece o cashback ----------------------
annotate("06-totem-identificacao-cashback.png",
         markers=[(1, 255, 300, 120, 300),
                  (2, 250, 1633, 150, 1633),
                  (3, 425, 1757, 250, 1757)],
         **TOTEM)

# --- 07 Totem: a confirmação com cupom e cashback --------------------------
annotate("07-totem-confirmacao-cupom-cashback.png",
         markers=[(1, 745, 532, 480, 532),
                  (2, 870, 662, 600, 662),
                  (3, 960, 1650, 780, 1650)],
         **TOTEM)

# --- 08 Totem: a lista de cupons com as regras em texto -------------------
annotate("08-totem-cupons-regras.png", crop=(0, 88, 1080, 1520), r=17, w=3,
         markers=[(1, 405, 369, 560, 369),
                  (2, 420, 424, 700, 424),
                  (3, 520, 602, 680, 602)])
