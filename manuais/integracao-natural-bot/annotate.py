"""Anota as doze capturas do #134 — ativação da integração com a Natural Bot.

As coordenadas estão sempre em **pixel da captura pura**, inclusive nas recortadas e nas
costuradas: `preparar()` e `montagem()` convertem. Medir na pura inteira é o que deixa mexer no
recorte depois sem remedir nada — a lição do painel lateral (#101), herdada pelo #127 e pelo
#129.

São dois sistemas, com geometrias diferentes:

* **BeeFood** (imagens 01 a 04). O painel lateral da API Aberta começa em x=1154 dos 2160 px e o
  resto da tela fica escurecido: `painel()` recorta no painel e põe faixa clara dos dois lados.
  Os diálogos (nova credencial, credencial criada) não moram dentro do painel, então têm recorte
  próprio em `dialogo()`, com o painel escurecido atrás como contexto.
* **Natural Bot** (imagens 05 a 12). Tela de 1440x900 em DPR 1.5, menu escuro à esquerda e
  diálogos no centro. Os diálogos de lá são mais largos que os da BeeFood, e começam em x=580:
  `dialogo_nb()` recorta neles. Nas telas cheias a etiqueta vai numa faixa em cima ou na área
  vazia à direita dos cards, porque o menu da esquerda é escuro e etiqueta verde sobre ele fica
  ilegível.

Duas imagens são **costuradas** por `montagem()`, para o passo caber em uma foto só:

* **02**, da linha de abas do painel direto para o `CRIAR CREDENCIAL`, que fica muito abaixo;
* **05**, do cabeçalho da aba *Integrações* direto para o card da BeeFood, que no painel do
  parceiro é o décimo segundo gestor de PDV — os outros onze são concorrentes e não entram.

A emenda sai **tracejada**: ali o print foi cortado, e o leitor tem de saber que entre as duas
metades existe tela que não está na foto. Nenhuma faixa e nenhuma costura é gravada na pura:
tudo é montado em memória aqui dentro, senão rodar duas vezes desloca todas as setas. Pura é o
print, e só.
"""

import math
import os

from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

VERDE = (22, 150, 78)
BRANCO = (255, 255, 255)
CINZA = (170, 180, 196)
A_LINHA = 235
A_ETIQ = 245
FAIXA = (255, 255, 255)

FONTES = [
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]

MARGEM = 150

# --- BeeFood: painel lateral da API Aberta, na captura de 2160x1950 ---------------------
PAINEL_X0 = 1154
ESQ_PAINEL = PAINEL_X0 - MARGEM // 2      # 1079
DIR_PAINEL = 2160 + MARGEM // 2           # 2235

# --- BeeFood: diálogos, que começam antes do painel ------------------------------------
DIALOGO_X0 = 520
ESQ_DIALOGO = DIALOGO_X0 - MARGEM // 2    # 445
DIR_DIALOGO = 1700 + MARGEM // 2          # 1775

# --- Natural Bot: diálogos no centro da tela de 2160x1350 ------------------------------
NB_X0 = 520
NB_X1 = 1700
ESQ_NB = NB_X0 - MARGEM // 2              # 445
DIR_NB = NB_X1 + MARGEM // 2              # 1775


def font(sz):
    for caminho in FONTES:
        if os.path.exists(caminho):
            return ImageFont.truetype(caminho, sz)
    raise RuntimeError("nenhuma fonte bold encontrada")


def seta(d, x0, y0, x1, y1, w):
    cor = VERDE + (A_LINHA,)
    d.line([(x0, y0), (x1, y1)], fill=cor, width=w)
    ang = math.atan2(y1 - y0, x1 - x0)
    L = w * 4.0
    for s in (0.5, -0.5):
        d.line([(x1, y1), (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))],
               fill=cor, width=w)


def etiqueta(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 3, cy - r - 3, cx + r + 3, cy + r + 3], fill=BRANCO + (245,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=VERDE + (A_ETIQ,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
           t, fill=BRANCO, font=fnt)


def desenhar(img, marcadores, r, w, saida):
    """Põe seta e etiqueta em cima da imagem já montada, com as coordenadas absolutas."""
    camada = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(camada)
    fnt = font(int(r * 1.25))
    for (num, ax, ay, bx, by) in marcadores:
        ang = math.atan2(ay - by, ax - bx)
        seta(d, bx + (r + 6) * math.cos(ang), by + (r + 6) * math.sin(ang), ax, ay, w)
        etiqueta(d, bx, by, r, num, fnt)
    Image.alpha_composite(img, camada).convert("RGB").save(os.path.join(OUT, saida))
    print("OK", saida, img.width, img.height, f"({len(marcadores)} seta(s))")


def preparar(nome, corte, esquerda, direita, topo, base):
    """Recorta e põe faixa clara em cada lado pedido. Devolve a imagem e o deslocamento."""
    img = Image.open(os.path.join(SRC, nome)).convert("RGBA")
    dx = dy = 0
    if corte:
        img = img.crop(corte)
        dx, dy = -corte[0], -corte[1]
    if esquerda or direita or topo or base:
        base_img = Image.new(
            "RGBA",
            (img.width + esquerda + direita, img.height + topo + base),
            FAIXA + (255,),
        )
        base_img.paste(img, (esquerda, topo))
        img = base_img
        dx += esquerda
        dy += topo
    return img, dx, dy


def annotate(nome, marcadores=(), corte=None, esquerda=0, direita=0, topo=0, base=0,
             saida=None, r=None, w=None):
    img, dx, dy = preparar(nome, corte, esquerda, direita, topo, base)
    r = r or int(img.width * 0.0125)
    w = w or max(2, int(img.width * 0.0022))
    desenhar(img, [(n, ax + dx, ay + dy, bx + dx, by + dy)
                   for (n, ax, ay, bx, by) in marcadores], r, w, saida or nome)


def montagem(fatias, marcadores=(), saida=None, esquerda=MARGEM, direita=MARGEM,
             costura=46, base=0, r=28, w=4):
    """Costura recortes de print numa imagem só, deixando a emenda à vista.

    Cada fatia é `(nome, (x0, y0, x1, y1), x_destino)`: o recorte da pura e onde a borda
    esquerda dele encosta na **moldura**, que é o sistema de coordenadas da primeira fatia.
    `x_destino=None` mantém o recorte no x em que ele foi fotografado.

    Marcador é `(num, ax, ay, bx, by, fatia)`, em pixel da pura daquela fatia.
    """
    quadro_x0, _, quadro_x1, _ = fatias[0][1]
    largura = esquerda + (quadro_x1 - quadro_x0) + direita

    recortes, deslocamentos, altura = [], [], 0
    for nome, caixa, destino in fatias:
        img = Image.open(os.path.join(SRC, nome)).convert("RGBA").crop(caixa)
        x0, y0 = caixa[0], caixa[1]
        px = esquerda + ((x0 if destino is None else destino) - quadro_x0)
        recortes.append((img, px, altura))
        deslocamentos.append((px - x0, altura - y0))
        altura += img.height + costura
    altura = altura - costura + base

    tela = Image.new("RGBA", (largura, altura), FAIXA + (255,))
    for img, px, py in recortes:
        tela.paste(img, (px, py))

    d = ImageDraw.Draw(tela)
    for _, _, py in recortes[1:]:
        y = py - costura // 2
        for x in range(esquerda + 20, largura - direita - 20, 64):
            d.line([(x, y), (min(x + 36, largura - direita - 20), y)], fill=CINZA, width=3)

    absolutos = []
    for (num, ax, ay, bx, by, fatia) in marcadores:
        dx, dy = deslocamentos[fatia]
        absolutos.append((num, ax + dx, ay + dy, bx + dx, by + dy))
    desenhar(tela, absolutos, r, w, saida)


def painel(nome, marcadores=(), y0=0, y1=1950, **kw):
    """Painel lateral da API Aberta: recorte no painel e faixa clara dos dois lados."""
    annotate(nome, marcadores=marcadores, corte=(PAINEL_X0, y0, 2160, y1),
             esquerda=MARGEM, direita=MARGEM, r=28, w=4, **kw)


def dialogo(nome, marcadores=(), y0=0, y1=1950, **kw):
    """Diálogo do BeeFood, com o painel escurecido atrás como contexto."""
    annotate(nome, marcadores=marcadores, corte=(DIALOGO_X0, y0, 1700, y1),
             esquerda=MARGEM, direita=MARGEM, r=30, w=4, **kw)


def dialogo_nb(nome, marcadores=(), y0=0, y1=1350, **kw):
    """Diálogo do painel da Natural Bot: recorte no diálogo, faixa dos dois lados."""
    annotate(nome, marcadores=marcadores, corte=(NB_X0, y0, NB_X1, y1),
             esquerda=MARGEM, direita=MARGEM, r=30, w=4, **kw)


# =====================================================================================
# Parte 1 — a credencial, no BeeFood
# =====================================================================================

# 01 — Aplicativos: a seção API e MCP e o card da API Aberta. Tela inteira, porque é o
# contexto de onde o painel sai; a etiqueta cabe no vão entre o menu e a primeira coluna.
annotate(
    "01-aplicativos-api-aberta.png",
    marcadores=(
        (1, 310, 555, 420, 555),      # menu Aplicativos (borda direita da faixa de seleção)
        (2, 520, 331, 412, 331),      # card API Aberta
    ),
    r=30, w=5,
)

# 02 — da aba Credencial direto para o CRIAR CREDENCIAL. As duas pontas do painel numa foto:
# no meio fica a credencial principal, que neste manual não se toca.
montagem(
    (
        ("02-painel-credencial.png", (PAINEL_X0, 312, 2160, 380), None),
        ("02-painel-credencial.png", (PAINEL_X0, 1545, 2160, 1778), None),
    ),
    saida="02-criar-credencial.png",
    marcadores=(
        (1, 1184, 333, ESQ_PAINEL, 333, 0),    # aba Credencial
        (2, 1225, 1584, ESQ_PAINEL, 1584, 1),  # RECICLAR (o que não se clica)
        (3, 1180, 1688, ESQ_PAINEL, 1688, 1),  # CRIAR CREDENCIAL
    ),
)

# 03 — o diálogo da nova credencial como ele tem de ficar: só os seis acessos da Natural Bot.
# Ele abre com tudo ligado, e isso o texto diz — fotografar os dois estados era repetir a
# mesma tela duas vezes.
dialogo(
    "03-nova-credencial-seis.png",
    y0=430, y1=1540,
    marcadores=(
        (1, 790, 637, ESQ_DIALOGO, 637),     # Pedidos: Consultar e Alterar
        # Na coluna da direita os rótulos *Consultar* e *Alterar* ficam na mesma linha dos
        # interruptores: seta que mira o interruptor atravessa os dois. Mira a borda do cartão.
        (2, 1535, 637, DIR_DIALOGO, 637),    # Catálogo: Consultar
        (3, 1535, 768, DIR_DIALOGO, 768),    # Loja: Consultar
        (4, 1535, 1158, DIR_DIALOGO, 1158),  # Webhooks: Consultar e Alterar
        (5, 1550, 1432, DIR_DIALOGO, 1432),  # CRIAR (F2)
    ),
)

# 04 — a tela que só existe depois de criar: os dois valores que vão para a Natural Bot.
dialogo(
    "04-credencial-criada.png",
    y0=660, y1=1290,
    marcadores=(
        (1, 752, 913, ESQ_DIALOGO, 913),     # clientId
        (2, 758, 1027, ESQ_DIALOGO, 1027),   # clientSecret
        (3, 1430, 1183, DIR_DIALOGO, 1183),  # FECHAR (ESC)
    ),
)


# =====================================================================================
# Parte 2 — ligar a BeeFood, no painel da Natural Bot
# =====================================================================================

# 05 — a aba Integrações e o card da BeeFood, costurados. No painel do parceiro a BeeFood é o
# décimo segundo gestor de PDV, atrás de onze concorrentes que não cabem num manual nosso: o
# card dele entra no lugar do primeiro, e a emenda tracejada diz que a lista foi cortada.
montagem(
    (
        # O menu escuro fica fora: ele reapareceria cortado na emenda, e o caminho até aqui já
        # está no título do passo e na trilha *Ferramentas › Configurações* da própria foto.
        ("05a-nb-integracoes.png", (425, 8, 2160, 630), None),
        ("05b-nb-card-beefood.png", (1307, 547, 1686, 780), 518),
    ),
    saida="05-nb-integracoes-beefood.png",
    esquerda=0, direita=MARGEM, base=40,
    marcadores=(
        (1, 1280, 262, 1280, 150, 0),              # aba Integrações
        (2, 2040, 572, 2160 + MARGEM // 2, 572, 0),  # aviso do gestor de PDV
        (3, 1665, 612, 1686 + 90, 612, 1),         # chave liga/desliga do card
        (4, 1455, 723, 1686 + 90, 723, 1),         # CONFIGURAR (ou EDITAR, se já tem credencial)
    ),
    r=28, w=5,
)

# 06 — o formulário da credencial: a própria tela lista os seis acessos.
dialogo_nb(
    "06-nb-form-credencial.png",
    y0=40, y1=1310,
    marcadores=(
        (1, 655, 589, ESQ_NB, 589),          # a lista dos seis acessos
        (2, 660, 745, ESQ_NB, 760),          # o aviso sobre webhook:read e webhook:write
        (3, 635, 925, ESQ_NB, 925),          # Client ID
        (4, 635, 1047, ESQ_NB, 1047),        # Client secret
        (5, 1550, 1251, DIR_NB, 1251),       # Conectar
    ),
)

# 07 — cardápio e de-para de pagamentos, a segunda etapa do mesmo diálogo.
dialogo_nb(
    "07-nb-cardapio-pagamentos.png",
    y0=160, y1=1200,
    marcadores=(
        (1, 635, 468, ESQ_NB, 468),          # Cardápio
        (2, 635, 627, ESQ_NB, 627),          # Formas de pagamento
        (3, 1524, 943, DIR_NB, 943),         # Ligar a integração ao salvar
        (4, 1550, 1109, DIR_NB, 1109),       # Salvar
    ),
)

# 08 — o resultado da verificação que a Natural Bot faz na BeeFood depois de salvar.
dialogo_nb(
    "08-nb-verificacao.png",
    y0=420, y1=940,
    marcadores=(
        (1, 611, 648, ESQ_NB, 648),          # configurada com sucesso
        (2, 611, 732, ESQ_NB, 732),          # aviso do canal de delivery
        (3, 1550, 843, DIR_NB, 843),         # Concluir
    ),
)

# 09 — a integração já configurada: é esta tela que diz que o webhook de status está ativo.
dialogo_nb(
    "09-nb-integracao-configurada.png",
    y0=40, y1=1310,
    marcadores=(
        (1, 648, 286, ESQ_NB, 286),          # Client ID mascarado, cardápio e pagamentos
        (2, 947, 458, ESQ_NB, 458),          # Editar Integração
        (3, 1524, 693, DIR_NB, 693),         # Integração ligada
        (4, 635, 832, ESQ_NB, 850),          # Webhook de status: ativo
        (5, 1352, 1114, DIR_NB, 1114),       # Ir para Produtos
    ),
)


# =====================================================================================
# Parte 3 — sincronizar o cardápio
# =====================================================================================

# 10 — Cardápio → Produtos e o botão Sinc. BeeFood. Faixa em cima, porque o botão fica na
# primeira linha da tela e não há espaço acima dele.
annotate(
    "10-nb-produtos-sinc.png",
    corte=(0, 0, 2160, 560), topo=MARGEM,
    marcadores=(
        (1, 390, 479, 500, 479),             # Produtos, no menu Cardápio
        (2, 1137, 220, 1137, -75),           # Sinc. BeeFood
    ),
    r=26, w=4,
)

# 11 — o diálogo da importação: as três opções vêm desmarcadas, e é assim que se roda a
# primeira vez.
dialogo_nb(
    "11-nb-importacao-opcoes.png",
    y0=140, y1=1270,
    marcadores=(
        (1, 653, 371, ESQ_NB, 371),          # a importação é processada em fila
        (2, 673, 705, ESQ_NB, 705),          # as três opções, desmarcadas
        (3, 1508, 988, DIR_NB, 988),         # Importar
    ),
)

# 12 — o fim da importação, com a conta do que entrou.
dialogo_nb(
    "12-nb-importacao-concluida.png",
    y0=680, y1=1270,
    marcadores=(
        (1, 653, 1006, ESQ_NB, 1006),        # Importação concluída
        (2, 1505, 1088, DIR_NB, 1088),       # categorias, produtos, variações e opções
        (3, 1535, 1232, DIR_NB, 1232),       # Fechar
    ),
)
