"""Anota os screenshots do manual BeeFood - Cardapio: hamburguer (#28).

Mesmo estilo dos demais manuais: setas finas/sutis em VERDE + badges numerados.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)

Capturas do painel web em 2160x1350 (viewport 1440x900, DPR 1.5).

O assunto novo deste manual e a formacao **Brinde** - opcao que o cliente escolhe
mas que nao muda o preco. Por isso varias imagens apontam para a mesma coisa em
lugares diferentes: o preco R$ 0,00 no cadastro, a opcao sem "+R$" no PDV, o total
que nao se altera e o item aparecendo no carrinho sem somar.

Regras herdadas dos #27 e #29:
- A seta mira a BORDA do botao (borda direita ~0.688 nos modais do PDV), nunca o
  meio, porque a ponta no meio cobre uma letra do rotulo.
- Badge na margem escura ao redor do modal, ou na area vazia abaixo do conteudo.
- Nas listagens, mirar ~0.02 abaixo do centro da linha para nao cobrir o valor.

Uma imagem de contexto (passthrough): o cardapio final com os dois lanches.
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


# ---------- Parte 1: os complementos ----------

# 01) Tres tipos de complemento no mesmo cardapio
# Os tres alvos ficam na PRIMEIRA coluna de cards, um por linha, e os badges na
# faixa da sidebar: assim as setas sao curtas e horizontais, sem cruzar os cards
# que sao justamente o assunto da imagem.
annotate("01-complementos.png", [
    (1, 0.218, 0.322, 0.090, 0.322),   # ponto da carne: com foto, sem preco
    (2, 0.218, 0.455, 0.090, 0.455),   # adicional: com foto e com preco
    (3, 0.180, 0.581, 0.090, 0.581),   # retirada: sem foto e sem preco
])

# ---------- Parte 2: o grupo Brinde (ponto da carne) ----------

# 02) Brinde + Obrigatorio, exatamente uma escolha
annotate("02-grupo-ponto-detalhes.png", [
    (1, 0.160, 0.319, 0.055, 0.310),   # Obrigatorio marcado
    (2, 0.160, 0.509, 0.055, 0.509),   # Brinde
    (3, 0.215, 0.803, 0.075, 0.780),   # Minimo 1
    (4, 0.342, 0.803, 0.470, 0.750),   # Maximo 1
])

# 03) As opcoes do grupo Brinde ficam com valor zero
annotate("03-grupo-ponto-opcoes.png", [
    (1, 0.786, 0.450, 0.830, 0.790),   # R$ 0,00 em todas as opcoes
])

# ---------- Parte 3: o grupo Normal (adicionais) ----------

# 04) Normal, de zero a cinco adicionais
annotate("04-grupo-adicionais-detalhes.png", [
    (1, 0.160, 0.439, 0.055, 0.439),   # Normal
    (2, 0.215, 0.803, 0.075, 0.780),   # Minimo 0
    (3, 0.342, 0.803, 0.470, 0.750),   # Maximo 5
])

# 05) Aqui o valor da opcao importa: ele soma
annotate("05-grupo-adicionais-opcoes.png", [
    (1, 0.786, 0.450, 0.830, 0.790),   # valor de cada adicional
])

# ---------- Parte 4: o grupo de retirada ----------

# 06) Brinde de novo, mas com minimo zero
annotate("06-grupo-retirar-detalhes.png", [
    (1, 0.160, 0.509, 0.055, 0.509),   # Brinde
    (2, 0.215, 0.803, 0.075, 0.780),   # Minimo 0
    (3, 0.342, 0.803, 0.470, 0.750),   # Maximo 3
])

# ---------- Parte 5: o produto ----------

# 07) X-Burger com preco cheio (diferente da pizza, aqui o preco fica no produto)
annotate("07-produto-xburger.png", [
    (1, 0.228, 0.437, 0.075, 0.450),   # ADICIONAR FOTO
    (2, 0.430, 0.430, 0.940, 0.400),   # Preco de Venda R$ 28,00
    (3, 0.600, 0.625, 0.940, 0.620),   # Descricao
])

# 08) Os tres grupos vinculados, na ordem em que o atendente pergunta
annotate("08-produto-grupos.png", [
    (1, 0.791, 0.352, 0.880, 0.560),   # coluna Tipo: Brinde, Normal, Brinde
    (2, 0.394, 0.352, 0.320, 0.560),   # numero de ordem e setas de reordenar
])

# ---------- Parte 6: a prova no PDV ----------

# 09) O grupo obrigatorio ganha selo vermelho
annotate("09-pdv-obrigatorio.png", [
    (1, 0.640, 0.420, 0.830, 0.370),   # selo Obrigatorio
    (2, 0.320, 0.447, 0.200, 0.390),   # "Escolha 1"
    (3, 0.688, 0.898, 0.830, 0.945),   # total: so o preco do produto
])

# 14) O que o Obrigatorio faz de fato: bloqueia com aviso
annotate("14-pdv-obrigatorio-bloqueia.png", [
    (1, 0.890, 0.062, 0.740, 0.150),   # aviso "Selecao obrigatoria"
])

# 10) Escolheu o ponto: o selo fica verde e o total NAO muda
annotate("10-pdv-brinde-nao-soma.png", [
    (1, 0.665, 0.420, 0.830, 0.370),   # selo verde: obrigatorio atendido
    (2, 0.684, 0.500, 0.830, 0.545),   # opcao marcada, sem "+R$" nenhum
    (3, 0.688, 0.898, 0.830, 0.945),   # total inalterado
])

# 11) Adicionais somam
annotate("11-pdv-adicionais.png", [
    (1, 0.400, 0.415, 0.220, 0.370),   # contador do grupo (2/5)
    (2, 0.684, 0.488, 0.830, 0.450),   # adicional marcado, com "+R$"
    (3, 0.688, 0.898, 0.830, 0.945),   # total com os dois adicionais
])

# 12) Retirada tambem nao muda o preco
annotate("12-pdv-retirar.png", [
    (1, 0.684, 0.245, 0.830, 0.200),   # item de retirada marcado
    (2, 0.688, 0.898, 0.830, 0.945),   # total igual ao da imagem anterior
])

# 13) No carrinho, tudo aparece - inclusive o que nao cobra
annotate("13-pdv-carrinho.png", [
    (1, 0.800, 0.310, 0.620, 0.240),   # itens listados, com os de Brinde
    (2, 0.955, 0.898, 0.720, 0.860),   # Valor Final
])

# ---------- Parte 7: reaproveitar os grupos ----------

# 15) X-Salada usando os mesmos grupos, sem o de ponto
annotate("15-xsalada-grupos.png", [
    (1, 0.420, 0.352, 0.360, 0.520),   # Adicionais: o mesmo grupo do X-Burger
    (2, 0.450, 0.408, 0.620, 0.520),   # Retirar ingredientes
])

# 16) Os dois lanches no cardapio (contexto)
passthrough("16-cardapio-final.png")

print("done")
