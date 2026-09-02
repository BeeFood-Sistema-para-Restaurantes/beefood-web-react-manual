"""Anota screenshots — #77 Cardápio digital presencial e QR Code.

Coordenadas em frações (0..1). Cada marcador:
  (numero, alvo_x, alvo_y, badge_x, badge_y)
Painel: 2160×1350 (viewport 1440×900, DPR 1.5).
Celular: 780×1688 (viewport 390×844, DPR 2).
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
FONT_CANDIDATES = [
    r"C:\Windows\Fonts\arialbd.ttf",
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def font(sz):
    for c in FONT_CANDIDATES:
        if os.path.exists(c):
            return ImageFont.truetype(c, sz)
    raise RuntimeError("fonte bold nao encontrada")


def draw_arrow(d, x0, y0, x1, y1, w):
    col = GREEN + (A_LINE,)
    d.line([(x0, y0), (x1, y1)], fill=col, width=w)
    ang = math.atan2(y1 - y0, x1 - x0)
    L = w * 3.6
    for s in (0.45, -0.45):
        d.line([(x1, y1), (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))], fill=col, width=w)


def badge(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], fill=WHITE + (235,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN + (A_BADGE,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]), t, fill=WHITE, font=fnt)


def passthrough(name, out_name=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGB")
    dest = out_name or name
    img.save(os.path.join(OUT, dest))
    print("OK (contexto)", dest)


def annotate(name, markers, ring=None, raio=0.0125, out_name=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    W, H = img.size
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
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, out_name or name))
    print("OK", out_name or name, W, H)


PHONE_W = 380
GAP = 18
PAD = 22
CAP_H = 44


def montar_celulares(nome_out, paineis):
    fnt = font(20)
    phones = []
    for nome, _ in paineis:
        im = Image.open(os.path.join(SRC, nome)).convert("RGB")
        h = int(im.height * PHONE_W / im.width)
        phones.append(im.resize((PHONE_W, h), Image.Resampling.LANCZOS))
    ph_h = phones[0].height
    n = len(phones)
    W = PAD * 2 + n * PHONE_W + (n - 1) * GAP
    H = PAD + CAP_H + ph_h + PAD
    canvas = Image.new("RGB", (W, H), (244, 244, 245))
    d = ImageDraw.Draw(canvas)
    for i, (im, (_, titulo)) in enumerate(zip(phones, paineis)):
        x = PAD + i * (PHONE_W + GAP)
        y = PAD + CAP_H
        bb = d.textbbox((0, 0), titulo, font=fnt)
        tw = bb[2] - bb[0]
        d.text((x + (PHONE_W - tw) / 2, PAD + 10), titulo, fill=(40, 40, 40), font=fnt)
        mask = Image.new("L", (PHONE_W, ph_h), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, PHONE_W - 1, ph_h - 1], radius=26, fill=255)
        canvas.paste(im, (x, y), mask)
        d.rounded_rectangle([x, y, x + PHONE_W - 1, y + ph_h - 1], radius=26, outline=(200, 200, 200), width=2)
    canvas.save(os.path.join(SRC, nome_out))
    print("MONTAR", nome_out, canvas.size)
    return W, H, ph_h


def no_painel(i, tx, ty, W, H, ph_h):
    x = PAD + i * (PHONE_W + GAP) + tx * PHONE_W
    y = PAD + CAP_H + ty * ph_h
    return x / W, y / H


if __name__ == "__main__":
    # 01) Aba + card Presencial (viewport inteiro)
    annotate("01-onde-fica.png", [
        (1, 0.235, 0.078, 0.235, 0.020),   # aba Configurações
        (2, 0.330, 0.385, 0.250, 0.300),   # título Presencial
        (3, 0.638, 0.385, 0.720, 0.300),   # switch Presencial Ativo
        (4, 0.430, 0.490, 0.560, 0.430),   # link /?tipo=p
        (5, 0.300, 0.585, 0.220, 0.660),   # botões QR
    ])

    # 02) recorte do card — cadastro e opções
    annotate("02-parametros.png", [
        (1, 0.720, 0.520, 0.900, 0.430),   # Cadastro
        (2, 0.580, 0.780, 0.520, 0.900),   # E-mail
        (3, 0.820, 0.780, 0.920, 0.900),   # Nascimento
        (4, 0.155, 0.630, 0.070, 0.560),   # Garçom
        (5, 0.155, 0.760, 0.070, 0.850),   # Fechamento
    ], raio=0.018)

    # 03) modal opções do garçom
    annotate("03-garcom-opcoes.png", [
        (1, 0.380, 0.390, 0.260, 0.280),   # switch Copo
        (2, 0.620, 0.790, 0.720, 0.860),   # FECHAR (ESC)
    ])

    # 04) QR geral
    annotate("04-qr-geral.png", [
        (1, 0.500, 0.430, 0.320, 0.280),   # o QR
        (2, 0.455, 0.715, 0.350, 0.715),   # Download
        (3, 0.545, 0.715, 0.660, 0.715),   # Imprimir
    ])

    # 05) QR mesa gerados
    annotate("05-qr-mesa.png", [
        (1, 0.360, 0.300, 0.250, 0.230),   # Mesa Inicial / Final
        (2, 0.520, 0.300, 0.640, 0.230),   # Gerar QR Codes
        (3, 0.680, 0.400, 0.800, 0.340),   # Download / Imprimir Todos
    ])

    # 06) Meus Links — grupo presencial (Sem mesa / Sem comanda)
    annotate("06-meus-links.png", [
        (1, 0.075, 0.825, 0.185, 0.770),   # Meus Links (rodapé)
        (2, 0.780, 0.505, 0.680, 0.450),   # CARDÁPIOS PRESENCIAL
        (3, 0.730, 0.640, 0.660, 0.560),   # Sem mesa
        (4, 0.850, 0.640, 0.920, 0.560),   # Sem comanda
        (5, 0.800, 0.730, 0.680, 0.790),   # olho · copiar · WhatsApp · QR (pedir)
        (6, 0.800, 0.880, 0.680, 0.940),   # Cardápio de visualização
    ])

    # 07) Mesa 2 escolhida — URL com ?mesa=2
    annotate("07-meus-links-mesa.png", [
        (1, 0.730, 0.650, 0.650, 0.580),   # Mesa 2
        (2, 0.800, 0.700, 0.680, 0.700),   # URL ?mesa=2
        (3, 0.800, 0.745, 0.680, 0.820),   # ícones deste link (Mesa 2)
    ])

    # 08) gerador passo 1
    annotate("08-gerador-passo1.png", [
        (1, 0.350, 0.500, 0.240, 0.320),   # QR Codes de Mesas
        (2, 0.650, 0.500, 0.780, 0.320),   # QR Codes de Comandas
    ])

    # 09) tipo de QR
    annotate("09-tipo-qr.png", [
        (1, 0.350, 0.500, 0.240, 0.300),   # Cardápio Digital Presencial
        (2, 0.650, 0.500, 0.780, 0.300),   # Código da Mesa
    ])

    # 09c) recomendação comanda (gate)
    annotate("09c-gate-comanda.png", [
        (1, 0.320, 0.420, 0.200, 0.250),   # não recomendado
        (2, 0.680, 0.420, 0.820, 0.250),   # recomendado
        (3, 0.720, 0.820, 0.820, 0.900),   # QUERO GERAR DE COMANDA
    ], out_name="09b-recomendacao-comanda.png")

    W, H, ph_h = montar_celulares("10-cardapio-digital.png", [
        ("10-cel-presencial-home.png", "Pedir  ·  /?tipo=p"),
        ("11-cel-visualizacao.png", "Só olhar  ·  visualização"),
    ])
    t1 = no_painel(0, 0.50, 0.955, W, H, ph_h)
    t2 = no_painel(1, 0.50, 0.955, W, H, ph_h)
    annotate("10-cardapio-digital.png", [
        (1, t1[0], t1[1], t1[0] - 0.04, t1[1] - 0.10),
        (2, t2[0], t2[1], t2[0] + 0.04, t2[1] - 0.10),
    ], raio=0.016)

    print("done")

