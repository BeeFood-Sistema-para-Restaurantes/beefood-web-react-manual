"""Anota as capturas do #113 — App do entregador: chegar no endereço.

Mesma técnica dos outros manuais do app: prints do material do dono, `copiar()` recorta por
fração e `rec()` converte pixel da prévia de 473x1024 em fração da imagem final, já com as
margens. Os ajudantes moram no miolo comum (`/tmp/ge/cabeca-app.py`).

Três coisas são próprias deste manual:

* **Quatro imagens são do Google Maps**, não do app. Elas entram porque a pergunta do entregador
  não é "o que o botão faz", é "o que eu vejo depois de tocar" — e o que ele vê é o Maps com a
  origem, as paradas e o tempo. A única anotação nelas é no bloco de origem/destino e no tempo.
* **O cabeçalho da rota virou imagem própria** (`04`), recortado da lista. Ele tem quatro
  informações em três linhas de 30 px; na lista inteira, quatro etiquetas viravam um nó.
* **A etiqueta *em rota* pede margem à direita** (`06`): ela fica no fim da linha do contador, e
  alcançá-la pela esquerda obrigaria a seta a atravessar o cabeçalho inteiro.

A lista com a rota (`03`) entra como contexto, sem seta: ela numera as próprias paradas, e
etiqueta verde numerada em cima disso põe duas numerações concorrendo na mesma imagem — a
armadilha que o #112 registrou.
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
# 01 e 02 — uma entrega: VER NO MAPA
# ---------------------------------------------------------------------------------------
# GOOGLE MAPS e WAZE ficam lado a lado, na mesma linha. Margem só em cima, e as três etiquetas
# apontam para baixo.
C1, TM1 = (0, 0.735, 1, 0.965), 0.30
copiar("05-ver-no-mapa/prints/01-opcoes-de-mapa.png", "01-ver-no-mapa.png", caixa=C1, largura=760)
margem("01-ver-no-mapa.png", m=0.0, tm=TM1)
a = rec(C1, m=0.0, tm=TM1)
annotate("01-ver-no-mapa.png", [
    (1, *a(255, 782), 0.54, 0.11),               # o título VER NO MAPA
    (2, *a(127, 826), 0.27, 0.11),               # GOOGLE MAPS
    (3, *a(345, 826), 0.73, 0.11),               # WAZE
], r=24, w=4)

# A partir daqui a tela é do **Google Maps**, não do app. Anotar só o que o app determinou: a
# origem, o destino e o tempo. O resto é o Maps de todo dia.
C2 = (0, 0.03, 1, 0.99)
copiar("05-ver-no-mapa/prints/02-google-maps-endereco.png",
       "02-google-maps-uma-parada.png", caixa=C2, largura=700)
margem("02-google-maps-uma-parada.png")
a = rec(C2)
annotate("02-google-maps-uma-parada.png", [
    (1, *a(112, 84), ETQ, a(0, 84)[1]),          # a origem: onde você está
    (2, *a(112, 140), ETQ, a(0, 140)[1]),        # o destino: o endereço do cliente
    (3, *a(22, 897), ETQ, a(0, 897)[1]),         # o tempo e a distância
], r=30, w=4)

# ---------------------------------------------------------------------------------------
# 03 a 06 — a rota que o restaurante montou
# ---------------------------------------------------------------------------------------
# Contexto, sem seta: a lista numera as próprias paradas, e etiqueta numerada em cima disso põe
# duas numerações concorrendo (armadilha registrada no #112).
C3 = (0, 0.105, 1, 0.905)
copiar("06-rota-do-restaurante/prints/01-rota-na-lista.png",
       "03-rota-na-lista.png", caixa=C3, largura=760)
passthrough("03-rota-na-lista.png")

# O cabeçalho da rota, sozinho: quatro informações em três linhas apertadas.
C4, M4, TM4, MD4 = (0, 0.12, 1, 0.238), 0.14, 0.30, 0.16
copiar("06-rota-do-restaurante/prints/01-rota-na-lista.png",
       "04-cabecalho-da-rota.png", caixa=C4, largura=1000)
margem("04-cabecalho-da-rota.png", m=M4, tm=TM4, md=MD4)
a = rec(C4, m=M4, tm=TM4, md=MD4)
annotate("04-cabecalho-da-rota.png", [
    (1, *a(33, 147), a(33, 0)[0], 0.11),         # o círculo amarelo com a letra da rota
    (2, *a(105, 147), a(105, 0)[0], 0.11),       # ROTA A
    (3, *a(278, 176), 0.92, a(0, 176)[1]),       # 0 de 3 entregues
    (4, *a(24, 212), 0.05, a(0, 212)[1]),        # INICIAR ROTA
], r=30, w=4)

C5 = (0, 0.105, 1, 0.80)
copiar("06-rota-do-restaurante/prints/02-outras-entregas.png",
       "05-outras-entregas.png", caixa=C5, largura=760)
margem("05-outras-entregas.png")
a = rec(C5)
annotate("05-outras-entregas.png", [
    (1, *a(12, 492), ETQ, a(0, 492)[1]),         # a faixa OUTRAS ENTREGAS (1)
    (2, *a(18, 623), ETQ, a(0, 623)[1]),         # o cartão solto, numerado por conta própria
], r=28, w=4)

# A etiqueta *em rota* fica no fim da linha do contador: margem à direita, e a seta entra por lá.
C6, M6, MD6 = (0, 0.12, 1, 0.238), 0.16, 0.16
copiar("06-rota-do-restaurante/prints/04-rota-despachada.png",
       "06-rota-despachada.png", caixa=C6, largura=1000)
margem("06-rota-despachada.png", m=M6, md=MD6)
a = rec(C6, m=M6, md=MD6)
annotate("06-rota-despachada.png", [
    (1, *a(318, 176), 0.92, a(0, 176)[1]),       # a etiqueta em rota
    (2, *a(24, 212), 0.06, a(0, 212)[1]),        # ABRIR NO MAPS, no lugar do INICIAR ROTA
], r=30, w=4)

C7 = (0, 0.03, 1, 0.99)
copiar("06-rota-do-restaurante/prints/03-rota-no-maps.png",
       "07-rota-no-maps.png", caixa=C7, largura=700)
margem("07-rota-no-maps.png")
a = rec(C7)
annotate("07-rota-no-maps.png", [
    (1, *a(112, 84), ETQ, a(0, 84)[1]),          # a origem: onde você está
    (2, *a(112, 140), ETQ, a(0, 140)[1]),        # 2 stops — as paradas do meio
    (3, *a(112, 196), ETQ, a(0, 196)[1]),        # a última parada, como destino final
    (4, *a(22, 830), ETQ, a(0, 830)[1]),         # o tempo e a distância do trajeto inteiro
], r=30, w=4)

# ---------------------------------------------------------------------------------------
# 08 e 09 — a melhor rota das entregas soltas
# ---------------------------------------------------------------------------------------
C8 = (0, 0.34, 1, 0.945)
copiar("07-melhor-rota/prints/01-abrir-rota.png", "08-abrir-rota.png", caixa=C8, largura=760)
margem("08-abrir-rota.png")
a = rec(C8)
annotate("08-abrir-rota.png", [
    (1, *a(24, 899), ETQ, a(0, 899)[1]),         # MELHOR ROTA GOOGLE MAPS (4)
    (2, *a(155, 407), ETQ, a(0, 407)[1]),        # o título ABRIR ROTA
    (3, *a(205, 506), ETQ, a(0, 506)[1]),        # o ícone do Google Maps
    (4, *a(155, 624), ETQ, a(0, 624)[1]),        # FECHAR
], r=28, w=4)

C9 = (0, 0.03, 1, 0.99)
copiar("07-melhor-rota/prints/02-rota-no-google-maps.png",
       "09-melhor-rota-no-maps.png", caixa=C9, largura=700)
margem("09-melhor-rota-no-maps.png")
a = rec(C9)
annotate("09-melhor-rota-no-maps.png", [
    (1, *a(112, 84), ETQ, a(0, 84)[1]),          # a origem: onde você está
    (2, *a(112, 140), ETQ, a(0, 140)[1]),        # 3 stops
    (3, *a(112, 196), ETQ, a(0, 196)[1]),        # a entrega mais longe, como destino final
    (4, *a(22, 830), ETQ, a(0, 830)[1]),         # o tempo e a distância do trajeto inteiro
], r=30, w=4)

# ---------------------------------------------------------------------------------------
# 10 a 12 — as três telas que o FAQ descrevia por texto
# ---------------------------------------------------------------------------------------
# Vieram da segunda rodada de capturas (`capturas-2/23-rota-com-problema/`). Todas as três são
# pergunta de FAQ com resposta escrita desde a primeira versão do manual; a foto entrou porque
# duas delas são **janela modal**, e janela modal é o que o leitor não consegue imaginar a partir
# da frase — ele precisa reconhecer a caixa na tela para saber que está na pergunta certa.
#
# Nas duas janelas o botão da direita é alcançado pela **direita**: CANCELAR e OK ficam no fim da
# linha de botões, e a seta que entra pela esquerda atravessaria o outro botão para chegar lá.
ETQ_DIR = 0.94

# 10 — o cabeçalho da rota, o INICIAR ROTA tocado e a janela que o servidor não confirmou.
# O recorte guarda o botão de propósito: a janela sozinha não diz **de onde** ela veio.
C10, M10, MD10 = (0, 0.113, 1, 0.645), 0.24, 0.13
copiar("capturas-2/23-rota-com-problema/prints/01-despacho-nao-confirmado.png",
       "10-despacho-nao-confirmado.png", caixa=C10, largura=700)
margem("10-despacho-nao-confirmado.png", m=M10, md=MD10)
a = rec(C10, m=M10, md=MD10)
annotate("10-despacho-nao-confirmado.png", [
    (1, *a(16, 200), ETQ, a(0, 200)[1]),         # INICIAR ROTA, o toque que abriu a janela
    (2, *a(58, 432), ETQ, a(0, 420)[1]),         # o título Despacho não confirmado
    (3, *a(58, 538), ETQ, a(0, 548)[1]),         # "Você ainda pode abrir o mapa e avisar"
    (4, *a(210, 607), ETQ, a(0, 607)[1]),        # CANCELAR
    (5, *a(414, 607), ETQ_DIR, a(0, 607)[1]),    # ABRIR MAPA
], r=36, w=5)

# 11 — duas rotas na mesma lista. Três marcadores por rota, nas mesmas três posições: é a
# repetição que responde a pergunta ("cada rota tem a sua letra, o seu contador e o seu botão")
# sem precisar de frase.
C11, M11 = (0, 0.045, 1, 0.918), 0.28
copiar("capturas-2/23-rota-com-problema/prints/03-duas-rotas.png",
       "11-duas-rotas.png", caixa=C11, largura=640)
margem("11-duas-rotas.png", m=M11)
a = rec(C11, m=M11)
annotate("11-duas-rotas.png", [
    (1, *a(16, 143), ETQ, a(0, 120)[1]),         # o círculo amarelo com o A
    (2, *a(85, 165), ETQ, a(0, 168)[1]),         # 0 de 3 entregues
    (3, *a(18, 200), ETQ, a(0, 216)[1]),         # o INICIAR ROTA da rota A
    (4, *a(16, 823), ETQ, a(0, 800)[1]),         # o círculo amarelo com o B
    (5, *a(85, 845), ETQ, a(0, 848)[1]),         # 0 de 2 entregues
    (6, *a(18, 880), ETQ, a(0, 896)[1]),         # o INICIAR ROTA da rota B
], r=26, w=4)

# 12 — a janela que aparece quando o cálculo da melhor rota não sai. O recorte vai do topo da
# folha ABRIR ROTA até o botão azul, porque os três elementos contam a sequência: o toque no
# botão, a folha que abriu e a janela que parou tudo.
C12, M12, MD12 = (0, 0.367, 1, 0.925), 0.24, 0.13
copiar("capturas-2/23-rota-com-problema/prints/02-falha-melhor-rota.png",
       "12-melhor-rota-falhou.png", caixa=C12, largura=700)
margem("12-melhor-rota-falhou.png", m=M12, md=MD12)
a = rec(C12, m=M12, md=MD12)
annotate("12-melhor-rota-falhou.png", [
    (1, *a(18, 898), ETQ, a(0, 898)[1]),         # MELHOR ROTA GOOGLE MAPS (4)
    (2, *a(157, 400), ETQ, a(0, 412)[1]),        # a folha ABRIR ROTA, atrás da janela
    (3, *a(58, 464), ETQ, a(0, 478)[1]),         # o título Permissão necessária
    (4, *a(58, 501), ETQ, a(0, 560)[1]),         # o texto da permissão de localização
    (5, *a(412, 579), ETQ_DIR, a(0, 579)[1]),    # OK, a única saída da janela
], r=30, w=4)
