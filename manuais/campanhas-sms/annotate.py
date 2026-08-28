"""Anota os screenshots do manual BeeFood - Campanhas SMS.
Mesmo estilo dos demais: setas finas/sutis em VERDE + badges numerados.
Coordenadas em fracoes (0..1).
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)

O editor e um painel lateral. Badges ficam na margem escura (x ~ 0.495),
com setas horizontais curtas — mesma tecnica do #16.

Dados pessoais: Maria Santos / Joao Silva (telefones de fixture do rascunho)
e os dois numeros da blacklist sao cobertos com borrão NA IMAGEM PURA
(repositorio publico). O telefone do comercial (15 99132-0694) foi autorizado
pelo dono para o teste e permanece visivel.
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
    img = Image.open(os.path.join(SRC, name)).convert("RGB")
    img.save(os.path.join(OUT, name))
    print("OK (contexto)", name)


def blur_pura(name, boxes):
    """Aplica borrão na pura (repositorio publico) e regrava o arquivo."""
    path = os.path.join(SRC, name)
    img = Image.open(path).convert("RGBA")
    W, H = img.size
    for (fx, fy, fw, fh) in boxes:
        caixa = (int(fx * W), int(fy * H), int((fx + fw) * W), int((fy + fh) * H))
        trecho = img.crop(caixa).filter(ImageFilter.GaussianBlur(radius=max(8, W // 120)))
        img.paste(trecho, caixa)
    img.convert("RGB").save(path)
    print("BORRAO pura", name)


def annotate(name, markers, ring=None, borrao=None, raio=0.0125):
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


# Borrão das puras já foi aplicado na primeira rodada. Não repetir aqui.

# ---------- Lista e abas ----------

annotate("01-lista-campanhas.png", [
    (1, 0.268, 0.108, 0.200, 0.055),   # aba Campanhas
    (2, 0.355, 0.108, 0.355, 0.048),   # aba Saldo & Extrato
    (3, 0.490, 0.108, 0.580, 0.048),   # aba Blacklist
    (4, 0.305, 0.198, 0.240, 0.155),   # NOVA CAMPANHA (borda do botao)
    (5, 0.790, 0.198, 0.700, 0.148),   # saldo
    (6, 0.935, 0.198, 0.960, 0.145),   # COMPRAR CREDITOS
])

# ---------- Passo 1 ----------

annotate("02-passo1-mensagem.png", [
    (1, 0.720, 0.205, 0.495, 0.205),   # nome
    (2, 0.720, 0.280, 0.495, 0.280),   # cardapio
    (3, 0.910, 0.355, 0.495, 0.355),   # contador GSM
    (4, 0.700, 0.400, 0.495, 0.400),   # variaveis
    (5, 0.575, 0.655, 0.495, 0.655),   # switch sem acento
], ring=[
    (0.555, 0.530, 0.420, 0.090),      # aviso de link
])

annotate("03-aviso-ucs2.png", [
    (1, 0.910, 0.355, 0.495, 0.340),   # contador UCS-2
    (2, 0.750, 0.530, 0.495, 0.510),   # aviso 70/67
    (3, 0.575, 0.655, 0.495, 0.680),   # switch desligado
])

# ---------- Passo 2 ----------

annotate("05-passo2-segmentacao.png", [
    (1, 0.680, 0.255, 0.495, 0.240),   # Por segmentacao
    (2, 0.800, 0.255, 0.495, 0.310),   # Telefone avulso
    (3, 0.900, 0.255, 0.495, 0.380),   # Planilha
    (4, 0.700, 0.335, 0.495, 0.480),   # Selecione um publico
])

annotate("06-passo2-avulso.png", [
    (1, 0.800, 0.255, 0.495, 0.240),   # Telefone avulso
    (2, 0.620, 0.330, 0.495, 0.310),   # campo telefone
    (3, 0.900, 0.330, 0.495, 0.380),   # ADICIONAR
    (4, 0.620, 0.480, 0.495, 0.500),   # Comercial Beefood
])

annotate("07-passo2-excel.png", [
    (1, 0.900, 0.255, 0.495, 0.240),   # Planilha
    (2, 0.680, 0.340, 0.495, 0.380),   # SELECIONAR ARQUIVO
])

# ---------- Envio ----------

annotate("09-aviso-link.png", [
    (1, 0.500, 0.470, 0.320, 0.400),   # texto do aviso
    (2, 0.620, 0.575, 0.780, 0.620),   # ENVIAR COM LINK
], raio=0.016)

annotate("09b-confirmar-envio.png", [
    (1, 0.500, 0.480, 0.320, 0.410),   # dest / custo / saldo
    (2, 0.620, 0.600, 0.780, 0.640),   # ENVIAR (ENTER)
], raio=0.016)

# ---------- Compra ----------

annotate("10-comprar-creditos.png", [
    (1, 0.500, 0.300, 0.260, 0.240),   # 32 creditos / total
    (2, 0.500, 0.430, 0.260, 0.400),   # slider
    (3, 0.380, 0.570, 0.260, 0.600),   # pacotes
], raio=0.014)

# ---------- Blacklist ----------

annotate("12-blacklist.png", [
    (1, 0.420, 0.280, 0.180, 0.220),   # texto opt-out
    (2, 0.880, 0.520, 0.930, 0.470),   # ADICIONAR MANUAL
    (3, 0.350, 0.630, 0.180, 0.650),   # tabela
])

annotate("13-adicionar-blacklist.png", [
    (1, 0.500, 0.480, 0.320, 0.410),   # campo telefone
    (2, 0.620, 0.575, 0.780, 0.620),   # SALVAR (F2)
], raio=0.016)

# ---------- Depois do envio ----------

annotate("14-lista-apos-envio.png", [
    (1, 0.420, 0.305, 0.300, 0.250),   # selo Enviada
    (2, 0.800, 0.205, 0.720, 0.155),   # saldo 92
    (3, 0.920, 0.305, 0.950, 0.360),   # olho
])

annotate("15-detalhe-envio.png", [
    (1, 0.420, 0.300, 0.200, 0.250),   # metricas
    (2, 0.820, 0.455, 0.920, 0.420),   # EXPORTAR CSV
    (3, 0.720, 0.920, 0.880, 0.920),   # ATUALIZAR
])

annotate("16-extrato-apos-envio.png", [
    (1, 0.800, 0.205, 0.720, 0.155),   # saldo 92
    (2, 0.420, 0.480, 0.220, 0.430),   # debito -3
])

print("done")
