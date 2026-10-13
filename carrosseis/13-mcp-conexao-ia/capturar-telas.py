"""Captura as telas do MCP, para a peça 13.

Somente leitura: nenhuma rota de escrita é chamada, e o único clique que muda
alguma coisa na tela é o que abre a folha lateral do MCP em *Aplicativos*.

São três grupos de imagem, e cada um existe por um motivo diferente:

1. **os cinco quadrados de logotipo da folha do MCP** — ChatGPT, Claude,
   Lovable, Cursor e BeeFood, cada um com o fundo que o próprio painel lhe dá.
   Eles são as `.origem__disco` da cena de convergência do slide 2. A folha
   desenha esses quadrados num **arco animado**, e item que anda não se
   fotografa. O painel já tem o estado parado pronto, na regra
   `@media (prefers-reduced-motion: reduce)` do `mcp-panel.css`, mas
   `emulate_media` sozinho não o alcança: `position: absolute` vem de uma
   classe utilitária com a mesma especificidade da regra de dentro da media
   query, e quem desempata é a ordem das folhas. A captura repete a regra do
   próprio painel com `!important` (`PARAR_ARCO`), e o que aparece é o layout
   que o produto desenha para quem pede menos movimento;
2. **os dois cartões do Desempenho** — `VALOR TOTAL` e `TICKET MÉDIO` dos
   últimos 30 dias. São a prova do slide 3: o número que a IA respondeu é o
   mesmo que o painel fecha. O recorte começa **abaixo** do seletor de datas,
   na linha *Últimos 30 dias*, porque data na arte envelhece o post;
3. **o cartão do MCP na grade de Aplicativos** — onde o recurso mora, com a
   borda arco-íris que o painel desenha em volta dele. É a arte do CTA: o
   último slide manda abrir *Aplicativos → MCP*, e esta é a porta.

O que **não** se captura aqui: o campo *Link do MCP*, o botão de copiar e a
lista de manuais. São tela de configuração — mostram onde se mexe, e carrossel
mostra o que passa a acontecer. O efeito delas é a conversa, e a conversa está
no `conversas.json`, medida pelo `consultar-mcp.py`.
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
PURAS.mkdir(exist_ok=True)

MEDIDAS: dict[str, dict] = {}

# A ordem é a da folha do MCP, e os nomes são os que o painel dá a cada um.
LOGOS = ["lovable", "claude", "chatgpt", "cursor", "beefood"]

# A mesma declaração do bloco `prefers-reduced-motion` do `mcp-panel.css`.
PARAR_ARCO = """
.mcp-panel-bg, .mcp-panel-grain, .mcp-arc-item, .mcp-rainbow-button,
.mcp-rainbow-button::before, .mcp-link-field, .mcp-link-field::before,
.mcp-app-card, .mcp-app-card::before, .mcp-app-card::after {
  animation: none !important;
}
.mcp-arc {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 18px !important;
}
.mcp-arc-item {
  position: static !important;
  margin: 0 !important;
  flex-shrink: 0 !important;
  opacity: 1 !important;
  transform: none !important;
}
"""


def tirar(pagina, nome: str, **kwargs):
    pagina.screenshot(path=str(PURAS / nome), **kwargs)
    print("PURA", nome)


def recortar(pagina, nome: str, de, ate=None, folga=14, lateral=None,
             folga_pe=None, folga_lado=None, parar_acima=None):
    """Recorta pela caixa medida no DOM, nunca estimada na miniatura.

    Mesma função das peças anteriores: `de` e `ate` são locators e dão o topo e
    o pé; `lateral` dá as bordas da esquerda e da direita. A caixa fica no
    `medidas.json`, que é o que permite refazer o mesmo quadro depois.

    `parar_acima` é novo aqui, e resolve o caso em que o que precisa ficar de
    fora é a **última** linha de um bloco: o pé passa a ser o topo desse
    locator, menos a folga. Medir uma sobra negativa dava o mesmo resultado e
    envelhecia mal, porque o número dependia da altura da linha.
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
    base = (parar_acima.bounding_box()["y"] - pe if parar_acima is not None
            else b["y"] + b["height"] + pe)
    caixa = {"x": x, "y": topo, "width": largura, "height": base - topo}
    pagina.screenshot(path=str(PURAS / nome), clip=caixa)
    MEDIDAS[nome] = caixa
    print("RECORTE", nome, {k: round(v) for k, v in caixa.items()})


def salvar_medidas():
    if not MEDIDAS:
        return
    arq = AQUI / "medidas.json"
    antigo = json.loads(arq.read_text()) if arq.is_file() else {}
    antigo.update({k: {c: round(v, 1) for c, v in cx.items()}
                   for k, cx in MEDIDAS.items()})
    arq.write_text(json.dumps(antigo, indent=2, ensure_ascii=False) + "\n")
    print("medidas.json:", len(antigo), "recortes")


def aplicativos():
    """A grade de Aplicativos e a folha lateral do MCP."""
    with sessao("painel") as pagina:
        pagina.emulate_media(reduced_motion="reduce")
        pagina.goto("https://beefood.app/aplicativos",
                    wait_until="domcontentloaded", timeout=90000)
        esperar(pagina)
        limpar(pagina)
        tirar(pagina, "01-aplicativos.png")

        # O cartão do MCP na grade, com a borda arco-íris que o painel desenha
        # em volta dele. É a arte do CTA.
        cartao = pagina.locator(".mcp-app-card").first
        if cartao.count():
            recortar(pagina, "rec-cartao-mcp.png", cartao, lateral=cartao, folga=12)

        pagina.get_by_text("Conecte o seu BeeFood a sua IA favorita",
                           exact=False).first.click()
        pagina.wait_for_timeout(6000)
        esperar(pagina)
        pagina.add_style_tag(content=PARAR_ARCO)
        pagina.wait_for_timeout(1500)
        tirar(pagina, "02-folha-mcp.png")

        itens = pagina.locator(".mcp-arc-item")
        print("quadrados no arco:", itens.count())
        for i, nome in enumerate(LOGOS):
            if i >= itens.count():
                break
            caixa = itens.nth(i).bounding_box()
            print("  ", nome, {k: round(v) for k, v in caixa.items()})
            pagina.screenshot(path=str(PURAS / f"logo-{nome}.png"), clip=caixa)
            MEDIDAS[f"logo-{nome}.png"] = caixa
        salvar_medidas()


def conferir(valor_painel: str, ticket_painel: str):
    """Exige que o painel fotografado e a conversa gravada digam o mesmo.

    A loja de demonstração **recebe pedido enquanto a peça é feita**: entre uma
    rodada e a seguinte o total subiu de 13.473,52 para 13.518,52 e depois
    para 13.563,52, em poucos minutos. Isso não é detalhe de execução — é o
    que decide se a peça tem **um** jogo de números ou dois, e a única imagem
    de captura dela existe justamente para dizer que o número da conversa é o
    do painel.

    Por isso a conferência é do script, e não do olho: rode o
    `consultar-mcp.py` e este, em seguida, no mesmo minuto.
    """
    arquivo = AQUI / "conversas.json"
    if not arquivo.is_file():
        print("AVISO: sem conversas.json; rode o consultar-mcp.py antes")
        return
    gravado = json.loads(arquivo.read_text())["resumo"]
    limpar_ = lambda t: t.replace("\xa0", " ").strip()  # noqa: E731
    par = [(limpar_(valor_painel), gravado["valorEscrito"]),
           (limpar_(ticket_painel), gravado["ticketEscrito"])]
    print("painel:", par[0][0], "|", par[1][0],
          "   conversa:", par[0][1], "|", par[1][1])
    if any(a != b for a, b in par):
        raise SystemExit(
            "ERRO: o painel e a conversa divergiram — a loja de demonstração "
            "recebeu pedido no meio. Rode o consultar-mcp.py e repita esta "
            "captura em seguida.")
    print("--> painel e conversa fecham no mesmo número")


def desempenho():
    """Os dois cartões do topo do Desempenho, nos últimos 30 dias.

    O período é o que a tela abre sozinha — *Últimos 30 dias* —, e é o mesmo
    que o `consultar-mcp.py` pergunta ao MCP. É isso que faz a peça ter **um**
    jogo de números: o painel e a conversa fecham no mesmo valor.

    O recorte começa na linha *Últimos 30 dias*, e não no seletor acima dela:
    ali estão as datas, e arte com data faz o post nascer velho.

    **O Desempenho não é uma página do painel: é um `iframe`** servido por
    `relatorios.beefood.com.br`. Procurar o rótulo no documento de fora não
    acha nada — nem `VALOR TOTAL`, nem `Valor total`, nem nada —, e a busca
    sai vazia em vez de dar erro, que é o pior jeito de descobrir isso.
    `frame_locator` resolve, e a caixa que ele mede já vem em coordenada da
    página, que é o que o `clip` do print espera.
    """
    with sessao("painel") as pagina:
        pagina.goto("https://beefood.app/desempenho",
                    wait_until="domcontentloaded", timeout=90000)
        esperar(pagina)
        limpar(pagina)
        tirar(pagina, "03-desempenho.png")

        relatorio = pagina.frame_locator("iframe")
        total = relatorio.get_by_text("VALOR TOTAL", exact=False).first
        ticket = relatorio.get_by_text("TICKET MÉDIO", exact=False).first
        # O quadro fecha no número, e a linha de comparação fica de fora.
        # `+131,3% vs período anterior` é verdade da loja de demonstração e,
        # numa peça de venda, lê como crescimento prometido pelo produto — é a
        # lição da #9, que cortou o `R$ 0,00 de receita gerada` pelo mesmo
        # motivo, do outro lado. O que o slide afirma é o total e o ticket, e
        # o quadro para exatamente onde a afirmação para.
        # O número é o irmão seguinte do rótulo, e a comparação é o de depois.
        # Fechar no pé do número com folga zero é o que deixa a linha verde
        # inteira de fora: 16 px de sobra traziam a metade de cima dela, e
        # linha cortada ao meio lê como erro de render.
        valor = ticket.locator("xpath=following-sibling::*[1]")
        cartao = ticket.locator("xpath=ancestor::div[contains(@class,'rounded')][1]")
        recortar(pagina, "rec-desempenho.png", total, valor,
                 lateral=(total, cartao), folga=20, folga_lado=(22, 22),
                 folga_pe=4)
        conferir(total.locator("xpath=following-sibling::*[1]").inner_text(),
                 valor.inner_text())

        # A QUEBRA POR CANAL NÃO SE FOTOGRAFA AQUI, e isso custou uma rodada.
        #
        # *Desempenho → Vendas → Origem* parece o par da pergunta do slide 4, e
        # não é: ele agrupa por **tipo de atendimento** (Delivery, Mesas, PDV,
        # Cardápio Digital, iFood, 99Food, Keeta), enquanto a API agrupa por
        # `salesChannel` — onde balcão, mesa e PDV caem todos em `MANUAL`. Os
        # dois somam o mesmo total e repartem diferente: a tela dá Delivery com
        # R$ 7.431,87 na lista e R$ 10.330,37 no pódio logo abaixo, porque nem
        # ela usa um corte só.
        #
        # Pôr a lista do chat ao lado dessa tela seria oferecer ao leitor duas
        # contas que não fecham entre si, e a peça inteira se apoia em fechar.
        # A prova de que a IA lê o dado certo é a de cima — valor total e
        # ticket médio, que são iguais nos dois lugares.
        salvar_medidas()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("alvos", nargs="*", default=[])
    args = ap.parse_args()
    alvos = args.alvos or ["aplicativos", "desempenho"]
    if "aplicativos" in alvos:
        aplicativos()
    if "desempenho" in alvos:
        desempenho()


if __name__ == "__main__":
    main()
