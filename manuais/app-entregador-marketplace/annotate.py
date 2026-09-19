"""Anota as capturas do #115 — App do entregador: pedido de iFood e de 99Food.

Mesma técnica dos outros manuais do app: prints do material do dono, `copiar()` recorta por
fração e `rec()` converte pixel da prévia de 473x1024 em fração da imagem final, já com as
margens. Os ajudantes moram no miolo comum (`/tmp/ge/cabeca-app.py`).

Quatro decisões são próprias deste manual:

* **Uma imagem serve as duas plataformas** (`01`): o print da lista do material tem o pedido de
  iFood e o de 99Food um embaixo do outro, com os dois chips. É a melhor imagem do manual, e
  nenhuma montagem foi necessária.
* **Cada tela de detalhes rende duas imagens**: o miolo (observação e chip) e o rodapé escuro. O
  rodapé é onde mora a informação que muda tudo — `COBRAR R$ 0,00` — e ele fica a 200 px de
  distância do chip na tela inteira.
* **O `COBRAR R$ 0,00` é alcançado pela direita.** Ele é a segunda coluna do rodapé; seta pela
  esquerda atravessaria o `TOTAL` e o valor do pedido.
* **Os dois avisos de cópia entram lado a lado** (`09`). Cada plataforma escreve um texto
  diferente (*Localizador copiado* contra *Código copiado*), e a diferença só é visível com as
  duas faixas verdes na mesma imagem. Duas imagens separadas mostrariam "um aviso verde", duas
  vezes.

A numeração dos arquivos segue a ordem do texto: iFood inteiro (`02` a `05`), 99Food inteiro
(`06` a `08`) e a comparação no fim (`09`).
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


# ---------------------------------------------------------------------------------------
# 01 — os dois chips na mesma lista
# ---------------------------------------------------------------------------------------
# O print do material tem o pedido de iFood (#1034) e o de 99Food (#1035) um embaixo do outro.
# O chip amarelo é alcançado pela **direita**: pela esquerda, a seta atravessaria a pílula do
# número do pedido, que é justamente o que a etiqueta 3 explica.
IF = "09-pedido-ifood/prints"
NN = "10-pedido-99food/prints"

C1, M1, MD1 = (0, 0.113, 1, 0.560), 0.28, 0.14
copiar(f"{IF}/01-chip-na-lista.png", "01-chip-na-lista.png", caixa=C1, largura=800)
margem("01-chip-na-lista.png", m=M1, md=MD1)
a = rec(C1, m=M1, md=MD1)
annotate("01-chip-na-lista.png", [
    (1, *a(57, 134), ETQ, a(0, 124)[1]),         # #1034 — o número do pedido no restaurante
    (2, *a(57, 170), ETQ, a(0, 196)[1]),         # o chip vermelho do iFood, com o localizador
    (3, *a(57, 397), ETQ, a(0, 388)[1]),         # #1035 — o outro pedido, mesma pílula laranja
    (4, *a(413, 397), 0.93, a(0, 420)[1]),       # o chip amarelo do 99Food, com o id longo
], r=26, w=4)

# ---------------------------------------------------------------------------------------
# 02 e 03 — o pedido de iFood nos detalhes
# ---------------------------------------------------------------------------------------
C2 = (0, 0.285, 1, 0.480)
copiar(f"{IF}/02-detalhes-ifood.png", "02-detalhes-ifood.png", caixa=C2, largura=820)
margem("02-detalhes-ifood.png")
a = rec(C2)
annotate("02-detalhes-ifood.png", [
    (1, *a(37, 320), ETQ, a(0, 320)[1]),         # a observação laranja que a integração escreveu
    (2, *a(42, 460), ETQ, a(0, 460)[1]),         # o chip do iFood repetido junto aos itens
], r=26, w=4)

# O rodapé escuro é o que muda tudo: pago online, nada a cobrar, e um botão a mais.
C3, M3, MD3 = (0, 0.725, 1, 0.978), 0.28, 0.16
copiar(f"{IF}/02-detalhes-ifood.png", "03-rodape-ifood.png", caixa=C3, largura=900)
margem("03-rodape-ifood.png", m=M3, md=MD3)
a = rec(C3, m=M3, md=MD3)
annotate("03-rodape-ifood.png", [
    (1, *a(22, 787), ETQ, a(0, 787)[1]),         # PAGO ONLINE
    (2, *a(298, 847), 0.93, a(0, 847)[1]),       # COBRAR R$ 0,00 — alcançado pela direita
    (3, *a(24, 897), ETQ, a(0, 897)[1]),         # CONFIRMAR ENTREGA IFOOD
    (4, *a(24, 960), ETQ, a(0, 960)[1]),         # FINALIZAR
], r=26, w=4)

# ---------------------------------------------------------------------------------------
# 04 e 05 — a confirmação no site do iFood, dentro do app
# ---------------------------------------------------------------------------------------
# A faixa de cima é do app; o resto da tela é o site do iFood. As duas primeiras etiquetas
# cobrem a faixa, as outras três a página.
C4, M4, MD4 = (0, 0.040, 1, 0.970), 0.26, 0.14
copiar(f"{IF}/03-tela-de-confirmacao.png",
       "04-tela-de-confirmacao-ifood.png", caixa=C4, largura=700)
margem("04-tela-de-confirmacao-ifood.png", m=M4, md=MD4)
a = rec(C4, m=M4, md=MD4)
annotate("04-tela-de-confirmacao-ifood.png", [
    (1, *a(112, 103), ETQ, a(0, 103)[1]),        # o localizador, dígito a dígito
    (2, *a(450, 88), 0.94, a(0, 88)[1]),         # o botão de copiar
    (3, *a(18, 195), ETQ, a(0, 195)[1]),         # Passo 1 de 2
    (4, *a(50, 740), ETQ, a(0, 740)[1]),         # os oito quadradinhos do código
    (5, *a(24, 950), ETQ, a(0, 950)[1]),         # Continuar, ainda apagado
], r=28, w=4)

# Faixa curta: só a linha dos oito dígitos preenchidos e o Continuar já vermelho.
C5 = (0, 0.555, 1, 0.672)
copiar(f"{IF}/05-codigo-preenchido.png", "05-codigo-preenchido.png", caixa=C5, largura=900)
margem("05-codigo-preenchido.png")
a = rec(C5)
annotate("05-codigo-preenchido.png", [
    (1, *a(48, 600), ETQ, a(0, 595)[1]),         # os oito dígitos nos quadradinhos
    (2, *a(24, 643), ETQ, a(0, 650)[1]),         # Continuar, agora ativo
], r=24, w=4)

# ---------------------------------------------------------------------------------------
# 06 e 07 — o pedido de 99Food nos detalhes
# ---------------------------------------------------------------------------------------
C6 = (0, 0.220, 1, 0.420)
copiar(f"{NN}/01-detalhes-99food.png", "06-detalhes-99food.png", caixa=C6, largura=820)
margem("06-detalhes-99food.png")
a = rec(C6)
annotate("06-detalhes-99food.png", [
    (1, *a(37, 262), ETQ, a(0, 262)[1]),         # a observação laranja, agora dizendo 99Food
    (2, *a(42, 393), ETQ, a(0, 393)[1]),         # o chip amarelo, com o id longo do pedido
], r=26, w=4)

C7, M7, MD7 = (0, 0.725, 1, 0.978), 0.28, 0.16
copiar(f"{NN}/01-detalhes-99food.png", "07-rodape-99food.png", caixa=C7, largura=900)
margem("07-rodape-99food.png", m=M7, md=MD7)
a = rec(C7, m=M7, md=MD7)
annotate("07-rodape-99food.png", [
    (1, *a(22, 787), ETQ, a(0, 787)[1]),         # PIX — a forma que o cliente usou na plataforma
    (2, *a(298, 847), 0.93, a(0, 847)[1]),       # COBRAR R$ 0,00, igual ao iFood
    (3, *a(24, 897), ETQ, a(0, 897)[1]),         # CONFIRMAR ENTREGA 99FOOD, amarelo
], r=26, w=4)

# ---------------------------------------------------------------------------------------
# 08 — a confirmação no site do 99Food
# ---------------------------------------------------------------------------------------
# A etiqueta 4 é o motivo desta imagem existir: o site pede **8 dígitos** e o código que o
# pedido trouxe tem 6. Está escrito na própria página, e o manual repete o aviso.
C8, M8, MD8 = (0, 0.040, 1, 0.970), 0.26, 0.14
copiar(f"{NN}/02-tela-de-confirmacao.png",
       "08-tela-de-confirmacao-99food.png", caixa=C8, largura=700)
margem("08-tela-de-confirmacao-99food.png", m=M8, md=MD8)
a = rec(C8, m=M8, md=MD8)
annotate("08-tela-de-confirmacao-99food.png", [
    (1, *a(188, 101), ETQ, a(0, 101)[1]),        # o código do pedido, sem rótulo
    (2, *a(450, 88), 0.94, a(0, 88)[1]),         # o mesmo botão de copiar
    (3, *a(140, 226), ETQ, a(0, 226)[1]),        # Etapa 1 e Etapa 2
    (4, *a(30, 398), ETQ, a(0, 398)[1]),         # a frase que pede um número de 8 dígitos
    (5, *a(37, 803), ETQ, a(0, 803)[1]),         # os oito quadradinhos, ainda vazios
], r=28, w=4)

# ---------------------------------------------------------------------------------------
# 09 — os dois avisos de cópia, lado a lado
# ---------------------------------------------------------------------------------------
# Separadas, as duas faixas verdes são "um aviso de sucesso", duas vezes. Juntas, mostram a
# única diferença que importa: o texto. Coordenadas aqui são da imagem **montada**, e por isso
# escritas à mão — `rec()` fala de um print só.
CT = (0, 0.055, 1, 0.172)
copiar(f"{IF}/04-localizador-copiado.png", "09a-copiado-ifood.png", caixa=CT, largura=620)
copiar(f"{NN}/03-codigo-copiado.png", "09b-copiado-99food.png", caixa=CT, largura=620)
lado_a_lado(["09a-copiado-ifood.png", "09b-copiado-99food.png"], "09-copiado-lado-a-lado.png")
com_margem("09-copiado-lado-a-lado.png", topo=0.45)
annotate("09-copiado-lado-a-lado.png", [
    (1, 0.098, 0.695, 0.098, 0.12),              # Localizador copiado com sucesso! (iFood)
    (2, 0.608, 0.695, 0.608, 0.12),              # Código copiado com sucesso! (99Food)
], r=24, w=4)

# ---------------------------------------------------------------------------------------
# 10 e 11 — quando a plataforma não responde, e quando ela não pede nada
# ---------------------------------------------------------------------------------------
# Vieram da segunda rodada (`capturas-2/19-sem-internet/` e `24-plataforma-sem-confirmacao/`).
# São as duas últimas perguntas do manual, que até agora não tinham foto.
CP2 = "capturas-2"

# 10 — a tela de confirmação com a página vazia. O recorte para no meio do branco de propósito:
# a imagem inteira seria 70% de nada, e o que ela precisa provar cabe na faixa de cima — a
# **faixa do aplicativo veio**, com o código e os botões; a **página da plataforma não**.
C10 = (0, 0.052, 1, 0.42)
copiar(f"{CP2}/19-sem-internet/prints/02-plataforma-nao-carrega.png",
       "10-plataforma-nao-carrega.png", caixa=C10, largura=700)
margem("10-plataforma-nao-carrega.png")
a = rec(C10)
annotate("10-plataforma-nao-carrega.png", [
    (1, *a(114, 104), ETQ, a(0, 104)[1]),        # o localizador, que é a parte do aplicativo
    (2, *a(60, 250), ETQ, a(0, 250)[1]),         # o branco: a página do site não veio
], r=28, w=4)

# 11 — o pedido de plataforma sem botão de confirmação. O recorte **começa abaixo da linha de
# *Realizado às***: ela traz data e hora, e este print é de dois dias depois dos outros deste
# manual. Nada no recorte mostra data, então nenhuma tinta precisou ser mexida.
C11, M11, MD11 = (0, 0.338, 1, 0.978), 0.24, 0.14
copiar(f"{CP2}/24-plataforma-sem-confirmacao/prints/01-selo-keeta.png",
       "11-plataforma-sem-confirmacao.png", caixa=C11, largura=700)
margem("11-plataforma-sem-confirmacao.png", m=M11, md=MD11)
a = rec(C11, m=M11, md=MD11)
annotate("11-plataforma-sem-confirmacao.png", [
    (1, *a(30, 366), ETQ, a(0, 366)[1]),         # o selo amarelo do pedido de plataforma
    (2, *a(13, 849), ETQ, a(0, 849)[1]),         # PAGO ONLINE
    (3, *a(302, 913), 0.93, a(0, 913)[1]),       # COBRAR R$ 0,00
    (4, *a(13, 960), ETQ, a(0, 960)[1]),         # FINALIZAR, o único botão do rodapé
], r=26, w=4)
