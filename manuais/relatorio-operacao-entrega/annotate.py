"""Anota as capturas do relatório **Operação de Entrega** (bloco Gestão de Entregas).

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



# ── As telas ──────────────────────────────────────────────────────────────
# O relatório mora num iframe: a geometria dos `.geo.json` já vem somada ao
# deslocamento do iframe (ver /tmp/ge/alvos.py, `medir_frame`).

carregar("01-menu-delivery.png")
annotate("01-menu-delivery.png",
         marcadores=[
             (1, *alvo("grupo_delivery", "dir"), 700, 724),
             (2, *alvo("item_operacao", "dir"), 900, 838),
             (3, *alvo("item_entregador", "dir"), 940, 940),
         ],
         molduras=[moldura("item_operacao", 8)])

carregar("02-periodo-hoje.png")
annotate("02-periodo-hoje.png",
         marcadores=[
             (1, *alvo("botao_periodo", "dir"), 800, 100),
             (2, *alvo("preset_hoje"), 620, 300),
         ],
         molduras=[moldura("preset_hoje", 6)])

carregar("03-kpis.png")
CARTOES = ("cartao_entregas", "cartao_taxa_entrega", "cartao_taxa_entregador",
           "cartao_duracao")
annotate("03-kpis.png",
         marcadores=[
             # o número fica dentro do cartão, à direita, onde ele é vazio
             (1, *alvo("cartao_entregas", "topo-esq"), 1290, 470),
             (2, *alvo("cartao_taxa_entrega", "topo-esq"), 1970, 665),
             (3, *alvo("cartao_taxa_entregador", "topo-esq"), 1290, 860),
             (4, *alvo("cartao_duracao", "topo-esq"), 1970, 860),
             (5, *alvo("botao_comparativo", "esq"), 1660, 255),
             (6, *alvo("botao_filtros"), 1020, 150),
             (7, *alvo("aba_dados", "dir"), 1120, 347),
         ],
         molduras=[moldura("cartao_taxa_entregador", 6)])

carregar("04-metricas-tempo.png")
annotate("04-metricas-tempo.png",
         marcadores=[
             (1, *alvo("etapa_confirmacao", "esq"), 700, 560),
             (2, *alvo("ajuda"), 1250, 450),
             (3, *alvo("etapa_saida", "esq"), 700, 790),
             (4, *alvo("onde_o_tempo", "topo-esq"), 700, 1010),
         ],
         molduras=[moldura("onde_o_tempo", 4)])

carregar("06-prazos.png")
annotate("06-prazos.png",
         marcadores=[
             (1, *alvo("no_prazo", "topo-esq"), 700, 480),
             (2, *alvo("atrasadas", "topo-esq"), 2100, 480),
             (3, *alvo("atraso_medio", "topo-esq"), 700, 700),
             (4, *alvo("nota_cobertura", "esq"), 700, 880),
         ])

passthrough("08-por-hora.png")

carregar("09-mapa.png")
annotate("09-mapa.png",
         marcadores=[
             (1, *alvo("cor_tempo"), 800, 460),
             (2, *alvo("por_bairro"), 1300, 460),
             (3, *alvo("tela_cheia", "esq"), 1660, 400),
             (4, *alvo("nota_geo", "esq"), 700, 1120),
         ],
         molduras=[moldura("cor_tempo", 6), moldura("por_bairro", 6)])

carregar("09b-mapa-bairros.png")
annotate("09b-mapa-bairros.png",
         marcadores=[
             (1, *alvo("col_tempo_rua", "cima"), 1450, 1010),
             (2, *alvo("col_pontualidade", "cima"), 1720, 1010),
             (3, *alvo("col_cobertura", "cima"), 1990, 1010),
         ],
         molduras=[moldura("linha_centro", 4)])

carregar("10-filtros.png")
annotate("10-filtros.png",
         marcadores=[
             (1, *alvo("origem", "esq"), 1330, 441),
             (2, *alvo("entregador", "esq"), 1330, 579),
             (3, *alvo("valor_min", "esq"), 1330, 717),
             (4, *alvo("horario", "esq"), 1330, 855),
             (5, *alvo("aplicar", "esq"), 1330, 1210),
         ])

carregar("11-dados.png")
annotate("11-dados.png",
         marcadores=[
             (1, *alvo("aba_dados"), 1120, 347),
             (2, *alvo("excel", "esq"), 1700, 170),
             (3, *alvo("col_entregador", "cima"), 1860, 620),
         ])
