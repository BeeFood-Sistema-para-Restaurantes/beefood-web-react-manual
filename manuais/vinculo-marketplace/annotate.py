"""Anota os screenshots do manual BeeFood - Vinculo Marketplace (#79).

Le de imagens-puras/ e escreve em imagens-tratadas/.

As coordenadas dos marcadores sao dadas em fracoes 0..1 da imagem PURA (tela cheia,
1440x900 com device_scale_factor 1.5). O recorte e aplicado depois, e o script converte
as coordenadas sozinho - assim medir na captura original continua valendo mesmo quando o
recorte muda. Quase toda tela deste manual e um modal centralizado, entao o recorte
padrao pega so o modal.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
FUNDO = (244, 244, 245)
A_LINE = 220
A_BADGE = 235
FONT_CANDIDATES = [
    r"C:\Windows\Fonts\arialbd.ttf",
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]

# Recorte do modal do Vinculo Marketplace (tela cheia -> so o modal)
MODAL = (0.145, 0.072, 0.862, 0.945)
# Recorte do modal Selecionar Vinculo (ele e menor e fica por cima do outro)
SELECIONAR = (0.268, 0.101, 0.733, 0.899)


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
        d.line([(x1, y1),
                (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))],
               fill=col, width=w)


def badge(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], fill=WHITE + (235,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN + (A_BADGE,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
           t, fill=WHITE, font=fnt)


def preparar(name, recorte=None, escala=1.0):
    img = Image.open(os.path.join(SRC, name)).convert("RGB")
    if recorte:
        W, H = img.size
        x0, y0, x1, y1 = recorte
        img = img.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
    if escala != 1.0:
        img = img.resize((int(img.width * escala), int(img.height * escala)), Image.LANCZOS)
    return img


def converter(f, recorte):
    """Fracao da imagem cheia -> fracao da imagem recortada."""
    if not recorte:
        return f
    x0, y0, x1, y1 = recorte
    fx, fy = f
    return ((fx - x0) / (x1 - x0), (fy - y0) / (y1 - y0))


def annotate(name, markers, ring=None, recorte=None, escala=1.0):
    base = preparar(name, recorte, escala).convert("RGBA")
    W, H = base.size
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = max(14, int(W * 0.0125))
    fnt = font(int(r * 1.2))
    w = max(2, int(W * 0.0022))
    for (fx, fy, fw, fh) in (ring or []):
        (cx, cy) = converter((fx, fy), recorte)
        (cx2, cy2) = converter((fx + fw, fy + fh), recorte)
        d.rectangle([cx * W, cy * H, cx2 * W, cy2 * H],
                    outline=GREEN + (A_LINE,), width=w)
    for (num, tx, ty, bx, by) in markers:
        (tx, ty) = converter((tx, ty), recorte)
        (bx, by) = converter((bx, by), recorte)
        TX, TY, BX, BY = tx * W, ty * H, bx * W, by * H
        ang = math.atan2(TY - BY, TX - BX)
        draw_arrow(d, BX + (r + 5) * math.cos(ang), BY + (r + 5) * math.sin(ang), TX, TY, w)
        badge(d, BX, BY, r, num, fnt)
    Image.alpha_composite(base, overlay).convert("RGB").save(os.path.join(OUT, name))
    print("OK", name, "->", (W, H))


# 1. Onde fica: menu ... do Delivery.
annotate(
    "01-delivery-menu.png",
    [
        (1, 0.930, 0.092, 0.888, 0.272),   # botao ...
        (2, 0.820, 0.132, 0.718, 0.238),   # item Vinculo Marketplace
    ],
    recorte=(0.62, 0.058, 1.00, 0.34),
    escala=1.5,
)

# 2. A tela: busca, filtro, contadores e as colunas que importam.
annotate(
    "02-listagem.png",
    [
        (1, 0.180, 0.196, 0.300, 0.130),   # campo de busca
        (2, 0.410, 0.196, 0.480, 0.130),   # filtro Todos/Vinculados/Pendentes
        (3, 0.790, 0.178, 0.700, 0.130),   # contadores
        (4, 0.628, 0.315, 0.730, 0.435),   # coluna Vinculo (Sem vinculo)
        (5, 0.787, 0.315, 0.845, 0.435),   # coluna Setor
    ],
    recorte=(0.145, 0.072, 0.862, 0.508),
    escala=1.25,
)

# 3. Achar o item e marcar.
annotate(
    "03-selecionar-item.png",
    [
        (1, 0.183, 0.315, 0.300, 0.400),   # caixa de selecao da linha
        (2, 0.318, 0.882, 0.300, 0.790),   # 1 item selecionado
        (3, 0.573, 0.882, 0.600, 0.790),   # botao Vincular
    ],
    recorte=MODAL,
)

# 4. Modal Selecionar Vinculo.
annotate(
    "04-selecionar-vinculo.png",
    [
        (1, 0.410, 0.167, 0.640, 0.150),   # Vincular: <item do marketplace>
        (2, 0.350, 0.258, 0.400, 0.330),   # busca do cardapio
        (3, 0.400, 0.425, 0.620, 0.425),   # produto escolhido
        (4, 0.618, 0.858, 0.500, 0.800),   # Confirmar Vinculo
    ],
    recorte=SELECIONAR,
    escala=1.6,
)

# 5. Depois do vinculo: status, vinculo, setor e contadores.
annotate(
    "05-vinculado.png",
    [
        (1, 0.225, 0.315, 0.290, 0.430),   # Vinculado
        (2, 0.548, 0.315, 0.600, 0.430),   # coluna Vinculo
        (3, 0.755, 0.315, 0.800, 0.430),   # coluna Setor
        (4, 0.790, 0.178, 0.700, 0.130),   # contadores
    ],
    recorte=(0.145, 0.072, 0.862, 0.508),
    escala=1.25,
)

# 6. Lote: marcar tudo de uma vez.
annotate(
    "06-lote-selecao.png",
    [
        (1, 0.180, 0.272, 0.300, 0.400),   # caixa do cabecalho
        (2, 0.322, 0.882, 0.300, 0.790),   # 2 itens selecionados
        (3, 0.573, 0.882, 0.600, 0.790),   # Vincular
    ],
    recorte=MODAL,
)

# 7. Lote pronto: dois nomes apontando para o mesmo produto.
annotate(
    "07-lote-resultado.png",
    [
        (1, 0.640, 0.360, 0.760, 0.440),
    ],
    ring=[(0.540, 0.295, 0.170, 0.080)],
    recorte=(0.145, 0.072, 0.862, 0.445),
    escala=1.3,
)

# 8. Regra de tipo: item Grupo Opcao mostra produtos E opcoes.
annotate(
    "08-opcao-selecionar.png",
    [
        (1, 0.470, 0.295, 0.610, 0.345),   # chip Opcoes de Grupo
        (2, 0.335, 0.421, 0.600, 0.395),   # grupo (produto a que a opcao pertence)
        (3, 0.455, 0.462, 0.640, 0.462),   # opcao escolhida
    ],
    recorte=SELECIONAR,
    escala=1.6,
)

# 9. Criar produto e vincular.
annotate(
    "09-criar-produto.png",
    [
        (1, 0.640, 0.882, 0.660, 0.790),   # botao Criar produto e vincular
        (2, 0.575, 0.535, 0.430, 0.610),   # Sim, criar (ENTER)
    ],
    recorte=MODAL,
)

# 10. O produto criado, dentro do Cardapio.
annotate(
    "10-cardapio-produto-criado.png",
    [
        (1, 0.180, 0.764, 0.300, 0.800),   # setor Vinculo Marketplace na lista
        (2, 0.395, 0.202, 0.550, 0.150),   # o produto criado
        (3, 0.383, 0.238, 0.550, 0.290),   # preco vazio
    ],
    recorte=(0.152, 0.100, 0.720, 0.840),
)

# 11. Excluir vinculo: o dialogo que avisa que nao tem volta.
annotate(
    "11-excluir-dialogo.png",
    [
        (1, 0.795, 0.882, 0.800, 0.790),   # botao Excluir
        (2, 0.545, 0.545, 0.420, 0.620),   # Sim, excluir (ENTER)
    ],
    recorte=MODAL,
)

# 12. O aviso dentro da venda.
annotate(
    "12-venda-aviso.png",
    [
        (1, 0.300, 0.385, 0.450, 0.345),   # o item com o nome do marketplace
        (2, 0.420, 0.452, 0.600, 0.492),   # a faixa de aviso
    ],
    recorte=(0.272, 0.325, 0.730, 0.505),
    escala=1.4,
)

# 13. O modal em modo venda: coluna Nivel.
annotate(
    "13-modo-venda.png",
    [
        (1, 0.345, 0.113, 0.620, 0.113),   # titulo com o numero do pedido
        (2, 0.808, 0.278, 0.720, 0.200),   # coluna Nivel
        (3, 0.300, 0.632, 0.300, 0.690),   # bloco de opcoes pendentes
    ],
    ring=[(0.165, 0.383, 0.690, 0.237)],
    recorte=(0.145, 0.072, 0.862, 0.740),
    escala=1.15,
)

# 14. O bloqueio da nota fiscal.
annotate(
    "14-bloqueio-fiscal.png",
    [
        (1, 0.600, 0.512, 0.420, 0.560),   # Vincular no item pendente
        (2, 0.600, 0.612, 0.645, 0.640),   # EMITIR FISCAL desabilitado
    ],
    recorte=(0.298, 0.359, 0.703, 0.660),
    escala=1.7,
)

print("done")
