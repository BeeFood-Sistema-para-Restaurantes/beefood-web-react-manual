#!/usr/bin/env python3
"""Confere que o texto dos slides foi reescrito, e não recortado da novidade.

    python .cursor/skills/carrossel-novidades/scripts/conferir-texto.py <slug>
    python ... <slug> --janela 6

Compara o texto visível dos slides com o texto publicado em
beefood.app/novidades e acusa qualquer sequência de N palavras que apareça igual
nos dois. Termo de tela ("Destaque na impressão", "Editar em Lote", "Cupom
Pedido") tem de repetir e por isso a janela padrão é 6 — nenhum rótulo do sistema
chega a seis palavras.

Não substitui a leitura: ele pega cópia literal, não pega roteiro que segue a
ordem do release com sinônimos. Isso quem vê é a tabela fato → ângulo → slide.
"""

import argparse
import re
import sys
import unicodedata
from html.parser import HTMLParser
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]  # .cursor/skills/<skill>/scripts -> raiz
sys.path.insert(0, str(Path(__file__).resolve().parent))

from pauta import FEED, baixar, fichas  # noqa: E402


class SomenteTexto(HTMLParser):
    """Texto visível do fragmento. Comentário de HTML fica de fora — é nota de
    implementação para quem edita o slide, não vai para a arte."""

    def __init__(self) -> None:
        super().__init__()
        self.pedacos: list[str] = []

    def handle_data(self, data: str) -> None:
        self.pedacos.append(data)

    def texto(self) -> str:
        return " ".join(self.pedacos)


def palavras(texto: str) -> list[str]:
    texto = unicodedata.normalize("NFKD", texto.lower())
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return re.findall(r"[a-z0-9]+", texto)


def sequencias(lista: list[str], n: int) -> set[tuple[str, ...]]:
    return {tuple(lista[i:i + n]) for i in range(len(lista) - n + 1)}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("slug", help="pasta em carrosseis/ e slug da novidade")
    p.add_argument("--janela", type=int, default=6,
                   help="tamanho da sequência considerada cópia (padrão 6)")
    args = p.parse_args()

    pasta = RAIZ / "carrosseis" / args.slug / "slides"
    if not pasta.is_dir():
        sys.exit(f"ERRO: não achei {pasta}")

    ficha = next((f for f in fichas(baixar(FEED)) if f["slug"] == args.slug), None)
    if ficha is None:
        sys.exit(f"ERRO: nenhuma novidade com slug {args.slug} no feed")

    # O título entra junto: copiar o título da novidade na capa é justamente o
    # erro mais comum, e foi o da primeira versão do destaque-impressao.
    fonte = sequencias(palavras(f"{ficha['titulo']} {ficha['texto']}"), args.janela)

    achados = 0
    conferidos = 0
    for arquivo in sorted(pasta.glob("*.html")):
        leitor = SomenteTexto()
        leitor.feed(arquivo.read_text(encoding="utf-8"))
        copiadas = sequencias(palavras(leitor.texto()), args.janela) & fonte
        for seq in sorted(copiadas):
            print(f"COPIADO  {arquivo.name}: {' '.join(seq)}")
            achados += 1
        conferidos += 1

    # A legenda entra na mesma régua dos slides: ela vai no mesmo post, e é ainda
    # mais fácil de encher com recorte do release, porque cabe texto longo.
    copy = pasta.parent / "copy-instagram.txt"
    if copy.is_file():
        copiadas = sequencias(palavras(copy.read_text(encoding="utf-8")), args.janela) & fonte
        for seq in sorted(copiadas):
            print(f"COPIADO  {copy.name}: {' '.join(seq)}")
            achados += 1
        conferidos += 1

    if achados:
        print(f"\n{achados} sequência(s) de {args.janela} palavras igual à "
              f"novidade. Reescreva: o slide tem de dizer a mesma coisa com "
              f"as palavras da publicação, não com as do release.")
        sys.exit(1)

    print(f"OK  nenhuma sequência de {args.janela} palavras repetida da novidade "
          f"({conferidos} arquivos)")


if __name__ == "__main__":
    main()
