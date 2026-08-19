"""Anota screenshots com setas e numeros para o manual BeeFood - Fechar Caixa.
Estilo: setas finas/sutis em VERDE (tom dos botoes do sistema), leve transparencia.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)
- alvo = ponta da seta (campo/botao)
- badge = posicao do circulo numerado (origem da seta)

Nos modais, os badges ficam na margem escurecida do overlay e as setas apontam
para dentro - assim nenhum numero cobre valor ou rotulo da tela.
"""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Pastas relativas a este manual: imagens puras (backup) -> imagens tratadas (com setas)
SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)          # verde (alinhado aos botoes do BeeFood)
WHITE = (255, 255, 255)
A_LINE = 220                   # alpha das setas (sutil)
A_BADGE = 235                  # alpha dos badges

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
    # halo branco fino + circulo verde semitransparente
    d.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], fill=WHITE + (235,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN + (A_BADGE,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    d.text((cx - tw / 2 - bb[0], cy - th / 2 - bb[1]), t, fill=WHITE, font=fnt)


def desfocar(img, regioes):
    """Borra regioes (fracoes) antes de anotar - usado para dado pessoal em tela."""
    W, H = img.size
    for (fx, fy, fw, fh) in regioes:
        caixa = (int(fx * W), int(fy * H), int((fx + fw) * W), int((fy + fh) * H))
        recorte = img.crop(caixa).filter(ImageFilter.GaussianBlur(radius=max(3, int(W * 0.005))))
        img.paste(recorte, caixa)
    return img


def annotate(name, markers, ring=None, blur=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    if blur:
        img = desfocar(img, blur)
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

# Etapa 1 - listagem com o caixa em aberto
annotate("01-listagem-caixa-aberto.png", [
    (1, 0.443, 0.314, 0.408, 0.225),   # status "Em aberto"
    (2, 0.200, 0.327, 0.140, 0.225),   # lupa Ver Caixa
])

# Etapa 1 - dentro do caixa: onde fica FECHAR CAIXA e o valor a conferir
annotate("02-ver-caixa-fechar.png", [
    (1, 0.740, 0.172, 0.700, 0.075),   # botao FECHAR CAIXA
    (2, 0.918, 0.515, 0.972, 0.575),   # VALOR EM CAIXA
])

# Etapa 2 - vendas sem pagamento total
annotate("03-vendas-pendentes.png", [
    (1, 0.181, 0.248, 0.075, 0.300),   # botao verde (pagar a venda)
    (2, 0.768, 0.200, 0.930, 0.150),   # coluna Faltante
    (3, 0.850, 0.908, 0.935, 0.850),   # FECHAR CAIXA MESMO ASSIM (F2)
])

# Etapa 2 - pagamento da venda registrado
# O CPF do cliente de teste aparece no campo Documento -> desfocado antes de anotar.
annotate("04-pagamento-venda.png", [
    (1, 0.835, 0.395, 0.930, 0.330),   # Pagamentos realizados / Pago
    (2, 0.625, 0.791, 0.930, 0.830),   # Pagamento completo
], blur=[(0.745, 0.102, 0.108, 0.036)])

# Etapa 2 - a venda volta para a lista como PAGA
annotate("05-venda-paga.png", [
    (1, 0.181, 0.248, 0.070, 0.300),   # botao virou check
    (2, 0.845, 0.248, 0.930, 0.180),   # badge PAGA
])

# Etapa 2 - aviso ao fechar com pendencias
annotate("06-aviso-fechar-mesmo-assim.png", [
    (1, 0.353, 0.442, 0.205, 0.400),   # por que confirmar os pagamentos antes
    (2, 0.390, 0.745, 0.230, 0.830),   # NAO, REVISAR (ESC)
    (3, 0.640, 0.745, 0.760, 0.830),   # FECHAR ASSIM MESMO (ENTER)
])

# Etapa 3 - conferencia em branco
annotate("07-conferencia-em-branco.png", [
    (1, 0.310, 0.256, 0.300, 0.055),   # coluna Entrada (valor apurado)
    (2, 0.658, 0.230, 0.630, 0.055),   # campo da 1a Conferencia
    (3, 0.730, 0.245, 0.960, 0.180),   # icone da calculadora
    (4, 0.120, 0.270, 0.045, 0.360),   # seta que abre o detalhe do Dinheiro
])

# Etapa 3 - calculadora somando as cedulas
annotate("08-calculadora-dinheiro.png", [
    (1, 0.368, 0.261, 0.250, 0.200),   # campo de valor
    (2, 0.378, 0.450, 0.250, 0.520),   # Valores Adicionados
    (3, 0.645, 0.695, 0.790, 0.640),   # Total
    (4, 0.645, 0.777, 0.760, 0.890),   # Incluir Conferencia
])

# Etapa 4 - conferencia preenchida com a quebra
annotate("09-conferencia-com-quebra.png", [
    (1, 0.905, 0.256, 0.965, 0.180),   # Diferenca -R$ 2,55
    (2, 0.910, 0.700, 0.965, 0.630),   # Quebra de Caixa (Falta)
    (3, 0.680, 0.775, 0.540, 0.850),   # Saldo Final Conferido
])

# Etapa 5 - confirmacao do fechamento
annotate("10-confirmar-fechamento.png", [
    (1, 0.665, 0.545, 0.800, 0.620),   # botao Fechar caixa
])

# Etapa 5 - impressao do resumo
annotate("11-imprimir-conferencia.png", [
    (1, 0.665, 0.532, 0.800, 0.620),   # Sim, imprimir
    (2, 0.525, 0.532, 0.360, 0.620),   # Nao
])

# Etapa 6 - listagem com o caixa fechado
annotate("12-listagem-fechado.png", [
    (1, 0.440, 0.298, 0.398, 0.212),   # Data/Hora Fechamento
    (2, 0.838, 0.305, 0.822, 0.128),   # Conf. Saldo Final
    (3, 0.935, 0.295, 0.945, 0.130),   # Quebra de Caixa
])

print("done")
