"""Anota as capturas do #111 — App do entregador: instalar, entrar e ficar disponível.

Nenhuma destas imagens é capturada aqui: as treze saem do material que o dono enviou, feito no
emulador `Pixel_7_Pro` contra a filial de teste. `copiar()` traz cada print do material para
`imagens-puras/` já recortado, porque o print de celular tem 1440x3120 e quase metade é faixa
preta ou tela vazia.

Dois padrões de coordenada convivem aqui, e é o que explica o `rec()`:

* **Medida no print inteiro.** Eu li as posições olhando o print original numa prévia de
  473x1024 — que é exatamente a proporção de 1440x3120. `rec(caixa)` recebe o mesmo recorte
  passado ao `copiar()` e converte pixel daquela prévia em fração da imagem final, já com a
  margem. Assim o recorte pode mudar sem refazer medição nenhuma.
* **Margem para a etiqueta.** Tela de celular é estreita e cheia: etiqueta por dentro cobre
  texto. Toda imagem ganha 30% de margem clara à esquerda, e a etiqueta vive lá.

A tela de trabalho (`08`) é a única com margem **em cima** também: o cabeçalho tem três coisas
na mesma linha (menu, título e pílula), e três etiquetas na margem esquerda cairiam uma sobre a
outra. Com faixa em cima, duas delas apontam de cima para baixo.
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
# 01 a 03 — as permissões que o Android pede antes do login
# ---------------------------------------------------------------------------------------
# São janelas do **Android**, não do app: fundo claro, botão azulado. O recorte joga fora a
# tela preta em volta, que não diz nada.
C1 = (0, 0.185, 1, 0.835)
copiar("01-primeiros-passos/prints/01-permissao-localizacao.png",
       "01-permissao-localizacao.png", caixa=C1, largura=700)
margem("01-permissao-localizacao.png")
a = rec(C1)
annotate("01-permissao-localizacao.png", [
    (1, *a(118, 567), ETQ, a(0, 567)[1]),        # Exata
    (2, *a(66, 640), ETQ, a(0, 640)[1]),         # Durante o uso do app
    (3, *a(66, 708), ETQ, a(0, 708)[1]),         # Apenas esta vez
    (4, *a(66, 777), ETQ, a(0, 777)[1]),         # Não permitir
], r=26, w=4)

C2 = (0, 0.055, 1, 0.965)
copiar("01-primeiros-passos/prints/02-permitir-o-tempo-todo.png",
       "02-permitir-o-tempo-todo.png", caixa=C2, largura=700)
margem("02-permitir-o-tempo-todo.png")
a = rec(C2)
annotate("02-permitir-o-tempo-todo.png", [
    (1, *a(44, 583), ETQ, a(0, 583)[1]),         # Permitir o tempo todo
    (2, *a(44, 656), ETQ, a(0, 656)[1]),         # Permitir durante o uso do app
    (3, *a(24, 875), ETQ, a(0, 875)[1]),         # Usar local exato
    (4, *a(12, 81), ETQ, a(0, 81)[1]),           # a flecha de voltar
], r=26, w=4)

C3 = (0, 0.295, 1, 0.735)
copiar("01-primeiros-passos/prints/03-permissao-camera.png",
       "03-permissao-camera.png", caixa=C3, largura=700)
margem("03-permissao-camera.png")
a = rec(C3)
annotate("03-permissao-camera.png", [
    (1, *a(66, 536), ETQ, a(0, 536)[1]),         # Durante o uso do app
    (2, *a(66, 604), ETQ, a(0, 604)[1]),         # Apenas esta vez
    (3, *a(66, 672), ETQ, a(0, 672)[1]),         # Não permitir
], r=26, w=4)

# ---------------------------------------------------------------------------------------
# 04 a 06 — o login
# ---------------------------------------------------------------------------------------
C4 = (0, 0.145, 1, 0.70)
copiar("01-primeiros-passos/prints/04-login-vazio.png", "04-login.png", caixa=C4, largura=700)
margem("04-login.png")
a = rec(C4)
annotate("04-login.png", [
    (1, *a(46, 478), ETQ, a(0, 478)[1]),         # Usuário
    (2, *a(46, 547), ETQ, a(0, 547)[1]),         # Senha
    (3, *a(46, 633), ETQ, a(0, 633)[1]),         # ENTRAR
], r=26, w=4)

# O olho e a senha dividem a **mesma linha**, e etiqueta na margem esquerda só alcançaria uma
# delas. Esta é a única imagem recortada em faixa: sobra do print só a linha da senha, e a
# margem vai **em cima**, com as duas etiquetas apontando para baixo.
C5, TM5 = (0.06, 0.505, 0.94, 0.565), 0.55
copiar("01-primeiros-passos/prints/06-senha-visivel.png",
       "05-senha-visivel.png", caixa=C5, largura=700)
margem("05-senha-visivel.png", m=0.0, tm=TM5)
a = rec(C5, m=0.0, tm=TM5)
annotate("05-senha-visivel.png", [
    (1, *a(110, 547), a(110, 0)[0], 0.22),       # a senha em texto
    (2, *a(395, 547), a(395, 0)[0], 0.22),       # o olho cortado
], r=26, w=4)

C6 = (0, 0.44, 1, 0.72)
copiar("01-primeiros-passos/prints/07-erro-credencial.png",
       "06-erro-credencial.png", caixa=C6, largura=700)
margem("06-erro-credencial.png")
a = rec(C6)
annotate("06-erro-credencial.png", [
    (1, *a(46, 612), ETQ, a(0, 612)[1]),         # a faixa vermelha
], r=26, w=4)

C7 = (0, 0.345, 1, 0.695)
copiar("01-primeiros-passos/prints/08-permissao-notificacoes.png",
       "07-permissao-notificacoes.png", caixa=C7, largura=700)
margem("07-permissao-notificacoes.png")
a = rec(C7)
annotate("07-permissao-notificacoes.png", [
    (1, *a(66, 565), ETQ, a(0, 565)[1]),         # Permitir
    (2, *a(66, 634), ETQ, a(0, 634)[1]),         # Não permitir
], r=26, w=4)

# ---------------------------------------------------------------------------------------
# 08 — a tela de trabalho
# ---------------------------------------------------------------------------------------
# A única com margem em cima: menu, título e pílula dividem a mesma linha do cabeçalho.
C8, TM8 = (0, 0.008, 1, 0.985), 0.07
copiar("01-primeiros-passos/prints/09-entregas-vazia.png",
       "08-tela-de-trabalho.png", caixa=C8, largura=760)
margem("08-tela-de-trabalho.png", tm=TM8)
a = rec(C8, tm=TM8)
annotate("08-tela-de-trabalho.png", [
    (1, *a(38, 96), a(38, 0)[0], 0.030),         # os três riscos do menu
    (2, *a(410, 96), a(410, 0)[0], 0.030),       # a pílula ONLINE
    (3, *a(120, 420), ETQ, a(0, 420)[1]),        # Nenhuma entrega agora
    (4, *a(140, 564), ETQ, a(0, 564)[1]),        # ATUALIZAR
    (5, *a(60, 965), ETQ, a(0, 965)[1]),         # as quatro abas
], r=30, w=4)

# ---------------------------------------------------------------------------------------
# 09 e 10 — a disponibilidade
# ---------------------------------------------------------------------------------------
C9 = (0, 0.41, 1, 0.985)
copiar("02-disponibilidade/prints/01-folha-disponibilidade.png",
       "09-folha-disponibilidade.png", caixa=C9, largura=760)
margem("09-folha-disponibilidade.png")
a = rec(C9)
annotate("09-folha-disponibilidade.png", [
    (1, *a(45, 533), ETQ, a(0, 533)[1]),         # Online
    (2, *a(45, 630), ETQ, a(0, 630)[1]),         # Em pausa
    (3, *a(45, 726), ETQ, a(0, 726)[1]),         # Offline
    (4, *a(22, 825), ETQ, a(0, 825)[1]),         # o aviso em cinza
    (5, *a(45, 906), ETQ, a(0, 906)[1]),         # CANCELAR
], r=28, w=4)

# As três pílulas, uma do lado da outra. Separadas, o leitor compara de memória; juntas, a
# diferença de cor salta. Sem etiqueta: a legenda embaixo da imagem dá conta, e número aqui
# cobriria a própria pílula.
PIL = (0.72, 0.050, 1.0, 0.110)
copiar("01-primeiros-passos/prints/09-entregas-vazia.png", "pil-online.png", PIL, 320)
copiar("02-disponibilidade/prints/02-pilula-pausa.png", "pil-pausa.png", PIL, 320)
copiar("02-disponibilidade/prints/03-pilula-offline.png", "pil-offline.png", PIL, 320)
lado_a_lado(["pil-online.png", "pil-pausa.png", "pil-offline.png"], "10-tres-pilulas.png")
passthrough("10-tres-pilulas.png")

# ---------------------------------------------------------------------------------------
# 11 a 13 — o menu, as permissões e o sair
# ---------------------------------------------------------------------------------------
C11 = (0, 0.037, 1, 0.61)
copiar("15-ajustes-e-sair/prints/01-menu-lateral.png", "11-menu.png", caixa=C11, largura=700)
margem("11-menu.png")
a = rec(C11)
annotate("11-menu.png", [
    (1, *a(30, 323), ETQ, a(0, 323)[1]),         # Entregas
    (2, *a(30, 385), ETQ, a(0, 385)[1]),         # Histórico
    (3, *a(30, 447), ETQ, a(0, 447)[1]),         # Código barras
    (4, *a(30, 509), ETQ, a(0, 509)[1]),         # Permissões
    (5, *a(30, 571), ETQ, a(0, 571)[1]),         # Sair
], r=26, w=4)

C12 = (0, 0.037, 1, 0.71)
copiar("15-ajustes-e-sair/prints/02-permissoes.png", "12-permissoes.png", caixa=C12, largura=700)
margem("12-permissoes.png")
a = rec(C12)
annotate("12-permissoes.png", [
    (1, *a(94, 240), ETQ, a(0, 240)[1]),        # Localização
    (2, *a(94, 358), ETQ, a(0, 358)[1]),        # Localização em segundo plano
    (3, *a(94, 501), ETQ, a(0, 501)[1]),        # Câmera
    (4, *a(94, 618), ETQ, a(0, 618)[1]),        # Notificações
], r=26, w=4)

C13 = (0, 0.53, 1, 0.955)
copiar("15-ajustes-e-sair/prints/03-confirmar-saida.png",
       "13-confirmar-saida.png", caixa=C13, largura=700)
margem("13-confirmar-saida.png")
a = rec(C13)
annotate("13-confirmar-saida.png", [
    (1, *a(72, 833), ETQ, a(0, 833)[1]),         # SAIR
    (2, *a(45, 906), ETQ, a(0, 906)[1]),         # CANCELAR
], r=26, w=4)
