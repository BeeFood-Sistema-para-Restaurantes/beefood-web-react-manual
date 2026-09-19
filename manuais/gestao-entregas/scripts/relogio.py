"""Acerta o relógio dos prints do aplicativo, sem redesenhar texto.

Os prints da segunda rodada foram tirados na madrugada de 19/09/2026, um e dois dias depois dos
da primeira. A tela do app mostra a data em letras grandes e vermelhas — *Previsão Entrega* —, e
um manual que abre com `17/09/2026 23:44` na seção 1 e mostra `19/09/2026 01:50` na seção 4 não é
o mesmo dia nem a mesma história. Este arquivo resolve isso **copiando a linha de data de um
print da primeira rodada** para dentro do print novo.

Copiar, e não escrever: a fonte do aplicativo é a Roboto do Android, que não existe nesta
máquina. Texto redesenhado aqui sairia com outro desenho de `9` e outro espaçamento, e ficaria
como remendo em cima do print. A linha transplantada é o mesmo Roboto, no mesmo corpo, com o
mesmo antisserrilhado — os dois prints saíram do mesmo emulador, em 1440x3120, e a linha da data
ocupa a mesma altura de tinta nos dois.

O transplante é de **tinta**, não de retângulo: a linha de referência virá como máscara de
opacidade, e a máscara é pintada com a cor de tinta e sobre a cor de fundo **do print de
destino**. É o que faz a troca funcionar embaixo da sombra da gaveta de notificação, onde o
Android escurece tudo o que está atrás — lá o vermelho é `228,63,50` sobre `245`, e não
`244,67,54` sobre branco. Colar um retângulo branco ali deixaria um remendo claro.

O que fica registrado, e é o limite do que este arquivo faz:

* muda **só a linha da data** dos cartões da lista. Endereço, valor, crachá do pedido e qualquer
  outra informação da tela continuam como o emulador as mostrou;
* a data que entra é a de um print da primeira rodada que já está no repositório — nenhum horário
  é inventado aqui;
* todos os cartões de um print ficam com a mesma data, que é como o dado nasce: pedidos semeados
  na mesma rodada têm a mesma previsão de entrega, e é o que os quatro cartões da seção 1 do #112
  mostram desde a primeira rodada.

Uso, de dentro do `annotate.py` de um manual:

    import relogio
    relogio.ajustar(img, relogio.tinta(REF))   # `img` é o print aberto, antes de recortar
"""

import numpy as np
from PIL import Image

# A linha da data é a única coisa vermelha da largura de uma frase dentro de um cartão: o `#` do
# crachá é laranja (verde alto), o *Cobrar* é verde, e a faixa vermelha da borda esquerda mora
# nos primeiros pixels da tela.
BORDA = 60
ALTURA = (40, 58)      # altura de tinta aceitável para a linha da data, em pixels
CARACTERES = 16        # o relógio ⏱ e os 15 caracteres de `DD/MM/AAAA HH:MM`
FOLGA = 10             # sobra copiada em volta da linha, onde a máscara é toda transparente


def _vermelho(rgb, borda=BORDA):
    """Tinta vermelha por **proporção**, não por brilho.

    Atrás de uma janela modal o Android escurece a tela toda, e o `244,67,54` do app chega a
    `98,27,22`. Um corte por brilho (`R > 150`) enxergaria a lista da frente e perderia a de trás,
    que é justamente onde estão duas das três telas do #113.
    """
    R, G, B = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    v = (R > 1.8 * G) & (R > 1.8 * B) & (R > 55)
    v[:, :borda] = False
    return v


def _corridas(linha, vao=3):
    """Agrupa colunas com tinta em caracteres, separados por `vao` colunas vazias."""
    xs = np.nonzero(linha)[0]
    fora, ini, ant = [], None, None
    for x in xs:
        if ant is None or x - ant > vao:
            if ini is not None:
                fora.append((ini, ant + 1))
            ini = x
        ant = x
    if ini is not None:
        fora.append((ini, ant + 1))
    return fora


def _mais_comum(faixa):
    cores, contas = np.unique(faixa.reshape(-1, 3), axis=0, return_counts=True)
    return cores[contas.argmax()].astype(float)


def _cor_da_tinta(faixa):
    """A cor cheia do texto: a mais comum **entre os pixels vermelhos** da linha.

    O fundo é maioria absoluta dentro da linha — letra é pouco pixel —, então a moda simples
    devolveria branco.
    """
    return _mais_comum(faixa[_vermelho(faixa.astype(int), borda=0)])


def faixas(img):
    """As linhas de data do print: `(y0, y1, x_texto0, x_texto1)`, de cima para baixo.

    `x_texto0` é onde começa o primeiro caractere **depois** do relógio ⏱ — o ícone fica onde
    está, só o texto é trocado.
    """
    rgb = np.asarray(img.convert("RGB")).astype(int)
    v = _vermelho(rgb)
    tinta = v.sum(axis=1) > 30
    achadas, y, H = [], 0, len(tinta)
    while y < H:
        if tinta[y]:
            y0 = y
            while y < H and tinta[y]:
                y += 1
            if ALTURA[0] <= y - y0 <= ALTURA[1]:
                cs = _corridas(v[y0:y].sum(axis=0) > 0)
                if len(cs) == CARACTERES:
                    achadas.append((y0, y, int(cs[1][0]), int(cs[-1][1])))
        y += 1
    return achadas


def tinta(referencia):
    """Lê a linha de data de um print de referência como máscara de opacidade.

    Devolve `(mascara, base)`: `mascara` é um array `0..1` do tamanho da linha com folga, e
    `base` é a distância do topo dela até a última fileira de tinta — a linha de apoio dos
    números. Colar alinhando pela base põe o texto na mesma altura do cartão, seja qual for a
    folga que o print de destino tenha em cima.
    """
    ref = Image.open(referencia).convert("RGB") if isinstance(referencia, str) else referencia
    achadas = faixas(ref)
    if not achadas:
        raise RuntimeError(f"nenhuma linha de data encontrada em {referencia}")
    y0, y1, x0, x1 = achadas[0]
    rgb = np.asarray(ref).astype(float)
    corte = rgb[y0 - FOLGA:y1 + FOLGA, x0:x1 + FOLGA]
    fundo = _mais_comum(rgb[y0 - FOLGA:y0 - 2, x0:x1].astype(np.uint8))
    letra = _cor_da_tinta(rgb[y0:y1, x0:x1].astype(np.uint8))
    # O canal verde é o que mais separa tinta de fundo neste vermelho (67 contra 255).
    a = np.clip((fundo[1] - corte[:, :, 1]) / (fundo[1] - letra[1]), 0, 1)
    # Só pixel puxado para o vermelho entra na máscara. Na folga de baixo já começa o endereço,
    # que é cinza escuro: pelo canal verde ele passaria por tinta cheia e sairia vermelho.
    a = np.where(corte[:, :, 0] - corte[:, :, 1] > 25, a, 0)
    return a, y1 - (y0 - FOLGA)


def ajustar(img, origem):
    """Troca a data de todas as linhas de data de `img` pela da `tinta()`.

    Cada linha é apagada com a cor de fundo medida logo abaixo dela, e a máscara é pintada com a
    cor de tinta medida na própria linha — o que preserva o escurecimento da gaveta de
    notificação. Devolve quantas linhas trocou.
    """
    mascara, base = origem
    mh, mw = mascara.shape
    rgb = np.asarray(img.convert("RGB")).astype(float)
    achadas = faixas(img)
    for (y0, y1, x0, x1) in achadas:
        letra = _cor_da_tinta(rgb[y0:y1, x0:x1].astype(np.uint8))
        xf = max(x1, x0 + mw) + 3
        # Apaga fileira por fileira, cada uma com a cor mais comum dela mesma. A sombra da
        # gaveta de notificação é um degradê vertical: um retângulo de cor única no meio dela
        # aparece como remendo mais claro em volta do texto.
        for y in range(y0 - 3, y1 + 3):
            fileira = rgb[y, x0:xf].astype(np.uint8)
            rgb[y, x0:xf] = _mais_comum(fileira[~_vermelho(fileira[None, :, :].astype(int),
                                                           borda=0)[0]][None, :, :])
        t, e = y1 - base, x0
        alvo = rgb[t:t + mh, e:e + mw]
        a = mascara[:alvo.shape[0], :alvo.shape[1]][:, :, None]
        rgb[t:t + mh, e:e + mw] = alvo * (1 - a) + letra * a
    img.paste(Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8)))
    return len(achadas)
