"""Anota os screenshots do manual BeeFood - Endereco do restaurante (#34).

Setas verdes + badges numerados. Coordenadas em fracoes (0..1).
Painel: 2160x1350 (viewport 1440x900, DPR 1.5).
"""
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


def annotate(name, markers, ring=None, borrao=None, raio=0.0125, out_name=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    W, H = img.size
    for (fx, fy, fw, fh) in (borrao or []):
        caixa = (int(fx * W), int(fy * H), int((fx + fw) * W), int((fy + fh) * H))
        trecho = img.crop(caixa).filter(ImageFilter.GaussianBlur(radius=max(6, W // 140)))
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
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, out_name or name))
    print("OK", out_name or name)


# 01) Resultado: cartoes Localizacao / Tipo + aba
annotate("01-area-entrega-resultado.png", [
    (1, 0.400, 0.205, 0.280, 0.305),   # cartao Localizacao
    (2, 0.780, 0.205, 0.900, 0.305),   # cartao Tipo
    (3, 0.090, 0.505, 0.090, 0.380),   # item do menu
])

# 02) Passo 1
annotate("02-step1-localizacao.png", [
    (1, 0.880, 0.135, 0.900, 0.230),   # Salvar e Avancar
    (2, 0.320, 0.215, 0.220, 0.180),   # Fuso
    (3, 0.400, 0.305, 0.220, 0.360),   # Busca
    (4, 0.500, 0.520, 0.220, 0.520),   # Mapa
    (5, 0.280, 0.880, 0.220, 0.780),   # Endereco confirmado
])

# 04) Modal confirmar
annotate("04-modal-confirmar.png", [
    (1, 0.500, 0.400, 0.300, 0.300),   # endereco detectado
    (2, 0.500, 0.555, 0.300, 0.555),   # Numero
    (3, 0.500, 0.640, 0.300, 0.700),   # Complemento
    (4, 0.620, 0.740, 0.780, 0.700),   # Confirmar e Avancar
])

# 05) Busca digitando o endereço da loja
annotate("05-busca-sugestoes.png", [
    (1, 0.400, 0.305, 0.220, 0.360),   # Busca
    (2, 0.500, 0.520, 0.220, 0.520),   # Pin / mapa
])

# 06) Passo 2 — os quatro tipos
annotate("06-step2-depois-endereco.png", [
    (1, 0.500, 0.210, 0.280, 0.155),   # endereco
    (2, 0.300, 0.380, 0.260, 0.500),   # KM
    (3, 0.450, 0.380, 0.450, 0.500),   # Raio
    (4, 0.600, 0.380, 0.640, 0.500),   # Bairro
    (5, 0.750, 0.380, 0.820, 0.500),   # CEP
])
