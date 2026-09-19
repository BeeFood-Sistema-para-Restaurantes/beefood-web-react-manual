"""Anota as capturas do #114 — Código de barras: ligar no cupom e ler no aplicativo.

São duas origens diferentes, e por isso duas convenções de coordenada convivem aqui:

* **Painel** (`01` e `02`): capturas de `/tmp/ge/cap-barras.py`, em 2160x1350. Elas nascem no
  #104, que mostra a mesma tela no contexto de liberar o entregador; aqui o recorte é outro
  (só a caixinha do código de barras), e a anotação é própria. `copiar_pura()` traz o arquivo.
* **Aplicativo** (`04` a `06`): prints do emulador Android que vieram no material do dono, em
  1440x3120. Recortados por fração para tirar a faixa preta, e reamostrados para 700 px de
  largura, que é o que deixa três telas de celular lado a lado na mesma página.

O cupom (`03`) é a única imagem que não é de tela: é a prévia de impressão do pedido, com a
etiqueta no pé — e o endereço do cliente já sai borrado da pura, porque o repositório é
público.
"""

import math
import os
import shutil

from PIL import Image, ImageDraw, ImageFont

# Os prints do app não são capturados aqui: vêm do material que o dono enviou, feito no
# emulador Android. `copiar()` traz cada um para `imagens-puras/`, que continua sendo o
# backup do manual, e só `imagens-tratadas/` é referenciada pelo `.md`.
MATERIAL = "../gestao-entregas/material-recebido/app-entregador"
SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(SRC, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
A_LINE = 235
A_BADGE = 245
FONTES = [
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def font(sz):
    for c in FONTES:
        if os.path.exists(c):
            return ImageFont.truetype(c, sz)
    raise RuntimeError("nenhuma fonte bold encontrada")


FUNDO = (233, 237, 239)


def com_margem(nome, esq=0.0, topo=0.0, dire=0.0, fundo=FUNDO):
    """Acrescenta margem clara à pura, para etiqueta e seta viverem **fora** da tela.

    Tela de celular é estreita e cheia: etiqueta dentro cobre texto, e foi o que aconteceu na
    primeira rodada do leitor de código de barras. Com margem, a seta entra pela borda e o
    print fica inteiro visível. `esq`, `topo` e `dire` são frações da imagem original.

    A margem da direita existe pelo motivo oposto à da esquerda: a coluna direita da tela do app
    é onde moram a flecha `>`, o selo de estado e o `!` de atraso. Alcançá-los pela esquerda
    obriga a seta a atravessar o cartão inteiro por cima do endereço.
    """
    img = Image.open(os.path.join(SRC, nome)).convert("RGB")
    W, H = img.size
    dx, dy, dd = int(W * esq), int(H * topo), int(W * dire)
    tela = Image.new("RGB", (W + dx + dd, H + dy), fundo)
    tela.paste(img, (dx, dy))
    tela.save(os.path.join(SRC, nome))
    print("MARGEM", nome, tela.size)


def copiar(origem, nome, caixa=None, largura=None):
    """Traz um print do material para `imagens-puras/`.

    `caixa` é em **fração** (esq, topo, dir, base) da imagem original: o print do celular tem
    1440x3120 e quase sempre sobra faixa preta em cima e embaixo, que só encolhe o que
    interessa. `largura` reamostra para um tamanho fixo, para as imagens do manual ficarem do
    mesmo tamanho na página.
    """
    caminho = os.path.join(MATERIAL, origem)
    img = Image.open(caminho).convert("RGB")
    if caixa:
        W, H = img.size
        img = img.crop((int(caixa[0] * W), int(caixa[1] * H),
                        int(caixa[2] * W), int(caixa[3] * H)))
    if largura and img.size[0] != largura:
        alt = round(img.size[1] * largura / img.size[0])
        img = img.resize((largura, alt), Image.LANCZOS)
    img.save(os.path.join(SRC, nome))
    print("PURA", nome, img.size)


def copiar_pura(origem, nome):
    """Print que já está em `imagens-puras/` de outro manual (mesma captura, outra anotação)."""
    shutil.copyfile(origem, os.path.join(SRC, nome))
    print("PURA", nome, "(copiada de outro manual)")


# Todo print do material tem 1440x3120. Eu leio as posições numa prévia de 473x1024 — a mesma
# proporção — e é nessa grade que as medições deste arquivo estão escritas. Medir uma vez, na
# tela inteira, e deixar o `rec()` converter é o que permite mexer no recorte depois sem
# remedir nada.
W0, H0 = 473, 1024
M = 0.30       # margem esquerda padrão, em fração da imagem final
ETQ = 0.10     # x da etiqueta, dentro da margem esquerda


def margem(nome, m=M, tm=0.0, md=0.0):
    """Margem em fração **do resultado** — o `com_margem()` pede em fração do print."""
    dentro = 1 - m - tm * 0 - md
    com_margem(nome,
               esq=m / dentro if m else 0.0,
               topo=tm / (1 - tm) if tm else 0.0,
               dire=md / dentro if md else 0.0)


def rec(caixa, m=M, tm=0.0, md=0.0):
    """Converte pixel da prévia do print inteiro em fração da imagem final já recortada.

    `caixa` é o mesmo recorte passado ao `copiar()`; `m`, `tm` e `md` são as margens que o
    `margem()` acrescentou, em fração da imagem final.
    """
    x0, x1 = caixa[0] * W0, caixa[2] * W0
    y0, y1 = caixa[1] * H0, caixa[3] * H0

    def f(x, y):
        return (m + (1 - m - md) * (x - x0) / (x1 - x0),
                tm + (1 - tm) * (y - y0) / (y1 - y0))
    return f


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


def annotate(nome, marcadores=(), molduras=(), r=None, w=None):
    """`marcadores`: (número, alvo_x, alvo_y, etiqueta_x, etiqueta_y) — tudo em **fração**.

    Fração e não pixel porque estes prints vêm recortados e reamostrados: pixel medido numa
    versão morre na primeira vez que o recorte mudar.
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
                            radius=int(r * 0.6), outline=GREEN + (A_LINE,), width=w)
    for (num, tfx, tfy, bfx, bfy) in marcadores:
        tx, ty, bx, by = tfx * W, tfy * H, bfx * W, bfy * H
        ang = math.atan2(ty - by, tx - bx)
        seta(d, bx + (r + 6) * math.cos(ang), by + (r + 6) * math.sin(ang), tx, ty, w)
        badge(d, bx, by, r, num, fnt)
    Image.alpha_composite(img, over).convert("RGB").save(os.path.join(OUT, nome))
    print("OK", nome, W, H)


def passthrough(nome):
    Image.open(os.path.join(SRC, nome)).convert("RGB").save(os.path.join(OUT, nome))
    print("CTX", nome)


def lado_a_lado(nomes, destino, espaco=24, fundo=(233, 237, 239)):
    """Junta prints na horizontal. Duas telas quase iguais explicam mais juntas que separadas."""
    imgs = [Image.open(os.path.join(SRC, n)).convert("RGB") for n in nomes]
    alt = max(i.size[1] for i in imgs)
    larg = sum(i.size[0] for i in imgs) + espaco * (len(imgs) - 1)
    tela = Image.new("RGB", (larg, alt), fundo)
    x = 0
    for i in imgs:
        tela.paste(i, (x, (alt - i.size[1]) // 2))
        x += i.size[0] + espaco
    tela.save(os.path.join(SRC, destino))
    print("JUNTA", destino, tela.size)


def p(x, y, W=2160, H=1350):
    """Pixel da captura do painel -> fração. Os valores vêm dos `.geo.json` do #104."""
    return x / W, y / H


M = 0.30      # margem esquerda das telas de celular


def t(x, y, m=M):
    """Fração medida no print do celular -> fração na imagem com margem."""
    return m + (1 - m) * x, y


# ---------------------------------------------------------------------------------------
# 01 e 02 — o painel: onde a etiqueta é ligada
# ---------------------------------------------------------------------------------------
copiar_pura("../gestao-entregas-liberar-entregador/imagens-puras/06-impressao-layout.png",
            "01-impressao-layout.png")
annotate("01-impressao-layout.png", [
    (1, *p(911, 103), *p(830, 250)),        # aba Layout
    (2, *p(600, 380), *p(600, 520)),        # Cupom Pedido
    (3, *p(1966, 380), *p(2060, 250)),      # lápis
], r=26, w=4)

copiar_pura("../gestao-entregas-liberar-entregador/imagens-puras/07-cupom-texto-padrao.png",
            "02-cupom-texto-padrao.png")
annotate("02-cupom-texto-padrao.png", [
    (1, *p(1141, 312), *p(1141, 200)),      # aba Texto Padrão
    (2, *p(591, 999), *p(420, 1080)),       # caixinha Código de Barras App Entrega
    (3, *p(591, 957), *p(420, 880)),        # QR Code Cardápio Digital, que não é isto
    (4, *p(1468, 1155), *p(1468, 1265)),    # SALVAR E FECHAR
], r=26, w=4)

# ---------------------------------------------------------------------------------------
# 03 — o cupom com a etiqueta no pé
# ---------------------------------------------------------------------------------------
# Única imagem do repositório que **já vem marcada na pura**: ela nasceu no #57, com a moldura e
# a seta desenhadas fora daqui, e é a prévia de um cupom impresso de verdade. Anotar de novo
# empilharia duas marcações sobre o mesmo alvo, então entra por `passthrough()`.
copiar_pura("../gestao-entregas-liberar-entregador/imagens-puras/08-cupom-impresso.png",
            "03-cupom-impresso.png")
passthrough("03-cupom-impresso.png")

# ---------------------------------------------------------------------------------------
# 04 a 07 — o aplicativo
# ---------------------------------------------------------------------------------------
# O rodapé do app. Sem etiqueta numerada de propósito: as quatro abas ficam colada uma na
# outra e qualquer número cobriria o nome de alguma. A moldura basta, e o texto cita a aba.
copiar("03-lista-de-entregas/prints/01-lista-quatro-entregas.png",
       "04-aba-codigo-barras.png", caixa=(0, 0.905, 1, 0.985), largura=900)
annotate("04-aba-codigo-barras.png", molduras=[(0.50, 0.06, 0.245, 0.86)], w=5)

copiar("08-codigo-de-barras/prints/01-leitor-aberto.png",
       "05-leitor-aberto.png", caixa=(0, 0.26, 1, 0.75), largura=700)
com_margem("05-leitor-aberto.png", esq=M / (1 - M))
annotate("05-leitor-aberto.png", [
    (1, *t(0.225, 0.137), 0.10, 0.137),     # LEITURA DE CÓDIGO
    (2, *t(0.06, 0.265), 0.10, 0.265),      # faixa de status (Aguardando Leitura)
    (3, *t(0.02, 0.49), 0.10, 0.49),        # faixa da câmera, entre as linhas vermelhas
    (4, *t(0.06, 0.878), 0.10, 0.878),      # VOLTAR
], r=26, w=4)

copiar("08-codigo-de-barras/prints/02-codigo-na-faixa.png",
       "06-codigo-na-faixa.png", caixa=(0, 0.26, 1, 0.75), largura=700)
com_margem("06-codigo-na-faixa.png", esq=M / (1 - M))
annotate("06-codigo-na-faixa.png", [
    (1, *t(0.02, 0.49), 0.10, 0.49),        # o código dentro da faixa
], r=26, w=4)

copiar("08-codigo-de-barras/prints/03-etiqueta-ean13.png", "07-etiqueta-ean13.png", largura=700)
passthrough("07-etiqueta-ean13.png")
