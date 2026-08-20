"""Anota screenshots — Manual Fiado (operar no dia a dia)."""
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

# regiões com nome/telefone de clientes
BORRAO_LISTA = [(0.12, 0.22, 0.55, 0.55)]
BORRAO_EXTRATO = [(0.08, 0.08, 0.85, 0.12)]
BORRAO_MIGRACAO = [(0.28, 0.18, 0.45, 0.65)]


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


def passthrough(name):
    Image.open(os.path.join(SRC, name)).convert("RGB").save(os.path.join(OUT, name))
    print("OK ctx", name)


def annotate(name, markers, ring=None, borrao=None):
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
    for fx, fy, fw, fh in (ring or []):
        d.rectangle([fx * W, fy * H, (fx + fw) * W, (fy + fh) * H], outline=GREEN + (A_LINE,), width=w)
    for num, tx, ty, bx, by in markers:
        ang = math.atan2(ty * H - by * H, tx * W - bx * W)
        sx, sy = bx * W + (r + 5) * math.cos(ang), by * H + (r + 5) * math.sin(ang)
        draw_arrow(d, sx, sy, tx * W, ty * H, w)
        badge(d, bx * W, by * H, r, num, fnt)
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, name))
    print("OK", name)


annotate("01-menu-fiado.png", [(1, 0.145, 0.72, 0.055, 0.58)])
annotate("02-visao-geral-kpis.png", [
    (1, 0.18, 0.55, 0.08, 0.35),
    (2, 0.52, 0.55, 0.42, 0.35),
    (3, 0.85, 0.55, 0.72, 0.35),
])
annotate("03-visao-geral-grafico.png", [
    (1, 0.88, 0.12, 0.72, 0.08),
    (2, 0.12, 0.35, 0.05, 0.25),
    (3, 0.35, 0.35, 0.28, 0.25),
])
passthrough("04-visao-geral-tabela.png")
annotate("05-controle-filtros-acoes.png", [
    (1, 0.10, 0.42, 0.04, 0.28),
    (2, 0.28, 0.42, 0.20, 0.28),
    (3, 0.52, 0.42, 0.44, 0.28),
    (4, 0.68, 0.42, 0.60, 0.28),
    (5, 0.92, 0.42, 0.82, 0.28),
])
annotate("06-controle-lista-clientes.png", [
    (1, 0.72, 0.32, 0.58, 0.18),
    (2, 0.72, 0.52, 0.58, 0.38),
    (3, 0.95, 0.32, 0.88, 0.18),
], borrao=BORRAO_LISTA)
annotate("07-vendas-sem-pagamento.png", [
    (1, 0.50, 0.55, 0.50, 0.12),
    (2, 0.78, 0.08, 0.68, 0.05),
    (3, 0.88, 0.45, 0.78, 0.38),
], borrao=BORRAO_MIGRACAO)
annotate("08-extrato-cliente.png", [
    (1, 0.35, 0.38, 0.22, 0.32),
    (2, 0.65, 0.38, 0.52, 0.32),
    (3, 0.78, 0.18, 0.62, 0.10),
    (4, 0.92, 0.18, 0.85, 0.10),
], borrao=BORRAO_EXTRATO)
annotate("09-modal-pagamento.png", [
    (1, 0.50, 0.38, 0.38, 0.22),
    (2, 0.50, 0.52, 0.38, 0.36),
    (3, 0.50, 0.66, 0.38, 0.50),
    (4, 0.50, 0.88, 0.38, 0.78),
])
annotate("10-modal-divida.png", [
    (1, 0.50, 0.42, 0.38, 0.28),
    (2, 0.50, 0.58, 0.38, 0.44),
    (3, 0.50, 0.82, 0.38, 0.72),
])
annotate("11-extrato-detalhado.png", [
    (1, 0.22, 0.12, 0.10, 0.06),
    (2, 0.38, 0.12, 0.30, 0.06),
    (3, 0.88, 0.10, 0.78, 0.06),
])
annotate("12-pdv-formas-pagamento.png", [
    (1, 0.72, 0.62, 0.58, 0.48),
    (2, 0.50, 0.78, 0.38, 0.65),
    (3, 0.50, 0.92, 0.38, 0.82),
])
annotate("13-forma-recebimento-fiado.png", [(1, 0.50, 0.50, 0.38, 0.35)])

print("annotate fiado concluído")
