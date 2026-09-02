"""Anota os screenshots do manual #78 Classificação RFV.

Le de imagens-puras/ e escreve em imagens-tratadas/.
Coordenadas em fracoes 0..1. Dado pessoal (nome/telefone) e coberto
na pura ANTES de gravar a tratada — o repositorio e publico.
"""
import math
import os

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
        d.line(
            [(x1, y1), (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))],
            fill=col,
            width=w,
        )


def badge(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], fill=WHITE + (235,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN + (A_BADGE,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text(
        (cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
        t,
        fill=WHITE,
        font=fnt,
    )


def aplicar_borrao(img, caixas):
    W, H = img.size
    for (fx, fy, fw, fh) in caixas:
        caixa = (int(fx * W), int(fy * H), int((fx + fw) * W), int((fy + fh) * H))
        trecho = img.crop(caixa).filter(ImageFilter.GaussianBlur(radius=max(8, W // 120)))
        img.paste(trecho, caixa)
    return img


def passthrough(name, borrao=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    if borrao:
        img = aplicar_borrao(img, borrao)
    img.convert("RGB").save(os.path.join(OUT, name))
    print("OK (contexto)", name)


def annotate(name, markers, ring=None, borrao=None, raio=0.0125):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    if borrao:
        img = aplicar_borrao(img, borrao)
    W, H = img.size
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = max(14, int(W * raio))
    fnt = font(int(r * 1.2))
    w = max(2, int(W * 0.0022))
    for (fx, fy, fw, fh) in (ring or []):
        x0, y0 = fx * W, fy * H
        d.rectangle(
            [x0, y0, x0 + fw * W, y0 + fh * H],
            outline=GREEN + (A_LINE,),
            width=w,
        )
    for (num, tx, ty, bx, by) in markers:
        TX, TY, BX, BY = tx * W, ty * H, bx * W, by * H
        ang = math.atan2(TY - BY, TX - BX)
        draw_arrow(
            d,
            BX + (r + 5) * math.cos(ang),
            BY + (r + 5) * math.sin(ang),
            TX,
            TY,
            w,
        )
        badge(d, BX, BY, r, num, fnt)
    out_img = Image.alpha_composite(img, overlay).convert("RGB")
    out_img.save(os.path.join(OUT, name))
    print("OK", name)


# 01) Menu lateral — Clientes
annotate("01-menu-clientes.png", [
    (1, 0.095, 0.705, 0.040, 0.620),  # item Clientes
])

# 02) Lista + botao RFV + chips (nome e telefone cobertos)
annotate("02-lista-rfv-chips.png", [
    (1, 0.805, 0.118, 0.740, 0.070),  # botao RFV
    (2, 0.848, 0.118, 0.900, 0.070),  # ajuda das classificacoes
    (3, 0.230, 0.208, 0.175, 0.155),  # chip Fieis
    (4, 0.198, 0.318, 0.155, 0.370),  # emoji da classificacao na linha
], borrao=[
    (0.165, 0.295, 0.320, 0.140),  # nome + telefone das duas linhas
])

# 03) Editar Parametros RFV
annotate("03-parametros-rfv.png", [
    (1, 0.270, 0.355, 0.220, 0.290),  # coluna Recencia
    (2, 0.500, 0.355, 0.500, 0.290),  # coluna Frequencia
    (3, 0.730, 0.355, 0.780, 0.290),  # coluna Valor
    (4, 0.175, 0.905, 0.120, 0.845),  # Resetar Padrao
])

# 04) Ajuda dos grupos (imagem mais alta)
annotate("04-classificacoes.png", [
    (1, 0.380, 0.210, 0.280, 0.165),  # R = Recencia
    (2, 0.560, 0.210, 0.700, 0.165),  # FV = Frequencia + Valor
    (3, 0.500, 0.330, 0.780, 0.290),  # card de um grupo
], borrao=[
    (0.160, 0.220, 0.100, 0.500),  # nomes que vazam a esquerda do modal
    (0.800, 0.220, 0.180, 0.500),  # nomes que vazam a direita
])

# 05) Ficha, aba Indicadores (nome e telefone cobertos)
annotate("05-ficha-indicadores.png", [
    (1, 0.415, 0.145, 0.330, 0.095),  # aba Indicadores
    (2, 0.295, 0.198, 0.210, 0.150),  # selo Fieis
    (3, 0.720, 0.182, 0.850, 0.125),  # Atualizado a cada 24h
    (4, 0.330, 0.400, 0.250, 0.530),  # circulo Recencia
    (5, 0.500, 0.400, 0.500, 0.545),  # circulo Frequencia
    (6, 0.670, 0.400, 0.780, 0.530),  # circulo Valor
], borrao=[
    (0.220, 0.100, 0.460, 0.055),  # nome e telefone no titulo do modal
    (0.160, 0.300, 0.110, 0.080),  # nome na lista atras do modal
])

# 06) Segmentacao: categoria RFV (basico)
annotate("06-segmentacao-rfv.png", [
    (1, 0.400, 0.250, 0.320, 0.190),  # chip da categoria RFV
    (2, 0.360, 0.780, 0.220, 0.820),  # Classificacao RFV (publico)
])

# 07) Campanha inteligente passo 1: campo Segmentacao (basico)
annotate("07-campanha-inteligente-segmentacao.png", [
    (1, 0.800, 0.365, 0.910, 0.305),  # Origem do publico
    (2, 0.620, 0.515, 0.520, 0.575),  # campo Segmentacao
])

print("done")
