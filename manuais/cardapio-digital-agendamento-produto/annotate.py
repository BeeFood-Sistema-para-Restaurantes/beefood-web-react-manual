"""Anota screenshots — #72 Produto só com agendamento (encomenda)."""
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


def annotate(name, markers, ring=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    W, H = img.size
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
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, name))
    print("OK", name, W, H)


# ---------- tira de celulares ----------
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


# ---------- par painel -> cardapio ----------
BG = (244, 244, 245)
DARK = (40, 40, 40)
MUTED = (100, 100, 100)
MID = 56
COL_W = 560
PAD_P = 28
TIT_H = 46
LAB_H = 32
FOOT_H = 56
RADIUS = 18


def crop_frac(name, box):
    im = Image.open(os.path.join(SRC, name)).convert("RGB")
    W, H = im.size
    x, y, w, h = box
    return im.crop((int(x * W), int(y * H), int((x + w) * W), int((y + h) * H)))


def encaixa(im, max_w, max_h):
    w, h = im.size
    scale = min(max_w / w, max_h / h)
    return im.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.Resampling.LANCZOS)


def cola_redondo(canvas, im, xy, radius=RADIUS):
    w, h = im.size
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=255)
    canvas.paste(im, xy, mask)
    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle([xy[0], xy[1], xy[0] + w - 1, xy[1] + h - 1], radius=radius,
                        outline=(200, 200, 200), width=2)


def seta_meio(d, x0, y, x1):
    w = 4
    d.line([(x0, y), (x1, y)], fill=GREEN, width=w)
    L = 14
    d.line([(x1, y), (x1 - L * math.cos(-0.45), y - L * math.sin(-0.45))], fill=GREEN, width=w)
    d.line([(x1, y), (x1 - L * math.cos(0.45), y + L * math.sin(0.45))], fill=GREEN, width=w)


def montar_par(nome_out, titulo, esq, dir_, lab_esq, lab_dir, rodape, max_h=420):
    esq = encaixa(esq, COL_W, max_h)
    dir_ = encaixa(dir_, COL_W, max_h)
    col_h = max(esq.height, dir_.height)
    W = PAD_P * 2 + COL_W * 2 + MID
    H = PAD_P + TIT_H + LAB_H + col_h + FOOT_H + PAD_P
    canvas = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(canvas)
    ft, fl, fr = font(22), font(16), font(15)
    bb = d.textbbox((0, 0), titulo, font=ft)
    d.text(((W - (bb[2] - bb[0])) / 2, PAD_P + 8), titulo, fill=DARK, font=ft)
    y_lab = PAD_P + TIT_H
    y_img = y_lab + LAB_H
    x_esq = PAD_P
    x_dir = PAD_P + COL_W + MID
    for lab, x in ((lab_esq, x_esq), (lab_dir, x_dir)):
        bb = d.textbbox((0, 0), lab, font=fl)
        d.text((x + (COL_W - (bb[2] - bb[0])) / 2, y_lab + 6), lab, fill=MUTED, font=fl)
    cola_redondo(canvas, esq, (x_esq + (COL_W - esq.width) // 2, y_img + (col_h - esq.height) // 2))
    cola_redondo(canvas, dir_, (x_dir + (COL_W - dir_.width) // 2, y_img + (col_h - dir_.height) // 2))
    seta_meio(d, x_esq + COL_W + 10, y_img + col_h / 2, x_dir - 10)
    bb = d.textbbox((0, 0), rodape, font=fr)
    d.text(((W - (bb[2] - bb[0])) / 2, y_img + col_h + 16), rodape, fill=DARK, font=fr)
    canvas.save(os.path.join(SRC, nome_out))
    canvas.save(os.path.join(OUT, nome_out))
    print("PAR", nome_out, canvas.size)


# ============================== figuras ==============================

annotate("01-lista-antes.png", [
    (1, 0.168, 0.545, 0.115, 0.660),
    (2, 0.800, 0.122, 0.700, 0.055),
])

annotate("02-lote-selecao.png", [
    (1, 0.610, 0.172, 0.640, 0.098),
    (2, 0.300, 0.244, 0.225, 0.222),
    (3, 0.298, 0.288, 0.228, 0.330),
    (4, 0.685, 0.858, 0.800, 0.815),
])

annotate("03-lote-campo.png", [
    (1, 0.303, 0.794, 0.225, 0.760),
    (2, 0.667, 0.780, 0.790, 0.730),
    (3, 0.730, 0.878, 0.820, 0.910),
])

annotate("04-lote-resultado.png", [
    (1, 0.640, 0.153, 0.555, 0.115),
    (2, 0.293, 0.207, 0.225, 0.245),
    (3, 0.740, 0.878, 0.825, 0.910),
])

annotate("05-lista-depois.png", [
    (1, 0.776, 0.272, 0.855, 0.335),
    (2, 0.442, 0.258, 0.535, 0.140),
])

annotate("06-produto-switch.png", [
    (1, 0.318, 0.262, 0.240, 0.222),
    (2, 0.353, 0.510, 0.258, 0.468),
    (3, 0.680, 0.898, 0.680, 0.958),
])

montar_par(
    "07-par-encomenda.png",
    "Somente Agendamento = Sim  →  etiqueta Encomenda",
    crop_frac("03-lote-campo.png", (0.278, 0.690, 0.450, 0.200)),
    crop_frac("07-cel-lista.png", (0.00, 0.455, 1.00, 0.235)),
    "No painel (Editar em Lote)",
    "No cardápio digital",
    "O produto continua à venda, mas com a marca Encomenda — e só sai com data e hora.",
    max_h=320,
)

celulares = ("07-cel-lista.png", "09-cel-ajuda.png", "11-cel-agendar.png")
if all(os.path.exists(os.path.join(SRC, n)) for n in celulares):
    W, H, ph_h = montar_celulares("08-cardapio-digital.png", [
        ("07-cel-lista.png", "Etiqueta Encomenda"),
        ("09-cel-ajuda.png", "O que ela quer dizer"),
        ("11-cel-agendar.png", "Continuar abre AGENDAR PEDIDO"),
    ])
    p = lambda i, tx, ty: no_painel(i, tx, ty, W, H, ph_h)
    a1, b1 = p(0, 0.300, 0.583), p(0, 0.640, 0.610)
    a2, b2 = p(1, 0.735, 0.818), p(1, 0.880, 0.880)
    a3, b3 = p(2, 0.750, 0.040), p(2, 0.880, 0.120)
    annotate("08-cardapio-digital.png", [
        (1, a1[0], a1[1], b1[0], b1[1]),
        (2, a2[0], a2[1], b2[0], b2[1]),
        (3, a3[0], a3[1], b3[0], b3[1]),
    ])

print("done")
