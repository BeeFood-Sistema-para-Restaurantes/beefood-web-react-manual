"""Anota os screenshots do manual #17 BeeFood Pixel Analytics.

Le de imagens-puras/ e escreve em imagens-tratadas/.
Coordenadas em fracoes 0..1, medidas com grade de fracoes.
"""
import math
import os

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
    for caminho in FONT_CANDIDATES:
        if os.path.exists(caminho):
            return ImageFont.truetype(caminho, sz)
    raise RuntimeError("nenhuma fonte bold encontrada")


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


def passthrough(name):
    img = Image.open(os.path.join(SRC, name)).convert("RGB")
    img.save(os.path.join(OUT, name))
    print("OK (contexto)", name)


def annotate(name, markers, ring=None, raio=0.0125):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    W, H = img.size
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = max(14, int(W * raio))
    fnt = font(int(r * 1.2))
    w = max(2, int(W * 0.0022))
    for (fx, fy, fw, fh) in (ring or []):
        x0, y0 = fx * W, fy * H
        d.rectangle(
            [x0, y0, x0 + fw * W, y0 + fh * H],
            outline=GREEN + (A_LINE,),
            width=w,
        )
    for (num, tx, ty, bx, by) in markers:
        TX, TY, BX, BY = tx * W, ty * H, bx * W, by * H
        ang = math.atan2(TY - BY, TX - BX)
        draw_arrow(
            d,
            BX + (r + 5) * math.cos(ang),
            BY + (r + 5) * math.sin(ang),
            TX,
            TY,
            w,
        )
        badge(d, BX, BY, r, num, fnt)
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, name))
    print("OK", name)


# 01) Menu: Food Marketing → BeeFood Pixel Analytics (estamos na home)
annotate("01-menu-food-marketing.png", [
    (1, 0.095, 0.148, 0.040, 0.148),  # FOOD MARKETING
    (2, 0.110, 0.198, 0.040, 0.198),  # BeeFood Pixel Analytics
])

# 02) Filtros do topo
annotate("02-filtros-topo.png", [
    (1, 0.300, 0.198, 0.300, 0.130),  # período
    (2, 0.430, 0.198, 0.430, 0.130),  # contexto
    (3, 0.560, 0.198, 0.560, 0.130),  # cardápio
    (4, 0.690, 0.198, 0.690, 0.130),  # origem
    (5, 0.820, 0.198, 0.820, 0.130),  # Excel
    (6, 0.940, 0.198, 0.940, 0.130),  # ajuda
])

# 03) Funil em colunas — as 6 etapas
annotate("03-funil-colunas.png", [
    (1, 0.280, 0.340, 0.280, 0.255),  # Visitas
    (2, 0.405, 0.340, 0.405, 0.255),  # Visualizações
    (3, 0.530, 0.340, 0.530, 0.255),  # Carrinho
    (4, 0.655, 0.340, 0.655, 0.255),  # Finalização
    (5, 0.780, 0.340, 0.780, 0.255),  # Pagamento
    (6, 0.905, 0.340, 0.905, 0.255),  # Pedidos
])

passthrough("04-funil-classico.png")

# 05) KPIs (depois de rolar até Receita / Ticket / Conversão)
annotate("05-kpis-resumo.png", [
    (1, 0.320, 0.640, 0.250, 0.555),  # Receita total
    (2, 0.550, 0.640, 0.550, 0.555),  # Ticket médio
    (3, 0.780, 0.640, 0.900, 0.555),  # Conversão geral
])

# 06) Ao vivo (canto inferior direito)
annotate("06-ao-vivo.png", [
    (1, 0.880, 0.560, 0.780, 0.500),  # título Ao vivo
    (2, 0.860, 0.680, 0.760, 0.680),  # um evento
])

passthrough("07-como-funciona.png")

# 08) Segmentação — tabela de origens
annotate("08-segmentacao.png", [
    (1, 0.300, 0.640, 0.220, 0.575),  # atalho Top Origens
    (2, 0.300, 0.860, 0.220, 0.860),  # linha Direto
    (3, 0.620, 0.800, 0.750, 0.740),  # coluna Conv. %
])
