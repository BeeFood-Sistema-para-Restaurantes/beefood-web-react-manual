"""Anota as capturas de **Quanto o entregador recebe** (taxa, valor, diária e KM).

As capturas do painel saem em 2160x1350 (1440x900 com `device_scale_factor=1.5`).

**As coordenadas não foram medidas no olho.** Ao lado de cada pura há um `*.geo.json` com
o `getBoundingClientRect()` de cada alvo no momento do print, já convertido para pixel da
imagem (CSS x 1,5). O `alvo()` abaixo lê esse arquivo, então a seta aponta para o elemento
e não para onde alguém achou que ele estava. Quem gerou os JSON: `/tmp/ge/cap119a.py`, `fix119*.py` e `cap119b.py`.

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



# ── Parte 1: onde se configura ────────────────────────────────────────────

carregar("01-area-grupo.png")
annotate("01-area-grupo.png",
         marcadores=[
             (1, *alvo("col_entregador", "cima"), 1700, 470),
             (2, *alvo("lapis"), 500, 470),
         ],
         molduras=[moldura("col_entregador", 10)])

carregar("02-grupo-valores.png")
annotate("02-grupo-valores.png",
         marcadores=[
             (1, *alvo("campo_frete", "esq"), 430, 314),
             (2, *alvo("campo_gratis", "dir"), 1720, 314),
             (3, *alvo("campo_entregador", "esq"), 430, 446),
             (4, *alvo("salvar", "cima"), 1500, 1040),
         ],
         molduras=[moldura("campo_entregador", 8)])

carregar("03-funcionario-diaria-km.png")
annotate("03-funcionario-diaria-km.png",
         marcadores=[
             (1, *alvo("opcao_entregador", "esq"), 450, 504),
             (2, *alvo("campo_diaria", "esq"), 450, 624),
             (3, *alvo("campo_km", "esq"), 450, 774),
             (4, *alvo("salvar", "cima"), 1700, 1090),
         ])

carregar("04-pedido-sem-valor.png")
annotate("04-pedido-sem-valor.png",
         marcadores=[
             (1, *alvo("bloco_entregador", "esq"), 1230, 620),
             (2, *alvo("nao_definido"), 1600, 850),
             (3, *alvo("lapis_valor"), 2000, 850),
         ])

carregar("05-pedido-editando.png")
annotate("05-pedido-editando.png",
         marcadores=[
             (1, *alvo("campo_valor", "esq"), 1250, 620),
             (2, *alvo("confirmar"), 1620, 860),
             (3, *alvo("cancelar"), 1850, 860),
         ])

carregar("06-pedido-com-valor.png")
annotate("06-pedido-com-valor.png",
         marcadores=[
             (1, *alvo("valor_gravado"), 1560, 860),
         ],
         molduras=[moldura("bloco_entregador", 8)])

# ── Parte 2: o relatório ──────────────────────────────────────────────────
# A tela tem 2160 px de largura e três faixas que interessam: os botões, os
# modos de cálculo e o miolo (cartões + tabela). Seis setas na imagem inteira
# ficariam empilhadas num canto, e a faixa vazia que sobra para a etiqueta é
# estreita — então cada faixa virou um recorte, com a etiqueta caindo na folga
# de baixo. A pura inteira fica no disco como backup.

CAB = (700, 175, 2130, 425)
KPI = (700, 390, 2140, 625)
TAB = (700, 560, 2140, 1000)

recortar("07-relatorio-taxa-cliente.png", "07a-cabecalho.png", CAB)
carregar("07-relatorio-taxa-cliente.png")
annotate("07a-cabecalho.png",
         marcadores=[
             (1, *desloca(alvo("ida_volta", "baixo"), CAB), *desloca((830, 400), CAB)),
             (2, *desloca(alvo("modo_cliente", "baixo"), CAB), *desloca((1100, 400), CAB)),
             (3, *desloca(alvo("modo_area", "baixo"), CAB), *desloca((1450, 400), CAB)),
             (4, *desloca(alvo("modo_km", "baixo"), CAB), *desloca((1890, 400), CAB)),
             (5, *desloca(alvo("imprimir_a4", "cima"), CAB), *desloca((1450, 198), CAB)),
             (6, *desloca(alvo("excel", "cima"), CAB), *desloca((2010, 198), CAB)),
         ])

recortar("07-relatorio-taxa-cliente.png", "07b-cartoes.png", KPI)
carregar("07-relatorio-taxa-cliente.png")
annotate("07b-cartoes.png",
         marcadores=[
             (1, *desloca(alvo("kpi_entregas", "baixo"), KPI), *desloca((800, 600), KPI)),
             (2, *desloca(alvo("kpi_km", "baixo"), KPI), *desloca((1090, 600), KPI)),
             (3, *desloca(alvo("kpi_taxa_cliente", "baixo"), KPI), *desloca((1380, 600), KPI)),
             (4, *desloca(alvo("kpi_taxa_entregador", "baixo"), KPI), *desloca((1660, 600), KPI)),
             (5, *desloca(alvo("kpi_diarias", "baixo"), KPI), *desloca((1960, 605), KPI)),
         ])

recortar("07-relatorio-taxa-cliente.png", "07c-resumo.png", TAB)
carregar("07-relatorio-taxa-cliente.png")
annotate("07c-resumo.png",
         marcadores=[
             (1, *desloca(alvo("aba_resumo", "cima"), TAB), *desloca((790, 578), TAB)),
             (2, *desloca(alvo("aba_detalhes", "cima"), TAB), *desloca((1130, 578), TAB)),
             (3, *desloca(alvo("coluna_taxa_cliente", "baixo"), TAB), *desloca((1440, 870), TAB)),
         ])

recortar("08-relatorio-taxa-entregador.png", "08-modo-area.png", TAB)
carregar("08-relatorio-taxa-entregador.png")
annotate("08-modo-area.png",
         marcadores=[
             (1, *desloca(alvo("coluna_taxa_entregador", "baixo"), TAB), *desloca((1420, 870), TAB)),
         ])

recortar("09-relatorio-km-funcionario.png", "09-modo-km.png", TAB)
carregar("09-relatorio-km-funcionario.png")
annotate("09-modo-km.png",
         marcadores=[
             (1, *desloca(alvo("coluna_km_ida", "baixo"), TAB), *desloca((1420, 870), TAB)),
         ])

recortar("10-relatorio-ida-volta.png", "10-ida-e-volta.png", TAB)
carregar("10-relatorio-ida-volta.png")
annotate("10-ida-e-volta.png",
         marcadores=[
             (1, *desloca(alvo("coluna_km_ida", "baixo"), TAB), *desloca((1180, 870), TAB)),
             (2, *desloca(alvo("coluna_km_volta", "baixo"), TAB), *desloca((1420, 870), TAB)),
             (3, *desloca(alvo("coluna_km_total", "baixo"), TAB), *desloca((1660, 870), TAB)),
         ])

carregar("11-todos-os-detalhes.png")
annotate("11-todos-os-detalhes.png",
         marcadores=[
             (1, *alvo("aba_detalhes", "baixo"), 1150, 500),
             (2, *alvo("col_taxa_entregador", "cima"), 1900, 560),
             (3, *alvo("col_km", "cima"), 1620, 480),
         ],
         molduras=[moldura("linha_com_valor", 4)])

carregar("12-detalhe-entregador.png")
annotate("12-detalhe-entregador.png",
         marcadores=[
             (1, *alvo("voltar"), 640, 330),
             (2, *alvo("kpi_total", "baixo"), 1850, 470),
             (3, *alvo("tabela_diarias", "topo-esq"), 600, 700),
             (4, *alvo("col_taxa_entregador", "baixo"), 1300, 470),
         ])
