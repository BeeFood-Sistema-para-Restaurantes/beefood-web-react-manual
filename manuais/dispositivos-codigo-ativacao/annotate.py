"""Anota as cinco capturas do #131 — código de ativação em Configuração -> Dispositivos.

Coordenadas em **fração de 0 a 1** da captura, medidas com a grade de frações (seção 3 da
memória geral). Todas as puras saem em 2160x1350.

Três das cinco imagens são modal, e o modal escurece o resto da tela. Onde a etiqueta não
cabe dentro da caixa branca sem cobrir texto, ela vai para a faixa escurecida à esquerda da
caixa: o círculo verde com número branco continua legível ali, e a seta aponta para dentro.
Isso vale para as etiquetas da lista de passos, do QR e da frase de limite.

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


def annotate(nome, marcadores=(), saida=None):
    """`marcadores` = (numero, alvo_x, alvo_y, etiqueta_x, etiqueta_y) em frações 0..1."""
    img = Image.open(os.path.join(SRC, nome)).convert("RGBA")
    W, H = img.size
    camada = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(camada)
    r = int(W * 0.0135)
    w = max(2, int(W * 0.0022))
    fnt = font(int(r * 1.25))
    for (num, afx, afy, bfx, bfy) in marcadores:
        ax, ay = afx * W, afy * H
        bx, by = bfx * W, bfy * H
        ang = math.atan2(ay - by, ax - bx)
        seta(d, bx + (r + 6) * math.cos(ang), by + (r + 6) * math.sin(ang), ax, ay, w)
        etiqueta(d, bx, by, r, num, fnt)
    Image.alpha_composite(img, camada).convert("RGB").save(os.path.join(OUT, saida or nome))
    print("OK", saida or nome, f"{W}x{H}", f"({len(marcadores)} seta(s))")


# Passo 1 — a tela, o item do menu, as vagas e o botão.
annotate(
    "01-tela-dispositivos.png",
    [
        (1, 0.112, 0.413, 0.400, 0.413),   # item Dispositivos, no grupo Configuração
        (2, 0.796, 0.205, 0.700, 0.270),   # linha "15 de 15 livres"
        (3, 0.930, 0.226, 0.930, 0.300),   # botão Ativar aparelho da seção
    ],
)

# Passo 2 — o modal já abre com o código gerado.
annotate(
    "02-modal-codigo-app-garcom.png",
    [
        (1, 0.316, 0.316, 0.262, 0.316),   # os três passos a fazer no aparelho
        (2, 0.552, 0.494, 0.638, 0.450),   # o código de ativação
        (3, 0.532, 0.547, 0.638, 0.600),   # botão Copiar
        (4, 0.446, 0.690, 0.380, 0.690),   # contagem "O código expira em"
    ],
)

# Passo 3 — aparelho com câmera: o mesmo modal traz o QR ao lado do código.
annotate(
    "03-modal-codigo-qr-app-entregador.png",
    [
        (1, 0.316, 0.367, 0.262, 0.367),   # terceiro passo fala da câmera
        (2, 0.327, 0.520, 0.262, 0.520),   # o QR para apontar a câmera
    ],
)

# Quando não há vaga livre, o modal não gera código.
annotate(
    "04-modal-sem-vaga-totem.png",
    [
        (1, 0.315, 0.464, 0.258, 0.464),   # aviso de limite do plano
        (2, 0.434, 0.583, 0.520, 0.583),   # botão CONTRATAR MAIS
    ],
)

# Passo 4 — o código fica na lista, segurando a vaga, até ser usado ou cancelado.
annotate(
    "05-codigo-aguardando-ativacao.png",
    [
        (1, 0.745, 0.217, 0.660, 0.280),   # "1 código aguardando ativação"
        (2, 0.421, 0.330, 0.500, 0.330),   # cartão do código, com a contagem
        (3, 0.408, 0.495, 0.490, 0.495),   # botão Cancelar
    ],
)
