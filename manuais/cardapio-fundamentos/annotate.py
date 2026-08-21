"""Anota os screenshots do manual BeeFood - Cardapio: fundamentos (#27).

Mesmo estilo dos demais manuais: setas finas/sutis em VERDE + badges numerados.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)
- alvo  = ponta da seta (campo/botao)
- badge = posicao do circulo numerado (origem da seta)

As capturas sao do painel web em 2160x1350 (viewport 1440x900, DPR 1.5).
Quase toda etapa acontece num modal centralizado com o fundo escurecido, entao os
badges ficam nessa margem escura (a esquerda, sobre a sidebar, ou a direita) e as
setas entram no modal. Nas telas de listagem, que tem fundo claro, o badge vai no
espaco vazio abaixo do conteudo.

Setas miram a BORDA do botao (inferior ou lateral), nunca o meio: a ponta no meio
cobre uma letra do rotulo.

Duas telas usam passthrough(): a listagem dos tres complementos com foto e a
listagem final de produtos - nas duas o ponto e o conjunto, nao um controle.

A imagem 25 e gerada a partir da MESMA captura pura da 07 (o modal Detalhes do
Grupo), com setas nos quatro modos de Formacao de Preco - e a ilustracao da parte
que compara os modos.

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
    """Copia uma imagem de CONTEXTO (sem setas) para imagens-tratadas/."""
    img = Image.open(os.path.join(SRC, name)).convert("RGB")
    img.save(os.path.join(OUT, name))
    print("OK (contexto)", name)


def annotate(name, markers, ring=None, borrao=None, raio=0.0125, out_name=None):
    """ring   = retangulos (x, y, largura, altura) em fracoes, para cercar uma area.
    borrao = retangulos (x, y, largura, altura) em fracoes, para tornar dados
             pessoais ilegiveis. Aplicado ANTES das setas.
    out_name = salva com outro nome (usado quando duas imagens do manual saem da
             mesma captura pura)."""
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


# ---------- Parte 1: as tres abas do Cardapio ----------

# 01) Onde tudo acontece: Produtos, Grupo de Opcoes e Complementos
# As setas param LOGO ABAIXO do rotulo da aba (y 0.100); mirando o texto elas
# cobriam uma letra.
annotate("01-cardapio-produtos-vazio.png", [
    (1, 0.185, 0.100, 0.205, 0.280),   # aba Produtos
    (2, 0.283, 0.100, 0.330, 0.280),   # aba Grupo de Opcoes
    (3, 0.394, 0.100, 0.455, 0.280),   # aba Complementos
])

# ---------- Parte 2: cadastrar os complementos ----------

# 02) Aba Complementos vazia
annotate("02-aba-complementos.png", [
    (1, 0.921, 0.090, 0.930, 0.235),   # Novo Complemento (F1)
])

# 03) Modal do complemento preenchido
annotate("03-modal-complemento.png", [
    (1, 0.650, 0.252, 0.940, 0.200),   # Nome (obrigatorio)
    (2, 0.430, 0.341, 0.940, 0.300),   # Preco de Venda
    (3, 0.228, 0.437, 0.075, 0.450),   # ADICIONAR FOTO
    (4, 0.665, 0.905, 0.665, 0.760),   # SALVAR E SAIR (F2) - por baixo, sem cruzar PROXIMO
])

# 04) Editor da foto
annotate("04-foto-editor.png", [
    (1, 0.388, 0.795, 0.190, 0.760),   # Girar / Flip H / Flip V / Trocar imagem
    (2, 0.661, 0.865, 0.850, 0.900),   # SALVAR (F2)
])

# 05) Os tres complementos com foto e preco (contexto)
passthrough("05-complementos-lista.png")

# ---------- Parte 3: criar o grupo de opcoes ----------

# 06) Aba Grupo de Opcoes vazia
annotate("06-aba-grupo-opcoes.png", [
    (1, 0.938, 0.090, 0.930, 0.235),   # Novo Grupo (F1)
])

# 07) Detalhes do Grupo
# Todos os alvos ficam na coluna esquerda do modal, entao os badges vao empilhados
# na margem escura da esquerda - assim nenhuma seta atravessa o modal.
annotate("07-grupo-detalhes.png", [
    (1, 0.163, 0.261, 0.055, 0.240),   # Nome do Grupo de Opcao (obrigatorio)
    (2, 0.160, 0.319, 0.055, 0.310),   # Obrigatorio
    (3, 0.160, 0.398, 0.055, 0.390),   # Formacao de Preco
    (4, 0.215, 0.803, 0.075, 0.780),   # Minimo
    (5, 0.342, 0.803, 0.470, 0.750),   # Maximo
])

# 25) Os quatro modos de Formacao de Preco (mesma captura da 07)
annotate("07-grupo-detalhes.png", [
    (1, 0.167, 0.439, 0.055, 0.439),   # Normal
    (2, 0.167, 0.509, 0.055, 0.509),   # Brinde
    (3, 0.167, 0.580, 0.055, 0.580),   # Valor da Maior
    (4, 0.167, 0.651, 0.055, 0.651),   # Proporcional
], out_name="25-formacao-preco.png")

# ---------- Parte 4: incluir as opcoes no grupo ----------

# 08) Aba Opcoes do grupo, ainda vazia
# A aba Opcoes nao leva seta: o proprio sistema ja a destaca em vermelho, e a seta
# que apontava para ela cruzava o rotulo "Produtos".
annotate("08-grupo-aba-opcoes-vazia.png", [
    (1, 0.236, 0.338, 0.200, 0.410),   # BUSCAR E CADASTRAR
    (2, 0.400, 0.338, 0.395, 0.410),   # CADASTRAR NOVA OPCAO
    (3, 0.556, 0.338, 0.560, 0.410),   # COPIAR DE OUTRO
    (4, 0.748, 0.338, 0.790, 0.410),   # Filtrar Texto
])

# 09) Buscar e Cadastrar Opcoes
annotate("09-buscar-cadastrar.png", [
    (1, 0.300, 0.163, 0.130, 0.130),   # busca por nome ou codigo
    (2, 0.745, 0.236, 0.880, 0.200),   # Selecionar todos
    (3, 0.759, 0.875, 0.880, 0.930),   # Adicionar
])

# 10) As tres opcoes dentro do grupo
annotate("10-grupo-opcoes-lista.png", [
    (1, 0.215, 0.408, 0.250, 0.750),   # opcao (foto e nome herdados do complemento)
    (2, 0.786, 0.437, 0.830, 0.750),   # valor da opcao
    (3, 0.665, 0.905, 0.500, 0.815),   # SALVAR E SAIR (F2)
])

# ---------- Parte 5: cadastrar o produto ----------

# 11) Novo Setor
annotate("11-novo-setor.png", [
    (1, 0.555, 0.289, 0.940, 0.250),   # Nome Interno do Setor
    (2, 0.689, 0.874, 0.930, 0.920),   # SALVAR E SAIR (F2)
])

# 12) Modal do produto preenchido
annotate("12-modal-produto.png", [
    (1, 0.228, 0.437, 0.075, 0.450),   # ADICIONAR FOTO
    (2, 0.650, 0.252, 0.940, 0.200),   # Nome (obrigatorio)
    (3, 0.600, 0.341, 0.940, 0.300),   # Setor
    (4, 0.430, 0.430, 0.940, 0.400),   # Preco de Venda
    (5, 0.600, 0.625, 0.940, 0.620),   # Descricao
    (6, 0.665, 0.905, 0.665, 0.960),   # SALVAR E SAIR (F2)
])

# ---------- Parte 6: vincular o grupo ao produto ----------

# 13) Aba Grupo de Opcoes do produto
annotate("13-produto-grupo-vazio.png", [
    (1, 0.513, 0.163, 0.760, 0.220),   # aba Grupo de Opcoes
    (2, 0.500, 0.383, 0.760, 0.450),   # BUSCAR GRUPO E VINCULAR
    (3, 0.500, 0.508, 0.760, 0.580),   # CADASTRAR NOVO GRUPO DE OPCOES
])

# 14) Buscar e Vincular Grupo de Opcoes
annotate("14-vincular-grupo.png", [
    (1, 0.272, 0.354, 0.130, 0.300),   # marcar o grupo
    (2, 0.706, 0.805, 0.900, 0.870),   # Vincular
])

# 15) Grupo vinculado ao produto
annotate("15-produto-grupo-vinculado.png", [
    (1, 0.681, 0.352, 0.620, 0.470),   # Qtd. Min.
    (2, 0.748, 0.352, 0.745, 0.470),   # Qtd. Max.
    (3, 0.795, 0.352, 0.870, 0.470),   # Tipo (formacao de preco)
    (4, 0.665, 0.905, 0.500, 0.815),   # SALVAR E SAIR (F2)
])

# 16) O produto no cardapio, dentro do setor (contexto)
passthrough("16-produtos-lista.png")

# ---------- Parte 7: conferir no PDV ----------

# 17) Modal de selecao das opcoes no PDV
annotate("17-pdv-modal-opcoes.png", [
    (1, 0.318, 0.447, 0.200, 0.380),   # nome do grupo, contador e "Escolha 0 a 3"
    (2, 0.684, 0.500, 0.830, 0.460),   # opcao marcada
    (3, 0.688, 0.898, 0.830, 0.945),   # Adicionar ao carrinho - total atualizado
])

# 18) Carrinho com o item montado
annotate("18-pdv-carrinho-total.png", [
    (1, 0.800, 0.270, 0.620, 0.200),   # item + adicionais no carrinho
    (2, 0.955, 0.898, 0.720, 0.860),   # Valor Final
])

# ---------- Parte 8: filtro, edicao e edicao em lote ----------

# 19) Sub-aba Opcoes: todas as opcoes do cardapio
# Só duas setas: as que apontavam para o funil e para a coluna Valor cruzavam as
# tres linhas da tabela. O funil aparece em uso na imagem 20.
annotate("19-subaba-opcoes.png", [
    (1, 0.262, 0.133, 0.420, 0.133),   # sub-aba Opcoes
    (2, 0.920, 0.216, 0.900, 0.500),   # Editar em Lote
])

# 20) Filtro da coluna Descricao aplicado
annotate("20-filtro-opcoes.png", [
    (1, 0.337, 0.330, 0.280, 0.520),   # campo "Digite para filtrar..."
    (2, 0.345, 0.205, 0.620, 0.300),   # Limpar 1 filtro
])

# 21) Editar Opcoes em Lote - etapa 1 (selecao)
annotate("21-lote-selecao.png", [
    (1, 0.292, 0.172, 0.180, 0.140),   # Buscar por nome
    (2, 0.618, 0.238, 0.860, 0.190),   # Desmarcar Todas
    (3, 0.284, 0.240, 0.180, 0.275),   # contador "3 de 3 opcoes selecionadas"
    (4, 0.716, 0.875, 0.870, 0.920),   # PROXIMO
])

# 22) Etapa 2 (configuracao)
annotate("22-lote-config.png", [
    (1, 0.301, 0.206, 0.190, 0.170),   # marcar Preco de Venda
    (2, 0.330, 0.245, 0.190, 0.300),   # qual preco (Venda)
    (3, 0.700, 0.245, 0.860, 0.200),   # tipo de ajuste (Adicionar)
    (4, 0.330, 0.299, 0.190, 0.380),   # unidade (Valor R$)
    (5, 0.700, 0.299, 0.860, 0.340),   # quanto
    (6, 0.716, 0.875, 0.870, 0.920),   # PROCESSAR (F2)
])

# 23) Etapa 3 (resultado)
annotate("23-lote-concluido.png", [
    (1, 0.450, 0.176, 0.200, 0.140),   # barra "Concluido - 3 de 3 opcoes"
    (2, 0.293, 0.206, 0.200, 0.280),   # "3 sucesso"
    (3, 0.716, 0.875, 0.870, 0.920),   # FECHAR (ESC)
])

# 24) Precos reajustados na listagem
annotate("24-opcoes-atualizadas.png", [
    (1, 0.578, 0.314, 0.620, 0.550),   # coluna Valor com os novos precos
])

print("done")
