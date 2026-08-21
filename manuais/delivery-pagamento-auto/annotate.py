"""Anota os screenshots do manual BeeFood - Delivery pagamento auto (#43)."""
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


# switch Pagamento Automático Delivery, canto inferior direito do card
annotate("02-pagamento-auto-ligado.png", [
    (1, 0.880, 0.900, 0.700, 0.820),
])

# menu Delivery, + Novo Pedido, filtro Sem pagamento
annotate("03-kanban.png", [
    (1, 0.080, 0.200, 0.160, 0.280),
    (2, 0.220, 0.095, 0.380, 0.055),
    (3, 0.380, 0.145, 0.500, 0.220),
])

# Coxinha selecionada, campo Intenção, Valor Total
annotate("05-coxinha-no-pedido.png", [
    (1, 0.630, 0.360, 0.500, 0.280),
    (2, 0.840, 0.280, 0.720, 0.200),
    (3, 0.900, 0.800, 0.740, 0.720),
])

# modal: forma Dinheiro, Troco, SALVAR
annotate("06-intencao-dinheiro.png", [
    (1, 0.500, 0.380, 0.320, 0.280),
    (2, 0.500, 0.560, 0.320, 0.640),
    (3, 0.600, 0.700, 0.760, 0.760),
])

# card #5 (850) no Preparo, filtro Sem pagamento
annotate("07-pedido-no-preparo.png", [
    (1, 0.480, 0.400, 0.320, 0.300),
    (2, 0.380, 0.145, 0.540, 0.080),
])

# card selecionado, badge PREPARO, PAGAMENTO, PEDIDO PRONTO
annotate("08-detalhe-preparo.png", [
    (1, 0.480, 0.360, 0.300, 0.240),
    (2, 0.820, 0.135, 0.940, 0.070),
    (3, 0.760, 0.950, 0.680, 0.870),
    (4, 0.900, 0.950, 0.960, 0.870),
])

# linha do tempo em Pronto, PAGAMENTO, PEDIDO ENTREGUE
annotate("09-pedido-pronto.png", [
    (1, 0.820, 0.240, 0.680, 0.160),
    (2, 0.760, 0.950, 0.680, 0.870),
    (3, 0.900, 0.950, 0.960, 0.870),
])

# badge ENTREGUE, Dinheiro Pago, aviso, Sem pagamento
annotate("10-depois-entregue.png", [
    (1, 0.820, 0.135, 0.940, 0.060),
    (2, 0.820, 0.760, 0.680, 0.680),
    (3, 0.820, 0.820, 0.680, 0.900),
    (4, 0.380, 0.145, 0.500, 0.220),
])

print("done")
