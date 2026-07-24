"""Anota screenshots do manual Integracao Repediu.
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


# ---------- Imagens de CONTEXTO (sem setas) ----------
passthrough("08-beefood-form-configurar.png")

# ---------- REPEDIU ----------

# 01) Integracoes -> card BeeFood -> botao Habilitado
annotate("01-repediu-integracoes-beefood.png", [
    (1, 0.275, 0.394, 0.190, 0.330),   # botao Habilitado (verde)
])

# 02) Painel de credenciais (Tracker de Vendas)
annotate("02-repediu-credenciais-vendas.png", [
    (1, 0.700, 0.209, 0.585, 0.150),   # campo Codigo da empresa (client_id)
    (2, 0.700, 0.248, 0.585, 0.320),   # campo Chave da empresa (client_secret)
])

# 03) Web/App Analytics -> Configuracao -> card BeeFood -> Habilitar
annotate("03-repediu-analytics-cards.png", [
    (1, 0.511, 0.279, 0.610, 0.360),   # botao Habilitar (card BeeFood)
])

# 04) Modal Chave de escrita -> Gerar chave
annotate("04-repediu-writekey-gerar.png", [
    (1, 0.655, 0.132, 0.600, 0.235),   # botao Gerar chave
])

# 05) Write Key gerada + Copiar
annotate("05-repediu-writekey-gerada.png", [
    (1, 0.720, 0.158, 0.600, 0.115),   # campo Write key
    (2, 0.945, 0.158, 0.860, 0.095),   # botao Copiar
])

# ---------- BEEFOOD ----------

# 06) Aplicativos -> card Repediu
annotate("06-beefood-aplicativos-repediu.png", [
    (1, 0.075, 0.289, 0.185, 0.235),   # menu lateral Aplicativos
    (2, 0.300, 0.218, 0.430, 0.300),   # card Repediu
])

# 07) Modal status -> Configurar
annotate("07-beefood-repediu-modal-status.png", [
    (1, 0.410, 0.512, 0.300, 0.455),   # status Tracker de Vendas inativo
    (2, 0.659, 0.514, 0.780, 0.575),   # botao Configurar
])

# 09) Formulario preenchido + SALVAR
annotate("09-beefood-form-preenchido.png", [
    (1, 0.420, 0.448, 0.300, 0.430),   # Client ID
    (2, 0.420, 0.513, 0.300, 0.560),   # Client Secret
    (3, 0.420, 0.675, 0.300, 0.660),   # Chave do tracker (Write Key)
    (4, 0.545, 0.759, 0.665, 0.800),   # SALVAR (F2)
])

# 10) Integracao ativa (dois trackers ativos)
annotate("10-beefood-repediu-ativo.png", [
    (1, 0.410, 0.512, 0.300, 0.455),   # Tracker de Vendas ativo
    (2, 0.415, 0.538, 0.300, 0.610),   # Tracker de Cardapio Digital ativo
])

print("done")
