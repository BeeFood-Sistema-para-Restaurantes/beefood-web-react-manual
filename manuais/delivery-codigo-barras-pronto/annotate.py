"""Anota as dez capturas do #132 — código de barras que envia o pedido para PRONTO.

Coordenadas em **fração de 0 a 1** da captura, medidas com a grade de frações (seção 3 da
memória geral). Seis puras saem em 2160x1350; as três do impresso saem estreitas (630 de
largura), porque são a captura do papel, e lá as etiquetas vão para a margem branca ao lado
do texto. O cupom aparece três vezes de propósito: sem o código, com o código e com o pé de
perto — é o par antes/depois que explica o que a caixinha faz.

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

# Passo 3 — de onde o impresso sai: o pedido na fila e a impressora do painel.
annotate(
    "03-botao-imprimir-cupom.png",
    [
        (1, 0.385, 0.255, 0.345, 0.310),   # cartão do pedido, para abrir o painel
        (2, 0.916, 0.184, 0.952, 0.125),   # ícone de impressora do painel do pedido
    ],
)

# Passo 4 — o mesmo cupom antes da caixinha: do PIX ele cai direto no rodapé.
annotate(
    "04-cupom-sem-codigo-barras.png",
    [
        (1, 0.300, 0.848, 0.085, 0.800),   # fim do cupom, onde o código vai entrar
    ],
    escala_etiqueta=2.4,
)

# Passo 4 — o cupom depois da caixinha: retirada, e o código no pé.
annotate(
    "05-cupom-com-codigo-barras.png",
    [
        (1, 0.352, 0.056, 0.160, 0.085),   # cabeçalho RETIRADA
        (2, 0.248, 0.752, 0.120, 0.700),   # o código de barras
    ],
    escala_etiqueta=2.4,
)

# Passo 4 — o pé do cupom de perto, para o leitor saber o que mirar.
annotate(
    "06-codigo-no-pe-do-cupom.png",
    [
        (1, 0.300, 0.500, 0.085, 0.500),   # o código de barras
    ],
    escala_etiqueta=2.4,
)

# Passo 5 — o pedido esperando na fila, antes de bipar.
annotate(
    "07-fila-antes-da-leitura.png",
    [
        (1, 0.377, 0.250, 0.325, 0.300),   # cartão do pedido na coluna PREPARO
        # A ponta para logo abaixo do contador: em cima dele, a cabeça da seta tapa o zero.
        (2, 0.766, 0.206, 0.800, 0.270),   # contador da coluna PRONTO, ainda em zero
    ],
)

# Passo 5 — depois de bipar: o aviso e o pedido já em PRONTO.
annotate(
    "08-pedido-em-pronto.png",
    [
        # A ponta mira a faixa do aviso **abaixo** da frase: em cima dela, tapa letra.
        (1, 0.855, 0.080, 0.855, 0.125),   # aviso "Pedido #38 marcado como Pronto"
        (2, 0.795, 0.288, 0.866, 0.288),   # o cartão agora na coluna PRONTO
    ],
)

# Quando o bipe não move nada — o pedido já estava em PRONTO.
annotate(
    "09-pedido-ja-esta-em-pronto.png",
    [
        (1, 0.855, 0.080, 0.855, 0.125),   # aviso "Pedido #38 já está em Pronto"
    ],
)

# Quando o bipe não move nada — o código não é de pedido nenhum da fila de hoje.
annotate(
    "10-pedido-nao-encontrado.png",
    [
        (1, 0.855, 0.105, 0.780, 0.142),   # tarja vermelha com o código que foi lido
    ],
)
