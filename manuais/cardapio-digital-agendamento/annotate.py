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


RED = (196, 48, 48)
MINT = (232, 246, 236)
CREAM = (255, 244, 228)
PILL_BG = (255, 236, 220)
OK_BG = (214, 239, 222)
CARD = (255, 255, 255)
W_DID = PAD_P * 2 + COL_W * 2 + MID


def anel(im, box, color, width=6, radius=12):
    out = im.convert("RGBA")
    ov = Image.new("RGBA", out.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    W, H = out.size
    fx, fy, fw, fh = box
    d.rounded_rectangle(
        [fx * W, fy * H, (fx + fw) * W, (fy + fh) * H],
        radius=radius, outline=color + (255,), width=width,
    )
    return Image.alpha_composite(out, ov).convert("RGB")


def _tb(d, text, fnt):
    bb = d.textbbox((0, 0), text, font=fnt)
    return bb[2] - bb[0], bb[3] - bb[1], bb


def _texto_centro(d, y, text, fnt, fill, width):
    tw, th, bb = _tb(d, text, fnt)
    d.text(((width - tw) / 2, y - bb[1]), text, fill=fill, font=fnt)
    return th


def _formula(parts, width, fnt, fnt_hi, bg=CARD):
    """parts: (texto, estilo) estilo = txt | op | hi | ok."""
    probe = Image.new("RGB", (width, 80), bg)
    d = ImageDraw.Draw(probe)
    chunks = []
    total = 0
    gap = 10
    for text, kind in parts:
        f = fnt_hi if kind in ("hi", "ok") else fnt
        tw, th, bb = _tb(d, text, f)
        pad_x = 12 if kind in ("hi", "ok") else 0
        pad_y = 6 if kind in ("hi", "ok") else 0
        chunks.append((text, kind, tw, th, bb, pad_x, pad_y, f))
        total += tw + pad_x * 2 + gap
    total -= gap
    h = max(th + pad_y * 2 for *_, th, _, _, pad_y, _ in chunks) + 8
    im = Image.new("RGB", (width, h), bg)
    d = ImageDraw.Draw(im)
    x = (width - total) / 2
    for text, kind, tw, th, bb, pad_x, pad_y, f in chunks:
        cy = (h - (th + pad_y * 2)) / 2
        if kind == "hi":
            d.rounded_rectangle([x, cy, x + tw + pad_x * 2, cy + th + pad_y * 2], radius=8, fill=PILL_BG)
            d.text((x + pad_x - bb[0], cy + pad_y - bb[1]), text, fill=RED, font=f)
        elif kind == "ok":
            d.rounded_rectangle([x, cy, x + tw + pad_x * 2, cy + th + pad_y * 2], radius=8, fill=OK_BG)
            d.text((x + pad_x - bb[0], cy + pad_y - bb[1]), text, fill=GREEN, font=f)
        else:
            d.text((x - bb[0], (h - th) / 2 - bb[1]), text, fill=DARK, font=f)
        x += tw + pad_x * 2 + gap
    return im


def _card_exemplo(num, titulo, lab_esq, lab_dir, campo, slot, formulas, tint):
    col_max = 500
    img_h = 168
    campo = encaixa(campo, col_max, img_h)
    slot = encaixa(slot, col_max, img_h)
    col_h = max(campo.height, slot.height)
    inner_w = W_DID - 40
    ft = font(18)
    fl = font(14)
    ff = font(20)
    fh = font(22)
    if formulas and isinstance(formulas[0], tuple):
        formulas = [formulas]
    forms = [_formula(p, inner_w - 32, ff, fh, tint) for p in formulas]
    form_h = sum(f.height for f in forms) + 4 * (len(forms) - 1)
    H = 16 + 28 + 22 + col_h + 14 + form_h + 16
    card = Image.new("RGB", (inner_w, H), tint)
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, inner_w - 1, H - 1], radius=16, outline=(210, 210, 210), width=1)
    d.ellipse([8, 14, 34, 40], fill=GREEN)
    tw, th, bb = _tb(d, str(num), font(16))
    d.text((21 - tw / 2 - bb[0], 27 - th / 2 - bb[1]), str(num), fill=WHITE, font=font(16))
    d.text((42, 18), titulo, fill=DARK, font=ft)
    y_lab = 48
    x_esq = 16
    x_dir = inner_w // 2 + 12
    col_w = (inner_w - 56) // 2
    for lab, x in ((lab_esq, x_esq), (lab_dir, x_dir)):
        tw, _, bb = _tb(d, lab, fl)
        d.text((x + (col_w - tw) / 2, y_lab - bb[1]), lab, fill=MUTED, font=fl)
    y_img = y_lab + 22
    cola_redondo(card, campo, (x_esq + (col_w - campo.width) // 2, y_img + (col_h - campo.height) // 2), 12)
    cola_redondo(card, slot, (x_dir + (col_w - slot.width) // 2, y_img + (col_h - slot.height) // 2), 12)
    seta_meio(d, x_esq + col_w + 4, y_img + col_h / 2, x_dir - 4)
    fy = y_img + col_h + 12
    for form in forms:
        card.paste(form, (16, fy))
        fy += form.height + 4
    return card


def _timeline():
    """Linha do dia: abre + 60 → 1ª faixa … última faixa + 60 → fecha."""
    w = W_DID - 40
    h = 118
    im = Image.new("RGB", (w, h), CARD)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=16, outline=(210, 210, 210), width=1)
    ft = font(15)
    fs = font(13)
    _texto_centro(d, 10, "Neste dia (abre 01:00 · fecha 23:59)", ft, DARK, w)
    y = 48
    x0, x1 = 20, w - 20
    bar_h = 18
    # proporção só didática, não em escala de 24 h
    marks = [
        (0.00, "01:00", "abre", MUTED),
        (0.18, "02:00", "1ª faixa", GREEN),
        (0.82, "22:00", "última", GREEN),
        (1.00, "23:59", "fecha", MUTED),
    ]
    d.rounded_rectangle([x0, y, x1, y + bar_h], radius=8, fill=(226, 226, 228))
    xa = x0 + (x1 - x0) * 0.18
    xb = x0 + (x1 - x0) * 0.82
    d.rounded_rectangle([xa, y, xb, y + bar_h], radius=8, fill=GREEN)
    d.rectangle([x0, y, xa, y + bar_h], fill=RED)
    d.rectangle([xb, y, x1, y + bar_h], fill=RED)
    for t, label, sub, col in marks:
        mx = x0 + (x1 - x0) * t
        d.line([(mx, y - 4), (mx, y + bar_h + 4)], fill=col, width=2)
        tw, th, bb = _tb(d, label, fs)
        tx = min(max(mx - tw / 2, 8), w - tw - 8)
        d.text((tx, y + bar_h + 10 - bb[1]), label, fill=col, font=fs)
        tw2, _, bb2 = _tb(d, sub, fs)
        tx2 = min(max(mx - tw2 / 2, 8), w - tw2 - 8)
        d.text((tx2, y + bar_h + 26 - bb2[1]), sub, fill=col, font=fs)
    # setas dos 60
    d.text((x0 + 8, y + 1), "60", fill=WHITE, font=fs)
    d.text((xb + 8, y + 1), "60", fill=WHITE, font=fs)
    return im


def _caixa_almoco():
    w = W_DID - 40
    ft = font(16)
    ff = font(18)
    fh = font(20)
    linhas = [
        "Mesma conta no almoço típico (grade 11:00–15:00, também 60 e 60)",
        None,
        [("abre 11:00", "txt"), ("+", "op"), ("60 min", "hi"), ("=", "op"), ("12:00 – 12:30", "ok")],
        [("fecha 15:00", "txt"), ("−", "op"), ("60 min", "hi"), ("=", "op"), ("limite 14:00", "txt")],
    ]
    form1 = _formula(linhas[2], w - 32, ff, fh, CREAM)
    form2 = _formula(linhas[3], w - 32, ff, fh, CREAM)
    h = 16 + 24 + 8 + form1.height + 6 + form2.height + 16
    im = Image.new("RGB", (w, h), CREAM)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=16, outline=(230, 200, 160), width=1)
    _texto_centro(d, 12, linhas[0], ft, DARK, w)
    im.paste(form1, (16, 42))
    im.paste(form2, (16, 42 + form1.height + 6))
    return im


def _nota_intervalo():
    w = W_DID - 40
    h = 52
    im = Image.new("RGB", (w, h), (236, 236, 238))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=12, outline=(210, 210, 210), width=1)
    fnt = font(15)
    t = "Intervalo 60 é outra conta: o começo da próxima faixa (02:00, 03:00…). A faixa em si dura 30 min."
    _texto_centro(d, 16, t, fnt, DARK, w)
    return im


def montar_horarios_didatico(nome_out):
    """Dois exemplos separados: iniciar 60 → 1ª faixa; finalizar 60 → última."""
    ini = anel(
        crop_frac("02-tempo.png", (0.225, 0.400, 0.355, 0.195)),
        (0.02, 0.66, 0.28, 0.30), RED, 5, 10,
    )
    fim = anel(
        crop_frac("02-tempo.png", (0.575, 0.400, 0.385, 0.195)),
        (0.02, 0.66, 0.26, 0.30), RED, 5, 10,
    )
    slot_ini = anel(
        crop_frac("05-cel-calendario.png", (0.00, 0.198, 1.00, 0.145)),
        (0.10, 0.38, 0.62, 0.36), GREEN, 5, 10,
    )
    slot_fim = anel(
        crop_frac("06-cel-horarios.png", (0.00, 0.70, 1.00, 0.085)),
        (0.10, 0.15, 0.72, 0.72), GREEN, 5, 10,
    )
    c1 = _card_exemplo(
        1,
        "Iniciar depois de aberto 60  →  primeira faixa",
        "No painel",
        "No cardápio",
        ini,
        slot_ini,
        [("abre 01:00", "txt"), ("+", "op"), ("60 min", "hi"), ("=", "op"), ("02:00 – 02:30", "ok")],
        MINT,
    )
    c2 = _card_exemplo(
        2,
        "Finalizar antes de fechar 60  →  última faixa",
        "No painel",
        "No cardápio",
        fim,
        slot_fim,
        [
            [("fecha 23:59", "txt"), ("−", "op"), ("60 min", "hi"), ("=", "op"), ("limite 22:59", "txt")],
            [("última faixa que cabe", "txt"), ("=", "op"), ("22:00 – 22:30", "ok")],
        ],
        CREAM,
    )
    tl = _timeline()
    alm = _caixa_almoco()
    nota = _nota_intervalo()
    gap = 14
    blocos = [c1, c2, tl, alm, nota]
    inner_h = sum(b.height for b in blocos) + gap * (len(blocos) - 1)
    H = 20 + 44 + 8 + inner_h + 20
    canvas = Image.new("RGB", (W_DID, H), BG)
    d = ImageDraw.Draw(canvas)
    ft = font(21)
    fs = font(14)
    _texto_centro(d, 16, "Os dois 60 cortam a janela  —  não são o intervalo", ft, DARK, W_DID)
    _texto_centro(d, 42, "Cada campo tem a própria conta. Veja o exemplo.", fs, MUTED, W_DID)
    y = 72
    x = (W_DID - c1.width) // 2
    for b in blocos:
        canvas.paste(b, (x, y))
        y += b.height + gap
    canvas.save(os.path.join(SRC, nome_out))
    canvas.save(os.path.join(OUT, nome_out))
    print("DIDATICO", nome_out, canvas.size)
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

montar_horarios_didatico("04-par-horarios.png")

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
