"""Captura as telas de RESULTADO do Programa de Pontos, para a peça 12.

Somente leitura do lado do restaurante. O roteiro do celular monta uma sacola e
resgata uma recompensa, e **para antes de fechar o pedido**: o ponto só sai do
saldo quando a venda nasce, e a venda não nasce aqui (é a técnica do ensaio).
O saldo de 121 pontos do cliente de teste foi creditado pelo `cenario.py` do
manual `programa-pontos`, e continua intacto — é o que mantém *Faltam 59 pts*
sendo a mesma conta em todos os slides.

O que **não** se captura aqui: a aba Configuração, as Regras de acúmulo, os dois
cartões de bônus e o cadastro de recompensa. São telas de campo, e tela de
configuração não entra em carrossel — o que entra é o efeito delas, que é
justamente o que o cliente lê.

Três armadilhas deste cardápio, herdadas do `capturar-cardapio.py` do manual e
confirmadas aqui:

* o rodapé só responde em `.v-bottom-navigation .v-btn`;
* **Perfil** deslogado abre o login e volta para a home — é preciso tocar de novo;
* a sacola só mostra o cartão de pontos **depois** da modalidade escolhida, e o
  caminho curto é *Retirar no estabelecimento* (entrega abre o mapa).

E uma quarta, que o manual não pegou porque capturou de manhã: **fora do horário
a loja exige agendamento** antes de liberar a etapa dos pontos. Marcar dia e hora
e tocar em *AGENDAR PEDIDO* não cria pedido nenhum — é escolha guardada na sacola
—, e sem essa etapa o *Continuar* não sai da modalidade. O script tenta agendar
sempre que a tela aparecer, e segue direto quando ela não aparece.

O produto do pedido é o lanche **Chicken Deluxe**, não o *Combo Chicken Deluxe*:
o combo tem dois grupos de opções obrigatórios, e com eles o botão *Adicionar*
não responde.

A diferença em relação ao manual é a resolução: celular em DPR **3**, porque aqui
o print entra reduzido dentro da moldura do slide, e a nitidez é o que sobra.

E há uma **recompensa de produto devolvida pela resposta da API**, registrada no
`cena.json`. Entre o manual e esta peça alguém trocou o cadastro: a recompensa
que o cliente via (`produtoID` 2515303, *Chicken Deluxe grátis* por 100 pontos)
saiu, e entrou uma com o id interno do painel, que o cardápio público descarta
em silêncio — é o defeito 1 do `fluxo-codigo.md` do manual. Com `--cru` o script
mostra a vitrine como ela está hoje, só com os três descontos.
"""

from __future__ import annotations

import argparse
import contextlib
import json
import os
import sys
from pathlib import Path

sys.path.append(".cursor/skills/carrossel/scripts")
from capturar import esperar, limpar, sessao  # noqa: E402

from playwright.sync_api import sync_playwright  # noqa: E402

AQUI = Path(__file__).resolve().parent
PURAS = AQUI / "imagens-puras"
PURAS.mkdir(exist_ok=True)

CARDAPIO = "https://menu.beefood.com.br/beefood3"
TELEFONE = "15999998888"            # cliente Teste Manual da sandbox
PRODUTO = "Chicken Deluxe"          # o lanche simples; o *Combo* tem grupo obrigatório
RECOMPENSA = "R$ 10,00 de desconto"

CELULAR = {"width": 390, "height": 844}
COMPUTADOR = {"width": 1440, "height": 900}

# As três de desconto são as que estão cadastradas hoje; a de produto é a que o
# manual fotografou de manhã e que saiu do cadastro desde então. Ver cena.json.
RECOMPENSAS = {
    "desconto": [{"id": 1, "valorDesconto": 5, "pontosNecessarios": 50},
                 {"id": 2, "valorDesconto": 10, "pontosNecessarios": 100},
                 {"id": 3, "valorDesconto": 20, "pontosNecessarios": 180}],
    "produto": [{"id": 4, "produtoID": 2515303, "pontosNecessarios": 100,
                 "pontosPorReal": 0}],
}


MEDIDAS: dict[str, dict] = {}


def assentar(pagina, ms: int = 4000):
    """Espera a fonte dos ícones chegar, e só então deixa fotografar.

    Os selos do cardápio — o desconto, o presente, a estrela — são glifos de
    webfont. Numa rodada a fonte não chegou a tempo e a vitrine saiu sem
    nenhum deles: a tela continua certa, e a prova, não. Os cinco segundos de
    espera da casa não pegam isso, porque o spinner já tinha sumido.
    """
    with contextlib.suppress(Exception):
        pagina.wait_for_load_state("networkidle", timeout=20000)
    with contextlib.suppress(Exception):
        pagina.evaluate("() => document.fonts.ready")
    pagina.wait_for_timeout(ms)


def tirar(pagina, nome: str, **kwargs):
    pagina.screenshot(path=str(PURAS / nome), **kwargs)
    print("PURA", nome)


def recortar(pagina, nome: str, de, ate=None, folga=14, lateral=None, folga_pe=None,
             folga_lado=None):
    """Recorta pela caixa MEDIDA no DOM, nunca estimada na miniatura.

    `de` e `ate` são locators: a faixa vai do topo do primeiro ao pé do último.
    Com `lateral`, um terceiro locator dá as bordas da esquerda e da direita —
    é o que tira o menu lateral do painel sem ninguém contar pixel. A medida
    fica no `medidas.json`, que é o que permite refazer o mesmo quadro quando a
    tela mudar de conteúdo.

    `folga_pe` separa a sobra de baixo da de cima. Serve para quando a linha
    seguinte precisa ficar de fora inteira e a de cima ainda precisa respirar.

    `folga_lado` faz o mesmo nos lados, e aceita um par `(esquerda, direita)`.
    Numa tabela, a célula já traz o próprio respiro: somar folga à direita
    deixa entrar uma lasca da coluna seguinte, que lê como erro de recorte.
    """
    a = de.bounding_box()
    b = (ate or de).bounding_box()
    topo = max(0, a["y"] - folga)
    if lateral is None:
        x, largura = 0, pagina.viewport_size["width"]
    else:
        esq, dir_ = lateral if isinstance(lateral, tuple) else (lateral, lateral)
        lado = folga if folga_lado is None else folga_lado
        f_esq, f_dir = lado if isinstance(lado, tuple) else (lado, lado)
        c, d = esq.bounding_box(), dir_.bounding_box()
        x = max(0, c["x"] - f_esq)
        largura = (d["x"] + d["width"] + f_dir) - x
    pe = folga if folga_pe is None else folga_pe
    caixa = {"x": x, "y": topo,
             "width": largura, "height": (b["y"] + b["height"] + pe) - topo}
    pagina.screenshot(path=str(PURAS / nome), clip=caixa)
    MEDIDAS[nome] = caixa
    print("RECORTE", nome, {k: round(v) for k, v in caixa.items()})


def salvar_medidas():
    if not MEDIDAS:
        return
    arq = AQUI / "medidas.json"
    antigo = json.loads(arq.read_text()) if arq.is_file() else {}
    antigo.update({k: {c: round(v, 1) for c, v in cx.items()} for k, cx in MEDIDAS.items()})
    arq.write_text(json.dumps(antigo, indent=2, ensure_ascii=False) + "\n")
    print("medidas.json:", len(antigo), "recortes")


def fechar_faixa_cupom(pagina):
    """A faixa verde de cupons cobre o topo e não tem a ver com pontos."""
    x = pagina.locator("i.mdi-close")
    if x.count():
        x.first.click()
        pagina.wait_for_timeout(1500)


def agendar_se_preciso(pagina):
    """Fora do horário, a sacola exige dia e hora antes de liberar os pontos."""
    botao = pagina.locator(".v-btn, button").filter(has_text="AGENDAR PEDIDO")
    if not botao.count():
        return False
    pagina.get_by_text("12:00 - 12:30", exact=False).first.click()
    pagina.wait_for_timeout(2000)
    botao.first.click()
    pagina.wait_for_timeout(12000)
    print("--> loja fechada: pedido agendado na sacola (nada foi gravado)")
    return True


def entrar(pagina):
    pagina.locator(".v-bottom-navigation .v-btn").filter(has_text="Perfil").first.click()
    pagina.wait_for_timeout(5000)
    pagina.locator("input[type=tel]").first.fill(TELEFONE)
    pagina.locator(".v-btn").filter(has_text="CONTINUAR").first.click()
    pagina.wait_for_timeout(10000)


def abrir(p, viewport, dpr, cru=False):
    nav = p.chromium.launch(args=["--no-sandbox"],
                            env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"})
    ctx = nav.new_context(viewport=viewport, device_scale_factor=dpr,
                          is_mobile=viewport is CELULAR, has_touch=viewport is CELULAR,
                          locale="pt-BR", timezone_id="America/Sao_Paulo")
    if not cru:
        ctx.route("**/pontos/recompensas/**",
                  lambda rota: rota.fulfill(status=200, content_type="application/json",
                                            body=json.dumps(RECOMPENSAS)))
    return nav, ctx, ctx.new_page()


def celular(p, cru=False):
    nav, ctx, pagina = abrir(p, CELULAR, 3, cru)
    sufixo = "-cru" if cru else ""
    try:
        pagina.goto(CARDAPIO, wait_until="domcontentloaded")
        pagina.wait_for_timeout(12000)
        fechar_faixa_cupom(pagina)
        assentar(pagina)

        # A porta de entrada: a faixa de acúmulo e a grade de produtos. O alto da
        # tela fica fora do recorte de propósito — ali mora o horário da loja, e
        # a sandbox está fechada; é estado da loja de exemplo, não do recurso.
        tirar(pagina, f"01-home-faixa-e-selo{sufixo}.png")
        if not cru:
            # O pé fecha no primeiro cartão inteiro. Descer até o segundo partia
            # a foto dele ao meio, e borda de recorte em cima de produto lê como
            # erro de render — a regra é fechar em área vazia.
            recortar(pagina,
                     "rec-home-faixa.png",
                     pagina.get_by_text("Acumule pontos a cada compra", exact=False).first,
                     pagina.get_by_text("R$ 29,00", exact=False).first,
                     folga=16, folga_pe=18)

        entrar(pagina)
        pagina.locator(".v-bottom-navigation .v-btn").filter(has_text="Perfil").first.click()
        pagina.wait_for_timeout(6000)

        # O saldo e o extrato, na mão de quem pediu
        pagina.get_by_text("Programa de pontos", exact=False).first.click()
        pagina.wait_for_timeout(8000)
        assentar(pagina)
        tirar(pagina, f"02-meus-pontos{sufixo}.png")

        # A vitrine: o que ele pode trocar, e quanto falta
        pagina.get_by_text("Ver o que você pode ganhar", exact=False).first.click()
        pagina.wait_for_timeout(7000)
        assentar(pagina)
        tirar(pagina, f"03-vitrine-recompensas{sufixo}.png")
        if not cru:
            recortar(pagina, "rec-vitrine.png",
                     pagina.get_by_text("Recompensas", exact=True).first,
                     pagina.get_by_text("Chicken Deluxe grátis", exact=False).first,
                     folga=18, folga_pe=38)
        pagina.keyboard.press("Escape")
        pagina.wait_for_timeout(2500)

        # Sacola: o lanche simples, retirada no balcão
        pagina.goto(CARDAPIO, wait_until="domcontentloaded")
        pagina.wait_for_timeout(10000)
        pagina.get_by_text(PRODUTO, exact=True).first.click()
        pagina.wait_for_timeout(8000)
        pagina.locator(".v-btn").filter(has_text="Adicionar").last.click()
        pagina.wait_for_timeout(8000)
        pagina.get_by_text("Ver sacola", exact=False).first.click()
        pagina.wait_for_timeout(9000)
        pagina.locator(".v-btn").filter(has_text="Continuar").last.click()
        pagina.wait_for_timeout(8000)
        pagina.get_by_text("Retirar no estabelecimento", exact=False).first.click()
        pagina.wait_for_timeout(4000)
        pagina.locator(".v-btn").filter(has_text="Continuar").last.click()
        pagina.wait_for_timeout(11000)
        if agendar_se_preciso(pagina):
            pagina.locator(".v-btn").filter(has_text="Continuar").last.click()
            pagina.wait_for_timeout(13000)

        pagina.get_by_text("Programa de Pontos", exact=False).first.scroll_into_view_if_needed()
        pagina.wait_for_timeout(2500)
        assentar(pagina)
        tirar(pagina, f"04-sacola-com-pontos{sufixo}.png")
        if not cru:
            # O quadro vai do total até a linha do ganho, e carrega o Continuar
            # no meio. É de propósito: o botão é igual nas duas fotos, e é ele
            # que faz o olho ir direto no número que mudou e no que não mudou.
            recortar(pagina, "rec-total-antes.png",
                     pagina.get_by_text("Total do pedido", exact=False).first,
                     pagina.get_by_text("Ganhe", exact=False).last,
                     folga=18, folga_pe=16)

        linha = pagina.get_by_text(RECOMPENSA, exact=False).first.locator(
            "xpath=ancestor::*[.//button or .//*[contains(@class,'v-btn')]][1]")
        linha.locator(".v-btn, button").filter(has_text="RESGATAR").first.click()
        pagina.wait_for_timeout(9000)
        assentar(pagina)
        tirar(pagina, f"05-sacola-resgatada{sufixo}.png")
        if not cru:
            # As duas faixas do antes e do depois saem com a MESMA caixa, medida
            # na mesma tela: altura diferente entre elas leria como corte torto.
            recortar(pagina, "rec-total-depois.png",
                     pagina.get_by_text("Total do pedido", exact=False).first,
                     pagina.get_by_text("Ganhe", exact=False).last,
                     folga=18, folga_pe=16)
        print("ATENÇÃO: o pedido NÃO foi fechado — o resgate não consumiu ponto.")
    finally:
        salvar_medidas()
        ctx.close()
        nav.close()


def computador(p, cru=False):
    nav, ctx, pagina = abrir(p, COMPUTADOR, 2, cru)
    try:
        pagina.goto(CARDAPIO, wait_until="domcontentloaded")
        pagina.wait_for_timeout(13000)
        fechar_faixa_cupom(pagina)
        banner = pagina.locator(".banner-pontos")
        print("banner-pontos no computador:", banner.count())
        if not banner.count():
            return
        banner.first.scroll_into_view_if_needed()
        pagina.wait_for_timeout(2500)
        tirar(pagina, "06-computador-cartao.png")
    finally:
        ctx.close()
        nav.close()


def painel():
    """As duas telas do lado do restaurante: o saldo em circulação e a automação.

    Telefone de cliente sai **borrado na pura**, porque a pura também é
    versionada e o repositório é público. O borrão pega só o nó mais interno de
    cada cadeia: borrar o ancestral apagaria a linha inteira.
    """
    with sessao("painel") as pagina:
        pagina.goto("https://beefood.app/programa-pontos", wait_until="domcontentloaded",
                    timeout=90000)
        esperar(pagina)
        limpar(pagina)
        pagina.get_by_role("button", name="Saldo por Cliente").first.click()
        esperar(pagina)
        borrados = pagina.evaluate(
            """() => {
              const re = /\\(?\\d{2}\\)?\\s?\\d{4,5}-?\\d{4}/;
              const todos = [...document.querySelectorAll('span,div,td,p')]
                .filter((e) => re.test(e.textContent || ''));
              const folhas = todos.filter((e) => !todos.some((o) => o !== e && e.contains(o)));
              folhas.forEach((e) => { e.style.filter = 'blur(6px)'; });
              return folhas.length;
            }"""
        )
        print("telefones borrados:", borrados)
        pagina.wait_for_timeout(1200)
        tirar(pagina, "07-saldo-por-cliente.png")
        # O menor ancestral que contém os quatro cartões é a própria grade: usá-la
        # dos dois lados pega o cartão inteiro, com ícone e borda. Medir pelo
        # texto cortava o ícone da esquerda, porque o `div` do texto começa depois.
        grade = pagina.get_by_text("Total de Pontos", exact=False).first.locator(
            "xpath=ancestor::div[.//*[contains(text(),'Média por Cliente')]][1]")
        recortar(pagina, "rec-totais-painel.png", grade, lateral=grade, folga=10)

        # Duas linhas da lista, para o slide nao ficar so com a faixa fina dos
        # totais. Sao as duas contas de teste com nome — as outras linhas da
        # sandbox aparecem como "-", e lista de tracos nao prova nada.
        #
        # O rótulo é *Saldo total* no DOM: o maiúsculo da tela é `text-transform`
        # do CSS, e xpath lê o texto, não o estilo. Ancorar em `SALDO TOTAL` não
        # acha nada e estoura em timeout.
        def cartao_da_linha(nome: str):
            return pagina.get_by_text(nome, exact=True).first.locator(
                "xpath=ancestor::div[.//*[contains(text(),'Saldo total')]][1]")

        primeira, ultima = cartao_da_linha("Bruno Pontos"), cartao_da_linha("Teste Manual")
        recortar(pagina, "rec-linhas-cliente.png", primeira, ultima,
                 folga=8, lateral=primeira)

        # A campanha e o público que a BeeFood já deixa cadastrados para os pontos
        pagina.goto("https://beefood.app/food-marketing/campanhas-whatsapp",
                    wait_until="domcontentloaded", timeout=90000)
        esperar(pagina)
        limpar(pagina)
        # As abas desta página não são `role="tab"`: são botões comuns. E clicar
        # pelo texto pega o título da seção, que fica atrás de outro bloco.
        pagina.locator("button").filter(has_text="Campanhas Inteligentes").first.click()
        esperar(pagina)
        with contextlib.suppress(Exception):
            pagina.get_by_text("Pontos parados", exact=False).first.scroll_into_view_if_needed()
            pagina.wait_for_timeout(1500)
        tirar(pagina, "08-campanha-pontos-parados.png")
        # O corte para antes da linha de receita: a loja de teste nunca disparou
        # nada, e R$ 0,00 numa peça de venda desmente a peça. É a lição da #9.
        cartao = pagina.locator("div").filter(
            has=pagina.get_by_text("Avisa quem tem pontos parados", exact=False)).last
        # O quadro começa na pílula `Ativo`, e não no título: são ela, o selo
        # `BeeFood` e a chave ligada à direita que provam a frase do slide — a
        # campanha chega cadastrada e ligada, e não é a loja que a monta.
        # (`Pontos parados` é o primeiro cartão da grade, então `.first` basta.)
        recortar(pagina, "rec-campanha.png",
                 pagina.get_by_text("Ativo", exact=True).first,
                 pagina.get_by_text("Avisa quem tem pontos parados", exact=False).first,
                 folga=10, folga_pe=6, lateral=cartao)

        pagina.goto("https://beefood.app/food-marketing/segmentacao-cliente",
                    wait_until="domcontentloaded", timeout=90000)
        esperar(pagina)
        limpar(pagina)
        tirar(pagina, "09-segmentacao-pontos-parados.png")
        # A direita da tabela e so data de criacao e botao. Cortada ali, a
        # faixa cai de 1218 para ~670 px de largura e o nome do publico chega
        # ao slide com o dobro do corpo — que e o que precisa ser lido.
        #
        # E o quadro comeca na linha dos pontos, nao no alto da tabela: acima
        # dela a sandbox tem *Cashback parado* duas vezes, e linha repetida num
        # print de venda le como defeito da tela. Ficam as duas linhas que
        # fazem a frase — a dos pontos e a seguinte, as duas feitas pela
        # BeeFood, que e o que prova o "ja vem pronto".
        tabela = pagina.locator("table, [role=table]").first
        recortar(pagina, "rec-segmentacao.png",
                 pagina.get_by_text("Pontos parados", exact=False).first,
                 pagina.get_by_text("Aniversariantes do dia", exact=False).first,
                 folga=14,
                 lateral=(tabela, pagina.get_by_text("Beefood (sistema)", exact=False).first),
                 folga_lado=(14, 0))
        salvar_medidas()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("alvos", nargs="*", default=[])
    ap.add_argument("--cru", action="store_true",
                    help="sem a recompensa de produto devolvida pela API")
    args = ap.parse_args()
    alvos = args.alvos or ["celular", "computador", "painel"]
    if "painel" in alvos:
        painel()
    if {"celular", "computador"} & set(alvos):
        with sync_playwright() as p:
            if "celular" in alvos:
                celular(p, args.cru)
            if "computador" in alvos:
                computador(p, args.cru)


if __name__ == "__main__":
    main()
