"""Anota as 13 capturas do #117 — Uma entrega do começo ao fim.

Este é o único manual do bloco com **imagens de duas origens**, e por isso o único com dois
jogos de ajudantes no mesmo arquivo:

* **As sete do painel** saem em 2160x1350 e têm, ao lado, um `*.geo.json` com o
  `getBoundingClientRect()` de cada alvo no instante do print. `alvo()` lê esse arquivo, então
  a seta aponta para o elemento medido e não para onde alguém achou que ele estava. Quem gerou
  os JSON: `/tmp/ge/cap117.py` e `/tmp/ge/cap117rel.py`.
* **As seis do celular** vêm do material que o dono mandou (emulador Android, 1440x3120).
  Não há DOM para medir: as posições foram lidas numa prévia de 473x1024 — mesma proporção —
  com a grade do `/tmp/ge/grade.py` por cima, e `rec()` converte pixel dessa prévia em fração
  da imagem final, já com as margens. É a mesma técnica dos seis manuais do aplicativo.

A margem clara existe porque tela de celular é estreita e cheia: etiqueta dentro cobre texto.
Nas capturas do painel ela não é necessária — sobra mapa à esquerda da lateral, e é lá que os
números moram.

**As puras do painel não são reescritas por este arquivo.** Elas são a única cópia da captura,
e a janela que as produziu não dá para repetir: os três pedidos voltaram ao estado original
depois do ensaio. Só as do celular passam por `copiar()` + `margem()`, e essas duas sempre
recomeçam do material.
"""

import json
import math
import os

from PIL import Image, ImageDraw, ImageFont

MATERIAL = "../gestao-entregas/material-recebido/app-entregador"
CICLO = "capturas-2/18-ciclo-completo/prints"
SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(SRC, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
FUNDO = (233, 237, 239)
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


def desenhar(nome, marcadores, molduras, r, w):
    """Miolo comum: recebe marcador e moldura já em **pixel** da imagem final."""
    img = Image.open(os.path.join(SRC, nome)).convert("RGBA")
    W, H = img.size
    over = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    fnt = font(int(r * 1.25))
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


# ===========================================================================================
# As sete do painel — coordenada em pixel, lida do `*.geo.json`
# ===========================================================================================
_geo = {}


def carregar(nome):
    global _geo
    caminho = os.path.join(SRC, nome.rsplit(".", 1)[0] + ".geo.json")
    _geo = json.load(open(caminho, encoding="utf-8")) if os.path.exists(caminho) else {}
    if not _geo:
        raise RuntimeError(f"sem geometria para {nome}")


def alvo(rotulo, borda=None, recuo=0):
    """Ponto da seta. `borda` evita que a ponta caia sobre o texto do elemento.

    `recuo` empurra a ponta para **fora** do elemento. Serve para rótulo que começa na própria
    borda, como o nome do entregador no cabeçalho da rota: a ponta na borda cai sobre a
    primeira letra, e a farpa da seta cobre a segunda.
    """
    p = _geo[rotulo]
    if borda == "esq":
        return p["x"] + 4 - recuo, p["cy"]
    if borda == "dir":
        return p["x"] + p["w"] - 4 + recuo, p["cy"]
    if borda == "cima":
        return p["cx"], p["y"] + 4
    if borda == "baixo":
        return p["cx"], p["y"] + p["h"] - 4
    if borda == "topo-esq":
        return p["x"] + 30, p["y"] + 14
    return p["cx"], p["cy"]


def moldura(rotulo, folga=6):
    p = _geo[rotulo]
    return (p["x"] - folga, p["y"] - folga,
            p["x"] + p["w"] + folga, p["y"] + p["h"] + folga)


def anotar_painel(nome, marcadores=(), molduras=(), r=27, w=5):
    desenhar(nome, marcadores, molduras, r, w)


# ===========================================================================================
# As seis do celular — coordenada em fração, medida na prévia de 473x1024
# ===========================================================================================
W0, H0 = 473, 1024
ETQ = 0.10      # x da etiqueta, dentro da margem esquerda
ETQ_DIR = 0.94  # x da etiqueta, dentro da margem direita


def copiar(origem, nome, caixa=None, largura=None):
    """Traz um print do material para `imagens-puras/`, recortado por fração."""
    img = Image.open(os.path.join(MATERIAL, origem)).convert("RGB")
    if caixa:
        W, H = img.size
        img = img.crop((int(caixa[0] * W), int(caixa[1] * H),
                        int(caixa[2] * W), int(caixa[3] * H)))
    if largura and img.size[0] != largura:
        alt = round(img.size[1] * largura / img.size[0])
        img = img.resize((largura, alt), Image.LANCZOS)
    img.save(os.path.join(SRC, nome))
    print("PURA", nome, img.size)


def margem(nome, m=0.26, md=0.0, tm=0.0):
    """Acrescenta margem clara à pura. `m`, `md` e `tm` são frações **do resultado**."""
    img = Image.open(os.path.join(SRC, nome)).convert("RGB")
    W, H = img.size
    dentro = 1 - m - md
    dx, dd = int(W * (m / dentro)) if m else 0, int(W * (md / dentro)) if md else 0
    dy = int(H * (tm / (1 - tm))) if tm else 0
    tela = Image.new("RGB", (W + dx + dd, H + dy), FUNDO)
    tela.paste(img, (dx, dy))
    tela.save(os.path.join(SRC, nome))
    print("MARGEM", nome, tela.size)


def rec(caixa, m=0.26, md=0.0, tm=0.0):
    """Converte pixel da prévia 473x1024 em fração da imagem final já recortada."""
    x0, x1 = caixa[0] * W0, caixa[2] * W0
    y0, y1 = caixa[1] * H0, caixa[3] * H0

    def f(x, y):
        return (m + (1 - m - md) * (x - x0) / (x1 - x0),
                tm + (1 - tm) * (y - y0) / (y1 - y0))
    return f


def anotar_app(nome, marcadores=(), molduras=(), r=26, w=4):
    """`marcadores` e `molduras` em **fração**; converte para pixel e desenha."""
    W, H = Image.open(os.path.join(SRC, nome)).size
    px = [(n, tx * W, ty * H, bx * W, by * H) for (n, tx, ty, bx, by) in marcadores]
    mol = [(a * W, b * H, c * W, e * H) for (a, b, c, e) in molduras]
    desenhar(nome, px, mol, r, w)


# ===========================================================================================
# 1. Os pedidos prontos, e o celular vazio
# ===========================================================================================
# As etiquetas moram no mapa: é o único vão livre da tela, e a lateral direita é densa demais
# para receber número em cima de texto. Os dois selos do topo são alcançados por baixo.
carregar("01-fila-de-pedidos.png")
anotar_painel("01-fila-de-pedidos.png",
              marcadores=[
                  (1, *alvo("chip_prontos", "baixo"), 472, 250),
                  (2, *alvo("chip_entregues", "baixo"), 796, 250),
                  (3, *alvo("grupo_sem_rota", "topo-esq"), 1420, 255),
                  (4, *alvo("pedido1105", "esq"), 1420, 567),
                  (5, *alvo("pin_entregador"), 700, 880),
              ],
              molduras=[moldura("chip_prontos"), moldura("chip_entregues"),
                        moldura("pedido1105")])

# ===========================================================================================
# 2. A rota montada, e a rota que chega
# ===========================================================================================
# O cabeçalho da rota tem seis alvos num vão de 72 px. Os dois da direita — o contador e o
# avião — são alcançados por cima, onde só há o campo de busca vazio; os outros pela esquerda.
carregar("02-rota-montada.png")
anotar_painel("02-rota-montada.png",
              marcadores=[
                  (1, *alvo("nome_entregador", "esq", recuo=16), 1330, 190),
                  (2, *alvo("letra_rota", "esq"), 1400, 290),
                  (3, *alvo("contagem", "cima"), 1948, 168),
                  (4, *alvo("aviao", "cima"), 2052, 168),
                  (5, *alvo("parada1", "esq"), 1400, 400),
                  (6, *alvo("parada3", "esq"), 1400, 563),
              ],
              molduras=[moldura("cabecalho_rota"), moldura("aviao")])

# A mesma rota, do lado do celular. Cinco alvos, todos alcançados pela margem esquerda.
#
# Toda ponta de seta aqui mira a **borda esquerda** do alvo, não o centro. A tela do app é uma
# coluna de texto alinhado à esquerda: seta que entra pela margem e para no centro risca a
# palavra que devia marcar. Foi o que aconteceu na primeira rodada destas seis imagens.
C3 = (0, 0.048, 1, 0.800)
copiar(f"{CICLO}/01-rota-recebida.png", "03-rota-no-app.png", caixa=C3, largura=640)
margem("03-rota-no-app.png", m=0.30)
a = rec(C3, m=0.30)
anotar_app("03-rota-no-app.png", [
    (1, *a(18, 147), ETQ, a(0, 120)[1]),    # ROTA A, com a letra que o painel deu
    (2, *a(62, 170), ETQ, a(0, 182)[1]),    # 0 de 3 entregues
    (3, *a(18, 211), ETQ, a(0, 244)[1]),    # INICIAR ROTA, ainda por tocar
    (4, *a(48, 277), ETQ, a(0, 306)[1]),    # o crachá laranja — e o número que não vem nele
    (5, *a(46, 391), ETQ, a(0, 391)[1]),    # Cobrar R$ 19,90, o mesmo valor do painel
])

# ===========================================================================================
# 3. O despacho: um clique que avisa o mundo
# ===========================================================================================
# A janela de confirmação flutua sobre o painel escurecido: aqui há espaço de sobra, e as sete
# etiquetas ficam fora do quadro branco, sem cobrir nada.
carregar("04-confirmar-despacho.png")
anotar_painel("04-confirmar-despacho.png",
              marcadores=[
                  (1, *alvo("titulo", "esq"), 620, 420),
                  (2, *alvo("linha_entregador", "esq"), 620, 505),
                  (3, *alvo("lista", "topo-esq"), 620, 600),
                  (4, *alvo("selo_pronto", "dir"), 1570, 556),
                  (5, *alvo("aviso_clientes", "esq"), 620, 801),
                  (6, *alvo("confirmar", "cima"), 1570, 879),
                  (7, *alvo("cancelar", "baixo"), 1059, 975),
              ],
              molduras=[moldura("confirmar"), moldura("selo_pronto")])

# O cabeçalho da rota no celular, depois do despacho. Faixa fina: três alvos e nada mais.
#
# A etiqueta *em rota* é alcançada pela **direita**, e é a razão da margem daquele lado: ela
# vive no fim da linha *0 de 3 entregues · em rota*, e pela esquerda a seta atravessaria o
# contador inteiro para marcar a palavra que vem depois dele.
C5, M5, MD5 = (0, 0.048, 1, 0.245), 0.22, 0.16
copiar(f"{CICLO}/02-em-rota.png", "05-em-rota-no-app.png", caixa=C5, largura=760)
margem("05-em-rota-no-app.png", m=M5, md=MD5)
a = rec(C5, m=M5, md=MD5)
anotar_app("05-em-rota-no-app.png", [
    (1, *a(18, 147), ETQ, a(0, 118)[1]),        # a letra da rota, a mesma do painel
    (2, *a(292, 168), ETQ_DIR, a(0, 168)[1]),   # em rota — a etiqueta que o despacho acendeu
    (3, *a(18, 211), ETQ, a(0, 214)[1]),        # ABRIR NO MAPS, no lugar do INICIAR ROTA
])

# Os detalhes da primeira parada. A tela inteira, com o vão do meio que é real: pedido de um
# item só não enche a lista. A coluna COBRAR é alcançada pela direita porque é o único alvo
# encostado na borda — pela esquerda, a seta atravessaria a coluna do TOTAL.
C6, M6, MD6 = (0, 0.113, 1, 0.990), 0.26, 0.12
copiar(f"{CICLO}/03-primeira-parada.png", "06-primeira-parada.png", caixa=C6, largura=620)
margem("06-primeira-parada.png", m=M6, md=MD6)
a = rec(C6, m=M6, md=MD6)
anotar_app("06-primeira-parada.png", [
    (1, *a(30, 182), ETQ, a(0, 150)[1]),        # o endereço, igual ao do cartão do painel
    (2, *a(30, 262), ETQ, a(0, 246)[1]),        # a observação que o cliente escreveu
    (3, *a(38, 364), ETQ, a(0, 342)[1]),        # Realizado às — a hora do pedido
    (4, *a(30, 399), ETQ, a(0, 424)[1]),        # o que ele está levando
    (5, *a(20, 785), ETQ, a(0, 785)[1]),        # Dinheiro, a forma combinada no pedido
    (6, *a(316, 848), ETQ_DIR, a(0, 848)[1]),   # COBRAR, em verde — o que ele recebe na porta
    (7, *a(22, 896), ETQ, a(0, 900)[1]),        # INICIAR COBRANÇA
])

# ===========================================================================================
# 4. A rua
# ===========================================================================================
carregar("07-mapa-ao-vivo.png")
anotar_painel("07-mapa-ao-vivo.png",
              marcadores=[
                  (1, *alvo("chip_em_rota", "baixo"), 629, 250),
                  (2, *alvo("chip_situacao", "esq"), 1400, 190),
                  (3, *alvo("parada1", "esq"), 1400, 380),
                  (4, *alvo("pin_entregador"), 1120, 700),
                  (5, *alvo("finalizar_rota", "cima"), 2052, 168),
              ],
              molduras=[moldura("chip_em_rota"), moldura("parada1")])

# ===========================================================================================
# 5. A porta do cliente
# ===========================================================================================
# Marca verde, uma frase e o valor: etiqueta aqui só repetiria a legenda.
copiar(f"{CICLO}/04-cobranca-concluida.png", "08-cobranca-concluida.png",
       caixa=(0, 0.352, 1, 0.600), largura=760)
passthrough("08-cobranca-concluida.png")

carregar("09-uma-de-tres.png")
# O contador é alcançado pela direita do próprio contador, e não pelo centro: no centro, a
# seta desceria em cima do nome do entregador, que termina onde o contador começa.
anotar_painel("09-uma-de-tres.png",
              marcadores=[
                  (1, *alvo("chip_entregues", "baixo"), 796, 250),
                  (2, *alvo("contagem", "dir"), 2010, 168),
                  (3, *alvo("parada1", "esq"), 1400, 365),
                  (4, *alvo("parada2", "esq"), 1400, 470),
                  (5, *alvo("pin_entregador"), 1150, 620),
              ],
              molduras=[moldura("chip_entregues"), moldura("parada2")])

# ===========================================================================================
# 6. O fim da viagem
# ===========================================================================================
# A pílula ONLINE entra na imagem de propósito, alcançada pela direita: lista vazia com o
# aplicativo online é a diferença entre "acabou o turno" e "caiu a conexão".
C10, M10, MD10 = (0, 0.048, 1, 0.610), 0.26, 0.12
copiar(f"{CICLO}/05-lista-sem-a-rota.png", "10-lista-sem-a-rota.png", caixa=C10, largura=700)
margem("10-lista-sem-a-rota.png", m=M10, md=MD10)
a = rec(C10, m=M10, md=MD10)
anotar_app("10-lista-sem-a-rota.png", [
    (1, *a(110, 421), ETQ, a(0, 421)[1]),       # Nenhuma entrega agora
    (2, *a(95, 500), ETQ, a(0, 500)[1]),        # arraste para atualizar
    (3, *a(130, 564), ETQ, a(0, 580)[1]),       # ATUALIZAR
    (4, *a(466, 82), ETQ_DIR, a(0, 82)[1]),     # ONLINE — ele continua conectado
])

carregar("11-rota-fora-da-tela.png")
anotar_painel("11-rota-fora-da-tela.png",
              marcadores=[
                  (1, *alvo("chip_entregues", "baixo"), 796, 250),
                  (2, *alvo("painel_vazio", "esq"), 1430, 288),
                  (3, *alvo("pin_entregador"), 700, 880),
              ],
              molduras=[moldura("chip_entregues")])

# ===========================================================================================
# 7. O que sobra do dia
# ===========================================================================================
# O cartão das métricas de tempo entra porque ele é o aviso que falta em toda leitura de
# relatório novo: com três pedidos, a média não é medida, e o número em branco não é defeito.
carregar("12-relatorio-do-dia.png")
anotar_painel("12-relatorio-do-dia.png",
              marcadores=[
                  (1, *alvo("periodo", "dir"), 700, 155),
                  (2, *alvo("aba_operacao", "esq"), 690, 347),
                  (3, *alvo("kpi_entregas", "esq"), 690, 492),
                  (4, *alvo("kpi_faturamento", "cima"), 1755, 350),
                  (5, *alvo("metrica_poucos", "esq"), 690, 1214),
              ],
              molduras=[moldura("kpi_entregas"), moldura("metrica_poucos")])

# O mesmo dia, no celular. As paradas aparecem da última para a primeira: é o ponto dos dois
# últimos marcadores, e a pergunta que o entregador faz ao abrir o Histórico.
C13, M13, MD13 = (0, 0.110, 1, 0.700), 0.26, 0.12
copiar(f"{CICLO}/06-historico-do-dia.png", "13-historico-do-dia.png", caixa=C13, largura=700)
margem("13-historico-do-dia.png", m=M13, md=MD13)
a = rec(C13, m=M13, md=MD13)
anotar_app("13-historico-do-dia.png", [
    (1, *a(98, 148), ETQ, a(0, 148)[1]),        # 6 Entregas — o período inteiro
    (2, *a(72, 263), ETQ, a(0, 245)[1]),        # Sábado 19/09/2026, o dia da janela
    (3, *a(70, 346), ETQ, a(0, 330)[1]),        # Entregue às 00:46
    (4, *a(22, 381), ETQ, a(0, 415)[1]),        # o 1 do histórico: a última parada da rota
    (5, *a(22, 651), ETQ, a(0, 651)[1]),        # o 3: a primeira parada da rota, por último
])
