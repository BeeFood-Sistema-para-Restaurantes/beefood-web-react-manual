"""Anota as capturas do #105 — Ler o mapa e o painel de entregas.

As capturas do painel saem em 2160x1350 (1440x900 com `device_scale_factor=1.5`).

**As coordenadas não foram medidas no olho.** Ao lado de cada pura há um `*.geo.json` com
o `getBoundingClientRect()` de cada alvo no momento do print, já convertido para pixel da
imagem (CSS x 1,5). O `alvo()` abaixo lê esse arquivo, então a seta aponta para o elemento
e não para onde alguém achou que ele estava. Quem gerou os JSON: `/tmp/ge/cap-geo.py`.

Só a **etiqueta** (onde cai o número) é decisão humana: ela depende de onde há espaço
vazio, e o `esq`/`dir`/`cima`/`baixo` servem para dizer isso em uma palavra.
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


# --- 01 A porta: o botão Entregas na tela Delivery ---------------------------
# Esta captura é anterior ao `geo.json`; as duas coordenadas foram medidas na pura.
annotate("01-porta-delivery.png",
         marcadores=[(1, 1786, 110, 1600, 210)],
         molduras=[(1726, 84, 1876, 136)])

# --- 02 O painel inteiro ----------------------------------------------------
# Os selos do topo saem daqui e vão para a 03: a etiqueta deles caía no mesmo ponto da
# etiqueta do botão Centralizar, e dois números empilhados não se leem.
carregar("02-painel-inteiro.png")
annotate("02-painel-inteiro.png",
         marcadores=[
             (1, *alvo("busca", "esq"), *etiqueta("busca", "esq", 120)),
             (2, *alvo("grupo_sem_rota", "esq"), *etiqueta("grupo_sem_rota", "esq", 120)),
             (3, *alvo("loja_no_mapa"), 822, 560),
             (4, *alvo("rodape_entregadores", "esq"), *etiqueta("rodape_entregadores", "esq", 120)),
             (5, *alvo("camada_mapa", "cima"), *etiqueta("camada_mapa", "cima", 100)),
             (6, *alvo("centralizar", "dir"), *etiqueta("centralizar", "dir", 130)),
         ],
         molduras=[moldura("busca"), moldura("grupo_sem_rota"),
                   moldura("rodape_entregadores"), moldura("camada_mapa")])

# --- 03 Os quatro selos do topo, em recorte ---------------------------------
# Os selos ocupam 800 px dos 2160 da tela: na imagem inteira as quatro setas ficariam
# empilhadas num canto, ilegíveis. O recorte pega a faixa do topo do mapa, com um vão
# embaixo para as etiquetas caberem sem cobrir os selos.
CAIXA_SELOS = (140, 70, 1560, 330)
recortar("02-painel-inteiro.png", "03-selos.png", CAIXA_SELOS)
carregar("02-painel-inteiro.png")
annotate("03-selos.png",
         marcadores=[
             (1, *desloca(alvo("chip_preparacao", "baixo"), CAIXA_SELOS),
              *desloca(etiqueta("chip_preparacao", "baixo", 110), CAIXA_SELOS)),
             (2, *desloca(alvo("chip_prontos", "baixo"), CAIXA_SELOS),
              *desloca(etiqueta("chip_prontos", "baixo", 110), CAIXA_SELOS)),
             (3, *desloca(alvo("chip_em_rota", "baixo"), CAIXA_SELOS),
              *desloca(etiqueta("chip_em_rota", "baixo", 110), CAIXA_SELOS)),
             (4, *desloca(alvo("chip_entregues", "baixo"), CAIXA_SELOS),
              *desloca(etiqueta("chip_entregues", "baixo", 110), CAIXA_SELOS)),
             (5, *desloca(alvo("pilula_despacho", "baixo"), CAIXA_SELOS),
              *desloca(etiqueta("pilula_despacho", "baixo", 110), CAIXA_SELOS)),
             (6, *desloca(alvo("recarregar", "baixo"), CAIXA_SELOS),
              *desloca(etiqueta("recarregar", "baixo", 110), CAIXA_SELOS)),
         ],
         r=22, w=4)

# --- 04 A lista completa de entregadores ------------------------------------
carregar("04-lista-entregadores.png")
annotate("04-lista-entregadores.png",
         marcadores=[
             (1, *alvo("titulo", "esq"), *etiqueta("titulo", "esq", 150)),
             # os dois cabeçalhos de grupo envolvem o grupo inteiro: a seta mira o topo
             (2, *alvo("grupo_disponivel", "topo-esq"), *etiqueta("grupo_disponivel", "esq", 150, "topo")),
             (3, *alvo("linha_entregador", "esq"), *etiqueta("linha_entregador", "esq", 150)),
             (4, *alvo("grupo_offline", "topo-esq"), *etiqueta("grupo_offline", "esq", 150, "topo")),
             (5, *alvo("sem_app", "esq"), *etiqueta("sem_app", "esq", 150)),
         ],
         molduras=[moldura("linha_entregador"), moldura("sem_app")])

# --- 05 Selo desligado: o pedido sai do mapa e da lista ---------------------
passthrough("05-filtro-preparacao-off.png")

# --- 06 As camadas do mapa --------------------------------------------------
passthrough("06-camadas-mapa.png")

# --- 07 A busca -------------------------------------------------------------
passthrough("07-busca.png")
