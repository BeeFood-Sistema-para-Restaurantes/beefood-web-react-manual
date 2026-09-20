#!/usr/bin/env python3
"""Lê a pauta dos carrosséis direto das Novidades do BeeFood.

A página `beefood.app/novidades` é um SPA, mas publica um RSS em
`/novidades/feed.xml` com **tudo em texto puro**: título, data, tipo
(Novidade / Melhoria), áreas e o corpo inteiro do anúncio. Ou seja: não há
motivo para raspar HTML nem para dirigir navegador só para saber o que sair.

Este script também aponta o **manual correspondente**, quando existe. É a
costura com a skill de manual: a novidade dá o gancho e a data, o manual dá o
passo a passo conferido no sistema. Nada aqui escreve em `manuais/`.

O outro gênero de pauta é a **função do sistema**, e ela não tem feed: mora numa
página de `beefood.com.br` (um segmento, um módulo, um tema). `--pagina` lê essa
página e devolve os blocos, a lista de funcionalidades e o FAQ — mais duas
colunas que existem só aqui: qual **manual** sustenta cada eixo (e quais não
têm nenhum, que é onde a tela vai ter de ser capturada ou desenhada) e quais
frases da página são **claim institucional**, que não vira slide.

Uso:
    python pauta.py                              # as 15 novidades mais recentes
    python pauta.py --limite 40 --tipo Novidade
    python pauta.py --buscar cupom
    python pauta.py --slug destaque-impressao    # material bruto de um item
    python pauta.py --slug destaque-impressao --json
    python pauta.py --pagina https://beefood.com.br/sistema-dark-kitchen/
    python pauta.py --pagina <url> --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
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


def mesma_raiz(a: str, b: str) -> bool:
    """`entregadores` e `entregador` são a mesma palavra para esta busca.

    A comparação exata deixou passar o manual do Painel para Entregadores: o
    release diz "Entregadores" e a pasta se chama `painel-entregador`, então só
    `painel` casava e a nota ficava em 1, abaixo do corte. Prefixo de 5 letras
    resolve plural e flexão sem abrir a porta para qualquer coisa.
    """
    return a == b or (len(min(a, b, key=len)) >= 5
                      and (a.startswith(b) or b.startswith(a)))


def notas_dos_manuais(titulo: str) -> list[tuple[int, Path]]:
    """Quantas palavras cada pasta de manual tem em comum com o título."""
    alvo = {p for p in normalizar(titulo).replace("-", " ").split()
            if len(p) > 3 and p not in VAZIAS}
    if not alvo:
        return []

    notas = []
    for pasta in sorted(p for p in MANUAIS.iterdir() if p.is_dir()):
        palavras = [p for p in normalizar(pasta.name).split("-") if len(p) > 3]
        nota = sum(1 for a in alvo if any(mesma_raiz(a, p) for p in palavras))
        if nota:
            notas.append((nota, pasta))
    return sorted(notas, key=lambda x: (-x[0], x[1].name))


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

    notas = notas_dos_manuais(ficha["titulo"])
    return notas[0][1] if notas and notas[0][0] >= 2 else None


# --- pauta de função: uma página do site -------------------------------------
#
# Página de segmento é WordPress com Elementor: o mesmo texto costuma sair duas
# vezes (variante de desktop e de celular) e vem embalado em dezenas de divs.
# Não há por que dirigir navegador: o que interessa é a hierarquia de títulos e
# o texto solto embaixo de cada um, e isso o parser da biblioteca-padrão lê.
#
# Só que parte das páginas do site **não está no WordPress**. O endereço público
# devolve uma casca — um `<div class="super-loader">` com "Carregando…" — e o
# conteúdo é montado por um app externo. Quem lê só o HTML de `beefood.com.br`
# conclui que a página está vazia, e foi exatamente o que aconteceu na pauta do
# totem: o carrossel inteiro foi escrito sem os fatos da página, que tinha
# seção de fidelidade, demonstração do aparelho e FAQ.
#
# O endereço do app está no próprio HTML da casca. O app entrega HTML pronto
# (pré-renderizado), então continua não sendo preciso navegador — só é preciso
# **perceber a casca e seguir o endereço**.
CASCA = re.compile(r"super-loader|Carregando…|Carregando\.\.\.")
APP_EXTERNO = re.compile(r"https://[a-z0-9.-]+\.lovable\.app(?:/[a-z0-9\-/]*)?", re.I)

IGNORAR = {"script", "style", "noscript", "svg", "path", "template", "head"}
TITULOS = {"h1", "h2", "h3", "h4", "h5", "h6"}
# `a` e `span` são os dois casos duplos do WordPress: sozinhos, são item de menu
# e rótulo de ícone; dentro de um parágrafo, são o parágrafo inteiro, porque o
# editor embrulha o texto em `<span style="font-weight: 400">`. Por isso eles
# contam como bloco só quando não há bloco aberto — ver `LeitorPagina`.
BLOCOS = {"p", "li", "figcaption", "blockquote", "summary"}
INLINE = {"a", "span"}
TEXTOS = BLOCOS | INLINE
PONTUACAO = re.compile(r"[.,;:?!]")

# Frase que vende a empresa, não o produto: ela pauta, mas não vira slide.
INSTITUCIONAL = re.compile(
    r"(\+?\s*\d[\d\.\s]*\s*(mil|milh[oõ]es)"          # +100 mil negócios
    r"|melhor(es)?\s+(avalia|suporte|sistema)"         # melhor avaliação/suporte
    r"|avalia[cç][aã]o\s+no\s+google"
    r"|l[ií]der\s+(de|do|em)"
    r"|n[ºo°]\s*1\b"
    r"|sem\s+custos?\b)", re.I)


class LeitorPagina(HTMLParser):
    """Devolve a página como uma lista de (tag, texto), na ordem em que aparece."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocos: list[tuple[str, str]] = []
        self._pilha: list[str] = []
        self._buf: list[str] = []
        self._pulando = 0

    def handle_starttag(self, tag, attrs):
        if tag in IGNORAR:
            self._pulando += 1
        elif tag in TITULOS or tag in BLOCOS:
            self._fechar()
            self._pilha.append(tag)
        elif tag in INLINE:
            # Dentro de um bloco, o inline é parte do texto dele; fechar aqui
            # jogaria fora o parágrafo, que é como o Elementor escreve todos.
            if not self._pilha:
                self._pilha.append(tag)
        elif tag == "br":
            self._buf.append(" ")

    def handle_endtag(self, tag):
        if tag in IGNORAR:
            self._pulando = max(0, self._pulando - 1)
        elif tag in TITULOS or tag in BLOCOS:
            self._fechar()
        elif tag in INLINE and self._pilha and self._pilha[-1] == tag:
            self._fechar()

    def handle_data(self, dado):
        if not self._pulando and self._pilha:
            self._buf.append(dado)

    def _fechar(self) -> None:
        if self._pilha:
            texto = re.sub(r"\s+", " ", "".join(self._buf)).strip()
            if texto:
                self.blocos.append((self._pilha[-1], texto))
            self._pilha.pop()
        self._buf = []

    def close(self):
        while self._pilha:
            self._fechar()
        super().close()


def fonte_real(html: str) -> str | None:
    """De onde o conteúdo vem, quando o endereço público é só uma casca.

    Devolve `None` quando a página se serve sozinha, que é o caso comum.
    """
    if not CASCA.search(html):
        return None
    achados = {u.rstrip("/") for u in APP_EXTERNO.findall(html)}
    com_caminho = [u for u in achados if urllib.parse.urlparse(u).path.strip("/")]
    if not com_caminho:
        return None
    # A casca cita a raiz do app e a rota da página; a rota é a mais comprida.
    return max(com_caminho, key=len)


def ler_pagina(url: str) -> dict:
    bruto = baixar(url).decode("utf-8", "replace")
    origem = url
    real = fonte_real(bruto)
    if real:
        bruto = baixar(real).decode("utf-8", "replace")
        origem = real

    leitor = LeitorPagina()
    leitor.feed(bruto)
    leitor.close()

    # Elementor repete o mesmo texto em variantes de layout: a segunda cópia não
    # acrescenta pauta nenhuma.
    vistos, limpos = set(), []
    for tag, texto in leitor.blocos:
        chave = normalizar(texto)
        if len(texto) < 3 or chave in vistos:
            continue
        # Link e span só interessam quando são pergunta: no acordeão de FAQ o
        # título da aba é um `<span>` (ou um `<a>`, dependendo do widget). O
        # resto é menu, botão e rótulo de ícone.
        if tag in ("a", "span") and not texto.endswith("?"):
            continue
        # Menu de cabeçalho e rodapé chega como uma linha só: vários nomes de
        # produto em sequência, sem pontuação nenhuma ("Soluções Presencial
        # Cardápio Digital QRCode Aplicativo para Garçom …"). Frase de verdade
        # com esse tamanho tem ponto, vírgula ou dois-pontos.
        if tag not in TITULOS and len(texto.split()) > 11 and not PONTUACAO.search(texto):
            continue
        vistos.add(chave)
        limpos.append((tag, texto))

    secoes: list[dict] = []
    faq: list[str] = []
    claims: list[str] = []
    atual = {"titulo": "(abertura)", "nivel": "h0", "linhas": []}
    for tag, texto in limpos:
        if INSTITUCIONAL.search(texto) and len(texto) < 120:
            claims.append(texto)
            continue
        if tag in TITULOS:
            if atual["linhas"] or atual["titulo"] != "(abertura)":
                secoes.append(atual)
            atual = {"titulo": texto, "nivel": tag, "linhas": []}
        else:
            if texto.endswith("?"):
                faq.append(texto)
            atual["linhas"].append(texto)
    secoes.append(atual)

    titulo = next((t for tag, t in limpos if tag == "h1"), "")
    return {
        "url": url,
        "servida_por": origem if origem != url else None,
        "titulo": titulo or (secoes[1]["titulo"] if len(secoes) > 1 else url),
        # Título sem corpo continua sendo pauta: "Para quem é o Cardápio no
        # Tablet" não tem parágrafo nenhum embaixo e é um eixo da página.
        "secoes": [s for s in secoes if s["linhas"] or s["nivel"] in ("h1", "h2", "h3")],
        "faq": faq,
        "claims": claims,
        "texto": " ".join(t for _, t in limpos),
    }


def manual_por_termos(texto: str) -> Path | None:
    """Mesma costura do `manual_de`, mas a partir de um pedaço de texto solto."""
    if not MANUAIS.is_dir():
        return None
    alvo = {p for p in normalizar(texto).replace("-", " ").split()
            if len(p) > 3 and p not in VAZIAS}
    melhor, nota_melhor = None, 0
    for pasta in sorted(p for p in MANUAIS.iterdir() if p.is_dir()):
        palavras = {p for p in normalizar(pasta.name).split("-") if len(p) > 3}
        nota = len(alvo & palavras)
        if nota > nota_melhor:
            melhor, nota_melhor = pasta, nota
    return melhor if nota_melhor >= 2 else None


def imprimir_pagina(ficha: dict) -> None:
    print(f"# {ficha['titulo']}\n")
    print(f"- Gênero: função do sistema (a capa NÃO leva pílula Novidade)")
    print(f"- Fonte: {ficha['url']}")
    if ficha.get("servida_por"):
        print(f"- O endereço público é uma casca; o conteúdo veio de {ficha['servida_por']}")
    print("- A página é pauta, não fato: o que o slide afirma sai do manual ou da tela\n")

    print("## Blocos da página\n")
    for s in ficha["secoes"]:
        if s["titulo"] == "(abertura)" and not s["linhas"]:
            continue
        manual = manual_por_termos(s["titulo"] + " " + " ".join(s["linhas"][:3]))
        marca = f"manual: {manual.name}" if manual else "SEM manual — captura ou desenho"
        print(f"### {s['titulo']}  [{marca}]")
        for linha in s["linhas"][:6]:
            print(f"    - {linha}")
        print()

    if ficha["faq"]:
        print("## Perguntas da própria página (bom banco de ângulo)\n")
        for p in ficha["faq"]:
            print(f"- {p}")
        print()

    if ficha["claims"]:
        print("## NÃO vira slide (claim institucional)\n")
        for c in ficha["claims"]:
            print(f"- {c}")
        print()


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
        # "Nenhum" é um palpite, e um palpite que já errou: o casamento é por
        # nome de pasta, e um manual pode existir chamado de outro jeito. Então
        # o script mostra em quem ele quase acreditou, para a conferência
        # custar um `ls` em vez de uma peça inteira capturada do zero.
        print("- Manual relacionado: não achei pelo nome — confira à mão antes"
              " de capturar do zero")
        quase = notas_dos_manuais(ficha["titulo"])[:3]
        if quase:
            print("  Pastas mais próximas: "
                  + ", ".join(f"`manuais/{p.name}/`" for _, p in quase))
    print(f"\n## Texto publicado\n\n{ficha['texto']}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slug", help="detalha um item e aponta o manual relacionado")
    ap.add_argument("--tipo", help="filtra por tipo (Novidade, Melhoria)")
    ap.add_argument("--buscar", help="filtra por termo no título ou no texto")
    ap.add_argument("--limite", type=int, default=15)
    ap.add_argument("--pagina", help="pauta de função: uma página de beefood.com.br")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.pagina:
        try:
            ficha = ler_pagina(args.pagina)
        except Exception as erro:
            sys.exit(f"ERRO ao ler {args.pagina}: {erro}")
        if args.json:
            print(json.dumps(ficha, ensure_ascii=False, indent=2))
        else:
            imprimir_pagina(ficha)
        return 0

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
