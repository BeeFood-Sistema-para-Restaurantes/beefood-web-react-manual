#!/usr/bin/env python3
"""Lê a pauta dos carrosséis direto das Novidades do BeeFood.

A página `beefood.app/novidades` é um SPA, mas publica um RSS em
`/novidades/feed.xml` com **tudo em texto puro**: título, data, tipo
(Novidade / Melhoria), áreas e o corpo inteiro do anúncio. Ou seja: não há
motivo para raspar HTML nem para dirigir navegador só para saber o que sair.

Este script também aponta o **manual correspondente**, quando existe. É a
costura com a skill de manual: a novidade dá o gancho e a data, o manual dá o
passo a passo conferido no sistema. Nada aqui escreve em `manuais/`.

Uso:
    python pauta.py                              # as 15 novidades mais recentes
    python pauta.py --limite 40 --tipo Novidade
    python pauta.py --buscar cupom
    python pauta.py --slug destaque-impressao    # material bruto de um item
    python pauta.py --slug destaque-impressao --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from email.utils import parsedate_to_datetime
from pathlib import Path
from xml.etree import ElementTree

FEED = "https://beefood.app/novidades/feed.xml"
RAIZ = Path(__file__).resolve().parents[4]  # .cursor/skills/<skill>/scripts -> raiz
MANUAIS = RAIZ / "manuais"

# Palavras que não ajudam a casar novidade com manual.
VAZIAS = {
    "a", "as", "o", "os", "de", "do", "da", "dos", "das", "e", "em", "no", "na",
    "nos", "nas", "para", "por", "com", "sem", "que", "se", "um", "uma", "ao",
    "aos", "mais", "agora", "novo", "nova", "voce", "seu", "sua", "the",
}


def baixar(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "beefood-carrossel/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def normalizar(texto: str) -> str:
    tabela = str.maketrans("áàâãäéèêëíìîïóòôõöúùûüçñ", "aaaaaeeeeiiiiooooouuuucn")
    return texto.lower().translate(tabela)


def fichas(xml: bytes) -> list[dict]:
    raiz = ElementTree.fromstring(xml)
    saida = []
    for item in raiz.iterfind("./channel/item"):
        def campo(nome: str) -> str:
            el = item.find(nome)
            return (el.text or "").strip() if el is not None else ""

        categorias = [(c.text or "").strip() for c in item.iterfind("category")]
        link = campo("link")
        data = campo("pubDate")
        saida.append({
            "slug": link.rstrip("/").rsplit("/", 1)[-1],
            "titulo": campo("title"),
            "link": link,
            "data": parsedate_to_datetime(data).strftime("%d/%m/%Y") if data else "",
            "tipo": categorias[0] if categorias else "",
            "areas": categorias[1:],
            "texto": re.sub(r"\s+", " ", campo("description")).strip(),
        })
    return saida


def manual_de(ficha: dict) -> Path | None:
    """Acha a pasta de manual que fala da mesma funcionalidade, se houver.

    Primeiro tenta o caminho óbvio (a pasta com o mesmo slug); depois cai numa
    contagem de palavras em comum entre o título da novidade e o nome da pasta.
    Devolve `None` sem drama: novidade sem manual é normal.
    """
    if not MANUAIS.is_dir():
        return None

    direto = MANUAIS / ficha["slug"]
    if direto.is_dir():
        return direto

    alvo = {p for p in normalizar(ficha["titulo"]).replace("-", " ").split()
            if len(p) > 3 and p not in VAZIAS}
    if not alvo:
        return None

    melhor, nota_melhor = None, 0
    for pasta in sorted(p for p in MANUAIS.iterdir() if p.is_dir()):
        palavras = {p for p in normalizar(pasta.name).split("-") if len(p) > 3}
        nota = len(alvo & palavras)
        if nota > nota_melhor:
            melhor, nota_melhor = pasta, nota
    return melhor if nota_melhor >= 2 else None


def imprimir_lista(lista: list[dict]) -> None:
    print(f"{'DATA':<12}{'TIPO':<11}{'SLUG':<44}TÍTULO")
    print("-" * 110)
    for f in lista:
        print(f"{f['data']:<12}{f['tipo']:<11}{f['slug'][:42]:<44}{f['titulo']}")
    print(f"\n{len(lista)} item(ns). Detalhe: pauta.py --slug <slug>")


def imprimir_ficha(ficha: dict) -> None:
    manual = manual_de(ficha)
    print(f"# {ficha['titulo']}\n")
    print(f"- Tipo: {ficha['tipo']}")
    print(f"- Data: {ficha['data']}")
    print(f"- Áreas: {', '.join(ficha['areas']) or '—'}")
    print(f"- Link: {ficha['link']}")
    if manual:
        print(f"- Manual relacionado: {manual.relative_to(RAIZ)}/")
        md = manual / f"{manual.name}.md"
        if md.is_file():
            print(f"  - texto: {md.relative_to(RAIZ)}")
        puras = manual / "imagens-puras"
        if puras.is_dir():
            qtd = len(list(puras.glob("*.png")))
            print(f"  - capturas prontas: {qtd} em {puras.relative_to(RAIZ)}/")
    else:
        print("- Manual relacionado: nenhum (as capturas terão de ser novas)")
    print(f"\n## Texto publicado\n\n{ficha['texto']}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slug", help="detalha um item e aponta o manual relacionado")
    ap.add_argument("--tipo", help="filtra por tipo (Novidade, Melhoria)")
    ap.add_argument("--buscar", help="filtra por termo no título ou no texto")
    ap.add_argument("--limite", type=int, default=15)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    try:
        lista = fichas(baixar(FEED))
    except Exception as erro:
        sys.exit(f"ERRO ao ler {FEED}: {erro}")

    if args.slug:
        achado = next((f for f in lista if f["slug"] == args.slug), None)
        if achado is None:
            sys.exit(f"ERRO: slug não encontrado: {args.slug}")
        manual = manual_de(achado)
        if args.json:
            achado = dict(achado)
            achado["manual"] = str(manual.relative_to(RAIZ)) if manual else None
            print(json.dumps(achado, ensure_ascii=False, indent=2))
        else:
            imprimir_ficha(achado)
        return 0

    if args.tipo:
        alvo = normalizar(args.tipo)
        lista = [f for f in lista if normalizar(f["tipo"]) == alvo]
    if args.buscar:
        termo = normalizar(args.buscar)
        lista = [f for f in lista
                 if termo in normalizar(f["titulo"]) or termo in normalizar(f["texto"])]

    lista = lista[: args.limite]
    if args.json:
        print(json.dumps(lista, ensure_ascii=False, indent=2))
    else:
        imprimir_lista(lista)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
