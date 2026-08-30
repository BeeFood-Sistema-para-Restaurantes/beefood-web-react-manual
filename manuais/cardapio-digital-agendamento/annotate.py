"""Anota screenshots — #70 Agendamento do cardápio digital."""
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


PHONE_W = 380
GAP = 18
PAD = 22
CAP_H = 44


def montar_celulares(nome_out, paineis):
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


annotate("01-aba-switches.png", [
    (1, 0.078, 0.325, 0.165, 0.260),
    (2, 0.500, 0.175, 0.280, 0.130),
    (3, 0.860, 0.355, 0.740, 0.305),
    (4, 0.860, 0.470, 0.740, 0.530),
    (5, 0.860, 0.590, 0.740, 0.650),
])

annotate("02-tempo.png", [
    (1, 0.400, 0.300, 0.260, 0.240),
    (2, 0.720, 0.300, 0.860, 0.240),
    (3, 0.400, 0.480, 0.260, 0.420),
    (4, 0.720, 0.480, 0.860, 0.420),
    (5, 0.400, 0.640, 0.260, 0.580),
    (6, 0.400, 0.800, 0.260, 0.740),
    (7, 0.720, 0.800, 0.860, 0.740),
])

if all(os.path.exists(os.path.join(SRC, n)) for n in (
    "04-cel-hoje-agendar.png", "05-cel-calendario.png", "06-cel-horarios.png"
)):
    W, H, ph_h = montar_celulares("03-cardapio-digital.png", [
        ("04-cel-hoje-agendar.png", "Hoje ou Agendar"),
        ("05-cel-calendario.png", "Dias do calendário"),
        ("06-cel-horarios.png", "Horários do dia"),
    ])
    f1 = lambda tx, ty: no_painel(0, tx, ty, W, H, ph_h)
    f2 = lambda tx, ty: no_painel(1, tx, ty, W, H, ph_h)
    f3 = lambda tx, ty: no_painel(2, tx, ty, W, H, ph_h)
    a1 = f1(0.72, 0.455)
    b1 = f1(0.16, 0.34)
    a2 = f2(0.18, 0.155)
    b2 = f2(0.12, 0.07)
    a3 = f3(0.42, 0.74)
    b3 = f3(0.14, 0.62)
    annotate("03-cardapio-digital.png", [
        (1, a1[0], a1[1], b1[0], b1[1]),
        (2, a2[0], a2[1], b2[0], b2[1]),
        (3, a3[0], a3[1], b3[0], b3[1]),
    ])
else:
    print("tira: celulares ainda nao capturados")

print("done")
