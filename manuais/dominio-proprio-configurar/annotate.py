"""Anota os screenshots do #101 — Domínio próprio e subdomínio.

Coordenadas em pixels da imagem final (2160x1350). O painel do Domínio Próprio
abre à direita, então as etiquetas ficam na faixa escurecida da esquerda e as
setas entram na horizontal — assim nenhuma seta cruza texto do painel.
"""
import os
import math
from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
A_LINE = 235
A_BADGE = 245
FONT_CANDIDATES = [
    r"C:\Windows\Fonts\arialbd.ttf",
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


def annotate(name, markers=(), ring=(), crop=None, out_name=None, r=None, w=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    if crop:
        img = img.crop(crop)
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


def passthrough(name):
    """Imagem de contexto: entra no manual sem seta."""
    Image.open(os.path.join(SRC, name)).convert("RGB").save(os.path.join(OUT, name))
    print("OK (contexto)", name)


# --- 01 Aplicativos → Domínio Próprio ---------------------------------------
annotate("01-aplicativos-dominio.png",
         markers=[(1, 295, 599, 411, 599),
                  (2, 1968, 719, 2078, 719)])

# --- 02 Passo 1: escolher o cardápio ----------------------------------------
annotate("02-escolher-cardapio.png",
         markers=[(1, 1477, 352, 1477, 500)],
         ring=[(1187, 228, 2126, 340)])

# --- 03 Passo 2: os dois tipos (contexto — os dois cartões são o conteúdo) --
passthrough("03-escolher-tipo.png")

# --- 04 Passo 3: endereço conferido -----------------------------------------
annotate("04-endereco-conferido.png",
         markers=[(1, 1183, 300, 1065, 300),
                  (2, 1183, 454, 1065, 454),
                  (3, 1183, 626, 1065, 626),
                  (4, 1983, 939, 1983, 1044)])

# --- 05 Cadastrado: preparando os dados do DNS ------------------------------
annotate("05-cadastrado-preparando.png",
         markers=[(1, 1183, 802, 1065, 802)])

# --- 06 Instrução: trocar os servidores DNS ---------------------------------
annotate("06-instrucao-ns.png",
         markers=[(1, 1882, 783, 1065, 783),
                  (2, 1194, 960, 1065, 960),
                  (3, 1219, 1196, 1065, 1196)],
         ring=[(1202, 819, 2109, 1114)])

print("done")
