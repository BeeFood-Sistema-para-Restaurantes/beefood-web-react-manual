"""Anota screenshots com setas e numeros para o manual BeeFood - Segunda Conferencia.
Estilo: setas finas/sutis em VERDE (tom dos botoes do sistema), leve transparencia.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)
- alvo = ponta da seta (campo/botao)
- badge = posicao do circulo numerado (origem da seta)

Nos modais, os badges ficam na margem escurecida do overlay e as setas apontam
para dentro, encostando na borda do elemento - assim nenhum numero cobre valor.
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


def annotate(name, markers):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    W, H = img.size
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = int(W * 0.0145)
    fnt = font(int(r * 1.2))
    w = max(2, int(W * 0.0024))
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

# Etapa 1 - o caixa fechado com quebra, e onde abrir a conferencia
annotate("01-listagem-caixa-fechado.png", [
    (1, 0.935, 0.365, 0.945, 0.200),   # Quebra de Caixa R$ 2,55
    (2, 0.251, 0.373, 0.160, 0.280),   # botao verde Ver Conferencia
])

# Etapa 2 - a 1a conferencia em modo leitura
annotate("02-primeira-conferencia-leitura.png", [
    (1, 0.470, 0.130, 0.470, 0.045),   # botao Adicionar 2a Conferencia
    (2, 0.680, 0.240, 0.600, 0.055),   # campos travados (somente leitura)
    (3, 0.910, 0.705, 0.962, 0.630),   # Quebra de Caixa R$ 2,55 (Falta)
])

# Etapa 3 - a 2a conferencia recem-aberta
annotate("03-segunda-conferencia-em-branco.png", [
    (1, 0.573, 0.120, 0.520, 0.045),   # coluna 2a Conferencia (onde digitar)
    (2, 0.831, 0.120, 0.898, 0.045),   # coluna 1a Conferencia (o que foi contado antes)
    (3, 0.130, 0.755, 0.045, 0.700),   # Observacoes da Conferencia
])

# Etapa 3 - recontagem do dinheiro pela calculadora
annotate("04-calculadora-recontagem.png", [
    (1, 0.368, 0.261, 0.250, 0.200),   # campo de valor
    (2, 0.378, 0.450, 0.250, 0.520),   # Valores Adicionados (100,00 + 2,55)
    (3, 0.645, 0.695, 0.790, 0.640),   # Total R$ 102,55
    (4, 0.645, 0.777, 0.760, 0.890),   # Incluir Conferencia
])

# Etapa 4 - a 2a conferencia fecha e a quebra desaparece
annotate("05-segunda-conferencia-conferida.png", [
    (1, 0.545, 0.155, 0.480, 0.035),   # valor recontado com check verde
    (2, 0.831, 0.120, 0.898, 0.045),   # 1a Conferencia ao lado (R$ 100,00)
    (3, 0.755, 0.635, 0.755, 0.720),   # Quebra de Caixa: Correto
    (4, 0.851, 0.635, 0.885, 0.720),   # Quebra 1a Conf.: R$ 2,55 (Falta)
])

# Etapa 5 - observacoes, confirmacao e o botao Conferir
annotate("06-observacoes-conferido.png", [
    (1, 0.130, 0.740, 0.045, 0.680),   # Observacoes preenchidas
    (2, 0.128, 0.877, 0.045, 0.820),   # checkbox marcado
    (3, 0.895, 0.936, 0.958, 0.870),   # botao Conferir habilitado
])

annotate("07-confirmar-conferencia.png", [
    (1, 0.670, 0.542, 0.800, 0.620),   # botao Conferir na confirmacao
])

# Etapa 6 - o resultado na listagem
annotate("08-listagem-conferido.png", [
    (1, 0.238, 0.358, 0.215, 0.305),   # cadeado (segunda conferencia concluida)
    (2, 0.788, 0.365, 0.760, 0.170),   # Conf. Saldo Final atualizado
    (3, 0.895, 0.358, 0.880, 0.170),   # Quebra de Caixa zerada
])

# Etapa 6 - a conferencia fica travada
annotate("09-conferencia-travada.png", [
    (1, 0.545, 0.164, 0.470, 0.035),   # campos travados
    (2, 0.831, 0.120, 0.898, 0.045),   # as duas conferencias registradas
    (3, 0.895, 0.936, 0.958, 0.870),   # botao Conferir desabilitado
])

print("done")
