"""Anota os screenshots do #94 Fechamento Fiscal.

Setas verdes + badges. Coordenadas em fracoes (0..1).
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)
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
        d.line([(x1, y1), (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))],
               fill=col, width=w)


def badge(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], fill=WHITE + (235,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN + (A_BADGE,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
           t, fill=WHITE, font=fnt)


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
        TX, TY, BX, BY = tx * W, ty * H, bx * W, by * H
        ang = math.atan2(TY - BY, TX - BX)
        draw_arrow(d, BX + (r + 5) * math.cos(ang), BY + (r + 5) * math.sin(ang), TX, TY, w)
        badge(d, BX, BY, r, num, fnt)
    Image.alpha_composite(img, overlay).convert("RGB").save(os.path.join(OUT, name))
    print("OK", name)


# 1. Resumo
annotate("01-tela-resumo.png", [
    (1, 0.235, 0.115, 0.235, 0.175),   # aba Fechamento
    (2, 0.905, 0.115, 0.820, 0.070),   # seletor Nippon
    (3, 0.680, 0.175, 0.600, 0.130),   # competencia
    (4, 0.790, 0.175, 0.790, 0.235),   # Mes inteiro
    (5, 0.880, 0.175, 0.880, 0.235),   # Exportar
    (6, 0.955, 0.175, 0.955, 0.235),   # XMLs
    (7, 0.280, 0.310, 0.200, 0.250),   # Valor autorizado
    (8, 0.480, 0.310, 0.560, 0.250),   # Documentos
    (9, 0.250, 0.430, 0.200, 0.500),   # Composicao
    (10, 0.250, 0.560, 0.200, 0.720),  # Tributos
])

# 2. Exportar
annotate("02-exportar-pdf-excel.png", [
    (1, 0.905, 0.205, 0.840, 0.155),   # PDF
    (2, 0.905, 0.245, 0.840, 0.300),   # Excel
])

# 3. Recorte
annotate("03-filtro-periodo.png", [
    (1, 0.530, 0.230, 0.480, 0.170),   # Mes inteiro (chip do popover)
    (2, 0.680, 0.230, 0.760, 0.175),   # 1a / 2a quinzena
    (3, 0.500, 0.280, 0.430, 0.340),   # De
    (4, 0.800, 0.620, 0.640, 0.680),   # APLICAR
])

# 4. Produtos
annotate("04-aba-produtos.png", [
    (1, 0.310, 0.175, 0.250, 0.125),   # aba Produtos
    (2, 0.360, 0.230, 0.500, 0.185),   # Por CFOP / CST / NCM
    (3, 0.280, 0.280, 0.210, 0.330),   # busca
    (4, 0.930, 0.280, 0.930, 0.220),   # Colunas
    (5, 0.280, 0.400, 0.200, 0.480),   # tabela
])

# 5. Por CFOP
annotate("05-produtos-por-cfop.png", [
    (1, 0.310, 0.230, 0.250, 0.175),   # Por CFOP
    (2, 0.300, 0.420, 0.210, 0.300),   # grafico
    (3, 0.620, 0.300, 0.780, 0.230),   # tabela
])

# 6. Documentos
annotate("06-aba-documentos.png", [
    (1, 0.400, 0.175, 0.400, 0.125),   # aba Documentos
    (2, 0.280, 0.240, 0.200, 0.200),   # busca
    (3, 0.780, 0.330, 0.700, 0.270),   # Ver itens
    (4, 0.870, 0.330, 0.870, 0.270),   # Ver XML
    (5, 0.945, 0.330, 0.945, 0.270),   # Baixar
])

# 7. Itens da nota
annotate("07-dialog-itens.png", [
    (1, 0.300, 0.345, 0.210, 0.260),   # NFC-e 332709
    (2, 0.300, 0.500, 0.210, 0.580),   # itens
])

# 8. Ajuda
annotate("08-ajuda-acesso.png", [
    (1, 0.965, 0.235, 0.900, 0.185),   # ?
    (2, 0.880, 0.340, 0.780, 0.400),   # Ver contadores
])

# 10. Permissao
annotate("10-permissao-fechamento-fiscal.png", [
    (1, 0.680, 0.280, 0.820, 0.230),   # filtro Fiscal
    (2, 0.420, 0.690, 0.280, 0.740),   # Fechamento Fiscal
])

print("done")
