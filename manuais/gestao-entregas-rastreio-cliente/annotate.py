"""Anota as capturas do #121 — o cliente acompanha a entrega no mapa.

As sete imagens deste manual **não** foram capturadas aqui: elas vêm de um pedido real que o
dono fez e entregou no cardápio `menu.beefood.com.br/beefood3`, com um entregador percorrendo o
trajeto da loja até o endereço. Chegaram pelo chat, já no padrão da casa — celular 780x1688
(viewport 390x844 em DPR 2) e computador 2000x1250.

Por isso o arquivo tem duas metades, e a ordem importa:

* `preparar()` recorta o que chegou e grava em `imagens-puras/`. Ela só roda quando a pasta do
  material ainda existe na máquina; depois que ela some, as puras já versionadas bastam. É a
  mesma regra do `copiar-imagens.py` do #24: **o importador nunca escreve em
  `imagens-tratadas/`**, senão a próxima execução apaga as setas.
* `annotate()` desenha seta e etiqueta sobre a pura e grava em `imagens-tratadas/`, a única
  pasta que o `.md` referencia.

A medição das setas está escrita em **pixel da captura original**, não em fração do resultado:
`rec()` converte, já descontando o recorte e a margem. Medir uma vez na tela inteira é o que
permite mexer no recorte depois sem remedir nada — a lição dos seis manuais do app (#111 a
#116). A grade que usei para ler esses pixels é gerada fora do repositório, em `/tmp`.
"""

import math
import os

from PIL import Image, ImageDraw, ImageFont

# De onde vieram as capturas. Caminho de upload do chat: ele não sobrevive à sessão, e é de
# propósito que o script funcione sem ele.
MATERIAL = os.path.expanduser("~/.cursor/projects/workspace/assets")
SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(SRC, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VERDE = (22, 150, 78)
BRANCO = (255, 255, 255)
A_LINHA = 235
A_ETIQ = 245
FUNDO = (233, 237, 239)
FONTES = [
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def font(sz):
    for c in FONTES:
        if os.path.exists(c):
            return ImageFont.truetype(c, sz)
    raise RuntimeError("nenhuma fonte bold encontrada")


def preparar(origem, nome, caixa=None):
    """Traz uma captura do material para `imagens-puras/`, recortada.

    `caixa` é em **pixel da captura original** (esq, topo, dir, base). Quase todo print de
    celular chega com a barra de navegação do cardápio no pé e um vão cinza embaixo, que só
    encolhe o que interessa na página publicada.
    """
    caminho = os.path.join(MATERIAL, origem)
    if not os.path.exists(caminho):
        print("PULA", nome, "(material não está nesta máquina; usando a pura versionada)")
        return
    img = Image.open(caminho).convert("RGB")
    if caixa:
        img = img.crop(caixa)
    img.save(os.path.join(SRC, nome))
    print("PURA", nome, img.size)


def com_margem(nome, esq=0.0, dire=0.0):
    """Acrescenta margem clara ao lado da pura, **fora** da tela.

    Tela de celular é estreita e cheia: etiqueta desenhada dentro dela cobre texto. Com margem,
    a etiqueta mora fora e a seta entra pela borda — o print continua inteiro visível. `esq` e
    `dire` são frações da largura original.

    A margem da direita existe pelo motivo oposto à da esquerda: na tela do pedido, a coluna
    direita é onde moram a hora do despacho e a flecha que abre a linha do tempo. Alcançá-las
    pela esquerda obriga a seta a atravessar a tela inteira por cima do nome do estado.
    """
    caminho = os.path.join(SRC, nome)
    img = Image.open(caminho).convert("RGB")
    W, H = img.size
    dx, dd = int(W * esq), int(W * dire)
    tela = Image.new("RGB", (W + dx + dd, H), FUNDO)
    tela.paste(img, (dx, 0))
    tela.save(caminho)
    print("MARGEM", nome, tela.size)


def margem(nome, m, md=0.0):
    """Margem em fração **do resultado** — `com_margem()` pede em fração do print."""
    dentro = 1 - m - md
    com_margem(nome, esq=m / dentro if m else 0.0, dire=md / dentro if md else 0.0)


def rec(caixa, m=0.0, md=0.0):
    """Converte pixel da captura original em fração da imagem final.

    `caixa` é o mesmo recorte passado ao `preparar()`; `m` e `md` são as margens que `margem()`
    acrescentou, em fração da imagem final.
    """
    x0, y0, x1, y1 = caixa

    def f(x, y):
        return (m + (1 - m - md) * (x - x0) / (x1 - x0),
                (y - y0) / (y1 - y0))
    return f


def seta(d, x0, y0, x1, y1, w):
    col = VERDE + (A_LINHA,)
    d.line([(x0, y0), (x1, y1)], fill=col, width=w)
    ang = math.atan2(y1 - y0, x1 - x0)
    L = w * 4.0
    for s in (0.5, -0.5):
        d.line([(x1, y1), (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))],
               fill=col, width=w)


def etiqueta(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 3, cy - r - 3, cx + r + 3, cy + r + 3], fill=BRANCO + (245,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=VERDE + (A_ETIQ,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
           t, fill=BRANCO, font=fnt)


def annotate(nome, marcadores=(), molduras=(), r=None, w=None):
    """`marcadores`: (número, alvo_x, alvo_y, etiqueta_x, etiqueta_y) — tudo em **fração**.

    Mire a **borda** do elemento quando ele tem texto: seta apontada para o meio de um rótulo
    cobre uma letra, e isso só aparece na conferência em tamanho real.
    """
    img = Image.open(os.path.join(SRC, nome)).convert("RGBA")
    W, H = img.size
    over = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    r = r or int(W * 0.033)
    fnt = font(int(r * 1.25))
    w = w or max(2, int(W * 0.006))
    for (fx, fy, fw, fh) in molduras:
        d.rounded_rectangle([fx * W, fy * H, (fx + fw) * W, (fy + fh) * H],
                            radius=int(r * 0.6), outline=VERDE + (A_LINHA,), width=w)
    for (num, tfx, tfy, efx, efy) in marcadores:
        tx, ty, ex, ey = tfx * W, tfy * H, efx * W, efy * H
        ang = math.atan2(ty - ey, tx - ex)
        seta(d, ex + (r + 6) * math.cos(ang), ey + (r + 6) * math.sin(ang), tx, ty, w)
        etiqueta(d, ex, ey, r, num, fnt)
    Image.alpha_composite(img, over).convert("RGB").save(os.path.join(OUT, nome))
    print("OK", nome, W, H)


# ---------------------------------------------------------------------------------------
# 01 — a mensagem de WhatsApp com o link
# ---------------------------------------------------------------------------------------
# O recorte corta a barra de digitação do WhatsApp no pé. A conversa fica inteira: a primeira
# bolha é o "pedido recebido" que já existia, e é ela que dá o número do pedido que reaparece
# em todas as outras imagens.
C1, M1 = (0, 0, 780, 950), 0.24
preparar("b16f5cc0-a2cb-479f-b1b8-41ab617ee5b2.png", "01-whatsapp-link.png", C1)
margem("01-whatsapp-link.png", M1)
a = rec(C1, M1)
annotate("01-whatsapp-link.png", [
    (1, *a(78, 724), 0.09, a(0, 724)[1]),        # "Seu pedido saiu para entrega." — o texto é seu
    (2, *a(58, 806), 0.09, a(0, 790)[1]),        # "Acompanhe a entrega", acrescentado pelo sistema
    (3, *a(48, 889), 0.09, a(0, 905)[1]),        # o código de 22 caracteres, só deste pedido
], r=30, w=4)

# ---------------------------------------------------------------------------------------
# 02 — o pedido em preparo, no celular do cliente
# ---------------------------------------------------------------------------------------
# Seis marcadores numa tela de celular só se leem porque as informações estão em linhas
# separadas e bem distantes: o número, a barra, o estado, a linha de acompanhamento e os dois
# pinos do mapa. O recorte tira a barra de abas do cardápio no pé.
C2, M2 = (0, 25, 780, 1598), 0.24
preparar("447fc54f-10d8-4784-bde8-10e89baeeab5.png", "02-pedido-em-preparo.png", C2)
margem("02-pedido-em-preparo.png", M2)
a = rec(C2, M2)
annotate("02-pedido-em-preparo.png", [
    (1, *a(28, 219), 0.08, a(0, 219)[1]),        # Pedido nº78 (1173)
    (2, *a(120, 307), 0.08, a(0, 300)[1]),       # a barra de progresso, com quatro etapas
    (3, *a(46, 363), 0.08, a(0, 380)[1]),        # "Pedido sendo preparado"
    (4, *a(112, 450), 0.08, a(0, 460)[1]),       # "Acompanhar entrega" + o aviso honesto
    (5, *a(352, 690), 0.08, a(0, 660)[1]),       # o pino da loja, com a logo
    (6, *a(372, 795), 0.08, a(0, 830)[1]),       # o pino do endereço do cliente
], r=32, w=4)

# ---------------------------------------------------------------------------------------
# 03 — saiu para entrega: o motoboy aparece
# ---------------------------------------------------------------------------------------
# A hora do despacho fica no canto direito da linha do estado, e é o único alvo deste manual
# que pede margem à direita: alcançá-la pela esquerda traçaria uma seta por cima de "Pedido saiu
# para entrega".
C3, M3, MD3 = (0, 25, 780, 1598), 0.24, 0.13
preparar("68ac2b96-11a5-41fd-8d7b-767d16081814.png", "03-saiu-para-entrega.png", C3)
margem("03-saiu-para-entrega.png", M3, MD3)
a = rec(C3, M3, MD3)
annotate("03-saiu-para-entrega.png", [
    (1, *a(46, 363), 0.07, a(0, 380)[1]),        # "Pedido saiu para entrega"
    (2, *a(690, 363), 0.955, a(0, 363)[1]),      # a hora do despacho, ao lado do estado
    (3, *a(118, 448), 0.07, a(0, 470)[1]),       # "Carlos está indo até você"
    (4, *a(118, 488), 0.07, a(0, 560)[1]),       # "A 640 m de você, em linha reta."
    (5, *a(360, 768), 0.07, a(0, 790)[1]),       # a moto, entre a loja e o destino
], r=32, w=4)

# ---------------------------------------------------------------------------------------
# 04 — a tela cheia do acompanhamento, no celular
# ---------------------------------------------------------------------------------------
# É a tela que o link do WhatsApp abre direto. Aqui não repito o título nem a distância, que
# já têm seta na imagem 03: marco só o que é novo — o botão de volta, o mapa alto com os três
# pontos e a folha deslizante.
C4, M4 = (0, 0, 780, 1688), 0.24
preparar("b21e0e55-5982-4636-99a6-fea58463f475.png", "04-mapa-tela-cheia.png", C4)
margem("04-mapa-tela-cheia.png", M4)
a = rec(C4, M4)
annotate("04-mapa-tela-cheia.png", [
    (1, *a(30, 58), 0.08, a(0, 58)[1]),          # "Ir para o pedido"
    (2, *a(26, 252), 0.08, a(0, 260)[1]),        # o cabeçalho: estado, distância e barra
    (3, *a(345, 650), 0.08, a(0, 620)[1]),       # a loja
    (4, *a(358, 831), 0.08, a(0, 830)[1]),       # a moto, que anda
    (5, *a(374, 930), 0.08, a(0, 1010)[1]),      # o endereço do cliente
    (6, *a(148, 1275), 0.08, a(0, 1275)[1]),     # a folha deslizante, com nome e horário
], r=32, w=4)

# ---------------------------------------------------------------------------------------
# 05 — a folha de baixo, com os itens abertos
# ---------------------------------------------------------------------------------------
# Recorte da mesma tela cheia, só da folha. A lista de itens aberta empurra o mapa para fora
# da tela, então a captura inteira mostraria pouco mapa e pouca lista; a folha sozinha se lê,
# e continua reconhecível porque vem com a alça, o cartão do entregador e o endereço.
C5, M5 = (0, 1020, 780, 1688), 0.24
preparar("5d332bb0-c0b0-47b3-a42c-a2c2c85f156e.png", "05-itens-do-pedido.png", C5)
margem("05-itens-do-pedido.png", M5)
a = rec(C5, M5)
annotate("05-itens-do-pedido.png", [
    (1, *a(145, 1160), 0.08, a(0, 1140)[1]),     # o nome do entregador
    (2, *a(148, 1200), 0.08, a(0, 1240)[1]),     # "Posição de 1 min atrás"
    (3, *a(76, 1497), 0.08, a(0, 1480)[1]),      # "1 item do pedido", que abre e fecha
    (4, *a(32, 1585), 0.08, a(0, 1610)[1]),      # o item, com os complementos e o valor
], r=30, w=4)

# ---------------------------------------------------------------------------------------
# 06 — a mesma tela cheia, no computador
# ---------------------------------------------------------------------------------------
# Esta é a única imagem que não precisa de margem: o mapa ocupa três quartos da largura e tem
# espaço vazio de sobra para as etiquetas, ao lado de cada alvo.
C6 = (0, 0, 2000, 1250)
preparar("023451f8-43aa-40c1-a873-7c5cfcafc197.png", "06-mapa-no-computador.png", C6)
a = rec(C6)
annotate("06-mapa-no-computador.png", [
    (1, *a(222, 49), 0.30, a(0, 49)[1]),         # "Ir para o pedido"
    (2, *a(508, 380), 0.30, a(0, 380)[1]),       # o cartão do entregador, com o horário
    (3, *a(1217, 205), 0.545, a(0, 300)[1]),     # a loja, no alto
    (4, *a(1270, 700), 0.545, a(0, 700)[1]),     # a moto, descendo
    (5, *a(1299, 880), 0.545, a(0, 950)[1]),     # o traço pontilhado: distância, não caminho
    (6, *a(1311, 1041), 0.780, a(0, 1140)[1]),   # o endereço do cliente
], r=30, w=4)

# ---------------------------------------------------------------------------------------
# 07 — pedido concluído
# ---------------------------------------------------------------------------------------
# O recorte para logo depois do cartão de avaliação: abaixo dele a tela é um vão cinza de
# quase 400 px, que na página publicada só empurra o texto para baixo.
C7, M7 = (0, 25, 780, 1270), 0.24
preparar("4c51cfaa-11c5-47cf-a3e7-cc6bc43c1dc4.png", "07-pedido-concluido.png", C7)
margem("07-pedido-concluido.png", M7)
a = rec(C7, M7)
annotate("07-pedido-concluido.png", [
    (1, *a(119, 176), 0.08, a(0, 215)[1]),       # o cabeçalho, agora com a data e a hora
    (2, *a(284, 260), 0.08, a(0, 300)[1]),       # "Pedido concluído"
    (3, *a(56, 1083), 0.08, a(0, 1083)[1]),      # "Avalie seu pedido"
], r=30, w=4)
