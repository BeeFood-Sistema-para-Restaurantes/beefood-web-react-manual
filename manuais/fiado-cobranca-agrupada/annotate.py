"""Anota screenshots — Manual Cobrança agrupada."""
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
BORRAO_CLIENTES = [(0.08, 0.28, 0.72, 0.55)]


def font(sz):
    for c in FONT_CANDIDATES:
        if os.path.exists(c):
            return ImageFont.truetype(c, sz)
    raise RuntimeError("fonte não encontrada")


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


def annotate(name, markers, borrao=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    W, H = img.size
    for fx, fy, fw, fh in (borrao or []):
        caixa = (int(fx * W), int(fy * H), int((fx + fw) * W), int((fy + fh) * H))
        img.paste(img.crop(caixa).filter(ImageFilter.GaussianBlur(radius=max(6, W // 140))), caixa)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = int(W * 0.0125)
    fnt = font(int(r * 1.2))
    w = max(2, int(W * 0.0022))
    for num, tx, ty, bx, by in markers:
        ang = math.atan2(ty * H - by * H, tx * W - bx * W)
        sx, sy = bx * W + (r + 5) * math.cos(ang), by * H + (r + 5) * math.sin(ang)
        draw_arrow(d, sx, sy, tx * W, ty * H, w)
        badge(d, bx * W, by * H, r, num, fnt)
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, name))
    print("OK", name)


annotate("01-botao-cobranca-agrupada.png", [(1, 0.28, 0.42, 0.12, 0.28)])
annotate("02-fase1-selecao-clientes.png", [
    (1, 0.35, 0.18, 0.22, 0.10),
    (2, 0.78, 0.18, 0.65, 0.10),
    (3, 0.08, 0.42, 0.04, 0.32),
    (4, 0.88, 0.28, 0.78, 0.18),
    (5, 0.88, 0.92, 0.78, 0.82),
], borrao=BORRAO_CLIENTES)
annotate("03-fase2-extrato-consolidado.png", [
    (1, 0.50, 0.45, 0.38, 0.20),
    (2, 0.18, 0.12, 0.08, 0.06),
    (3, 0.88, 0.92, 0.78, 0.82),
], borrao=[(0.10, 0.22, 0.80, 0.60)])
annotate("04-fase3-pagamentos.png", [
    (1, 0.18, 0.12, 0.08, 0.06),
    (2, 0.25, 0.32, 0.12, 0.22),
    (3, 0.55, 0.32, 0.42, 0.22),
    (4, 0.50, 0.82, 0.38, 0.70),
    (5, 0.88, 0.92, 0.78, 0.82),
])
annotate("05-fase4-processamento.png", [
    (1, 0.50, 0.45, 0.38, 0.30),
    (2, 0.50, 0.55, 0.38, 0.40),
])
annotate("06-processamento-concluido.png", [(1, 0.50, 0.45, 0.38, 0.30)])

print("annotate cobrança concluído")
