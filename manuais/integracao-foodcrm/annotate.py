"""Anota screenshots do manual Integracao FoodCRM.
Mesmo estilo dos demais manuais: setas finas/sutis em VERDE + badges numerados.
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
    """Copia uma imagem de CONTEXTO (sem setas) para imagens-tratadas/."""
    img = Image.open(os.path.join(SRC, name)).convert("RGB")
    img.save(os.path.join(OUT, name))
    print("OK (contexto)", name)


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


# ---------- FOODCRM ----------

# 01) Integracoes (menu) + botao "Acessar a documentacao"
annotate("01-foodcrm-integracoes.png", [
    (1, 0.037, 0.255, 0.140, 0.300),   # menu lateral Integracoes
    (2, 0.813, 0.141, 0.700, 0.230),   # botao Acessar a documentacao
])

# 02) Painel "API de integracao" -> API Key / Token + Copiar
annotate("02-foodcrm-api-token.png", [
    (1, 0.885, 0.224, 0.735, 0.300),   # campo API Key / Token
    (2, 0.978, 0.224, 0.900, 0.360),   # botao Copiar (token)
])

# ---------- BEEFOOD ----------

# 03) Aplicativos (menu) + card FoodCRM
annotate("03-beefood-aplicativos-card.png", [
    (1, 0.029, 0.292, 0.140, 0.340),   # menu lateral Aplicativos
    (2, 0.397, 0.220, 0.520, 0.300),   # card FoodCRM
])

# 04) Modal "Credenciais por Cardapio" -> status + botao Adicionar
annotate("04-beefood-modal-cardapios.png", [
    (1, 0.420, 0.524, 0.300, 0.460),   # status Nao configurado
    (2, 0.603, 0.512, 0.720, 0.575),   # botao + Adicionar
])

# 05) Modal de credencial -> API key + Ativo + SALVAR
annotate("05-beefood-modal-apikey.png", [
    (1, 0.493, 0.457, 0.350, 0.420),   # campo API key
    (2, 0.576, 0.545, 0.700, 0.560),   # switch Ativo
    (3, 0.555, 0.627, 0.680, 0.685),   # botao SALVAR (F2)
])

# 06) Integracao ativa (status Ativo + botao Editar)
annotate("06-beefood-ativo.png", [
    (1, 0.396, 0.524, 0.290, 0.460),   # status Ativo
    (2, 0.610, 0.512, 0.730, 0.575),   # botao Editar
])

print("done")
