"""Ensaio: o que define a janela de 6 h do painel?

O painel chama `useDeliveryPedidos(..., 6)`, e a sandbox tem pedidos de iFood,
Keeta e 99Food criados de madrugada — fora da janela. Se a janela olhasse a
data da **etapa**, mover o pedido de situação o traria de volta e o manual
poderia mostrar o ícone de cada canal.

O ensaio pega um pedido de marketplace, passeia pelas situações e mede, depois
de cada passo, se ele entra na listagem de 6 h e o que mudou no registro.

    python exp_janela.py            # usa o primeiro pedido de marketplace
    python exp_janela.py 59567509   # um preVendaID específico
"""
from __future__ import annotations

import json
import sys

from playwright.sync_api import sync_playwright

from beefood import abrir, api_get, api_post
from smoketeste import conferir_alvo

DATAS = [
    "dataVenda", "horaCadastro", "dataPedido", "horaPedido",
    "dataHoraAguardando", "dataHoraEmPreparo", "dataHoraPronto",
]
ORIGENS_MARKETPLACE = ("iFood", "Keeta", "99Food")


def listar(page, s, horas):
    _, lista = api_get(
        page, f"/api/venda2/delivery/{s['empresaID']}/{s['filialID']}/{s['usuarioID']}/{horas}"
    )
    return lista if isinstance(lista, list) else []


def registro(page, s, pre):
    _, det = api_get(
        page, f"/api/venda2/vendaDetalhes/{s['empresaID']}/{s['usuarioID']}/{pre}/0"
    )
    return (det or {}).get("venda") or {}


def mover(page, s, venda, destino):
    corpo = {
        "empresaID": s["empresaID"], "filialID": s["filialID"],
        "usuarioID": s["usuarioID"], "usuario": s["usuario"],
        "clienteID": venda.get("clienteID"),
        "situacaoDelivery": destino,
        "situacaoDeliveryAnterior": venda.get("situacaoDelivery"),
        "preVendaID": venda["preVendaID"],
        "numeroPreVenda": venda.get("numeroPreVenda"),
        "numeroPedido": venda.get("numeroPedido") or 0,
        "tipoPedido": venda.get("tipoPedido"),
        "correlationId": venda.get("correlationId"),
        "nnID": venda.get("nnID"), "keetaId": venda.get("keetaId"),
        "tipoPagStr": venda.get("tipoPagStr"),
        "filialIDOrigem": venda.get("filialIDOrigem"),
        "consumoLocal": venda.get("consumoLocal"),
        "tipo": "DELIVERY", "esteira": False,
    }
    st, r = api_post(page, "/api/venda2/atualizaSituacaoDelivery", corpo)
    return st, r


def medir(page, s, pre, rotulo):
    venda = registro(page, s, pre)
    na_janela = any(p["preVendaID"] == pre for p in listar(page, s, 6))
    print(f"\n-- {rotulo} --")
    print(f"   situacao={venda.get('situacaoDelivery')}  origem={venda.get('origem')}")
    print(f"   na janela de 6 h: {'SIM' if na_janela else 'nao'}")
    print("   " + json.dumps({k: venda.get(k) for k in DATAS}, ensure_ascii=False))
    return venda, na_janela


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
            amplos = listar(page, s, 2000)
            alvo = [
                x for x in amplos
                if (x.get("origem") or "") in ORIGENS_MARKETPLACE
                and str(x.get("situacaoDelivery")).upper() not in ("CANCELADO", "ENTREGUE")
            ]
            if not alvo:
                raise SystemExit("nenhum pedido de marketplace disponivel")
            pre = alvo[0]["preVendaID"]
        print("alvo preVendaID", pre)

        venda, _ = medir(page, s, pre, "estado inicial")
        original = str(venda.get("situacaoDelivery") or "AGUARDANDO").upper()

        for destino in ("AGUARDANDO", "PREPARO", "PRONTO"):
            if str(venda.get("situacaoDelivery")).upper() == destino:
                continue
            st, r = mover(page, s, venda, destino)
            print(f"\n   mover -> {destino}: {st} {json.dumps(r, ensure_ascii=False)[:100]}")
            venda, _ = medir(page, s, pre, f"depois de {destino}")

        if str(venda.get("situacaoDelivery")).upper() != original:
            mover(page, s, venda, original)
            medir(page, s, pre, f"restaurado para {original}")

        browser.close()
