#!/usr/bin/env python3
"""Confere que o texto dos slides foi reescrito, e não recortado da fonte.

    python .cursor/skills/carrossel/scripts/conferir-texto.py <slug>
    python ... <slug> --janela 6
    python ... <pasta> --novidade <slug-da-novidade>
    python ... <pasta> --fonte https://beefood.com.br/sistema-dark-kitchen/
    python ... <pasta> --fonte manuais/gestao-entregas-mapa-painel

A pasta do carrossel costuma ter o mesmo nome da novidade. Quando o slug
publicado é comprido demais para virar nome de pasta
(`cardapio-digital-avisos-banners-capas-midia`), `--novidade` diz qual entrada
do feed é a fonte. Em peça do gênero **função do sistema** não existe feed:
`--fonte` aponta a página do site, que é copy pronta e por isso ainda mais fácil
de recortar sem perceber.

E há o terceiro caso: **módulo em liberação**, sem release e sem página de
vendas — o fato vive só no manual. Aí `--fonte` recebe um caminho do
repositório em vez de uma URL, e pode ser repetido; pasta vale como o
`.md` de dentro dela. É o cenário mais perigoso dos três, porque o manual foi
escrito pela casa: o texto é bom, está à mão, e recortá-lo não soa como cópia.

Compara o texto visível dos slides com o texto da fonte e acusa qualquer
sequência de N palavras que apareça igual nos dois. Termo de tela ("Destaque na
impressão", "Editar em Lote", "Cupom Pedido") tem de repetir e por isso a janela
padrão é 6 — nenhum rótulo do sistema chega a seis palavras.

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

from pauta import FEED, baixar, fichas, ler_pagina  # noqa: E402

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
    "Capas e Destaques",
    # Nome de campanha padrão das Campanhas Inteligentes. Este tem seis
    # palavras e estoura a janela sozinho — e é rótulo de cartão na tela, o
    # que o leitor procura quando abre a aba.
    "Recebeu o cardápio e não pediu",
)


# Classe cujo conteúdo NÃO é copy, e por isso não conta quando se compara uma
# peça com outra. São dois motivos:
#
# - interface desenhada (`tela-`, `cupom`) — duas peças que mostram a mesma
#   tela repetem "MELTED brioche bun…" porque é o produto, não porque alguém
#   copiou a copy da outra;
# - cromo do slide (`contador`, `pontos`, `arraste`) — "1 de 9" e "arraste"
#   estão em todo carrossel por construção, e colados ao texto vizinho ainda
#   inventam sequências que ninguém escreveu.
FORA_DA_COPY = ("tela-", "cupom", "contador", "pontos", "arraste")

# Tag sem fechamento não conta profundidade: `<img>` dentro de uma tela
# desenhada incrementaria o contador para sempre e o bloco nunca terminaria.
VOID = {"img", "br", "hr", "input", "meta", "link", "source", "wbr"}


class SomenteTexto(HTMLParser):
    """Texto visível do fragmento. Comentário de HTML fica de fora — é nota de
    implementação para quem edita o slide, não vai para a arte.

    Com `sem_desenho`, a interface desenhada e o cromo do slide também ficam de
    fora.
    Serve para comparar uma peça com outra: ali o que interessa é a **copy**, e
    a interface desenhada é prova, que pode e deve se repetir.
    """

    def __init__(self, sem_desenho: bool = False) -> None:
        super().__init__()
        self.pedacos: list[str] = []
        self._sem_desenho = sem_desenho
        self._pulando = 0
        self._fundo = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        if not self._sem_desenho or tag in VOID:
            return
        # A profundidade tem de ser contada mesmo dentro do bloco pulado: sem
        # isso, a primeira tag de fechamento de um filho reabriria a captura.
        if self._pulando:
            self._fundo += 1
            return
        classe = dict(attrs).get("class") or ""
        if any(c.startswith(FORA_DA_COPY) for c in classe.split()):
            self._pulando = 1
            self._fundo = 0

    def handle_endtag(self, tag: str) -> None:
        if not self._pulando:
            return
        if self._fundo:
            self._fundo -= 1
        else:
            self._pulando = 0

    def handle_data(self, data: str) -> None:
        if not self._pulando:
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


# "    12|" no começo da linha: o prefixo que as ferramentas de leitura põem na
# saída e que volta para dentro do arquivo quando alguém reescreve um trecho a
# partir do que leu. Dentro de comentário de HTML ele não aparece na arte, e por
# isso sobrevive a rodadas de revisão; dentro de texto, vira sujeira renderizada.
MARCA_DE_LINHA = re.compile(r"^ *\d+\|")


def ler_fonte_local(caminho: str) -> tuple[str, str]:
    """O texto de um manual do repositório, e como ele se chama na saída.

    Pasta de manual vale pelo `.md` de dentro dela, que é onde o passo a passo
    mora; `MEMORIA.md` e `fluxo-codigo.md` ficam de fora porque são nota de
    produção e ninguém recorta slide deles.
    """
    alvo = (RAIZ / caminho) if not Path(caminho).is_absolute() else Path(caminho)
    if alvo.is_dir():
        arquivos = [alvo / f"{alvo.name}.md"]
        if not arquivos[0].is_file():
            arquivos = sorted(alvo.glob("*.md"))
    else:
        arquivos = [alvo]

    partes = []
    for arquivo in arquivos:
        if not arquivo.is_file():
            raise FileNotFoundError(arquivo)
        partes.append(arquivo.read_text(encoding="utf-8"))
    return " ".join(partes), caminho


def conferir_marcas(pasta: Path) -> int:
    achados = 0
    for arquivo in sorted(pasta.rglob("*")):
        if arquivo.suffix not in (".html", ".md", ".txt", ".json"):
            continue
        for n, linha in enumerate(arquivo.read_text(encoding="utf-8").splitlines(), 1):
            if MARCA_DE_LINHA.match(linha):
                rel = arquivo.relative_to(pasta)
                print(f"MARCA DE LINHA  {rel}:{n}: {linha.strip()[:60]}")
                achados += 1
    return achados


def copy_da_peca(pasta: Path) -> str:
    """Só a LEGENDA do `copy-instagram.txt`.

    O cabeçalho é nota de produção e o texto alternativo descreve a imagem —
    duas peças que mostram a mesma prova descrevem a mesma coisa, e é certo que
    descrevam. O que não pode repetir é a legenda.
    """
    copy = pasta / "copy-instagram.txt"
    if not copy.is_file():
        return ""
    blocos = re.split(r"={10,}", copy.read_text(encoding="utf-8"))
    return " ".join(b for i, b in enumerate(blocos)
                    if i and "LEGENDA" in blocos[i - 1])


def texto_da_peca(pasta: Path) -> str:
    """O que uma peça ESCREVEU: a copy dos slides e a legenda.

    Fora ficam a interface desenhada dentro dos mockups e o texto alternativo,
    que descrevem prova. Prova se reusa entre peças de propósito.
    """
    partes = []
    for arquivo in sorted((pasta / "slides").glob("*.html")):
        leitor = SomenteTexto(sem_desenho=True)
        leitor.feed(arquivo.read_text(encoding="utf-8"))
        partes.append(leitor.texto())
    partes.append(copy_da_peca(pasta))
    return " ".join(partes)


def conferir_vizinhos(pasta: Path, janela: int) -> int:
    """Avisa quando a peça repete frase de outro carrossel já publicado.

    Prova se reusa entre peças — a tela de cadastro do produto é a mesma no
    totem e no tablet, porque o cadastro não muda por canal. **A copy não**: o
    slide reusado fala com um leitor diferente, e repetir o texto entrega duas
    peças que parecem a mesma.

    Isto é AVISO e não erro de propósito. Duas peças da mesma família podem
    precisar dizer o mesmo rótulo de tela em sequência, e travar a entrega por
    isso ensinaria a contornar o conferidor. Quem lê decide caso a caso — mas
    agora precisa decidir, em vez de não ficar sabendo.
    """
    minhas = sequencias(palavras(texto_da_peca(pasta)), janela)
    if not minhas:
        return 0

    achados = 0
    for outra in sorted(pasta.parent.iterdir()):
        if outra == pasta or not (outra / "slides").is_dir():
            continue
        repetidas = minhas & sequencias(palavras(texto_da_peca(outra)), janela)
        for seq in sorted(repetidas):
            print(f"REPETIDO de {outra.name}: {' '.join(seq)}")
            achados += 1
    return achados


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("slug", help="pasta em carrosseis/")
    p.add_argument("--novidade",
                   help="slug da novidade no feed, quando difere do da pasta")
    p.add_argument("--fonte", action="append",
                   help="URL da página de origem, quando a pauta não é o feed "
                        "(gênero função do sistema), ou caminho de manual no "
                        "repositório; pode repetir")
    p.add_argument("--janela", type=int, default=6,
                   help="tamanho da sequência considerada cópia (padrão 6)")
    args = p.parse_args()

    pasta = RAIZ / "carrosseis" / args.slug / "slides"
    if not pasta.is_dir():
        sys.exit(f"ERRO: não achei {pasta}")

    # Peça de função não tem release: a fonte é a página do site, que é copy
    # pronta e por isso ainda mais fácil de recortar sem perceber.
    if args.fonte:
        pedacos, nomes = [], []
        for fonte in args.fonte:
            try:
                if fonte.startswith(("http://", "https://")):
                    pagina = ler_pagina(fonte)
                    pedacos.append(f"{pagina['titulo']} {pagina['texto']}")
                    nomes.append(fonte)
                else:
                    texto, nome = ler_fonte_local(fonte)
                    pedacos.append(texto)
                    nomes.append(nome)
            except Exception as erro:
                sys.exit(f"ERRO ao ler {fonte}: {erro}")
        origem = ", ".join(nomes)
        bruto = " ".join(pedacos)
    else:
        alvo = args.novidade or args.slug
        ficha = next((f for f in fichas(baixar(FEED)) if f["slug"] == alvo), None)
        if ficha is None:
            sys.exit(f"ERRO: nenhuma novidade com slug {alvo} no feed")
        origem = f"novidade {alvo}"
        # O título entra junto: copiar o título da novidade na capa é justamente
        # o erro mais comum, e foi o da primeira versão do destaque-impressao.
        bruto = f"{ficha['titulo']} {ficha['texto']}"

    fonte = sequencias(palavras(bruto), args.janela)

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

    vizinhos = conferir_vizinhos(pasta.parent, args.janela)
    achados += conferir_marcas(pasta.parent)

    if achados:
        print(f"\n{achados} problema(s). COPIADO: reescreva — o slide tem de "
              f"dizer a mesma coisa com as palavras da publicação, não com as "
              f"do release nem com as da página de vendas ({origem}). MARCA DE "
              f"LINHA: apague o prefixo, ele veio da saída de uma ferramenta de "
              f"leitura e não do arquivo.")
        sys.exit(1)

    print(f"OK  nenhuma sequência de {args.janela} palavras repetida de "
          f"{origem} ({conferidos} arquivos)")
    if vizinhos:
        print(f"AVISO  {vizinhos} trecho(s) repetido(s) de outro carrossel — "
              f"veja acima se cada um é prova reusada ou copy que deveria ter "
              f"sido reescrita.")


if __name__ == "__main__":
    main()
