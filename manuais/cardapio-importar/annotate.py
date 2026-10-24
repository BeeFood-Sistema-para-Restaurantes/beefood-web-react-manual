"""Anota as dezoito capturas do #130 — importação de cardápio.

Coordenadas em **fração de 0 a 1** da captura, medidas com a grade de frações (seção 3 da
memória geral). As puras saem em dois tamanhos — 2160x1350 e 2160x1500 — e a fração dispensa
tratar os dois casos.

Este manual não precisou de nenhuma geometria especial, e isso é uma escolha, não um descuido:
todas as quatro telas são de largura cheia e têm área vazia dentro da própria captura, então a
etiqueta cabe sem recorte e sem faixa montada em volta. Faixa e recorte existem para painel
lateral e para tira de celular, onde metade da imagem é tela escurecida.

Duas capturas entram **sem seta**, por `passthrough()`: a lista de produtos e a de grupos de
opção, depois da importação do iFood. Elas são a prova do resultado, e são densas — não há
pixel vazio onde pôr etiqueta sem cobrir um produto, e não há nada para o leitor clicar nelas.

Regra que vale para todo manual da casa: nada é gravado na pura. Rodar duas vezes tem de dar os
mesmos bytes.
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


def passthrough(nome, saida=None):
    img = Image.open(os.path.join(SRC, nome)).convert("RGB")
    img.save(os.path.join(OUT, saida or nome))
    print("OK", saida or nome, f"{img.width}x{img.height}", "(contexto)")


# =====================================================================================
# Caminho 1 — Copiar do iFood
# =====================================================================================

# 01 — a tela como o cliente novo a encontra: um botão só, e o item no menu do Cardápio.
annotate(
    "01-copiar-ifood-vazio.png",
    marcadores=(
        (1, 0.100, 0.345, 0.215, 0.345),     # menu Copiar do iFood (borda direita do rótulo)
        (2, 0.487, 0.648, 0.395, 0.648),     # botão Copiar Cardápio do iFood (borda esquerda)
    ),
)

# 02 — o modal: a URL da loja e o cardápio que vai receber os produtos.
annotate(
    "02-modal-url-ifood.png",
    marcadores=(
        (1, 0.345, 0.456, 0.255, 0.456),     # campo URL do Restaurante no iFood
        (2, 0.663, 0.456, 0.740, 0.420),     # ícone de colar da área de transferência
        (3, 0.345, 0.554, 0.255, 0.554),     # Cardápio Destino
        (4, 0.605, 0.645, 0.605, 0.730),     # CONFIRMAR (borda inferior do botão)
    ),
)

# 03 — a fila. O cartão é raso e largo, então as etiquetas moram embaixo dele.
annotate(
    "03-importacao-na-fila.png",
    marcadores=(
        (1, 0.748, 0.215, 0.700, 0.310),     # selo Na fila — posição N
        (2, 0.872, 0.220, 0.900, 0.310),     # botão Cancelar (borda inferior)
    ),
)

# 04 — a extração em curso: mensagem que gira, contador e barra.
annotate(
    "04-importacao-em-andamento.png",
    marcadores=(
        (1, 0.740, 0.305, 0.690, 0.450),     # mensagem rotativa (Processando setores...)
        (2, 0.393, 0.345, 0.430, 0.450),     # contador de produtos processados
        (3, 0.898, 0.386, 0.930, 0.450),     # porcentagem da barra
    ),
)

# 05 — concluído: é este selo que autoriza ir conferir o cardápio.
annotate(
    "05-importacao-concluida.png",
    marcadores=(
        (1, 0.862, 0.305, 0.830, 0.400),     # selo Concluído (borda esquerda)
        (2, 0.397, 0.345, 0.450, 0.420),     # 41/41 produtos processados
    ),
)

# 06 e 07 — o resultado. Densas de propósito: o recado é o volume do que entrou.
passthrough("06-produtos-importados.png")
passthrough("07-grupos-opcoes-importados.png")


# =====================================================================================
# Caminho 2 — Copiar de Imagem (Digitalize seu Cardápio)
# =====================================================================================

# 08 — o envio: o que a tela aceita e o campo que orienta a leitura da IA.
annotate(
    "08-digitalizar-arquivo.png",
    marcadores=(
        (1, 0.452, 0.360, 0.360, 0.300),     # formatos e limite de tamanho
        (2, 0.358, 0.555, 0.450, 0.555),     # miniatura do arquivo escolhido
        (3, 0.400, 0.690, 0.480, 0.640),     # Instruções adicionais (opcional)
        (4, 0.572, 0.945, 0.572, 0.890),     # Continuar (borda superior do botão)
    ),
)

# 09 — a conferência: o que a IA leu, em cardápio, antes de virar cadastro.
annotate(
    "09-digitalizar-revisao.png",
    marcadores=(
        (1, 0.232, 0.138, 0.190, 0.138),     # nome do estabelecimento, itens e categorias
        (2, 0.533, 0.110, 0.470, 0.062),     # botão Excel (leva o extraído para planilha)
        (3, 0.275, 0.300, 0.420, 0.300),     # categorias e itens extraídos
        (4, 0.842, 0.963, 0.790, 0.963),     # Continuar (borda esquerda)
    ),
)

# 10 — o assistente: a correção por frase, que é o que esta tela tem de próprio.
annotate(
    "10-digitalizar-assistente.png",
    marcadores=(
        (1, 0.585, 0.871, 0.520, 0.871),     # campo de conversa do assistente
        (2, 0.614, 0.416, 0.560, 0.480),     # resposta do assistente
        (3, 0.477, 0.333, 0.445, 0.295),     # preço já corrigido na lista
    ),
)

# 11 — o único ponto sem volta deste caminho.
annotate(
    "11-digitalizar-confirmar.png",
    marcadores=(
        (1, 0.697, 0.583, 0.780, 0.620),     # Confirmar (borda inferior)
    ),
)

# 12 — o resumo do que entrou, para conferir contra o que a revisão mostrava.
annotate(
    "12-digitalizar-resultado.png",
    marcadores=(
        (1, 0.572, 0.455, 0.572, 0.545),     # cartões com setores, produtos e complementos
    ),
)


# =====================================================================================
# Caminho 3 — Importar via Excel
# =====================================================================================

# 13 — passo 1. As etiquetas ficam fora do modal, na tela escurecida: dentro dele não há vão.
annotate(
    "13-excel-passo1.png",
    marcadores=(
        (1, 0.882, 0.142, 0.845, 0.200),     # botão Importar, de onde o modal sai
        (2, 0.252, 0.342, 0.185, 0.342),     # avisos de nome, NCM e CEST
        (3, 0.253, 0.490, 0.185, 0.490),     # área de arrastar ou escolher o arquivo
        (4, 0.253, 0.651, 0.185, 0.651),     # BAIXAR TEMPLATE
    ),
)

# 14 — passo 2. O mapeamento já vem pronto; o que o leitor faz aqui é conferir.
annotate(
    "14-excel-mapeamento.png",
    marcadores=(
        (1, 0.244, 0.266, 0.185, 0.266),     # registros encontrados e campos mapeados
        (2, 0.250, 0.362, 0.185, 0.362),     # Coluna do Excel
        (3, 0.462, 0.362, 0.400, 0.362),     # Campo do Sistema
        (4, 0.730, 0.470, 0.800, 0.470),     # Exemplo lido da planilha
        (5, 0.742, 0.875, 0.800, 0.875),     # IMPORTAR (borda superior)
    ),
)

# 15 — passo 4. Linha por linha: é aqui que se vê o que não entrou.
annotate(
    "15-excel-resultado.png",
    marcadores=(
        (1, 0.252, 0.402, 0.185, 0.402),     # enviados, sucesso e falhas
        (2, 0.752, 0.402, 0.820, 0.370),     # contador de falhas
        (3, 0.752, 0.545, 0.820, 0.545),     # coluna Status, linha por linha
        (4, 0.752, 0.719, 0.820, 0.719),     # FECHAR (ESC)
    ),
)


# =====================================================================================
# Caminho 4 — Clonar e importar
# =====================================================================================

# 16 — onde fica, e o que ele pede: usuário e senha da **outra** empresa.
annotate(
    "16-clonagem-credenciais.png",
    marcadores=(
        (1, 0.105, 0.556, 0.105, 0.645),     # menu Clonar e importar (borda de baixo)
        (2, 0.235, 0.175, 0.195, 0.175),     # aba Cardápio de outra empresa
        (3, 0.252, 0.450, 0.190, 0.450),     # Usuário da empresa de origem
        (4, 0.252, 0.548, 0.190, 0.548),     # Senha da empresa de origem
        (5, 0.248, 0.611, 0.190, 0.660),     # Continuar
    ),
)

# 17 — a prévia: o que vem de lá, o que já existe aqui e a escolha dos impostos.
annotate(
    "17-clonagem-previa.png",
    marcadores=(
        (1, 0.435, 0.368, 0.510, 0.320),     # nome da empresa de origem
        (2, 0.732, 0.434, 0.790, 0.434),     # o que existe na origem
        (3, 0.717, 0.540, 0.790, 0.560),     # aviso de que o destino já tem cadastro
        (4, 0.253, 0.609, 0.190, 0.609),     # copiar também os impostos
        (5, 0.248, 0.659, 0.190, 0.700),     # Copiar cadastro
    ),
)

# 18 — a confirmação. O clique em COPIAR é o que grava.
annotate(
    "18-clonagem-confirmacao.png",
    marcadores=(
        (1, 0.635, 0.556, 0.720, 0.590),     # COPIAR (borda inferior)
    ),
)
