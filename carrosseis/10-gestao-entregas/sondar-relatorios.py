#!/usr/bin/env python3
"""Fotografa os dois relatórios de entrega de cima a baixo, para escolher o corte.

Os relatórios vivem num iframe de `relatorios.beefood.com.br` e são mais altos
que a tela. Este script rola a área de conteúdo do iframe e guarda uma tira por
rolagem em `sonda/`, que é o material para decidir onde cada slide corta — a
sandbox tem número de verdade em alguns cartões e `Poucos pedidos` em outros.

    python sondar-relatorios.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(".cursor/skills/carrossel/scripts")
from capturar import esperar, limpar, sessao  # noqa: E402

PASTA = Path(__file__).resolve().parent
SONDA = PASTA / "sonda"
DESEMPENHO = "https://beefood.app/desempenho"

RELATORIOS = {
    "operacao": "Operação de Entrega",
    "entregador": "Entregador (Taxa / KM)",
}


def rolar(pagina, quanto: int) -> None:
    """Rola o miolo do relatório com a roda do mouse.

    O iframe é de outro domínio (`relatorios.beefood.com.br`), então
    `contentDocument` é `null` e não há como mexer no `scrollTop` de dentro. A
    roda do mouse atravessa a fronteira porque é evento de navegador.
    """
    pagina.mouse.move(1000, 600)
    pagina.mouse.wheel(0, quanto)


def main() -> None:
    SONDA.mkdir(parents=True, exist_ok=True)
    with sessao() as pagina:
        for nome, item in RELATORIOS.items():
            pagina.goto(DESEMPENHO)
            esperar(pagina, 9000)
            limpar(pagina)
            quadro = pagina.frame_locator("iframe")
            quadro.locator('button:has-text("Delivery")').first.click()
            pagina.wait_for_timeout(1500)
            quadro.locator(f'button:has-text("{item}")').first.click()
            pagina.wait_for_timeout(9000)

            for tira in range(5):
                destino = SONDA / f"{nome}-{tira}.png"
                pagina.screenshot(path=str(destino), type="png")
                print("·", destino.name)
                rolar(pagina, 500)
                pagina.wait_for_timeout(1200)


if __name__ == "__main__":
    main()
