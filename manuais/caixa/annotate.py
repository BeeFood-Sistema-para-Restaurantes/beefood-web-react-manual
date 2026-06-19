"""Anota screenshots com setas e numeros para o manual BeeFood.
Estilo: setas finas/sutis em VERDE (tom dos botoes do sistema), leve transparencia.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)
- alvo = ponta da seta (campo/botao)
- badge = posicao do circulo numerado (origem da seta)
"""
import os, math
from PIL import Image, ImageDraw, ImageFont

# Pastas relativas a este manual: imagens puras (backup) -> imagens tratadas (com setas)
SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)          # verde (alinhado aos botoes do BeeFood)
WHITE = (255, 255, 255)
A_LINE = 220                   # alpha das setas (sutil)
A_BADGE = 235                  # alpha dos badges

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
    # halo branco fino + circulo verde semitransparente
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
    r = int(W * 0.0145)            # raio do badge (menor = mais sutil)
    fnt = font(int(r * 1.2))
    w = max(2, int(W * 0.0024))    # espessura fina das setas
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

# 1) Abrir caixa - modal preenchido
annotate("03-modal-abrir-caixa-preenchido.png", [
    (1, 0.360, 0.392, 0.250, 0.392),   # Saldo Inicial em Dinheiro *
    (2, 0.360, 0.485, 0.250, 0.485),   # Caixa *
    (3, 0.360, 0.580, 0.250, 0.580),   # Tipos de Venda
    (4, 0.400, 0.728, 0.250, 0.728),   # ABRIR CAIXA
])

# 2) PDV - formas de pagamento
annotate("05-pdv-formas-pagamento.png", [
    (1, 0.553, 0.300, 0.470, 0.205),   # Dinheiro
    (2, 0.620, 0.700, 0.470, 0.700),   # Falta / Valor total
])

# 3) PDV - dinheiro valor + confirmar
annotate("06-pdv-dinheiro-valor.png", [
    (1, 0.470, 0.432, 0.330, 0.432),   # Valor do pagamento
    (2, 0.500, 0.648, 0.340, 0.648),   # CONFIRMAR
])

# 4) Listagem com caixa aberto - Ver Caixa
annotate("08-caixa-listagem-aberto.png", [
    (1, 0.191, 0.272, 0.110, 0.200),   # lupa Ver Caixa
    (2, 0.450, 0.272, 0.560, 0.200),   # Em aberto
])

# 5) Ver Caixa - resumo dinheiro
annotate("09-ver-caixa-check.png", [
    (1, 0.300, 0.231, 0.175, 0.165),   # operacao Venda 571
    (2, 0.665, 0.305, 0.585, 0.295),   # VENDAS EM DINHEIRO
    (3, 0.665, 0.332, 0.585, 0.400),   # VALOR EM CAIXA
])

print("done")
