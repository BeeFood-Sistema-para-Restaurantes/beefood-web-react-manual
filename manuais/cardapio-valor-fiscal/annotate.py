"""Anota as sete capturas do #133 — o campo Valor fiscal do produto e do complemento.

Coordenadas em **fração de 0 a 1** da captura (seção 3 da memória geral). As puras saem em
2160x1350; a última é recortada antes de anotar, porque a etapa 3 do lote é uma janela quase
vazia e só a faixa de cima interessa.

Onde não há branco limpo dentro da janela, a etiqueta vai para a faixa escurecida ao lado —
o círculo verde com número branco continua legível ali, e a seta aponta para dentro.

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


def annotate(nome, marcadores=(), saida=None, escala_etiqueta=1.0, recorte=None):
    """`marcadores` = (numero, alvo_x, alvo_y, etiqueta_x, etiqueta_y) em frações 0..1.

    `recorte` = (x0, y0, x1, y1), também em frações, aplicado **antes** das setas; as
    coordenadas dos marcadores são então frações do recorte, não da pura.
    """
    img = Image.open(os.path.join(SRC, nome)).convert("RGBA")
    if recorte:
        W0, H0 = img.size
        img = img.crop((int(recorte[0] * W0), int(recorte[1] * H0),
                        int(recorte[2] * W0), int(recorte[3] * H0)))
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


# Passo 1 — a tela Cardápio, aba Produtos: o cadastro abre no clique do nome.
annotate(
    "01-cardapio-produtos.png",
    [
        (1, 0.500, 0.610, 0.575, 0.632),   # nome do combo no cartão
    ],
)

# Passo 2 — o cadastro aberto: o preço de venda e o bloco que esconde o campo.
annotate(
    "02-produto-opcoes-avancadas.png",
    [
        (1, 0.330, 0.440, 0.255, 0.480),   # Preço de Venda R$ 60,00
        (2, 0.318, 0.800, 0.255, 0.800),   # Opções avançadas (fechado)
    ],
)

# Passo 3 — o campo preenchido, o texto de apoio e o salvar.
annotate(
    "03-produto-valor-fiscal.png",
    [
        (1, 0.330, 0.512, 0.250, 0.512),   # campo Valor fiscal com R$ 42,00
        (2, 0.320, 0.556, 0.245, 0.590),   # texto de apoio
        (3, 0.640, 0.900, 0.668, 0.952),   # SALVAR E SAIR (F2)
    ],
)

# Passo 4 — o mesmo campo no complemento que sai de brinde.
annotate(
    "04-complemento-valor-fiscal.png",
    [
        (1, 0.700, 0.591, 0.800, 0.620),   # preços de Delivery/Presencial vazios
        (2, 0.250, 0.745, 0.165, 0.745),   # campo Valor fiscal com R$ 8,00
        (3, 0.670, 0.900, 0.713, 0.952),   # SALVAR E SAIR (F2)
    ],
)

# Passo 5 — Editar em Lote, etapa 1: de onde sai e o que ficou marcado.
annotate(
    "05-lote-selecao.png",
    [
        (1, 0.800, 0.165, 0.800, 0.210),   # botão Editar em Lote, atrás da janela
        (2, 0.300, 0.247, 0.232, 0.258),   # contador de selecionados
        (3, 0.716, 0.875, 0.782, 0.875),   # PRÓXIMO
    ],
)

# Passo 6 — etapa 2: a caixinha Valor fiscal, o valor e o processar.
annotate(
    "06-lote-valor-fiscal.png",
    [
        (1, 0.292, 0.344, 0.228, 0.344),   # caixinha Valor fiscal marcada
        (2, 0.704, 0.384, 0.782, 0.384),   # campo com R$ 30,00
        (3, 0.716, 0.875, 0.790, 0.875),   # PROCESSAR
    ],
)

# Passo 7 — etapa 3: a confirmação, item por item. Recortada na faixa que importa.
annotate(
    "07-lote-resultado.png",
    [
        (1, 0.190, 0.490, 0.300, 0.490),   # "2 sucesso"
    ],
    recorte=(0.255, 0.075, 0.760, 0.330),
    escala_etiqueta=1.8,
)
