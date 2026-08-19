"""Anota os screenshots do manual BeeFood - Segmentacao de Clientes.
Mesmo estilo dos demais manuais: setas finas/sutis em VERDE + badges numerados.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)
- alvo = ponta da seta (campo/botao)
- badge = posicao do circulo numerado (origem da seta)

Alem das setas, este manual usa `borrao`: a lista de clientes do publico mostra
nome, telefone e e-mail de pessoas reais da conta de testes, e essas areas
precisam sair ilegiveis antes de a imagem ir para o repositorio (que e publico).
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

# Arial no Windows do dono; Arimo/DejaVu no Linux (Cloud Agent). Primeiro que existir vence.
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


def annotate(name, markers, ring=None, borrao=None):
    """ring   = retangulos (x, y, largura, altura) em fracoes, para cercar uma area.
    borrao = retangulos (x, y, largura, altura) em fracoes, para tornar dados
             pessoais ilegiveis. Aplicado ANTES das setas."""
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    W, H = img.size

    for (fx, fy, fw, fh) in (borrao or []):
        caixa = (int(fx * W), int(fy * H), int((fx + fw) * W), int((fy + fh) * H))
        trecho = img.crop(caixa).filter(ImageFilter.GaussianBlur(radius=max(6, W // 140)))
        img.paste(trecho, caixa)

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


# ---------- A tela ----------

# 01) Lista de segmentacoes
annotate("01-lista.png", [
    (1, 0.237, 0.068, 0.150, 0.028),   # botao Nova segmentacao
    (2, 0.371, 0.068, 0.430, 0.028),   # botao Modelos prontos
    (3, 0.700, 0.119, 0.880, 0.078),   # aviso da base elegivel
    (4, 0.375, 0.207, 0.570, 0.250),   # selo BeeFood (publico fixo)
    (5, 0.925, 0.478, 0.870, 0.545),   # acoes de um publico seu
])

# 02) Modelos prontos
annotate("02-modelos-prontos.png", [
    (1, 0.243, 0.196, 0.170, 0.130),   # a categoria do modelo
    (2, 0.276, 0.316, 0.180, 0.360),   # Pre-visualizar
    (3, 0.276, 0.360, 0.180, 0.420),   # Usar este modelo
])

# ---------- Montar a primeira segmentacao ----------

# 03) O seletor de campo, com os 37 filtros por categoria
annotate("03-seletor-campo.png", [
    (1, 0.500, 0.110, 0.620, 0.055),   # quantos campos existem
    (2, 0.500, 0.152, 0.640, 0.108),   # busca por nome do campo
    (3, 0.330, 0.200, 0.180, 0.245),   # as categorias (chips)
    (4, 0.301, 0.352, 0.180, 0.400),   # um campo (cartao)
])

# 04) A primeira regra montada
annotate("04-primeira-regra.png", [
    (1, 0.400, 0.297, 0.520, 0.235),   # nome da segmentacao
    (2, 0.855, 0.297, 0.795, 0.235),   # switch Ativa
    (3, 0.132, 0.468, 0.068, 0.468),   # o campo
    (4, 0.390, 0.478, 0.390, 0.585),   # o operador
    (5, 0.518, 0.478, 0.548, 0.585),   # o valor
    (6, 0.128, 0.525, 0.068, 0.600),   # ADICIONAR REGRA
    (7, 0.128, 0.712, 0.068, 0.790),   # TESTAR PUBLICO
    (8, 0.855, 0.730, 0.930, 0.790),   # SALVAR (F2)
])

# 05) O resultado do teste
annotate("05-resultado-teste.png", [
    (1, 0.500, 0.450, 0.330, 0.400),   # o percentual
    (2, 0.500, 0.503, 0.330, 0.545),   # quantos de quantos elegiveis
    (3, 0.469, 0.665, 0.330, 0.700),   # Ver clientes
])

# ---------- Combinar regras ----------

# 06) Duas condicoes com E
annotate("06-duas-regras-e.png", [
    (1, 0.237, 0.465, 0.170, 0.560),   # primeira condicao
    (2, 0.150, 0.509, 0.075, 0.560),   # o seletor E / OU
    (3, 0.237, 0.546, 0.170, 0.640),   # segunda condicao
    (4, 0.540, 0.546, 0.620, 0.640),   # valor em R$ (mascara)
])

# 07) Duas condicoes com OU, multiselect e valor em reais
annotate("07-duas-regras-ou.png", [
    (1, 0.554, 0.465, 0.640, 0.400),   # multiselect com os chips escolhidos
    (2, 0.159, 0.509, 0.080, 0.560),   # OU marcado
    (3, 0.540, 0.546, 0.640, 0.640),   # valor em R$
])

# ---------- Depois de salvar ----------

# 08) Painel de detalhes
annotate("08-detalhes.png", [
    (1, 0.730, 0.253, 0.660, 0.205),   # filtros escolhidos, em texto
    (2, 0.712, 0.360, 0.650, 0.330),   # o tamanho do publico
    (3, 0.762, 0.462, 0.700, 0.530),   # Editar
    (4, 0.926, 0.462, 0.940, 0.550),   # Exportar Excel
])

# 09) Os clientes que caíram no publico (dados pessoais borrados)
annotate("09-clientes-do-publico.png", [
    (1, 0.618, 0.030, 0.500, 0.075),   # quantos clientes
    (2, 0.766, 0.108, 0.640, 0.155),   # busca dentro do publico
    (3, 0.900, 0.240, 0.960, 0.310),   # os indicadores de cada cliente
], borrao=[
    # nome + telefone + e-mail de cada cartao (a conta e de testes, mas os
    # dados sao de pessoas e o repositorio e publico)
    (0.542, 0.172, 0.170, 0.048),
    (0.542, 0.297, 0.170, 0.048),
    (0.542, 0.423, 0.170, 0.048),
    (0.542, 0.548, 0.170, 0.066),
    (0.542, 0.693, 0.170, 0.066),
    (0.542, 0.836, 0.170, 0.066),
])

print("done")
