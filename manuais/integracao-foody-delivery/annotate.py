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


for n in [
    "01-foody-menu-apis.png",
    "02-foody-criar-token.png",
    "03-foody-criar-webhook.png",
    "07-whatsapp-acompanhamento.png",
]:
    passthrough(n)

# 1 = menu Aplicativos; 2 = card Foody Delivery (2ª fileira, centro da seção Entrega)
annotate("04-aplicativos-foody.png", [
    (1, 0.085, 0.430, 0.200, 0.365),
    (2, 0.550, 0.600, 0.680, 0.520),
])

# 1 Token; 2 Token Webhook; 3 Sincronizar manualmente; 4 SALVAR E SAIR
annotate("05-modal-foody-config.png", [
    (1, 0.520, 0.330, 0.340, 0.290),
    (2, 0.520, 0.430, 0.340, 0.490),
    (3, 0.400, 0.545, 0.280, 0.590),
    (4, 0.680, 0.720, 0.800, 0.660),
])

# 1 PREPARO; 2 Todas as origens; 3 lista de origens; 4 SALVAR
annotate("06-modal-foody-origens.png", [
    (1, 0.400, 0.455, 0.270, 0.405),
    (2, 0.655, 0.575, 0.500, 0.530),
    (3, 0.380, 0.720, 0.260, 0.780),
    (4, 0.680, 0.880, 0.800, 0.820),
])
print("done")
