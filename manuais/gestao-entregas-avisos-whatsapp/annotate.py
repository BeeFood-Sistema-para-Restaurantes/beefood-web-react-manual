"""Anota as capturas do #110 — Avisos de WhatsApp da entrega.

As capturas do painel saem em 2160x1350 (1440x900 com `device_scale_factor=1.5`) e ao lado de
cada pura há um `*.geo.json` com o `getBoundingClientRect()` do alvo no momento do print, já
em pixel da imagem. Quem gerou: `/tmp/ge/cap110.py`, `cap110b.py` e `cap110c.py`.

Duas imagens não vêm do sistema: as conversas de WhatsApp são **mockup**, porque o sandbox
não tem número conectado e o dono autorizou mensagem fake neste manual. Elas não são escritas
à mão — o `/tmp/ge/mock110.py` lê o `msgPadrao` gravado no banco, troca os marcadores pelos
dados do cenário e resolve o `{a|b}` na primeira opção. Entram por `passthrough()`.
"""

import json
import math
import os

from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
A_LINE = 235
A_BADGE = 245
FONTES = [
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]

_geo = {}


def font(sz):
    for c in FONTES:
        if os.path.exists(c):
            return ImageFont.truetype(c, sz)
    raise RuntimeError("nenhuma fonte bold encontrada")


def carregar(nome):
    """Lê o `*.geo.json` da captura e deixa os alvos acessíveis por rótulo."""
    global _geo
    caminho = os.path.join(SRC, nome.rsplit(".", 1)[0] + ".geo.json")
    _geo = json.load(open(caminho, encoding="utf-8")) if os.path.exists(caminho) else {}
    if not _geo:
        print(f"   (sem geometria para {nome} — coordenadas na mão)")


def alvo(rotulo, borda=None):
    """Ponto da seta. `borda` evita que a ponta caia sobre o texto do elemento.

    Mirar o **centro** de um botão com rótulo cobre uma letra. `borda='esq'` põe a ponta na
    borda esquerda, e assim por diante — o elemento fica marcado sem nada tapado.
    """
    p = _geo[rotulo]
    if borda == "esq":
        return p["x"] + 4, p["cy"]
    if borda == "dir":
        return p["x"] + p["w"] - 4, p["cy"]
    if borda == "cima":
        return p["cx"], p["y"] + 4
    if borda == "baixo":
        return p["cx"], p["y"] + p["h"] - 4
    if borda == "topo-esq":
        # cabeçalho de grupo: o rótulo fica no canto superior esquerdo de um contêiner
        # largo, e mirar o centro do topo deixa a ponta no vazio, longe do texto
        return p["x"] + 30, p["y"] + 14
    return p["cx"], p["cy"]


def etiqueta(rotulo, lado, folga=150, altura=None):
    """Posição do número, a uma folga do elemento, no lado pedido.

    `altura='topo'` alinha a etiqueta com a **primeira linha** do elemento em vez do centro.
    Faz diferença em contêiner alto: o cabeçalho *Disponível (1)* da lista de entregadores
    envolve o grupo inteiro (490 px), e a etiqueta no centro ficava ao lado da terceira
    linha do grupo, apontando para o entregador errado.
    """
    p = _geo[rotulo]
    y = p["y"] + 16 if altura == "topo" else p["cy"]
    if lado == "esq":
        return p["x"] - folga, y
    if lado == "dir":
        return p["x"] + p["w"] + folga, y
    if lado == "cima":
        return p["cx"], p["y"] - folga
    return p["cx"], p["y"] + p["h"] + folga


def moldura(rotulo, folga=6):
    p = _geo[rotulo]
    return (p["x"] - folga, p["y"] - folga,
            p["x"] + p["w"] + folga, p["y"] + p["h"] + folga)


def seta(d, x0, y0, x1, y1, w):
    col = GREEN + (A_LINE,)
    d.line([(x0, y0), (x1, y1)], fill=col, width=w)
    ang = math.atan2(y1 - y0, x1 - x0)
    L = w * 4.0
    for s in (0.5, -0.5):
        d.line([(x1, y1), (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))],
               fill=col, width=w)


def badge(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 3, cy - r - 3, cx + r + 3, cy + r + 3], fill=WHITE + (245,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN + (A_BADGE,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
           t, fill=WHITE, font=fnt)


def recortar(origem, destino, caixa):
    """Grava um recorte da pura **também em imagens-puras/**, como fonte do annotate.

    Existe para a faixa de selos do topo: os quatro selos ocupam 800 px de uma imagem de
    2160, e as quatro setas na imagem inteira ficariam empilhadas num canto. Recortar aqui,
    e não na captura, mantém a pura original como backup.
    """
    Image.open(os.path.join(SRC, origem)).convert("RGB").crop(caixa).save(
        os.path.join(SRC, destino))
    print("RECORTE", destino, caixa)


def desloca(ponto, caixa):
    """Converte coordenada da pura inteira para coordenada do recorte."""
    return ponto[0] - caixa[0], ponto[1] - caixa[1]


def annotate(nome, marcadores=(), molduras=(), r=None, w=None):
    img = Image.open(os.path.join(SRC, nome)).convert("RGBA")
    W, H = img.size
    over = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    r = r or int(W * 0.0125)
    fnt = font(int(r * 1.25))
    w = w or max(2, int(W * 0.0022))
    for (x0, y0, x1, y1) in molduras:
        d.rounded_rectangle([x0, y0, x1, y1], radius=int(r * 0.6),
                            outline=GREEN + (A_LINE,), width=w)
    for (num, tx, ty, bx, by) in marcadores:
        ang = math.atan2(ty - by, tx - bx)
        seta(d, bx + (r + 6) * math.cos(ang), by + (r + 6) * math.sin(ang), tx, ty, w)
        badge(d, bx, by, r, num, fnt)
    Image.alpha_composite(img, over).convert("RGB").save(os.path.join(OUT, nome))
    print("OK", nome, W, H)


def passthrough(nome):
    Image.open(os.path.join(SRC, nome)).convert("RGB").save(os.path.join(OUT, nome))
    print("CTX", nome)


# ---------------------------------------------------------------------------------------
# 01 — a lista de notificações, com os dois grupos
# ---------------------------------------------------------------------------------------
carregar("01-lista-notificacoes.png")
annotate("01-lista-notificacoes.png", [
    (1, *alvo("delivery", "esq"), *etiqueta("delivery", "esq", 120)),
    (2, *alvo("interruptor"), *etiqueta("interruptor", "esq", 120)),
    # o lápis não tem rótulo de texto para medir: a coluna dele é fixa, no fim do cartão
    (3, 1905, 364, 2050, 250),
])

# ---------------------------------------------------------------------------------------
# 02 — o grupo Entregador, e o aviso do cliente que fica logo acima dele
# ---------------------------------------------------------------------------------------
carregar("02-grupo-entregador.png")
annotate("02-grupo-entregador.png", [
    (1, *alvo("grupo", "esq"), *etiqueta("grupo", "esq", 120)),
    (2, *alvo("nova", "esq"), *etiqueta("nova", "esq", 190)),
    (3, *alvo("cancelada", "esq"), *etiqueta("cancelada", "esq", 190)),
    (4, *alvo("relatorio", "esq"), *etiqueta("relatorio", "esq", 190)),
    # "Entregador próximo" é o quarto aviso da entrega, e ele **não** está neste grupo:
    # é mensagem de cliente, então mora no grupo Delivery, acima
    (5, 719, 803, 470, 720),
])

# ---------------------------------------------------------------------------------------
# 03 — Nova entrega: o texto de fábrica e a paleta de variáveis
# ---------------------------------------------------------------------------------------
carregar("03-modal-nova-entrega.png")
annotate("03-modal-nova-entrega.png", [
    (1, *alvo("mensagem", "cima"), *etiqueta("mensagem", "cima", 90)),
    (2, 1852, 175, 1700, 90),          # Restaurar padrão
    (3, 1180, 1000, 1010, 1080),       # a paleta de variáveis
])

# ---------------------------------------------------------------------------------------
# 04 — Relatório diário: os quatro marcadores que só existem nesta mensagem
# ---------------------------------------------------------------------------------------
carregar("04-modal-relatorio-diario.png")
annotate("04-modal-relatorio-diario.png", [
    # os dois marcadores são vizinhos de linha: as etiquetas vão para a área vazia do campo,
    # à direita, senão uma cobre o texto da outra
    (1, 1330, 382, 1760, 330),         # **DETALHE_ENTREGAS**
    (2, 1250, 411, 1760, 470),         # **LINHA_TAXAS**
])

# ---------------------------------------------------------------------------------------
# 05 — Entregador próximo: o campo de km, que só existe aqui
# ---------------------------------------------------------------------------------------
carregar("05-modal-entregador-proximo.png")
annotate("05-modal-entregador-proximo.png", [
    (1, *alvo("km"), *etiqueta("km", "dir", 430)),
    (2, *alvo("mensagem", "cima"), *etiqueta("mensagem", "cima", 70)),
    (3, *alvo("variacoes", "esq"), *etiqueta("variacoes", "esq", 120)),
    (4, *alvo("salvar"), *etiqueta("salvar", "cima", 110)),
])

# ---------------------------------------------------------------------------------------
# 07 — o teto de 50 km: 2000 no campo de km é recusado
# ---------------------------------------------------------------------------------------
carregar("07-km-recusado.png")
annotate("07-km-recusado.png", [
    (1, *alvo("km"), *etiqueta("km", "baixo", 120)),
    (2, *alvo("aviso", "esq"), *etiqueta("aviso", "esq", 140)),
])

# ---------------------------------------------------------------------------------------
# 08 e 09 — as conversas. Mockup, e recortadas para não sobrar fundo vazio.
# ---------------------------------------------------------------------------------------
recortar("08-whatsapp-do-entregador.png", "08a-conversa-entregador.png", (0, 0, 958, 1620))
passthrough("08a-conversa-entregador.png")

recortar("09-whatsapp-do-cliente.png", "09a-conversa-cliente.png", (0, 0, 1944, 1340))
passthrough("09a-conversa-cliente.png")

# ---------------------------------------------------------------------------------------
# 10 — o Celular do funcionário, que é para onde as três mensagens vão
# ---------------------------------------------------------------------------------------
CAIXA_FUNC = (540, 140, 1620, 1180)
carregar("10-funcionario-celular.png")
recortar("10-funcionario-celular.png", "10a-celular-do-entregador.png", CAIXA_FUNC)
annotate("10a-celular-do-entregador.png", [
    # etiqueta **dentro** da caixinha, no fim dela: as duas estão vazias, e qualquer lado de
    # fora cobriria o rótulo do campo de cima (E-mail) ou de baixo (Data de Admissão)
    (1, *desloca(alvo("telefone", "esq"), CAIXA_FUNC), 440, 602),
    (2, *desloca(alvo("celular", "esq"), CAIXA_FUNC), 895, 602),
])
