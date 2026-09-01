"""Anota os screenshots do manual BeeFood - Entendendo a numeracao dos pedidos (#74).

Le de imagens-puras/ e escreve em imagens-tratadas/.
Coordenadas em fracoes 0..1 (independem da resolucao), medidas com grade de fracoes.

Algumas imagens sao recortadas antes de anotar: a tela cheia do Historico tem 16
colunas e o numero fica ilegivel na pagina publicada. Onde o recorte deixa a faixa
estreita, entra uma margem a esquerda para a seta sair dela e chegar ao numero sem
atravessar botao.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
FUNDO = (244, 244, 245)
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


def preparar(name, recorte=None, escala=1.0, margem_esq=0):
    """Abre a pura, recorta, redimensiona e acrescenta a margem esquerda."""
    img = Image.open(os.path.join(SRC, name)).convert("RGB")
    if recorte:
        W, H = img.size
        x0, y0, x1, y1 = recorte
        img = img.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
    if escala != 1.0:
        img = img.resize((int(img.width * escala), int(img.height * escala)),
                         Image.LANCZOS)
    if margem_esq:
        novo = Image.new("RGB", (img.width + margem_esq, img.height), FUNDO)
        novo.paste(img, (margem_esq, 0))
        img = novo
    return img


def annotate(name, markers, ring=None, recorte=None, escala=1.0, margem_esq=0):
    base = preparar(name, recorte, escala, margem_esq).convert("RGBA")
    W, H = base.size
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = max(14, int(W * 0.0125))
    fnt = font(int(r * 1.2))
    w = max(2, int(W * 0.0022))
    for (fx, fy, fw, fh) in (ring or []):
        x0, y0 = fx * W, fy * H
        d.rectangle([x0, y0, x0 + fw * W, y0 + fh * H],
                    outline=GREEN + (A_LINE,), width=w)
    for (num, tx, ty, bx, by) in markers:
        TX, TY, BX, BY = tx * W, ty * H, bx * W, by * H
        ang = math.atan2(TY - BY, TX - BX)
        draw_arrow(d, BX + (r + 5) * math.cos(ang), BY + (r + 5) * math.sin(ang),
                   TX, TY, w)
        badge(d, BX, BY, r, num, fnt)
    Image.alpha_composite(base, overlay).convert("RGB").save(os.path.join(OUT, name))
    print("OK", name, "->", (W, H))


def passthrough(name, recorte=None, escala=1.0):
    img = preparar(name, recorte, escala)
    img.save(os.path.join(OUT, name))
    print("OK (contexto)", name, "->", img.size)


# 1. Parametros -> card PDV: onde se liga o numero de pedido no PDV.
annotate(
    "01-parametros-pdv.png",
    [
        (1, 0.275, 0.400, 0.455, 0.400),   # rotulo "Numero de Pedido no PDV"
        (2, 0.905, 0.449, 0.758, 0.449),   # o switch
    ],
    recorte=(0.325, 0.455, 0.820, 0.680),
    escala=1.15,
)

# 2. A VIRADA DO CONTADOR: o pedido volta para 1 e a venda continua subindo.
annotate(
    "02-historico-virada.png",
    [
        (1, 0.115, 0.186, 0.045, 0.186),   # 1 (931)  - 1o pedido do caixa novo
        (2, 0.115, 0.270, 0.045, 0.270),   # 60 (930) - ultimo do caixa anterior
        (3, 0.112, 0.775, 0.045, 0.775),   # 924      - venda sem numero de pedido
    ],
    recorte=(0.243, 0.215, 0.620, 0.930),
    escala=1.0,
    margem_esq=110,
)

# 3. Mesa nao recebe numero de pedido - e nao consome numero (5 -> mesas -> 6).
annotate(
    "03-historico-mesa.png",
    [
        (1, 0.115, 0.327, 0.045, 0.327),   # 6 (859) - delivery, tem os dois
        (2, 0.100, 0.612, 0.045, 0.612),   # bloco das mesas
        (3, 0.115, 0.894, 0.045, 0.894),   # 5 (850) - delivery anterior
    ],
    ring=[(0.108, 0.377, 0.727, 0.470)],
    # Comeca abaixo do cabecalho fixo: ele encobre a primeira linha visivel.
    # O cabecalho da coluna aparece na imagem 02.
    recorte=(0.243, 0.296, 0.620, 0.930),
    escala=1.0,
    margem_esq=110,
)

# 4. Delivery: o formato #pedido (venda) no card.
annotate(
    "04-delivery.png",
    [
        (1, 0.530, 0.129, 0.720, 0.129),   # #59 (929)
        (2, 0.530, 0.612, 0.720, 0.612),   # #60 (930)
    ],
    recorte=(0.335, 0.190, 0.535, 0.530),
    escala=1.8,
)

# 5. Detalhe da venda: os dois numeros escritos por extenso.
annotate(
    "05-venda-detalhe.png",
    [
        (1, 0.251, 0.068, 0.330, 0.068),   # Venda No 931
        (2, 0.495, 0.155, 0.580, 0.155),   # Pedido No 1
    ],
    recorte=(0.290, 0.055, 0.720, 0.320),
    escala=1.3,
)

# 6. O cupom que o cliente recebe.
annotate(
    "06-cupom.png",
    [
        (1, 0.710, 0.103, 0.860, 0.103),   # Pedido #1 (931)
    ],
    recorte=(0.020, 0.005, 0.980, 0.762),
    escala=1.3,
)

print("done")
