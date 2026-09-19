"""Anota as capturas do #120 — setas verdes e números. Coordenadas em frações 0..1.

Cada marcador é `(número, x-alvo, y-alvo, x-badge, y-badge)`: a ponta da seta cai no
alvo e o número fica no lugar vazio mais próximo. `ring` desenha um retângulo verde
quando o alvo é um botão pequeno que não merece número próprio — é o caso do ⋮ do
cabeçalho do Delivery, que fica encostado no menu que ele abre e não sobra espaço para
badge nenhum sem cobrir o que interessa.
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

FONT_CANDIDATES = [
    r"C:\Windows\Fonts\arialbd.ttf",
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def font(sz):
    for caminho in FONT_CANDIDATES:
        if os.path.exists(caminho):
            return ImageFont.truetype(caminho, sz)
    raise RuntimeError("fonte bold nao encontrada")


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
    out_img.save(os.path.join(OUT, name))
    print("OK", name)


# O painel inteiro: a busca, as duas colunas e o que cada cartão conta.
# Toda ponta cai na **borda** do texto, nunca no meio dele: mirar no centro faz a linha
# atravessar a palavra e o print fica ilegível justamente no ponto que ele explica.
annotate("01-painel-completo.png", [
    (1, 0.365, 0.040, 0.560, 0.040),
    (2, 0.152, 0.112, 0.285, 0.112),
    (3, 0.607, 0.112, 0.755, 0.112),
    (4, 0.545, 0.512, 0.600, 0.640),
    (5, 0.648, 0.505, 0.775, 0.630),
    (6, 0.930, 0.478, 0.950, 0.610),
    (7, 0.128, 0.678, 0.240, 0.790),
])

# Abrir pela tela Delivery: o ⋮ do cabeçalho ganha moldura, o item do menu ganha o número.
annotate("02-abrir-pela-tela-delivery.png", [
    (1, 0.900, 0.243, 0.960, 0.345),
], ring=[(0.927, 0.058, 0.032, 0.050)])

# Abrir por /aplicativos: a janela de apresentação e o botão que abre o painel.
annotate("03-abrir-por-aplicativos.png", [
    (1, 0.752, 0.262, 0.880, 0.262),
    (2, 0.756, 0.897, 0.878, 0.940),
])

# O cartão clicado: cabeçalho com o canal, cliente, itens e total.
annotate("04-detalhe-do-pedido.png", [
    (1, 0.292, 0.112, 0.180, 0.085),
    (2, 0.262, 0.228, 0.155, 0.250),
    (3, 0.258, 0.318, 0.150, 0.375),
    (4, 0.755, 0.520, 0.870, 0.555),
])

print("done")
