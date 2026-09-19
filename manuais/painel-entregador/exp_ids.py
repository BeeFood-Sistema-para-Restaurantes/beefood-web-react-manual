"""Ensaio: `origem` é derivada dos identificadores de plataforma?

A pista veio do script da sessão de Gestão de Entregas (`smoke-app.js`): a lista de
colunas que ele grava em `_PreVenda` tem `ifoodLocalizer`, `nnID`, `keetaId` e
`marketPlace` — e **não tem `origem`**. Ainda assim os pedidos que ele montou
aparecem na API como `origem: "iFood"`, `"99Food"` e `"Keeta"`.

Conclusão a testar: `origem` não é coluna gravada, é **derivada** —
`ifoodLocalizer` → iFood, `nnID` → 99Food, `keetaId` → Keeta, `aiqfomeId` → AIQFome,
`filialIDOrigem` → Cardápio Digital, nada → Manual.

O que combina com o que a base mostra:

| Pedido da base | Identificador | `origem` |
|---|---|---|
| 59567509 | `ifoodLocalizer` 48731502 | iFood |
| 59567521 | `nnID` 5764687241800647938 | 99Food |
| 59587145 | `keetaId` 4900112233445566 | Keeta |
| 58903154 | `filialIDOrigem` 39202 | Cardápio Digital |

Se a regra é essa, basta **gravar o identificador** para o painel mostrar o ícone do
canal. Este ensaio procura uma rota autenticada que grave esses campos: manda cada
candidata com o identificador e relê o pedido.

    python exp_ids.py               # usa um pedido Manual da janela
    python exp_ids.py 59616499      # um preVendaID específico
"""
from __future__ import annotations

import json
import sys

from playwright.sync_api import sync_playwright

from beefood import abrir, api_get, api_post
from smoketeste import conferir_alvo

LIDOS = [
    "origem", "marketPlace", "ifoodLocalizer", "ifoodShortReference",
    "correlationId", "nnID", "keetaId", "aiqfomeId", "filialIDOrigem",
    "situacaoDelivery",
]

# Os identificadores de teste usados na sondagem. São fictícios e não existem do outro
# lado: pedido assim nunca deve ser finalizado pelo app, porque a baixa tentaria avisar
# a plataforma de verdade (aviso herdado do `smoke-app.js`).
MARCA = {
    "ifoodLocalizer": "48739120",
    "ifoodShortReference": "4821 - Coleta 7312",
    "correlationId": "5f21a7c4-9b30-4d6e-8a15-73c0e2b41d99",
    "marketPlace": True,
}


def ler(page, s, pre):
    _, det = api_get(
        page, f"/api/venda2/vendaDetalhes/{s['empresaID']}/{s['usuarioID']}/{pre}/0"
    )
    venda = (det or {}).get("venda") or {}
    return {k: venda.get(k) for k in LIDOS}, venda


def candidatas(s, venda, pre):
    """Rotas autenticadas que já recebem esses campos ou que poderiam gravá-los."""
    base = {
        "empresaID": s["empresaID"], "filialID": s["filialID"],
        "usuarioID": s["usuarioID"], "usuario": s["usuario"],
        "preVendaID": pre, "numeroPreVenda": venda.get("numeroPreVenda"),
        "numeroPedido": venda.get("numeroPedido") or 0,
        "tipoPedido": venda.get("tipoPedido") or "DELIVERY",
        "tipo": "DELIVERY",
    }
    return [
        # A rota do kanban já declara nnID/keetaId/correlationId no seu contrato
        # (`useAtualizarSituacaoDelivery.ts`). A pergunta é se ela **grava** ou só repassa.
        ("venda2/atualizaSituacaoDelivery", {
            **base, "esteira": False,
            "clienteID": venda.get("clienteID"),
            "situacaoDelivery": venda.get("situacaoDelivery"),
            "situacaoDeliveryAnterior": venda.get("situacaoDelivery"),
            **MARCA,
        }),
        ("venda2/atualizaCardapio", {**base, **MARCA}),
        ("venda2/atualizaDocumento", {**base, **MARCA}),
        ("venda2/atualizaTipoPedido", {**base, **MARCA}),
        ("venda2/atualizaObs", {**base, "obs": "ensaio de identificador", **MARCA}),
        ("venda2/salvarValores", {**base, **MARCA}),
    ]


if __name__ == "__main__":
    with sync_playwright() as p:
        browser, ctx, page = abrir(p, "/delivery")
        bruto = page.evaluate("() => JSON.parse(localStorage.getItem('beefood_user_session') || '{}')")
        s = {
            "empresaID": bruto.get("empresaID"),
            "filialID": bruto.get("filialID"),
            "usuarioID": bruto.get("usuarioID"),
            "usuario": bruto.get("usuario") or "Principal",
        }
        conferir_alvo(s)

        if len(sys.argv) > 1:
            pre = int(sys.argv[1])
        else:
            _, lista = api_get(
                page,
                f"/api/venda2/delivery/{s['empresaID']}/{s['filialID']}/{s['usuarioID']}/6",
            )
            alvo = [
                x for x in (lista if isinstance(lista, list) else [])
                if (x.get("origem") or "") == "Manual"
                and str(x.get("situacaoDelivery")).upper() in ("PREPARO", "PRONTO")
            ]
            if not alvo:
                raise SystemExit("nenhum pedido Manual na janela para o ensaio")
            pre = alvo[0]["preVendaID"]
        print("alvo preVendaID", pre)

        antes, venda = ler(page, s, pre)
        print("antes ", json.dumps(antes, ensure_ascii=False))

        for rota, corpo in candidatas(s, venda, pre):
            st, resp = api_post(page, f"/api/{rota}", corpo)
            depois, _ = ler(page, s, pre)
            mudou = {k: v for k, v in depois.items() if antes.get(k) != v}
            print(f"\n{rota}: {st} {json.dumps(resp, ensure_ascii=False)[:120]}")
            print(f"   mudou: {json.dumps(mudou, ensure_ascii=False) if mudou else 'nada'}")
            if mudou:
                antes = depois

        browser.close()
