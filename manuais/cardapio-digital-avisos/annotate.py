"""Anota os screenshots do manual BeeFood - Avisos do cardapio digital (#47).

Mesmo estilo dos demais manuais: setas finas/sutis em VERDE + badges numerados.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)

Capturas do painel em 2160x1350 (viewport 1440x900, DPR 1.5).
Cardapio publico mobile em 780x1688 (viewport 390x844, DPR 2).
LANG=pt_BR.UTF-8 no Chromium para o campo type=time sair em 24h.

Imagens de contexto (passthrough): o modal do aviso no cardapio, em que o
assunto e o cartaz inteiro — seta so atrapalharia.
Sem borrao: nenhuma captura tem dado de cliente.
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


def annotate(name, markers, ring=None, borrao=None, raio=0.0125, out_name=None):
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
    out_img.save(os.path.join(OUT, out_name or name))
    print("OK", out_name or name)


# 01) Aba vazia
annotate("01-aba-vazia.png", [
    (1, 0.118, 0.705, 0.210, 0.640),   # item Avisos no menu lateral
    (2, 0.520, 0.330, 0.780, 0.250),   # bloco de regras (1:1, so imagem)
    (3, 0.318, 0.640, 0.500, 0.780),   # dropzone Arraste a imagem
])

# 02) Modal recem-aberto, titulo obrigatorio
annotate("02-modal-titulo-vazio.png", [
    (1, 0.560, 0.300, 0.760, 0.240),   # Titulo * Obrigatorio
    (2, 0.500, 0.470, 0.760, 0.520),   # Descricao opcional
    (3, 0.700, 0.860, 0.560, 0.860),   # SALVAR (F2) — borda direita
])

# 03) Feriado preenchido
annotate("03-modal-feriado.png", [
    (1, 0.320, 0.280, 0.220, 0.220),   # cartaz do aviso
    (2, 0.560, 0.290, 0.760, 0.230),   # titulo preenchido
    (3, 0.500, 0.470, 0.760, 0.500),   # descricao
    (4, 0.450, 0.615, 0.240, 0.615),   # dias da semana
    (5, 0.700, 0.860, 0.560, 0.900),   # SALVAR (F2)
])

# 04) Horario com faixa (Dia inteiro desligado)
annotate("04-modal-horario.png", [
    (1, 0.335, 0.615, 0.220, 0.555),   # DOM desmarcado
    (2, 0.680, 0.665, 0.800, 0.610),   # Dia inteiro off
    (3, 0.400, 0.720, 0.260, 0.800),   # Inicio 18:00
    (4, 0.580, 0.720, 0.740, 0.800),   # Fim 23:00
])

# 05) So delivery
annotate("05-modal-delivery.png", [
    (1, 0.348, 0.752, 0.230, 0.690),   # Delivery ligado
    (2, 0.455, 0.752, 0.580, 0.690),   # Presencial desligado
])

# 06) Lista com os 3 cards
annotate("06-lista-tres-avisos.png", [
    (1, 0.280, 0.520, 0.200, 0.400),   # dropzone ainda disponivel
    (2, 0.420, 0.420, 0.420, 0.300),   # card Fechados no feriado
    (3, 0.580, 0.420, 0.620, 0.300),   # card Novo horario
    (4, 0.740, 0.420, 0.820, 0.300),   # card Hoje so delivery
])

# 07) Confirmar remover
annotate("07-confirmar-remover.png", [
    (1, 0.620, 0.560, 0.780, 0.500),   # REMOVER (ENTER) — borda
])

# 09) Cardapio desktop — faixa entre filtro e produtos
annotate("09-cardapio-desktop.png", [
    (1, 0.175, 0.320, 0.080, 0.180),   # Fechados no feriado
    (2, 0.415, 0.320, 0.415, 0.140),   # Novo horario
    (3, 0.655, 0.320, 0.780, 0.180),   # Hoje so delivery
])

# 10) Modal no desktop — o cartaz e o recado (contexto)
passthrough("10-cardapio-desktop-modal.png")

# 11) Cardapio mobile — dois cards no carrossel
annotate("11-cardapio-mobile.png", [
    (1, 0.270, 0.700, 0.120, 0.560),   # Fechados no feriado
    (2, 0.730, 0.700, 0.880, 0.560),   # Novo horario
], raio=0.028)

# 12) Modal no mobile — so fecha (contexto: o cartaz e o assunto)
passthrough("12-cardapio-mobile-modal.png")

print("done")
