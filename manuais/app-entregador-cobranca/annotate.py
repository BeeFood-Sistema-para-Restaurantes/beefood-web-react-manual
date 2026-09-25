"""Anota as capturas do #116 — App do entregador: receber na porta.

Mesma técnica dos outros manuais do app: prints do material do dono, `copiar()` recorta por
fração e `rec()` converte pixel da prévia de 473x1024 em fração da imagem final, já com as
margens. Os ajudantes moram no miolo comum (`/tmp/ge/cabeca-app.py`).

Este é o manual do dinheiro, e é o maior do bloco do aplicativo: treze imagens, de três
capítulos do material (cobrança, divisão de conta e finalizar sem cobrar). O que ele tem de
próprio:

* **Quase toda imagem é um recorte de folha.** A cobrança acontece em folhas que sobem por cima
  da tela de pagamento; recortar a folha, e não a tela inteira, é o que deixa o texto legível.
  A tela de pagamento (`03`) é a única capturada inteira, porque é o mapa da operação.
* **O rodapé tem três colunas** (`TOTAL`, `TROCO`, `COBRAR`) e por isso usa **três margens ao
  mesmo tempo**: esquerda para a primeira coluna e os botões, direita para o valor a cobrar, e
  uma margem em cima só para a coluna do meio, que não tem lado livre nenhum.
* **A tela de sucesso entra sem seta** (`08`): uma marca verde e uma frase não precisam de
  etiqueta, e a única etiqueta possível apontaria para o texto que a legenda já repete.
* **O contador de caracteres é alcançado pela direita** (`13`). Ele é a prova de que a
  observação tem limite, e vive encostado na borda.

A ordem dos arquivos é a ordem do texto: cobrança inteira (`01` a `08`), divisão de conta
(`09` a `11`) e finalizar sem cobrar (`12` e `13`).
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


def annotate(nome, marcadores=(), molduras=(), r=None, w=None, m=0.0, md=0.0):
    """`marcadores`: (número, alvo_x, alvo_y, etiqueta_x, etiqueta_y) — tudo em **fração**.

    Fração e não pixel porque estes prints vêm recortados e reamostrados: pixel medido numa
    versão morre na primeira vez que o recorte mudar.

    `m` e `md` montam a margem **em memória**, sem gravar na pura. As dezenove imagens do
    aplicativo usam o `margem()`, que grava — e ali isso é inofensivo, porque o `copiar()`
    reconstrói a pura do material versionado a cada execução. A imagem `20` é diferente: ela é
    **capturada** pelo `capturar-parametro.py` e não se reconstrói, então margem gravada nela se
    acumularia a cada execução e deslocaria as setas. Foi o defeito encontrado no #125.
    """
    pura = Image.open(os.path.join(SRC, nome)).convert("RGB")
    if m or md:
        Wp, Hp = pura.size
        largura = round(Wp / (1 - m - md))
        tela = Image.new("RGB", (largura, Hp), FUNDO)
        tela.paste(pura, (round(largura * m), 0))
        pura = tela
    img = pura.convert("RGBA")
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


CO = "11-cobranca-na-porta/prints"
DV = "12-divisao-de-conta/prints"
SC = "13-finalizar-sem-cobrar/prints"

# ---------------------------------------------------------------------------------------
# 01 — o rodapé: onde a cobrança começa
# ---------------------------------------------------------------------------------------
# Três colunas em pé de igualdade e nenhuma delas com lado livre: a do meio (TROCO) é alcançada
# por cima, a da direita (COBRAR) pela direita, e o resto pela esquerda.
C1, M1, TM1, MD1 = (0, 0.715, 1, 0.978), 0.26, 0.26, 0.14
copiar(f"{CO}/01-rodape-de-cobranca.png", "01-rodape-de-cobranca.png", caixa=C1, largura=900)
margem("01-rodape-de-cobranca.png", m=M1, tm=TM1, md=MD1)
a = rec(C1, m=M1, tm=TM1, md=MD1)
annotate("01-rodape-de-cobranca.png", [
    (1, *a(22, 786), ETQ, a(0, 786)[1]),         # a forma prevista — o que o cliente disse ao pedir
    (2, *a(22, 848), ETQ, a(0, 848)[1]),         # TOTAL, o valor do pedido
    (3, *a(185, 820), a(185, 0)[0], 0.09),       # TROCO, alcançado por cima: coluna do meio
    (4, *a(390, 848), 0.94, a(0, 848)[1]),       # COBRAR, em verde — o que você recebe
    (5, *a(24, 896), ETQ, a(0, 896)[1]),         # INICIAR COBRANÇA
    (6, *a(24, 960), ETQ, a(0, 960)[1]),         # FINALIZAR SEM COBRAR
], r=26, w=4)

# ---------------------------------------------------------------------------------------
# 02 — a conferência do item em destaque
# ---------------------------------------------------------------------------------------
C2 = (0, 0.630, 1, 0.950)
copiar(f"{CO}/02-conferir-destaque.png", "02-conferir-destaque.png", caixa=C2, largura=820)
margem("02-conferir-destaque.png")
a = rec(C2)
annotate("02-conferir-destaque.png", [
    (1, *a(35, 690), ETQ, a(0, 690)[1]),         # a pergunta, em letras maiúsculas
    (2, *a(40, 763), ETQ, a(0, 763)[1]),         # o item que precisa ser conferido
    (3, *a(30, 840), ETQ, a(0, 840)[1]),         # CONFIRMAR
], r=26, w=4)

# ---------------------------------------------------------------------------------------
# 03 — a tela de pagamento inteira
# ---------------------------------------------------------------------------------------
# A única tela capturada por inteiro: é o mapa da operação, e o vazio no meio dela é real —
# a tela é assim quando há uma pessoa só pagando.
C3, M3, MD3 = (0, 0.112, 1, 0.985), 0.26, 0.14
copiar(f"{CO}/03-tela-de-pagamento.png", "03-tela-de-pagamento.png", caixa=C3, largura=700)
margem("03-tela-de-pagamento.png", m=M3, md=MD3)
a = rec(C3, m=M3, md=MD3)
annotate("03-tela-de-pagamento.png", [
    # O selo PEDIDO #NNNN é o marcador 1 porque é a única tela do app que mostra o número do
    # pedido — medido nos prints das duas rodadas. Alcançado pela direita: ele mora encostado
    # na borda, e vir pela esquerda cruzaria o nome do cliente.
    (1, *a(440, 145), 0.94, a(0, 145)[1]),       # PEDIDO #1030 — o número, só aqui
    (2, *a(35, 207), ETQ, a(0, 207)[1]),         # A RECEBER — o valor grande
    (3, *a(305, 268), 0.94, a(0, 268)[1]),       # JÁ PAGO, alcançado pela direita
    (4, *a(452, 324), 0.94, a(0, 330)[1]),       # o + do DIVIDIR CONTA
    (5, *a(45, 419), ETQ, a(0, 419)[1]),         # o valor da Pessoa 1
    (6, *a(430, 419), 0.94, a(0, 419)[1]),       # o lápis que edita o valor
    (7, *a(35, 477), ETQ, a(0, 477)[1]),         # Troco para, e o troco calculado
    (8, *a(35, 537), ETQ, a(0, 545)[1]),         # o campo de observação
    (9, *a(24, 952), ETQ, a(0, 952)[1]),         # CONFIRMAR PAGAMENTO
], r=26, w=4)

# ---------------------------------------------------------------------------------------
# 04 a 06 — escolher a forma, a bandeira e o troco
# ---------------------------------------------------------------------------------------
C4, M4, MD4 = (0, 0.340, 1, 0.985), 0.24, 0.14
copiar(f"{CO}/04-forma-de-pagamento.png", "04-forma-de-pagamento.png", caixa=C4, largura=760)
margem("04-forma-de-pagamento.png", m=M4, md=MD4)
a = rec(C4, m=M4, md=MD4)
annotate("04-forma-de-pagamento.png", [
    (1, *a(40, 518), ETQ, a(0, 518)[1]),         # Dinheiro — a forma prevista já vem marcada
    (2, *a(440, 518), 0.94, a(0, 518)[1]),       # o tique vermelho, alcançado pela direita
    (3, *a(95, 607), ETQ, a(0, 607)[1]),         # Com bandeira, na linha do Débito
    (4, *a(30, 943), ETQ, a(0, 943)[1]),         # CANCELAR
], r=26, w=4)

C5 = (0, 0.550, 1, 0.985)
copiar(f"{CO}/05-bandeira-do-cartao.png", "05-bandeira-do-cartao.png", caixa=C5, largura=760)
margem("05-bandeira-do-cartao.png")
a = rec(C5)
annotate("05-bandeira-do-cartao.png", [
    (1, *a(70, 671), ETQ, a(0, 671)[1]),         # Opcional — a taxa resolve pela forma
    (2, *a(40, 725), ETQ, a(0, 725)[1]),         # as bandeiras cadastradas
    (3, *a(30, 871), ETQ, a(0, 871)[1]),         # CONTINUAR SEM BANDEIRA
], r=26, w=4)

C6 = (0, 0.310, 1, 0.650)
copiar(f"{CO}/06-troco-para-quanto.png", "06-troco-para-quanto.png", caixa=C6, largura=820)
margem("06-troco-para-quanto.png")
a = rec(C6)
annotate("06-troco-para-quanto.png", [
    (1, *a(40, 454), ETQ, a(0, 454)[1]),         # o valor que o cliente pediz de troco, já preenchido
    (2, *a(30, 531), ETQ, a(0, 531)[1]),         # CONFIRMAR
    (3, *a(30, 603), ETQ, a(0, 603)[1]),         # SEM TROCO
], r=26, w=4)

# ---------------------------------------------------------------------------------------
# 07 e 08 — a última folha e o resultado
# ---------------------------------------------------------------------------------------
C7 = (0, 0.600, 1, 0.950)
copiar(f"{CO}/07-confirmar-cobranca.png", "07-confirmar-cobranca.png", caixa=C7, largura=820)
margem("07-confirmar-cobranca.png")
a = rec(C7)
annotate("07-confirmar-cobranca.png", [
    (1, *a(40, 683), ETQ, a(0, 683)[1]),         # a frase com o valor que vai ser registrado
    (2, *a(40, 767), ETQ, a(0, 767)[1]),         # a linha da forma e do valor
    (3, *a(30, 840), ETQ, a(0, 840)[1]),         # CONFIRMAR — depois daqui está no caixa
], r=26, w=4)

# Marca verde e uma frase: etiqueta aqui só repetiria a legenda.
copiar(f"{CO}/08-pagamento-confirmado.png", "08-pagamento-confirmado.png",
       caixa=(0, 0.340, 1, 0.600), largura=760)
passthrough("08-pagamento-confirmado.png")

# ---------------------------------------------------------------------------------------
# 09 a 11 — dividir a conta
# ---------------------------------------------------------------------------------------
C9, M9, MD9 = (0, 0.105, 1, 0.900), 0.26, 0.14
copiar(f"{DV}/01-duas-pessoas.png", "09-duas-pessoas.png", caixa=C9, largura=700)
margem("09-duas-pessoas.png", m=M9, md=MD9)
a = rec(C9, m=M9, md=MD9)
annotate("09-duas-pessoas.png", [
    (1, *a(22, 324), ETQ, a(0, 324)[1]),         # DIVIDIR CONTA, agora com 2
    (2, *a(452, 324), 0.94, a(0, 330)[1]),       # o + que criou a segunda pessoa
    (3, *a(45, 419), ETQ, a(0, 419)[1]),         # o valor da Pessoa 1, dividido em partes iguais
    (4, *a(40, 506), ETQ, a(0, 506)[1]),         # Selecione a forma — campo que só existe dividindo
    (5, *a(35, 578), ETQ, a(0, 590)[1]),         # o bloco da Pessoa 2
], r=26, w=4)

C10 = (0, 0.340, 1, 0.786)
copiar(f"{DV}/03-duas-formas.png", "10-duas-formas.png", caixa=C10, largura=760)
margem("10-duas-formas.png")
a = rec(C10)
annotate("10-duas-formas.png", [
    (1, *a(45, 508), ETQ, a(0, 508)[1]),         # a forma da Pessoa 1
    (2, *a(45, 716), ETQ, a(0, 716)[1]),         # a forma da Pessoa 2
    (3, *a(35, 765), ETQ, a(0, 765)[1]),         # Troco para, que apareceu por causa do dinheiro
], r=26, w=4)

C11 = (0, 0.570, 1, 0.950)
copiar(f"{DV}/04-confirmar-duas-linhas.png", "11-confirmar-duas-linhas.png",
       caixa=C11, largura=820)
margem("11-confirmar-duas-linhas.png")
a = rec(C11)
annotate("11-confirmar-duas-linhas.png", [
    (1, *a(32, 659), ETQ, a(0, 659)[1]),         # o valor cheio, a soma das partes
    (2, *a(40, 735), ETQ, a(0, 750)[1]),         # uma linha numerada por pessoa
], r=26, w=4)

# ---------------------------------------------------------------------------------------
# 12 e 13 — finalizar sem cobrar
# ---------------------------------------------------------------------------------------
C12 = (0, 0.620, 1, 0.950)
copiar(f"{SC}/03-confirmar-finalizacao.png", "12-finalizar-sem-cobrar.png",
       caixa=C12, largura=820)
margem("12-finalizar-sem-cobrar.png")
a = rec(C12)
annotate("12-finalizar-sem-cobrar.png", [
    (1, *a(40, 725), ETQ, a(0, 725)[1]),         # o valor em aberto, escrito no texto
    (2, *a(30, 840), ETQ, a(0, 840)[1]),         # CONTINUAR
    (3, *a(30, 911), ETQ, a(0, 911)[1]),         # CANCELAR — a saída, se foi toque errado
], r=26, w=4)

C13, M13, MD13 = (0, 0.048, 1, 0.580), 0.26, 0.14
copiar(f"{SC}/05-observacao-preenchida.png", "13-observacao-preenchida.png",
       caixa=C13, largura=760)
margem("13-observacao-preenchida.png", m=M13, md=MD13)
a = rec(C13, m=M13, md=MD13)
annotate("13-observacao-preenchida.png", [
    (1, *a(65, 237), ETQ, a(0, 237)[1]),         # Finalizar Entrega, com o saldo em aberto
    (2, *a(30, 381), ETQ, a(0, 381)[1]),         # a observação escrita
    (3, *a(455, 436), 0.94, a(0, 436)[1]),       # o contador de caracteres
    (4, *a(30, 490), ETQ, a(0, 490)[1]),         # FINALIZAR
], r=26, w=4)

# ---------------------------------------------------------------------------------------
# 14 a 19 — as seis telas de quando a cobrança não fecha
# ---------------------------------------------------------------------------------------
# Vieram da segunda rodada de capturas (`capturas-2/22-erros-de-cobranca/` e `_triagem/`). Quatro
# perguntas do FAQ deste manual são as mais usadas pelo suporte e nenhuma tinha foto; a última
# delas — pagamento registrado sem baixa — é uma **sequência de três telas**, e é o laço em que o
# suporte cai. Por isso ela ganhou três imagens em vez de uma: quem está no laço precisa
# reconhecer em qual das três telas está para saber o que fazer.
#
# As três telas de resultado (`15`, `16` e `17`) entram **inteiras**, com o vão do meio que é
# real. Recortar só o título e colar os botões embaixo deixaria a imagem mais compacta e mentiria
# sobre a tela: ela é uma marca, uma frase e um botão no pé, com muito espaço vazio entre eles —
# e é justamente esse vazio que faz o entregador procurar um botão que não existe.
EC = "capturas-2/22-erros-de-cobranca/prints"
TR = "capturas-2/_triagem/prints"
ETQ_DIR = 0.94

# 14 — a divisão que não soma. O recorte junta o valor a receber, as duas partes e o aviso
# vermelho, porque a conta que o leitor precisa fazer é 5 + 9,95 contra 19,90.
C14, M14 = (0, 0.107, 1, 0.820), 0.26
copiar(f"{EC}/01-soma-precisa-fechar.png", "14-soma-nao-fecha.png", caixa=C14, largura=620)
margem("14-soma-nao-fecha.png", m=M14)
a = rec(C14, m=M14)
annotate("14-soma-nao-fecha.png", [
    (1, *a(70, 183), ETQ, a(0, 183)[1]),         # A RECEBER: o valor que as partes têm de somar
    (2, *a(88, 405), ETQ, a(0, 405)[1]),         # a parte da Pessoa 1
    (3, *a(88, 645), ETQ, a(0, 645)[1]),         # a parte da Pessoa 2
    (4, *a(137, 790), ETQ, a(0, 790)[1]),        # A soma precisa ser R$ 19,90
], r=26, w=4)

# 15 — o erro do servidor. Título, explicação e os dois botões: o de repetir e o de desistir.
C15, M15 = (0, 0.045, 1, 0.978), 0.26
copiar(f"{EC}/02-nao-foi-possivel-cobrar.png", "15-erro-no-pagamento.png",
       caixa=C15, largura=560)
margem("15-erro-no-pagamento.png", m=M15)
a = rec(C15, m=M15)
annotate("15-erro-no-pagamento.png", [
    (1, *a(110, 491), ETQ, a(0, 491)[1]),        # Erro no Pagamento
    (2, *a(76, 532), ETQ, a(0, 560)[1]),         # O servidor não confirmou o pagamento
    (3, *a(22, 878), ETQ, a(0, 878)[1]),         # TENTAR NOVAMENTE
    (4, *a(22, 952), ETQ, a(0, 952)[1]),         # VOLTAR PARA ENTREGAS
], r=26, w=4)

# 16 — pedido já pago. Marca **verde**, e é o detalhe que decide a leitura: não é erro.
C16, M16 = (0, 0.045, 1, 0.978), 0.26
copiar(f"{EC}/03-pedido-ja-pago.png", "16-pedido-ja-pago.png", caixa=C16, largura=560)
margem("16-pedido-ja-pago.png", m=M16)
a = rec(C16, m=M16)
annotate("16-pedido-ja-pago.png", [
    (1, *a(139, 515), ETQ, a(0, 515)[1]),        # Pedido já pago
    (2, *a(56, 555), ETQ, a(0, 582)[1]),         # Não há saldo a receber. Finalize a entrega…
    (3, *a(22, 951), ETQ, a(0, 951)[1]),         # FECHAR
], r=26, w=4)

# 17 — a tela de sucesso do caso em que a baixa não saiu. Ela é **quase** igual à do `08`: mesma
# marca verde, mesmo título. A diferença mora na frase de baixo, e é só ela que diz que a entrega
# continua aberta — por isso ela é o marcador 2 e a legenda insiste nisso.
C17, M17 = (0, 0.045, 1, 0.978), 0.26
copiar(f"{EC}/04-falta-finalizar.png", "17-pagamento-sem-baixa.png", caixa=C17, largura=560)
margem("17-pagamento-sem-baixa.png", m=M17)
a = rec(C17, m=M17)
annotate("17-pagamento-sem-baixa.png", [
    (1, *a(75, 514), ETQ, a(0, 514)[1]),         # Pagamento Confirmado! — o mesmo título do 08
    (2, *a(83, 555), ETQ, a(0, 582)[1]),         # "Finalize a entrega — o dinheiro já está no caixa"
    (3, *a(22, 951), ETQ, a(0, 951)[1]),         # VOLTAR PARA ENTREGAS
], r=26, w=4)

# 18 — de volta nos detalhes. O recorte guarda o rodapé de propósito: ele ainda mostra COBRAR com
# o valor cheio, porque a tela não recarregou, e é esse rodapé que faz o entregador cobrar duas
# vezes. O valor é alcançado pela direita — pela esquerda a seta atravessaria a coluna do TOTAL.
C18, M18, MD18 = (0, 0.410, 1, 0.962), 0.24, 0.13
copiar(f"{TR}/pos22.png", "18-pagamento-registrado.png", caixa=C18, largura=700)
margem("18-pagamento-registrado.png", m=M18, md=MD18)
a = rec(C18, m=M18, md=MD18)
annotate("18-pagamento-registrado.png", [
    (1, *a(58, 467), ETQ, a(0, 467)[1]),         # Pagamento registrado
    (2, *a(58, 501), ETQ, a(0, 512)[1]),         # Finalize a entrega.
    (3, *a(412, 579), ETQ_DIR, a(0, 579)[1]),    # OK
    (4, *a(306, 845), ETQ_DIR, a(0, 845)[1]),    # COBRAR R$ 19,90 — o rodapé que não recarregou
    (5, *a(22, 958), ETQ, a(0, 958)[1]),         # FINALIZAR SEM COBRAR, o caminho certo agora
], r=30, w=4)

# 19 — a baixa que não passa. O FINALIZAR atrás da janela entra porque a pergunta do leitor é
# "eu apertei o botão certo?" — e a resposta é sim: o botão está certo, a lista é que está velha.
C19, M19, MD19 = (0, 0.410, 1, 0.908), 0.24, 0.13
copiar(f"{TR}/pos22d.png", "19-nao-foi-possivel-dar-baixa.png", caixa=C19, largura=700)
margem("19-nao-foi-possivel-dar-baixa.png", m=M19, md=MD19)
a = rec(C19, m=M19, md=MD19)
annotate("19-nao-foi-possivel-dar-baixa.png", [
    (1, *a(58, 464), ETQ, a(0, 464)[1]),         # Não foi possível dar baixa
    (2, *a(58, 501), ETQ, a(0, 512)[1]),         # O servidor não confirmou a entrega
    (3, *a(412, 579), ETQ_DIR, a(0, 579)[1]),    # OK
    (4, *a(22, 840), ETQ, a(0, 840)[1]),         # FINALIZAR, atrás da janela
], r=30, w=4)

# ---------------------------------------------------------------------------------------
# 20 — o parâmetro que liga e desliga a tela de pagamento
# ---------------------------------------------------------------------------------------
# A única imagem deste manual que não vem do celular: é o card **Delivery** de Configuração →
# Parâmetros, capturado no navegador pelo `capturar-parametro.py`. Ela abre o manual, porque a
# primeira pergunta de quem chega aqui virou "meu entregador tem essa tela?".
#
# Duas diferenças de tratamento em relação às dezenove de cima:
#
# * **Não passa pelo `margem()`.** Aquele ajudante grava a margem dentro da pura, o que só é
#   inofensivo quando o `copiar()` reconstrói a pura do material a cada execução. Esta pura é
#   capturada e não se reconstrói: margem gravada nela se somaria a cada rodada e deslocaria as
#   setas — o defeito encontrado no #125. Aqui a margem é montada em memória, pelo `annotate()`.
# * **A medição é em pixel do próprio print**, e não na grade de 473x1024: este print não é uma
#   tela de celular, é um recorte de um card do navegador, e não existe prévia comum para
#   converter.
#
# O card cabe inteiro, os dois interruptores juntos, e é de propósito: os nomes são parecidos, o
# de cima já tem manual próprio (#43) e a confusão entre os dois é o erro previsível.
P20 = "20-parametro-entregador-registra-pagamento.png"
M20, MD20 = 0.13, 0.08
_p20 = Image.open(os.path.join(SRC, P20)).size
_W20 = _p20[0] / (1 - M20 - MD20)


def p20(x, y):
    """Pixel do print do card em fração da imagem final, já com as duas margens."""
    return (M20 + x / _W20, y / _p20[1])


annotate(P20, [
    (1, *p20(52, 87), 0.0635, 87 / _p20[1]),      # o card Delivery — onde o parâmetro mora
    (2, *p20(50, 171), 0.0635, 171 / _p20[1]),    # Pagamento Automático Delivery: o vizinho
    (3, *p20(50, 263), 0.0635, 263 / _p20[1]),    # Entregador registra pagamento: este é o novo
    (4, *p20(1146, 290), 0.955, 290 / _p20[1]),   # o interruptor, desligado neste print
], r=26, w=3, m=M20, md=MD20)
