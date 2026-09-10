"""Anota os screenshots do #96 Portal do contador.

Setas verdes + badges. Coordenadas em fracoes (0..1).
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)
"""
import math
import os

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


def desfocar(img, regioes):
    """Embaça valores fiscais do cliente antes das setas."""
    W, H = img.size
    raio = max(20, W // 55)
    for (fx, fy, fw, fh) in regioes:
        caixa = (int(fx * W), int(fy * H), int((fx + fw) * W), int((fy + fh) * H))
        recorte = img.crop(caixa).filter(ImageFilter.GaussianBlur(radius=raio))
        img.paste(recorte.filter(ImageFilter.GaussianBlur(radius=raio)), caixa)
    return img


def annotate(name, markers, ring=None, blur=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    if blur:
        img = desfocar(img, blur)
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


# 1-2 e-mails (mesmos dos anexos do #95)
annotate("01-email-criar-senha.png", [
    (1, 0.500, 0.400, 0.220, 0.340),   # empresa
    (2, 0.500, 0.440, 0.220, 0.500),   # documento
    (3, 0.500, 0.530, 0.280, 0.600),   # CRIAR MINHA SENHA
], blur=[
    (0.500, 0.428, 0.230, 0.045),
    (0.400, 0.648, 0.230, 0.045),
])

annotate("02-email-acessar-portal.png", [
    (1, 0.500, 0.420, 0.220, 0.370),   # 2 CNPJs
    (2, 0.500, 0.530, 0.280, 0.600),   # ACESSAR O PORTAL
], blur=[
    (0.500, 0.448, 0.230, 0.045),
])

# 3. Identificar
annotate("03-login-identificar.png", [
    (1, 0.500, 0.470, 0.280, 0.430),   # campo
    (2, 0.500, 0.540, 0.280, 0.590),   # Continuar
    (3, 0.500, 0.620, 0.280, 0.680),   # Acessar painel
])

# 5. Senha
annotate("05-login-senha.png", [
    (1, 0.500, 0.400, 0.280, 0.350),   # nome + documento / trocar
    (2, 0.500, 0.480, 0.280, 0.520),   # senha
    (3, 0.500, 0.545, 0.280, 0.600),   # Entrar
    (4, 0.500, 0.585, 0.720, 0.650),  # Esqueci
], blur=[
    (0.385, 0.405, 0.180, 0.040),
])

# 6. Clientes
annotate("06-meus-clientes.png", [
    (1, 0.120, 0.145, 0.280, 0.090),   # resumo 2 empresas
    (2, 0.120, 0.240, 0.320, 0.180),   # cartao MAGA
    (3, 0.080, 0.265, 0.200, 0.320),   # selo Matriz
    (4, 0.120, 0.400, 0.280, 0.360),   # Edicao fiscal
    (5, 0.150, 0.445, 0.320, 0.500),   # permissoes
], blur=[
    (0.026, 0.245, 0.145, 0.035),  # MAGA
    (0.026, 0.592, 0.145, 0.038),  # Nippon
    (0.352, 0.612, 0.165, 0.040),  # Hey Sushi
])

# 7. Competencias
annotate("07-competencias.png", [
    (1, 0.220, 0.040, 0.380, 0.040),   # seletor cliente
    (2, 0.080, 0.200, 0.080, 0.140),   # mes
    (3, 0.820, 0.255, 0.720, 0.180),   # Ver fechamento
    (4, 0.930, 0.255, 0.970, 0.320),   # Baixar XMLs
], blur=[
    (0.018, 0.198, 0.165, 0.035),  # CNPJ
    (0.018, 0.322, 0.130, 0.045),  # set
    (0.018, 0.472, 0.130, 0.045),  # ago
    (0.018, 0.615, 0.130, 0.045),  # jul
    (0.018, 0.765, 0.130, 0.045),  # jun
    (0.018, 0.915, 0.130, 0.045),  # mai
])

# 8. Fechamento
annotate("08-fechamento.png", [
    (1, 0.180, 0.055, 0.180, 0.110),   # abas
    (2, 0.080, 0.230, 0.080, 0.175),   # Mes inteiro
    (3, 0.820, 0.175, 0.820, 0.120),   # Exportar
    (4, 0.150, 0.300, 0.080, 0.360),   # cartoes
    (5, 0.200, 0.520, 0.080, 0.600),   # tributos
], blur=[
    (0.018, 0.198, 0.220, 0.038),  # CNPJ
    (0.040, 0.295, 0.165, 0.058),  # valor autorizado
    (0.018, 0.455, 0.965, 0.058),  # composição
    (0.280, 0.605, 0.200, 0.090),  # ICMS
    (0.280, 0.745, 0.200, 0.055),  # total tributos
    (0.830, 0.612, 0.155, 0.055),  # valor por tipo
])

# 9. Produtos
annotate("09-produtos.png", [
    (1, 0.220, 0.055, 0.220, 0.110),   # aba Produtos
    (2, 0.220, 0.230, 0.080, 0.180),   # Por CFOP / CST / NCM
    (3, 0.200, 0.380, 0.080, 0.450),   # tabela
], blur=[
    (0.888, 0.360, 0.112, 0.510),  # coluna R$
])

# 10. Documentos
annotate("10-documentos.png", [
    (1, 0.180, 0.200, 0.080, 0.160),   # busca
    (2, 0.900, 0.300, 0.900, 0.230),   # Ver XML / Baixar
    (3, 0.760, 0.300, 0.680, 0.230),   # Ver itens
], blur=[
    (0.075, 0.295, 0.095, 0.595),  # numero
    (0.268, 0.295, 0.220, 0.595),  # chave
    (0.610, 0.295, 0.105, 0.595),  # valor
])

# 11. NFe recebidas
annotate("11-nfe-recebidas.png", [
    (1, 0.180, 0.055, 0.180, 0.110),   # aba
    (2, 0.150, 0.185, 0.080, 0.240),   # intervalo
    (3, 0.200, 0.560, 0.080, 0.500),   # lista
], blur=[
    (0.335, 0.358, 0.195, 0.065),  # valor total
    (0.108, 0.585, 0.530, 0.355),  # fornecedor, n°, valor
])

# 12. Edicao fiscal
annotate("12-edicao-fiscal.png", [
    (1, 0.280, 0.055, 0.280, 0.110),   # aba
    (2, 0.180, 0.230, 0.080, 0.175),   # Sem NCM
    (3, 0.940, 0.320, 0.850, 0.250),   # Editar
])

print("done")
