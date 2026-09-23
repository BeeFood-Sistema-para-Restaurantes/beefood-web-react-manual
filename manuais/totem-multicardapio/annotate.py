"""Anota os screenshots do #124 — Mais de um cardápio no totem.

Coordenadas em pixels **da imagem já recortada** (o recorte é aplicado antes das
setas). Cada seta mira a borda do elemento, nunca o meio do texto.

Três padrões de recorte aqui:

- **Painel** (2160x1350): o modal do totem ocupa o centro e sobra tela escurecida
  dos dois lados; o recorte pega o modal e cola uma faixa branca à esquerda, que é
  onde ficam as etiquetas numeradas.
- **Aparelho** (1080x1920): a tela é estreita e cheia, então a etiqueta também vai
  para uma faixa branca à esquerda (`pad_left`) e a seta entra na horizontal.
- **Aparelho em duas partes** (`crops`): a sacola tem os itens no alto e o total no
  pé, com meia tela vazia no meio. As duas partes entram empilhadas, com um risco
  cinza no lugar do corte, para o leitor saber que é a mesma tela.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
CINZA = (196, 196, 200)
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


def empilhar(img, crops, risco=10):
    """Duas faixas da mesma tela, uma sobre a outra, com o corte visível."""
    partes = [img.crop(c) for c in crops]
    larg = max(p.width for p in partes)
    alt = sum(p.height for p in partes) + risco * (len(partes) - 1)
    base = Image.new("RGBA", (larg, alt), WHITE + (255,))
    y = 0
    for i, p in enumerate(partes):
        base.paste(p, (0, y))
        y += p.height
        if i < len(partes) - 1:
            ImageDraw.Draw(base).rectangle([0, y, larg, y + risco - 1],
                                           fill=CINZA + (255,))
            y += risco
    return base


def annotate(name, markers=(), ring=(), crop=None, crops=None, pad_left=0, pad_top=0,
             r=None, w=None, out_name=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    if crops:
        img = empilhar(img, crops)
    elif crop:
        img = img.crop(crop)
    if pad_left or pad_top:
        base = Image.new("RGBA", (img.width + pad_left, img.height + pad_top),
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


# O aparelho inteiro, com faixa branca à esquerda (a tela não tem espaço vazio).
TOTEM = dict(pad_left=150, r=17, w=3)

# --- 01 Painel: a aba Cardápios -------------------------------------------
# A aba tem duas linhas e para: o corte em 760 tira o vão vazio até o rodapé do
# modal. Sem faixa branca, porque as três etiquetas cabem dentro do modal.
annotate("01-modal-cardapios-chave.png", crop=(410, 95, 1755, 760), r=27, w=4,
         markers=[(1, 603, 158, 640, 112),
                  (2, 1246, 335, 1246, 296),
                  (3, 1250, 505, 1282, 562)])

# --- 02 Aparelho: a tela Escolha um cardápio ------------------------------
annotate("02-totem-escolha-cardapio.png", crop=(0, 0, 1080, 780), r=17, w=3,
         markers=[(1, 350, 170, 350, 116),
                  (2, 152, 430, 78, 430),
                  (3, 152, 612, 78, 612),
                  (4, 1015, 98, 1015, 168)])

# --- 03 Aparelho: os dois cardápios na mesma tela -------------------------
annotate("03-totem-todos-cardapios.png",
         markers=[(1, 765, 455, 935, 455),
                  (2, 1123, 478, 1140, 530),
                  (3, 205, 630, 75, 630),
                  (4, 205, 805, 75, 805)],
         **TOTEM)

# --- 04 Aparelho: só o cardápio adicional ---------------------------------
annotate("04-totem-cardapio-adicional.png",
         markers=[(1, 845, 432, 1006, 432),
                  (2, 1128, 470, 1140, 524)],
         **TOTEM)

# --- 05 Aparelho: a sacola com item dos dois cardápios --------------------
annotate("05-totem-sacola-mista.png",
         crops=[(0, 0, 1080, 630), (0, 1700, 1080, 1920)],
         markers=[(1, 360, 135, 75, 135),
                  (2, 360, 404, 75, 404),
                  (3, 1052, 690, 800, 690)],
         **TOTEM)

# --- 06 Painel: o pedido misto --------------------------------------------
# A origem "AutoAtendimento" fica no alto da ficha, mas é assunto do #123: aqui a
# lição são os dois itens na MESMA venda, e a seta nela só disputava espaço com a
# linha do tempo do pedido.
annotate("06-painel-pedido-misto.png", crop=(320, 60, 2160, 1270), pad_top=110,
         r=26, w=4,
         markers=[(1, 821, 200, 821, 55),
                  (2, 470, 1025, 640, 1075),
                  (3, 1120, 946, 880, 925),
                  (4, 1120, 1009, 880, 1030),
                  (5, 1645, 1227, 1440, 1270)])

# --- 07 Painel: trocar de cardápio para cadastrar -------------------------
# O corte em 882 fica entre o nome da loja e o identificador dela, para a imagem
# não terminar no meio de uma linha de texto.
annotate("07-painel-editando-cardapio.png", crop=(300, 0, 2160, 882), r=26, w=4,
         markers=[(1, 1758, 133, 1758, 196),
                  (2, 300, 180, 620, 180)])
