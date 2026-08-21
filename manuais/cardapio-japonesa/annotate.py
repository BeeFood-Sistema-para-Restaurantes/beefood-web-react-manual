"""Anota os screenshots do manual BeeFood - Cardapio: comida japonesa (#31).

Mesmo estilo dos demais manuais: setas finas/sutis em VERDE + badges numerados.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)

Capturas do painel web em 2160x1350 (viewport 1440x900, DPR 1.5).

O caso novo deste manual e o combinado de PRECO FECHADO com CONTAGEM EXATA:
grupo Brinde com minimo = maximo = 4 escolhas de 5 pecas, e cada opcao com
maximo 4 para o cliente poder repetir o mesmo item. Por isso as setas da imagem
10 mostram tres coisas ao mesmo tempo: o contador cheio, a opcao repetida e a
que ficou de fora.

Regras herdadas dos manuais anteriores do bloco:
- A seta mira a BORDA do botao (borda direita ~0.688 nos modais do PDV).
- Nas listagens, mirar ~0.02 abaixo do centro da linha para nao cobrir o valor.
- Em tabela com mais de duas linhas, apontar para a ULTIMA linha, vindo de baixo.
- Nos contadores do PDV, mirar a borda direita (~0.700), nao o numero.

Uma imagem de contexto (passthrough): o cardapio com o combinado e o temaki.
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


# ---------- Parte 1: as pecas como complementos ----------

# 01) Os extras com preco e os blocos de 5 pecas sem preco
# A lista sai em ordem alfabetica, entao na primeira coluna a linha 1 e um extra
# (Cebolinha) e a linha 2 e um bloco de pecas (Sashimi). A numeracao segue a tela.
annotate("01-complementos.png", [
    (1, 0.218, 0.322, 0.090, 0.322),   # extra: com preco
    (2, 0.218, 0.455, 0.090, 0.455),   # bloco de pecas: sem preco
])

# ---------- Parte 2: o grupo da montagem (contagem exata) ----------

# 02) Brinde + Obrigatorio + minimo igual ao maximo
annotate("02-grupo-pecas-detalhes.png", [
    (1, 0.160, 0.319, 0.055, 0.310),   # Obrigatorio
    (2, 0.160, 0.509, 0.055, 0.509),   # Brinde: as pecas nao somam
    (3, 0.215, 0.803, 0.075, 0.780),   # Minimo 4
    (4, 0.342, 0.803, 0.470, 0.750),   # Maximo 4 - igual ao minimo
])

# 03) As opcoes: nome com a quantidade, valor zero e limite por opcao
annotate("03-grupo-pecas-opcoes.png", [
    (1, 0.729, 0.450, 0.640, 0.790),   # limite da opcao: 0 - 4
    (2, 0.786, 0.450, 0.830, 0.790),   # R$ 0,00 em todas
])

# 04) Onde se define o maximo de repeticao de cada opcao
annotate("04-grupo-pecas-opcao-expandida.png", [
    (1, 0.437, 0.512, 0.390, 0.700),   # Maximo da opcao = 4
    (2, 0.505, 0.512, 0.570, 0.700),   # Valor zero
])

# ---------- Parte 3: os extras ----------

# 05) Grupo Normal, compartilhado com o temaki
annotate("05-grupo-extras-detalhes.png", [
    (1, 0.160, 0.439, 0.055, 0.439),   # Normal
    (2, 0.342, 0.803, 0.470, 0.750),   # Maximo 3
])

# 06) Adicionais do temaki, com preco
annotate("06-grupo-adicionais-temaki.png", [
    (1, 0.786, 0.450, 0.830, 0.790),   # preco de cada adicional
])

# ---------- Parte 4: os produtos ----------

# 07) Combinado com preco fechado
annotate("07-produto-combinado.png", [
    (1, 0.650, 0.252, 0.940, 0.200),   # Nome com a quantidade de pecas
    (2, 0.430, 0.430, 0.940, 0.400),   # Preco fechado do combinado
    (3, 0.600, 0.625, 0.940, 0.620),   # Descricao explicando a montagem
])

# 08) Os dois grupos do combinado
annotate("08-produto-grupos.png", [
    (1, 0.791, 0.408, 0.880, 0.560),   # coluna Tipo: Brinde e Normal
    (2, 0.700, 0.408, 0.620, 0.560),   # Qtd. Min. e Qtd. Max.
])

# ---------- Parte 5: a prova no PDV ----------

# 09) Aberto: preco fechado e a regra da montagem
annotate("09-pdv-combinado-inicial.png", [
    (1, 0.320, 0.447, 0.200, 0.390),   # "Escolha 4" e o selo Obrigatorio
    (2, 0.688, 0.898, 0.830, 0.945),   # total = preco fechado
])

# 10) Quatro de quatro: repetida, vazia e o total inalterado
annotate("10-pdv-contagem-exata.png", [
    (1, 0.480, 0.420, 0.230, 0.380),   # contador 4/4 e o check verde
    (2, 0.700, 0.500, 0.830, 0.460),   # a mesma opcao escolhida duas vezes
    (3, 0.700, 0.663, 0.830, 0.700),   # a opcao que ficou de fora, em 0
    (4, 0.688, 0.898, 0.830, 0.945),   # total: continua o preco fechado
])

# 11) Os extras, sim, somam
annotate("11-pdv-combinado-extras.png", [
    (1, 0.379, 0.418, 0.200, 0.370),   # grupo Extras, contador 1/3
    (2, 0.684, 0.492, 0.830, 0.450),   # extra marcado, com "+R$"
    (3, 0.688, 0.898, 0.830, 0.945),   # total com o extra
])

# 12) No carrinho, a montagem com as quantidades
annotate("12-pdv-carrinho.png", [
    (1, 0.800, 0.330, 0.620, 0.250),   # as escolhas com "2x", "1x"
    (2, 0.955, 0.898, 0.720, 0.860),   # Valor Final
])

# 13) O temaki: produto simples, e o grupo Extras reaproveitado
annotate("13-pdv-temaki.png", [
    (1, 0.320, 0.420, 0.200, 0.370),   # grupo Extras, o mesmo do combinado
    (2, 0.684, 0.823, 0.830, 0.790),   # adicional marcado
    (3, 0.688, 0.898, 0.830, 0.945),   # total do temaki com o adicional
])

# 14) O cardapio com os dois produtos (contexto)
passthrough("14-cardapio-final.png")

print("done")
