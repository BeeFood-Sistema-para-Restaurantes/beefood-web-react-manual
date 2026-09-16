#!/usr/bin/env python3
"""Recorta, dos prints de produção do manual, as peças que entram nas telas
desenhadas do totem e do tablet.

    python carrosseis/traducao-cardapio-presencial/preparar-telas.py

Por que recortar em vez de usar o print inteiro dentro do aparelho: print de
tela cheia de totem ou de tablet reduzido para caber num slide fica com letra de
4 px no feed — ilegível. As telas dos slides são desenhadas em CSS, com
tipografia ampliada, e recebem **as fotos reais** destes recortes. Assim o
layout é o do sistema e as imagens são as do sistema; só a escala do texto muda.

Origem (prints que o dono mandou, versionados no manual):

- `manual-08-totem-menu.png`    — totem em inglês, 1186x699
- `manual-09-tablet-cardapio.png` — tablet em inglês, 1280x800

As coordenadas foram medidas no arquivo, não estimadas: o corpo do totem começa
em x=288, o banner vai de y=17 a y=367 e a linha de cards tem faixas em
298-573, 585-860 e 873-1148.
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

PASTA = Path(__file__).resolve().parent
PURAS = PASTA / "imagens-puras"

# (arquivo de origem, caixa, destino, tamanho final)
RECORTES = [
    # Banner do totem com a pílula de bandeiras e o CANCEL ORDER reais. É a
    # peça mais valiosa: prova a novidade com pixel de produção.
    ("manual-08-totem-menu.png", (288, 17, 1158, 367), "tela-totem-banner.png", None),
    # As três bebidas do setor Drinks. São latas parecidas de propósito: é o
    # que o setor tem de verdade (Cola US, Coca Cola 350ml, Coca Zero 350ml).
    ("manual-08-totem-menu.png", (298, 457, 573, 699), "foto-bebida-1.png", (275, 242)),
    ("manual-08-totem-menu.png", (585, 457, 860, 699), "foto-bebida-2.png", (275, 242)),
    ("manual-08-totem-menu.png", (873, 457, 1148, 699), "foto-bebida-3.png", (275, 242)),
    # As mesmas bebidas no print do tablet, em enquadramento mais fechado. Servem
    # para a grade do totem não repetir a mesma lata quatro vezes.
    ("manual-09-tablet-cardapio.png", (432, 178, 672, 390), "foto-bebida-4.png", None),
    ("manual-09-tablet-cardapio.png", (432, 412, 672, 624), "foto-bebida-5.png", None),
]


def main() -> None:
    faltando = [o for o, *_ in RECORTES if not (PURAS / o).is_file()]
    if faltando:
        sys.exit("ERRO: faltam os prints de origem: " + ", ".join(sorted(set(faltando))))

    for origem, caixa, destino, tamanho in RECORTES:
        with Image.open(PURAS / origem) as im:
            peca = im.convert("RGB").crop(caixa)
            if tamanho and peca.size != tamanho:
                peca = peca.resize(tamanho, Image.LANCZOS)
            peca.save(PURAS / destino)
        print(f"OK  {destino}  {peca.size[0]}x{peca.size[1]}  <- {origem}{caixa}")


if __name__ == "__main__":
    main()
