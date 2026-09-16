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

# Nome de produto não é prosa do release: sai dos dois lados antes da comparação.
#
# "Totem de Autoatendimento e no Cardápio Digital no Tablet" tem nove palavras e
# estourava a janela sozinho, só porque a novidade também precisa dizer em quais
# aplicativos a coisa funciona. Exigir sinônimo aqui não deixa o texto mais
# autoral, deixa errado — e a saída fácil seria a pior de todas: trocar por
# "totem" e "tablet" e deixar o leitor adivinhar se o cardápio do celular também
# mudou.
#
# Esta lista é só para nome que o dono do produto escolheu, nunca para frase que
# você quer reaproveitar. Cada linha nova aqui é uma frase que o conferidor
# deixa passar para sempre.
NOMES_DE_PRODUTO = (
    "Totem de Autoatendimento",
    "Cardápio Digital no Tablet",
    "Cardápio Digital",
    "Cupom Pedido",
    "Editar em Lote",
    "Destaque na impressão",
    "Salvar e Sair",
)


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


def sem_acento(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", texto.lower())
    return "".join(c for c in texto if not unicodedata.combining(c))


def palavras(texto: str) -> list[str]:
    texto = sem_acento(texto)
    for nome in NOMES_DE_PRODUTO:
        # Vira um token só: apagar juntaria as palavras da volta e inventaria
        # sequências que ninguém escreveu.
        texto = texto.replace(sem_acento(nome), " nomedeproduto ")
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
        texto = copy.read_text(encoding="utf-8")
        # O cabeçalho do arquivo é nota de produção: ele diz qual novidade é,
        # com o título dela, e nada disso vai para o Instagram. Conferir o
        # cabeçalho só ensinava a escrever o cabeçalho errado.
        if "====" in texto:
            texto = texto[texto.index("===="):]
        copiadas = sequencias(palavras(texto), args.janela) & fonte
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
