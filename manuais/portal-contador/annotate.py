"""Anota os screenshots do #96 Portal do contador.

Setas verdes + badges. Coordenadas em fracoes (0..1).
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)
"""
import math
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps, ImageStat

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


def faixas(perfil, gap):
    """Trechos com tinta no perfil, unindo lacunas de ate `gap` pixels.

    Trechos com menos de 6 px caem fora: sao bordas de tabela, nao texto.
    """
    achadas = []
    inicio = fim = None
    for i, v in enumerate(perfil):
        if v >= 2:
            inicio = i if inicio is None else inicio
            fim = i
        elif inicio is not None and i - fim > gap:
            achadas.append((inicio, fim + 1))
            inicio = fim = None
    if inicio is not None:
        achadas.append((inicio, fim + 1))
    return [(a, b) for a, b in achadas if b - a >= 6]


def desfocar(img, regioes):
    """Suaviza so a mancha de cada valor: da para ver que ali tem um numero."""
    W, H = img.size
    gap = max(6, W // 150)
    for (fx, fy, fw, fh) in regioes:
        x0, y0 = int(fx * W), int(fy * H)
        x1, y1 = int((fx + fw) * W), int((fy + fh) * H)
        lg, at = x1 - x0, y1 - y0
        cinza = ImageOps.autocontrast(img.crop((x0, y0, x1, y1)).convert("L"))
        fundo = ImageStat.Stat(cinza).median[0]
        tinta = cinza.point(lambda v: 255 if abs(v - fundo) > 28 else 0)
        for (ly0, ly1) in faixas(list(tinta.resize((1, at), Image.BOX).getdata()), 1):
            linha = tinta.crop((0, ly0, lg, ly1)).resize((lg, 1), Image.BOX)
            alt = ly1 - ly0
            margem = max(2, alt // 4)
            for (lx0, lx1) in faixas(list(linha.getdata()), gap):
                caixa = (max(0, x0 + lx0 - margem), max(0, y0 + ly0 - margem),
                         min(W, x0 + lx1 + margem), min(H, y0 + ly1 + margem))
                img.paste(img.crop(caixa).filter(ImageFilter.GaussianBlur(max(3, alt // 4))), caixa)
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
    (0.592, 0.441, 0.144, 0.026),  # documento no texto
    (0.471, 0.661, 0.128, 0.024),  # documento no rodape
])

annotate("02-email-acessar-portal.png", [
    (1, 0.500, 0.420, 0.220, 0.370),   # 2 CNPJs
    (2, 0.500, 0.530, 0.280, 0.600),   # ACESSAR O PORTAL
], blur=[
    (0.561, 0.452, 0.142, 0.030),  # documento no texto
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
    (0.358, 0.423, 0.096, 0.022),  # documento do contador
])

# 6. Clientes
annotate("06-meus-clientes.png", [
    (1, 0.120, 0.145, 0.280, 0.090),   # resumo 2 empresas
    (2, 0.120, 0.240, 0.320, 0.180),   # cartao MAGA
    (3, 0.080, 0.265, 0.200, 0.320),   # selo Matriz
    (4, 0.120, 0.400, 0.280, 0.360),   # Edicao fiscal
    (5, 0.150, 0.445, 0.320, 0.500),   # permissoes
], blur=[
    (0.021, 0.258, 0.098, 0.021),  # CNPJ da MAGA
    (0.021, 0.606, 0.098, 0.021),  # CNPJ da matriz
    (0.350, 0.606, 0.098, 0.021),  # CNPJ da filial
])

# 7. Competencias
annotate("07-competencias.png", [
    (1, 0.220, 0.040, 0.380, 0.040),   # seletor cliente
    (2, 0.080, 0.200, 0.080, 0.140),   # mes
    (3, 0.820, 0.255, 0.720, 0.180),   # Ver fechamento
    (4, 0.930, 0.255, 0.970, 0.320),   # Baixar XMLs
], blur=[
    (0.008, 0.207, 0.098, 0.020),  # CNPJ
    (0.021, 0.340, 0.074, 0.021),  # set
    (0.021, 0.491, 0.074, 0.021),  # ago
    (0.021, 0.642, 0.074, 0.021),  # jul
    (0.021, 0.793, 0.074, 0.021),  # jun
    (0.021, 0.944, 0.074, 0.021),  # mai
])

# 8. Fechamento
annotate("08-fechamento.png", [
    (1, 0.180, 0.055, 0.180, 0.110),   # abas
    (2, 0.080, 0.230, 0.080, 0.175),   # Mes inteiro
    (3, 0.820, 0.175, 0.820, 0.120),   # Exportar
    (4, 0.150, 0.300, 0.080, 0.360),   # cartoes
    (5, 0.200, 0.520, 0.080, 0.600),   # tributos
], blur=[
    (0.084, 0.207, 0.098, 0.021),  # CNPJ
    (0.048, 0.328, 0.100, 0.028),  # valor autorizado
    (0.020, 0.485, 0.795, 0.025),  # composição
    (0.420, 0.635, 0.070, 0.050),  # ICMS
    (0.400, 0.780, 0.092, 0.025),  # total dos tributos
    (0.915, 0.643, 0.070, 0.023),  # valor total por tipo
])

# 9. Produtos
annotate("09-produtos.png", [
    (1, 0.220, 0.055, 0.220, 0.110),   # aba Produtos
    (2, 0.220, 0.230, 0.080, 0.180),   # Por CFOP / CST / NCM
    (3, 0.200, 0.380, 0.080, 0.450),   # tabela
])  # a tela corta antes das colunas de R$: nao ha valor a esconder

# 10. Documentos
annotate("10-documentos.png", [
    (1, 0.180, 0.200, 0.080, 0.160),   # busca
    (2, 0.900, 0.300, 0.900, 0.230),   # Ver XML / Baixar
    (3, 0.760, 0.300, 0.680, 0.230),   # Ver itens
], blur=[
    (0.083, 0.318, 0.040, 0.572),  # numero da nota
    (0.264, 0.318, 0.136, 0.572),  # chave de acesso
    (0.619, 0.318, 0.047, 0.572),  # valor
])

# 11. NFe recebidas
annotate("11-nfe-recebidas.png", [
    (1, 0.180, 0.055, 0.180, 0.110),   # aba
    (2, 0.150, 0.185, 0.080, 0.240),   # intervalo
    (3, 0.200, 0.560, 0.080, 0.500),   # lista
], blur=[
    (0.345, 0.381, 0.093, 0.030),  # valor total
    (0.103, 0.612, 0.290, 0.292),  # fornecedor e CNPJ
    (0.418, 0.615, 0.062, 0.260),  # numero / serie
    (0.525, 0.615, 0.062, 0.260),  # valor
])

# 12. Edicao fiscal
annotate("12-edicao-fiscal.png", [
    (1, 0.280, 0.055, 0.280, 0.110),   # aba
    (2, 0.180, 0.230, 0.080, 0.175),   # Sem NCM
    (3, 0.940, 0.320, 0.850, 0.250),   # Editar
])

print("done")
