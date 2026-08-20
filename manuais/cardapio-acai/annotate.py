"""Anota os screenshots do manual BeeFood - Cardapio: acai (#30).

Mesmo estilo dos demais manuais: setas finas/sutis em VERDE + badges numerados.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)

Capturas do painel web em 2160x1350 (viewport 1440x900, DPR 1.5).

O caso novo deste manual e o padrao da acaiteria: acompanhamentos INCLUSOS num
grupo Brinde com limite, e os pagos num grupo Normal separado. Por isso as
imagens dos dois grupos vem em par, com as setas nas mesmas posicoes.

Atencao a um detalhe de layout: o modal do grupo **Cobertura** abre com a faixa
amarela de grupo compartilhado, que empurra todo o conteudo ~0,07 para baixo. As
coordenadas da imagem 06 sao proprias por causa disso, e os campos Minimo/Maximo
ficam fora da area visivel - o texto do manual usa a regra que aparece no PDV.

Regras herdadas dos #27, #28 e #29:
- A seta mira a BORDA do botao (borda direita ~0.688 nos modais do PDV).
- Badge na margem escura ao redor do modal, ou na area vazia do proprio modal.
- Nas listagens, mirar ~0.02 abaixo do centro da linha para nao cobrir o valor.
- Na listagem de complementos, alvos na primeira coluna e badges na faixa da
  sidebar, para as setas nao cruzarem os cards.

Uma imagem de contexto (passthrough): o cardapio com os tres tamanhos.
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

# 01) Os que entram no preco e os que cobram
annotate("01-complementos.png", [
    (1, 0.218, 0.322, 0.090, 0.322),   # acompanhamento incluso: sem preco
    (2, 0.845, 0.322, 0.845, 0.730),   # extra pago: com preco
])

# ---------- Parte 2: o grupo dos inclusos (Brinde com limite) ----------

# 02) Brinde + limite de 3
annotate("02-grupo-inclusos-detalhes.png", [
    (1, 0.160, 0.509, 0.055, 0.509),   # Brinde
    (2, 0.215, 0.803, 0.075, 0.780),   # Minimo 0
    (3, 0.342, 0.803, 0.470, 0.750),   # Maximo 3 - e ele que faz o "ate 3 inclusos"
])

# 03) Todas as opcoes a R$ 0,00
annotate("03-grupo-inclusos-opcoes.png", [
    (1, 0.786, 0.450, 0.830, 0.790),   # R$ 0,00 em todas
])

# ---------- Parte 3: o grupo dos extras (Normal) ----------

# 04) Normal, ate cinco extras
annotate("04-grupo-extras-detalhes.png", [
    (1, 0.160, 0.439, 0.055, 0.439),   # Normal
    (2, 0.215, 0.803, 0.075, 0.780),   # Minimo 0
    (3, 0.342, 0.803, 0.470, 0.750),   # Maximo 5
])

# 05) Aqui o valor da opcao soma
annotate("05-grupo-extras-opcoes.png", [
    (1, 0.786, 0.450, 0.830, 0.790),   # preco de cada extra
])

# ---------- Parte 4: a cobertura ----------

# 06) Grupo compartilhado pelos tres tamanhos
# Layout deslocado pela faixa amarela: o conteudo desce ~0,07 e os campos de
# Quantidade ficam fora da area visivel.
annotate("06-grupo-cobertura-detalhes.png", [
    (1, 0.845, 0.164, 0.935, 0.164),   # aviso de grupo compartilhado
    (2, 0.160, 0.508, 0.055, 0.508),   # Normal
])

# 14) A aba Produtos prova o compartilhamento
annotate("14-grupo-produtos-3x.png", [
    (1, 0.362, 0.235, 0.560, 0.235),   # aba Produtos (3)
    (2, 0.300, 0.444, 0.250, 0.700),   # os tres tamanhos usando o mesmo grupo
])

# ---------- Parte 5: os tres tamanhos ----------

# 07) Cada tamanho e um produto, com o seu preco
annotate("07-produto-acai500.png", [
    (1, 0.650, 0.252, 0.940, 0.200),   # Nome com o tamanho
    (2, 0.430, 0.430, 0.940, 0.400),   # Preco de Venda do tamanho
])

# 08) Os mesmos tres grupos em cada tamanho
# As setas apontam para a ULTIMA linha, vindo de baixo: mirando a primeira linha
# elas atravessavam as outras duas e cobriam a palavra "Brinde".
annotate("08-produto-grupos.png", [
    (1, 0.791, 0.464, 0.880, 0.600),   # coluna Tipo: Brinde e Normal
    (2, 0.700, 0.464, 0.620, 0.600),   # Qtd. Min. e Qtd. Max. de cada grupo
])

# ---------- Parte 6: a prova no PDV ----------

# 09) Aberto, so o preco do tamanho
annotate("09-pdv-inicial.png", [
    (1, 0.320, 0.419, 0.200, 0.370),   # "Escolha 0 a 3"
    (2, 0.688, 0.898, 0.830, 0.945),   # total = preco do tamanho
])

# 10) Tres inclusos escolhidos: o quarto trava e o total nao muda
annotate("10-pdv-inclusos-limite.png", [
    (1, 0.480, 0.394, 0.230, 0.355),   # contador 3/3
    (2, 0.684, 0.634, 0.830, 0.680),   # a quarta opcao fica bloqueada
    (3, 0.688, 0.898, 0.830, 0.945),   # total inalterado
])

# 11) Extras somam
annotate("11-pdv-extras.png", [
    (1, 0.470, 0.206, 0.230, 0.170),   # contador 2/5
    (2, 0.684, 0.284, 0.830, 0.250),   # extra marcado, com "+R$"
    (3, 0.688, 0.898, 0.830, 0.945),   # total com os dois extras
])

# 12) Cobertura: uma so
annotate("12-pdv-cobertura.png", [
    (1, 0.684, 0.492, 0.830, 0.450),   # cobertura marcada
    (2, 0.688, 0.898, 0.830, 0.945),   # total final
])

# 13) No carrinho aparece tudo, inclusive o que nao cobra
annotate("13-pdv-carrinho.png", [
    (1, 0.800, 0.330, 0.620, 0.250),   # as escolhas listadas
    (2, 0.955, 0.898, 0.720, 0.860),   # Valor Final
])

# 15) Os tres tamanhos no cardapio (contexto)
passthrough("15-cardapio-final.png")

print("done")
