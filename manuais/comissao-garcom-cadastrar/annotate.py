"""Anota os screenshots do manual #83 — Comissão do garçom: cadastrar e lançar."""
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


annotate("01-lista-funcionarios.png", [
    (1, 0.24, 0.11, 0.16, 0.05),   # + Novo Funcionário (F1)
    (2, 0.62, 0.20, 0.74, 0.12),   # card Garçons
    (3, 0.48, 0.40, 0.38, 0.48),   # selo Garçom da Ana
])
annotate("02-ana-dados.png", [
    (1, 0.32, 0.28, 0.20, 0.20),   # Nome
    (2, 0.62, 0.28, 0.76, 0.20),   # Código Operador
    (3, 0.72, 0.88, 0.86, 0.80),   # CADASTRAR (F2)
])
annotate("03-ana-funcao.png", [
    (1, 0.32, 0.32, 0.20, 0.24),   # radio Garçom
    (2, 0.38, 0.44, 0.22, 0.52),   # Comissão (%)
    (3, 0.72, 0.88, 0.86, 0.80),   # CADASTRAR (F2)
], ring=[(0.26, 0.28, 0.48, 0.22)])
annotate("04-usuario-ana.png", [
    (1, 0.29, 0.36, 0.18, 0.26),   # Login e Senha
    (2, 0.29, 0.52, 0.18, 0.58),   # Funcionário
    (3, 0.29, 0.62, 0.72, 0.56),   # Grupo de Acesso
    (4, 0.72, 0.72, 0.84, 0.66),   # Aplicativos
    (5, 0.72, 0.80, 0.84, 0.88),   # SALVAR (F2)
])
annotate("05-lista-usuarios.png", [
    (1, 0.22, 0.26, 0.12, 0.18),   # ana.garcom
    (2, 0.22, 0.34, 0.12, 0.42),   # bruno.garcom
])
annotate("06-garcom-ana.png", [
    (1, 0.84, 0.32, 0.70, 0.22),   # Garçom: Ana Garçom
    (2, 0.84, 0.78, 0.70, 0.86),   # Taxa Serviço (10%)
])
annotate("07-pedido-ana.png", [
    (1, 0.84, 0.12, 0.70, 0.06),   # Mesa 16
    (2, 0.84, 0.26, 0.70, 0.34),   # Garçom: Ana Garçom
    (3, 0.84, 0.80, 0.70, 0.70),   # Taxa + R$ 1,45
    (4, 0.50, 0.92, 0.32, 0.86),   # Carrinho
])
annotate("09-prova-comissao.png", [
    (1, 0.76, 0.26, 0.76, 0.14),   # Comissão Total
    (2, 0.28, 0.42, 0.55, 0.36),   # Ana Garçom
    (3, 0.28, 0.50, 0.55, 0.58),   # Bruno Garçom
])

print("done")
