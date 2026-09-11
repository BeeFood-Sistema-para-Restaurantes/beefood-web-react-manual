"""Anota os screenshots do #98 — taxa de serviço opcional no cupom."""
import os
import math
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
        d.line([(x1, y1), (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))],
               fill=col, width=w)


def badge(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], fill=WHITE + (235,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN + (A_BADGE,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
           t, fill=WHITE, font=fnt)


def annotate(name, markers, ring=None, crop=None, rmin=0):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    W0, H0 = img.size
    if crop:
        img = img.crop((int(crop[0] * W0), int(crop[1] * H0),
                        int(crop[2] * W0), int(crop[3] * H0)))
    W, H = img.size
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = max(rmin, int(W * 0.0125))
    fnt = font(int(r * 1.2))
    w = max(2, int(W * 0.0022))
    for (fx, fy, fw, fh) in (ring or []):
        x0, y0 = fx * W, fy * H
        d.rectangle([x0, y0, x0 + fw * W, y0 + fh * H], outline=GREEN + (A_LINE,), width=w)
    for (num, tx, ty, bx, by) in markers:
        TX, TY, BX, BY = tx * W, ty * H, bx * W, by * H
        ang = math.atan2(TY - BY, TX - BX)
        draw_arrow(d, BX + (r + 5) * math.cos(ang), BY + (r + 5) * math.sin(ang), TX, TY, w)
        badge(d, BX, BY, r, num, fnt)
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, name))
    print("OK", name)


annotate("01-aba-layout.png", [
    (1, 0.405, 0.090, 0.500, 0.185),  # aba Layout
    (2, 0.300, 0.278, 0.500, 0.278),  # Cupom Pedido
])

annotate("02-modal-abas.png", [
    (1, 0.528, 0.218, 0.700, 0.300),  # aba Texto Padrão
])

annotate("03-texto-rodape.png", [
    (1, 0.620, 0.655, 0.810, 0.500),  # rodapé Presencial
    (2, 0.705, 0.878, 0.820, 0.800),  # SALVAR E FECHAR
], ring=[
    (0.508, 0.548, 0.230, 0.130),  # caixa do rodapé Presencial
])

annotate("04-detalhe-venda.png", [
    (1, 0.355, 0.778, 0.220, 0.700),  # Taxa Serviço (10%)
    (2, 0.658, 0.108, 0.780, 0.185),  # impressora do cupom
])

annotate("05-cupom-presencial.png", [
    (1, 0.20, 0.536, 0.10, 0.536),  # Serviço (10%)
    (2, 0.50, 0.804, 0.12, 0.804),  # TAXA DE SERVIÇO OPCIONAL
], crop=(0.0, 0.0, 1.0, 0.56), rmin=14)

print("done")
