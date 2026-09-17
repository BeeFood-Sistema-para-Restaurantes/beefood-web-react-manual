#!/usr/bin/env python3
"""Capturas deste carrossel que exigem clique (o CLI do capturar.py não basta).

Rodar da raiz do repositório:
    python carrosseis/traducao-cardapio-presencial/capturar-telas.py

O que sai em imagens-puras/:
    05-cadastro-ingles.png     a linha do Nome com o inglês escrito, para o slide 5
    07-novidades-celular.png   a página de novidades no celular (CTA)

As telas do totem saem do `capturar-totem.py` da skill, que roda no totem de
exemplo. O tablet continua desenhado em CSS (`.tela-tablet`).
"""

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ / ".cursor" / "skills" / "carrossel-novidades" / "scripts"))

from capturar import esperar, limpar, sessao  # noqa: E402

PURAS = Path(__file__).resolve().parent / "imagens-puras"
PURAS.mkdir(exist_ok=True)

# As três bandeiras são os únicos elementos do modal com esta combinação de
# classes. Achá-las por texto não dá: são <img> sem alt de idioma, e o rótulo
# "Inglês" só aparece depois do clique.
BANDEIRAS = "[role='dialog'] [class*='rounded-full'][class*='p-0.5'][class*='transition-all']"


# O produto do exemplo é o mesmo que aparece no totem do slide 3, e a tradução
# gravada aqui é a mesma do `traducoes.json`. Assim o carrossel fecha: o slide 3
# mostra CHEDDAR & BACON FRIES na tela do cliente, e o slide 5 mostra o campo
# onde esse texto foi escrito.
PRODUTO = ("Acompanhamentos", "Batata frita com cheddar e bacon")
TRADUCAO = {
    1: ("CHEDDAR & BACON FRIES",
        "200 g portion of french fries with cheddar sauce and chopped bacon"),
    2: ("PAPAS CON CHEDDAR Y TOCINO",
        "Porción de 200 g de papas fritas con salsa de cheddar y tocino picado"),
}


def abrir_produto(pagina) -> None:
    setor, produto = PRODUTO
    pagina.get_by_text(setor, exact=True).first.click()
    esperar(pagina)
    pagina.get_by_text(produto, exact=True).first.click()
    esperar(pagina)
    limpar(pagina)

    bandeiras = pagina.locator(BANDEIRAS)
    if bandeiras.count() != 3:
        raise SystemExit(
            f"ERRO: achei {bandeiras.count()} bandeiras, esperava 3. Se achou "
            "zero, a empresa do sandbox perdeu o Totem/Tablet do contrato — "
            "sem um dos dois o recurso não aparece.")


def gravar_traducao() -> None:
    """Escreve inglês e espanhol no produto do sandbox.

    O sandbox só tinha tradução na Coca Cola, e refrigerante não combinava com
    o cardápio que o carrossel mostra. Em vez de fotografar o produto errado,
    cadastrei a tradução do produto certo: é escrita no sandbox, não montagem.
    """
    with sessao("painel") as pagina:
        pagina.goto("https://beefood.app/cardapio", wait_until="domcontentloaded",
                    timeout=90000)
        esperar(pagina)
        limpar(pagina)
        abrir_produto(pagina)

        for indice, (nome, descricao) in TRADUCAO.items():
            pagina.locator(BANDEIRAS).nth(indice).click()
            esperar(pagina, espera_final=1500)
            pagina.fill("#nome", nome)
            pagina.fill("#descricao", descricao)
            print(f"--> bandeira {indice}: {nome}")

        pagina.click("text=SALVAR E SAIR (F2)")
        esperar(pagina)
        print("OK  tradução gravada")


def cadastro_em_ingles() -> None:
    """O print que sustenta o slide 5: a versão em inglês mora no mesmo produto.

    O recorte é a linha do Nome com o inglês selecionado — as três bandeiras, a
    etiqueta do idioma e o nome traduzido dentro do mesmo campo. Com o Brasil
    selecionado o print mostra o nome em português, que não prova nada.
    """
    with sessao("painel") as pagina:
        pagina.goto("https://beefood.app/cardapio", wait_until="domcontentloaded",
                    timeout=90000)
        esperar(pagina)
        limpar(pagina)
        abrir_produto(pagina)

        pagina.locator(BANDEIRAS).nth(1).click()
        esperar(pagina, espera_final=2000)

        # Recorte de ~464x186 px lógicos, medido nos elementos e não estimado: a
        # posição do modal muda com a largura da janela. Ele abre 20 px acima do
        # rótulo Nome e fecha 16 px abaixo do campo Setor, que é onde a tela tem
        # vão — corte no meio de campo parece defeito. A 904 px de exibição sai a
        # 1,95x, e o rótulo de 15 px da interface vira 29 px na arte.
        rotulo = pagina.locator("label", has_text="Nome").first.bounding_box()
        setor = pagina.get_by_role("combobox").first.bounding_box()
        x0, y0 = rotulo["x"] - 14, rotulo["y"] - 20
        altura = setor["y"] + setor["height"] + 16 - y0
        print(f"--> recorte {464}x{round(altura)} em x={round(x0)}, y={round(y0)}")

        pagina.screenshot(path=str(PURAS / "05-cadastro-ingles.png"), type="png",
                          clip={"x": x0, "y": y0, "width": 464, "height": altura})
        print("OK  05-cadastro-ingles.png")


def novidades_no_celular() -> None:
    with sessao("celular", publico=True) as pagina:
        pagina.goto("https://beefood.app/novidades", wait_until="networkidle",
                    timeout=90000)
        esperar(pagina)
        pagina.screenshot(path=str(PURAS / "07-novidades-celular.png"), type="png")
        print("OK  07-novidades-celular.png")


if __name__ == "__main__":
    gravar_traducao()
    cadastro_em_ingles()
    novidades_no_celular()
