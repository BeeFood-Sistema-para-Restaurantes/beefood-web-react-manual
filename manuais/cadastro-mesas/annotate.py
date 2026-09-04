"""Anota os screenshots do manual BeeFood - Cadastro de mesas e QR Code (#80).

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
        (1, 0.055, 0.240, 0.205, 0.240),   # item Mesas
        (2, 0.048, 0.150, 0.205, 0.150),   # Voltar (sai do submenu)
    ],
    recorte=(0.0, 0.11, 0.32, 0.42),
    escala=2.2,
)

# 2. A tela de cadastro de mesas.
annotate(
    "02-tela-mesas.png",
    [
        (1, 0.245, 0.105, 0.245, 0.140),   # Nova Mesa (F1)
        (2, 0.400, 0.105, 0.400, 0.140),   # busca
        (3, 0.530, 0.105, 0.530, 0.140),   # contador de mesas
        (4, 0.755, 0.105, 0.755, 0.140),   # Criar em Lote
        (5, 0.875, 0.105, 0.875, 0.140),   # Gerar QR Code
    ],
    recorte=BARRA,
    escala=1.2,
)

# 3. Modal Nova Mesa.
annotate(
    "03-nova-mesa.png",
    [
        (1, 0.410, 0.435, 0.600, 0.400),   # Codigo
        (2, 0.410, 0.532, 0.600, 0.497),   # Descricao
        (3, 0.605, 0.586, 0.480, 0.586),   # Ativo
        (4, 0.607, 0.680, 0.665, 0.715),   # Salvar
    ],
    recorte=MODAL_P,
    escala=2.2,
)

# 5. Modal Editar Mesa.
annotate(
    "05-editar-mesa.png",
    [
        (1, 0.395, 0.657, 0.430, 0.700),   # Excluir
        (2, 0.610, 0.657, 0.610, 0.700),   # Salvar
    ],
    recorte=MODAL_P,
    escala=2.2,
)

# 6. Dialogo de exclusao.
annotate(
    "06-excluir-mesa.png",
    [
        (1, 0.400, 0.480, 0.400, 0.590),   # texto do aviso
        (2, 0.630, 0.551, 0.640, 0.600),   # botao Excluir
    ],
    recorte=(0.30, 0.38, 0.71, 0.63),
    escala=2.0,
)

# 7. Criar em Lote com conflito de numeracao.
annotate(
    "07-lote-conflito.png",
    [
        (1, 0.410, 0.412, 0.600, 0.378),   # quantidade
        (2, 0.410, 0.510, 0.600, 0.475),   # numeracao inicial
        (3, 0.420, 0.590, 0.460, 0.660),   # aviso de conflito
    ],
    recorte=(0.33, 0.25, 0.675, 0.76),
    escala=2.2,
)

# 8. Criar em Lote valido.
annotate(
    "08-lote-previsao.png",
    [
        (1, 0.430, 0.585, 0.470, 0.650),   # previsao do que sera criado
        (2, 0.600, 0.678, 0.600, 0.730),   # Criar Mesas
    ],
    recorte=(0.33, 0.25, 0.675, 0.78),
    escala=2.2,
)

# 9. Depois do lote.
annotate(
    "09-lote-resultado.png",
    [
        (1, 0.530, 0.105, 0.530, 0.140),   # contador atualizado
        (2, 0.640, 0.615, 0.640, 0.660),   # as mesas novas
    ],
    recorte=(0.145, 0.045, 1.0, 0.72),
    escala=1.0,
)

# 10. Os tres tipos de QR Code.
annotate(
    "10-qr-tipos.png",
    [
        (1, 0.328, 0.720, 0.328, 0.765),   # Cardapio Digital Presencial
        (2, 0.500, 0.720, 0.500, 0.765),   # Codigo da Mesa
        (3, 0.672, 0.720, 0.672, 0.765),   # Codigo de Barras
    ],
    recorte=(0.23, 0.20, 0.775, 0.81),
    escala=1.5,
)

# 11. A pergunta sobre comanda.
annotate(
    "11-qr-gate-comanda.png",
    [
        (1, 0.404, 0.628, 0.404, 0.668),   # Sim, uso Comanda
        (2, 0.595, 0.628, 0.595, 0.668),   # Nao, so Mesas
    ],
    recorte=MODAL_M,
    escala=1.9,
)

# 12. O comparativo (contexto, sem setas).
passthrough("12-qr-recomendacao.png", recorte=(0.185, 0.175, 0.818, 0.83), escala=1.4)

# 13. QR Code do cardapio digital presencial.
annotate(
    "13-qr-cardapio-presencial.png",
    [
        (1, 0.320, 0.400, 0.320, 0.345),   # Mesa Inicial
        (2, 0.412, 0.400, 0.412, 0.345),   # Mesa Final
        (3, 0.500, 0.400, 0.560, 0.345),   # Gerar QR Codes
        (4, 0.660, 0.470, 0.700, 0.420),   # Imprimir Todos
    ],
    recorte=MODAL_QR,
    escala=1.6,
)

# 14. QR Code do codigo da mesa.
annotate(
    "14-qr-codigo-mesa.png",
    [
        (1, 0.337, 0.600, 0.300, 0.680),   # o QR de uma mesa
        (2, 0.545, 0.470, 0.545, 0.420),   # Download Todos
    ],
    recorte=MODAL_QR,
    escala=1.6,
)

# 15. Codigo de barras EAN-13.
annotate(
    "15-codigo-barras.png",
    [
        (1, 0.337, 0.600, 0.300, 0.690),   # o codigo de barras
    ],
    recorte=MODAL_QR,
    escala=1.6,
)

# 16. O mapa do salao com as mesas.
annotate(
    "16-mapa-salao.png",
    [
        (1, 0.322, 0.135, 0.400, 0.100),   # aba Mesas
        (2, 0.200, 0.230, 0.200, 0.320),   # mesa livre
        (3, 0.310, 0.265, 0.430, 0.320),   # mesa ocupada
    ],
    recorte=(0.145, 0.06, 0.66, 0.55),
    escala=1.4,
)

# 17. A folha de QR Codes pronta para imprimir (contexto).
passthrough("17-folha-impressa.png", recorte=(0.0, 0.0, 1.0, 0.60), escala=1.0)

# 18. O cardapio que abre no celular do cliente (contexto).
passthrough("18-cardapio-celular.png", recorte=(0.0, 0.0, 1.0, 0.72), escala=0.72)

print("done")
