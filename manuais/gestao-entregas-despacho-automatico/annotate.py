"""Anota as capturas do #109 — Despacho automático.

As capturas do painel saem em 2160x1350 (1440x900 com `device_scale_factor=1.5`).

**As coordenadas não foram medidas no olho.** Ao lado de cada pura há um `*.geo.json` com
o `getBoundingClientRect()` de cada alvo no momento do print, já convertido para pixel da
imagem (CSS x 1,5). O `alvo()` abaixo lê esse arquivo, então a seta aponta para o elemento
e não para onde alguém achou que ele estava. Quem gerou os JSON: `/tmp/ge/cap109.py` e
`cap109c.py`, com `fix109.py` e `fix109b.py` para dois alvos que saíram errados.

A janela de regras é a única captura do bloco que **não** sai em 2160x1350: ela tem 876 px de
altura em CSS e não cabe num viewport de 900. Foi fotografada em 1440x1200, e por isso a
imagem dela tem 1800 px de altura.

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


# --- 01a A janela: o que ela é e os dois avisos -----------------------------
# Duas cópias da mesma pura: onze setas numa imagem só viram novelo, e os avisos e as regras
# são assuntos diferentes. `recortar` com a caixa inteira serve de cópia.
recortar("01-janela-regras.png", "01a-janela-avisos.png", (0, 0, 2160, 1800))
carregar("01-janela-regras.png")
annotate("01a-janela-avisos.png",
         marcadores=[
             (1, *alvo("explicacao", "esq"), 420, 346),
             (2, *alvo("switch_liga"), 1780, 432),
             (3, *alvo("aviso_tela_aberta", "esq"), 420, 530),
             (4, *alvo("aviso_2h", "dir"), 1780, 640),
         ],
         molduras=[moldura("switch_liga"), moldura("aviso_tela_aberta"),
                   moldura("aviso_2h")])

# --- 01b A janela: as sete regras -------------------------------------------
recortar("01-janela-regras.png", "01b-janela-regras.png", (0, 0, 2160, 1800))
carregar("01-janela-regras.png")
annotate("01b-janela-regras.png",
         marcadores=[
             (1, *alvo("max_entregas", "esq"), 420, 771),
             (2, *alvo("dist_max", "esq"), 420, 927),
             (3, *alvo("tempo_max", "esq"), 420, 1107),
             (4, *alvo("liberar_quando", "dir"), 1790, 807),
             (5, *alvo("raio", "dir"), 1790, 987),
             (6, *alvo("considerar_posicao", "dir"), 1790, 1126),
             (7, *alvo("tolerancia_gps", "dir"), 1790, 1332),
         ],
         molduras=[moldura("titulo_agrupamento"), moldura("titulo_entregador")])

# --- 02 O interruptor ligado ------------------------------------------------
carregar("02-janela-ligada.png")
annotate("02-janela-ligada.png",
         marcadores=[
             (1, *alvo("switch_liga"), 1780, 432),
             (2, *alvo("linha_toggle", "esq"), 420, 432),
             (3, *alvo("salvar", "dir"), 1790, 1490),
         ],
         molduras=[moldura("switch_liga"), moldura("salvar")])

# --- 03 A rota que nasceu sozinha -------------------------------------------
carregar("03-rota-automatica.png")
annotate("03-rota-automatica.png",
         marcadores=[
             (1, *alvo("nome_entregador", "esq"), 1300, 430),
             (2, *alvo("chip_situacao", "esq"), 1300, 560),
             (3, *alvo("grupo_sem_rota", "esq"), 1300, 300),
             (4, *alvo("selo_despacho", "baixo"), 1080, 250),
         ],
         molduras=[moldura("cabecalho_rota"), moldura("selo_despacho")])

# --- 04 A rota que ganhou entregador ----------------------------------------
carregar("04-rota-associada.png")
annotate("04-rota-associada.png",
         marcadores=[
             (1, *alvo("nome_entregador", "esq"), 1300, 430),
             (2, *alvo("chip_situacao", "esq"), 1300, 560),
             (3, *alvo("aviao", "esq"), 1300, 700),
             (4, *alvo("chip_prontos", "baixo"), *etiqueta("chip_prontos", "baixo", 110)),
         ],
         molduras=[moldura("cabecalho_rota"), moldura("aviao")])


