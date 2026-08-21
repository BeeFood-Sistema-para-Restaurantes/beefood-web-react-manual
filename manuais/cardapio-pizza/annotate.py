"""Anota os screenshots do manual BeeFood - Cardapio: pizza (#29).

Mesmo estilo dos demais manuais: setas finas/sutis em VERDE + badges numerados.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)

Capturas do painel web em 2160x1350 (viewport 1440x900, DPR 1.5).

Duas regras herdadas do #27, que valem aqui tambem:
- A seta mira a BORDA do botao (nos modais centralizados, borda direita ~0.688
  no PDV e ~0.716 nos assistentes), nunca o meio: a ponta no meio cobre uma letra.
- Badge na margem escura ao redor do modal; dentro do modal so quando ha area
  vazia de sobra.

O manual compara dois modos de preco, entao varias imagens vem em par (uma do
grupo Valor da Maior, outra do Proporcional) com as setas nas mesmas posicoes -
isso ajuda o leitor a ver o que mudou.

Uma imagem de contexto (passthrough): o cardapio final com as duas pizzas.
Sem borrao: nenhuma captura tem dado de cliente.
"""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

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
    raise RuntimeError("nenhuma fonte bold encontrada: " + ", ".join(FONT_CANDIDATES))


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


def annotate(name, markers, ring=None, borrao=None, raio=0.0125, out_name=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    W, H = img.size

    for (fx, fy, fw, fh) in (borrao or []):
        caixa = (int(fx * W), int(fy * H), int((fx + fw) * W), int((fy + fh) * H))
        trecho = img.crop(caixa).filter(ImageFilter.GaussianBlur(radius=max(6, W // 140)))
        img.paste(trecho, caixa)

    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = int(W * raio)
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
    out_img.save(os.path.join(OUT, out_name or name))
    print("OK", out_name or name)


# ---------- Parte 1: os sabores como complementos ----------

# 01) Os quatro sabores e as duas bordas, com foto e preco inteiro
annotate("01-complementos-sabores.png", [
    (1, 0.651, 0.348, 0.600, 0.550),   # preco inteiro do sabor
    (2, 0.640, 0.398, 0.860, 0.550),   # "Usado 2 vezes" nos dois grupos de sabor
])

# ---------- Parte 2: o grupo Valor da Maior ----------

# 02) Detalhes do grupo: Valor da Maior, 1 a 2 sabores
annotate("02-grupo-maior-detalhes.png", [
    (1, 0.160, 0.580, 0.055, 0.580),   # Valor da Maior
    (2, 0.215, 0.803, 0.075, 0.780),   # Minimo 1
    (3, 0.342, 0.803, 0.470, 0.750),   # Maximo 2
])

# 03) Opcoes do grupo Valor da Maior: preco INTEIRO da pizza em cada sabor
annotate("03-grupo-maior-opcoes.png", [
    (1, 0.786, 0.450, 0.830, 0.790),   # valor inteiro do sabor
    (2, 0.729, 0.450, 0.640, 0.790),   # limite da opcao: 0 - 1
])

# ---------- Parte 3: o grupo Proporcional ----------

# 04) Detalhes do grupo: Proporcional, exatamente 2 metades
annotate("04-grupo-prop-detalhes.png", [
    (1, 0.160, 0.651, 0.055, 0.651),   # Proporcional
    (2, 0.215, 0.803, 0.075, 0.780),   # Minimo 2
    (3, 0.342, 0.803, 0.470, 0.750),   # Maximo 2
])

# 05) Opcoes do grupo Proporcional: preco de MEIA pizza em cada sabor
annotate("05-grupo-prop-opcoes.png", [
    (1, 0.786, 0.450, 0.830, 0.790),   # valor de meia pizza
    (2, 0.729, 0.450, 0.640, 0.790),   # limite da opcao: 0 - 2
])

# 06) A linha da opcao aberta: onde se define o maximo 2 e o valor da metade
annotate("06-grupo-prop-opcao-expandida.png", [
    (1, 0.437, 0.512, 0.390, 0.700),   # Maximo da opcao = 2
    (2, 0.505, 0.512, 0.570, 0.700),   # Valor = metade
    (3, 0.753, 0.598, 0.870, 0.700),   # SALVAR da linha
])

# ---------- Parte 4: a borda ----------

# 07) Grupo Borda, compartilhado pelas duas pizzas
annotate("07-grupo-borda.png", [
    (1, 0.845, 0.164, 0.935, 0.164),   # aviso de grupo compartilhado
    (2, 0.729, 0.500, 0.640, 0.700),   # limite da opcao: 0 - 1
    (3, 0.786, 0.500, 0.830, 0.700),   # valor da borda (soma)
])

# ---------- Parte 5: o produto ----------

# 08) O produto com Preco de Venda R$ 0,00
annotate("08-produto-preco-zero.png", [
    (1, 0.228, 0.437, 0.075, 0.450),   # ADICIONAR FOTO
    (2, 0.600, 0.341, 0.940, 0.300),   # Setor Pizzas
    (3, 0.430, 0.430, 0.940, 0.400),   # Preco de Venda R$ 0,00
])

# 09) Os dois grupos vinculados, com a formacao de preco na coluna Tipo
# Duas setas: a terceira, que apontava a linha da Borda, cruzava as outras duas.
# A linha da Borda esta logo abaixo e o texto do manual a descreve.
annotate("09-produto-grupos.png", [
    (1, 0.791, 0.368, 0.880, 0.520),   # coluna Tipo (a formacao de preco de cada grupo)
    (2, 0.700, 0.368, 0.620, 0.520),   # Qtd. Min. e Qtd. Max.
])

# ---------- Parte 6: a prova no PDV ----------

# 10) Valor da Maior com um sabor
annotate("10-pdv-maior-1sabor.png", [
    (1, 0.347, 0.425, 0.200, 0.380),   # "Escolha 1 a 2"
    (2, 0.684, 0.522, 0.830, 0.480),   # sabor marcado
    (3, 0.688, 0.898, 0.830, 0.945),   # total = preco do sabor
])

# 11) Valor da Maior com dois sabores: cobra so o mais caro
annotate("11-pdv-maior-2sabores.png", [
    (1, 0.312, 0.467, 0.180, 0.530),   # aviso azul da regra especial
    (2, 0.684, 0.522, 0.830, 0.470),   # os dois sabores marcados
    (3, 0.688, 0.898, 0.830, 0.945),   # total = o sabor mais caro
])

# 12) Proporcional com o mesmo sabor duas vezes: pizza inteira
annotate("12-pdv-prop-inteira.png", [
    (1, 0.347, 0.430, 0.200, 0.380),   # "Escolha 2" e contador 2/2
    (2, 0.700, 0.472, 0.830, 0.430),   # quantidade 2 no mesmo sabor
    (3, 0.688, 0.898, 0.830, 0.945),   # total = preco da pizza inteira
])

# 13) Proporcional meio a meio: a media dos dois sabores
annotate("13-pdv-prop-meio.png", [
    (1, 0.700, 0.472, 0.830, 0.430),   # metade 1
    (2, 0.700, 0.553, 0.830, 0.600),   # metade 2
    (3, 0.688, 0.898, 0.830, 0.945),   # total = soma das metades
])

# 14) Borda somando por cima do sabor
annotate("14-pdv-prop-borda.png", [
    (1, 0.684, 0.492, 0.830, 0.450),   # Borda Catupiry marcada
    (2, 0.688, 0.898, 0.830, 0.945),   # total com a borda
])

# 15) As duas pizzas no cardapio (contexto)
passthrough("15-cardapio-final.png")

print("done")
