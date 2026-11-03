"""Anota as cinco capturas do #132 — código de barras que envia o pedido para PRONTO.

Coordenadas em **fração de 0 a 1** da captura, medidas com a grade de frações (seção 3 da
memória geral). Quatro puras saem em 2160x1350; a do cupom sai estreita e alta (630x1139),
porque é a captura do papel, e lá as etiquetas vão para a margem branca ao lado do texto.

Na imagem do modal, a etiqueta que não cabe dentro da caixa branca sem cobrir texto vai
para a faixa escurecida ao lado: o círculo verde com número branco continua legível ali, e
a seta aponta para dentro. Vale para a caixinha e para o botão de salvar.

Regra que vale para todo manual da casa: nada é gravado na pura. Rodar duas vezes tem de dar
os mesmos bytes.
"""

import math
import os

from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

VERDE = (22, 150, 78)
BRANCO = (255, 255, 255)
A_LINHA = 235
A_ETIQ = 245

FONTES = [
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def font(sz):
    for caminho in FONTES:
        if os.path.exists(caminho):
            return ImageFont.truetype(caminho, sz)
    raise RuntimeError("nenhuma fonte bold encontrada")


def seta(d, x0, y0, x1, y1, w):
    cor = VERDE + (A_LINHA,)
    d.line([(x0, y0), (x1, y1)], fill=cor, width=w)
    ang = math.atan2(y1 - y0, x1 - x0)
    L = w * 4.0
    for s in (0.5, -0.5):
        d.line([(x1, y1), (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))],
               fill=cor, width=w)


def etiqueta(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 3, cy - r - 3, cx + r + 3, cy + r + 3], fill=BRANCO + (245,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=VERDE + (A_ETIQ,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
           t, fill=BRANCO, font=fnt)


def annotate(nome, marcadores=(), saida=None, escala_etiqueta=1.0):
    """`marcadores` = (numero, alvo_x, alvo_y, etiqueta_x, etiqueta_y) em frações 0..1.

    `escala_etiqueta` existe só para o cupom: ele é estreito, e um círculo proporcional à
    largura sairia pequeno demais ao lado de um texto de 18 px.
    """
    img = Image.open(os.path.join(SRC, nome)).convert("RGBA")
    W, H = img.size
    camada = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(camada)
    r = int(W * 0.0135 * escala_etiqueta)
    w = max(2, int(W * 0.0022 * escala_etiqueta))
    fnt = font(int(r * 1.25))
    for (num, afx, afy, bfx, bfy) in marcadores:
        ax, ay = afx * W, afy * H
        bx, by = bfx * W, bfy * H
        ang = math.atan2(ay - by, ax - bx)
        seta(d, bx + (r + 6) * math.cos(ang), by + (r + 6) * math.sin(ang), ax, ay, w)
        etiqueta(d, bx, by, r, num, fnt)
    Image.alpha_composite(img, camada).convert("RGB").save(os.path.join(OUT, saida or nome))
    print("OK", saida or nome, f"{W}x{H}", f"({len(marcadores)} seta(s))")


# Passo 1 — onde a configuração mora: Configuração -> Impressão, aba Layout.
annotate(
    "01-aba-layout-cupom-pedido.png",
    [
        (1, 0.415, 0.100, 0.475, 0.152),   # aba Layout, mirando o traço vermelho
        (2, 0.896, 0.269, 0.820, 0.197),   # linha Cupom Pedido, com o lápis
    ],
)

# Passo 2 — a caixinha nova, na aba Texto Padrão, no quadro Delivery.
annotate(
    "02-caixinha-codigo-barras-pronto.png",
    [
        (1, 0.500, 0.223, 0.452, 0.272),   # aba Texto Padrão, mirando o traço vermelho
        (2, 0.270, 0.755, 0.205, 0.755),   # caixinha do código de barras para PRONTO
        (3, 0.754, 0.881, 0.812, 0.881),   # botão SALVAR E FECHAR
    ],
)

# Passo 3 — o cupom: pedido de retirada e o código de barras no pé.
annotate(
    "03-cupom-com-codigo-barras.png",
    [
        (1, 0.352, 0.056, 0.160, 0.085),   # cabeçalho RETIRADA
        (2, 0.248, 0.752, 0.120, 0.700),   # o código de barras
    ],
    escala_etiqueta=2.4,
)

# Passo 4 — o pedido esperando na fila, antes de bipar.
annotate(
    "04-fila-antes-da-leitura.png",
    [
        (1, 0.377, 0.250, 0.325, 0.300),   # cartão do pedido na coluna PREPARO
    ],
)

# Passo 5 — depois de bipar: o aviso e o pedido já em PRONTO.
annotate(
    "05-pedido-em-pronto.png",
    [
        (1, 0.780, 0.097, 0.780, 0.151),   # aviso "Pedido #33 marcado como Pronto"
        (2, 0.812, 0.250, 0.862, 0.250),   # o cartão agora na coluna PRONTO
    ],
)
