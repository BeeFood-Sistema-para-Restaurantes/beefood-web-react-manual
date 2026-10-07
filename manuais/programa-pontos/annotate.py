"""Anota as capturas do #126 — Programa de pontos.

As dezessete puras foram capturadas aqui mesmo, por `capturar-painel.py` e
`capturar-cardapio.py`. Este arquivo só desenha seta verde e etiqueta numerada por cima
delas e grava em `imagens-tratadas/`, a única pasta que o `.md` referencia.

Três coisas deste manual que valem explicação:

* **As margens são montadas em memória**, dentro de `annotate()` — nunca gravadas na pura.
  Gravá-las tornava o script não repetível: a segunda execução somava margem sobre margem e
  deslocava todas as setas. Pura é o print, e só. É a regra que o #125 pagou para aprender.
* **Há margem em cima (`topo`), e não só nos lados.** A tela do histórico é uma tabela: o
  cabeçalho das colunas fica abaixo da busca, e qualquer seta que venha de uma faixa lateral
  atravessa a linha da busca. Com faixa em cima, a seta desce direto na coluna.
* **Os seis prints de celular usam as mesmas duas margens** (0,22 à esquerda e 0,10 à direita),
  mesmo quando uma delas sobra. Imagem publicada em sequência com largura diferente fica
  torta na página, e a largura final só é igual se a margem for igual.

As coordenadas estão em **fração da pura**, lidas numa grade de frações sobreposta à captura
(gerada fora do repositório, em `/tmp`). `alvo()` converte para fração da imagem final, já
somando as margens; a etiqueta é dada direto em fração da final, porque ela mora **fora** do
print, na faixa clara, onde a fração da pura seria negativa.

Mire a **borda** do elemento quando ele tem texto: seta apontada para o meio de um rótulo
cobre uma letra, e isso só aparece na conferência em tamanho real.
"""

import math
import os

from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

VERDE = (22, 150, 78)
BRANCO = (255, 255, 255)
A_LINHA = 235
A_ETIQ = 245
FUNDO = (233, 237, 239)
FONTES = [
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def font(sz):
    for c in FONTES:
        if os.path.exists(c):
            return ImageFont.truetype(c, sz)
    raise RuntimeError("nenhuma fonte bold encontrada")


def alvo(m=0.0, md=0.0, topo=0.0):
    """Fração da pura -> fração da imagem final, descontando as margens de `annotate()`."""

    def f(x, y):
        return (m + (1 - m - md) * x, topo + (1 - topo) * y)

    return f


def seta(d, x0, y0, x1, y1, w):
    col = VERDE + (A_LINHA,)
    d.line([(x0, y0), (x1, y1)], fill=col, width=w)
    ang = math.atan2(y1 - y0, x1 - x0)
    L = w * 4.0
    for s in (0.5, -0.5):
        d.line([(x1, y1), (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))],
               fill=col, width=w)


def etiqueta(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 3, cy - r - 3, cx + r + 3, cy + r + 3], fill=BRANCO + (245,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=VERDE + (A_ETIQ,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
           t, fill=BRANCO, font=fnt)


def annotate(nome, marcadores=(), r=30, w=5, m=0.0, md=0.0, topo=0.0):
    """`marcadores`: (número, alvo_x, alvo_y, etiqueta_x, etiqueta_y) — tudo em fração da final.

    `m`, `md` e `topo` são as faixas claras à esquerda, à direita e em cima, em fração da
    imagem **final**. Elas existem porque etiqueta desenhada dentro de tela cheia cobre texto:
    com a faixa, a etiqueta mora fora do print e a seta entra pela borda.
    """
    pura = Image.open(os.path.join(SRC, nome)).convert("RGB")
    Wp, Hp = pura.size
    if m or md or topo:
        largura = round(Wp / (1 - m - md))
        altura = round(Hp / (1 - topo))
        tela = Image.new("RGB", (largura, altura), FUNDO)
        tela.paste(pura, (round(largura * m), altura - Hp))
        pura = tela
    img = pura.convert("RGBA")
    W, H = img.size
    over = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    fnt = font(int(r * 1.25))
    for (num, tfx, tfy, efx, efy) in marcadores:
        tx, ty, ex, ey = tfx * W, tfy * H, efx * W, efy * H
        ang = math.atan2(ty - ey, tx - ex)
        seta(d, ex + (r + 6) * math.cos(ang), ey + (r + 6) * math.sin(ang), tx, ty, w)
        etiqueta(d, ex, ey, r, num, fnt)
    Image.alpha_composite(img, over).convert("RGB").save(os.path.join(OUT, nome))
    print("OK", nome, W, H)


# ---------------------------------------------------------------------------------------
# Painel — 01 a 10
# ---------------------------------------------------------------------------------------
# A tela inteira do sistema, com o menu à esquerda: é o mapa do caminho, e a única imagem do
# manual em que o menu importa. Não precisa de margem — o vão branco entre o menu e o cartão
# da aba comporta as etiquetas, e sobra espaço à direita da faixa de aviso.
annotate("01-ativar-programa-pontos.png", [
    (1, 0.146, 0.359, 0.200, 0.359),   # Fidelidade (CRM) -> Programa de pontos
    (2, 0.153, 0.075, 0.185, 0.145),   # aba Configuração
    (3, 0.910, 0.220, 0.962, 0.185),   # a faixa do processamento da madrugada
    (4, 0.240, 0.327, 0.185, 0.290),   # o switch que liga o programa
    (5, 0.566, 0.145, 0.500, 0.145),   # MIGRAR PARA CASHBACK / TRAZER PARA PONTOS
], r=30, w=5)

# Daqui até a 05 são recortes de cartão da aba Configuração, e todos usam a mesma margem
# esquerda: o conteúdo encosta na borda esquerda do cartão, e etiqueta desenhada ali cobriria
# o rótulo do campo.
M = 0.18
a = alvo(M)
annotate("02-regras-de-acumulo.png", [
    (1, *a(0.024, 0.310), 0.075, 0.310),   # pontos ganhos a cada R$ 1,00
    (2, *a(0.024, 0.562), 0.075, 0.562),   # validade dos pontos
    (3, *a(0.512, 0.298), 0.508, 0.298),   # o canal travado, que não se desliga
    (4, *a(0.512, 0.646), 0.508, 0.646),   # os cinco canais opcionais
    (5, *a(0.046, 0.776), 0.075, 0.776),   # o quadro de exemplo
], r=26, w=4, m=M)

a = alvo(M)
annotate("03-bonus-e-taxa-de-entrega.png", [
    (1, *a(0.914, 0.144), 0.754, 0.144),   # switch do bônus de boas-vindas
    (2, *a(0.038, 0.347), 0.075, 0.347),   # quantos pontos de bônus
    (3, *a(0.914, 0.659), 0.754, 0.659),   # switch da taxa de entrega
    (4, *a(0.036, 0.692), 0.075, 0.692),   # o subtítulo, que diz o que o nome não diz
    (5, *a(0.038, 0.867), 0.075, 0.867),   # pontos por real de taxa
], r=26, w=4, m=M)

a = alvo(M)
annotate("04-recompensas-de-desconto.png", [
    (1, *a(0.040, 0.318), 0.075, 0.318),   # uma recompensa já cadastrada
    (2, *a(0.930, 0.318), 0.836, 0.318),   # a lixeira
    (3, *a(0.024, 0.787), 0.075, 0.787),   # Valor do desconto (R$)
    (4, *a(0.420, 0.787), 0.524, 0.700),   # Pontos necessários
    (5, *a(0.880, 0.845), 0.902, 0.730),   # ADICIONAR
], r=26, w=4, m=M)

a = alvo(M)
annotate("05-recompensas-de-produto.png", [
    (1, *a(0.040, 0.379), 0.075, 0.379),   # a linha que ficou "Produto #2515303"
    (2, *a(0.040, 0.574), 0.075, 0.574),   # a linha que ficou com o nome do produto
    (3, *a(0.045, 0.863), 0.075, 0.863),   # Selecionar produto
    (4, *a(0.552, 0.746), 0.633, 0.640),   # Pontos necessários
    (5, *a(0.880, 0.818), 0.902, 0.700),   # ADICIONAR
], r=26, w=4, m=M)

# O histórico é uma tabela. A margem de cima existe porque o cabeçalho das colunas fica
# **abaixo** da linha da busca: seta vinda de faixa lateral atravessaria a busca inteira. A da
# direita existe porque a coluna Pontos é a última, encostada na borda do cartão.
TOPO6, MD6 = 0.09, 0.08
a = alvo(0, MD6, TOPO6)
annotate("06-historico-de-pontos.png", [
    (1, *a(0.695, 0.208), 0.640, 0.042),   # a busca
    (2, *a(0.985, 0.208), 0.965, 0.279),   # o filtro Todos os tipos
    (3, *a(0.408, 0.317), 0.327, 0.378),   # a coluna Tipo
    (4, *a(0.987, 0.317), 0.965, 0.420),   # a coluna Pontos, com sinal
], r=30, w=5, md=MD6, topo=TOPO6)

# Saldo por Cliente: os quatro cartões de total em cima, a busca, e uma linha por cliente. O
# miolo de cada linha é vazio e comporta etiqueta; os cartões de total não, porque encostam na
# barra das abas — daí a faixa em cima. O olho do extrato é o último elemento da linha, com o
# saldo logo antes dele: alcançá-lo pela esquerda riscaria o saldo, e por isso há faixa também
# à direita.
TOPO7, MD7 = 0.08, 0.04
a = alvo(0, MD7, TOPO7)
annotate("07-saldo-por-cliente.png", [
    (1, *a(0.342, 0.140), 0.328, 0.036),   # os quatro totais
    (2, *a(0.655, 0.261), 0.557, 0.320),   # Novo Saldo
    (3, *a(0.857, 0.559), 0.662, 0.594),   # o saldo do cliente, na linha dele
    (4, *a(0.930, 0.552), 0.975, 0.588),   # o olho que abre o extrato
], r=30, w=5, md=MD7, topo=TOPO7)

# O extrato é um painel lateral estreito, e todo o conteúdo dele é centralizado ou encostado à
# esquerda: só a faixa clara dá lugar para etiqueta.
M8 = 0.16
a = alvo(M8)
annotate("08-extrato-do-cliente.png", [
    (1, *a(0.410, 0.311), 0.055, 0.311),   # SALDO ATUAL
    (2, *a(0.085, 0.410), 0.055, 0.410),   # ADICIONAR / REMOVER / TRANSFERIR
    (3, *a(0.030, 0.519), 0.055, 0.519),   # Gerado / Usado / Expirado
    (4, *a(0.148, 0.763), 0.055, 0.763),   # a primeira linha do extrato
    (5, *a(0.148, 0.821), 0.055, 0.860),   # o motivo, que o cliente também lê
], r=26, w=4, m=M8)

# A janela de adicionar pontos tem fundo escurecido nos dois lados: etiqueta ali se lê bem e
# não cobre nada da própria janela.
annotate("09-adicionar-pontos.png", [
    (1, 0.282, 0.338, 0.175, 0.338),   # Pontos
    (2, 0.282, 0.468, 0.175, 0.468),   # Expira em (dias) — opcional
    (3, 0.282, 0.639, 0.175, 0.639),   # Motivo *
    (4, 0.725, 0.771, 0.850, 0.771),   # CONFIRMAR (F2)
], r=28, w=4)

# A fila é tabela curta e larga. O vão entre o menu do sistema e o cartão da aba comporta as
# etiquetas da esquerda; a coluna Mensagem é alcançada pela faixa da direita, porque ela é a
# última e o texto dela é longo.
MD10 = 0.06
a = alvo(0, MD10)
annotate("10-fila-de-processamento.png", [
    (1, *a(0.237, 0.240), 0.172, 0.240),   # a faixa do processamento da madrugada
    (2, *a(0.243, 0.532), 0.172, 0.532),   # os quatro contadores
    (3, *a(0.240, 0.778), 0.172, 0.778),   # a coluna Status
    (4, *a(0.835, 0.850), 0.970, 0.850),   # a coluna Mensagem
], r=30, w=5, md=MD10)

# ---------------------------------------------------------------------------------------
# Cardápio digital — 11 a 16
# ---------------------------------------------------------------------------------------
# Os seis prints de celular compartilham as duas margens, e por isso saem todos com a mesma
# largura final. A da direita existe pelo motivo oposto à da esquerda: a coluna direita da
# tela é onde moram o selo do produto, os botões de resgate e o rodapé do cardápio, e
# alcançá-los pela esquerda obrigaria a seta a atravessar a tela por cima do nome do item.
MC, MDC = 0.22, 0.10
a = alvo(MC, MDC)

annotate("11-cardapio-faixa-pontos.png", [
    (1, *a(0.090, 0.369), 0.110, 0.369),   # a faixa "Acumule pontos a cada compra"
    (2, *a(0.930, 0.564), 0.955, 0.564),   # o selo de presente no produto resgatável
    (3, *a(0.875, 0.962), 0.955, 0.962),   # Perfil, no rodapé
], r=32, w=4, m=MC, md=MDC)

annotate("12-cardapio-perfil-programa-pontos.png", [
    (1, *a(0.875, 0.962), 0.955, 0.962),   # Perfil, agora aceso
    (2, *a(0.980, 0.840), 0.955, 0.840),   # Programa de pontos, no menu do perfil
], r=32, w=4, m=MC, md=MDC)

annotate("13-cardapio-meus-pontos.png", [
    (1, *a(0.093, 0.138), 0.110, 0.138),   # o saldo
    (2, *a(0.038, 0.224), 0.110, 0.210),   # Extrato
    (3, *a(0.065, 0.263), 0.110, 0.265),   # Ganhou
    (4, *a(0.135, 0.300), 0.110, 0.320),   # o motivo digitado no painel
    (5, *a(0.065, 0.354), 0.110, 0.390),   # Usou
    (6, *a(0.195, 0.968), 0.110, 0.968),   # Ver o que você pode ganhar
], r=32, w=4, m=MC, md=MDC)

annotate("14-cardapio-recompensas.png", [
    (1, *a(0.172, 0.130), 0.110, 0.155),   # a regra de acúmulo e a validade
    (2, *a(0.170, 0.308), 0.110, 0.308),   # uma recompensa de desconto
    (3, *a(0.915, 0.315), 0.955, 0.250),   # Disponível
    (4, *a(0.915, 0.479), 0.955, 0.420),   # Faltam 59 pts
    (5, *a(0.170, 0.550), 0.110, 0.550),   # a recompensa de produto
    (6, *a(0.195, 0.966), 0.110, 0.966),   # Ver meu extrato
], r=32, w=4, m=MC, md=MDC)

annotate("15-cardapio-trocar-pontos.png", [
    (1, *a(0.105, 0.101), 0.110, 0.115),   # o cartão Programa de Pontos
    (2, *a(0.093, 0.306), 0.110, 0.306),   # quantos pontos ele tem
    (3, *a(0.900, 0.371), 0.955, 0.320),   # RESGATAR
    (4, *a(0.905, 0.518), 0.955, 0.468),   # INSUFICIENTE
    (5, *a(0.900, 0.588), 0.955, 0.640),   # ADICIONAR, da recompensa de produto
    (6, *a(0.093, 0.969), 0.110, 0.969),   # Ganhe 29 pontos, no rodapé
], r=32, w=4, m=MC, md=MDC)

annotate("16-cardapio-resgate-aplicado.png", [
    (1, *a(0.100, 0.431), 0.110, 0.431),   # a recompensa resgatada
    (2, *a(0.900, 0.444), 0.955, 0.390),   # REMOVER
    (3, *a(0.100, 0.520), 0.110, 0.540),   # as outras, agora indisponíveis
    (4, *a(0.945, 0.862), 0.955, 0.800),   # o total do pedido, já com o desconto
    (5, *a(0.093, 0.969), 0.110, 0.969),   # Ganhe 29 pontos: o desconto não tira o ganho
], r=32, w=4, m=MC, md=MDC)

# ---------------------------------------------------------------------------------------
# 17 — o mesmo cardápio no computador
# ---------------------------------------------------------------------------------------
# Faixa do topo da página, de largura inteira: no computador o programa não vira faixa
# amarela, vira cartão na coluna da direita. Sobra branco entre o nome da loja e o cartão.
annotate("17-banner-pontos-computador.png", [
    (1, 0.730, 0.485, 0.635, 0.470),   # o cartão Programa de Pontos
    (2, 0.726, 0.760, 0.660, 0.900),   # Ver o que você pode ganhar
], r=30, w=5)

print("pronto")
