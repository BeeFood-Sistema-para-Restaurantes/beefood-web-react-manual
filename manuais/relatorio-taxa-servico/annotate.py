"""Anota os screenshots do manual #85 — Relatório de taxa de serviço."""
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


annotate("01-filtro-data.png", [
    (1, 0.24, 0.10, 0.14, 0.05),   # botão da data
    (2, 0.28, 0.18, 0.16, 0.26),   # Hoje / topo dos períodos
    (3, 0.48, 0.53, 0.60, 0.62),   # Confirmar
])
annotate("02-relatorio-taxa.png", [
    (1, 0.15, 0.50, 0.22, 0.42),   # Taxa Serviço no menu do iframe
    (2, 0.28, 0.24, 0.50, 0.14),   # KPI Total Taxa Serviço
    (3, 0.28, 0.42, 0.50, 0.50),   # Taxa Serviço por Garçom
])
annotate("03-produto-sem-taxa.png", [
    (1, 0.38, 0.72, 0.26, 0.64),   # Opções avançadas
    (2, 0.42, 0.78, 0.26, 0.86),   # Sem taxa de serviço
])
annotate("04-detalhe-venda.png", [
    (1, 0.32, 0.18, 0.20, 0.24),   # Taxa Serviço / Ana Garçom
    (2, 0.50, 0.38, 0.38, 0.46),   # RECEBIDO e Mesa 16
    (3, 0.92, 0.38, 0.94, 0.28),   # Tipo Taxa %
])
annotate("05-caixa-resumo-taxa.png", [
    (1, 0.82, 0.22, 0.92, 0.14),   # Resumo Presencial
    (2, 0.82, 0.40, 0.92, 0.30),   # Taxa Ana / Bruno
    (3, 0.82, 0.46, 0.70, 0.42),   # TOTAL (inclui Sem Funcionário)
])

print("done")
