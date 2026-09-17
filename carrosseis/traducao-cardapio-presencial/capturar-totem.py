#!/usr/bin/env python3
"""Fotografa as telas do Totem de Autoatendimento com o cardápio traduzido.

    python carrosseis/traducao-cardapio-presencial/capturar-totem.py

Por que este script existe, e por que ele não é um `capturar.py --rota`: o totem
é outro aplicativo (`totem.beefood.app`), abre por token de filial e não tem
login. O dono passou o totem de exemplo da ONE Stand
(`empresaID=350&filialID=380`), que tem cardápio de verdade — hambúrguer, combo,
sobremesa — e é o que o carrossel precisa mostrar.

**Nenhum pedido é finalizado.** O roteiro abre a tela inicial, entra no cardápio,
troca de idioma e abre um produto. Nada é enviado para a cozinha.

## O truque, e por que ele é honesto

A ONE Stand **não tem tradução cadastrada**: a API devolve `aaTraducao: null` na
configuração da filial e `traducao: null` em cada setor e produto. Sem isso o
aplicativo esconde o seletor de idioma — é a própria regra do produto.

Então o script **intercepta a resposta da API** e injeta:

- `aaTraducao: true` na filial, que é a chave que faz o seletor aparecer;
- o campo `traducao` de cada setor e produto, no formato que o aplicativo lê:
  `{"en": {...}, "es": {...}}` como string JSON.

O texto em inglês e em espanhol é o do `traducoes.json`, **escrito para este
carrossel**. Não é tradução automática nem cópia do exemplo do manual.

O que sai daqui é print do aplicativo de produção: layout, fotos, tipografia,
cores e o seletor de idioma são os do totem. O que é nosso é o conteúdo do
cardápio traduzido — exatamente o que o lojista vai cadastrar. Por isso estes
prints **não levam selo de ilustração**: a tela é real.

Saída: `imagens-puras/totem-*.png`.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent
PURAS = PASTA / "imagens-puras"
TRADUCOES = PASTA / "traducoes.json"

TOTEM = ("https://totem.beefood.app/?empresaID=350&filialID=380"
         "&token=669461A4-1729-4E31-9BD2-8446993BBE7C")

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


def anotar(item: dict, verbetes: dict, faltando: set[str], rotulo: str) -> None:
    """Escreve o campo `traducao` do item, se houver verbete para o nome dele."""
    nome = item.get("descricao")
    verbete = verbetes.get(nome)
    if verbete:
        item["traducao"] = json.dumps(verbete, ensure_ascii=False)
    elif nome:
        faltando.add(f"{rotulo}: {nome}")


def montar_rotas(pagina, traducoes: dict) -> tuple[set[str], dict[str, str]]:
    """Liga a interceptação das três respostas que o totem usa para montar a tela.

    Devolve o que só dá para saber depois de a resposta passar: os nomes sem
    verbete de tradução e o catálogo de fotos (nome do produto → URL da imagem).
    """
    setores = traducoes["setores"]
    produtos = traducoes["produtos"]
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

    grupos = traducoes["grupos"]

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

    pagina.route("**/api/totem2/filial/**", filial)
    pagina.route("**/api/totem2/setores/**", traduzir_setores)
    pagina.route("**/api/totem2/produtos/**", traduzir_produtos)
    return faltando, catalogo


def main() -> None:
    from playwright.sync_api import sync_playwright

    if not TRADUCOES.is_file():
        sys.exit(f"ERRO: não achei {TRADUCOES}")
    traducoes = json.loads(TRADUCOES.read_text(encoding="utf-8"))
    PURAS.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as pw:
        navegador = pw.chromium.launch()
        ctx = navegador.new_context(viewport=TELA, device_scale_factor=1,
                                    locale="pt-BR")
        pagina = ctx.new_page()
        faltando, catalogo = montar_rotas(pagina, traducoes)
        pagina.goto(TOTEM, wait_until="networkidle", timeout=120000)
        pagina.wait_for_timeout(ESPERA_CARGA)

        # 1. Tela inicial, agora com o seletor de idioma que a filial liberou.
        salvar(pagina, "totem-espera-idioma.png")

        # 2. Cardápio, no setor dos hambúrgueres avulsos. Este setor, e não o de
        #    combo: o preço de combo sai como "A partir de R$ 35,90", e esse
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
        banner.screenshot(path=str(PURAS / "totem-banner-en.png"), type="png")
        print(f"OK  {(PURAS / 'totem-banner-en.png').relative_to(PASTA.parent.parent)}")

        # 3. O mesmo setor nos três idiomas. Trocar de idioma volta a rolagem
        #    para o topo, então o setor é reaberto depois de cada troca — é
        #    isso que faz as três fotos servirem de antes e depois.
        for idioma, arquivo in (("pt-BR", "totem-menu-pt.png"),
                                ("en-US", "totem-menu-en.png"),
                                ("es-ES", "totem-menu-es.png")):
            escolher_idioma(pagina, idioma)
            abrir_setor(pagina, SETOR_BURGERS)
            salvar(pagina, arquivo)

        # 4. Produto aberto em inglês: é onde a descrição e os grupos de
        #    complemento aparecem traduzidos, e é o argumento do carrossel numa
        #    imagem só — o cliente monta o lanche inteiro na língua dele.
        escolher_idioma(pagina, "en-US")
        abrir_setor(pagina, SETOR_BURGERS)
        abrir_produto(pagina, "MELTED")
        salvar(pagina, "totem-produto-en.png")

        # 5. As fotos dos produtos, do jeito que o sistema serve. A tela do
        #    slide é desenhada (print inteiro reduzido fica com letra de 4 px),
        #    mas a foto dentro dela é a mesma que está no aparelho.
        baixar_fotos(pagina, catalogo)

        # 6. A tela de espera de novo, num totem de 720p, para a capa.
        ctx_menor = navegador.new_context(viewport=TELA_MENOR,
                                          device_scale_factor=2, locale="pt-BR")
        menor = ctx_menor.new_page()
        montar_rotas(menor, traducoes)
        menor.goto(TOTEM, wait_until="networkidle", timeout=120000)
        menor.wait_for_timeout(ESPERA_CARGA)
        salvar(menor, "totem-espera-idioma-720.png")

        # E a mesma tela depois de tocar na bandeira dos Estados Unidos: o botão
        # vira START ORDER. É a versão que a capa usa, porque a capa pergunta
        # "seu cardápio já fala inglês?" e essa tela responde sozinha.
        escolher_idioma(menor, "en-US")
        salvar(menor, "totem-espera-en-720.png")

        navegador.close()

    if faltando:
        print("AVISO: sem tradução no traducoes.json:")
        for f in sorted(faltando):
            print("   ", f)


# O seletor não abre modal: são três botões de bandeira lado a lado, e o
# aplicativo identifica cada um pelo `aria-label`. Clicar troca o idioma da tela
# inteira na hora, que é o gesto que o cliente faz no aparelho.
IDIOMAS = {
    "pt-BR": "Português (Brasil)",
    "en-US": "English (United States)",
    "es-ES": "Español (España)",
}


def escolher_idioma(pagina, idioma: str) -> None:
    pagina.click(f"button[aria-label='{IDIOMAS[idioma]}']", force=True)
    pagina.wait_for_timeout(2500)


# Os setores são escolhidos por posição, e não por nome, porque o nome muda com
# o idioma — que é justamente o que o carrossel está mostrando. 0 é Promoções,
# 1 é Combos Burger, 2 é Burgers Avulsos.
SETOR_BURGERS = 2


def abrir_setor(pagina, indice: int) -> None:
    """Clica o setor na coluna da esquerda, que é como o cliente navega.

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


# Os produtos que entram nas telas desenhadas dos slides. Foram escolhidos
# porque o nome **muda** de idioma (batata frita vira french fries), que é o que
# o carrossel precisa provar, e porque a foto deles é boa o bastante para
# aguentar a redução do feed.
FOTOS = {
    "BATATA FRITA": "foto-batata.png",
    "CEBOLA EMPANADA": "foto-cebola.png",
    "MOZZA STICKS - PALITOS DE MUSSARELA": "foto-mozza.png",
    "BATATA FRITA COM CHEDDAR E BACON": "foto-batata-cheddar.png",
    "MELTED": "foto-melted.png",
    "TASTY BACON": "foto-tasty-bacon.png",
    "ONE CLASSIC": "foto-one-classic.png",
    # Miniaturas da coluna de setores. No aparelho cada setor mostra a foto de
    # um produto dele, e é isso que dá cor à coluna.
    "SMASH 2.0": "foto-smash.png",
    "BROWNIE COM SORVETE E MORANGO": "foto-brownie.png",
    "MILK SHAKE MORANGO": "foto-shake.png",
    "COCA-COLA 350ML": "foto-refri.png",
    "MOLHO CHEDDAR - 30ml": "foto-molho.png",
}


def baixar_fotos(pagina, catalogo: dict[str, str]) -> None:
    """Baixa a foto de cada produto da lista, pela URL que a própria API serve.

    Vem `.webp` do servidor e sai `.png` aqui, que é o formato que o resto da
    esteira usa.
    """
    from io import BytesIO

    from PIL import Image

    for nome, arquivo in FOTOS.items():
        link = catalogo.get(nome.strip())
        if not link:
            print(f"AVISO: sem foto para {nome}")
            continue
        dados = pagina.request.get(link).body()
        with Image.open(BytesIO(dados)) as im:
            im.convert("RGB").save(PURAS / arquivo)
        print(f"OK  {(PURAS / arquivo).relative_to(PASTA.parent.parent)}")


def salvar(pagina, arquivo: str) -> None:
    alvo = PURAS / arquivo
    pagina.screenshot(path=str(alvo), type="png")
    print(f"OK  {alvo.relative_to(PASTA.parent.parent)}")


if __name__ == "__main__":
    main()
