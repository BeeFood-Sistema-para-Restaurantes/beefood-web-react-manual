"""Helpers comuns — copiado em cada manual da serie WhatsApp."""
import os, math, shutil
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


def annotate(name, markers, ring=None, src_name=None, borrao=None, raio=0.0125):
    origem = src_name or name
    img = Image.open(os.path.join(SRC, origem)).convert("RGBA")
    W, H = img.size
    if borrao:
        for (fx, fy, fw, fh) in borrao:
            caixa = (int(fx * W), int(fy * H), int((fx + fw) * W), int((fy + fh) * H))
            trecho = img.crop(caixa).filter(ImageFilter.GaussianBlur(radius=max(12, W // 90)))
            img.paste(trecho, caixa)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = int(W * raio)
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


def passthrough(name, src_name=None):
    origem = src_name or name
    shutil.copyfile(os.path.join(SRC, origem), os.path.join(OUT, name))
    print("OK (contexto)", name)


PHONE_W, GAP, PAD, CAP_H = 380, 18, 22, 44


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


annotate("01-lista.png", [
    (1, 0.240, 0.275, 0.175, 0.210),
    (2, 0.280, 0.355, 0.175, 0.420),
])
annotate("02-novo-contato.png", [
    (1, 0.500, 0.430, 0.280, 0.360),
    (2, 0.500, 0.500, 0.280, 0.560),
    (3, 0.620, 0.580, 0.780, 0.640),
])
montar_celulares("03-whatsapp-boletim.png", [("w-boletim.png", "Resumo das 07h")])
passthrough("03-whatsapp-boletim.png")
