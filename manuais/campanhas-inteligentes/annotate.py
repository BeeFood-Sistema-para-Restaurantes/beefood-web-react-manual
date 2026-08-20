"""Anota os screenshots do manual BeeFood - Campanhas Inteligentes.
Mesmo estilo dos demais manuais: setas finas/sutis em VERDE + badges numerados.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)
- alvo = ponta da seta (campo/botao)
- badge = posicao do circulo numerado (origem da seta)

O editor de campanha e um painel lateral com o resto da tela escurecido. Nele os
badges ficam na MARGEM escura (x ~ 0.495), com setas horizontais curtas — mesma
tecnica usada no manual de fechar caixa. Onde o campo esta na coluna direita do
painel, usamos `ring` em vez de seta.

O telefone do cliente na tela de historico ja foi coberto na imagem pura: o
repositorio e publico e nenhum dado pessoal pode ser versionado.
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


def annotate(name, markers, ring=None, borrao=None, raio=0.0125):
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
    out_img.save(os.path.join(OUT, name))
    print("OK", name)


# ---------- A aba e os cards ----------

# 01) As seis campanhas: estados e o selo da BeeFood
annotate("01-lista-campanhas.png", [
    (1, 0.420, 0.090, 0.610, 0.030),   # aba Campanhas Inteligentes
    (2, 0.172, 0.262, 0.105, 0.215),   # selo Ativo
    (3, 0.376, 0.289, 0.300, 0.222),   # chave liga/desliga
    (4, 0.462, 0.690, 0.400, 0.755),   # selo Pausado
    (5, 0.745, 0.690, 0.680, 0.755),   # selo Rascunho
])

# 02) Anatomia do card (recorte)
annotate("02-card-anatomia.png", [
    (1, 0.091, 0.070, 0.090, 0.215),   # status
    (2, 0.270, 0.070, 0.310, 0.215),   # selo BeeFood
    (3, 0.815, 0.070, 0.790, 0.215),   # chave liga/desliga
    (4, 0.415, 0.472, 0.600, 0.450),   # selo do gatilho
    (5, 0.325, 0.617, 0.620, 0.580),   # receita gerada
    (6, 0.270, 0.862, 0.500, 0.965),   # Resultado / Historico
], raio=0.030)

# 03) Card em rascunho (recorte)
annotate("03-card-rascunho.png", [
    (1, 0.126, 0.070, 0.130, 0.215),   # selo Rascunho
    (2, 0.300, 0.897, 0.520, 0.965),   # Revisar e ativar
], raio=0.030)

# ---------- Passo 1 ----------

# 04) Publico por segmentacao
annotate("04-passo1-publico-segmentacao.png", [
    (1, 0.560, 0.373, 0.495, 0.373),   # Cardapio
    (2, 0.560, 0.502, 0.495, 0.502),   # Segmentacao
], ring=[
    (0.552, 0.163, 0.437, 0.078),      # Como esta automacao funciona
    (0.772, 0.352, 0.215, 0.042),      # Origem do publico
])

# 13) Gatilho por evento (carrinho abandonado)
annotate("13-passo1-gatilho-evento.png", [
    (1, 0.560, 0.520, 0.495, 0.520),   # Esperar antes de enviar (min)
    (2, 0.560, 0.655, 0.495, 0.655),   # frase-resumo da janela
], ring=[
    (0.772, 0.365, 0.215, 0.042),      # Origem do publico = Carrinho abandonado
    (0.772, 0.500, 0.215, 0.042),      # Considerar eventos das ultimas (h)
])

# ---------- Passo 2: mensagem, variacoes e variaveis ----------

passthrough("05-passo2-variacoes.png")

# 17) Uma variacao com variacao automatica (recorte)
annotate("17-variacao-com-spintax.png", [
    (1, 0.680, 0.497, 0.800, 0.630),   # texto com {opcao1|opcao2}
    (2, 0.100, 0.790, 0.220, 0.665),   # Previa
], ring=[
    (0.545, 0.055, 0.420, 0.100),      # tag obrigatoria + Inserir variavel
], raio=0.022)

passthrough("07-aviso-sem-link.png")
passthrough("14-modal-variaveis.png")
passthrough("15-variaveis-bloqueadas.png")
passthrough("16-spintax.png")

# ---------- Passo 3: agenda e anti-spam ----------

# 08) Agenda completa
annotate("08-passo3-agenda.png", [
    (1, 0.565, 0.475, 0.495, 0.475),   # Dias da semana
    (2, 0.560, 0.570, 0.495, 0.570),   # Horario de inicio
    (3, 0.560, 0.665, 0.495, 0.665),   # Anti Banimento
    (4, 0.560, 0.885, 0.495, 0.885),   # Intervalo minimo
], ring=[
    (0.552, 0.316, 0.437, 0.065),      # aviso do cardapio aberto
])

passthrough("09-anti-banimento-ligado.png")
passthrough("10-anti-banimento-desligado.png")
passthrough("11-alerta-risco-banimento.png")
passthrough("12-intervalo-e-ritmo.png")

# ---------- Ligar, pausar e acompanhar ----------

passthrough("20-dialogo-ativar.png")
passthrough("18-resultado.png")

# 19) Historico: a mensagem como o cliente recebeu
annotate("19-historico.png", [
    (1, 0.790, 0.436, 0.900, 0.400),   # Exportar CSV
    (2, 0.664, 0.538, 0.664, 0.745),   # mensagem enviada
    (3, 0.800, 0.548, 0.900, 0.600),   # Converteu?
])

# ---------- Catalogo de modelos ----------

passthrough("22-modelos-prontos.png")

print("done")
