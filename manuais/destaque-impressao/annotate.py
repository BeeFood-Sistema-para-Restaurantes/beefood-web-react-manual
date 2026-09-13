"""Anota os screenshots do #99 — Destaque na impressão."""
import os
import math
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
    for caminho in FONT_CANDIDATES:
        if os.path.exists(caminho):
            return ImageFont.truetype(caminho, sz)
    raise RuntimeError("nenhuma fonte bold encontrada")


def draw_arrow(d, x0, y0, x1, y1, w):
    col = GREEN + (A_LINE,)
    d.line([(x0, y0), (x1, y1)], fill=col, width=w)
    ang = math.atan2(y1 - y0, x1 - x0)
    L = w * 3.6
    for s in (0.45, -0.45):
        d.line([(x1, y1), (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))],
               fill=col, width=w)


def badge(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], fill=WHITE + (235,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN + (A_BADGE,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
           t, fill=WHITE, font=fnt)


def annotate(name, markers, ring=None, crop=None, rmin=0):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    W0, H0 = img.size
    if crop:
        img = img.crop((int(crop[0] * W0), int(crop[1] * H0),
                        int(crop[2] * W0), int(crop[3] * H0)))
    W, H = img.size
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = max(rmin, int(W * 0.0125))
    fnt = font(int(r * 1.2))
    w = max(2, int(W * 0.0022))
    for (fx, fy, fw, fh) in (ring or []):
        x0, y0 = fx * W, fy * H
        d.rectangle([x0, y0, x0 + fw * W, y0 + fh * H], outline=GREEN + (A_LINE,), width=w)
    for (num, tx, ty, bx, by) in markers:
        TX, TY, BX, BY = tx * W, ty * H, bx * W, by * H
        ang = math.atan2(TY - BY, TX - BX)
        draw_arrow(d, BX + (r + 5) * math.cos(ang), BY + (r + 5) * math.sin(ang), TX, TY, w)
        badge(d, BX, BY, r, num, fnt)
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, name))
    print("OK", name, W, H)


annotate("01-cadastro-produto.png", [
    (1, 0.255, 0.722, 0.155, 0.630),  # switch Destaque na impressão
])

annotate("02-cadastro-complemento.png", [
    (1, 0.255, 0.668, 0.155, 0.575),  # switch no Molho verde
])

annotate("03-editar-lote.png", [
    (1, 0.305, 0.500, 0.185, 0.400),  # checkbox do campo
    (2, 0.700, 0.855, 0.830, 0.760),  # PROCESSAR
], ring=[
    (0.285, 0.455, 0.430, 0.085),  # card Destaque na impressão
])

annotate("04-detalhe-venda.png", [
    (1, 0.655, 0.088, 0.575, 0.175),  # impressora do cupom
    (2, 0.688, 0.088, 0.780, 0.175),  # chapéu da cozinha
])

annotate("05-cupom-pedido.png", [
    (1, 0.04, 0.355, 0.93, 0.355),
    (2, 0.04, 0.405, 0.93, 0.405),
    (3, 0.04, 0.548, 0.93, 0.548),
], crop=(0.0, 0.0, 1.0, 0.50), rmin=16)

annotate("06-cupom-cozinha.png", [
    (1, 0.04, 0.445, 0.93, 0.445),
    (2, 0.04, 0.505, 0.93, 0.505),
    (3, 0.04, 0.700, 0.93, 0.700),
], crop=(0.0, 0.0, 1.0, 0.32), rmin=16)

print("done")
