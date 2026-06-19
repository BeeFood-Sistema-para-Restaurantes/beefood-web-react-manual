"""Anota screenshots do manual Reforma Tributaria (IBS/CBS).
Mesmo estilo do manual de caixa: setas finas/sutis em VERDE + badges numerados.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)
- alvo = ponta da seta (campo/botao)
- badge = posicao do circulo numerado (origem da seta)
"""
import os, math
from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
A_LINE = 220
A_BADGE = 235

FONT_PATH = r"C:\Windows\Fonts\arialbd.ttf"


def font(sz):
    return ImageFont.truetype(FONT_PATH, sz)


def draw_arrow(d, x0, y0, x1, y1, w):
    col = GREEN + (A_LINE,)
    d.line([(x0, y0), (x1, y1)], fill=col, width=w)
    ang = math.atan2(y1 - y0, x1 - x0)
    L = w * 3.6
    for s in (0.45, -0.45):
        xa = x1 - L * math.cos(ang - s)
        ya = y1 - L * math.sin(ang - s)
        d.line([(x1, y1), (xa, ya)], fill=col, width=w)


def badge(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], fill=WHITE + (235,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN + (A_BADGE,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    d.text((cx - tw / 2 - bb[0], cy - th / 2 - bb[1]), t, fill=WHITE, font=fnt)


def passthrough(name):
    """Copia uma imagem de CONTEXTO (sem setas) para imagens-tratadas/,
    para que TODAS as imagens usadas no manual fiquem em imagens-tratadas/."""
    img = Image.open(os.path.join(SRC, name)).convert("RGB")
    out = os.path.join(OUT, name)
    img.save(out)
    print("OK (contexto)", out)


def annotate(name, markers, ring=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    W, H = img.size
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = int(W * 0.0125)
    fnt = font(int(r * 1.2))
    w = max(2, int(W * 0.0022))
    for (fx, fy, fw, fh) in (ring or []):
        x0, y0 = fx * W, fy * H
        d.rectangle([x0, y0, x0 + fw * W, y0 + fh * H], outline=GREEN + (A_LINE,), width=w)
    for (num, tx, ty, bx, by) in markers:
        TX, TY = tx * W, ty * H
        BX, BY = bx * W, by * H
        ang = math.atan2(TY - BY, TX - BX)
        sx = BX + (r + 5) * math.cos(ang)
        sy = BY + (r + 5) * math.sin(ang)
        draw_arrow(d, sx, sy, TX, TY, w)
        badge(d, BX, BY, r, num, fnt)
    out_img = Image.alpha_composite(img, overlay).convert("RGB")
    out = os.path.join(OUT, name)
    out_img.save(out)
    print("OK", out)


# ---------- Configuracoes por imagem ----------

# Imagens de CONTEXTO (sem setas) -> copiadas para imagens-tratadas/
for _ctx in (
    "01-edicao-fiscal-grade.png",
    "02-grupos-colunas-ibscbs.png",
    "03-colunas-ibscbs-grade.png",
    "10-concluido.png",
):
    passthrough(_ctx)

# 04) Grade: produto marcado + botao EDITAR IMPOSTOS (coords reais via bbox)
annotate("04-produto-selecionado-editar-impostos.png", [
    (1, 0.112, 0.229, 0.210, 0.150),   # checkbox do produto
    (2, 0.942, 0.959, 0.840, 0.890),   # botao EDITAR IMPOSTOS (flutuante, canto inf. dir.)
])

# 07) Catalogo CST IBS/CBS carregado (dropdown)
annotate("07-cst-catalogo-carregado.png", [
    (1, 0.500, 0.200, 0.300, 0.170),   # campo de busca do CST
    (2, 0.430, 0.243, 0.300, 0.300),   # opcao "000 - Tributacao integral"
])

# 08) Modal preenchido (os 4 campos + PROXIMO)
annotate("08-modal-preenchido.png", [
    (1, 0.415, 0.646, 0.295, 0.646),   # CST IBS/CBS
    (2, 0.585, 0.646, 0.715, 0.620),   # cClassTrib
    (3, 0.585, 0.715, 0.715, 0.715),   # Aliq. IBS UF (%)
    (4, 0.585, 0.785, 0.715, 0.790),   # Aliq. CBS (%)
    (5, 0.630, 0.844, 0.730, 0.860),   # PROXIMO
])

# 09) Revisar alteracoes + CONFIRMAR
annotate("09-revisar-alteracoes.png", [
    (1, 0.420, 0.460, 0.300, 0.460),   # lista "Alteracoes a aplicar"
    (2, 0.627, 0.715, 0.730, 0.730),   # CONFIRMAR (F2)
])

print("done")
