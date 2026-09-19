#!/usr/bin/env python3
"""Capturas deste carrossel que exigem clique (o CLI do capturar.py não basta).

Rodar da raiz do repositório:
    python carrosseis/01-destaque-impressao/capturar-telas.py

O que sai em imagens-puras/:
    01-cupom-bebida.png      cupom real com SÓ a bebida destacada (imagem da capa)
    03-modal-produto.png     modal da Coca Cola 350ml com o interruptor ligado
    03-modal-janela.png      pedaço do modal que entra na janela em sangria
    03-modal-recorte.png     faixa do interruptor, usada na lupa sobre a janela
    04-novidades-celular.png a página de novidades no celular

O cupom vem em duas etapas, porque a primeira registra uma venda no sandbox:
    python carrosseis/01-destaque-impressao/capturar-telas.py venda   # uma vez só
    python carrosseis/01-destaque-impressao/capturar-telas.py cupom   # reimprime
"""

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ / ".cursor" / "skills" / "carrossel" / "scripts"))

from capturar import esperar, ganchar_cupom, limpar, salvar_cupom, sessao  # noqa: E402

PURAS = Path(__file__).resolve().parent / "imagens-puras"
PURAS.mkdir(exist_ok=True)

VIEWPORT = (1440, 900)


def recorte(x0: float, y0: float, x1: float, y1: float) -> dict:
    largura, altura = VIEWPORT
    return {"x": round(x0 * largura), "y": round(y0 * altura),
            "width": round((x1 - x0) * largura), "height": round((y1 - y0) * altura)}


def modal_do_produto() -> None:
    """A tela-chave: o interruptor Destaque na impressão no cadastro.

    O sandbox tem **dois** produtos chamados Coca Cola 350ml (um deles com Preço
    Programado). Por isso o clique vai pelo cartão de dentro do setor Bebidas,
    por posição, e não por texto: nome repetido pega o produto errado.
    """
    with sessao("painel") as pagina:
        pagina.goto("https://beefood.app/cardapio", wait_until="domcontentloaded",
                    timeout=90000)
        esperar(pagina)
        limpar(pagina)

        pagina.get_by_text("Coca Cola 350ml", exact=True).first.click()
        esperar(pagina)
        limpar(pagina)

        # O interruptor fica logo abaixo de Descrição; rolar até ele garante que
        # entra no recorte.
        alvo = pagina.get_by_text("Destaque na impressão", exact=False).first
        alvo.scroll_into_view_if_needed()
        pagina.wait_for_timeout(1500)

        pagina.screenshot(path=str(PURAS / "03-modal-produto.png"), type="png")
        print("OK  03-modal-produto.png")

        # Dois recortes, dois papéis. A janela em sangria dá o contexto ("é uma
        # tela do sistema") e por isso pode ser larga; a lupa por cima é a que
        # precisa ser lida, e para isso não passa de ~440 px de largura lógica.
        pagina.screenshot(path=str(PURAS / "03-modal-janela.png"), type="png",
                          clip=recorte(0.25, 0.47, 0.67, 0.83))
        print("OK  03-modal-janela.png")

        # A borda direita da lupa cai em área vazia: corte no meio de uma
        # palavra parece defeito.
        pagina.screenshot(path=str(PURAS / "03-modal-recorte.png"), type="png",
                          clip=recorte(0.295, 0.706, 0.615, 0.780))
        print("OK  03-modal-recorte.png")


def novidades_no_celular() -> None:
    with sessao("celular", publico=True) as pagina:
        pagina.goto("https://beefood.app/novidades", wait_until="networkidle",
                    timeout=90000)
        esperar(pagina)
        pagina.screenshot(path=str(PURAS / "04-novidades-celular.png"), type="png")
        print("OK  04-novidades-celular.png")


def registrar_pedido() -> None:
    """Registra no sandbox o pedido que vai virar a imagem da capa.

    Por que um pedido novo em vez do print do manual #99: aquele cupom sai com
    DUAS linhas em preto, a Coca Cola e o "Sem Maionese Verde", porque o manual
    precisava mostrar que complemento também destaca. Na capa do carrossel duas
    faixas dividem a atenção e contradizem o slide 7, que pede parcimônia. Aqui
    o combo é montado sem o complemento destacado, então o preto sai só na
    bebida — e continua sendo impressão de verdade, não desenho.

    Efeito colateral: uma venda em dinheiro na empresa de teste. Rode uma vez; a
    etapa `cupom` reimprime o pedido quantas vezes precisar, de graça.
    """
    with sessao("painel") as pagina:
        pagina.goto("https://beefood.app/pdv", wait_until="domcontentloaded",
                    timeout=90000)
        esperar(pagina, 7000)
        limpar(pagina)

        pagina.fill('input[placeholder="Digite algo para buscar..."]', "Combo One Burger")
        esperar(pagina, 3000)
        # O cartão do PDV não é <button>: é uma div com cursor-pointer. Seletor
        # herdado do manual #99, que já tropeçou nisto.
        cartoes = [c for c in pagina.locator('div[class*="cursor-pointer"]').all()
                   if "One Burger" in (c.inner_text() or "")
                   and "COMBO" in (c.inner_text() or "").upper()]
        if not cartoes:
            raise SystemExit("ERRO: não achei o cartão do Combo One Burger no PDV")
        cartoes[0].click()
        esperar(pagina, 4000)

        # Escolhe só o que o combo pede escolher. O grupo "Burger" tem uma opção
        # única e já vem marcada: clicar nela DESMARCA, o obrigatório fica vazio
        # e o "Adicionar ao carrinho" fecha o modal sem pôr nada no carrinho —
        # sem erro na tela. Foi o que travou as duas primeiras tentativas.
        # "Sem Maionese Verde" fica de fora de propósito: é o outro item com
        # destaque ligado no sandbox.
        modal = pagina.locator('div[role="dialog"]').last
        for item in ("Batata frita", "Coca Cola 350ml"):
            alvo = modal.get_by_text(item, exact=True).first
            alvo.scroll_into_view_if_needed()
            alvo.click()
            esperar(pagina, 1200)

        # O botão fica habilitado mesmo com grupo obrigatório vazio, e aí o clique
        # não põe nada no carrinho. O preço no rótulo é o que prova a seleção:
        # 28,00 é o combo cru, 39,00 é com batata (+3) e Coca (+8).
        botao = modal.locator('button:has-text("Adicionar ao carrinho")').first
        rotulo = botao.inner_text()
        if "39,00" not in rotulo:
            raise SystemExit(f"ERRO: seleção incompleta — botão diz {rotulo!r}")
        botao.click()
        esperar(pagina, 4000)

        receber = pagina.locator('button:has-text("Receber (F3)")').first
        if receber.is_disabled():
            raise SystemExit("ERRO: carrinho vazio depois de adicionar; tela diz: "
                             f"{pagina.inner_text('body')[:800]!r}")

        receber.click()
        esperar(pagina, 6000)
        pagina.locator('button:has-text("Dinheiro")').first.click()
        esperar(pagina, 3000)
        pagina.locator('button:has-text("CONFIRMAR")').first.click()
        esperar(pagina, 8000)
        print("--> venda registrada")


def cupom_da_ultima_venda() -> None:
    """Reimprime a venda mais recente e guarda o Cupom Pedido dela.

    Largura de 340 px porque a bobina é um bloco de largura fixa centralizado na
    página de impressão: num viewport largo sobra margem branca dos dois lados, e
    aí o recorte da arte teria que mexer no eixo X também. Em 340 o papel é a
    imagem inteira e o slide só precisa dizer onde cortar em cima.
    """
    with sessao("painel") as pagina:
        pagina.goto("https://beefood.app/historico", wait_until="domcontentloaded",
                    timeout=90000)
        esperar(pagina, 6000)
        limpar(pagina)
        linha = pagina.locator("table tbody tr").first
        (linha.locator("button").first if linha.locator("button").count() else linha).click()
        # O detalhe da venda é a tela lenta do sistema (MEMORIA-GERAL, seção 3).
        esperar(pagina, 14000)
        limpar(pagina)

        ganchar_cupom(pagina)
        impressora = pagina.locator('[role="dialog"] button').filter(
            has=pagina.locator("svg.lucide-printer"))
        if impressora.count() == 0:
            impressora = pagina.locator("button").filter(
                has=pagina.locator("svg.lucide-printer"))
        impressora.first.click(force=True)

        destino = PURAS / "01-cupom-bebida.png"
        texto = salvar_cupom(pagina, destino, largura=340)
        pretas = [l for l in texto.splitlines() if "Coca Cola" in l]
        print(f"OK  {destino.name}")
        print(f"--> linha da bebida no cupom: {pretas}")
        print("--> confira no PNG que existe UMA faixa preta; se saiu mais de "
              "uma, o sandbox ganhou outro item com destaque ligado")


if __name__ == "__main__":
    etapas = sys.argv[1:] or ["telas"]
    if "venda" in etapas:
        registrar_pedido()
    if "cupom" in etapas:
        cupom_da_ultima_venda()
    if "telas" in etapas:
        modal_do_produto()
        novidades_no_celular()
