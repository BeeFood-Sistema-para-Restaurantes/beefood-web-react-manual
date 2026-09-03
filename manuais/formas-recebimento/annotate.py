"""Anota os screenshots do manual BeeFood - Cadastrar forma de recebimento (#82).

Le de imagens-puras/ e escreve em imagens-tratadas/.
As coordenadas dos marcadores sao dadas em fracoes 0..1 da imagem PURA (tela cheia,
1440x900 com device_scale_factor 1.5); o recorte e aplicado depois e o script converte
sozinho. Assim medir uma vez na captura cheia serve para qualquer recorte.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

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

# Recortes reaproveitados
LISTA = (0.145, 0.045, 1.0, 0.55)      # barra de acoes + primeiras linhas
MODAL = (0.185, 0.19, 0.815, 0.80)     # modal da forma de recebimento (3 abas)


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
        d.line([(x1, y1),
                (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))],
               fill=col, width=w)


def badge(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], fill=WHITE + (235,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN + (A_BADGE,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
           t, fill=WHITE, font=fnt)


def preparar(name, recorte=None, escala=1.0, borrao=None):
    """borrao: regioes (x, y, largura, altura) em fracoes da imagem cheia, borradas
    antes do recorte. Usado para cobrir dado pessoal de cliente."""
    img = Image.open(os.path.join(SRC, name)).convert("RGB")
    for (bx, by, bw, bh) in (borrao or []):
        W, H = img.size
        cx = (int(bx * W), int(by * H), int((bx + bw) * W), int((by + bh) * H))
        img.paste(img.crop(cx).filter(ImageFilter.GaussianBlur(9)), cx)
    if recorte:
        W, H = img.size
        x0, y0, x1, y1 = recorte
        img = img.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
    if escala != 1.0:
        img = img.resize((int(img.width * escala), int(img.height * escala)), Image.LANCZOS)
    return img


def converter(f, recorte):
    if not recorte:
        return f
    x0, y0, x1, y1 = recorte
    return ((f[0] - x0) / (x1 - x0), (f[1] - y0) / (y1 - y0))


def annotate(name, markers, ring=None, recorte=None, escala=1.0, borrao=None):
    base = preparar(name, recorte, escala, borrao).convert("RGBA")
    W, H = base.size
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = max(14, int(W * 0.0125))
    fnt = font(int(r * 1.2))
    w = max(2, int(W * 0.0022))
    for (fx, fy, fw, fh) in (ring or []):
        (cx, cy) = converter((fx, fy), recorte)
        (cx2, cy2) = converter((fx + fw, fy + fh), recorte)
        d.rectangle([cx * W, cy * H, cx2 * W, cy2 * H], outline=GREEN + (A_LINE,), width=w)
    for (num, tx, ty, bx, by) in markers:
        (tx, ty) = converter((tx, ty), recorte)
        (bx, by) = converter((bx, by), recorte)
        TX, TY, BX, BY = tx * W, ty * H, bx * W, by * H
        ang = math.atan2(TY - BY, TX - BX)
        draw_arrow(d, BX + (r + 5) * math.cos(ang), BY + (r + 5) * math.sin(ang), TX, TY, w)
        badge(d, BX, BY, r, num, fnt)
    Image.alpha_composite(base, overlay).convert("RGB").save(os.path.join(OUT, name))
    print("OK", name, "->", (W, H))


def passthrough(name, recorte=None, escala=1.0, borrao=None):
    img = preparar(name, recorte, escala, borrao)
    img.save(os.path.join(OUT, name))
    print("OK (contexto)", name, "->", img.size)


# 1. Onde fica: submenu Cadastros.
annotate(
    "01-menu-cadastros.png",
    [
        (1, 0.075, 0.320, 0.230, 0.320),   # item Formas Recebimento
    ],
    recorte=(0.0, 0.11, 0.34, 0.42),
    escala=2.2,
)

# 2. A listagem: e aqui que se liga o canal.
annotate(
    "02-listagem.png",
    [
        (1, 0.250, 0.105, 0.250, 0.140),   # Nova Forma (F1)
        (2, 0.560, 0.105, 0.560, 0.140),   # filtro por usuario
        (3, 0.280, 0.196, 0.238, 0.238),   # switch Ativo
        (4, 0.795, 0.172, 0.665, 0.155),   # switch Delivery
        (5, 0.855, 0.190, 0.665, 0.210),   # switch Presencial
        (6, 0.378, 0.276, 0.545, 0.276),   # etiqueta de desconto/acrescimo
    ],
    recorte=LISTA,
    escala=1.15,
)

# 3. O modal, aba Configuracao.
annotate(
    "03-nova-forma.png",
    [
        (1, 0.310, 0.409, 0.440, 0.409),   # Titulo
        (2, 0.400, 0.640, 0.470, 0.700),   # Tipo
        (3, 0.762, 0.418, 0.680, 0.418),   # Delivery/Retirada
        (4, 0.762, 0.471, 0.680, 0.471),   # Presencial
        (5, 0.400, 0.307, 0.545, 0.300),   # as tres abas
        (6, 0.665, 0.752, 0.560, 0.755),   # SALVAR E SAIR (F2)
    ],
    recorte=MODAL,
    escala=1.5,
)

# 4. Ajuste no pagamento.
annotate(
    "04-ajuste-pagamento.png",
    [
        (1, 0.600, 0.816, 0.720, 0.816),   # as cinco opcoes
        (2, 0.700, 0.660, 0.760, 0.720),   # o campo do valor
    ],
    recorte=(0.20, 0.55, 0.83, 0.90),
    escala=1.5,
)

# 5. Aba Taxas e Bandeiras.
annotate(
    "05-aba-taxas.png",
    [
        (1, 0.341, 0.315, 0.550, 0.300),   # a aba
        (2, 0.280, 0.507, 0.280, 0.568),   # Taxa (%)
        (3, 0.470, 0.507, 0.470, 0.568),   # Desconto Fixo (R$)
        (4, 0.660, 0.503, 0.660, 0.568),   # Dias para Recebimento
    ],
    recorte=MODAL,
    escala=1.5,
)

# 6. Aba TEF.
annotate(
    "06-aba-tef.png",
    [
        (1, 0.447, 0.315, 0.620, 0.300),   # a aba
    ],
    recorte=MODAL,
    escala=1.5,
)

# 7. A forma criada na listagem.
annotate(
    "07-forma-criada.png",
    [
        (1, 0.360, 0.180, 0.560, 0.180),   # a forma nova
        (2, 0.835, 0.185, 0.700, 0.245),   # os dois canais ligados
    ],
    recorte=(0.145, 0.045, 1.0, 0.36),
    escala=1.15,
)

# 8. A forma no recebimento de uma mesa (canal presencial).
annotate(
    "08-pagamento-presencial.png",
    [
        (1, 0.575, 0.318, 0.660, 0.480),   # a forma nova, primeira da lista
    ],
    recorte=(0.145, 0.055, 0.860, 0.95),
    escala=1.0,
    borrao=[(0.715, 0.085, 0.150, 0.055)],   # documento do cliente (repositorio publico)
)

# 9. A OUTRA tela: Cardapio Digital -> Formas Recebimento.
annotate(
    "09-cardapio-digital-formas.png",
    [
        (1, 0.575, 0.090, 0.625, 0.140),   # a aba Formas Recebimento
        (2, 0.235, 0.138, 0.190, 0.138),   # botao Adicionar
        (3, 0.790, 0.235, 0.660, 0.285),   # switches Delivery / Retirada
    ],
    recorte=(0.145, 0.045, 1.0, 0.58),
    escala=1.15,
)

# 10. O modal do cardapio digital.
annotate(
    "10-cardapio-adicionar.png",
    [
        (1, 0.780, 0.215, 0.955, 0.185),   # Nome
        (2, 0.780, 0.325, 0.955, 0.292),   # Vincular a Forma de Pagamento
        (3, 0.905, 0.958, 0.790, 0.958),   # ADICIONAR (F2)
    ],
    recorte=(0.635, 0.0, 1.0, 1.0),
    escala=1.7,
)

# 11. A terceira tela (Financeiro), so para nao confundir (contexto).
passthrough("11-financeiro-formas.png", recorte=(0.145, 0.045, 1.0, 0.70), escala=1.0)

print("done")
