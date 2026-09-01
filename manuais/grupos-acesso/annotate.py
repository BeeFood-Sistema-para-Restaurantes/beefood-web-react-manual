"""Anota os screenshots do estudo de grupos de acesso.

Mesmo estilo dos demais manuais: setas finas em VERDE + badges numerados.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)
- alvo = ponta da seta (campo/botao)
- badge = posicao do circulo numerado (origem da seta)

Alem de `annotate` e `passthrough`, este manual usa `comparar`: recorta a MESMA
regiao de duas capturas (antes/depois) e monta as duas lado a lado com titulo.
Sem isso, restricao que so muda a opacidade de um switch nao aparece no print.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
CINZA = (244, 244, 245)
TEXTO = (40, 40, 45)
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
        d.line([(x1, y1), (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))],
               fill=col, width=w)


def badge(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], fill=WHITE + (235,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN + (A_BADGE,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
           t, fill=WHITE, font=fnt)


def _marcar(img, markers, ring=None):
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
    return Image.alpha_composite(img, overlay).convert("RGB")


def passthrough(name, saida=None):
    """Copia uma imagem de CONTEXTO (sem setas) para imagens-tratadas/."""
    img = Image.open(os.path.join(SRC, name)).convert("RGB")
    img.save(os.path.join(OUT, saida or name))
    print("OK (contexto)", saida or name)


def annotate(name, markers, ring=None, saida=None, crop=None):
    """crop = (x, y, largura, altura) em fracoes, aplicado ANTES das setas."""
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    if crop:
        W, H = img.size
        fx, fy, fw, fh = crop
        img = img.crop((int(fx * W), int(fy * H), int((fx + fw) * W), int((fy + fh) * H)))
    img = _marcar(img, markers, ring)
    img.save(os.path.join(OUT, saida or name))
    print("OK", saida or name)


def comparar(saida, painel_esq, painel_dir, crop, markers_esq=None, markers_dir=None,
             ring_esq=None, ring_dir=None, largura=760):
    """Monta duas capturas recortadas na MESMA regiao, lado a lado, com titulo.

    painel_* = (arquivo, titulo). crop = (x, y, largura, altura) em fracoes.
    markers_*/ring_* usam fracoes DO RECORTE, nao da captura inteira.
    """
    GAP, PAD, CAP_H = 18, 22, 46
    partes = []
    for arq, titulo, mk, rg in ((painel_esq[0], painel_esq[1], markers_esq, ring_esq),
                                (painel_dir[0], painel_dir[1], markers_dir, ring_dir)):
        img = Image.open(os.path.join(SRC, arq)).convert("RGBA")
        W, H = img.size
        fx, fy, fw, fh = crop
        img = img.crop((int(fx * W), int(fy * H), int((fx + fw) * W), int((fy + fh) * H)))
        img = _marcar(img, mk or [], rg).convert("RGBA")
        esc = largura / img.size[0]
        img = img.resize((largura, int(img.size[1] * esc)), Image.LANCZOS)
        partes.append((img, titulo))

    alt = max(p[0].size[1] for p in partes)
    total_w = PAD * 2 + largura * 2 + GAP
    total_h = PAD * 2 + CAP_H + alt
    canvas = Image.new("RGB", (total_w, total_h), CINZA)
    d = ImageDraw.Draw(canvas)
    fnt = font(24)
    for i, (img, titulo) in enumerate(partes):
        x = PAD + i * (largura + GAP)
        bb = d.textbbox((0, 0), titulo, font=fnt)
        d.text((x + (largura - (bb[2] - bb[0])) / 2, PAD + (CAP_H - (bb[3] - bb[1])) / 2 - bb[1]),
               titulo, fill=TEXTO, font=fnt)
        canvas.paste(img.convert("RGB"), (x, PAD + CAP_H))
        d.rectangle([x, PAD + CAP_H, x + largura - 1, PAD + CAP_H + img.size[1] - 1],
                    outline=(210, 210, 214), width=1)
    canvas.save(os.path.join(OUT, saida))
    print("OK (comparativo)", saida)


# =====================================================================
# 1. Onde tudo se configura
# =====================================================================

# Aba Usuarios: quem e quem, com o grupo de cada um
annotate("01-usuarios-aba-usuarios.png", [
    (1, 0.093, 0.320, 0.175, 0.400),   # menu Usuarios
    (2, 0.196, 0.070, 0.168, 0.140),   # aba Usuarios
    (3, 0.318, 0.070, 0.440, 0.120),   # aba Grupos de Acesso
    (4, 0.790, 0.212, 0.700, 0.330),   # coluna Grupo de Acesso
])

# Aba Grupos de Acesso
annotate("02-aba-grupos-de-acesso.png", [
    (1, 0.235, 0.146, 0.330, 0.240),   # + Novo Grupo
    (2, 0.898, 0.252, 0.830, 0.340),   # lapis do grupo
    (3, 0.360, 0.146, 0.480, 0.240),   # Buscar grupo
])

# O modal com as permissoes
annotate("03-modal-grupo-todas-permissoes.png", [
    (1, 0.400, 0.262, 0.480, 0.190),   # Descricao
    (2, 0.300, 0.324, 0.180, 0.262),   # Buscar permissao
    (3, 0.660, 0.324, 0.830, 0.250),   # filtro por recurso
    (4, 0.291, 0.393, 0.170, 0.420),   # selo da categoria
    (5, 0.272, 0.443, 0.150, 0.520),   # setinha de expandir
    (6, 0.712, 0.443, 0.860, 0.430),   # switch
])

# O filtro por recurso aberto: as dez categorias
annotate("04-filtro-por-recurso.png", [
    (1, 0.660, 0.324, 0.520, 0.250),   # Todos os recursos
    (2, 0.620, 0.560, 0.850, 0.620),   # a lista de categorias
])

# A busca por permissao
annotate("05-busca-permissao.png", [
    (1, 0.300, 0.324, 0.180, 0.262),   # campo de busca
    (2, 0.310, 0.470, 0.160, 0.560),   # o resultado
])

# Os seis sub-itens de Cadastro de Cardapio
annotate("06-acoes-do-cardapio.png", [
    (1, 0.272, 0.443, 0.150, 0.400),   # setinha de Cadastro de Cardapio
    (2, 0.712, 0.497, 0.860, 0.470),   # Excluir
    (3, 0.712, 0.542, 0.880, 0.545),   # Editar (exceto preco)
    (4, 0.712, 0.586, 0.880, 0.615),   # Editar Preco
    (5, 0.712, 0.630, 0.870, 0.685),   # Editar Ativo
    (6, 0.712, 0.675, 0.850, 0.750),   # Adicionar Novo
    (7, 0.712, 0.719, 0.820, 0.810),   # Editar em Lote
])

# O cadastro do usuario: onde o grupo e a Funcao Gerente sao atribuidos
annotate("20-cadastro-usuario-gerente.png", [
    (1, 0.290, 0.572, 0.180, 0.540),   # Grupo de Acesso
    (2, 0.531, 0.645, 0.790, 0.600),   # switch Gerente
    (3, 0.686, 0.660, 0.860, 0.680),   # switch Aplicativos
    (4, 0.720, 0.740, 0.820, 0.800),   # SALVAR (F2)
])

# =====================================================================
# 2. A tela de produto — referencia
# =====================================================================

annotate("30a-lista-cardapio-completo.png", [
    (1, 0.905, 0.088, 0.905, 0.185),   # + Novo Produto (F1)
    (2, 0.265, 0.152, 0.175, 0.190),   # + Novo Setor
    (3, 0.800, 0.157, 0.735, 0.190),   # Editar em Lote
])

annotate("30b-produto-completo.png", [
    (1, 0.190, 0.155, 0.085, 0.120),   # abas do modal
    (2, 0.308, 0.252, 0.085, 0.235),   # Nome
    (3, 0.308, 0.427, 0.085, 0.405),   # Preco de Venda
    (4, 0.308, 0.482, 0.085, 0.520),   # Custo
    (5, 0.205, 0.870, 0.085, 0.900),   # OPCOES
    (6, 0.665, 0.870, 0.665, 0.955),   # SALVAR E SAIR (F2)
])

# =====================================================================
# 3. Comparativos antes/depois — o que cada restricao faz na tela
# =====================================================================

# 3.1 Sem "Editar (exceto preco)": listas e botao de IA apagados;
# os campos de texto ficam iguais e apenas deixam de aceitar digitacao.
comparar(
    "31-comparativo-sem-editar.png",
    ("30b-produto-completo.png", "Com Editar (exceto preço)"),
    ("31b-produto-sem-editar.png", "Sem Editar (exceto preço)"),
    crop=(0.28, 0.30, 0.58, 0.28),
    ring_dir=[(0.034, 0.045, 0.794, 0.140),    # Setor e Etiqueta
              (0.733, 0.372, 0.224, 0.150)],   # Unidade
)

# 3.2 Sem "Editar Preco": Preco de Venda e Custo viram somente leitura
comparar(
    "32-comparativo-sem-preco.png",
    ("30b-produto-completo.png", "Com Editar Preço"),
    ("32b-produto-sem-preco.png", "Sem Editar Preço"),
    crop=(0.28, 0.385, 0.58, 0.16),
    ring_esq=[(0.034, 0.125, 0.216, 0.270),    # Preco de Venda
              (0.034, 0.600, 0.284, 0.260)],   # Custo
    ring_dir=[(0.034, 0.125, 0.216, 0.270),
              (0.034, 0.600, 0.284, 0.260)],
)

# 3.3 Sem "Editar Ativo": as chaves da aba Cardapios ficam apagadas
comparar(
    "33-comparativo-sem-ativo.png",
    ("40b-aba-cardapios-completo.png", "Com Editar Ativo"),
    ("43b-aba-cardapios-sem-ativo.png", "Sem Editar Ativo"),
    crop=(0.155, 0.185, 0.73, 0.19),
    ring_dir=[(0.089, 0.384, 0.486, 0.200)],   # Delivery, Presencial, Totem
)

# 3.4 Sem "Editar Ativo": o menu do card perde as tres acoes de ativacao
comparar(
    "33b-comparativo-menu-card-sem-ativo.png",
    ("40a-menu-card-completo.png", "Com Editar Ativo"),
    ("43a-menu-card-sem-ativo.png", "Sem Editar Ativo"),
    crop=(0.465, 0.36, 0.20, 0.40),
)

# 3.5 Sem "Excluir": o menu do card perde o Excluir
comparar(
    "34-comparativo-menu-card-sem-excluir.png",
    ("40a-menu-card-completo.png", "Com Excluir"),
    ("44a-menu-card-sem-excluir.png", "Sem Excluir"),
    crop=(0.465, 0.36, 0.20, 0.40),
)

# 3.6 Sem "Excluir": o menu OPCOES do rodape fica vazio
comparar(
    "34b-comparativo-menu-opcoes-sem-excluir.png",
    ("40c-menu-opcoes-completo.png", "Com Excluir"),
    ("44c-menu-opcoes-sem-excluir.png", "Sem Excluir"),
    crop=(0.150, 0.855, 0.24, 0.14),
)

# 3.7 Sem "Adicionar Novo" e sem "Editar em Lote": o cabecalho perde os botoes
comparar(
    "35-comparativo-sem-novo-lote.png",
    ("30a-lista-cardapio-completo.png", "Com Adicionar Novo e Editar em Lote"),
    ("35a-lista-cardapio-sem-novo-lote.png", "Sem as duas permissões"),
    crop=(0.155, 0.035, 0.845, 0.135),
)

# 3.8 Sem "Cadastro de Cardapio": o grupo Cardapio sai do menu lateral
comparar(
    "36-comparativo-menu-cardapio.png",
    ("36a-menu-com-cardapio.png", "Com Cadastro de Cardápio"),
    ("36b-menu-sem-cardapio.png", "Sem Cadastro de Cardápio"),
    crop=(0.0, 0.125, 0.145, 0.55),
    largura=360,
    ring_esq=[(0.05, 0.520, 0.90, 0.070)],     # o item Cardapio
    ring_dir=[(0.05, 0.520, 0.90, 0.070)],     # o vao onde ele estava
)

print("done")
