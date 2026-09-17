#!/usr/bin/env python3
"""Reescreve o indice de manuais do README.md a partir das pastas.

O indice era mantido a mao e envelheceu: em 17/09/2026 havia 99 pastas em
manuais/ e 63 linhas na tabela. Trinta e seis manuais prontos nao apareciam para
quem abre o repositorio, e ninguem percebeu porque nada quebra -- a tabela
continua valida, so incompleta.

A fonte da verdade passa a ser a pasta. O titulo de cada manual sai do H1 do
proprio arquivo, entao renomear ou reescrever o titulo ja aparece aqui.

Uso, da raiz do repositorio:
    python .cursor/skills/manual-sistema/scripts/indice-manuais.py
    python .cursor/skills/manual-sistema/scripts/indice-manuais.py --conferir

--conferir nao escreve: sai com codigo 1 se o README estiver desatualizado, para
entrar na conferencia de fim de manual junto do validar-imagens.py.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# .cursor/skills/manual-sistema/scripts/ -> raiz do repositorio
RAIZ = Path(__file__).resolve().parents[4]
MANUAIS = RAIZ / "manuais"
README = RAIZ / "README.md"

ABRE = "<!-- INDICE-MANUAIS:inicio -->"
FECHA = "<!-- INDICE-MANUAIS:fim -->"

# Arquivos de trabalho da pasta: nenhum deles e o manual.
AUXILIARES = {"MEMORIA.md", "fluxo-codigo.md", "texto-documentation.ia.md"}


def manual_da_pasta(pasta: Path) -> Path | None:
    """O .md que e o manual. Quase sempre <nome-da-pasta>.md; quando o arquivo
    tem outro nome (reforma-tributaria-ibscbs/reforma-tributaria.md), sobra um
    so depois de tirar os auxiliares."""
    preferido = pasta / f"{pasta.name}.md"
    if preferido.is_file():
        return preferido
    candidatos = [p for p in sorted(pasta.glob("*.md")) if p.name not in AUXILIARES]
    return candidatos[0] if len(candidatos) == 1 else None


def titulo(arquivo: Path) -> str:
    for linha in arquivo.read_text(encoding="utf-8").splitlines():
        if linha.startswith("# "):
            return linha[2:].strip()
    return arquivo.stem


def tabela() -> tuple[str, list[str]]:
    linhas = ["| Manual | Pasta |", "|--------|-------|"]
    avisos = []
    for pasta in sorted(p for p in MANUAIS.iterdir() if p.is_dir()):
        arquivo = manual_da_pasta(pasta)
        if arquivo is None:
            avisos.append(f"{pasta.name}: nao achei um .md unico que seja o manual")
            continue
        alvo = arquivo.relative_to(RAIZ)
        linhas.append(f"| {titulo(arquivo)} | [`{pasta.name}/`]({alvo}) |")
    return "\n".join(linhas), avisos


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--conferir", action="store_true",
                   help="nao escreve; sai com 1 se o README estiver desatualizado")
    args = p.parse_args()

    texto = README.read_text(encoding="utf-8")
    if ABRE not in texto or FECHA not in texto:
        sys.exit(f"ERRO: nao achei os marcadores {ABRE} / {FECHA} no README.md")

    corpo, avisos = tabela()
    antes, resto = texto.split(ABRE, 1)
    _, depois = resto.split(FECHA, 1)
    novo = f"{antes}{ABRE}\n\n{corpo}\n\n{FECHA}{depois}"

    for aviso in avisos:
        print(f"aviso  {aviso}")

    quantos = corpo.count("\n") - 1
    if args.conferir:
        if novo != texto:
            sys.exit(f"README.md desatualizado: rode sem --conferir ({quantos} manuais)")
        print(f"OK  indice do README em dia ({quantos} manuais)")
        return

    if novo == texto:
        print(f"OK  indice ja estava em dia ({quantos} manuais)")
        return
    README.write_text(novo, encoding="utf-8")
    print(f"OK  README.md atualizado com {quantos} manuais")


if __name__ == "__main__":
    main()
