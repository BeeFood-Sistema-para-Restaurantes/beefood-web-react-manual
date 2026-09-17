"""Anota os screenshots do #103 — Venda Sugestiva (UpSell).

Capturas do painel saem em 2160x1350 (1440x900 com device_scale 1.5) e as
coordenadas dos marcadores estão em **pixels** dessas imagens, medidas com a
grade de `/tmp/grade103.py`.

As telas do cardápio público saem em 780x1688 (390x844 com DPR 2) e entram no
manual como **tira de celulares** (`montar_celulares`), padrão do #19/#20/#64:
as puras individuais são só a fonte, no `.md` vai apenas a tira.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
FUNDO_TIRA = (244, 244, 245)
A_LINE = 235
A_BADGE = 245
FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]

PHONE_W = 380
GAP = 18
PAD = 22
CAP_H = 44


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


def annotate(name, markers=(), ring=(), r=None, w=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
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
        draw_arrow(d, bx + (r + 6) * math.cos(ang), by + (r + 6) * math.sin(ang), tx, ty, w)
        badge(d, bx, by, r, num, fnt)
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, name))
    print("OK", name, W, H)


def montar_celulares(destino, paineis):
    """Junta prints de celular lado a lado. paineis: [(arquivo, titulo)]."""
    fnt = font(22)
    phones = []
    for arquivo, _ in paineis:
        im = Image.open(os.path.join(SRC, arquivo)).convert("RGB")
        h = int(im.height * PHONE_W / im.width)
        phones.append(im.resize((PHONE_W, h), Image.Resampling.LANCZOS))
    ph_h = phones[0].height
    n = len(phones)
    W = PAD * 2 + n * PHONE_W + (n - 1) * GAP
    H = PAD + CAP_H + ph_h + PAD
    canvas = Image.new("RGB", (W, H), FUNDO_TIRA)
    d = ImageDraw.Draw(canvas)
    for i, (im, (_, titulo)) in enumerate(zip(phones, paineis)):
        x = PAD + i * (PHONE_W + GAP)
        y = PAD + CAP_H
        bb = d.textbbox((0, 0), titulo, font=fnt)
        d.text((x + (PHONE_W - (bb[2] - bb[0])) / 2, PAD + 12), titulo, fill=(40, 40, 40), font=fnt)
        mask = Image.new("L", (PHONE_W, ph_h), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, PHONE_W - 1, ph_h - 1], radius=26, fill=255)
        canvas.paste(im, (x, y), mask)
        d.rounded_rectangle([x, y, x + PHONE_W - 1, y + ph_h - 1], radius=26,
                            outline=(200, 200, 200), width=2)
    canvas.save(os.path.join(SRC, destino))
    print("MONTOU", destino, canvas.size)
    return ph_h


def no_celular(i, tx, ty, ph_h):
    """Fração dentro do aparelho `i` da tira -> pixel da tira."""
    return PAD + i * (PHONE_W + GAP) + tx * PHONE_W, PAD + CAP_H + ty * ph_h


def passthrough(name):
    Image.open(os.path.join(SRC, name)).convert("RGB").save(os.path.join(OUT, name))
    print("CTX", name)


# --- 01 Três pontinhos da tela Cardápio -------------------------------------
annotate("01-menu-acoes.png",
         markers=[(1, 1836, 99, 1500, 99),
                  (2, 1596, 320, 1420, 320)],
         ring=[(1826, 76, 1876, 122), (1568, 288, 1868, 356)])

# --- 02 Janela geral (lista de produtos) ------------------------------------
annotate("02-janela-geral.png",
         markers=[(1, 552, 266, 400, 266),
                  (2, 1032, 244, 1148, 142),
                  (3, 1628, 266, 1790, 266),
                  (4, 956, 350, 1150, 350),
                  (5, 596, 426, 430, 426),
                  (6, 1620, 601, 1780, 601)],
         ring=[(536, 240, 1000, 296), (1020, 240, 1204, 296), (1330, 240, 1620, 296),
               (852, 332, 950, 366)])

# --- 03a Janela de escolha ainda vazia (contexto) ---------------------------
passthrough("03a-janela-vazia.png")

# --- 03 Janela de escolha com 4 marcados ------------------------------------
annotate("03-janela-escolha.png",
         markers=[(1, 545, 544, 380, 544),
                  (2, 532, 325, 396, 325),
                  (3, 1640, 247, 1790, 247),
                  (4, 1626, 1192, 1800, 1192)],
         ring=[(534, 528, 566, 560), (536, 300, 862, 352), (1160, 1168, 1620, 1218)])

# --- 03b Aviso de salvo (contexto) ------------------------------------------
annotate("03b-toast-salvo.png",
         markers=[(1, 1700, 110, 1450, 240)],
         ring=[(1548, 40, 2140, 148)])

# --- 04 Três pontinhos do produto -------------------------------------------
annotate("04-menu-produto.png",
         markers=[(1, 1356, 506, 1160, 506),
                  (2, 1298, 852, 1510, 962)],
         ring=[(1344, 484, 1382, 528), (1040, 838, 1300, 890)])

# --- 05 Aba Venda Sugestiva no cadastro do produto --------------------------
annotate("05-aba-cadastro.png",
         markers=[(1, 1500, 176, 1500, 112),
                  (2, 1816, 295, 1890, 348),
                  (3, 362, 424, 240, 424),
                  (4, 382, 630, 240, 630)],
         ring=[(1400, 180, 1600, 232), (1610, 278, 1810, 312), (366, 392, 1560, 460)])

# --- 06 Limite de 6 -------------------------------------------------------
annotate("06-limite.png",
         markers=[(1, 1144, 247, 880, 247),
                  (2, 545, 544, 400, 544)],
         ring=[(1150, 228, 1630, 268), (534, 528, 566, 560)])

# --- 07 Cardápio digital delivery (tira de 3 celulares) ---------------------
ph = montar_celulares("07-delivery.png", [
    ("07-delivery-sugestao.png", "1. A sugestão aparece"),
    ("07-delivery-produto-sugerido.png", "2. O produto sugerido abre"),
    ("07-delivery-sacola.png", "3. Os dois na sacola"),
])
p0 = lambda tx, ty: no_celular(0, tx, ty, ph)
p1 = lambda tx, ty: no_celular(1, tx, ty, ph)
p2 = lambda tx, ty: no_celular(2, tx, ty, ph)
annotate("07-delivery.png",
         markers=[(1, *p0(0.36, 0.268), *p0(0.74, 0.222)),
                  (2, *p0(0.50, 0.912), *p0(0.50, 0.848)),
                  (3, *p1(0.60, 0.930), *p1(0.60, 0.868)),
                  (4, *p2(0.280, 0.355), *p2(0.86, 0.445)),
                  (5, *p2(0.655, 0.872), *p2(0.34, 0.815))],
         r=16, w=3)

# --- 08 Cardápio digital presencial (tira de 2 celulares) -------------------
ph = montar_celulares("08-presencial.png", [
    ("08-presencial-sugestao.png", "Mesma janela no presencial"),
    ("08-presencial-sacola.png", "Sacola do presencial"),
])
q0 = lambda tx, ty: no_celular(0, tx, ty, ph)
q1 = lambda tx, ty: no_celular(1, tx, ty, ph)
annotate("08-presencial.png",
         markers=[(1, *q0(0.255, 0.388), *q0(0.60, 0.388)),
                  (2, *q1(0.700, 0.905), *q1(0.34, 0.845))],
         r=14, w=3)

# --- 09 Relatório: Desempenho > Delivery > Sugestões ------------------------
annotate("09-relatorio-delivery.png",
         markers=[(1, 212, 745, 300, 745),
                  (2, 648, 662, 780, 662),
                  (3, 624, 906, 760, 906),
                  (4, 600, 112, 720, 112),
                  (5, 940, 380, 1060, 300),
                  (6, 1991, 240, 1991, 320)],
         ring=[(20, 722, 250, 768), (336, 640, 640, 684), (348, 884, 616, 928),
               (352, 84, 640, 142), (722, 300, 2110, 480), (1866, 186, 2116, 240)])

# --- 09b Mais sugeridos (contexto) -----------------------------------------
passthrough("09-relatorio-delivery-listas.png")

# --- 10 Mesmo relatório em Presencial --------------------------------------
annotate("10-relatorio-presencial.png",
         markers=[(1, 648, 716, 780, 716),
                  (2, 624, 894, 760, 894)],
         ring=[(336, 694, 640, 738), (348, 872, 616, 916)])
