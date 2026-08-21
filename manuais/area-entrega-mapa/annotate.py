"""Anota os screenshots do manual BeeFood - Area de entrega por mapa (#35).

Painel 2160x1350; cardapio digital 1170x2532 (viewport 390x844, DPR 3).
"""
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


def annotate(name, markers, raio=0.0125, out_name=None):
    if not os.path.exists(os.path.join(SRC, name)):
        print("SKIP", name)
        return
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
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, out_name or name))
    print("OK", out_name or name)


annotate("02-step2-tipos.png", [
    (1, 0.500, 0.210, 0.280, 0.155),
    (2, 0.450, 0.380, 0.450, 0.500),
    (3, 0.500, 0.800, 0.500, 0.700),
])

annotate("03-nova-regiao-tipo.png", [
    (1, 0.380, 0.520, 0.280, 0.400),
    (2, 0.520, 0.520, 0.620, 0.400),
    (3, 0.900, 0.300, 0.740, 0.280),
    (4, 0.900, 0.370, 0.740, 0.400),
    (5, 0.860, 0.530, 0.740, 0.600),
    (6, 0.820, 0.640, 0.740, 0.720),
])

annotate("04b-form-circulo-campos.png", [
    (1, 0.420, 0.520, 0.260, 0.380),
    (2, 0.900, 0.300, 0.740, 0.260),
    (3, 0.820, 0.620, 0.720, 0.560),
    (4, 0.920, 0.620, 0.900, 0.560),
    (5, 0.820, 0.700, 0.720, 0.760),
    (6, 0.920, 0.700, 0.900, 0.760),
    (7, 0.900, 0.900, 0.780, 0.840),
])

annotate("04c-nao-entrega.png", [
    (1, 0.900, 0.370, 0.740, 0.320),
    (2, 0.420, 0.520, 0.260, 0.400),
    (3, 0.860, 0.560, 0.740, 0.620),
    (4, 0.900, 0.900, 0.780, 0.840),
])

annotate("04d-desenhando-poligono.png", [
    (1, 0.500, 0.280, 0.500, 0.200),
    (2, 0.500, 0.780, 0.500, 0.700),
    (3, 0.500, 0.840, 0.280, 0.840),
    (4, 0.900, 0.640, 0.740, 0.560),
])

annotate("01-step3-regioes.png", [
    (1, 0.400, 0.205, 0.280, 0.300),
    (2, 0.480, 0.550, 0.300, 0.550),
    (3, 0.900, 0.480, 0.780, 0.380),
    (4, 0.900, 0.900, 0.780, 0.800),
])

annotate("05-editar-regiao.png", [
    (1, 0.420, 0.520, 0.260, 0.380),
    (2, 0.900, 0.640, 0.740, 0.560),
    (3, 0.900, 0.900, 0.780, 0.800),
])

if os.path.exists(os.path.join(SRC, "07-menu-dentro-area.png")):
    annotate("07-menu-dentro-area.png", [
        (1, 0.50, 0.16, 0.16, 0.10),
        (2, 0.38, 0.30, 0.16, 0.28),
        (3, 0.38, 0.36, 0.16, 0.42),
    ], raio=0.028)

if os.path.exists(os.path.join(SRC, "09-menu-fora-area.png")):
    annotate("09-menu-fora-area.png", [
        (1, 0.42, 0.36, 0.16, 0.42),
        (2, 0.50, 0.46, 0.16, 0.52),
    ], raio=0.028)
