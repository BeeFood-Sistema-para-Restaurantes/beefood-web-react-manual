#!/usr/bin/env python3
"""Monta o .zip de entrega do carrossel: as imagens e a legenda.

    python .cursor/skills/carrossel-novidades/scripts/empacotar.py <slug>

Junta `png/*.png` e `copy-instagram.txt` em `entrega/<slug>.zip`. Os nomes dentro
do zip são os mesmos de fora, sem pasta intermediária, porque quem recebe
costuma arrastar o conteúdo direto para o celular e a ordem de publicação é a
ordem alfabética dos arquivos.

A folha de contato fica de fora: ela é ferramenta de revisão, e no meio das oito
imagens alguém acaba postando a nona por engano.
"""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]  # .cursor/skills/<skill>/scripts -> raiz


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("slug", help="pasta em carrosseis/")
    args = p.parse_args()

    pasta = RAIZ / "carrosseis" / args.slug
    if not pasta.is_dir():
        sys.exit(f"ERRO: não achei {pasta}")

    imagens = sorted((pasta / "png").glob("*.png"))
    if not imagens:
        sys.exit(f"ERRO: nenhum png em {pasta / 'png'} — rode o renderizar.py")

    copy = pasta / "copy-instagram.txt"
    if not copy.is_file():
        sys.exit(f"ERRO: falta {copy.name} — a entrega é imagem mais legenda")

    destino = pasta / "entrega" / f"{args.slug}.zip"
    destino.parent.mkdir(exist_ok=True)

    # Data fixa no cabeçalho de cada membro: sem isso o zip muda de conteúdo a
    # cada rodada só pela hora, e o diff do commit fica ilegível.
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for arquivo in [*imagens, copy]:
            info = zipfile.ZipInfo(arquivo.name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, arquivo.read_bytes())

    kb = destino.stat().st_size // 1024
    print(f"OK  {destino.relative_to(RAIZ)}  {len(imagens)} imagens + "
          f"{copy.name}  {kb} KB")


if __name__ == "__main__":
    main()
