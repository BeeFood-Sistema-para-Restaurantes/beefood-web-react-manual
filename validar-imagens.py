#!/usr/bin/env python3
"""Confere se as imagens que os manuais referenciam existem de verdade.

Um manual publicado com imagem faltando quebra em silencio: o markdown fica
valido, o texto continua legivel e so quem abre a pagina descobre. Este script
faz a checagem antes.

O que verifica, para cada pasta em manuais/:

1. Toda imagem referenciada pelo manual existe em imagens-tratadas/.
2. Toda imagem referenciada pelo texto-documentation.ia.md tambem existe
   (e o prompt de publicacao nao lista imagem que o manual nao usa).
3. Nao ha arquivo orfao em imagens-tratadas/ -- presente na pasta, mas que
   nenhum manual referencia.

Uso:
    python validar-imagens.py            # todos os manuais
    python validar-imagens.py caixa      # so um manual (nome da pasta)

Codigo de saida: 0 se tudo certo, 1 se houver imagem faltando.
Orfao nao derruba a saida: e aviso, nao erro.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
MANUAIS = RAIZ / "manuais"

# Imagem em markdown: ![alt](caminho)
REF_MARKDOWN = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
# O prompt de publicacao lista caminhos soltos, sem sintaxe de imagem.
REF_SOLTA = re.compile(r"imagens-tratadas/([\w.-]+\.(?:png|jpe?g|webp|gif))")

EXTENSOES = {".png", ".jpg", ".jpeg", ".webp", ".gif"}


def arquivo_do_manual(pasta: Path) -> Path | None:
    """O .md principal e o que tem o nome da pasta."""
    candidato = pasta / f"{pasta.name}.md"
    if candidato.is_file():
        return candidato
    # Alguns manuais antigos usam nome curto (ex.: reforma-tributaria.md).
    outros = [
        p
        for p in pasta.glob("*.md")
        if p.name not in {"MEMORIA.md", "fluxo-codigo.md", "texto-documentation.ia.md"}
    ]
    return outros[0] if len(outros) == 1 else None


def referencias_markdown(md: Path) -> list[str]:
    texto = md.read_text(encoding="utf-8")
    saida = []
    for alvo in REF_MARKDOWN.findall(texto):
        alvo = alvo.split()[0].strip("<>")  # ignora title entre aspas
        if Path(alvo).suffix.lower() in EXTENSOES:
            saida.append(alvo)
    return saida


def checar(pasta: Path) -> tuple[int, int, list[str]]:
    """Devolve (faltando, orfaos, linhas do relatorio) de um manual."""
    linhas: list[str] = []
    manual = arquivo_do_manual(pasta)
    if manual is None:
        linhas.append("  ! nao identifiquei o .md principal desta pasta")
        return 0, 0, linhas

    tratadas = pasta / "imagens-tratadas"
    refs = referencias_markdown(manual)
    faltando = [r for r in refs if not (pasta / r).is_file()]

    linhas.append(f"  {manual.name}: {len(refs)} referencia(s)")
    for r in faltando:
        linhas.append(f"    FALTA  {r}")

    # Prompt de publicacao: precisa listar exatamente o que o manual usa.
    prompt = pasta / "texto-documentation.ia.md"
    if prompt.is_file():
        no_prompt = REF_SOLTA.findall(prompt.read_text(encoding="utf-8"))
        so_no_manual = [Path(r).name for r in refs]
        divergencia = [n for n in dict.fromkeys(no_prompt) if n not in so_no_manual]
        if divergencia:
            linhas.append(
                f"    ! o prompt de publicacao lista {len(divergencia)} imagem(ns) "
                "que o manual nao usa:"
            )
            for n in divergencia:
                linhas.append(f"        {n}")

    # Orfaos: arquivo na pasta que ninguem referencia.
    orfaos: list[str] = []
    if tratadas.is_dir():
        usados = {Path(r).name for r in refs}
        orfaos = sorted(
            p.name
            for p in tratadas.iterdir()
            if p.suffix.lower() in EXTENSOES and p.name not in usados
        )
        for n in orfaos:
            linhas.append(f"    orfao  {n}")

    if not faltando and not orfaos:
        existentes = len(refs) - len(faltando)
        linhas.append(f"    ok     {existentes} imagem(ns) no lugar")

    return len(faltando), len(orfaos), linhas


def main() -> int:
    if not MANUAIS.is_dir():
        sys.exit(f"ERRO: pasta nao encontrada: {MANUAIS}")

    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    pastas = sorted(p for p in MANUAIS.iterdir() if p.is_dir())
    if alvo:
        pastas = [p for p in pastas if p.name == alvo]
        if not pastas:
            sys.exit(f"ERRO: manual nao encontrado: {alvo}")

    total_faltando = total_orfaos = 0
    com_problema: list[str] = []

    for pasta in pastas:
        faltando, orfaos, linhas = checar(pasta)
        print(f"\n{pasta.name}")
        for l in linhas:
            print(l)
        total_faltando += faltando
        total_orfaos += orfaos
        if faltando:
            com_problema.append(f"{pasta.name} ({faltando} faltando)")

    print("\n" + "=" * 60)
    print(f"manuais verificados: {len(pastas)}")
    print(f"imagens faltando   : {total_faltando}")
    print(f"orfaos             : {total_orfaos}")
    if com_problema:
        print("\nnao publicar estes manuais:")
        for m in com_problema:
            print(f"  - {m}")
        return 1
    print("\ntodos os manuais tem as imagens que referenciam.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
