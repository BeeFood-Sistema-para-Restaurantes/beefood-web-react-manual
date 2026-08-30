"""Anota screenshots — #67 Lançamentos: contas a receber."""
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
    print("OK", name, W, H)


annotate("01-receber-vendas.png", [
    (1, 0.370, 0.085, 0.370, 0.165),
    (2, 0.500, 0.355, 0.300, 0.290),
    (3, 0.860, 0.355, 0.930, 0.270),
])
annotate("02-detalhe-venda.png", [
    (1, 0.450, 0.560, 0.280, 0.500),
    (2, 0.380, 0.600, 0.260, 0.680),
    (3, 0.620, 0.280, 0.760, 0.220),
])
annotate("03-receita-extra.png", [
    (1, 0.400, 0.220, 0.280, 0.165),
    (2, 0.650, 0.220, 0.780, 0.165),
    (3, 0.610, 0.420, 0.780, 0.420),
    (4, 0.400, 0.500, 0.260, 0.560),
    (5, 0.680, 0.880, 0.780, 0.820),
])
annotate("04-lista-receita.png", [
    (1, 0.330, 0.355, 0.250, 0.280),
    (2, 0.620, 0.355, 0.720, 0.280),
    (3, 0.860, 0.355, 0.930, 0.430),
])
annotate("05-todos.png", [
    (1, 0.580, 0.085, 0.580, 0.165),
    (2, 0.720, 0.155, 0.850, 0.155),
    (3, 0.440, 0.355, 0.280, 0.430),
])
print("done")
