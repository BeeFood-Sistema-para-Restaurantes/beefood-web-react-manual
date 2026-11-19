"""Anota as dezesseis capturas do #134 — ativação da integração com a Natural Bot.

As coordenadas estão sempre em **pixel da captura pura**, inclusive nas recortadas:
`preparar()` converte. Medir na pura inteira é o que deixa mexer no recorte depois sem remedir
nada — a lição do painel lateral (#101), herdada pelo #127 e pelo #129.

São dois sistemas, com geometrias diferentes:

* **BeeFood** (imagens 01 a 06). O painel lateral da API Aberta começa em x=1154 dos 2160 px e o
  resto da tela fica escurecido: `painel()` recorta no painel e põe faixa clara dos dois lados.
  Os diálogos (nova credencial, credencial criada) não moram dentro do painel, então têm recorte
  próprio em `dialogo()`, com o painel escurecido atrás como contexto.
* **Natural Bot** (imagens 07 a 16). Tela de 1440x900 em DPR 1.5, menu escuro à esquerda e
  diálogos no centro. Os diálogos de lá são mais largos que os da BeeFood, e começam em x=580:
  `dialogo_nb()` recorta neles. Nas telas cheias (aba Integrações, Produtos) a etiqueta vai numa
  faixa em cima ou na área vazia à direita dos cards, porque o menu da esquerda é escuro e
  etiqueta verde sobre ele fica ilegível.

Nenhuma faixa é gravada na pura: tudo é montado em memória aqui dentro, senão rodar duas vezes
desloca todas as setas. Pura é o print, e só.
"""

import math
import os

from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

VERDE = (22, 150, 78)
BRANCO = (255, 255, 255)
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
    W, H = img.size
    camada = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(camada)
    r = r or int(W * 0.0125)
    w = w or max(2, int(W * 0.0022))
    fnt = font(int(r * 1.25))
    for (num, ax, ay, bx, by) in marcadores:
        ax, bx = ax + dx, bx + dx
        ay, by = ay + dy, by + dy
        ang = math.atan2(ay - by, ax - bx)
        seta(d, bx + (r + 6) * math.cos(ang), by + (r + 6) * math.sin(ang), ax, ay, w)
        etiqueta(d, bx, by, r, num, fnt)
    Image.alpha_composite(img, camada).convert("RGB").save(os.path.join(OUT, saida or nome))
    print("OK", saida or nome, W, H, f"({len(marcadores)} seta(s))")


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

# 02 — o painel abriu na aba Credencial. O recado é que a credencial principal já existe e é a
# mesma do portal: não é ela que vai para a Natural Bot.
painel(
    "02-painel-credencial.png",
    y0=0, y1=640,
    marcadores=(
        (1, 1185, 333, ESQ_PAINEL, 333),     # aba Credencial
        (2, 1205, 588, ESQ_PAINEL, 588),     # "Esta é a credencial exibida no portal docs..."
    ),
)

# 03 — o fim do mesmo cartão, no segundo recorte da mesma pura: o RECICLAR que não se clica e o
# CRIAR CREDENCIAL, que é o caminho deste manual.
painel(
    "02-painel-credencial.png",
    saida="03-criar-credencial.png",
    y0=1430, y1=1790,
    marcadores=(
        (1, 1225, 1582, ESQ_PAINEL, 1582),   # RECICLAR (o que não se clica)
        (2, 1180, 1687, ESQ_PAINEL, 1687),   # CRIAR CREDENCIAL
    ),
)

# 04 — o diálogo da nova credencial, como ele abre: todos os recursos ligados.
dialogo(
    "04-nova-credencial-tudo.png",
    y0=430, y1=1540,
    marcadores=(
        (1, 790, 637, ESQ_DIALOGO, 637),     # os dois interruptores de Pedidos
        (2, 795, 664, ESQ_DIALOGO, 724),     # o nome do acesso, embaixo do interruptor
        (3, 785, 768, ESQ_DIALOGO, 830),     # Consultar de Clientes (um dos que saem)
    ),
)

# 05 — o mesmo diálogo depois de desligar o resto: só os seis acessos da Natural Bot.
dialogo(
    "05-nova-credencial-seis.png",
    y0=430, y1=1540,
    marcadores=(
        (1, 790, 637, ESQ_DIALOGO, 637),     # Pedidos: Consultar e Alterar
        (2, 1300, 637, DIR_DIALOGO, 637),    # Catálogo: Consultar
        (3, 1300, 768, DIR_DIALOGO, 768),    # Loja: Consultar
        (4, 1445, 1158, DIR_DIALOGO, 1158),  # Webhooks: Consultar e Alterar
        (5, 1550, 1432, DIR_DIALOGO, 1432),  # CRIAR (F2)
    ),
)

# 06 — a tela que só existe depois de criar: os dois valores que vão para a Natural Bot.
dialogo(
    "06-credencial-criada.png",
    y0=660, y1=1290,
    marcadores=(
        (1, 752, 913, ESQ_DIALOGO, 913),     # clientId
        (2, 758, 1027, ESQ_DIALOGO, 1027),  # clientSecret
        (3, 1430, 1183, DIR_DIALOGO, 1183),  # FECHAR (ESC)
    ),
)


# =====================================================================================
# Parte 2 — ligar a BeeFood, no painel da Natural Bot
# =====================================================================================

# 07 — Configurações, aba Integrações: o aviso de que só um gestor de PDV fica ativo.
annotate(
    "07-nb-configuracoes-integracoes.png",
    direita=MARGEM,
    marcadores=(
        (1, 390, 776, 500, 776),             # menu Configurações (borda da faixa de seleção)
        (2, 1280, 262, 1280, 150),           # aba Integrações
        (3, 2040, 572, 2160 + MARGEM // 2, 572),   # aviso do gestor de PDV
    ),
    r=28, w=5,
)

# 08 — o card da BeeFood, entre os gestores de PDV. Recorte no card: a lista é longa e o que
# importa é o que o card tem (a chave e o botão).
annotate(
    "08-nb-card-beefood.png",
    corte=(1240, 480, 2160, 840),
    marcadores=(
        (1, 1665, 612, 1810, 612),           # chave liga/desliga
        (2, 1455, 723, 1810, 723),           # CONFIGURAR (ou EDITAR, se já tem credencial)
    ),
    r=20, w=3,
)

# 09 — o formulário da credencial: a própria tela lista os seis acessos.
dialogo_nb(
    "09-nb-form-credencial.png",
    y0=40, y1=1310,
    marcadores=(
        (1, 655, 589, ESQ_NB, 589),          # a lista dos seis acessos
        (2, 660, 745, ESQ_NB, 760),          # o aviso sobre webhook:read e webhook:write
        (3, 635, 925, ESQ_NB, 925),          # Client ID
        (4, 635, 1047, ESQ_NB, 1047),        # Client secret
        (5, 1550, 1251, DIR_NB, 1251),       # Conectar
    ),
)

# 10 — cardápio e de-para de pagamentos, a segunda etapa do mesmo diálogo.
dialogo_nb(
    "10-nb-cardapio-pagamentos.png",
    y0=160, y1=1200,
    marcadores=(
        (1, 635, 468, ESQ_NB, 468),          # Cardápio
        (2, 635, 627, ESQ_NB, 627),          # Formas de pagamento
        (3, 1524, 943, DIR_NB, 943),         # Ligar a integração ao salvar
        (4, 1550, 1109, DIR_NB, 1109),       # Salvar
    ),
)

# 11 — o resultado da verificação que a Natural Bot faz na BeeFood depois de salvar.
dialogo_nb(
    "11-nb-verificacao.png",
    y0=420, y1=940,
    marcadores=(
        (1, 611, 648, ESQ_NB, 648),          # configurada com sucesso
        (2, 611, 732, ESQ_NB, 732),          # aviso do canal de delivery
        (3, 1550, 843, DIR_NB, 843),         # Concluir
    ),
)

# 12 — a integração já configurada: é esta tela que diz que o webhook de status está ativo.
dialogo_nb(
    "12-nb-integracao-configurada.png",
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

# 13 — Cardápio → Produtos e o botão Sinc. BeeFood. Faixa em cima, porque o botão fica na
# primeira linha da tela e não há espaço acima dele.
annotate(
    "13-nb-produtos-sinc.png",
    corte=(0, 0, 2160, 560), topo=MARGEM,
    marcadores=(
        (1, 390, 479, 500, 479),             # Produtos, no menu Cardápio
        (2, 1137, 220, 1137, -75),           # Sinc. BeeFood
    ),
    r=26, w=4,
)

# 14 — o diálogo da importação: as três opções vêm desmarcadas, e é assim que se roda a
# primeira vez.
dialogo_nb(
    "14-nb-importacao-opcoes.png",
    y0=140, y1=1270,
    marcadores=(
        (1, 653, 371, ESQ_NB, 371),          # a importação é processada em fila
        (2, 673, 705, ESQ_NB, 705),          # as três opções, desmarcadas
        (3, 1508, 988, DIR_NB, 988),         # Importar
    ),
)

# 15 — o fim da importação, com a conta do que entrou.
dialogo_nb(
    "15-nb-importacao-concluida.png",
    y0=680, y1=1270,
    marcadores=(
        (1, 653, 1006, ESQ_NB, 1006),        # Importação concluída
        (2, 1505, 1088, DIR_NB, 1088),       # categorias, produtos, variações e opções
        (3, 1535, 1232, DIR_NB, 1232),       # Fechar
    ),
)

# 16 — a lista de produtos com o cardápio que chegou da BeeFood.
annotate(
    "16-nb-produtos-importados.png",
    corte=(440, 300, 2160, 1150), esquerda=MARGEM,
    marcadores=(
        (1, 483, 375, 365, 375),             # aba Todos
        (2, 690, 723, 365, 723),             # um produto que veio da BeeFood
    ),
    r=24, w=4,
)
