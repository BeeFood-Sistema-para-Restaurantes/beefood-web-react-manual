"""Anota os screenshots do #100 — Tradução do cardápio presencial.

Coordenadas em pixels da imagem final (2160x1350). Cada seta sai de um
espaço vazio e mira a borda do elemento, nunca o meio do texto.
"""
import os
import math
from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
A_LINE = 235
A_BADGE = 245
FONT_CANDIDATES = [
    r"C:\Windows\Fonts\arialbd.ttf",
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


def annotate(name, markers=(), ring=(), crop=None, pad_right=0, pad_top=0, r=None, w=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    if crop:
        img = img.crop(crop)
    if pad_right or pad_top:
        base = Image.new("RGBA", (img.width + pad_right, img.height + pad_top),
                         WHITE + (255,))
        base.paste(img, (0, pad_top))
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
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, name))
    print("OK", name, W, H)


# --- 01 Setor em português: onde ficam as bandeiras --------------------------
annotate("01-setor-bandeiras.png",
         markers=[(1, 1612, 327, 1761, 327)],
         ring=[(1470, 298, 1610, 358)])

# --- 02 Setor em inglês: bandeira ativa + campo traduzido -------------------
annotate("02-setor-ingles.png",
         markers=[(1, 1554, 297, 1554, 221),
                  (2, 1611, 394, 1761, 394)],
         ring=[(839, 363, 1616, 426)])

# --- 03 Produto: nome e descrição no idioma escolhido -----------------------
annotate("03-produto-ingles.png",
         markers=[(1, 943, 289, 1139, 289),
                  (2, 1808, 844, 1951, 844)],
         ring=[(726, 262, 945, 319)])

# --- 04 Complemento ---------------------------------------------------------
annotate("04-complemento-ingles.png",
         markers=[(1, 774, 297, 949, 297)],
         ring=[(561, 270, 776, 327)])

# --- 05 Grupo de opções -----------------------------------------------------
annotate("05-grupo-opcoes-ingles.png",
         markers=[(1, 1029, 302, 1181, 302)],
         ring=[(886, 274, 1034, 331)])

# --- 06 Totem: Habilitar tradução -------------------------------------------
annotate("06-totem-idiomas.png",
         markers=[(1, 475, 757, 359, 757)],
         ring=[(443, 633, 1073, 953)])

# --- 07/08/09 telas do cliente (imagens enviadas pelo dono, resolução menor) -
# 07 Totem, tela inicial: bandeiras embaixo do FAÇA SEU PEDIDO (recorte tira a
# borda vazia da tela do totem; dx=-40, dy=-175)
annotate("07-totem-iniciar-idioma.png",
         crop=(40, 175, 1095, 650),
         markers=[(1, 418, 370, 310, 370)],
         ring=[(422, 330, 636, 411)],
         r=15, w=3)

# 08 Totem, menu: faixa branca em cima para o número do seletor de idioma
annotate("08-totem-menu-idioma.png",
         pad_top=100,
         markers=[(1, 1044, 130, 1044, 52),
                  (2, 80, 321, 205, 321),
                  (3, 184, 388, 205, 358)],
         ring=[(938, 133, 1150, 199)],
         r=15, w=3)

# 09 Tablet: produto traduzido, produto sem tradução e bandeiras da lateral
annotate("09-tablet-coca-traduzida.png",
         markers=[(1, 858, 208, 960, 172),
                  (2, 95, 668, 190, 630),
                  (3, 932, 480, 1000, 480)],
         ring=[(688, 204, 852, 290), (688, 438, 928, 524), (40, 624, 92, 756)],
         r=15, w=3)

print("done")
