"""Procura a rota do ERP que grava `origem` de marketplace.

Duas rotas já foram medidas e nenhuma serve:

| Rota | Quem usa | `origem` que grava |
|---|---|---|
| `POST app3/api/venda2/salvar` | tela `/delivery` | sempre `Manual` (`exp_origem.py`) |
| `POST app/datasnap/rest/tmesa/pedido` | cardápio público | sempre `Cardápio Digital` |

Ou seja: a origem é decidida **pela rota**, não por campo do corpo. Então deve existir
uma terceira rota, a que as integrações chamam. Este ensaio procura por ela.

O corpo enviado é `{}` de propósito: rota que existe reclama de parâmetro, rota que não
existe devolve 404/501 — dá para mapear o ERP **sem criar pedido nenhum**.

    python exp_rotas_erp.py           # varre os candidatos
    python exp_rotas_erp.py sufixo    # tenta tmesa/pedido com parâmetro de caminho
"""
from __future__ import annotations

import json
import sys

from playwright.sync_api import sync_playwright

from beefood import abrir
from pedido_marketplace import ORIGEM_CARDAPIO, autorizacao

ERP = "https://app.beetechapi.be/datasnap/rest"

# Classe/método plausíveis para a entrada de pedido de plataforma. O padrão do DataSnap
# é `/datasnap/rest/<TClasse>/<Metodo>`, e as classes já vistas em produção são
# `tmesa` (pedido do cardápio), `tvenda` (fiscal) e `tempresaDelivery` (configuração).
CANDIDATOS = [
    "tmesa/pedidoMarketplace",
    "tmesa/pedidoMarketPlace",
    "tmesa/pedidoIfood",
    "tmesa/pedidoDelivery",
    "tmesa/pedidoPlataforma",
    "tmesa/pedidoIntegracao",
    "tmesa/pedidoExterno",
    "tmarketplace/pedido",
    "tmarketPlace/pedido",
    "tifood/pedido",
    "tintegracao/pedido",
    "tplataforma/pedido",
    "tdelivery/pedido",
    "tvenda/pedido",
    "tvenda/pedidoMarketplace",
    # A de controle: esta existe, e serve de régua para comparar as respostas.
    "tmesa/pedido",
]

# `validaDelivery/1` mostra que o ERP aceita parâmetro no caminho. Se `origem` for um
# parâmetro posicional do `pedido`, um desses sufixos muda o que ele grava.
SUFIXOS = ["", "/0", "/1", "/2", "/iFood", "/Keeta"]

# A resposta de erro do `tmesa/pedido` é do Node ("Cannot read properties of undefined"),
# e o 404 é o do Express — ou seja, `app.beetechapi.be/datasnap/rest/...` é o **mesmo
# backend Node**, só com o caminho legado do DataSnap. Então vale varrer também a família
# nova de rotas, `/api/<modulo>/<metodo>`, que é a que a tela usa.
FAMILIA_API = [
    "api/venda2/salvarMarketplace",
    "api/venda2/salvarMarketPlace",
    "api/venda2/pedidoMarketplace",
    "api/venda2/salvarDelivery",
    "api/venda2/salvarIntegracao",
    "api/venda2/importarPedido",
    "api/venda2/receberPedido",
    "api/marketplace2/pedido",
    "api/marketplace2/salvar",
    "api/marketplace/pedido",
    "api/ifood2/pedido",
    "api/ifood/pedido",
    "api/keeta2/pedido",
    "api/keeta/pedido",
    "api/integracao2/pedido",
    "api/pedido2/salvar",
    # Régua: esta existe (a tela usa).
    "api/venda2/salvar",
]


def sondar(page, caminho: str, corpo: dict, base: str = ERP):
    resp = page.request.post(
        f"{base}/{caminho}",
        headers={
            "Content-Type": "application/json",
            "Authorization": autorizacao(),
            "Origin": ORIGEM_CARDAPIO,
            "Referer": f"{ORIGEM_CARDAPIO}/",
        },
        data=json.dumps(corpo),
    )
    texto = (resp.text() or "").replace("\n", " ")[:220]
    print(f"  {resp.status:>4}  {caminho:<34} {texto}")
    return resp.status


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "classes"
    with sync_playwright() as p:
        browser, ctx, page = abrir(p, "/delivery")
        if modo == "sufixo":
            print("== tmesa/pedido com parametro de caminho (corpo vazio) ==")
            for sufixo in SUFIXOS:
                sondar(page, f"tmesa/pedido{sufixo}", {})
        elif modo == "api":
            for host in ("https://app.beetechapi.be", "https://app3.beetechapi.be"):
                print(f"\n== familia /api em {host} (corpo vazio) ==")
                for caminho in FAMILIA_API:
                    sondar(page, caminho, {}, base=host)
        else:
            print("== candidatos de rota (corpo vazio, nada e criado) ==")
            for caminho in CANDIDATOS:
                sondar(page, caminho, {})
        browser.close()
