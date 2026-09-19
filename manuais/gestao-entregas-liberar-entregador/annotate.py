"""Anota as capturas do #104 — Liberar o entregador.

As capturas do painel saem em 2160x1350 (1440x900 com `device_scale_factor=1.5`).

**As coordenadas não foram medidas no olho.** Ao lado de cada pura há um `*.geo.json` com
o `getBoundingClientRect()` de cada alvo no momento do print, já convertido para pixel da
imagem (CSS x 1,5). O `alvo()` abaixo lê esse arquivo, então a seta aponta para o elemento
e não para onde alguém achou que ele estava. Quem gerou os JSON: `/tmp/ge/c104*.py`.

Só a **etiqueta** (onde cai o número) é decisão humana: ela depende de onde há espaço
vazio, e o `esq`/`dir`/`cima`/`baixo` servem para dizer isso em uma palavra.

A oitava imagem é a única sem geometria: é a foto de um cupom impresso, herdada do #57,
e já vem com a marcação verde do artigo original. Ela passa direto.
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


# --- 01 A lista de funcionários ---------------------------------------------
carregar("01-lista-funcionarios.png")
annotate("01-lista-funcionarios.png",
         marcadores=[
             (1, *alvo("novo", "esq"), *etiqueta("novo", "esq", 130)),
             (2, *alvo("busca", "cima"), *etiqueta("busca", "cima", 60)),
             (3, *alvo("card_entregadores", "cima"), *etiqueta("card_entregadores", "cima", 110)),
             (4, *alvo("chip_entregador", "dir"), *etiqueta("chip_entregador", "dir", 150)),
             (5, *alvo("lapis", "dir"), *etiqueta("lapis", "dir", 110)),
         ],
         molduras=[moldura("novo"), moldura("card_entregadores", 14),
                   moldura("chip_entregador")])

# --- 02 A janela do funcionário, aba Dados ----------------------------------
carregar("02-funcionario-dados.png")
annotate("02-funcionario-dados.png",
         marcadores=[
             (1, *alvo("nome", "esq"), *etiqueta("nome", "esq", 150)),
             (2, *alvo("aba_funcao", "cima"), *etiqueta("aba_funcao", "cima", 90)),
             (3, *alvo("ativo", "esq"), *etiqueta("ativo", "esq", 150)),
             (4, *alvo("salvar", "cima"), *etiqueta("salvar", "dir", 150)),
         ],
         molduras=[moldura("aba_funcao"), moldura("ativo"), moldura("salvar")])

# --- 03 A aba Função: é ela que cria o entregador ----------------------------
carregar("03-funcionario-funcao.png")
annotate("03-funcionario-funcao.png",
         marcadores=[
             (1, *alvo("opcao_entregador", "esq"), *etiqueta("opcao_entregador", "esq", 160)),
             (2, *alvo("valor_diaria", "esq"), *etiqueta("valor_diaria", "esq", 160)),
             (3, *alvo("valor_km", "esq"), *etiqueta("valor_km", "esq", 160)),
             (4, *alvo("opcao_garcom", "dir"), *etiqueta("opcao_garcom", "dir", 200)),
             (5, *alvo("salvar", "cima"), *etiqueta("salvar", "dir", 150)),
         ],
         molduras=[moldura("bloco_entregador"), moldura("salvar")])

# --- 04 A lista de usuários -------------------------------------------------
carregar("04-usuarios-lista.png")
annotate("04-usuarios-lista.png",
         marcadores=[
             (1, *alvo("novo", "esq"), *etiqueta("novo", "esq", 130)),
             (2, *alvo("coluna_funcao", "cima"), *etiqueta("coluna_funcao", "cima", 70)),
             (3, *alvo("chip_entregador", "baixo"), *etiqueta("chip_entregador", "baixo", 155)),
         ],
         molduras=[moldura("novo"), moldura("chip_entregador")])

# --- 05 A janela do usuário: o switch que destrava o app --------------------
carregar("05-usuario-novo.png")
annotate("05-usuario-novo.png",
         marcadores=[
             (1, *alvo("login", "esq"), *etiqueta("login", "esq", 150)),
             (2, *alvo("senha", "esq"), *etiqueta("senha", "esq", 150)),
             (3, *alvo("funcionario", "esq"), *etiqueta("funcionario", "esq", 150)),
             (4, *alvo("grupo", "esq"), *etiqueta("grupo", "esq", 150)),
             (5, *alvo("aplicativos", "cima"), *etiqueta("aplicativos", "dir", 160)),
             (6, *alvo("salvar", "baixo"), *etiqueta("salvar", "baixo", 110)),
         ],
         molduras=[moldura("funcionario"), moldura("aplicativos"), moldura("salvar")])

# --- 06 Onde ficam os layouts de impressão ----------------------------------
carregar("06-impressao-layout.png")
annotate("06-impressao-layout.png",
         marcadores=[
             (1, *alvo("aba_layout", "baixo"), *etiqueta("aba_layout", "baixo", 62)),
             (2, *alvo("cupom_pedido", "esq"), *etiqueta("cupom_pedido", "esq", 150)),
             (3, *alvo("lapis", "dir"), *etiqueta("lapis", "dir", 120)),
         ],
         molduras=[moldura("lapis")])

# --- 07 A caixinha do código de barras --------------------------------------
carregar("07-cupom-texto-padrao.png")
annotate("07-cupom-texto-padrao.png",
         marcadores=[
             (1, *alvo("aba_texto", "cima"), *etiqueta("aba_texto", "cima", 90)),
             (2, *alvo("cx_barras", "esq"), *etiqueta("cx_barras", "esq", 200)),
             (3, *alvo("cx_qrcode", "esq"), *etiqueta("cx_qrcode", "esq", 320)),
             (4, *alvo("salvar", "cima"), *etiqueta("salvar", "cima", 120)),
         ],
         molduras=[moldura("rot_barras"), moldura("salvar")])

# --- 08 O cupom impresso, com o código no pé (herdado do #57) ---------------
passthrough("08-cupom-impresso.png")
