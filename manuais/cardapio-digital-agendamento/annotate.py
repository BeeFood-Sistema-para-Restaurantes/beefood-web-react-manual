"""Anota screenshots — #70 Agendamento do cardápio digital."""
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
    nw, nh = max(1, int(w * scale)), max(1, int(h * scale))
    return im.resize((nw, nh), Image.Resampling.LANCZOS)


def cola_redondo(canvas, im, xy, radius=RADIUS):
    w, h = im.size
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=255)
    canvas.paste(im, xy, mask)
    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle([xy[0], xy[1], xy[0] + w - 1, xy[1] + h - 1], radius=radius, outline=(200, 200, 200), width=2)


def seta_meio(d, x0, y, x1):
    w = 4
    ym = y
    d.line([(x0, ym), (x1, ym)], fill=GREEN, width=w)
    ang = 0
    L = 14
    d.line([(x1, ym), (x1 - L * math.cos(ang - 0.45), ym - L * math.sin(-0.45))], fill=GREEN, width=w)
    d.line([(x1, ym), (x1 - L * math.cos(ang + 0.45), ym + L * math.sin(0.45))], fill=GREEN, width=w)


def empilha(imgs, gap=12):
    w = max(i.width for i in imgs)
    h = sum(i.height for i in imgs) + gap * (len(imgs) - 1)
    out = Image.new("RGB", (w, h), BG)
    y = 0
    for im in imgs:
        out.paste(im, ((w - im.width) // 2, y))
        y += im.height + gap
    return out


def montar_par(nome_out, titulo, esq, dir_, lab_esq, lab_dir, rodape):
    """Painel (esq) → cardápio (dir). esq/dir: Image ou lista de Images."""
    if isinstance(esq, list):
        esq = empilha(esq)
    if isinstance(dir_, list):
        dir_ = empilha(dir_)
    max_h = 420
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
    cx0 = x_esq + COL_W + 10
    cx1 = x_dir - 10
    seta_meio(d, cx0, y_img + col_h / 2, cx1)
    bb = d.textbbox((0, 0), rodape, font=fr)
    d.text(((W - (bb[2] - bb[0])) / 2, y_img + col_h + 16), rodape, fill=DARK, font=fr)
    canvas.save(os.path.join(SRC, nome_out))
    canvas.save(os.path.join(OUT, nome_out))
    print("PAR", nome_out, canvas.size)
    return canvas.size


annotate("01-aba-switches.png", [
    (1, 0.078, 0.325, 0.165, 0.260),
    (2, 0.500, 0.175, 0.280, 0.130),
    (3, 0.860, 0.355, 0.740, 0.305),
    (4, 0.860, 0.470, 0.740, 0.530),
    (5, 0.860, 0.590, 0.740, 0.650),
])

montar_par(
    "02-par-chaves.png",
    "As três chaves  →  Hoje e Agendar",
    crop_frac("01-aba-switches.png", (0.230, 0.285, 0.735, 0.400)),
    crop_frac("04-cel-hoje-agendar.png", (0.02, 0.165, 0.96, 0.40)),
    "No painel",
    "No cardápio",
    "Agendamento ligado: aparecem Hoje (agora) e Agendar. Só aceita off = os dois botões.",
)

montar_par(
    "03-par-dias.png",
    "Dias mínimo 2 e máximo 7  →  faixa Dia",
    crop_frac("02-tempo.png", (0.225, 0.175, 0.740, 0.250)),
    crop_frac("05-cel-calendario.png", (0.00, 0.000, 1.00, 0.230)),
    "No painel",
    "No cardápio",
    "Primeira bolinha = TER 01 (mínimo 2). Sem HOJE nem amanhã. Máximo 7 = sete dias a partir daí.",
)

montar_par(
    "04-par-horarios.png",
    "60 min depois / 60 antes / intervalo 60  →  Hora Aproximada",
    [
        crop_frac("02-tempo.png", (0.225, 0.400, 0.740, 0.200)),
        crop_frac("02-tempo.png", (0.225, 0.700, 0.740, 0.230)),
    ],
    [
        crop_frac("05-cel-calendario.png", (0.00, 0.198, 1.00, 0.250)),
        crop_frac("06-cel-horarios.png", (0.00, 0.540, 1.00, 0.250)),
    ],
    "No painel",
    "No cardápio",
    "Primeira faixa 02:00–02:30 (abre 01:00 + 60). Última 22:00–22:30. Intervalo 60 = de hora em hora.",
)

if all(os.path.exists(os.path.join(SRC, n)) for n in (
    "04-cel-hoje-agendar.png", "05-cel-calendario.png", "06-cel-horarios.png"
)):
    W, H, ph_h = montar_celulares("05-cardapio-digital.png", [
        ("04-cel-hoje-agendar.png", "Hoje ou Agendar"),
        ("05-cel-calendario.png", "Dias do calendário"),
        ("06-cel-horarios.png", "Horários do dia"),
    ])
    f1 = lambda tx, ty: no_painel(0, tx, ty, W, H, ph_h)
    f2 = lambda tx, ty: no_painel(1, tx, ty, W, H, ph_h)
    f3 = lambda tx, ty: no_painel(2, tx, ty, W, H, ph_h)
    a1 = f1(0.72, 0.455)
    b1 = f1(0.16, 0.34)
    a2 = f2(0.18, 0.155)
    b2 = f2(0.12, 0.07)
    a3 = f3(0.42, 0.74)
    b3 = f3(0.14, 0.62)
    annotate("05-cardapio-digital.png", [
        (1, a1[0], a1[1], b1[0], b1[1]),
        (2, a2[0], a2[1], b2[0], b2[1]),
        (3, a3[0], a3[1], b3[0], b3[1]),
    ])

print("done")
