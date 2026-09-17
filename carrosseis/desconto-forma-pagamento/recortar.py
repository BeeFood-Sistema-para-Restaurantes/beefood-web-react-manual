#!/usr/bin/env python3
"""Os recortes deste carrossel, tirados dos prints de producao dos manuais.

Nada aqui e captura nova: os manuais #64 (`cardapio-digital-desconto-formas`) e
#82 (`formas-recebimento`) ja versionam as telas desta novidade, e print de
manual e o mesmo print. O que falta e o recorte — a tela inteira reduzida para a
largura do slide fica com letra de 10 px no feed, e o selo de desconto tem 11 px
logicos na origem.

Onde o corte e so vertical o slide resolve sozinho (`.recorte--topo` com
`object-position`); onde ele e nos dois eixos, como no painel, precisa de
arquivo. Entao este script gera os cinco, e as coordenadas abaixo foram
**medidas no arquivo** com Pillow, nao estimadas na miniatura:

- nos prints de celular (780x1688, ou seja 390x844 logicos em DPR 2) o fundo da
  pagina e cinza (#f7f7f8) e os cartoes sao brancos puros, entao a borda de cada
  cartao e a faixa de linhas em que mais de 90% dos pixels ficam entre 200 e 250
  de luminancia. Foi assim que sairam 440..709 (cartao de valores do Pix) e
  440..753 (o do vale, uma linha mais alto porque o nome da bandeira quebra);
- nos prints de painel (2160x1350, 1440x900 logicos em DPR 1.5) o alvo foi
  achado pela tinta vermelha da lista aberta e do botao.

Uso, da raiz do repositorio:
    python3 carrosseis/desconto-forma-pagamento/recortar.py
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parents[2]
SAIDA = Path(__file__).resolve().parent / "imagens-puras"

MANUAL_CARDAPIO = RAIZ / "manuais/cardapio-digital-desconto-formas/imagens-puras"
MANUAL_FORMAS = RAIZ / "manuais/formas-recebimento/imagens-puras"

# (arquivo de origem, caixa (x0, y0, x1, y1), por que essa caixa)
RECORTES: dict[str, tuple[Path, tuple[int, int, int, int], str]] = {
    # Do "PAGUE ONLINE" ate a base do cartao do dinheiro. Termina no vao entre o
    # dinheiro (borda em 707) e o debito (borda em 724): corte dentro de um
    # cartao pareceria falha de render.
    "sacola-formas.png": (
        MANUAL_CARDAPIO / "07-cardapio-outras.png",
        (0, 124, 780, 716),
        "lista de formas com o selo de cada uma, antes da escolha",
    ),
    # O cartao de valores inteiro, com 10 px do cinza da pagina de cada lado
    # para a borda arredondada nao ficar rente ao corte.
    "total-pix.png": (
        MANUAL_CARDAPIO / "06-cardapio-pix.png",
        (0, 430, 780, 720),
        "R$ 39,00 - R$ 1,95 = R$ 37,05, com o Pix escolhido",
    ),
    "total-vale.png": (
        MANUAL_CARDAPIO / "08-cardapio-vale.png",
        (0, 430, 780, 764),
        "o mesmo R$ 39,00 + R$ 1,95 = R$ 40,95, com o vale escolhido",
    ),
    # Rotulo, campo e a lista aberta, colados nas bordas da propria lista
    # (x 1106..1401, medido numa linha dentro dela). Um corte mais largo pega o
    # "Percentual (%)" e o botao de salvar cortados no meio da palavra, e pega a
    # pagina escurecida atras do modal, que comeca em y 1079.
    "lista-ajuste.png": (
        MANUAL_FORMAS / "04-ajuste-pagamento.png",
        (1106, 790, 1404, 1186),
        "as cinco opcoes: sem ajuste, desconto e acrescimo, em % e em R$",
    ),
    # Tres das quatro colunas de botoes. A primeira coluna nao tem ajuste em
    # nenhuma das duas linhas, e cortada antes dela a grade sobe de 1,8x para
    # 2,4x — que e a diferenca entre ler e adivinhar o "+R$ 5,00".
    # O corte comeca em 1288, no meio do vao limpo entre a pilula CTRL+1 (que
    # acaba em 1283) e o cartao da segunda coluna (que comeca em 1293), e em 312,
    # abaixo do titulo da secao. A direita para em 1845: de 1846 em diante
    # comeca a borda do modal.
    "caixa-formas.png": (
        MANUAL_FORMAS / "08-pagamento-presencial.png",
        (1288, 312, 1845, 558),
        "dinheiro -1,00%, credito +3,00% e vale alimentacao +R$ 5,00",
    ),
}


def main() -> int:
    SAIDA.mkdir(parents=True, exist_ok=True)
    for nome, (origem, caixa, motivo) in RECORTES.items():
        if not origem.is_file():
            print(f"ERRO  nao achei {origem.relative_to(RAIZ)}")
            return 1
        recorte = Image.open(origem).crop(caixa)
        destino = SAIDA / nome
        recorte.save(destino)
        print(f"OK  {destino.relative_to(RAIZ)}  {recorte.width}x{recorte.height}"
              f"  <- {origem.name} {caixa}")
        print(f"    {motivo}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
