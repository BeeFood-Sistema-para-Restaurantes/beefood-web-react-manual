"""Anota as onze capturas do #127 — integração com o Entregas Expressas.

As coordenadas estão sempre em **pixel da captura pura**, inclusive nas imagens recortadas:
`preparar()` converte. Medir uma vez na captura inteira é o que permite mexer no recorte
depois sem remedir nada — a lição dos manuais do painel lateral (#101) e dos seis do app.

As puras vêm de dois lugares, e o manual mostra as duas pontas da integração:

* as cinco do BeeFood saem do `capturar-painel.py` (viewport 1440x900 para a tela de
  Aplicativos e 1440x1300 para o painel lateral, sempre em DPR 1.5);
* as quatro do Entregas Expressas saem do `importar.py`, que as baixa do artigo público do
  parceiro e já cobre telefone e e-mail antes de gravar a pura.

Três geometrias, cada uma com o seu motivo:

* **Painel lateral** (`painel()`): o painel começa em x=1154 dos 2160 px e o resto é tela
  escurecida. Recorta no painel e põe faixa clara **dos dois lados** — a da esquerda para as
  etiquetas de quem aponta texto, a da direita para as de quem aponta selo, ícone de olho e
  botão encostado na borda. A da direita existe porque mirar da esquerda um elemento que vive
  no canto direito faz a seta atravessar o rótulo inteiro.
* **Diálogo no centro** (`dialogo()`): não está dentro do painel, então tem recorte próprio,
  com o painel escurecido atrás como contexto. Mesma faixa dos dois lados.
* **Captura do parceiro**: entra inteira. O painel do Entregas Expressas tem margem de página
  vazia à esquerda, e as etiquetas moram ali — não precisa de faixa.

Rodar duas vezes tem de dar os mesmos bytes: nenhuma faixa é gravada na pura, só montada em
memória aqui dentro. Pura é o print, e só.
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
MARGEM = 150          # faixa clara de cada lado, onde ficam as etiquetas
RAIO_PAINEL = 28
TRACO_PAINEL = 4

# Centro das faixas, em pixel da pura: é onde as etiquetas vão.
ESQ_PAINEL = PAINEL_X0 - MARGEM // 2      # 1079
DIR_PAINEL = 2160 + MARGEM // 2           # 2235


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


def preparar(nome, corte, margem):
    """Recorta e põe a faixa clara dos dois lados. Devolve a imagem e o deslocamento."""
    img = Image.open(os.path.join(SRC, nome)).convert("RGBA")
    dx = dy = 0
    if corte:
        img = img.crop(corte)
        dx, dy = -corte[0], -corte[1]
    if margem:
        base = Image.new("RGBA", (img.width + 2 * margem, img.height), FAIXA + (255,))
        base.paste(img, (margem, 0))
        img = base
        dx += margem
    return img, dx, dy


def annotate(nome, marcadores=(), corte=None, margem=0, saida=None, r=None, w=None):
    img, dx, dy = preparar(nome, corte, margem)
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
    Image.alpha_composite(img, camada).convert("RGB").save(
        os.path.join(OUT, saida or nome))
    print("OK", saida or nome, W, H, f"({len(marcadores)} seta(s))")


def painel(nome, marcadores=(), y0=0, y1=1950, **kw):
    """Imagem do painel lateral: recorte no painel e faixa clara dos dois lados."""
    annotate(nome, marcadores=marcadores, corte=(PAINEL_X0, y0, 2160, y1),
             margem=MARGEM, r=RAIO_PAINEL, w=TRACO_PAINEL, **kw)


def dialogo(nome, marcadores=(), y0=0, y1=1950, **kw):
    """Diálogo no centro da tela, com o painel escurecido atrás como contexto."""
    annotate(nome, marcadores=marcadores, corte=(620, y0, 2160, y1),
             margem=MARGEM, r=30, w=4, **kw)


# As etiquetas dos diálogos moram nas mesmas faixas, mas o recorte começa antes.
ESQ_DIALOGO = 620 - MARGEM // 2           # 545
DIR_DIALOGO = DIR_PAINEL                  # 2235


# =====================================================================================
# Parte 1 — a credencial, no BeeFood
# =====================================================================================

# 01 — Aplicativos: o card da API Aberta. Tela inteira, sem recorte: é o contexto de onde
# o painel sai, e a etiqueta cabe no vão entre o menu e a primeira coluna de cards.
annotate(
    "01-aplicativos-api-aberta.png",
    marcadores=(
        (1, 306, 648, 420, 648),     # menu Aplicativos (borda direita da faixa de seleção)
        (2, 500, 332, 400, 332),     # card API Aberta
    ),
    r=30, w=5,
)

# 02 — o painel abriu, na aba Credencial. Etiquetas 1 e 2 na faixa da esquerda (apontam
# texto); 3 e 4 na da direita, porque o ícone de olho e o selo moram no canto direito.
painel(
    "02-painel-api-aberta.png",
    y0=0, y1=628,
    marcadores=(
        (1, 1184, 334, ESQ_PAINEL, 334),     # aba Credencial
        (2, 1218, 517, ESQ_PAINEL, 517),     # Client ID
        (3, 2098, 530, DIR_PAINEL, 530),     # ícone de olho (revela o Client Secret)
        (4, 2104, 435, DIR_PAINEL, 435),     # selo Ativa
    ),
)

# 03 — as permissões e os botões, do mesmo print. Segundo recorte da mesma pura: o painel
# tem 1950 px de altura e não cabe numa imagem legível.
painel(
    "02-painel-api-aberta.png",
    saida="03-permissoes-da-credencial.png",
    y0=628, y1=1800,
    marcadores=(
        (1, 1180, 717, ESQ_PAINEL, 717),      # Pedidos
        (2, 1180, 1032, ESQ_PAINEL, 1032),    # Loja
        (3, 1205, 1561, ESQ_PAINEL, 1561),    # SALVAR PERMISSÕES
        (4, 1465, 1652, DIR_PAINEL, 1652),    # RECICLAR (o que não se clica)
        (5, 1180, 1756, ESQ_PAINEL, 1756),    # CRIAR CREDENCIAL
    ),
)

# 04 — o diálogo da nova credencial.
dialogo(
    "04-nova-credencial.png",
    y0=380, y1=1580,
    marcadores=(
        (1, 748, 609, ESQ_DIALOGO, 609),      # Pedidos: consultar e alterar
        (2, 748, 923, ESQ_DIALOGO, 923),      # Loja: consultar
        (3, 1430, 1468, DIR_DIALOGO, 1468),   # CRIAR (F2)
    ),
)


# =====================================================================================
# Parte 2 — a integração, no Entregas Expressas (capturas do parceiro)
# =====================================================================================

annotate(
    "05-ee-cadastrar-integracao.png",
    marcadores=(
        (1, 879, 88, 879, 150),      # menu Configurações (seta de baixo para cima)
        (2, 950, 197, 800, 197),     # CADASTRAR INTEGRAÇÃO
    ),
    r=20, w=3,
)

# Os campos de Coleta, Forma de Pagamento e Tipo de Serviço ficam no pé desta captura, com a
# etiqueta já fora da imagem — eles aparecem inteiros na próxima, e é lá que o manual aponta.
annotate(
    "06-ee-colar-credencial.png",
    marcadores=(
        (1, 211, 634, 100, 610),     # Client ID
        (2, 1115, 634, 1240, 634),   # Client Secret (borda direita do campo)
        (3, 208, 664, 100, 700),     # Testar credencial
    ),
    r=20, w=3,
)

annotate(
    "07-ee-quando-vira-entrega.png",
    marcadores=(
        (1, 204, 507, 95, 507),      # quando a loja aceita o pedido
        (2, 201, 626, 95, 626),      # receber pedidos do iFood / da 99Food
        (3, 201, 699, 95, 699),      # exigir retorno só com dinheiro a devolver
        (4, 201, 751, 95, 760),      # atualizar o status do pedido na BeeFood
        (5, 770, 810, 880, 810),     # chamar entregador após X segundos
    ),
    r=20, w=3,
)


# =====================================================================================
# Parte 3 — o webhook, de volta no BeeFood
# =====================================================================================

painel(
    "08-aba-webhooks.png",
    y0=305, y1=638,
    marcadores=(
        (1, 1180, 418, ESQ_PAINEL, 418),      # NOVO WEBHOOK
    ),
)

dialogo(
    "09-novo-webhook.png",
    y0=470, y1=1520,
    marcadores=(
        (1, 729, 688, ESQ_DIALOGO, 688),      # URL (https)
        (2, 742, 804, ESQ_DIALOGO, 804),      # Eventos
        (3, 731, 1060, ESQ_DIALOGO, 1060),    # E-mail de contato
        (4, 728, 1122, ESQ_DIALOGO, 1122),    # Autenticação Basic
        (5, 1430, 1395, DIR_DIALOGO, 1395),   # SALVAR (F2)
    ),
)

painel(
    "10-webhook-ativo.png",
    y0=305, y1=1010,
    marcadores=(
        (1, 1225, 487, ESQ_PAINEL, 487),      # Secret do webhook
        (2, 1210, 592, ESQ_PAINEL, 592),      # JÁ GUARDEI
        (3, 2104, 830, DIR_PAINEL, 830),      # selo Ativo
        (4, 1216, 955, ESQ_PAINEL, 955),      # chave liga/desliga, EDITAR e EXCLUIR
    ),
)


# =====================================================================================
# Parte 4 — o pedido chegando (captura do parceiro)
# =====================================================================================

annotate(
    "11-ee-pedido-no-painel.png",
    marcadores=(
        (1, 191, 172, 95, 172),      # número do pedido no Entregas Expressas
        (2, 645, 269, 560, 269),     # valores e distância
        (3, 195, 466, 95, 466),      # Entregador: buscando
        (4, 193, 886, 95, 886),      # PEDIDO VIA BEEFOOD, canal e valor a receber
    ),
    r=20, w=3,
)
