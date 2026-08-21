"""Anota os screenshots do manual BeeFood - Area de entrega por KM (#36)."""
import os, math
from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)
GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
A_LINE, A_BADGE = 220, 235
FONT_CANDIDATES = [
    r"C:\Windows\Fonts\arialbd.ttf",
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def font(sz):
    for c in FONT_CANDIDATES:
        if os.path.exists(c):
            return ImageFont.truetype(c, sz)
    raise RuntimeError("fonte")


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


def annotate(name, markers, raio=0.0125):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    W, H = img.size
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = int(W * raio)
    fnt = font(int(r * 1.2))
    w = max(2, int(W * 0.0022))
    for (num, tx, ty, bx, by) in markers:
        TX, TY, BX, BY = tx * W, ty * H, bx * W, by * H
        ang = math.atan2(TY - BY, TX - BX)
        draw_arrow(d, BX + (r + 5) * math.cos(ang), BY + (r + 5) * math.sin(ang), TX, TY, w)
        badge(d, BX, BY, r, num, fnt)
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, name))
    print("OK", name)


annotate("01-step2-km.png", [
    (1, 0.500, 0.210, 0.280, 0.155),
    (2, 0.300, 0.380, 0.280, 0.500),
    (3, 0.500, 0.800, 0.500, 0.700),
])

annotate("03-modal-km-vazio.png", [
    (1, 0.500, 0.320, 0.300, 0.280),
    (2, 0.620, 0.320, 0.780, 0.280),
    (3, 0.500, 0.400, 0.300, 0.400),
    (4, 0.500, 0.470, 0.300, 0.500),
    (5, 0.500, 0.560, 0.300, 0.600),
    (6, 0.500, 0.640, 0.300, 0.700),
    (7, 0.620, 0.760, 0.780, 0.760),
])

annotate("04-modal-km-preenchido.png", [
    (1, 0.500, 0.320, 0.300, 0.280),
    (2, 0.500, 0.400, 0.300, 0.400),
    (3, 0.500, 0.470, 0.300, 0.500),
    (4, 0.500, 0.560, 0.300, 0.600),
    (5, 0.500, 0.640, 0.300, 0.700),
    (6, 0.620, 0.760, 0.780, 0.760),
])

annotate("05-lista-km-pronta.png", [
    (1, 0.400, 0.205, 0.280, 0.300),
    (2, 0.280, 0.360, 0.220, 0.300),
    (3, 0.500, 0.500, 0.280, 0.500),
    (4, 0.880, 0.460, 0.900, 0.360),
])

annotate("06-menu-km-busca.png", [
    (1, 0.50, 0.22, 0.16, 0.14),
    (2, 0.50, 0.34, 0.16, 0.44),
], raio=0.028)

annotate("07-menu-km-form.png", [
    (1, 0.36, 0.155, 0.14, 0.10),
    (2, 0.80, 0.155, 0.90, 0.10),
    (3, 0.36, 0.245, 0.14, 0.30),
    (4, 0.72, 0.56, 0.88, 0.50),
], raio=0.028)

annotate("08-menu-km-perto.png", [
    (1, 0.50, 0.18, 0.16, 0.10),
    (2, 0.42, 0.30, 0.16, 0.38),
], raio=0.028)
