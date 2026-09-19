"""Estuda os pedidos da empresa 38311 antes de montar o cenário do #104.

Responde três coisas, lendo a API de produção em vez de adivinhar pela tela:

1. quais `origem` existem hoje e quantos pedidos em cada `situacaoDelivery`;
2. o registro completo de um pedido de cada origem pedida (iFood, Keeta,
   99Food e Cardápio Digital), para copiar o formato no smoke teste;
3. os prazos do cabeçalho do delivery, que são a base do alerta de atraso.

    python diagnostico.py            # janela de 6 h (a mesma do painel)
    python diagnostico.py 720        # janela maior, para achar origem antiga
"""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict

from playwright.sync_api import sync_playwright

from beefood import abrir, api_get

ORIGENS_ALVO = ["iFood", "Keeta", "99Food", "Cardápio Digital"]

CAMPOS_CHAVE = [
    "preVendaID", "numeroPreVenda", "numeroPedido", "origem", "marketPlace",
    "ifoodShortReference", "keetaId", "nnID", "correlationId", "situacao",
    "situacaoDelivery", "tipoPedido", "consumoLocal", "dataHoraPedido",
    "dataHoraEmPreparo", "dataHoraPronto", "dataHoraRetirada", "nome",
    "telefone", "valorTotal", "valorFrete", "endereco", "clienteID",
    "filialID", "filialIDOrigem", "tipoPagStr",
]


def main(horas: int):
    with sync_playwright() as p:
        browser, ctx, page = abrir(p, "/delivery")
        s = page.evaluate("() => JSON.parse(localStorage.getItem('beefood_user_session') || '{}')")
        emp, fil, usr = s.get("empresaID"), s.get("filialID"), s.get("usuarioID")
        print("SESSAO", json.dumps({"empresaID": emp, "filialID": fil, "usuarioID": usr}))

        status, pedidos = api_get(page, f"/api/venda2/delivery/{emp}/{fil}/{usr}/{horas}")
        print("DELIVERY", status, "n =", len(pedidos) if isinstance(pedidos, list) else pedidos)
        if not isinstance(pedidos, list):
            browser.close()
            return

        por_origem = Counter(p_.get("origem") or "(vazio)" for p_ in pedidos)
        print("\n== ORIGENS (janela de", horas, "h) ==")
        for origem, n in por_origem.most_common():
            print(f"  {origem:<20} {n}")

        matriz = defaultdict(Counter)
        for p_ in pedidos:
            matriz[p_.get("origem") or "(vazio)"][p_.get("situacaoDelivery")] += 1
        print("\n== ORIGEM x SITUACAO ==")
        for origem, cont in matriz.items():
            print(f"  {origem:<20} {dict(cont)}")

        print("\n== TIPOPEDIDO x SITUACAO ==")
        tp = defaultdict(Counter)
        for p_ in pedidos:
            tp[p_.get("tipoPedido")][p_.get("situacaoDelivery")] += 1
        for k, cont in tp.items():
            print(f"  {k}: {dict(cont)}")

        print("\n== AMOSTRA POR ORIGEM ==")
        for origem in ORIGENS_ALVO:
            amostra = [p_ for p_ in pedidos if (p_.get("origem") or "") == origem]
            print(f"\n--- {origem} ({len(amostra)} na janela) ---")
            if not amostra:
                print("   nenhum pedido nesta janela")
                continue
            alvo = amostra[0]
            print(json.dumps({k: alvo.get(k) for k in CAMPOS_CHAVE}, ensure_ascii=False, indent=2))
            st, det = api_get(page, f"/api/venda2/vendaDetalhes/{emp}/{usr}/{alvo['preVendaID']}/0")
            print("   vendaDetalhes", st, "chaves:", list(det)[:20] if isinstance(det, dict) else type(det))
            if isinstance(det, dict):
                print(json.dumps(det, ensure_ascii=False)[:2500])

        print("\n== CABECALHO DELIVERY (prazos do alerta de atraso) ==")
        st, cab = api_get(page, f"/api/empresaDelivery2/cabecalhoDelivery/{emp}/{fil}/{usr}")
        print(st, json.dumps(cab, ensure_ascii=False)[:1500])

        browser.close()


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 6)
