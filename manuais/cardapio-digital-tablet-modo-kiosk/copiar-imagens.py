#!/usr/bin/env python3
"""Copia as capturas do manual do Modo Kiosk para dentro deste manual.

As imagens deste manual nao sao produzidas aqui: elas vem do repositorio do app
Android, em docs/images/kiosk/. Este script copia essas capturas para
imagens-puras/ (backup) e imagens-tratadas/ (as que o manual referencia), e
avisa se alguma faltar.

A lista de arquivos NAO esta escrita aqui: ela e lida do proprio manual, na
ordem em que aparece. Assim o script nunca fica dessincronizado do texto.

Uso:
    python copiar-imagens.py                 # usa a origem padrao
    python copiar-imagens.py <pasta-origem>  # usa outra pasta

Origem padrao (maquina do dono, Windows):
    c:\\projetos\\beetech-appgarcom-android\\docs\\images\\kiosk
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
MANUAL = AQUI / "cardapio-digital-tablet-modo-kiosk.md"
PURAS = AQUI / "imagens-puras"
TRATADAS = AQUI / "imagens-tratadas"

ORIGENS_PADRAO = [
    Path(r"c:\projetos\beetech-appgarcom-android\docs\images\kiosk"),
    Path.home() / "refs" / "beetech-appgarcom-android" / "docs" / "images" / "kiosk",
]


def imagens_do_manual() -> list[str]:
    """Nomes dos PNG referenciados pelo manual, na ordem de aparicao."""
    texto = MANUAL.read_text(encoding="utf-8")
    return re.findall(r"imagens-tratadas/([\w.-]+\.png)", texto)


def escolher_origem(argumento: str | None) -> Path:
    if argumento:
        origem = Path(argumento)
        if not origem.is_dir():
            sys.exit(f"ERRO: a pasta de origem nao existe: {origem}")
        return origem

    for candidata in ORIGENS_PADRAO:
        if candidata.is_dir():
            return candidata

    sys.exit(
        "ERRO: nenhuma pasta de origem encontrada. Tentadas:\n  "
        + "\n  ".join(str(c) for c in ORIGENS_PADRAO)
        + "\n\nPasse a pasta como argumento:\n"
        "  python copiar-imagens.py <pasta-com-os-21-png>"
    )


def main() -> int:
    if not MANUAL.is_file():
        sys.exit(f"ERRO: manual nao encontrado: {MANUAL}")

    esperadas = imagens_do_manual()
    if not esperadas:
        sys.exit("ERRO: o manual nao referencia nenhuma imagem. Algo esta errado.")

    origem = escolher_origem(sys.argv[1] if len(sys.argv) > 1 else None)
    print(f"origem : {origem}")
    print(f"destino: {TRATADAS.name}/ e {PURAS.name}/")
    print(f"manual referencia {len(esperadas)} imagens\n")

    PURAS.mkdir(exist_ok=True)
    TRATADAS.mkdir(exist_ok=True)

    copiadas, faltando = [], []
    for ordem, nome in enumerate(esperadas, start=1):
        arquivo = origem / nome
        if arquivo.is_file():
            shutil.copy2(arquivo, PURAS / nome)
            shutil.copy2(arquivo, TRATADAS / nome)
            copiadas.append(nome)
            print(f"  {ordem:2d}. OK      {nome}")
        else:
            faltando.append(nome)
            print(f"  {ordem:2d}. FALTA   {nome}")

    # Arquivo na origem que o manual nao usa costuma ser captura antiga ou
    # renomeada -- vale avisar em vez de copiar em silencio.
    sobrando = sorted(
        p.name for p in origem.glob("*.png") if p.name not in set(esperadas)
    )

    print(f"\ncopiadas: {len(copiadas)}/{len(esperadas)}")
    if sobrando:
        print("\nna origem, mas nao usados pelo manual:")
        for nome in sobrando:
            print(f"  - {nome}")

    if faltando:
        print(f"\nFALTAM {len(faltando)} arquivo(s). O manual nao esta completo.")
        return 1

    print("\nTudo copiado. Proximo passo:")
    print("  git add manuais/cardapio-digital-tablet-modo-kiosk/imagens-*")
    print('  git commit -m "docs(modo-kiosk): adiciona as capturas do manual"')
    print("  git push")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
