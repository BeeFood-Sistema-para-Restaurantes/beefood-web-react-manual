"""Anota os screenshots do #102 — Gerar Cardápio em PDF.

Coordenadas em pixels da imagem final. As capturas do sistema saem em
2160x1350 (1440x900 com device_scale 1.5) e vieram medidas pelo `caixa()` do
`capturar.py`. As imagens 11 e 12 são montagens feitas aqui a partir das
páginas do PDF já renderizadas em `imagens-puras/pdf-*.png`.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
CINZA_FUNDO = (238, 238, 240)
CINZA_TEXTO = (70, 70, 78)
BORDA = (200, 200, 206)
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


def annotate(name, markers=(), ring=(), crop=None, pad_right=0, pad_top=0, r=None, w=None,
             origem=None):
    img = Image.open(os.path.join(SRC, origem or name)).convert("RGBA")
    if crop:
        img = img.crop(crop)
    if pad_right or pad_top:
        base = Image.new("RGBA", (img.width + pad_right, img.height + pad_top), WHITE + (255,))
        base.paste(img, (0, pad_top))
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
        draw_arrow(d, bx + (r + 6) * math.cos(ang), by + (r + 6) * math.sin(ang), tx, ty, w)
        badge(d, bx, by, r, num, fnt)
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, name))
    print("OK", name, W, H)


def legenda(d, texto, cx, cy, tamanho=30):
    fnt = font(tamanho)
    bb = d.textbbox((0, 0), texto, font=fnt)
    d.text((cx - (bb[2] - bb[0]) / 2, cy), texto, fill=CINZA_TEXTO, font=fnt)


def montar(destino, paginas, escala=1.0, margem=90, gap=90, topo=78, baixo=100, tamanho=30):
    """Coloca páginas do PDF lado a lado num fundo cinza, com legenda em cima."""
    imagens = [Image.open(os.path.join(SRC, arq)).convert("RGB") for arq, _ in paginas]
    if escala != 1.0:
        imagens = [i.resize((round(i.width * escala), round(i.height * escala)), Image.LANCZOS)
                   for i in imagens]
    largura = margem * 2 + sum(i.width for i in imagens) + gap * (len(imagens) - 1)
    altura = topo + max(i.height for i in imagens) + baixo
    fundo = Image.new("RGB", (largura, altura), CINZA_FUNDO)
    d = ImageDraw.Draw(fundo)
    x = margem
    for imagem, (_, titulo) in zip(imagens, paginas):
        fundo.paste(imagem, (x, topo))
        d.rectangle([x, topo, x + imagem.width - 1, topo + imagem.height - 1], outline=BORDA, width=2)
        legenda(d, titulo, x + imagem.width // 2, topo - tamanho - 22, tamanho)
        x += imagem.width + gap
    fundo.save(os.path.join(SRC, destino))
    print("MONTOU", destino, fundo.size)


# --- 01 Menu lateral: Cardápio > Cardápio em PDF ----------------------------
annotate("01-menu-cardapio-pdf.png",
         markers=[(1, 155, 812, 155, 900)],
         ring=[(8, 752, 306, 806)])

# --- 02 Atalho no menu de ações da tela Cardápio ----------------------------
annotate("02-acoes-gerar-pdf.png",
         markers=[(1, 1820, 100, 1450, 100),
                  (2, 1568, 259, 1450, 259)],
         ring=[(1824, 70, 1884, 130), (1572, 233, 1872, 285)])

# --- 03 Etapa 1: cardápios, preço e seções ---------------------------------
annotate("03-etapa1-cardapios-itens.png",
         markers=[(1, 1224, 325, 1340, 325),
                  (2, 1224, 504, 1340, 504),
                  (3, 1228, 975, 1340, 975),
                  (4, 1584, 908, 1440, 908)],
         ring=[(336, 246, 1218, 405), (336, 474, 768, 534), (330, 712, 1222, 1238)])

# --- 04 Etapa 1: nome, descrição e preço só do impresso --------------------
annotate("04-etapa1-itens-editaveis.png",
         markers=[(1, 423, 986, 360, 986),
                  (2, 500, 958, 620, 911),
                  (3, 790, 958, 900, 911),
                  (4, 1070, 958, 1130, 911)],
         ring=[(427, 966, 467, 1006), (465, 956, 753, 1016),
               (757, 956, 1041, 1016), (1041, 956, 1197, 1016)],
         r=25)

# --- 05 Etapa 2: os cinco modelos ------------------------------------------
annotate("05-etapa2-modelos.png",
         markers=[(1, 1235, 620, 1420, 620)],
         ring=[(336, 396, 1221, 861)])

# --- 06/07 Etapa 2: recorte da coluna de ajustes + faixa branca à direita ---
# (crop tira a prévia e a lateral; dx=-316, dy=-160)
annotate("06-etapa2-pagina-fotos.png",
         crop=(316, 160, 1250, 1320), pad_right=140,
         markers=[(1, 908, 180, 984, 180),
                  (2, 908, 329, 984, 329),
                  (3, 908, 458, 984, 458),
                  (4, 892, 616, 984, 616),
                  (5, 426, 685, 500, 685),
                  (6, 744, 801, 818, 801)],
         ring=[(20, 125, 902, 236), (20, 299, 902, 359), (20, 428, 902, 488),
               (810, 592, 888, 640), (30, 652, 422, 718), (34, 770, 740, 832)],
         r=22, w=3)

annotate("07-etapa2-o-que-mostrar.png",
         crop=(316, 160, 1250, 1320), pad_right=140,
         markers=[(1, 892, 636, 984, 636),
                  (2, 892, 768, 984, 768),
                  (3, 892, 888, 984, 888),
                  (4, 892, 954, 984, 954),
                  (5, 892, 1020, 984, 1020)],
         ring=[(810, 612, 888, 660), (810, 744, 888, 792), (810, 864, 888, 912),
               (810, 930, 888, 978), (810, 996, 888, 1044)],
         r=22, w=3)

# --- 08 Etapa 3: marca, logo, QR Code e cores ------------------------------
annotate("08-etapa3-marca.png",
         markers=[(1, 1224, 380, 1340, 380),
                  (2, 1224, 640, 1340, 640),
                  (3, 1224, 896, 1340, 896),
                  (4, 1224, 1100, 1340, 1100),
                  (5, 1735, 1008, 1900, 1008)],
         ring=[(336, 285, 1218, 480), (336, 498, 1218, 796), (336, 866, 1218, 926),
               (330, 1020, 1222, 1195), (1652, 969, 1731, 1048)])

# --- 09 Etapa 3: capa ------------------------------------------------------
annotate("09-etapa3-capa.png",
         markers=[(1, 1210, 675, 1340, 675),
                  (2, 1060, 783, 1180, 783),
                  (3, 1210, 903, 1340, 903),
                  (4, 1010, 587, 1120, 587),
                  (5, 1760, 830, 1900, 790)],
         ring=[(1126, 651, 1204, 699), (350, 750, 1054, 816),
               (350, 867, 1204, 939), (330, 554, 1004, 620)])

# --- 10 Etapa 4: revisar e baixar ------------------------------------------
annotate("10-etapa4-revisar-baixar.png",
         markers=[(1, 1230, 300, 1340, 300),
                  (2, 1230, 405, 1340, 405),
                  (3, 1230, 483, 1340, 483)],
         ring=[(330, 240, 1224, 363), (330, 369, 1224, 441), (330, 447, 1224, 519)])

# --- 11 O PDF pronto: capa + página de itens -------------------------------
montar("11-pdf-pronto.png",
       [("pdf-capa.png", "Capa (página 1)"),
        ("pdf-pagina.png", "Página de itens (página 2)")])

annotate("11-pdf-pronto.png",
         markers=[(1, 475, 560, 390, 560),
                  (2, 856, 740, 940, 740),
                  (3, 595, 876, 670, 876),
                  (4, 1796, 160, 1880, 160),
                  (5, 1506, 248, 1590, 248),
                  (6, 1152, 310, 1120, 310),
                  (7, 1700, 1345, 1700, 1400)],
         ring=[(481, 521, 609, 649), (240, 668, 850, 813), (500, 832, 589, 921),
               (1154, 128, 1790, 193), (1154, 230, 1500, 267), (1148, 266, 1500, 363),
               (1154, 1310, 1940, 1338)],
         r=24, w=3)

# --- 12 Três modelos, mesmo cardápio --------------------------------------
montar("12-modelos.png",
       [("pdf-modelo-classico.png", "Clássico (fotos desligadas)"),
        ("pdf-modelo-fotografico.png", "Fotográfico"),
        ("pdf-modelo-quadro.png", "Quadro")],
       escala=0.62, margem=60, gap=60, topo=74, baixo=54, tamanho=26)

annotate("12-modelos.png")
