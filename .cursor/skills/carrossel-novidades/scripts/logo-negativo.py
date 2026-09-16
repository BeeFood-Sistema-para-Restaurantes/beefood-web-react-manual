#!/usr/bin/env python3
"""Deriva a versão do logo para fundo escuro a partir da de fundo claro.

A marca da BeeFood é um selo de abelha: corpo e letras em preto, asas em
branco, tarjas em amarelo, "food" em vermelho. Em fundo escuro, o arquivo
original perde o preto (some no fundo) e as asas brancas ficam soltas no ar.

Achatar tudo em branco com `filter: brightness(0) invert(1)` resolve a
visibilidade e mata a identidade: vão embora o amarelo da abelha e o vermelho
do "food", que é justamente o que faz o logo parecer o logo.

O que este script faz é o negativo de verdade — só o tom de cinza inverte, a
cor fica:

- pixel sem cor (preto, branco, cinza da borda serrilhada) vira tinta BRANCA
  com alfa proporcional ao quanto ele era escuro. Preto vira branco opaco,
  branco vira transparente (e aí a asa mostra o fundo do slide, como mostrava
  o papel), e o cinza do meio sai meio transparente — o que faz a borda casar
  com qualquer fundo escuro, não só com um;
- pixel com cor (amarelo, vermelho) passa intacto.

Uso:
    python logo-negativo.py            # regrava assets/logo-beefood-escuro.png
    python logo-negativo.py --conferir # só avisa se o arquivo está defasado

Rode de novo quando o `logo-beefood.png` mudar.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("ERRO: falta Pillow — pip install pillow")

SKILL = Path(__file__).resolve().parent.parent
CLARO = SKILL / "assets" / "logo-beefood.png"
ESCURO = SKILL / "assets" / "logo-beefood-escuro.png"

# Acima disso o pixel é cor da marca (amarelo, vermelho) e não tinta neutra.
CROMA = 40


def negativo(origem: Path) -> Image.Image:
    im = Image.open(origem).convert("RGBA")
    saida = Image.new("RGBA", im.size, (0, 0, 0, 0))
    pixels_origem = im.load()
    pixels_saida = saida.load()

    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = pixels_origem[x, y]
            if a == 0:
                continue
            if max(r, g, b) - min(r, g, b) > CROMA:
                pixels_saida[x, y] = (r, g, b, a)
                continue
            # Tinta neutra: o quanto ela era escura é o quanto de branco entra.
            tom = (r + g + b) // 3
            pixels_saida[x, y] = (255, 255, 255, (255 - tom) * a // 255)
    return saida


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--conferir", action="store_true",
                    help="não grava; sai com erro se o arquivo estiver defasado")
    args = ap.parse_args()

    if not CLARO.is_file():
        sys.exit(f"ERRO: logo de fundo claro ausente: {CLARO}")

    novo = negativo(CLARO)

    if args.conferir:
        if not ESCURO.is_file():
            sys.exit(f"ERRO: falta {ESCURO.name} — rode logo-negativo.py")
        if Image.open(ESCURO).convert("RGBA").tobytes() != novo.tobytes():
            sys.exit(f"ERRO: {ESCURO.name} está defasado — rode logo-negativo.py")
        print(f"OK  {ESCURO.name} confere com {CLARO.name}")
        return

    novo.save(ESCURO)
    print(f"OK  {ESCURO.name}  {novo.size[0]}x{novo.size[1]}")


if __name__ == "__main__":
    main()
