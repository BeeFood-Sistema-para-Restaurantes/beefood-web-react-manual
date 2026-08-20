#!/usr/bin/env python3
"""Copia as capturas do manual do Modo Kiosk para dentro deste manual.

As imagens deste manual nao sao produzidas aqui: elas vem do repositorio do app
Android, em docs/images/kiosk/. Este script copia essas capturas para
imagens-puras/ (backup) e imagens-tratadas/ (as que o manual referencia), e
avisa se alguma faltar.

A lista de arquivos NAO esta escrita aqui: ela e lida do proprio manual, na
ordem em que aparece. Assim o script nunca fica dessincronizado do texto.

Uso:
    python copiar-imagens.py                    # procura a origem sozinho
    python copiar-imagens.py <pasta>            # usa essa pasta
    python copiar-imagens.py <arquivo.zip>      # usa esse zip

Origens procuradas automaticamente, nesta ordem:
    1. c:\\projetos\\beetech-appgarcom-android\\docs\\images\\kiosk  (maquina do dono)
    2. ~/refs/beetech-appgarcom-android/docs/images/kiosk            (Cloud Agent)
    3. o zip mais recente em ~/.cursor/projects/workspace/uploads/   (Cloud Agent)

O suporte a zip existe por um motivo pratico: no Cloud Agent, imagem colada no
chat NAO chega como arquivo -- so documento chega, e vai para a pasta uploads.
Um .zip e documento, entao ele chega.

Tanto na pasta quanto no zip a busca e recursiva: nao importa se os PNG estao
na raiz ou dentro de subpastas.
"""

from __future__ import annotations

import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
MANUAL = AQUI / "cardapio-digital-tablet-modo-kiosk.md"
PURAS = AQUI / "imagens-puras"
TRATADAS = AQUI / "imagens-tratadas"

UPLOADS = Path.home() / ".cursor" / "projects" / "workspace" / "uploads"

PASTAS_PADRAO = [
    Path(r"c:\projetos\beetech-appgarcom-android\docs\images\kiosk"),
    Path.home() / "refs" / "beetech-appgarcom-android" / "docs" / "images" / "kiosk",
]


def imagens_do_manual() -> list[str]:
    """Nomes dos PNG referenciados pelo manual, na ordem de aparicao."""
    texto = MANUAL.read_text(encoding="utf-8")
    return re.findall(r"imagens-tratadas/([\w.-]+\.png)", texto)


def extrair_zip(zip_path: Path) -> Path:
    destino = Path(tempfile.mkdtemp(prefix="kiosk-zip-"))
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(destino)
    print(f"zip extraido: {zip_path.name}")
    return destino


def escolher_origem(argumento: str | None) -> tuple[Path, Path | None]:
    """Devolve (pasta de origem, pasta temporaria a apagar no fim)."""
    if argumento:
        alvo = Path(argumento)
        if alvo.is_file() and alvo.suffix.lower() == ".zip":
            temp = extrair_zip(alvo)
            return temp, temp
        if alvo.is_dir():
            return alvo, None
        sys.exit(f"ERRO: origem invalida (nao e pasta nem .zip): {alvo}")

    for pasta in PASTAS_PADRAO:
        if pasta.is_dir():
            return pasta, None

    if UPLOADS.is_dir():
        zips = sorted(UPLOADS.glob("*.zip"), key=lambda p: p.stat().st_mtime)
        if zips:
            temp = extrair_zip(zips[-1])
            return temp, temp

    sys.exit(
        "ERRO: nenhuma origem encontrada. Procurei em:\n  "
        + "\n  ".join(str(p) for p in PASTAS_PADRAO)
        + f"\n  {UPLOADS}/*.zip"
        + "\n\nPasse a origem como argumento:\n"
        "  python copiar-imagens.py <pasta-com-os-png>\n"
        "  python copiar-imagens.py <arquivo.zip>"
    )


def indexar(raiz: Path) -> dict[str, Path]:
    """Mapeia nome do arquivo -> caminho, buscando em toda a arvore."""
    encontrados: dict[str, Path] = {}
    for arquivo in raiz.rglob("*.png"):
        # O primeiro que aparecer ganha; nomes repetidos em subpastas sao raros
        # e o relatorio mostra de onde veio cada um.
        encontrados.setdefault(arquivo.name, arquivo)
    return encontrados


def main() -> int:
    if not MANUAL.is_file():
        sys.exit(f"ERRO: manual nao encontrado: {MANUAL}")

    esperadas = imagens_do_manual()
    if not esperadas:
        sys.exit("ERRO: o manual nao referencia nenhuma imagem. Algo esta errado.")

    origem, temporaria = escolher_origem(sys.argv[1] if len(sys.argv) > 1 else None)
    try:
        disponiveis = indexar(origem)

        print(f"origem : {origem}")
        print(f"destino: {TRATADAS.name}/ e {PURAS.name}/")
        print(f"manual referencia {len(esperadas)} imagens")
        print(f"origem tem {len(disponiveis)} png\n")

        PURAS.mkdir(exist_ok=True)
        TRATADAS.mkdir(exist_ok=True)

        copiadas, faltando = [], []
        for ordem, nome in enumerate(esperadas, start=1):
            arquivo = disponiveis.get(nome)
            if arquivo is not None:
                shutil.copy2(arquivo, PURAS / nome)
                shutil.copy2(arquivo, TRATADAS / nome)
                copiadas.append(nome)
                print(f"  {ordem:2d}. OK      {nome}")
            else:
                faltando.append(nome)
                print(f"  {ordem:2d}. FALTA   {nome}")

        # PNG na origem que o manual nao usa costuma ser captura antiga ou
        # renomeada -- vale avisar em vez de ignorar em silencio.
        sobrando = sorted(set(disponiveis) - set(esperadas))

        print(f"\ncopiadas: {len(copiadas)}/{len(esperadas)}")
        if sobrando:
            print("\nna origem, mas nao usados pelo manual:")
            for nome in sobrando:
                print(f"  - {nome}")

        if faltando:
            print(f"\nFALTAM {len(faltando)} arquivo(s). O manual nao esta completo.")
            return 1

        print("\nTudo copiado. Confira e suba:")
        print("  python ../../validar-imagens.py cardapio-digital-tablet-modo-kiosk")
        print("  git add manuais/cardapio-digital-tablet-modo-kiosk/imagens-*")
        print('  git commit -m "docs(modo-kiosk): adiciona as capturas do manual"')
        print("  git push")
        return 0
    finally:
        if temporaria is not None:
            shutil.rmtree(temporaria, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
