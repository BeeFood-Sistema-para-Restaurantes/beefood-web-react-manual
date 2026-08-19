"""Anota os screenshots do manual BeeFood - Restricoes de Caixa.
Mesmo estilo dos demais manuais: setas finas/sutis em VERDE + badges numerados.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)
- alvo = ponta da seta (campo/botao)
- badge = posicao do circulo numerado (origem da seta)

Nos modais, os badges ficam na margem escurecida do overlay e as setas apontam
para dentro - assim nenhum numero cobre valor ou rotulo.
"""
import os, math
from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
A_LINE = 220
A_BADGE = 235

# Arial no Windows do dono; Arimo/DejaVu no Linux (Cloud Agent). Primeiro que existir vence.
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
    """Copia uma imagem de CONTEXTO (sem setas) para imagens-tratadas/."""
    img = Image.open(os.path.join(SRC, name)).convert("RGB")
    img.save(os.path.join(OUT, name))
    print("OK (contexto)", name)


def annotate(name, markers, ring=None):
    """ring = retangulos (x, y, largura, altura) em fracoes, para cercar a area
    onde algo SUMIU - util quando nao ha elemento para a seta apontar."""
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
    out_img = Image.alpha_composite(img, overlay).convert("RGB")
    out_img.save(os.path.join(OUT, name))
    print("OK", name)


# ---------- Onde se configura ----------

# 01) Configuracao -> Usuarios -> aba Grupos de Acesso
annotate("01-grupos-de-acesso.png", [
    (1, 0.142, 0.274, 0.190, 0.375),   # menu Usuarios
    (2, 0.365, 0.085, 0.680, 0.075),   # aba Grupos de Acesso
    (3, 0.330, 0.234, 0.480, 0.300),   # o grupo Acesso Funcionario
])

# 02) O modal do grupo, com os quatro switches de caixa
annotate("02-modal-editar-grupo.png", [
    (1, 0.270, 0.349, 0.135, 0.300),   # campo Buscar permissao
    (2, 0.755, 0.561, 0.900, 0.500),   # Abrir e Fechar Caixa
    (3, 0.755, 0.608, 0.930, 0.600),   # Visualizar Valores de Referencia
    (4, 0.755, 0.647, 0.930, 0.700),   # Visualizar Caixas Fechados
    (5, 0.755, 0.684, 0.900, 0.790),   # Transferencia de Operacoes
])

# ---------- O caixa completo, para comparar ----------

# 03) A tela de caixa de quem tem tudo liberado
annotate("03-caixa-completo.png", [
    (1, 0.375, 0.085, 0.550, 0.160),   # aba Cancelamentos
    (2, 0.845, 0.240, 0.720, 0.115),   # colunas Saldo Final / Conf. / Quebra
    (3, 0.215, 0.368, 0.175, 0.290),   # botoes de acao da linha
])

# 05) O modal de um caixa, com tudo liberado
annotate("05-modal-caixa-completo.png", [
    (1, 0.323, 0.155, 0.200, 0.075),   # botao TRANSFERIR
    (2, 0.585, 0.155, 0.550, 0.070),   # icones Cancelamentos e Excluidos
    (3, 0.700, 0.402, 0.590, 0.470),   # Resumo com os valores
])

# ---------- Restricao 1 - Abrir e Fechar Caixa ----------

# 04) O menu do funcionario, ja sem o item Caixa
annotate("04-menu-sem-caixa.png", [
    (1, 0.148, 0.215, 0.190, 0.365),   # o vao onde ficava o menu Caixa
    (2, 0.300, 0.130, 0.560, 0.050),   # confirma de quem e a tela
], ring=[(0.006, 0.180, 0.135, 0.065)])

# ---------- Restricao 2 - Visualizar Valores de Referencia ----------

# 06) A listagem sem nenhuma coluna de valor
annotate("06-listagem-sem-valores.png", [
    (1, 0.870, 0.247, 0.760, 0.130),   # onde ficavam as tres colunas
    (2, 0.205, 0.297, 0.178, 0.225),   # a coluna Acoes, so com a lupa
])

# 07) O painel Resumo vazio
annotate("07-resumo-vazio.png", [
    (1, 0.700, 0.285, 0.580, 0.350),   # Nenhum resumo disponivel
])

# 08) A conferencia completa (referencia)
annotate("08-conferencia-completa.png", [
    (1, 0.450, 0.357, 0.420, 0.255),   # Entrada / Saida / Saldo
    (2, 0.710, 0.357, 0.700, 0.255),   # 1a Conferencia
    (3, 0.851, 0.357, 0.930, 0.255),   # Diferenca
])

# 09) A mesma conferencia, cega
annotate("09-conferencia-cega.png", [
    (1, 0.710, 0.406, 0.520, 0.340),   # so Forma de Pagamento e 1a Conferencia
    (2, 0.640, 0.450, 0.450, 0.480),   # o campo para digitar o que foi contado
])

# ---------- Restricao 3 - Visualizar Caixas Fechados ----------

# 10) So o caixa aberto aparece
annotate("10-listagem-so-aberto.png", [
    (1, 0.300, 0.305, 0.200, 0.400),   # a unica linha da lista
    (2, 0.340, 0.925, 0.500, 0.870),   # Mostrando 1-1 de 1
])

# ---------- Restricao 4 - Transferencia de Operacoes ----------

# 11) O modal sem TRANSFERIR e sem os dois icones
annotate("11-modal-sem-transferir.png", [
    (1, 0.295, 0.176, 0.240, 0.075),   # o vao onde ficava o TRANSFERIR
    (2, 0.615, 0.176, 0.580, 0.070),   # o vao dos icones Cancelamentos/Excluidos
])

# ---------- Restricao 5 - Cadastro de Caixas ----------

# 12) O switch, em Empresa
annotate("12-switch-cadastro-de-caixas.png", [
    (1, 0.270, 0.349, 0.135, 0.300),   # busca por "cadastro de caixas"
    (2, 0.755, 0.451, 0.900, 0.420),   # o switch desligado
])

# 13) O menu Configuracao com o item Caixa
annotate("13-menu-config-com-caixa.png", [
    (1, 0.070, 0.480, 0.185, 0.530),   # item Caixa
])

# 14) O mesmo menu sem o item Caixa
annotate("14-menu-config-sem-caixa.png", [
    (1, 0.075, 0.460, 0.200, 0.520),   # o item sumiu entre Migrar Dados e TEF
])

# ---------- Restricao 6 - Funcao Gerente ----------

# 15) O cadastro do usuario
annotate("15-funcao-gerente.png", [
    (1, 0.295, 0.561, 0.170, 0.500),   # Grupo de Acesso
    (2, 0.545, 0.645, 0.600, 0.830),   # switch Gerente
])

# 16) O caixa de quem nao e gerente: sem a aba Cancelamentos
annotate("16-caixa-sem-cancelamentos.png", [
    (1, 0.295, 0.078, 0.620, 0.078),   # so a aba Listagem de Caixa
])

# ---------- Restricao 7 - Usuario Fixo (o "caixa por usuario" de verdade) ----------

# 17) Configuracao -> Caixa, com a coluna Usuario Fixo
annotate("17-cadastro-de-caixas.png", [
    (1, 0.070, 0.480, 0.185, 0.550),   # menu Configuracao -> Caixa
    (2, 0.575, 0.135, 0.800, 0.055),   # coluna Usuario Fixo
    (3, 0.330, 0.200, 0.300, 0.300),   # a linha do caixa (clique para editar)
])

# 18) O campo Usuario Fixo preenchido
annotate("18-usuario-fixo.png", [
    (1, 0.365, 0.581, 0.230, 0.540),   # Usuario Fixo
    (2, 0.360, 0.634, 0.230, 0.720),   # switch Ativo
    (3, 0.625, 0.716, 0.760, 0.780),   # SALVAR (F2)
])

# 19) O funcionario passa a ver so o caixa dele
annotate("19-caixa-so-o-seu.png", [
    (1, 0.567, 0.335, 0.640, 0.420),   # Usuario Abertura = caixa.manual
    (2, 0.345, 0.928, 0.520, 0.870),   # Mostrando 1-1 de 1
])

# ---------- O parametro que NAO faz o que promete ----------

# 20) Configuracao -> Parametros -> Caixa
annotate("20-parametro-caixa-por-usuario.png", [
    (1, 0.320, 0.560, 0.235, 0.660),   # rotulo e descricao
    (2, 0.812, 0.562, 0.900, 0.660),   # o switch
])

print("done")
