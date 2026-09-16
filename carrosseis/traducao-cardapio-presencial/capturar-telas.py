#!/usr/bin/env python3
"""Capturas deste carrossel que exigem clique (o CLI do capturar.py não basta).

Rodar da raiz do repositório:
    python carrosseis/traducao-cardapio-presencial/capturar-telas.py

O que sai em imagens-puras/:
    05-cadastro-bandeiras.png  modal da Coca Cola 350ml com as três bandeiras
    05-cadastro-recorte.png    a faixa do Nome, para o realce do slide 5
    07-novidades-celular.png   a página de novidades no celular (CTA)

Totem e tablet não entram aqui: rodam em Android, não sobem no Cloud Agent
(`MEMORIA-GERAL.md`, seção 6) e por isso são desenhados em CSS nos slides, com
`.selo-ilustracao`.
"""

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ / ".cursor" / "skills" / "carrossel-novidades" / "scripts"))

from capturar import esperar, limpar, sessao  # noqa: E402

PURAS = Path(__file__).resolve().parent / "imagens-puras"
PURAS.mkdir(exist_ok=True)

VIEWPORT = (1440, 900)

# As três bandeiras são os únicos elementos do modal com esta combinação de
# classes. Achá-las por texto não dá: são <img> sem alt de idioma, e o rótulo
# "Inglês" só aparece depois do clique.
BANDEIRAS = "[role='dialog'] [class*='rounded-full'][class*='p-0.5'][class*='transition-all']"


def recorte(x0: float, y0: float, x1: float, y1: float) -> dict:
    largura, altura = VIEWPORT
    return {"x": round(x0 * largura), "y": round(y0 * altura),
            "width": round((x1 - x0) * largura), "height": round((y1 - y0) * altura)}


def cadastro_com_bandeiras() -> None:
    """O print que sustenta o slide 5: a tradução mora no mesmo cadastro.

    Fica no Brasil selecionado de propósito. Com o inglês selecionado a tela
    mostra a etiqueta "Inglês" e o campo destacado, que é linguagem de manual —
    aqui o que interessa é a linha do Nome com as três bandeiras e as bolinhas
    verdes, que é o que responde "não, você não mantém dois cardápios".
    """
    with sessao("painel") as pagina:
        pagina.goto("https://beefood.app/cardapio", wait_until="domcontentloaded",
                    timeout=90000)
        esperar(pagina)
        limpar(pagina)

        # O sandbox tem dois produtos com este nome (um com Preço Programado);
        # o primeiro é o do setor Bebidas, que é o do manual.
        pagina.get_by_text("Coca Cola 350ml", exact=True).first.click()
        esperar(pagina)
        limpar(pagina)

        bandeiras = pagina.locator(BANDEIRAS)
        if bandeiras.count() != 3:
            raise SystemExit(
                f"ERRO: achei {bandeiras.count()} bandeiras, esperava 3. Se achou "
                "zero, a empresa do sandbox perdeu o Totem/Tablet do contrato — "
                "sem um dos dois o recurso não aparece.")

        caixas = [b.bounding_box() for b in bandeiras.all()]
        print(f"--> bandeiras em x={[round(c['x']) for c in caixas]}, "
              f"y={round(caixas[0]['y'])}")

        # Recorte de 464x180 px lógicos: a 904 px de exibição sai a 1,95x, e o
        # rótulo de 15 px da interface vira 29 px na arte. As bordas caem em vão:
        # à direita, no espaço entre o campo Setor (acaba em 876) e a Etiqueta
        # (começa em 892) — cortar a Etiqueta pela metade parecia defeito.
        pagina.screenshot(path=str(PURAS / "05-cadastro-bandeiras.png"), type="png",
                          clip=recorte(420 / 1440, 160 / 900, 884 / 1440, 340 / 900))
        print("OK  05-cadastro-bandeiras.png")


def novidades_no_celular() -> None:
    with sessao("celular", publico=True) as pagina:
        pagina.goto("https://beefood.app/novidades", wait_until="networkidle",
                    timeout=90000)
        esperar(pagina)
        pagina.screenshot(path=str(PURAS / "07-novidades-celular.png"), type="png")
        print("OK  07-novidades-celular.png")


if __name__ == "__main__":
    cadastro_com_bandeiras()
    novidades_no_celular()
