"""Ensaio: o `venda2/salvar` aceita `origem` de marketplace?

O painel mostra o ícone do canal no cartão, então o manual precisa de pedido de
iFood, Keeta e 99Food. A pergunta é se a rota que a tela `/delivery` usa para
criar pedido aceita esses campos ou se ela os ignora.

O ensaio manda o mesmo pedido com os campos de marketplace em **três posições**
(raiz, dentro de `delivery` e dentro de `cliente`), lê o registro de volta pelo
`vendaDetalhes` e cancela no fim. Nada fica no ambiente.

    python exp_origem.py            # cria, lê e cancela
    python exp_origem.py manter     # cria e lê, sem cancelar
"""
from __future__ import annotations

import json
import sys
from datetime import datetime

from playwright.sync_api import sync_playwright

from beefood import abrir, api_get, api_post
from smoketeste import ENDERECO, P, conferir_alvo

MARCADOR = "[ENSAIO-ORIGEM]"

# Tudo o que um pedido de iFood tem de diferente, conforme o `diagnostico.py`.
MARKETPLACE = {
    "origem": "iFood",
    "marketPlace": True,
    "ifoodShortReference": "9911 - Coleta 4242",
    "ifoodLocalizer": "48731999",
    "correlationId": "a1b2c3d4-0000-4444-8888-999900001111",
    "keetaId": None,
    "nnID": None,
}

CAMPOS_LIDOS = [
    "preVendaID", "origem", "marketPlace", "ifoodShortReference", "ifoodLocalizer",
    "correlationId", "keetaId", "nnID", "situacaoDelivery", "tipoPedido",
    "dataHoraPedido", "dataHoraAguardando", "horaCadastro", "observacoes",
]


def payload(s: dict) -> dict:
    agora = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    pid, nome, preco = P["one_burger"]
    corpo = {
        "preVendaID": None,
        "numeroPreVenda": None,
        "esteira": False,
        "empresaID": s["empresaID"],
        "filialID": s["filialID"],
        "filialIDOrigem": None,
        "usuarioID": s["usuarioID"],
        "funcionarioID": None,
        "tipo": "DELIVERY",
        "situacao": "ABERTO",
        "nomeAvulso": None,
        "obsx": f"{MARCADOR} {datetime.now():%d/%m %H:%M}",
        "pdvImprimirCozinhaAposPagamento": False,
        "delivery": {
            "situacaoDelivery": "PREPARO",
            "tipoPedido": "DELIVERY",
            "agendamento": None,
            "funcionarioID": None,
            "tipoPagStr": "PAGO ONLINE",
            "tipoPagBandeiraStr": None,
            "troco": None,
            # posição 2: dentro do objeto de delivery
            **MARKETPLACE,
        },
        "mesa": None,
        "produtos": [{
            "preVendaServicoID": None,
            "preVendaID": None,
            "usuarioID": s["usuarioID"],
            "produtoID": pid,
            "qtd": 1.0,
            "custo": 0,
            "venda": preco,
            "descricao": nome,
            "obsVenda": None,
            "semTaxaServico": False,
            "dataHoraLancamento": agora,
            "impresso": None,
            "mobile": True,
            "valorOpcoes": 0,
        }],
        "valores": {
            "produtos": preco,
            "acrescimo": 0,
            "taxaEntrega": 8.0,
            "valorEntregador": 0,
            "taxaServico": {"tipo": "R$", "valor": 0, "total": 0},
            "desconto": {"tipo": "R$", "valor": 0},
            "valorTotal": round(preco + 8.0, 2),
            "valorPago": 0,
        },
        "cliente": {
            "clienteID": None,
            "nome": "Ensaio Origem",
            "cpf_cnpj": None,
            "telefone": None,
            "endereco": dict(ENDERECO),
            # posição 3: junto do cliente
            **MARKETPLACE,
        },
        # posição 1: na raiz
        **MARKETPLACE,
    }
    return corpo



if __name__ == "__main__":
    manter = len(sys.argv) > 1 and sys.argv[1] == "manter"
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

        st, resp = api_post(page, "/api/venda2/salvar", payload(s))
        print("salvar", st, json.dumps(resp, ensure_ascii=False)[:400])

        pre = None
        if isinstance(resp, dict):
            pre = resp.get("preVendaID") or (resp.get("venda") or {}).get("preVendaID")
        if not pre:
            _, lista = api_get(
                page,
                f"/api/venda2/delivery/{s['empresaID']}/{s['filialID']}/{s['usuarioID']}/1",
            )
            if isinstance(lista, list) and lista:
                pre = max(x["preVendaID"] for x in lista)
        print("preVendaID", pre)

        st, det = api_get(
            page, f"/api/venda2/vendaDetalhes/{s['empresaID']}/{s['usuarioID']}/{pre}/0"
        )
        venda = (det or {}).get("venda") or {}
        print("\n== o que o servidor gravou ==")
        print(json.dumps({k: venda.get(k) for k in CAMPOS_LIDOS}, ensure_ascii=False, indent=2))

        if not manter:
            st, r = api_post(page, "/api/venda2/atualizaSituacaoDelivery", {
                "empresaID": s["empresaID"], "filialID": s["filialID"],
                "usuarioID": s["usuarioID"], "usuario": s["usuario"],
                "clienteID": venda.get("clienteID"),
                "situacaoDelivery": "CANCELADO",
                "situacaoDeliveryAnterior": venda.get("situacaoDelivery"),
                "preVendaID": pre, "numeroPreVenda": venda.get("numeroPreVenda"),
                "numeroPedido": venda.get("numeroPedido") or 0,
                "tipoPedido": "DELIVERY",
                "motivoCancelamento": "Ensaio de origem do manual",
                "tipo": "DELIVERY", "esteira": False,
            })
            print("\ncancelado", st, json.dumps(r, ensure_ascii=False)[:160])

        browser.close()
