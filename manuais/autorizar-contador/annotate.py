"""Anota os screenshots do #95 Autorizar o contador.

Setas verdes + badges. Coordenadas em fracoes (0..1).
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)
"""
import math
import os

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
        TX, TY, BX, BY = tx * W, ty * H, bx * W, by * H
        ang = math.atan2(TY - BY, TX - BX)
        draw_arrow(d, BX + (r + 5) * math.cos(ang), BY + (r + 5) * math.sin(ang), TX, TY, w)
        badge(d, BX, BY, r, num, fnt)
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, name))
    print("OK", name)


# 1. Lista
annotate("01-aba-contadores.png", [
    (1, 0.310, 0.115, 0.310, 0.070),   # aba Contadores
    (2, 0.900, 0.175, 0.900, 0.115),   # + Autorizar
    (3, 0.220, 0.280, 0.170, 0.230),   # nome
    (4, 0.430, 0.280, 0.430, 0.230),   # Empresa inteira
    (5, 0.540, 0.280, 0.540, 0.230),   # status
    (6, 0.680, 0.280, 0.680, 0.230),   # permissoes
    (7, 0.860, 0.280, 0.800, 0.230),   # ultimo acesso
    (8, 0.965, 0.280, 0.965, 0.230),   # tres pontinhos
])

# 2. Formulario
annotate("02-dialog-autorizar.png", [
    (1, 0.420, 0.230, 0.280, 0.200),   # CPF/CNPJ
    (2, 0.420, 0.300, 0.280, 0.300),   # Nome
    (3, 0.420, 0.385, 0.280, 0.400),   # E-mail
    (4, 0.420, 0.455, 0.280, 0.470),   # Telefone
    (5, 0.420, 0.560, 0.280, 0.600),   # aviso CNPJs
    (6, 0.655, 0.720, 0.780, 0.680),   # XML
    (7, 0.655, 0.755, 0.780, 0.800),   # Ver fechamento
    (8, 0.655, 0.845, 0.780, 0.900),   # Editar impostos
])

# 3. Menu da linha Ativo
annotate("03-menu-acoes.png", [
    (1, 0.880, 0.395, 0.780, 0.320),   # Alterar permissoes
    (2, 0.850, 0.430, 0.760, 0.500),   # redefinir senha
    (3, 0.850, 0.530, 0.760, 0.580),   # Encerrar
])

# 4. Permissoes
annotate("04-dialog-permissoes.png", [
    (1, 0.620, 0.430, 0.720, 0.390),   # XML
    (2, 0.620, 0.480, 0.720, 0.520),   # Ver fechamento
    (3, 0.620, 0.560, 0.720, 0.620),   # Editar impostos
])

# 5. Encerrar
annotate("05-confirmar-encerrar.png", [
    (1, 0.500, 0.470, 0.280, 0.430),   # recado
    (2, 0.600, 0.530, 0.720, 0.500),   # ENCERRAR
    (3, 0.460, 0.530, 0.380, 0.580),   # CANCELAR
])

# 6. E-mail primeiro acesso
annotate("06-email-primeiro-acesso.png", [
    (1, 0.500, 0.380, 0.220, 0.330),   # titulo
    (2, 0.500, 0.430, 0.220, 0.480),   # empresa + documento
    (3, 0.500, 0.530, 0.280, 0.600),   # CRIAR MINHA SENHA
])

# 7. E-mail conta existente
annotate("07-email-conta-existente.png", [
    (1, 0.580, 0.455, 0.220, 0.370),   # 2 CNPJs
    (2, 0.500, 0.530, 0.280, 0.480),   # ACESSAR O PORTAL
    (3, 0.500, 0.610, 0.280, 0.680),   # senha ja cadastrada
])

print("done")
