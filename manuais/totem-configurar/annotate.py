"""Anota os screenshots do #121 — Totem de Autoatendimento: pôr no ar e configurar.

Coordenadas em pixels **da imagem já recortada** (o recorte é aplicado antes das
setas). Cada seta sai de um espaço vazio e mira a borda do elemento, nunca o meio
do texto.

Dois padrões de recorte aqui:

- **Painel** (2160x1350): o modal do totem ocupa o centro e sobra tela escurecida
  dos dois lados. O recorte pega o modal e cola uma faixa branca à esquerda, que é
  onde ficam as etiquetas numeradas.
- **Totem** (1080x1920): a barra de cima do aparelho desenha o logotipo da loja
  dentro de um espaço quadrado, e o nosso logotipo é retangular (350x112) — ele sai
  cortado. Onde essa barra não ensina nada, o recorte a deixa de fora.
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
             r=None, w=None, out_name=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    if crop:
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


# Recorte do modal do totem no painel: o modal vai de x=410 a x=1750 e de y=95 a
# y=1245 na captura de 2160x1350. A faixa branca de 150 px à esquerda recebe as
# etiquetas.
MODAL = dict(crop=(410, 95, 1755, 1250), pad_left=150, r=27, w=4)
# O aparelho sem a barra de cima (o logotipo retangular sai cortado nela).
TOTEM_SEM_BARRA = dict(crop=(0, 52, 1080, 1920), r=17, w=3)

# --- 01 Aplicativos: onde mora o card do totem ------------------------------
annotate("01-aplicativos-card-totem.png",
         crop=(312, 520, 2135, 1000), pad_top=110, r=24, w=4,
         markers=[(1, 1002 - 312, 745 - 520 + 110, 700, 55)],
         ring=[(995 - 312, 742 - 520 + 110, 1478 - 312, 848 - 520 + 110)])

# --- 02 Aba Configuração, topo ---------------------------------------------
annotate("02-modal-configuracao-topo.png",
         markers=[(1, 1215, 100, 1050, 100),
                  (2, 213, 176, 70, 176),
                  (3, 215, 330, 70, 330),
                  (4, 860, 268, 700, 305)],
         **MODAL)

# --- 03 Aba Configuração, meio --------------------------------------------
annotate("03-modal-configuracao-meio.png",
         markers=[(1, 200, 262, 70, 262),
                  (2, 1120, 248, 1295, 300),
                  (3, 215, 563, 70, 563),
                  (4, 872, 583, 700, 470),
                  (5, 872, 698, 700, 800)],
         **MODAL)

# --- 04 Aba Configuração, fim ---------------------------------------------
annotate("04-modal-configuracao-fim.png",
         markers=[(1, 200, 426, 70, 426),
                  (2, 200, 633, 70, 633),
                  (3, 200, 847, 70, 847)],
         **MODAL)

# --- 05 Aba Pagamentos -----------------------------------------------------
annotate("05-modal-pagamentos.png",
         markers=[(1, 200, 292, 70, 292),
                  (2, 210, 350, 70, 420),
                  (3, 1406, 653, 1406, 810)],
         **MODAL)

# --- 06 Totem: a tela de pagamento ----------------------------------------
annotate("06-totem-pagamento.png",
         markers=[(1, 425, 120, 215, 120),
                  (2, 277, 770, 277, 900),
                  (3, 800, 770, 720, 900)],
         crop=(0, 88, 1080, 1100), r=17, w=3)

# --- 07 Aba Aparência ------------------------------------------------------
annotate("07-modal-aparencia.png",
         markers=[(1, 200, 300, 70, 300),
                  (2, 213, 620, 70, 620),
                  (3, 680, 848, 680, 935),
                  (4, 1205, 976, 1080, 1080)],
         **MODAL)

# --- 08 Totem: tela de espera ---------------------------------------------
annotate("08-totem-espera.png", r=17, w=3,
         markers=[(1, 540, 800, 540, 690),
                  (2, 440, 1100, 250, 1100)])

# --- 09 Aba Download -------------------------------------------------------
annotate("09-modal-download.png",
         markers=[(1, 350, 380, 70, 380),
                  (2, 1300, 370, 1395, 300),
                  (3, 347, 641, 70, 641)],
         **MODAL)

# --- 10 Totem: coluna de setores SEM foto ---------------------------------
annotate("10-totem-cardapio-sem-foto-setor.png", r=17, w=3,
         markers=[(1, 120, 800, 120, 950)])

# --- 11 Painel: o cadastro do setor ---------------------------------------
annotate("11-painel-setor-foto.png", crop=(500, 80, 1660, 1270), pad_left=150,
         r=25, w=4,
         markers=[(1, 225, 523, 70, 523),
                  (2, 495, 779, 70, 779),
                  (3, 1150, 1020, 1150, 930)])

# --- 12 Painel: o banco de imagens ----------------------------------------
annotate("12-painel-foto-setor-banco.png", crop=(200, 180, 1950, 1130),
         pad_top=110, r=25, w=4,
         markers=[(1, 440, 500, 300, 330),
                  (2, 1400, 205, 1400, 55),
                  (3, 1500, 990, 1330, 940)])

# --- 13 Totem: coluna de setores COM foto ---------------------------------
annotate("13-totem-cardapio-com-foto-setor.png", r=17, w=3,
         markers=[(1, 120, 1450, 120, 1600)])

# --- 14 Totem: pedido feito (mensagem final + senha) ----------------------
annotate("14-totem-pedido-feito.png", crop=(0, 665, 1080, 1500), r=17, w=3,
         markers=[(1, 655, 185, 850, 185),
                  (2, 724, 419, 900, 445),
                  (3, 352, 576, 180, 576)])
