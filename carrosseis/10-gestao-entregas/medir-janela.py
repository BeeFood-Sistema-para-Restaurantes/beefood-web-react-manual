#!/usr/bin/env python3
"""Mede a caixa da janela numa captura de tela inteira.

As janelas do painel são fotografadas inteiras (`capturar-telas.py --medir`) e
recortadas depois, com a caixa em pixel de arquivo. Medir no DOM não serviu:
`[role="dialog"]` casa com mais de um elemento da página. Aqui a conta é ótica —
o véu escurece a página e a janela é a única coisa branca.

    python medir-janela.py despacho-regras lista-entregadores app-lojas
"""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

PURAS = Path(__file__).resolve().parent / "imagens-puras"


def medir(nome: str) -> None:
    with Image.open(PURAS / f"{nome}.png") as imagem:
        cinza = imagem.convert("L")
        # 250 separa o branco da janela do branco esmaecido pelo véu.
        caixa = cinza.point(lambda v: 255 if v >= 250 else 0).getbbox()
    print(f'    "{nome}": {caixa},')


if __name__ == "__main__":
    for nome in sys.argv[1:]:
        medir(nome)
