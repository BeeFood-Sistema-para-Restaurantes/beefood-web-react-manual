"""Anota screenshots — #72 Ficha Técnica.

Coordenadas em frações (0..1), independentes da resolução.
Rodar dentro da pasta do manual: python annotate.py
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
A_LINE = 220
A_BADGE = 235
FONT_CANDIDATES = [
    r"C:\Windows\Fonts\arialbd.ttf",
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def font(sz):
    for c in FONT_CANDIDATES:
        if os.path.exists(c):
            return ImageFont.truetype(c, sz)
    raise RuntimeError("fonte bold nao encontrada")


def draw_arrow(d, x0, y0, x1, y1, w):
    col = GREEN + (A_LINE,)
    d.line([(x0, y0), (x1, y1)], fill=col, width=w)
    ang = math.atan2(y1 - y0, x1 - x0)
    L = w * 3.6
    for s in (0.45, -0.45):
        d.line([(x1, y1), (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))], fill=col, width=w)


def badge(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], fill=WHITE + (235,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN + (A_BADGE,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]), t, fill=WHITE, font=fnt)


def annotate(name, markers):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    W, H = img.size
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = int(W * 0.0125)
    fnt = font(int(r * 1.2))
    w = max(2, int(W * 0.0022))
    for (num, tx, ty, bx, by) in markers:
        TX, TY = tx * W, ty * H
        BX, BY = bx * W, by * H
        ang = math.atan2(TY - BY, TX - BX)
        sx = BX + (r + 5) * math.cos(ang)
        sy = BY + (r + 5) * math.sin(ang)
        draw_arrow(d, sx, sy, TX, TY, w)
        badge(d, BX, BY, r, num, fnt)
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, name))
    print("OK", name, W, H)


def passthrough(name):
    """Imagem de contexto: entra no manual sem setas."""
    Image.open(os.path.join(SRC, name)).convert("RGB").save(os.path.join(OUT, name))
    print("CTX", name)


# ---------------------------------------------------------------- insumo

annotate("01-insumos-lista.png", [
    (1, 0.205, 0.185, 0.300, 0.088),
    (2, 0.512, 0.318, 0.600, 0.250),
    (3, 0.640, 0.243, 0.800, 0.180),
])

annotate("02-insumo-cadastro.png", [
    (1, 0.222, 0.394, 0.270, 0.320),
    (2, 0.215, 0.518, 0.245, 0.620),
    (3, 0.430, 0.518, 0.480, 0.620),
    (4, 0.610, 0.755, 0.700, 0.690),
])

annotate("03-insumo-estoque.png", [
    (1, 0.452, 0.247, 0.410, 0.180),
    (2, 0.220, 0.375, 0.250, 0.460),
    (3, 0.680, 0.375, 0.760, 0.460),
])

# ---------------------------------------------------------------- ficha do lanche

annotate("04-ficha-adicionar.png", [
    (1, 0.200, 0.298, 0.220, 0.375),
    (2, 0.600, 0.298, 0.590, 0.380),
    (3, 0.702, 0.298, 0.720, 0.380),
    (4, 0.760, 0.298, 0.860, 0.375),
])

annotate("05-ficha-completa.png", [
    (1, 0.545, 0.494, 0.440, 0.440),
    (2, 0.720, 0.494, 0.860, 0.440),
    (3, 0.640, 0.808, 0.450, 0.875),
])

annotate("06-produto-custos.png", [
    (1, 0.320, 0.530, 0.330, 0.662),
    (2, 0.500, 0.530, 0.545, 0.662),
    (3, 0.690, 0.530, 0.760, 0.662),
    (4, 0.820, 0.462, 0.925, 0.412),
])

# ---------------------------------------------------------------- adicionais e porção

annotate("07-ficha-adicional-carne.png", [
    (1, 0.302, 0.175, 0.400, 0.230),
    (2, 0.700, 0.447, 0.845, 0.400),
    (3, 0.690, 0.103, 0.640, 0.190),
])

passthrough("08-ficha-adicional-bacon.png")

annotate("09-ficha-porcao.png", [
    (1, 0.540, 0.439, 0.440, 0.439),
    (2, 0.540, 0.548, 0.440, 0.548),
    (3, 0.650, 0.595, 0.580, 0.665),
])

annotate("10-estoque-coluna-ficha.png", [
    (1, 0.858, 0.318, 0.860, 0.245),
    (2, 0.845, 0.420, 0.940, 0.470),
    (3, 0.462, 0.420, 0.400, 0.470),
])

# ---------------------------------------------------------------- prova

annotate("11-pdv-dois-adicionais.png", [
    (1, 0.398, 0.420, 0.255, 0.420),
    (2, 0.665, 0.581, 0.775, 0.620),
    (3, 0.470, 0.882, 0.290, 0.905),
])

annotate("12-movimentacoes-venda.png", [
    (1, 0.500, 0.240, 0.425, 0.185),
    (2, 0.670, 0.240, 0.870, 0.185),
    (3, 0.500, 0.562, 0.425, 0.607),
])

# ---------------------------------------------------------------- manutenção

annotate("13-ficha-editar-linha.png", [
    (1, 0.505, 0.766, 0.400, 0.766),
    (2, 0.792, 0.752, 0.880, 0.815),
])

annotate("14-ficha-remover.png", [
    (1, 0.600, 0.531, 0.700, 0.585),
])

annotate("15-insumo-receita.png", [
    (1, 0.300, 0.519, 0.230, 0.450),
    (2, 0.300, 0.584, 0.240, 0.655),
])

print("done")
