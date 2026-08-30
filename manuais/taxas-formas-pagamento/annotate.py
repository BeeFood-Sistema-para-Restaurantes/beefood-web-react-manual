"""Anota screenshots — #65 Taxas das formas de recebimento."""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

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


def annotate(name, markers, ring=None, borrao=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    W, H = img.size
    for (fx, fy, fw, fh) in (borrao or []):
        caixa = (int(fx * W), int(fy * H), int((fx + fw) * W), int((fy + fh) * H))
        trecho = img.crop(caixa).filter(ImageFilter.GaussianBlur(radius=max(8, W // 120)))
        img.paste(trecho, caixa)
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


annotate("01-formas-pagamento.png", [
    (1, 0.090, 0.675, 0.200, 0.600),
    (2, 0.400, 0.800, 0.280, 0.720),
    (3, 0.780, 0.955, 0.780, 0.870),
])
annotate("02-debito-config.png", [
    (1, 0.400, 0.340, 0.280, 0.280),
    (2, 0.640, 0.340, 0.760, 0.280),
    (3, 0.680, 0.805, 0.820, 0.870),
], ring=[(0.575, 0.775, 0.145, 0.055)])
annotate("03-credito-config.png", [
    (1, 0.400, 0.340, 0.280, 0.280),
    (2, 0.640, 0.340, 0.760, 0.280),
    (3, 0.680, 0.805, 0.820, 0.870),
], ring=[(0.575, 0.775, 0.145, 0.055)])
annotate("04-vr-config.png", [
    (1, 0.400, 0.340, 0.280, 0.280),
    (2, 0.640, 0.340, 0.760, 0.280),
    (3, 0.680, 0.805, 0.820, 0.870),
], ring=[(0.575, 0.775, 0.145, 0.055)])
annotate("05-tabela-configurada.png", [
    (1, 0.720, 0.500, 0.220, 0.440),
    (2, 0.720, 0.660, 0.220, 0.740),
])
annotate("06-pdv-pago.png", [
    (1, 0.680, 0.545, 0.540, 0.480),
    (2, 0.812, 0.538, 0.910, 0.470),
])
annotate("07-detalhe-pagamento.png", [
    (1, 0.430, 0.560, 0.300, 0.500),
    (2, 0.580, 0.560, 0.710, 0.500),
    (3, 0.430, 0.645, 0.300, 0.730),
], borrao=[
    (0.240, 0.150, 0.220, 0.100),
    (0.580, 0.140, 0.250, 0.120),
])
annotate("08-desemp-recebimento.png", [
    (1, 0.195, 0.305, 0.290, 0.240),
    (2, 0.700, 0.348, 0.580, 0.280),
    (3, 0.800, 0.348, 0.900, 0.280),
    (4, 0.620, 0.775, 0.400, 0.850),
])
annotate("09-desemp-dados.png", [
    (1, 0.355, 0.155, 0.250, 0.105),
    (2, 0.220, 0.255, 0.140, 0.200),
    (3, 0.780, 0.340, 0.900, 0.280),
], borrao=[
    (0.300, 0.230, 0.200, 0.620),
])
print("done")
