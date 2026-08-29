"""Anota screenshots — #19 Cashback configurar."""
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
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, name))
    print("OK", name)


annotate("01-crm-cashback-config.png", [
    (1, 0.078, 0.305, 0.175, 0.240),
    (2, 0.225, 0.095, 0.360, 0.055),
    (3, 0.300, 0.325, 0.200, 0.400),
    (4, 0.300, 0.530, 0.200, 0.600),
])
annotate("02-limites-canais.png", [
    (1, 0.300, 0.175, 0.200, 0.115),
    (2, 0.300, 0.285, 0.200, 0.345),
    (3, 0.600, 0.195, 0.780, 0.140),
    (4, 0.720, 0.415, 0.860, 0.360),
])
annotate("03-percentual-dias.png", [
    (1, 0.400, 0.155, 0.200, 0.230),
    (2, 0.300, 0.480, 0.180, 0.400),
    (3, 0.400, 0.700, 0.200, 0.640),
    (4, 0.450, 0.860, 0.200, 0.920),
])
annotate("04-cardapio-digital-redirect.png", [
    (1, 0.080, 0.580, 0.180, 0.500),
    (2, 0.550, 0.680, 0.550, 0.380),
])
annotate("05-cardapio-banner.png", [
    (1, 0.500, 0.390, 0.160, 0.300),
])
annotate("06-cardapio-identificar.png", [
    (1, 0.500, 0.255, 0.160, 0.155),
    (2, 0.500, 0.345, 0.160, 0.430),
])
print("done")
