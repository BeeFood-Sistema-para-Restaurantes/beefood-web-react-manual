"""Anota os screenshots do #101 — Domínio próprio e subdomínio.

Coordenadas sempre em pixels da **captura pura** (2160x1350), inclusive nas
imagens recortadas — a função converte.

O Domínio Próprio abre num painel lateral que começa em x=1154 e vai até a borda
direita: os 1154 px da esquerda são a tela escurecida, sem uso. Toda imagem desse
painel é recortada em `PAINEL` e ganha uma faixa branca de `MARGEM` px à esquerda,
onde ficam as etiquetas — assim nenhuma seta cruza texto e nada de espaço morto
entra no manual.
"""
import os
import math
from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

PAINEL = (1154, 0, 2160, 1350)   # painel lateral do Domínio Próprio
MARGEM = 150                     # faixa branca à esquerda, para as etiquetas
RAIO = 27                        # etiqueta do tamanho da captura inteira (2160 px)
TRACO = 4

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


def preparar(name, crop, pad_left):
    """Recorta e devolve a imagem já com a faixa branca, mais o deslocamento (dx, dy)."""
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    dx = dy = 0
    if crop:
        img = img.crop(crop)
        dx, dy = -crop[0], -crop[1]
    if pad_left:
        base = Image.new("RGBA", (img.width + pad_left, img.height), WHITE + (255,))
        base.paste(img, (pad_left, 0))
        img = base
        dx += pad_left
    return img, dx, dy


def annotate(name, markers=(), ring=(), crop=None, pad_left=0, out_name=None,
             r=None, w=None):
    img, dx, dy = preparar(name, crop, pad_left)
    W, H = img.size
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = r or int(W * 0.0125)
    fnt = font(int(r * 1.25))
    w = w or max(2, int(W * 0.0022))
    for (x0, y0, x1, y1) in ring:
        d.rounded_rectangle([x0 + dx, y0 + dy, x1 + dx, y1 + dy], radius=int(r * 0.6),
                            outline=GREEN + (A_LINE,), width=w)
    for (num, tx, ty, bx, by) in markers:
        tx, bx = tx + dx, bx + dx
        ty, by = ty + dy, by + dy
        ang = math.atan2(ty - by, tx - bx)
        draw_arrow(d, bx + (r + 6) * math.cos(ang), by + (r + 6) * math.sin(ang),
                   tx, ty, w)
        badge(d, bx, by, r, num, fnt)
    Image.alpha_composite(img, overlay).convert("RGB").save(
        os.path.join(OUT, out_name or name))
    print("OK", out_name or name, W, H)


def passthrough(name, crop=None):
    """Imagem de contexto: entra no manual sem seta (mas recortada igual às outras)."""
    img, _, _ = preparar(name, crop, 0)
    img.convert("RGB").save(os.path.join(OUT, name))
    print("OK (contexto)", name, img.size[0], img.size[1])


def ate(fim: int):
    """Painel cortado na altura `fim` — corta o branco sobrando embaixo."""
    return (PAINEL[0], PAINEL[1], PAINEL[2], fim)


def painel(name, markers=(), ring=(), crop=PAINEL, **kw):
    """Atalho para as imagens do painel lateral."""
    annotate(name, markers=markers, ring=ring, crop=crop, pad_left=MARGEM,
             r=RAIO, w=TRACO, **kw)


# --- 01 Aplicativos → Domínio Próprio (tela inteira, sem recorte) -----------
annotate("01-aplicativos-dominio.png",
         markers=[(1, 295, 599, 411, 599),
                  (2, 1968, 719, 2078, 719)])

# --- 02 Passo 1: escolher o cardápio ----------------------------------------
painel("02-escolher-cardapio.png",
       markers=[(1, 1190, 284, 1065, 284)],
       ring=[(1187, 228, 2126, 340)],
       crop=ate(440))

# --- 03 Passo 2: os dois tipos (contexto — os dois cartões são o conteúdo) --
passthrough("03-escolher-tipo.png", crop=ate(760))

# --- 04 Passo 3: endereço conferido -----------------------------------------
painel("04-endereco-conferido.png",
       markers=[(1, 1183, 300, 1065, 300),
                (2, 1183, 454, 1065, 454),
                (3, 1183, 626, 1065, 626),
                (4, 1983, 939, 1983, 1044)],
       crop=ate(1130))

# --- 05 Cadastrado: preparando os dados do DNS ------------------------------
painel("05-cadastrado-preparando.png",
       markers=[(1, 1183, 802, 1065, 802)],
       crop=ate(1080))

# --- 06 Instrução: trocar os servidores DNS ---------------------------------
painel("06-instrucao-ns.png",
       markers=[(1, 1882, 783, 1065, 783),
                (2, 1194, 960, 1065, 960),
                (3, 1219, 1196, 1065, 1196)],
       ring=[(1202, 819, 2109, 1114)])

# --- 07 Domínio no ar -------------------------------------------------------
painel("07-dominio-no-ar.png",
       markers=[(1, 1187, 270, 1065, 270),
                (2, 1187, 395, 1065, 395),
                (3, 1190, 600, 1065, 600)])

# --- 11 Rodapé do painel: o botão de excluir (recorte da mesma captura do No ar) --
annotate("07-dominio-no-ar.png", out_name="11-excluir-botao.png",
         markers=[(1, 1900, 1310, 1660, 1310)],
         crop=(1154, 1262, 2160, 1350), pad_left=0, r=RAIO, w=TRACO)

# --- 12 Confirmação da exclusão (diálogo no centro da tela) -----------------
annotate("12-confirmar-exclusao.png",
         markers=[(1, 705, 593, 620, 593),
                  (2, 1358, 782, 1358, 872)],
         crop=(680, 470, 1500, 920), pad_left=MARGEM, r=RAIO, w=TRACO)

print("done")
