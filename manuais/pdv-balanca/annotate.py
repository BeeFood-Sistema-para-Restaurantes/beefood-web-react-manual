"""Anota os screenshots do manual BeeFood - PDV balanca (#46)."""
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
    raise RuntimeError("nenhuma fonte bold encontrada")


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


def passthrough(name):
    img = Image.open(os.path.join(SRC, name)).convert("RGB")
    img.save(os.path.join(OUT, name))
    print("OK (contexto)", name)


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



annotate("02-digitos-2-6.png", [
    (1, 0.812, 0.480, 0.900, 0.420),
    (2, 0.500, 0.560, 0.280, 0.520),
    (3, 0.360, 0.680, 0.220, 0.740),
    (4, 0.620, 0.680, 0.780, 0.740),
])
annotate("04-cadastro-queijo.png", [
    (1, 0.280, 0.280, 0.180, 0.180),
    (2, 0.520, 0.360, 0.700, 0.300),
    (3, 0.520, 0.500, 0.700, 0.560),
    (4, 0.420, 0.300, 0.280, 0.220),
])
annotate("05-pdv-vazio.png", [
    (1, 0.420, 0.160, 0.280, 0.080),
    (2, 0.280, 0.360, 0.180, 0.280),
])
annotate("07-pdv-queijo-0350.png", [
    (1, 0.820, 0.160, 0.920, 0.080),
    (2, 0.280, 0.300, 0.180, 0.220),
    (3, 0.860, 0.520, 0.920, 0.620),
])
annotate("08-tipo-valor.png", [
    (1, 0.500, 0.560, 0.280, 0.500),
    (2, 0.400, 0.700, 0.220, 0.780),
])
annotate("10-pdv-queijo-0500.png", [
    (1, 0.820, 0.160, 0.920, 0.080),
    (2, 0.280, 0.300, 0.180, 0.220),
    (3, 0.860, 0.520, 0.920, 0.620),
])
passthrough("01-bloco-balanca.png")
annotate("06-pdv-digitando-ean.png", [
    (1, 0.420, 0.160, 0.280, 0.080),
])
passthrough("09-pdv-digitando-valor.png")

print('done')
