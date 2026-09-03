"""Anota os screenshots do manual BeeFood - Cadastro de comandas e QR Code (#81).

Le de imagens-puras/ e escreve em imagens-tratadas/.
As coordenadas dos marcadores sao dadas em fracoes 0..1 da imagem PURA (tela cheia,
1440x900 com device_scale_factor 1.5); o recorte e aplicado depois e o script converte
sozinho. Assim medir uma vez na captura cheia serve para qualquer recorte.
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

# Recortes reaproveitados
BARRA = (0.145, 0.045, 1.0, 0.272)      # barra de acoes + primeira linha de cards
MODAL_P = (0.33, 0.27, 0.675, 0.74)    # modal pequeno (Nova Mesa / Editar)
MODAL_M = (0.30, 0.28, 0.71, 0.72)     # modal medio (pergunta da comanda)
MODAL_QR = (0.26, 0.25, 0.775, 0.80)   # modais de QR Code


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


def preparar(name, recorte=None, escala=1.0):
    img = Image.open(os.path.join(SRC, name)).convert("RGB")
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


def annotate(name, markers, ring=None, recorte=None, escala=1.0):
    base = preparar(name, recorte, escala).convert("RGBA")
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


def passthrough(name, recorte=None, escala=1.0):
    img = preparar(name, recorte, escala)
    img.save(os.path.join(OUT, name))
    print("OK (contexto)", name, "->", img.size)


# 1. Onde fica: submenu Cadastros.
annotate(
    "01-menu-cadastros.png",
    [
        (1, 0.058, 0.280, 0.205, 0.280),   # item Comandas
    ],
    recorte=(0.0, 0.11, 0.32, 0.42),
    escala=2.2,
)

# 2. A tela de cadastro de comandas.
annotate(
    "02-tela-comandas.png",
    [
        (1, 0.252, 0.105, 0.252, 0.140),   # Nova Comanda (F1)
        (2, 0.410, 0.105, 0.410, 0.140),   # busca
        (3, 0.545, 0.105, 0.545, 0.140),   # contador
        (4, 0.762, 0.105, 0.762, 0.140),   # Criar em Lote
        (5, 0.878, 0.105, 0.878, 0.140),   # Gerar QR Code
    ],
    recorte=BARRA,
    escala=1.2,
)

# 3. Modal Nova Comanda.
annotate(
    "03-nova-comanda.png",
    [
        (1, 0.410, 0.435, 0.600, 0.400),   # Codigo
        (2, 0.410, 0.532, 0.600, 0.497),   # Descricao
        (3, 0.605, 0.586, 0.480, 0.586),   # Ativo
        (4, 0.607, 0.680, 0.665, 0.715),   # Salvar
    ],
    recorte=MODAL_P,
    escala=2.2,
)

# 4. Dialogo de exclusao.
annotate(
    "04-excluir-comanda.png",
    [
        (1, 0.400, 0.480, 0.400, 0.590),   # texto do aviso
        (2, 0.632, 0.551, 0.645, 0.600),   # botao Excluir
    ],
    recorte=(0.30, 0.38, 0.71, 0.63),
    escala=2.0,
)

# 5. Criar em Lote.
annotate(
    "05-lote-previsao.png",
    [
        (1, 0.415, 0.412, 0.610, 0.378),   # quantidade
        (2, 0.415, 0.510, 0.610, 0.475),   # numeracao inicial
        (3, 0.430, 0.585, 0.470, 0.650),   # previsao
    ],
    recorte=(0.33, 0.25, 0.675, 0.78),
    escala=2.2,
)

# 6. Depois do lote.
annotate(
    "06-lote-resultado.png",
    [
        (1, 0.545, 0.105, 0.545, 0.140),   # contador atualizado
    ],
    recorte=(0.145, 0.045, 1.0, 0.72),
    escala=1.0,
)

# 7. Os tres tipos de QR Code.
annotate(
    "07-qr-tipos.png",
    [
        (1, 0.328, 0.720, 0.328, 0.765),   # Cardapio Digital Presencial
        (2, 0.500, 0.720, 0.500, 0.765),   # Codigo da Comanda
        (3, 0.672, 0.720, 0.672, 0.765),   # Codigo de Barras
    ],
    recorte=(0.23, 0.20, 0.775, 0.81),
    escala=1.5,
)

# 8. QR Code do cardapio digital presencial.
annotate(
    "08-qr-cardapio-presencial.png",
    [
        (1, 0.320, 0.400, 0.320, 0.345),   # Comanda Inicial
        (2, 0.418, 0.400, 0.418, 0.345),   # Comanda Final
        (3, 0.510, 0.400, 0.570, 0.345),   # Gerar QR Codes
        (4, 0.665, 0.470, 0.705, 0.420),   # Imprimir Todos
    ],
    recorte=MODAL_QR,
    escala=1.6,
)

# 9. A folha pronta para imprimir (contexto).
passthrough("09-folha-impressa.png", recorte=(0.0, 0.0, 1.0, 0.60), escala=1.0)

# 10. QR Code do codigo da comanda.
annotate(
    "10-qr-codigo-comanda.png",
    [
        (1, 0.337, 0.600, 0.300, 0.680),   # o QR de uma comanda
        (2, 0.550, 0.470, 0.550, 0.420),   # Download Todos
    ],
    recorte=MODAL_QR,
    escala=1.6,
)

# 11. Codigo de barras EAN-13.
annotate(
    "11-codigo-barras.png",
    [
        (1, 0.337, 0.600, 0.300, 0.690),   # o codigo de barras
    ],
    recorte=MODAL_QR,
    escala=1.6,
)

# 12. O mapa do salao, aba Comandas.
annotate(
    "12-mapa-comandas.png",
    [
        (1, 0.212, 0.135, 0.300, 0.100),   # aba Comandas
        (2, 0.185, 0.203, 0.185, 0.320),   # comanda livre
        (3, 0.310, 0.265, 0.430, 0.320),   # comanda ocupada
    ],
    recorte=(0.145, 0.06, 0.66, 0.55),
    escala=1.4,
)

print("done")
