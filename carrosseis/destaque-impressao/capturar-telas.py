#!/usr/bin/env python3
"""Capturas deste carrossel que exigem clique (o CLI do capturar.py não basta).

Rodar da raiz do repositório:
    python carrosseis/destaque-impressao/capturar-telas.py

O que sai em imagens-puras/:
    03-modal-produto.png     modal da Coca Cola 350ml com o interruptor ligado
    03-modal-janela.png      pedaço do modal que entra na janela em sangria
    03-modal-recorte.png     faixa do interruptor, usada na lupa sobre a janela
    04-novidades-celular.png a página de novidades no celular
"""

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ / ".cursor" / "skills" / "carrossel-novidades" / "scripts"))

from capturar import esperar, limpar, sessao  # noqa: E402

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


if __name__ == "__main__":
    modal_do_produto()
    novidades_no_celular()
