"""Anota as catorze capturas do #129 — integração com o Route Delivery.

As coordenadas estão sempre em **pixel da captura pura**, inclusive nas recortadas:
`preparar()` converte. Medir na captura inteira é o que permite mexer no recorte depois sem
remedir nada — a lição do painel lateral (#101), herdada pelo #127.

As puras vêm de dois lugares, e o manual mostra as duas pontas da integração:

* as sete do BeeFood saem do `capturar-painel.py` (1440x900 para a tela de Aplicativos e
  1440x1300 para o painel lateral, sempre em DPR 1.5);
* as seis do Route Delivery saem do `importar.py`, que as decodifica do HTML do artigo público
  do parceiro — lá elas vêm embutidas em base64, não como arquivo.

Quatro geometrias, cada uma com o seu motivo:

* **Painel lateral** (`painel()`): o painel começa em x=1154 dos 2160 px e o resto é tela
  escurecida. Recorta no painel e põe faixa clara **dos dois lados** — a da esquerda para quem
  aponta texto, a da direita para selo e botão encostados na borda.
* **Diálogo no centro** (`dialogo()`): não está dentro do painel, então tem recorte próprio, com
  o painel escurecido atrás como contexto.
* **Captura larga e rasa do parceiro** (`faixa()`): tira de 160 a 550 px de altura, com faixa
  em cima e embaixo. Seta horizontal não serve aqui: numa tira dessas, os alvos ficam em duas
  linhas, e etiqueta na laterais faria a seta atravessar a linha inteira.
* **Captura alta do parceiro** (`lado()`): faixa à esquerda e à direita, como no painel.

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

# Painel lateral da API Aberta, na captura de 2160x1950.
PAINEL_X0 = 1154
MARGEM = 150
RAIO_PAINEL = 28
TRACO_PAINEL = 4

# Centro das faixas do painel, em pixel da pura: é onde as etiquetas moram.
ESQ_PAINEL = PAINEL_X0 - MARGEM // 2      # 1079
DIR_PAINEL = 2160 + MARGEM // 2           # 2235

# O diálogo tem recorte próprio, que começa antes do painel.
DIALOGO_X0 = 620
ESQ_DIALOGO = DIALOGO_X0 - MARGEM // 2    # 545
DIR_DIALOGO = DIR_PAINEL                  # 2235


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
    """Painel lateral: recorte no painel e faixa clara dos dois lados."""
    annotate(nome, marcadores=marcadores, corte=(PAINEL_X0, y0, 2160, y1),
             esquerda=MARGEM, direita=MARGEM, r=RAIO_PAINEL, w=TRACO_PAINEL, **kw)


def dialogo(nome, marcadores=(), y0=0, y1=1950, **kw):
    """Diálogo no centro da tela, com o painel escurecido atrás como contexto."""
    annotate(nome, marcadores=marcadores, corte=(DIALOGO_X0, y0, 2160, y1),
             esquerda=MARGEM, direita=MARGEM, r=30, w=4, **kw)


def faixa(nome, marcadores=(), altura=110, r=22, **kw):
    """Tira larga e rasa do parceiro: etiquetas em cima e embaixo, setas na vertical."""
    annotate(nome, marcadores=marcadores, topo=altura, base=altura, r=r, w=3, **kw)


def lado(nome, marcadores=(), margem=150, r=24, **kw):
    """Captura alta do parceiro: faixa à esquerda e à direita."""
    annotate(nome, marcadores=marcadores, esquerda=margem, direita=margem, r=r, w=3, **kw)


# =====================================================================================
# Parte 1 — a credencial do Route Delivery, no BeeFood
# =====================================================================================

# 01 — Aplicativos: o card da API Aberta. Tela inteira, sem recorte: é o contexto de onde o
# painel sai, e a etiqueta cabe no vão entre o menu e a primeira coluna de cards.
annotate(
    "01-aplicativos-api-aberta.png",
    marcadores=(
        (1, 306, 648, 420, 648),     # menu Aplicativos (borda direita da faixa de seleção)
        (2, 500, 332, 400, 332),     # card API Aberta
    ),
    r=30, w=5,
)

# 02 — o painel abriu na aba Credencial. O recado desta imagem é que a credencial que o artigo
# do parceiro manda criar no portal é a que já está aqui — por isso a seta no rodapé do cartão.
painel(
    "02-painel-credencial.png",
    y0=0, y1=628,
    marcadores=(
        (1, 1184, 334, ESQ_PAINEL, 334),     # aba Credencial
        (2, 1206, 588, ESQ_PAINEL, 588),     # "Esta é a credencial exibida no portal docs..."
    ),
)

# 03 — o fim do mesmo cartão: as permissões que o Route Delivery pede, o RECICLAR que não se
# clica e o CRIAR CREDENCIAL, que é o caminho deste manual. Segundo recorte da mesma pura.
painel(
    "02-painel-credencial.png",
    saida="03-criar-credencial.png",
    y0=628, y1=1880,
    marcadores=(
        (1, 1180, 717, ESQ_PAINEL, 717),      # Pedidos
        (2, 1180, 1032, ESQ_PAINEL, 1032),    # Loja
        (3, 1180, 1652, ESQ_PAINEL, 1652),    # RECICLAR (o que não se clica)
        (4, 1180, 1756, ESQ_PAINEL, 1756),    # CRIAR CREDENCIAL
    ),
)

# 04 — o diálogo da nova credencial: já nasce com os recursos ligados.
dialogo(
    "04-nova-credencial.png",
    y0=380, y1=1580,
    marcadores=(
        (1, 748, 609, ESQ_DIALOGO, 609),      # Pedidos: consultar e alterar
        (2, 748, 923, ESQ_DIALOGO, 923),      # Loja: consultar
        (3, 1430, 1468, DIR_DIALOGO, 1468),   # CRIAR (F2)
    ),
)

# 05 — a tela que só existe depois de criar: os dois valores que vão para o Route Delivery.
dialogo(
    "05-credencial-criada.png",
    y0=640, y1=1320,
    marcadores=(
        (1, 742, 914, ESQ_DIALOGO, 914),      # clientId
        (2, 742, 1027, ESQ_DIALOGO, 1027),    # clientSecret
        (3, 1423, 1184, DIR_DIALOGO, 1184),   # FECHAR (ESC)
    ),
)


# =====================================================================================
# Parte 2 — o vínculo da loja, no Route Delivery (capturas do parceiro)
# =====================================================================================

lado(
    "06-rd-cartao-beefood.png",
    margem=120, r=18,
    marcadores=(
        (1, 575, 106, 648 + 60, 106),         # selo Ativa (borda direita)
        (2, 68, 318, -60, 318),               # lojas vinculadas, eventos e erros
    ),
)

lado(
    "07-rd-vincular-loja.png",
    marcadores=(
        (1, 235, 185, -75, 185),              # Comércio no sistema
        (2, 2324, 178, 2352 + 75, 178),       # Client ID
        (3, 235, 300, -75, 300),              # Client Secret
        (4, 255, 419, -75, 419),              # Credencial do sandbox (fica desmarcado)
        (5, 2324, 483, 2352 + 75, 483),       # Testar credencial e vincular
    ),
)

annotate(
    "08-rd-integracao-ativa.png",
    base=170, r=22, w=3,
    marcadores=(
        (1, 2013, 97, 2013, 160 + 85),        # selo Ativa
        (2, 2213, 112, 2213, 160 + 85),       # Pausar integração
    ),
)

lado(
    "09-rd-liberar-na-chegada.png",
    r=22,
    marcadores=(
        (1, 58, 203, -75, 203),               # liberar o pedido assim que chegar
    ),
)

lado(
    "10-rd-canais-marketplace.png",
    marcadores=(
        (1, 344, 400, -75, 400),              # canais de marketplace
        (2, 310, 485, -75, 485),              # Buscar pedidos agora
    ),
)


# =====================================================================================
# Parte 3 — o webhook, de volta no BeeFood
# =====================================================================================

# 11 — a linha da loja no Route Delivery: de onde sai o endereço do webhook (1 e 2) e onde o
# secret da BeeFood é colado depois (3 e 4). Duas linhas de alvos, então duas faixas.
faixa(
    "11-rd-endereco-webhook.png",
    marcadores=(
        (1, 1150, 89, 1150, -55),             # endereço do webhook da loja
        (2, 1605, 78, 1605, -55),             # Copiar
        (3, 1100, 240, 1100, 256 + 55),       # campo do secret do webhook
        (4, 1605, 229, 1605, 256 + 55),       # Salvar
    ),
)

painel(
    "12-aba-webhooks.png",
    y0=305, y1=512,
    marcadores=(
        (1, 1180, 418, ESQ_PAINEL, 418),      # NOVO WEBHOOK
    ),
)

dialogo(
    "13-novo-webhook.png",
    y0=470, y1=1520,
    marcadores=(
        (1, 729, 688, ESQ_DIALOGO, 688),      # URL (https)
        (2, 742, 804, ESQ_DIALOGO, 804),      # Eventos
        (3, 731, 1060, ESQ_DIALOGO, 1060),    # E-mail de contato
        (4, 728, 1122, ESQ_DIALOGO, 1122),    # Autenticação Basic (fica em branco)
        (5, 1403, 1395, DIR_DIALOGO, 1395),   # SALVAR (F2)
    ),
)

painel(
    "14-webhook-ativo.png",
    y0=305, y1=1010,
    marcadores=(
        (1, 1225, 487, ESQ_PAINEL, 487),      # Secret do webhook
        (2, 1210, 592, ESQ_PAINEL, 592),      # JÁ GUARDEI
        (3, 2102, 828, DIR_PAINEL, 828),      # selo Ativo (borda direita do selo)
        (4, 1216, 955, ESQ_PAINEL, 955),      # chave liga/desliga, EDITAR e EXCLUIR
    ),
)
