"""Anota screenshots — #71 Aparência e layout do cardápio digital."""
import os
import math
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
        d.line(
            [(x1, y1), (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))],
            fill=col,
            width=w,
        )


def badge(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], fill=WHITE + (235,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN + (A_BADGE,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text(
        (cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
        t,
        fill=WHITE,
        font=fnt,
    )


def annotate(name, markers, ring=None, out_name=None):
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
    dest = out_name or name
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, dest))
    print("OK", dest, W, H)


def passthrough(name, out_name=None):
    im = Image.open(os.path.join(SRC, name)).convert("RGB")
    dest = out_name or name
    im.save(os.path.join(OUT, dest))
    print("PASS", dest, im.size)


BG = (244, 244, 245)
DARK = (40, 40, 40)
MUTED = (100, 100, 100)
MID = 56
COL_W = 620
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
    nw, nh = max(1, int(w * scale)), max(1, int(h * scale))
    return im.resize((nw, nh), Image.Resampling.LANCZOS)


def cola_redondo(canvas, im, xy, radius=RADIUS):
    w, h = im.size
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=255)
    canvas.paste(im, xy, mask)
    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle(
        [xy[0], xy[1], xy[0] + w - 1, xy[1] + h - 1],
        radius=radius,
        outline=(200, 200, 200),
        width=2,
    )


def seta_meio(d, x0, y, x1):
    w = 4
    d.line([(x0, y), (x1, y)], fill=GREEN, width=w)
    L = 14
    d.line([(x1, y), (x1 - L * math.cos(-0.45), y - L * math.sin(-0.45))], fill=GREEN, width=w)
    d.line([(x1, y), (x1 - L * math.cos(0.45), y + L * math.sin(0.45))], fill=GREEN, width=w)


def empilha(imgs, gap=12):
    w = max(i.width for i in imgs)
    h = sum(i.height for i in imgs) + gap * (len(imgs) - 1)
    out = Image.new("RGB", (w, h), BG)
    y = 0
    for im in imgs:
        out.paste(im, ((w - im.width) // 2, y))
        y += im.height + gap
    return out


def montar_par(nome_out, titulo, esq, dir_, lab_esq, lab_dir, rodape, max_h=460):
    if isinstance(esq, list):
        esq = empilha(esq)
    if isinstance(dir_, list):
        dir_ = empilha(dir_)
    esq = encaixa(esq, COL_W, max_h)
    dir_ = encaixa(dir_, COL_W, max_h)
    col_h = max(esq.height, dir_.height)
    W = PAD_P * 2 + COL_W * 2 + MID
    H = PAD_P + TIT_H + LAB_H + col_h + FOOT_H + PAD_P
    canvas = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(canvas)
    ft = font(22)
    fl = font(16)
    fr = font(15)
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
    return canvas


def montar_dois_pares(nome_out, titulo, par1, par2):
    """par = (esq, dir, lab_esq, lab_dir, sub)."""
    cards = []
    inner_w = PAD_P * 2 + COL_W * 2 + MID - 40
    for esq, dir_, lab_e, lab_d, sub in (par1, par2):
        esq = encaixa(esq, 500, 280)
        dir_ = encaixa(dir_, 500, 280)
        col_h = max(esq.height, dir_.height)
        h = 28 + 22 + col_h + 36
        card = Image.new("RGB", (inner_w, h), (255, 255, 255))
        d = ImageDraw.Draw(card)
        d.rounded_rectangle([0, 0, inner_w - 1, h - 1], radius=16, outline=(210, 210, 210), width=1)
        fl = font(15)
        fs = font(14)
        y_lab = 10
        x_esq = 16
        x_dir = inner_w // 2 + 12
        col_w = (inner_w - 56) // 2
        for lab, x in ((lab_e, x_esq), (lab_d, x_dir)):
            bb = d.textbbox((0, 0), lab, font=fl)
            d.text((x + (col_w - (bb[2] - bb[0])) / 2, y_lab), lab, fill=MUTED, font=fl)
        y_img = 34
        cola_redondo(card, esq, (x_esq + (col_w - esq.width) // 2, y_img + (col_h - esq.height) // 2), 12)
        cola_redondo(card, dir_, (x_dir + (col_w - dir_.width) // 2, y_img + (col_h - dir_.height) // 2), 12)
        seta_meio(d, x_esq + col_w + 4, y_img + col_h / 2, x_dir - 4)
        bb = d.textbbox((0, 0), sub, font=fs)
        d.text(((inner_w - (bb[2] - bb[0])) / 2, y_img + col_h + 10), sub, fill=DARK, font=fs)
        cards.append(card)
    gap = 16
    inner_h = sum(c.height for c in cards) + gap
    W = inner_w + 40
    H = 20 + 44 + inner_h + 20
    canvas = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(canvas)
    ft = font(21)
    bb = d.textbbox((0, 0), titulo, font=ft)
    d.text(((W - (bb[2] - bb[0])) / 2, 18), titulo, fill=DARK, font=ft)
    y = 64
    x = 20
    for c in cards:
        canvas.paste(c, (x, y))
        y += c.height + gap
    canvas.save(os.path.join(SRC, nome_out))
    canvas.save(os.path.join(OUT, nome_out))
    print("DOIS", nome_out, canvas.size)
    return canvas


# --- 01: onde fica ---
annotate("00-admin-full.png", [
    (1, 0.095, 0.268, 0.185, 0.205),
    (2, 0.638, 0.398, 0.730, 0.310),
    (3, 0.268, 0.448, 0.185, 0.390),
    (4, 0.305, 0.812, 0.210, 0.755),
    (5, 0.505, 0.812, 0.620, 0.755),
], out_name="01-onde-fica.png")

# --- 02: capa/logo → cardápio ---
montar_par(
    "02-par-capa-logo.png",
    "Capa e logo  →  topo do cardápio",
    crop_frac("02-preview.png", (0.00, 0.00, 1.00, 1.00)),
    crop_frac("10-cel-home-lista.png", (0.00, 0.00, 1.00, 0.42)),
    "No painel (clique na câmera)",
    "No cardápio",
    "Capa = foto larga do topo. Logo = círculo sobre a capa. Máximo 1 MB (PNG, JPG ou WEBP).",
    max_h=580,
)

# --- 03: cor do tema (o modal já é o resultado lado a lado) ---
annotate("03b-modal-cor-tema.png", [
    (1, 0.120, 0.145, 0.220, 0.090),
    (2, 0.280, 0.880, 0.180, 0.800),
    (3, 0.780, 0.880, 0.880, 0.800),
], out_name="03-cor-tema.png")

# --- 04: lista completa (uma figura só para caber zoom) ---
montar_par(
    "04-par-lista.png",
    "Lista completa  →  primeiro setor no cardápio",
    crop_frac("04b-layout-setor.png", (0.00, 0.00, 0.50, 1.00)),
    empilha([
        crop_frac("10-cel-home-lista.png", (0.00, 0.66, 1.00, 0.08)),
        crop_frac("10b-cel-home-lista-produtos.png", (0.00, 0.40, 1.00, 0.50)),
    ], gap=8),
    "No painel",
    "No cardápio",
    "Uma página só. O cliente rola e usa o filtro de setores.",
    max_h=700,
)

# --- 05: navegação por setores ---
montar_par(
    "05-par-setores.png",
    "Navegação por setores  →  grid no cardápio",
    crop_frac("04b-layout-setor.png", (0.50, 0.00, 0.50, 1.00)),
    crop_frac("13-cel-home-setores.png", (0.00, 0.00, 1.00, 1.00)),
    "No painel",
    "No cardápio",
    "Primeira tela = grid de setores. Setor sem foto usa o logo da loja.",
    max_h=700,
)

# --- 06: em rolagem ---
montar_par(
    "06-par-rolagem.png",
    "Em Rolagem  →  todos os grupos na mesma tela",
    crop_frac("04c-layout-opcoes.png", (0.00, 0.00, 0.50, 1.00)),
    crop_frac("11-cel-produto-rolagem.png", (0.00, 0.00, 1.00, 0.78)),
    "No painel",
    "No cardápio",
    "Burger, acompanhamentos e bebidas na mesma tela. Vale para a loja inteira.",
    max_h=700,
)

# --- 07: em passos ---
montar_par(
    "07-par-passos.png",
    "Em Passos  →  um grupo por vez",
    crop_frac("04c-layout-opcoes.png", (0.50, 0.00, 0.50, 1.00)),
    crop_frac("14-cel-produto-passos.png", (0.00, 0.22, 1.00, 0.78)),
    "No painel",
    "No cardápio",
    "1 · 2 · 3 e o botão Próximo. Vale para a loja inteira.",
    max_h=700,
)

# --- 08: vitrine ---
montar_par(
    "08-par-vitrine.png",
    "Vitrine de Promoções  →  aba Promoções",
    crop_frac("05b-vitrine-aberta.png", (0.220, 0.520, 0.500, 0.360)),
    crop_frac("12-cel-promocoes.png", (0.00, 0.00, 1.00, 0.70)),
    "No painel",
    "No cardápio",
    "Aba só aparece se existir produto com preço promocional valendo agora.",
    max_h=580,
)

print("done")
