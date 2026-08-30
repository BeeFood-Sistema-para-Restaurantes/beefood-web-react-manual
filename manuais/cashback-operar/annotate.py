"""Anota screenshots — #20 Cashback operar."""
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


PHONE_W = 380
GAP = 18
PAD = 22
CAP_H = 44


def montar_celulares(nome_out, paineis):
    """Junta prints de celular lado a lado. paineis: [(arquivo, titulo)]."""
    fnt = font(20)
    phones = []
    for nome, _ in paineis:
        im = Image.open(os.path.join(SRC, nome)).convert("RGB")
        h = int(im.height * PHONE_W / im.width)
        phones.append(im.resize((PHONE_W, h), Image.Resampling.LANCZOS))
    ph_h = phones[0].height
    n = len(phones)
    W = PAD * 2 + n * PHONE_W + (n - 1) * GAP
    H = PAD + CAP_H + ph_h + PAD
    canvas = Image.new("RGB", (W, H), (244, 244, 245))
    d = ImageDraw.Draw(canvas)
    for i, (im, (_, titulo)) in enumerate(zip(phones, paineis)):
        x = PAD + i * (PHONE_W + GAP)
        y = PAD + CAP_H
        bb = d.textbbox((0, 0), titulo, font=fnt)
        tw = bb[2] - bb[0]
        d.text((x + (PHONE_W - tw) / 2, PAD + 10), titulo, fill=(40, 40, 40), font=fnt)
        mask = Image.new("L", (PHONE_W, ph_h), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, PHONE_W - 1, ph_h - 1], radius=26, fill=255)
        canvas.paste(im, (x, y), mask)
        d.rounded_rectangle([x, y, x + PHONE_W - 1, y + ph_h - 1], radius=26, outline=(200, 200, 200), width=2)
    canvas.save(os.path.join(SRC, nome_out))
    print("MONTAR", nome_out, canvas.size)
    return W, H, ph_h


def no_painel(i, tx, ty, W, H, ph_h):
    x = PAD + i * (PHONE_W + GAP) + tx * PHONE_W
    y = PAD + CAP_H + ty * ph_h
    return x / W, y / H


annotate("01-historico.png", [
    (1, 0.325, 0.090, 0.420, 0.045),
    (2, 0.430, 0.145, 0.280, 0.110),
    (3, 0.280, 0.230, 0.180, 0.300),
    (4, 0.450, 0.480, 0.220, 0.400),
])
annotate("02-saldo-clientes.png", [
    (1, 0.400, 0.090, 0.500, 0.045),
    (2, 0.350, 0.265, 0.250, 0.210),
    (3, 0.350, 0.400, 0.250, 0.470),
    (4, 0.720, 0.265, 0.860, 0.210),
])
annotate("03-detalhe-cliente.png", [
    (1, 0.830, 0.235, 0.700, 0.175),
    (2, 0.740, 0.320, 0.660, 0.380),
    (3, 0.920, 0.320, 0.960, 0.380),
    (4, 0.830, 0.600, 0.700, 0.540),
])
annotate("04-modal-ajuste.png", [
    (1, 0.490, 0.430, 0.320, 0.370),
    (2, 0.490, 0.550, 0.320, 0.610),
    (3, 0.490, 0.690, 0.320, 0.750),
    (4, 0.560, 0.795, 0.720, 0.750),
])
annotate("05-modal-remover.png", [
    (1, 0.490, 0.455, 0.320, 0.395),
    (2, 0.490, 0.600, 0.320, 0.660),
    (3, 0.500, 0.500, 0.720, 0.455),
    (4, 0.560, 0.795, 0.720, 0.750),
])
annotate("06-fila-processamento.png", [
    (1, 0.500, 0.090, 0.620, 0.045),
    (2, 0.350, 0.285, 0.250, 0.220),
    (3, 0.250, 0.420, 0.180, 0.360),
    (4, 0.720, 0.450, 0.860, 0.380),
])
annotate("07-pdv-usar-cashback.png", [
    (1, 0.550, 0.125, 0.680, 0.075),
    (2, 0.670, 0.190, 0.850, 0.145),
    (3, 0.380, 0.800, 0.250, 0.740),
])
annotate("08-pdv-modal-aplicar.png", [
    (1, 0.500, 0.405, 0.320, 0.350),
    (2, 0.580, 0.475, 0.700, 0.420),
    (3, 0.500, 0.585, 0.320, 0.640),
    (4, 0.570, 0.670, 0.720, 0.725),
])
Wc, Hc, ph_h = montar_celulares("09-cardapio-checkout.png", [
    ("08-cardapio-checkout-saldo.png", "Sacola — saldo"),
    ("09-cardapio-checkout-usar.png", "Sacola — usando"),
])
p1 = lambda tx, ty: no_painel(0, tx, ty, Wc, Hc, ph_h)
p2 = lambda tx, ty: no_painel(1, tx, ty, Wc, Hc, ph_h)
s1, b1 = p1(0.42, 0.13), p1(0.16, 0.07)
s2, b2 = p1(0.86, 0.12), p1(0.62, 0.22)
s3, b3 = p2(0.42, 0.13), p2(0.16, 0.07)
s4, b4 = p2(0.55, 0.44), p2(0.82, 0.38)
annotate("09-cardapio-checkout.png", [
    (1, s1[0], s1[1], b1[0], b1[1]),
    (2, s2[0], s2[1], b2[0], b2[1]),
    (3, s3[0], s3[1], b3[0], b3[1]),
    (4, s4[0], s4[1], b4[0], b4[1]),
])
print("done")
