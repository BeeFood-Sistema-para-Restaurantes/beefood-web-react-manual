"""Anota as capturas do #112 — App do entregador: as entregas do dia e o histórico.

Mesma técnica do #111: os prints vêm do material do dono (emulador `Pixel_7_Pro`), `copiar()`
recorta por fração e `rec()` converte pixel da prévia de 473x1024 — a proporção exata de
1440x3120 — em fração da imagem final, já com as margens.

Duas imagens nascem de recorte **dentro** de um print maior, e é de propósito:

* `02-cartao.png` é um cartão só, tirado da lista de quatro. O cartão tem seis informações em
  três linhas apertadas; na lista inteira, seis etiquetas viravam um emaranhado. Sozinho, com
  margem à esquerda **e** em cima, cada uma tem espaço.
* `05-rodape.png` é a faixa escura dos detalhes. Ela é a parte que o entregador olha na porta do
  cliente, e some no meio de uma tela que tem mais dois cartões acima.

Nenhuma outra tela do app precisa disso: as demais têm uma informação por linha.
"""

import math
import os
import shutil
import sys

from PIL import Image, ImageDraw, ImageFont

# Os prints do app não são capturados aqui: vêm do material que o dono enviou, feito no
# emulador Android. `copiar()` traz cada um para `imagens-puras/`, que continua sendo o
# backup do manual, e só `imagens-tratadas/` é referenciada pelo `.md`.
MATERIAL = "../gestao-entregas/material-recebido/app-entregador"
SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(SRC, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

# Os prints da segunda rodada foram tirados dois dias depois dos da primeira, e a lista mostra a
# data em letras vermelhas. `relogio` transplanta a linha de data de um print da primeira rodada
# para dentro deles, com os glifos do próprio aplicativo — a seção 1 e a seção 4 deste manual
# passam a ser o mesmo dia. Só a linha da data muda; o resto da tela é o que o emulador mostrou.
sys.path.insert(0, "../gestao-entregas/scripts")
import relogio  # noqa: E402

# A data de referência é a do print que abre o manual: `17/09/2026 23:44`, a previsão dos quatro
# pedidos da seção 1.
DATA = relogio.tinta(f"{MATERIAL}/03-lista-de-entregas/prints/01-lista-quatro-entregas.png")

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


def copiar(origem, nome, caixa=None, largura=None, data=False):
    """Traz um print do material para `imagens-puras/`.

    `caixa` é em **fração** (esq, topo, dir, base) da imagem original: o print do celular tem
    1440x3120 e quase sempre sobra faixa preta em cima e embaixo, que só encolhe o que
    interessa. `largura` reamostra para um tamanho fixo, para as imagens do manual ficarem do
    mesmo tamanho na página.

    `data=True` passa o print pelo `relogio`, que troca a linha de *Previsão Entrega* pela do
    print de referência. Vale para os prints da segunda rodada, tirados dois dias depois.
    """
    caminho = os.path.join(MATERIAL, origem)
    img = Image.open(caminho).convert("RGB")
    if data:
        print("RELOGIO", nome, relogio.ajustar(img, DATA), "linha(s) de data")
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
# 01 a 03 — a lista de entregas
# ---------------------------------------------------------------------------------------
C1 = (0, 0.105, 1, 0.845)
copiar("03-lista-de-entregas/prints/01-lista-quatro-entregas.png",
       "01-lista.png", caixa=C1, largura=760)
passthrough("01-lista.png")

# Um cartão só. Seis informações em três linhas: com margem à esquerda **e** em cima, três
# etiquetas apontam para baixo e duas entram pela lateral, sem uma cobrir a outra.
C2, M2, TM2 = (0, 0.115, 1, 0.305), 0.22, 0.28
copiar("03-lista-de-entregas/prints/01-lista-quatro-entregas.png",
       "02-cartao.png", caixa=C2, largura=900)
margem("02-cartao.png", m=M2, tm=TM2)
a = rec(C2, m=M2, tm=TM2)
annotate("02-cartao.png", [
    (1, *a(60, 148), a(60, 0)[0], 0.09),         # a etiqueta #1026
    (2, *a(137, 160), a(137, 0)[0], 0.09),       # Previsão Entrega, com a hora
    (3, *a(448, 220), a(448, 0)[0], 0.09),       # a flecha >
    (4, *a(18, 213), 0.07, a(0, 213)[1]),        # o círculo da parada
    (5, *a(48, 291), 0.07, a(0, 291)[1]),        # Cobrar R$
], r=34, w=5)

C3 = (0, 0.70, 1, 0.905)
copiar("03-lista-de-entregas/prints/02-fim-da-lista.png",
       "03-fim-da-lista.png", caixa=C3, largura=760)
margem("03-fim-da-lista.png")
a = rec(C3)
annotate("03-fim-da-lista.png", [
    (1, *a(140, 781), ETQ, a(0, 781)[1]),        # ATUALIZAR
    (2, *a(24, 899), ETQ, a(0, 899)[1]),         # MELHOR ROTA GOOGLE MAPS (4)
], r=26, w=4)

# ---------------------------------------------------------------------------------------
# 04 a 07 — os detalhes da entrega
# ---------------------------------------------------------------------------------------
C4 = (0, 0.055, 1, 0.70)
copiar("04-detalhes-da-entrega/prints/01-topo-dos-detalhes.png",
       "04-detalhes.png", caixa=C4, largura=760)
margem("04-detalhes.png")
a = rec(C4)
annotate("04-detalhes.png", [
    (1, *a(30, 190), ETQ, a(0, 190)[1]),         # o endereço
    (2, *a(36, 241), ETQ, a(0, 241)[1]),         # a tarja do complemento
    (3, *a(30, 299), ETQ, a(0, 299)[1]),         # Observações, em laranja
    (4, *a(36, 337), ETQ, 0.46),                 # VER NO MAPA
    (5, *a(30, 456), ETQ, a(0, 456)[1]),         # os itens do pedido
    (6, *a(42, 528), ETQ, a(0, 528)[1]),         # a linha preta do item em destaque
    (7, *a(30, 590), ETQ, a(0, 590)[1]),         # Estabelecimento e Destinatário
], r=30, w=4)

# A faixa escura, sozinha. É o que o entregador olha na porta do cliente, e na tela inteira ela
# fica no pé, depois de dois cartões.
C5 = (0, 0.725, 1, 0.99)
copiar("04-detalhes-da-entrega/prints/01-topo-dos-detalhes.png",
       "05-rodape.png", caixa=C5, largura=760)
margem("05-rodape.png")
a = rec(C5)
annotate("05-rodape.png", [
    (1, *a(22, 778), ETQ, a(0, 778)[1]),         # FORMA DE PAGAMENTO
    (2, *a(22, 830), ETQ, a(0, 830)[1]),         # TOTAL, TROCO e COBRAR
    (3, *a(36, 896), ETQ, a(0, 896)[1]),         # INICIAR COBRANÇA
    (4, *a(36, 961), ETQ, a(0, 961)[1]),         # FINALIZAR SEM COBRAR
], r=26, w=4)

C6 = (0, 0.61, 1, 0.96)
copiar("04-detalhes-da-entrega/prints/02-conferir-destaque.png",
       "06-conferir-destaque.png", caixa=C6, largura=760)
margem("06-conferir-destaque.png")
a = rec(C6)
annotate("06-conferir-destaque.png", [
    (1, *a(30, 690), ETQ, a(0, 690)[1]),         # o título da folha
    (2, *a(30, 763), ETQ, a(0, 763)[1]),         # o item marcado
    (3, *a(36, 840), ETQ, a(0, 840)[1]),         # CONFIRMAR
    (4, *a(36, 911), ETQ, a(0, 911)[1]),         # CANCELAR
], r=26, w=4)

C7 = (0, 0.055, 1, 0.99)
copiar("04-detalhes-da-entrega/prints/03-sem-complemento.png",
       "07-sem-complemento.png", caixa=C7, largura=700)
margem("07-sem-complemento.png")
a = rec(C7)
annotate("07-sem-complemento.png", [
    (1, *a(30, 200), ETQ, a(0, 200)[1]),         # o endereço, sem tarja nem observação
    (2, *a(36, 272), ETQ, a(0, 272)[1]),         # VER NO MAPA, que subiu
    (3, *a(22, 828), ETQ, a(0, 828)[1]),         # o rodapé sem a coluna TROCO
], r=30, w=4)

# ---------------------------------------------------------------------------------------
# 08 a 10 — o histórico
# ---------------------------------------------------------------------------------------
C8 = (0, 0.11, 1, 0.50)
copiar("14-historico/prints/01-historico-do-dia.png",
       "08-historico-dias.png", caixa=C8, largura=760)
margem("08-historico-dias.png")
a = rec(C8)
annotate("08-historico-dias.png", [
    (1, *a(100, 148), ETQ, a(0, 148)[1]),        # 4 Entregas
    (2, *a(110, 209), ETQ, a(0, 209)[1]),        # o período
    (3, *a(24, 278), ETQ, a(0, 278)[1]),         # o cartão do dia
    (4, *a(428, 367), ETQ, a(0, 367)[1]),        # a flecha > do dia
    (5, *a(140, 459), ETQ, a(0, 459)[1]),        # ATUALIZAR
], r=28, w=4)

C9, M9, MD9 = (0, 0.24, 1, 0.80), 0.22, 0.18
copiar("14-historico/prints/02-dia-expandido.png",
       "09-dia-expandido.png", caixa=C9, largura=760)
margem("09-dia-expandido.png", m=M9, md=MD9)
a = rec(C9, m=M9, md=MD9)
annotate("09-dia-expandido.png", [
    (1, *a(30, 279), 0.07, a(0, 279)[1]),        # a flecha de voltar
    (2, *a(70, 347), 0.07, a(0, 347)[1]),        # o pedido e a hora da entrega
    (3, *a(438, 545), 0.93, a(0, 545)[1]),       # o ! vermelho do atraso
    (4, *a(70, 662), 0.07, a(0, 662)[1]),        # a etiqueta do marketplace
], r=28, w=4)

C10 = (0, 0.055, 1, 0.94)
copiar("14-historico/prints/03-detalhe-no-historico.png",
       "10-detalhe-no-historico.png", caixa=C10, largura=700)
margem("10-detalhe-no-historico.png")
a = rec(C10)
annotate("10-detalhe-no-historico.png", [
    (1, *a(30, 297), ETQ, a(0, 297)[1]),         # Observações, com a Obs. Entrega
    (2, *a(80, 700), ETQ, a(0, 700)[1]),         # VALOR TOTAL DO PEDIDO
    (3, *a(40, 830), ETQ, a(0, 830)[1]),         # a linha do tempo
], r=30, w=4)

# ---------------------------------------------------------------------------------------
# 11 a 15 — a lista que muda sem o entregador mexer
# ---------------------------------------------------------------------------------------
# Vieram da segunda rodada (`capturas-2/16-notificacoes/`, `17-troca-de-entregador/`,
# `19-sem-internet/`, `21-listas-vazias/` e uma da `_triagem/`). Todas respondem a mesma família de
# pergunta: **a lista mudou e eu não fiz nada** — chegou entrega, saiu entrega, ou ela parou de
# mudar porque o sinal caiu.
#
# Duas regras novas de recorte nasceram aqui:
#
# * **As duas de notificação (`11` e `13`) são as únicas do bloco que guardam a barra do sistema.**
#   Nelas a barra não mostra relógio: mostra o ícone e o nome **BeeFood Entregador**, que é o que
#   diz de quem é o aviso. Cortar a barra tiraria justamente o que a imagem prova. Nas outras
#   quatro o recorte começa abaixo dela, porque o relógio do emulador estava em UTC.
# * **O par antes/depois (`14`) tem um marcador em cada metade, na mesma altura.** O cartão que saiu
#   ocupava exatamente o lugar que o seguinte passou a ocupar; marcar as duas metades no mesmo ponto
#   é o que mostra a substituição sem precisar de legenda comparativa.
NT = "capturas-2/16-notificacoes/prints"
TC = "capturas-2/17-troca-de-entregador/prints"
SI = "capturas-2/19-sem-internet/prints"
TR = "capturas-2/_triagem/prints"
ETQ_DIR = 0.94

# 11 — o aviso chegando por cima da lista.
C11, M11 = (0, 0.0, 1, 0.274), 0.26
copiar(f"{NT}/01-aviso-chegando.png", "11-aviso-chegando.png", caixa=C11, largura=700,
       data=True)
margem("11-aviso-chegando.png", m=M11)
a = rec(C11, m=M11)
annotate("11-aviso-chegando.png", [
    (1, *a(48, 22), ETQ, a(0, 22)[1]),           # BeeFood Entregador, na barra do sistema
    (2, *a(82, 90), ETQ, a(0, 80)[1]),           # Novo pedido para você · agora
    (3, *a(82, 115), ETQ, a(0, 128)[1]),         # Toque para ver a entrega
    (4, *a(20, 196), ETQ, a(0, 210)[1]),         # o primeiro cartão, visível por baixo
], r=24, w=4)

# 12 — depois do toque: aba Entregas em foco, a entrega nova no fim e o contador do botão azul
# um número acima.
C12, M12 = (0, 0.045, 1, 0.981), 0.26
copiar(f"{NT}/02-lista-depois-do-toque.png", "12-lista-depois-do-toque.png",
       caixa=C12, largura=620, data=True)
margem("12-lista-depois-do-toque.png", m=M12)
a = rec(C12, m=M12)
annotate("12-lista-depois-do-toque.png", [
    (1, *a(24, 566), ETQ, a(0, 566)[1]),         # o terceiro cartão: o que acabou de chegar
    (2, *a(18, 892), ETQ, a(0, 892)[1]),         # MELHOR ROTA GOOGLE MAPS (3)
    (3, *a(30, 985), ETQ, a(0, 985)[1]),         # a aba Entregas, em vermelho
], r=26, w=4)

# 13 — o outro aviso, o que ninguém quer receber.
C13, M13 = (0, 0.0, 1, 0.274), 0.26
copiar(f"{TC}/01-aviso-de-remocao.png", "13-aviso-de-remocao.png", caixa=C13, largura=700,
       data=True)
margem("13-aviso-de-remocao.png", m=M13)
a = rec(C13, m=M13)
annotate("13-aviso-de-remocao.png", [
    (1, *a(82, 90), ETQ, a(0, 80)[1]),           # Um pedido saiu da sua lista · agora
    (2, *a(82, 115), ETQ, a(0, 128)[1]),         # Toque para conferir suas entregas
], r=24, w=4)

# 14 — o par antes/depois. O recorte é curto de propósito: começa no fim do cartão 2 e vai até o
# botão azul, que é a faixa onde a diferença está. Tela inteira duas vezes lado a lado ficaria
# ilegível, e a metade de cima é idêntica nas duas.
C14, TM14 = (0, 0.430, 1, 0.930), 0.20
copiar(f"{TR}/lista-antes.png", "14a-antes.png", caixa=C14, largura=520, data=True)
copiar(f"{TC}/02-lista-sem-o-pedido.png", "14b-depois.png", caixa=C14, largura=520, data=True)
lado_a_lado(["14a-antes.png", "14b-depois.png"], "14-antes-e-depois.png")
com_margem("14-antes-e-depois.png", topo=TM14 / (1 - TM14))
# Coordenada escrita à mão: `rec()` fala de um print só, e aqui são dois colados. A metade
# esquerda ocupa 0..0,489 e a direita 0,511..1; o alvo é o mesmo ponto nas duas — o círculo
# numerado do terceiro cartão —, alcançado por uma seta vertical que desce pela calha vazia à
# esquerda dos endereços.
annotate("14-antes-e-depois.png", [
    (1, 0.028, 0.372, 0.028, 0.10),              # antes: o cartão 3 era a Rua Aparecida
    (2, 0.539, 0.372, 0.539, 0.10),              # depois: o mesmo lugar, com o endereço seguinte
], r=24, w=4)
