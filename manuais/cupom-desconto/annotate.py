"""Anota screenshots — setas verdes + badges. Coordenadas em fracoes 0..1."""
import os, math
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
    raise RuntimeError("fonte bold nao encontrada")


def draw_arrow(d, x0, y0, x1, y1, w):
    col = GREEN + (A_LINE,)
    d.line([(x0, y0), (x1, y1)], fill=col, width=w)
    ang = math.atan2(y1 - y0, x1 - x0)
    L = w * 3.6
    for s in (0.45, -0.45):
        xa = x1 - L * math.cos(ang - s)
        ya = y1 - L * math.sin(ang - s)
        d.line([(x1, y1), (xa, ya)], fill=col, width=w)


def badge(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], fill=WHITE + (235,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN + (A_BADGE,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    d.text((cx - tw / 2 - bb[0], cy - th / 2 - bb[1]), t, fill=WHITE, font=fnt)


def annotate(name, markers, ring=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    W, H = img.size
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = int(W * 0.0125)
    fnt = font(int(r * 1.2))
    w = max(2, int(W * 0.0022))
    for (fx, fy, fw, fh) in (ring or []):
        x0, y0 = fx * W, fy * H
        d.rectangle([x0, y0, x0 + fw * W, y0 + fh * H], outline=GREEN + (A_LINE,), width=w)
    for (num, tx, ty, bx, by) in markers:
        TX, TY = tx * W, ty * H
        BX, BY = bx * W, by * H
        ang = math.atan2(TY - BY, TX - BX)
        sx = BX + (r + 5) * math.cos(ang)
        sy = BY + (r + 5) * math.sin(ang)
        draw_arrow(d, sx, sy, TX, TY, w)
        badge(d, BX, BY, r, num, fnt)
    out_img = Image.alpha_composite(img, overlay).convert("RGB")
    out_img.save(os.path.join(OUT, name))
    print("OK", name)


annotate("01-lista-cupons.png", [
    (1, 0.085, 0.280, 0.200, 0.230),
    (2, 0.233, 0.146, 0.380, 0.130),
])
annotate("02-modal-novo-topo.png", [
    (1, 0.291, 0.178, 0.200, 0.140),
    (2, 0.290, 0.284, 0.200, 0.340),
    (3, 0.295, 0.444, 0.200, 0.500),
    (4, 0.629, 0.174, 0.760, 0.140),
    (5, 0.700, 0.360, 0.800, 0.400),
])
annotate("03-modal-novo-regras.png", [
    (1, 0.299, 0.237, 0.200, 0.190),
    (2, 0.525, 0.237, 0.640, 0.190),
    (3, 0.618, 0.636, 0.760, 0.600),
])
annotate("04-modal-avancado.png", [
    (1, 0.500, 0.430, 0.280, 0.390),
    (2, 0.420, 0.560, 0.260, 0.620),
])
annotate("05-cardapio-banner.png", [
    (1, 0.505, 0.030, 0.220, 0.090),
])
annotate("06-cardapio-lista-cupons.png", [
    (1, 0.500, 0.145, 0.220, 0.145),
    (2, 0.500, 0.420, 0.180, 0.380),
])
print("done")
