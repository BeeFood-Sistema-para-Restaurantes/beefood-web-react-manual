"""Anota os screenshots do manual BeeFood - Capas e Destaques (#48).

Mesmo estilo dos demais manuais: setas finas/sutis em VERDE + badges numerados.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)

Painel e cardapio desktop: 2160x1350 (viewport 1440x900, DPR 1.5).
Cardapio mobile: 780x1688 (viewport 390x844, DPR 2).
Previa do celular: recorte do aside (~481x1175).
LANG=pt_BR.UTF-8 no Chromium.

Sem borrao: nenhuma captura tem dado de cliente.
Duas imagens de contexto (passthrough): a vitrine no desktop e no mobile,
em que o assunto e o banner inteiro.
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


# 01) Cartao na aba Configuracoes + previa
annotate("01-configuracoes-card.png", [
    (1, 0.300, 0.508, 0.175, 0.430),   # titulo Capas e Destaques
    (2, 0.605, 0.508, 0.700, 0.400),   # GERENCIAR (borda do botao)
    (3, 0.885, 0.280, 0.930, 0.140),   # previa do celular (capa)
])

# 02) Modal vazio
annotate("02-modal-vazio.png", [
    (1, 0.500, 0.205, 0.800, 0.145),   # aviso de formato
    (2, 0.340, 0.315, 0.200, 0.300),   # Destaques da capa
    (3, 0.720, 0.315, 0.800, 0.380),   # ADICIONAR (borda)
    (4, 0.360, 0.640, 0.200, 0.640),   # Destaques da sua loja
    (5, 0.705, 0.915, 0.800, 0.850),   # SALVAR (F2)
])

# 03) Imagem do combo
annotate("03-modal-capa-imagem.png", [
    (1, 0.360, 0.375, 0.200, 0.300),   # miniatura + badge imagem
    (2, 0.500, 0.400, 0.200, 0.460),   # Todos os dias · canais
    (3, 0.720, 0.375, 0.800, 0.375),   # interruptor
    (4, 0.705, 0.915, 0.800, 0.850),   # SALVAR
])

# 04) Imagem + video nas capas
annotate("04-modal-capa-video.png", [
    (1, 0.358, 0.435, 0.200, 0.520),   # badge video (segunda linha)
    (2, 0.378, 0.255, 0.200, 0.200),   # contador 2/5 no titulo
    (3, 0.222, 0.358, 0.160, 0.280),   # alca de ordem (primeira linha)
])

# 05) Agenda expandida
annotate("05-modal-agendar.png", [
    (1, 0.340, 0.475, 0.200, 0.420),   # dias da semana
    (2, 0.775, 0.500, 0.850, 0.430),   # Exibir o dia inteiro
    (3, 0.350, 0.575, 0.200, 0.680),   # Delivery / Presencial
    (4, 0.655, 0.340, 0.780, 0.400),   # FECHAR (recolhe) — badge na linha, longe do ADICIONAR
])

# 06) Vitrine da loja
annotate("06-modal-loja.png", [
    (1, 0.380, 0.505, 0.200, 0.430),   # titulo Destaques da sua loja
    (2, 0.375, 0.582, 0.200, 0.560),   # linha da imagem
    (3, 0.375, 0.685, 0.200, 0.760),   # linha do video
    (4, 0.745, 0.915, 0.850, 0.850),   # SALVAR (F2)
])

# 07) Previa do celular (recorte estreito)
annotate("07-preview-celular.png", [
    (1, 0.500, 0.175, 0.160, 0.100),   # carrossel da capa
    (2, 0.500, 0.540, 0.160, 0.620),   # vitrine milkshake
], raio=0.038)

# 08) Cardapio desktop
annotate("08-cardapio-desktop.png", [
    (1, 0.380, 0.220, 0.120, 0.160),   # capa / carrossel do topo
    (2, 0.380, 0.630, 0.120, 0.740),   # vitrine
])

# 09) Vitrine no desktop — o banner e o assunto
passthrough("09-cardapio-desktop-loja.png")

# 10) Cardapio mobile
annotate("10-cardapio-mobile.png", [
    (1, 0.500, 0.155, 0.140, 0.080),   # capa
    (2, 0.500, 0.520, 0.140, 0.620),   # vitrine
], raio=0.028)

# 11) Vitrine no mobile — o banner e o assunto
passthrough("11-cardapio-mobile-loja.png")

print("done")
