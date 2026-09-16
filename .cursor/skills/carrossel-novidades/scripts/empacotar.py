#!/usr/bin/env python3
"""Monta o .zip de entrega do carrossel: as imagens e a legenda.

    python .cursor/skills/carrossel-novidades/scripts/empacotar.py <slug>

Junta `png/*.png` e `copy-instagram.txt` em `entrega/<slug>.zip`. Os nomes dentro
do zip são os mesmos de fora, sem pasta intermediária, porque quem recebe
costuma arrastar o conteúdo direto para o celular e a ordem de publicação é a
ordem alfabética dos arquivos.

A folha de contato fica de fora: ela é ferramenta de revisão, e no meio das
imagens do carrossel alguém acaba postando uma imagem a mais por engano.

Se o carrossel tiver uma **capa alternativa** (`capa-alternativa/png/*.png`),
ela entra numa subpasta de mesmo nome dentro do zip. Fica separada de propósito:
quem arrasta o conteúdo para o celular leva só o carrossel, e quem quiser trocar
a capa vai buscar na pasta.
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

    alternativas = sorted((pasta / "capa-alternativa" / "png").glob("*.png"))

    destino = pasta / "entrega" / f"{args.slug}.zip"
    destino.parent.mkdir(exist_ok=True)

    membros = [(a.name, a) for a in imagens]
    membros.append((copy.name, copy))
    membros += [(f"capa-alternativa/{a.name}", a) for a in alternativas]

    # Data fixa no cabeçalho de cada membro: sem isso o zip muda de conteúdo a
    # cada rodada só pela hora, e o diff do commit fica ilegível.
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for nome, arquivo in membros:
            info = zipfile.ZipInfo(nome, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, arquivo.read_bytes())

    kb = destino.stat().st_size // 1024
    extra = f" + {len(alternativas)} capa(s) alternativa(s)" if alternativas else ""
    print(f"OK  {destino.relative_to(RAIZ)}  {len(imagens)} imagens + "
          f"{copy.name}{extra}  {kb} KB")


if __name__ == "__main__":
    main()
