"""Captura as três telas de painel desta peça, recortadas no DOM.

Quatro das seis imagens do carrossel são desenho, porque o resultado de uma API
acontece dentro do sistema do outro. As duas que **são** captura fecham a peça,
e por isso elas têm de ser exatamente o que o leitor vai encontrar no painel
dele:

| Arquivo | De onde | Para que slide |
|---|---|---|
| `rec-estoque-api.png` | *Aplicativos → API Aberta*, a linha **Estoque** do formulário de permissões | 5 |
| `rec-cartoes.png` | *Aplicativos*, os dois cartões — MCP e API Aberta — lado a lado | 6 |

A terceira captura não mora aqui: `rec-autorizacao.png` é a linha de Estoque na
tela *Conectar com BeeFood*, e essa tela só existe **dentro** do fluxo de
autorização do MCP. Não há rota no painel que a abra, então ela é capturada no
meio do caminho, pelo `--retrato` do `consultar-estoque.py`. É a técnica que a
#13 inventou — e aqui ela serve para fotografar justamente a linha que a #13
teve de deixar de fora, porque na época dizia *Em breve*.

**Todo recorte é medido no DOM e é faixa contínua.** Nenhuma montagem: duas
partes distantes da mesma tela coladas passariam por uma tela só, que é o que
não são.

**O que não pode encostar na imagem:** o Client ID e o campo do Client Secret.
A folha abre com *Credencial principal*, e credencial de loja em produção não é
credencial de sandbox descartável — o repositório é público. O recorte da linha
de Estoque começa muito abaixo disso, e o script **confere** que nenhum `code`
da página caiu dentro do quadro antes de salvar.

Uso:
    python carrosseis/16-api-estoque/capturar-telas.py
    python carrosseis/16-api-estoque/capturar-telas.py --so cartoes
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.append(".cursor/skills/carrossel/scripts")
from capturar import esperar, limpar, sessao  # noqa: E402

AQUI = Path(__file__).resolve().parent
PURAS = AQUI / "imagens-puras"
APLICATIVOS = "https://beefood.app/aplicativos"
FOLGA = 10


def caixa_de(alvo, folga: int = FOLGA) -> dict:
    """Mede o elemento **depois** de trazê-lo para dentro da janela.

    `clip` que passa da borda do viewport corta calado: o Playwright devolve a
    imagem do tamanho que coube e não reclama. É a armadilha que a #14
    documentou, e aqui ela mordeu de novo — a linha de Estoque é a última do
    formulário e nasce a 874 px numa janela de 900, então o recorte saía com
    16 px de altura e metade da palavra. Rolar primeiro resolve, e a conferência
    de tamanho em `main` é a rede embaixo.
    """
    # `block: center` e não o `scroll_into_view_if_needed`: este último para
    # assim que o elemento encosta na janela, e a folga do recorte continua
    # fora dela — a linha de Estoque é a última do formulário e saía sem os
    # 10 px de baixo. Centralizado, sobra espaço dos dois lados.
    alvo.evaluate("el => el.scrollIntoView({block: 'center', inline: 'center'})")
    alvo.page.wait_for_timeout(700)
    caixa = alvo.bounding_box()
    if not caixa:
        raise SystemExit("ERRO: o elemento não tem caixa — a tela carregou?")
    return {"x": caixa["x"] - folga, "y": caixa["y"] - folga,
            "width": caixa["width"] + folga * 2,
            "height": caixa["height"] + folga * 2}


def sem_credencial(pagina, quadro: dict) -> None:
    """Aborta se algum `code` da página cair dentro do recorte.

    Os dois `code` da folha são o Client ID e o Client Secret mascarado. Esta
    é a guarda que a #14 pediu em prosa e que aqui é executada: o repositório é
    público, e a imagem **pura** também é versionada.
    """
    for marca in pagina.locator("code").all():
        c = marca.bounding_box()
        if not c:
            continue
        cruza = (c["x"] < quadro["x"] + quadro["width"]
                 and c["x"] + c["width"] > quadro["x"]
                 and c["y"] < quadro["y"] + quadro["height"]
                 and c["y"] + c["height"] > quadro["y"])
        if cruza:
            raise SystemExit("ERRO: a credencial cairia dentro do recorte")


def abrir_api_aberta(pagina) -> None:
    pagina.goto(APLICATIVOS, wait_until="domcontentloaded", timeout=90000)
    esperar(pagina)
    limpar(pagina)
    pagina.get_by_text("Integre seu sistema ao BeeFood via API REST",
                       exact=False).first.click()
    pagina.wait_for_timeout(9000)
    esperar(pagina)


def estoque_api(pagina) -> dict:
    """A linha Estoque do formulário de permissões da credencial.

    O quadro sobe do rótulo *Estoque* até a moldura que embrulha a linha — é o
    cartão arredondado que o formulário dá a cada área, com a descrição embaixo
    do nome e as duas chaves à direita. Ele basta sozinho: *Consultar* e
    *Alterar* vêm escritos ao lado de cada chave, então esta captura não
    precisa de cabeçalho de coluna.
    """
    abrir_api_aberta(pagina)
    linha = pagina.get_by_text("Insumos, categorias, itens e movimentações",
                               exact=True).first.locator(
        "xpath=ancestor::div[contains(@class,'rounded-2xl')][1]")
    # Folga de 4, e não os 10 de sempre: o formulário separa os cartões por
    # 8 px, então 10 de folga trazem uma fatia do cartão de cima e outra do de
    # baixo. Na arte elas leem como elemento cortado, não como recorte. A folga
    # de um recorte de cartão é metade do respiro entre eles, no máximo.
    quadro = caixa_de(linha, 4)
    sem_credencial(pagina, quadro)
    destino = PURAS / "rec-estoque-api.png"
    pagina.screenshot(path=str(destino), clip=quadro)
    return {"arquivo": destino.name, "quadro": quadro,
            "texto": linha.inner_text().replace("\n", " · ")}


def cartoes(pagina) -> dict:
    """A seção *API e MCP* da grade de Aplicativos, inteira.

    O painel agrupa os aplicativos por assunto, e os dois cartões desta peça
    moram na mesma seção, lado a lado, debaixo do rótulo **API e MCP**. O
    recorte é o bloco da seção — um elemento só, então a faixa é contínua por
    construção — e por isso ele traz o rótulo junto: o CTA manda abrir uma das
    duas portas, e o leitor encontra as duas sob aquele título.

    A grade é de três colunas e a seção só tem dois cartões, então o terço da
    direita vem vazio. O quadro fecha no pé do cartão mais baixo e o slide
    corta a sobra de largura — ver o roteiro.
    """
    pagina.goto(APLICATIVOS, wait_until="domcontentloaded", timeout=90000)
    esperar(pagina)
    limpar(pagina)

    secao = pagina.locator('*:text-is("API e MCP")').last.locator("xpath=..")
    cartao = pagina.locator('*:text-is("API Aberta")').last.locator(
        "xpath=ancestor::div[contains(@class,'rounded-lg')][1]")
    bloco, direito = caixa_de(secao), cartao.bounding_box()
    # A seção ocupa as três colunas da grade e o terceiro terço está vazio: o
    # quadro para no fim do segundo cartão, senão a arte leva 320 px de nada.
    largura = (direito["x"] - bloco["x"]) + direito["width"] * 2 + 12 + FOLGA
    quadro = {**bloco, "width": min(bloco["width"], largura)}
    sem_credencial(pagina, quadro)
    destino = PURAS / "rec-cartoes.png"
    pagina.screenshot(path=str(destino), clip=quadro)
    return {"arquivo": destino.name, "quadro": quadro,
            "texto": secao.inner_text().replace("\n", " · ")}


def meu_estoque(pagina, aba: str, arquivo: str, largura: int,
                pilula: str | None = None, busca: str | None = None,
                realcar: str | None = None, com_pilulas: bool = True) -> dict:
    """Uma linha de **Meu Estoque** com as pílulas de situação em cima.

    É a metade do painel das duas provas pareadas — o que a #13 chama de "o que
    o painel mostra" —, e o quadro é escolhido pelo que a conversa afirma:

    - as **pílulas** (`Regular`, `Baixo`, `Crítico`) são o placar da aba, e é o
      que prova "é o único abaixo do mínimo" sem precisar listar os outros;
    - a **linha** traz mínimo, saldo e situação, que são as três coisas que a
      resposta desenhada diz.

    A janela é **estreita**, e não os 1440 de sempre. A tabela acompanha a
    largura da janela: a 1440 ela sai com 1190 px de CSS e, posta nos 904 px da
    faixa do slide, ENCOLHE para 0,76× — letra de 14 px chega ao feed com 10. É
    a lição da #14 sobre portal que reflui, agora dentro do nosso próprio
    painel. Cada aba pede a sua largura, porque o número de colunas muda:

    | Aba | Janela | Tabela | Escala a 904 |
    |---|---|---|---|
    | Insumos (9 colunas) | 1120 | 870 | 1,04× |
    | Produtos (11 colunas) | 1140 | 901 | 1,00× |

    As duas escalas são vizinhas de propósito: as duas capturas aparecem em
    slides seguidos, e letra que muda de tamanho de uma página para a outra lê
    como descuido.

    A data fica de fora de propósito. A tela de *Movimentações* seria uma prova
    melhor — ela tem o antes e o depois do saldo na mesma célula —, mas traz uma
    coluna **Data** no meio, e data na arte faz o post nascer velho.
    """
    pagina.set_viewport_size({"width": largura, "height": 900})
    pagina.goto("https://beefood.app/estoque",
                wait_until="domcontentloaded", timeout=90000)
    esperar(pagina)
    limpar(pagina)

    pagina.get_by_text(aba, exact=True).first.click()
    pagina.wait_for_timeout(4000)
    esperar(pagina)
    limpar(pagina)

    if pilula:
        pagina.locator(f'button:has-text("{pilula}")').first.click()
        pagina.wait_for_timeout(4000)
        esperar(pagina)
    if busca:
        pagina.get_by_placeholder("Buscar por produto ou setor...").first.fill(busca)
        pagina.wait_for_timeout(4000)
        esperar(pagina)

    linhas = pagina.locator("tbody tr")
    if linhas.count() != 1:
        raise SystemExit(
            f"ERRO: a tela mostrou {linhas.count()} linhas e o recorte pede 1. "
            "Item que não aparece sozinho não serve de prova.")
    linha = linhas.first

    # O quadro é uma faixa contínua entre o topo escolhido e o pé da linha. A
    # tabela começa 16 px à esquerda das pílulas, então o x e a largura saem
    # dela: alinhar pelas pílulas deixaria a moldura da tabela cortada.
    #
    # As pílulas entram só onde elas PROVAM alguma coisa. Na consulta, *Baixo 1*
    # é o que sustenta "é o único abaixo do mínimo". Na escrita, a tela está
    # filtrada por busca e as pílulas passam a contar só a linha achada — todas
    # dizem 1, e um *Regular 1* na página seguinte a um *Regular 10* lê como
    # contradição. Onde a pílula não prova, ela sai.
    fileira = caixa_de(pagina.locator('button:has-text("Regular")').first.locator(
        "xpath=.."), FOLGA)
    tabela = pagina.locator("thead tr").first.bounding_box()
    if not com_pilulas:
        fileira = {**fileira, "y": tabela["y"] - FOLGA}
    # Tabela mais larga que a janela quer dizer que o painel pôs uma barra de
    # rolagem horizontal, e o recorte cortaria a última coluna. Quem resolve é
    # a janela, não o recorte: cada aba tem um número de colunas.
    if tabela["x"] + tabela["width"] > largura:
        raise SystemExit(
            f"ERRO: a tabela de {aba} pede {round(tabela['x'] + tabela['width'])} px "
            f"e a janela tem {largura} — alargue a janela desta aba")
    pe = linha.bounding_box()
    quadro = {"x": tabela["x"] - 1, "y": fileira["y"], "width": tabela["width"] + 2,
              "height": pe["y"] + pe["height"] + FOLGA - fileira["y"]}

    destino = PURAS / arquivo
    pagina.screenshot(path=str(destino), clip=quadro)

    medida: dict = {"arquivo": destino.name, "quadro": quadro,
                    "pilulas": fileira_de_pilulas(pagina),
                    "texto": linha.inner_text().replace("\n", " · ")}

    # O anel vermelho não é estimado na miniatura: a caixa da célula é medida
    # dentro do quadro e vira porcentagem, que é o que o slide sabe aplicar. A
    # célula é achada pelo NOME DA COLUNA, e não pelo valor que está nela: o
    # saldo mora dentro de um `input`, e texto de `input` não é texto do DOM.
    if realcar:
        colunas = [c.inner_text().strip() for c in
                   pagina.locator("thead tr th").all()]
        if realcar not in colunas:
            raise SystemExit(f"ERRO: não há coluna {realcar} — achei {colunas}")
        celula = linha.locator("td").nth(colunas.index(realcar)).bounding_box()
        medida["realce"] = {
            "x": round((celula["x"] - 10 - quadro["x"]) / quadro["width"] * 100, 1),
            "y": round((celula["y"] - 8 - quadro["y"]) / quadro["height"] * 100, 1),
            "width": round((celula["width"] + 20) / quadro["width"] * 100, 1),
            "height": round((celula["height"] + 16) / quadro["height"] * 100, 1),
        }
    return medida


def fileira_de_pilulas(pagina) -> str:
    return " · ".join(b.inner_text().replace("\n", " ") for b in
                      pagina.locator('button:has-text("Regular"), '
                                     'button:has-text("Baixo"), '
                                     'button:has-text("Crítico")').all())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--so", choices=["estoque", "cartoes", "baixo", "entrada"],
                    help="captura só uma das telas")
    args = ap.parse_args()

    PURAS.mkdir(parents=True, exist_ok=True)
    medidas = {}
    with sessao("painel") as pagina:
        pagina.emulate_media(reduced_motion="reduce")
        if args.so == "baixo":
            medidas["insumoAbaixoDoMinimo"] = meu_estoque(
                pagina, "Insumos", "rec-insumo-baixo.png", 1120,
                pilula="Baixo", realcar="Estoque Atual")
        elif args.so == "entrada":
            medidas["produtoDepoisDaEntrada"] = meu_estoque(
                pagina, "Produtos", "rec-produto-entrada.png", 1140,
                busca="Sprite Original 350ml", realcar="Estoque Atual",
                com_pilulas=False)
        if args.so in (None, "cartoes"):
            medidas["cartoes"] = cartoes(pagina)
        if args.so in (None, "estoque"):
            medidas["estoqueNaApiAberta"] = estoque_api(pagina)

    # A rede embaixo da armadilha do `clip`: a janela tem DPR 2, então o PNG
    # precisa sair com o dobro do quadro pedido. Saindo menor, o recorte passou
    # da borda e a imagem está cortada — e isso não levanta erro sozinho.
    from PIL import Image
    for chave, dados in medidas.items():
        with Image.open(PURAS / dados["arquivo"]) as img:
            dados["tamanho"] = [img.width, img.height]
        esperado = [round(dados["quadro"]["width"] * 2),
                    round(dados["quadro"]["height"] * 2)]
        # 2 px de tolerância: a caixa do DOM vem fracionária e o arredondamento
        # do Playwright não é o do `round`. Corte de verdade erra por dezenas.
        if any(abs(a - b) > 2 for a, b in zip(dados["tamanho"], esperado)):
            raise SystemExit(
                f"ERRO: {dados['arquivo']} saiu {dados['tamanho']} e o quadro "
                f"pedia {esperado} — o recorte passou da janela")
        print(f"OK  {dados['arquivo']}  {dados['tamanho'][0]}x{dados['tamanho'][1]}")

    arquivo = AQUI / "medidas.json"
    antigo = json.loads(arquivo.read_text()) if arquivo.is_file() else {}
    arquivo.write_text(json.dumps({**antigo, **medidas}, indent=2,
                                  ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
