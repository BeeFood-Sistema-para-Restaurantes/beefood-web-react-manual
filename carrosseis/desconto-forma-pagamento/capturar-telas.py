#!/usr/bin/env python3
"""A unica captura nova deste carrossel: a pagina de novidades do CTA.

O resto da peca sai de `recortar.py`, que corta os prints de producao ja
versionados nos manuais #64 e #82.

A lista de `beefood.app/novidades` e ordenada por data, e esta publicacao e de
agosto: aberta na home, o celular mostra outra novidade e o CTA acaba com um
print falando de outro assunto. O script filtra o aplicativo Cardapio Digital e
rola ate o **titulo** desta publicacao encostar no cabecalho fixo — parando no
cartao inteiro, a data de publicacao entra na arte e **data o post**, que e o
que a `MEMORIA-CARROSSEIS.md` manda evitar.

Uso, da raiz do repositorio:
    python3 carrosseis/desconto-forma-pagamento/capturar-telas.py
"""

from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ / ".cursor/skills/carrossel-novidades/scripts"))

from capturar import sessao, esperar, limpar  # noqa: E402

SAIDA = Path(__file__).resolve().parent / "imagens-puras"
TITULO = "Desconto ou acréscimo por forma de pagamento"

# Altura do cabecalho fixo da pagina, em px logicos.
CABECALHO = 64


def pagina_de_novidades() -> None:
    with sessao("celular", publico=True) as pagina:
        pagina.goto("https://beefood.app/novidades",
                    wait_until="domcontentloaded", timeout=90000)
        esperar(pagina)
        limpar(pagina)

        pagina.click("button:has-text('Todos os aplicativos')")
        pagina.wait_for_timeout(1500)
        pagina.locator('[role="option"]').filter(
            has_text="Cardápio Digital").first.click()
        pagina.wait_for_timeout(2500)

        pagina.evaluate(
            """(dados) => {
              const titulo = [...document.querySelectorAll('h2, h3')]
                .find(e => (e.textContent || '').includes(dados.titulo));
              if (!titulo) throw new Error('cartão da novidade não encontrado');
              const y = titulo.getBoundingClientRect().top + window.scrollY;
              window.scrollTo(0, y - dados.cabecalho - dados.folga);
            }""",
            {"titulo": TITULO, "cabecalho": CABECALHO, "folga": 12})
        pagina.wait_for_timeout(1500)

        arquivo = SAIDA / "novidades-celular.png"
        pagina.screenshot(path=str(arquivo), type="png")
        print(f"OK  {arquivo.relative_to(RAIZ)}")


def main() -> int:
    SAIDA.mkdir(parents=True, exist_ok=True)
    pagina_de_novidades()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
