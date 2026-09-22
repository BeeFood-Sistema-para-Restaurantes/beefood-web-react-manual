"""Anota os screenshots do #123 — O pedido do totem no painel.

Coordenadas em pixels **da imagem já recortada** (o recorte entra antes das
setas). Cada seta sai de um espaço vazio e mira a borda do elemento.

Três padrões de recorte:

- **Página do painel**: sai a barra de cima (o "Indique e ganhe!") e entra uma
  faixa branca no alto, onde ficam as etiquetas do menu lateral.
- **Painel lateral** (a ficha da venda e os Filtros de Histórico): recorta no
  painel e cola faixa branca do lado de onde a seta vem — à direita quando o
  alvo está no fim da linha, à esquerda quando está no começo.
- **Totem** (1080x1920): sai a barra de cima, onde o logotipo retangular da loja
  aparece cortado dentro de um espaço quadrado.

As capturas `01-totem-pagamento.png` e `03-totem-pedido-feito.png` ficam só como
backup: as duas telas são documentadas no #121, e aqui o manual usa apenas o
aviso do pagamento em dinheiro.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
A_LINE = 235
A_BADGE = 245
FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def font(sz):
    for caminho in FONT_CANDIDATES:
        if os.path.exists(caminho):
            return ImageFont.truetype(caminho, sz)
    raise RuntimeError("nenhuma fonte bold encontrada")


def draw_arrow(d, x0, y0, x1, y1, w):
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


def annotate(name, markers=(), ring=(), crop=None, pad_left=0, pad_top=0,
             pad_right=0, r=None, w=None, out_name=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    if crop:
        img = img.crop(crop)
    if pad_left or pad_top or pad_right:
        base = Image.new("RGBA",
                         (img.width + pad_left + pad_right, img.height + pad_top),
                         WHITE + (255,))
        base.paste(img, (pad_left, pad_top))
        img = base
    W, H = img.size
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = r or int(W * 0.0125)
    fnt = font(int(r * 1.25))
    w = w or max(2, int(W * 0.0022))
    for (x0, y0, x1, y1) in ring:
        d.rounded_rectangle([x0, y0, x1, y1], radius=int(r * 0.6),
                            outline=GREEN + (A_LINE,), width=w)
    for (num, tx, ty, bx, by) in markers:
        ang = math.atan2(ty - by, tx - bx)
        draw_arrow(d, bx + (r + 6) * math.cos(ang), by + (r + 6) * math.sin(ang),
                   tx, ty, w)
        badge(d, bx, by, r, num, fnt)
    Image.alpha_composite(img, overlay).convert("RGB").save(
        os.path.join(OUT, out_name or name))
    print("OK", out_name or name, W, H)


# Página do painel sem a barra de cima, com faixa branca no alto.
PAGINA = dict(crop=(0, 86, 2160, 1290), pad_top=110, r=27, w=4)
# A mesma coisa, indo até o pé da página (o rodapé da tabela de vendas).
PAGINA_ALTA = dict(crop=(0, 86, 2160, 1330), pad_top=110, r=27, w=4)

# --- 02 Totem: o aviso do pagamento em dinheiro ----------------------------
annotate("02-totem-dinheiro.png", crop=(0, 88, 1080, 1300), r=17, w=3,
         markers=[(1, 175, 792, 60, 792),
                  (2, 200, 917, 60, 917),
                  (3, 500, 1056, 300, 1056)])

# --- 04 Delivery: o pedido do totem na coluna Aguardando -------------------
annotate("04-painel-delivery-pedido-totem.png",
         markers=[(1, 1220, 187, 1360, 129),
                  (2, 560, 649, 560, 774),
                  (3, 790, 454, 950, 454)],
         **PAGINA)

# --- 05 A ficha da venda: origem AutoAtendimento e o pagamento no caixa ----
# Painel lateral de x=1345 a x=2160 e de y=200 a y=1290; a faixa de 160 px à
# direita recebe as etiquetas, porque os valores ficam no fim de cada linha.
annotate("05-painel-pedido-detalhe.png",
         crop=(1345, 200, 2160, 1350), pad_right=160, r=27, w=4,
         markers=[(1, 780, 215, 890, 215),
                  (2, 670, 828, 890, 828),
                  (3, 760, 983, 890, 983),
                  (4, 780, 1110, 890, 1110)])

# --- 06 Histórico de Vendas: o filtro de origem ----------------------------
annotate("06-painel-historico-filtro-origem.png",
         crop=(1480, 0, 2160, 1350), pad_left=150, r=27, w=4,
         markers=[(1, 195, 348, 70, 348),
                  (2, 730, 828, 730, 930),
                  (3, 195, 1210, 70, 1210)])

# --- 07 Histórico de Vendas: a lista só com as vendas do totem ------------
annotate("07-painel-historico-lista-totem.png",
         markers=[(1, 755, 167, 900, 167),
                  (2, 520, 538, 520, 674),
                  (3, 875, 1317, 1010, 1317)],
         **PAGINA_ALTA)

# --- 08 Desempenho: onde se filtra por origem -----------------------------
annotate("08-painel-desempenho-origem.png",
         markers=[(1, 295, 769, 295, 55),
                  (2, 1250, 366, 1450, 404)],
         **PAGINA)

# --- 09 Desempenho: o que o totem vendeu ----------------------------------
annotate("09-painel-desempenho-autoatendimento.png",
         markers=[(1, 1250, 366, 1450, 404),
                  (2, 915, 601, 1250, 601),
                  (3, 1085, 688, 1300, 688),
                  (4, 1210, 866, 1390, 866)],
         **PAGINA)
