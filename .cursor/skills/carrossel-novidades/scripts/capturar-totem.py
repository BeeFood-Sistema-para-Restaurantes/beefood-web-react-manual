#!/usr/bin/env python3
"""Fotografa as telas do Totem de Autoatendimento, com o cardápio traduzido.

    python capturar-totem.py --saida carrosseis/<slug>/imagens-puras \
        --conteudo carrosseis/<slug>/traducoes.json

Por que não é `capturar.py --rota`: o totem é outro aplicativo
(`totem.beefood.app`), abre por token de filial e não tem login. O padrão é o
totem de exemplo da ONE Stand (`empresaID=350&filialID=380`), que tem cardápio
de verdade — hambúrguer, combo, sobremesa — e é o que serve de cenário.

**Nenhum pedido é finalizado.** O roteiro abre a tela inicial, entra no
cardápio, troca de idioma e abre um produto. Nada é enviado para a cozinha.

## O truque, e por que ele é honesto

A loja de exemplo **não tem tradução cadastrada**: a API devolve `aaTraducao:
null` na configuração da filial e `traducao: null` em cada setor e produto. Sem
isso o aplicativo esconde o seletor de idioma — é a própria regra do produto.

Então o script **intercepta a resposta da API** e injeta:

- `aaTraducao: true` na filial, que é a chave que faz o seletor aparecer;
- o campo `traducao` de cada setor e produto, no formato que o aplicativo lê:
  `{"en": {...}, "es": {...}}` como string JSON.

O texto vem do `--conteudo`, escrito à mão para o carrossel. Não é tradução
automática nem cópia do exemplo do manual.

A mesma interceptação troca **a arte de fundo** do totem (tela de espera e faixa
do cardápio) pelas imagens de `--fundos` (o `preparar-fundo.py` as monta). A loja
de exemplo anuncia um pudim ali, e num carrossel sobre tradução o olho lê o preço
do pudim em vez do cardápio em inglês.

O que sai daqui é print do aplicativo de produção: layout, fotos de produto,
tipografia, cores e o seletor de idioma são os do totem. Nosso é o conteúdo
traduzido — exatamente o que o lojista vai cadastrar — e a foto de fundo.

## Onde cada arquivo cai

| Vai para | O que é |
|---|---|
| `--saida` | prova daquele carrossel: cardápio nos idiomas, produto aberto, recorte de cartão |
| `--biblioteca` | o que serve para o próximo: fotos de produto, banner, tela de espera |

A biblioteca é `assets/fotos/` da skill, e os slides a alcançam por
`src="skill:fotos/<arquivo>.png"`. Capturando de **outra** loja, aponte
`--biblioteca` para outro lugar: os nomes são genéricos e sobrescrevem.

## O arquivo de conteúdo

```json
{
  "setores":  {"Combos Burger": {"en": "Burger Combos", "es": "..."}},
  "grupos":   {"Escolha o molho": {"en": "Choose your sauce", "es": "..."}},
  "produtos": {"BATATA FRITA": {"en": {"descricao": "FRENCH FRIES",
                                       "descritivo": "..."}, "es": {...}}},
  "fotos":    {"BATATA FRITA": "foto-batata.png"}
}
```

`fotos` é opcional: nome do produto no sistema → arquivo na biblioteca. Só baixa
o que está listado; a loja tem quase cem produtos e o resto não interessa.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
BIBLIOTECA = SKILL / "assets" / "fotos"
FUNDOS = SKILL / "assets" / "fundos"

TOTEM = ("https://totem.beefood.app/?empresaID=350&filialID=380"
         "&token=669461A4-1729-4E31-9BD2-8446993BBE7C")

# A loja de exemplo anuncia um pudim na tela de espera e na faixa do cardápio, e
# isso rouba a imagem. Endereço de mentira: nada sai para a internet, a rota
# `servir_fundo` responde com o arquivo da pasta `--fundos`.
FUNDO_BASE = "https://carrossel.beefood.local/"
ARTES = {"AASLIDE": "-espera.png", "AACAPA": "-banner.png"}

# O aparelho do catálogo é retrato. 1080x1920 é a tela dele, e é a proporção que
# a moldura `.totem__tela` do slide espera (9/16) — print entra sem recorte.
TELA = {"width": 1080, "height": 1920}

# A mesma tela de espera, capturada num totem de 720p. O aplicativo desenha o
# botão e as bandeiras em px fixo, então numa tela menor eles ocupam **mais**
# proporção: a pílula das bandeiras sai 1,5x maior em relação à imagem. É a
# versão que entra na capa, onde o aparelho aparece com 380 px de largura e a
# pílula de 1080p viraria um pontinho. A proporção é a mesma (9/16).
TELA_MENOR = {"width": 720, "height": 1280}

# O botão de começar pulsa para sempre, e o Playwright espera estabilidade até
# estourar o tempo. Todo clique aqui vai com force=True pelo mesmo motivo.
ESPERA_CARGA = 6000

# O seletor não abre modal: são três botões de bandeira lado a lado, e o
# aplicativo identifica cada um pelo `aria-label`. Clicar troca o idioma da tela
# inteira na hora, que é o gesto que o cliente faz no aparelho.
IDIOMAS = {
    "pt-BR": "Português (Brasil)",
    "en-US": "English (United States)",
    "es-ES": "Español (España)",
}


def anotar(item: dict, verbetes: dict, faltando: set[str], rotulo: str) -> None:
    """Escreve o campo `traducao` do item, se houver verbete para o nome dele."""
    nome = item.get("descricao")
    verbete = verbetes.get(nome)
    if verbete:
        item["traducao"] = json.dumps(verbete, ensure_ascii=False)
    elif nome:
        faltando.add(f"{rotulo}: {nome}")


def montar_rotas(contexto, conteudo: dict, fundos: Path | None,
                 nome_fundo: str) -> tuple[set[str], dict[str, str]]:
    """Liga a interceptação das respostas que o totem usa para montar a tela.

    Devolve o que só dá para saber depois de a resposta passar: os nomes sem
    verbete de tradução e o catálogo de fotos (nome do produto → URL da imagem).
    """
    setores = conteudo.get("setores", {})
    grupos = conteudo.get("grupos", {})
    produtos = conteudo.get("produtos", {})
    faltando: set[str] = set()
    catalogo: dict[str, str] = {}

    def filial(rota):
        resposta = rota.fetch()
        dados = resposta.json()
        alvos = dados if isinstance(dados, list) else [dados]
        for item in alvos:
            item["aaTraducao"] = True
        rota.fulfill(response=resposta, json=dados)

    def traduzir_setores(rota):
        resposta = rota.fetch()
        dados = resposta.json()
        for item in dados:
            nome = item.get("setor")
            verbete = setores.get(nome)
            if verbete:
                item["traducao"] = json.dumps(
                    {i: {"setor": t} for i, t in verbete.items()}, ensure_ascii=False)
            elif nome:
                faltando.add(f"setor: {nome}")
        rota.fulfill(response=resposta, json=dados)

    def traduzir_produtos(rota):
        resposta = rota.fetch()
        dados = resposta.json()
        for item in dados:
            anotar(item, produtos, faltando, "produto")
            if item.get("s3Link"):
                catalogo[item["descricao"].strip()] = item["s3Link"]
            # Grupo de complemento tem o mesmo contrato do produto, e é o que faz
            # a tela de montar o combo ficar em inglês inteira. Sem isto, o
            # cabeçalho sai traduzido e a opção embaixo dele fica em português.
            for grupo in item.get("gruposList") or []:
                nome = grupo.get("descricao")
                verbete = grupos.get(nome)
                if verbete:
                    grupo["traducao"] = json.dumps(
                        {i: {"descricao": t} for i, t in verbete.items()},
                        ensure_ascii=False)
                elif nome:
                    faltando.add(f"grupo: {nome}")
                for opcao in grupo.get("opc") or []:
                    anotar(opcao, produtos, faltando, "opção")
        rota.fulfill(response=resposta, json=dados)

    def trocar_fundos(rota):
        """Põe a nossa foto no lugar da arte promocional da loja de exemplo.

        `imagens/slides` é o que passa na tela de espera e `imagens/empresa`
        traz a capa do cardápio (`AACAPA`) e o logotipo da loja (`AALOGO`, que
        continua o dela). O link vira um endereço que não existe e que a rota
        abaixo atende com o arquivo de `--fundos`.
        """
        resposta = rota.fetch()
        dados = resposta.json()
        for item in dados:
            sufixo = ARTES.get(item.get("tipo"))
            if sufixo:
                item["s3Link"] = f"{FUNDO_BASE}{nome_fundo}{sufixo}"
        rota.fulfill(response=resposta, json=dados)

    def servir_fundo(rota):
        arquivo = fundos / rota.request.url.rsplit("/", 1)[-1]
        rota.fulfill(status=200, content_type="image/png", body=arquivo.read_bytes())

    # Rota no **contexto**, e não na página: o totem é PWA, e a foto de fundo é
    # pedida pelo service worker dele. `page.route` não enxerga esse pedido, e
    # a imagem chega quebrada — o contexto é criado com `service_workers`
    # bloqueado (`abrir`) justamente por isso.
    contexto.route("**/api/totem2/filial/**", filial)
    contexto.route("**/api/totem2/setores/**", traduzir_setores)
    contexto.route("**/api/totem2/produtos/**", traduzir_produtos)
    if fundos:
        contexto.route("**/api/totem2/imagens/**", trocar_fundos)
        contexto.route(f"{FUNDO_BASE}**", servir_fundo)
    return faltando, catalogo


def abrir(navegador, tela: dict, escala: int):
    """Contexto do totem, com o service worker desligado.

    Sem `service_workers="block"` o PWA serve as imagens pelo próprio worker, e
    o que a interceptação devolve não chega até a página.
    """
    return navegador.new_context(viewport=tela, device_scale_factor=escala,
                                 locale="pt-BR", service_workers="block")


def escolher_idioma(pagina, idioma: str) -> None:
    pagina.click(f"button[aria-label='{IDIOMAS[idioma]}']", force=True)
    pagina.wait_for_timeout(2500)


def abrir_setor(pagina, indice: int) -> None:
    """Clica o setor na coluna da esquerda, que é como o cliente navega.

    Por posição, e não por nome, porque o nome muda com o idioma — que é
    justamente o que o carrossel está mostrando. Na ONE Stand: 0 Promoções,
    1 Combos Burger, 2 Burgers Avulsos, 3 Sobremesas, 4 Acompanhamentos.

    A coluna é a única fileira de botões colada na borda esquerda; o primeiro
    deles é a marca da loja, sem rótulo, e por isso entra o filtro por texto.
    """
    pagina.evaluate("""(n) => {
      const coluna = [...document.querySelectorAll('button')].filter(b => {
        const r = b.getBoundingClientRect();
        return r.left < 5 && r.width < 300 && r.height > 100
               && (b.innerText || '').trim() !== '';
      });
      coluna[n]?.click();
    }""", indice)
    pagina.wait_for_timeout(3000)


def abrir_produto(pagina, nome: str) -> None:
    """Abre a ficha do produto. `exact` evita cair no combo de mesmo nome."""
    pagina.get_by_text(nome, exact=True).first.click(force=True)
    pagina.wait_for_timeout(3500)


def medir_primeiro_cartao(pagina) -> dict:
    """Caixa do primeiro cartão do setor aberto, para recortar só ele.

    Abrir um setor rola a seção dele para o topo, então a grade que interessa é
    a única `grid` larga encostada na borda de cima. Medir em vez de fixar a
    caixa importa porque o recorte tem de cair **no mesmo lugar** nos idiomas:
    é isso que faz as fotos se lerem como um item só.
    """
    return pagina.evaluate("""() => {
      const grade = [...document.querySelectorAll('div.grid')].find(g => {
        const r = g.getBoundingClientRect();
        return r.width > 500 && r.top > -20 && r.top < 240;
      });
      const r = grade.querySelector('button').getBoundingClientRect();
      return {x: r.x, y: r.y, width: r.width, height: r.height};
    }""")


def baixar_fotos(pagina, catalogo: dict[str, str], fotos: dict[str, str],
                 destino: Path) -> None:
    """Baixa a foto de cada produto listado, pela URL que a própria API serve.

    Vem `.webp` do servidor e sai `.png` aqui, que é o formato que o resto da
    esteira usa. A tela do slide costuma ser desenhada (print inteiro reduzido
    fica com letra de 4 px), mas a foto dentro dela é a mesma do aparelho.
    """
    from io import BytesIO

    from PIL import Image

    for nome, arquivo in fotos.items():
        link = catalogo.get(nome.strip())
        if not link:
            print(f"AVISO: sem foto para {nome}")
            continue
        dados = pagina.request.get(link).body()
        with Image.open(BytesIO(dados)) as im:
            im.convert("RGB").save(destino / arquivo)
        print(f"OK  {destino / arquivo}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--saida", type=Path, required=True,
                    help="pasta imagens-puras do carrossel")
    ap.add_argument("--conteudo", type=Path, required=True,
                    help="JSON com setores, grupos, produtos e fotos")
    ap.add_argument("--url", default=TOTEM)
    ap.add_argument("--setor-cardapio", type=int, default=2,
                    help="setor fotografado nos três idiomas (padrão: 2)")
    ap.add_argument("--setor-cartao", type=int, default=4,
                    help="setor de onde sai o recorte de um cartão (padrão: 4)")
    ap.add_argument("--produto", default="MELTED",
                    help="produto aberto na ficha em inglês")
    ap.add_argument("--cartao", default="cartao",
                    help="prefixo dos recortes de cartão")
    ap.add_argument("--biblioteca", type=Path, default=BIBLIOTECA,
                    help="onde caem fotos de produto, banner e tela de espera")
    ap.add_argument("--fundos", type=Path, default=FUNDOS,
                    help="pasta das artes de fundo; vazio mantém a arte da loja")
    ap.add_argument("--nome-fundo", default="fundo-totem")
    args = ap.parse_args()

    from playwright.sync_api import sync_playwright

    if not args.conteudo.is_file():
        sys.exit(f"ERRO: não achei {args.conteudo}")
    conteudo = json.loads(args.conteudo.read_text(encoding="utf-8"))
    fundos = args.fundos if str(args.fundos) else None
    args.saida.mkdir(parents=True, exist_ok=True)
    args.biblioteca.mkdir(parents=True, exist_ok=True)

    def rotas(contexto):
        return montar_rotas(contexto, conteudo, fundos, args.nome_fundo)

    with sync_playwright() as pw:
        navegador = pw.chromium.launch()
        ctx = abrir(navegador, TELA, 1)
        pagina = ctx.new_page()
        faltando, catalogo = rotas(ctx)
        pagina.goto(args.url, wait_until="networkidle", timeout=120000)
        pagina.wait_for_timeout(ESPERA_CARGA)

        # 1. Tela inicial, agora com o seletor de idioma que a filial liberou.
        salvar(pagina, args.saida / "totem-espera-idioma.png")

        # 2. Cardápio. O setor padrão é o dos hambúrgueres avulsos, e não o de
        #    combo: preço de combo sai como "A partir de R$ 35,90", e esse
        #    "A partir de" é string fixa no aplicativo, que não passa pelo
        #    idioma. Uma frase em português no meio de uma tela em inglês
        #    desmente o slide inteiro, então a foto é de onde o preço é um
        #    número só.
        pagina.click("button:has-text('FAÇA SEU PEDIDO')", force=True)
        pagina.wait_for_timeout(ESPERA_CARGA + 2000)

        # 2b. O banner do topo, sozinho. Ele é a peça mais valiosa da captura:
        #     traz o CANCEL ORDER e a pílula de bandeiras de produção, e é o
        #     que entra dentro da tela desenhada do slide como pixel real.
        escolher_idioma(pagina, "en-US")
        banner = pagina.locator("img[alt='Capa']").first.locator("xpath=..")
        alvo = args.biblioteca / "totem-banner-en.png"
        banner.screenshot(path=str(alvo), type="png")
        print(f"OK  {alvo}")

        # 3. O mesmo setor nos três idiomas. Trocar de idioma volta a rolagem
        #    para o topo, então o setor é reaberto depois de cada troca — é
        #    isso que faz as três fotos servirem de antes e depois.
        for idioma, arquivo in (("pt-BR", "totem-menu-pt.png"),
                                ("en-US", "totem-menu-en.png"),
                                ("es-ES", "totem-menu-es.png")):
            escolher_idioma(pagina, idioma)
            abrir_setor(pagina, args.setor_cardapio)
            salvar(pagina, args.saida / arquivo)

        # 4. Produto aberto em inglês: é onde a descrição e os grupos de
        #    complemento aparecem traduzidos, e é o argumento do carrossel numa
        #    imagem só — o cliente monta o lanche inteiro na língua dele.
        escolher_idioma(pagina, "en-US")
        abrir_setor(pagina, args.setor_cardapio)
        abrir_produto(pagina, args.produto)
        salvar(pagina, args.saida / "totem-produto-en.png")

        # 5. As fotos dos produtos, do jeito que o sistema serve.
        baixar_fotos(pagina, catalogo, conteudo.get("fotos", {}), args.biblioteca)

        # 6. A tela de espera de novo, num totem de 720p, para a capa.
        ctx_menor = abrir(navegador, TELA_MENOR, 2)
        menor = ctx_menor.new_page()
        rotas(ctx_menor)
        menor.goto(args.url, wait_until="networkidle", timeout=120000)
        menor.wait_for_timeout(ESPERA_CARGA)
        salvar(menor, args.biblioteca / "totem-espera-idioma-720.png")

        # E a mesma tela depois de tocar na bandeira dos Estados Unidos: o botão
        # vira START ORDER. É a versão que a capa usa, porque a capa pergunta
        # "seu cardápio já fala inglês?" e essa tela responde sozinha.
        escolher_idioma(menor, "en-US")
        salvar(menor, args.biblioteca / "totem-espera-en-720.png")

        # 7. O mesmo item do cardápio, recortado no cartão, nos três idiomas. É
        #    a prova de que muda o nome e a foto e o preço continuam os mesmos.
        #    Contexto próprio com escala 2 porque o cartão tem 248 px de largura
        #    no aparelho e aparece com 288 na arte — ampliar print de 1x deixa a
        #    letra pastosa.
        ctx_nitido = abrir(navegador, TELA, 2)
        nitido = ctx_nitido.new_page()
        rotas(ctx_nitido)
        nitido.goto(args.url, wait_until="networkidle", timeout=120000)
        nitido.wait_for_timeout(ESPERA_CARGA)
        nitido.click("button:has-text('FAÇA SEU PEDIDO')", force=True)
        nitido.wait_for_timeout(ESPERA_CARGA + 2000)
        for idioma, sufixo in (("pt-BR", "pt"), ("en-US", "en"), ("es-ES", "es")):
            escolher_idioma(nitido, idioma)
            abrir_setor(nitido, args.setor_cartao)
            salvar(nitido, args.saida / f"{args.cartao}-{sufixo}.png",
                   medir_primeiro_cartao(nitido))

        navegador.close()

    if faltando:
        print("AVISO: sem tradução no arquivo de conteúdo:")
        for f in sorted(faltando):
            print("   ", f)


def salvar(pagina, alvo: Path, recorte: dict | None = None) -> None:
    pagina.screenshot(path=str(alvo), type="png", clip=recorte)
    print(f"OK  {alvo}")


if __name__ == "__main__":
    main()
