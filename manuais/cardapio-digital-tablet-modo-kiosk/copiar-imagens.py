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
    python copiar-imagens.py <url-do-zip>       # baixa o zip dessa url

Origens procuradas automaticamente, nesta ordem:
    1. c:\\projetos\\beetech-appgarcom-android\\docs\\images\\kiosk  (maquina do dono)
    2. ~/refs/beetech-appgarcom-android/docs/images/kiosk            (Cloud Agent)
    3. o zip mais recente em ~/.cursor/projects/workspace/uploads/   (Cloud Agent)

O suporte a zip e a url existe por um motivo pratico: no Cloud Agent, imagem
colada no chat NAO chega como arquivo -- ela entra no contexto do modelo, sem
caminho em disco e sem url, e nao ha como grava-la. Ja um zip publicado numa
url o agente baixa sozinho, porque o VM tem saida de internet liberada.

Link do Google Drive e aceito e convertido para download direto. Precisa ser
link de ARQUIVO (um .zip) compartilhado com "qualquer pessoa com o link", nao
link de pasta: pasta do Drive nao da para baixar sem credencial.

Tanto na pasta quanto no zip a busca e recursiva: nao importa se os PNG estao
na raiz ou dentro de subpastas.
"""

from __future__ import annotations

import re
import shutil
import sys
import tempfile
import urllib.error
import urllib.request
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


def extrair_zip(zip_path: Path, destino: Path | None = None) -> Path:
    destino = destino or Path(tempfile.mkdtemp(prefix="kiosk-zip-"))
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(destino)
    print(f"zip extraido: {zip_path.name}")
    return destino


def eh_url(texto: str) -> bool:
    return texto.startswith(("http://", "https://"))


# O id do arquivo aparece como "/file/d/<id>/" nos links de compartilhamento e
# como "?id=<id>" nos links de download que o proprio Drive gera.
ID_DRIVE = re.compile(r"/file/d/([\w-]+)|[?&]id=([\w-]+)")


DOMINIOS_DRIVE = (
    "drive.google.com",
    "drive.usercontent.google.com",
    "docs.google.com",
)


def normalizar_google_drive(url: str) -> str:
    """Converte link de compartilhamento do Drive em link de download direto."""
    if not any(dominio in url for dominio in DOMINIOS_DRIVE):
        return url

    if "/folders/" in url or "/drive/folders/" in url:
        sys.exit(
            "ERRO: esse e um link de PASTA do Google Drive, e pasta nao da para\n"
            "baixar sem credencial. Compacte a pasta num .zip, suba o .zip no\n"
            "Drive, compartilhe com 'qualquer pessoa com o link' e passe o link\n"
            "do arquivo."
        )

    achado = ID_DRIVE.search(url)
    if achado is None:
        sys.exit(f"ERRO: nao encontrei o id do arquivo neste link do Drive:\n  {url}")

    identificador = achado.group(1) or achado.group(2)
    # "confirm=t" pula a tela de aviso do antivirus, que o Drive mostra em vez do
    # arquivo quando ele e grande demais para ser verificado.
    return (
        "https://drive.usercontent.google.com/download"
        f"?id={identificador}&export=download&confirm=t"
    )


def baixar_zip(url: str, destino: Path) -> Path:
    alvo = destino / "origem.zip"
    # Sem User-Agent de navegador alguns hosts (o Drive entre eles) devolvem
    # pagina de erro em vez do arquivo.
    pedido = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

    print(f"baixando: {url}")
    try:
        with urllib.request.urlopen(pedido, timeout=300) as resposta:
            with alvo.open("wb") as saida:
                shutil.copyfileobj(resposta, saida)
    except urllib.error.HTTPError as erro:
        sys.exit(f"ERRO: o servidor respondeu {erro.code} ({erro.reason})\n  {url}")
    except urllib.error.URLError as erro:
        sys.exit(f"ERRO: nao consegui alcancar a url: {erro.reason}\n  {url}")

    tamanho = alvo.stat().st_size
    print(f"baixado: {tamanho / 1024:.0f} KB")

    if not zipfile.is_zipfile(alvo):
        sys.exit(
            "ERRO: o que baixou nao e um zip. Quase sempre isso significa que o\n"
            "link nao esta publico: o servidor devolveu a pagina de login em vez\n"
            "do arquivo. No Drive, abra Compartilhar e marque 'qualquer pessoa\n"
            "com o link'."
        )
    return alvo


def escolher_origem(argumento: str | None) -> tuple[Path, Path | None]:
    """Devolve (pasta de origem, pasta temporaria a apagar no fim)."""
    if argumento:
        if eh_url(argumento):
            # Normalizar antes de criar a pasta: link invalido aborta aqui, sem
            # deixar pasta temporaria para tras.
            url = normalizar_google_drive(argumento)
            temp = Path(tempfile.mkdtemp(prefix="kiosk-url-"))
            try:
                extrair_zip(baixar_zip(url, temp), temp)
            except BaseException:
                # Inclui o SystemExit dos erros de download: sem isso, cada
                # tentativa falha deixa uma pasta em /tmp.
                shutil.rmtree(temp, ignore_errors=True)
                raise
            return temp, temp

        alvo = Path(argumento)
        if alvo.is_file() and alvo.suffix.lower() == ".zip":
            temp = extrair_zip(alvo)
            return temp, temp
        if alvo.is_dir():
            return alvo, None
        sys.exit(f"ERRO: origem invalida (nao e pasta, zip nem url): {alvo}")

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
        "  python copiar-imagens.py <arquivo.zip>\n"
        "  python copiar-imagens.py <url-do-zip>"
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
