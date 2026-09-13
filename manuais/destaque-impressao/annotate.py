"""Anota os screenshots do #99 — Destaque na impressão."""
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


def annotate(name, markers=(), ring=(), crop=None, pad_right=0, r=None, w=None):
    """Marcadores e molduras em pixels da imagem final (após crop e pad)."""
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    W0, H0 = img.size
    if crop:
        img = img.crop(crop)
    if pad_right:
        base = Image.new("RGBA", (img.width + pad_right, img.height), WHITE + (255,))
        base.paste(img, (0, 0))
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


# --- Cadastro do produto (2160x1350): switch "Destaque na impressão" ---------
annotate("01-cadastro-produto.png",
         markers=[(1, 634, 987, 520, 987)],
         ring=[(640, 953, 1222, 1024)])

# --- Cadastro do complemento (2160x1350) -------------------------------------
annotate("02-cadastro-complemento.png",
         markers=[(1, 474, 913, 360, 913)],
         ring=[(480, 881, 1102, 948)])

# --- Editar em Lote (2160x1350): card do campo + botão PROCESSAR -------------
annotate("03-editar-lote.png",
         markers=[(1, 1548, 690, 1664, 690),
                  (2, 1552, 1181, 1668, 1181)],
         ring=[(620, 641, 1542, 738),
               (1304, 1150, 1549, 1212)])

# --- Detalhe da venda (contexto: o que foi pedido) ---------------------------
annotate("04-detalhe-venda.png",
         ring=[(598, 372, 1564, 710)])

# --- Cupom Pedido (600x1950): faixa branca à direita para os números --------
annotate("05-cupom-pedido.png",
         markers=[(1, 533, 365, 664, 365),
                  (2, 533, 413, 664, 413),
                  (3, 533, 553, 664, 553)],
         crop=(0, 0, 600, 992), pad_right=170, r=19, w=3)

# --- Cupom da Cozinha (600x1950) --------------------------------------------
annotate("06-cupom-cozinha.png",
         markers=[(1, 533, 300, 664, 300),
                  (2, 533, 347, 664, 347),
                  (3, 533, 437, 664, 437)],
         crop=(0, 0, 600, 568), pad_right=170, r=19, w=3)

print("done")
