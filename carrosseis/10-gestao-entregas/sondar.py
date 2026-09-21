#!/usr/bin/env python3
"""Sonda o estado do sandbox antes de decidir a cena das capturas.

Grava o JSON do painel de Gestao de Entregas e um print cru da tela, para o
roteiro saber com o que esta lidando: quantos pedidos, quantas rotas, quantos
entregadores com posicao. Nada e escrito no servidor.

    python sondar.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.append(".cursor/skills/carrossel/scripts")
from capturar import esperar, limpar, sessao  # noqa: E402

PASTA = Path(__file__).resolve().parent
PAINEL = "https://beefood.app/gestao-entregas"


def main() -> None:
    coletado: dict = {}

    with sessao() as pagina:
        def guardar(resposta):
            url = resposta.url
            if "/entrega2/gestao/" in url:
                try:
                    coletado[url.split("/entrega2/gestao/")[1].split("/")[0]] = resposta.json()
                except Exception as erro:  # noqa: BLE001
                    coletado.setdefault("erros", []).append(f"{url}: {erro}")

        pagina.on("response", guardar)
        pagina.goto(PAINEL)
        esperar(pagina, 9000)
        limpar(pagina)
        pagina.screenshot(path=str(PASTA / "sonda-painel.png"), type="png")

    (PASTA / "sonda-painel.json").write_text(
        json.dumps(coletado, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    for chave, valor in coletado.items():
        if isinstance(valor, dict):
            print(chave, {k: (len(v) if isinstance(v, list) else v)
                          for k, v in valor.items() if k != "pedidos" or True})


if __name__ == "__main__":
    main()
