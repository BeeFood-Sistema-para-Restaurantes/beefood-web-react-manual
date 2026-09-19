"""Prazos do delivery — a base do alerta de atraso do painel.

O cartão fica amarelo em 70% do prazo, laranja em 85% e vermelho quando passa
(`src/utils/deliveryAtraso.ts`). O prazo de um pedido de DELIVERY é o
`deliveryTempoEntregaMinutosMax`. Este script imprime os três campos e, para
cada pedido da janela, quantos minutos faltam para cada virada de cor — é o que
permite programar a captura em vez de esperar no escuro.

    python prazo.py
"""
from __future__ import annotations

import json
from datetime import datetime

from playwright.sync_api import sync_playwright

from beefood import abrir, api_get
from smoketeste import conferir_alvo

CAMPOS = [
    "deliveryTempoEntregaMinutos",
    "deliveryTempoEntregaMinutosMax",
    "deliveryTempoRetiradaMinutos",
]
LIMIARES = (("amarelo", 0.70), ("laranja", 0.85), ("vermelho", 1.00))


def minutos_desde(texto: str | None) -> float | None:
    if not texto:
        return None
    base = datetime(
        int(texto[0:4]), int(texto[5:7]), int(texto[8:10]),
        int(texto[11:13]), int(texto[14:16]),
    )
    return (datetime.now() - base).total_seconds() / 60


if __name__ == "__main__":
    with sync_playwright() as p:
        browser, ctx, page = abrir(p, "/delivery")
        bruto = page.evaluate("() => JSON.parse(localStorage.getItem('beefood_user_session') || '{}')")
        s = {
            "empresaID": bruto.get("empresaID"),
            "filialID": bruto.get("filialID"),
            "usuarioID": bruto.get("usuarioID"),
        }
        conferir_alvo(s)

        st, cab = api_get(
            page,
            f"/api/empresaDelivery2/cabecalhoDelivery/{s['empresaID']}/{s['filialID']}/{s['usuarioID']}",
        )
        cfg = cab if isinstance(cab, dict) else {}
        print("cabecalhoDelivery", st)
        print(json.dumps({k: cfg.get(k) for k in CAMPOS}, ensure_ascii=False, indent=2))
        prazo = cfg.get("deliveryTempoEntregaMinutosMax") or cfg.get("deliveryTempoEntregaMinutos")
        print(f"\nprazo de DELIVERY usado pelo alerta: {prazo} min")
        if prazo:
            for nome, pct in LIMIARES:
                print(f"  {nome:<9} a partir de {round(prazo * pct)} min do pedido")

        _, lista = api_get(
            page, f"/api/venda2/delivery/{s['empresaID']}/{s['filialID']}/{s['usuarioID']}/6"
        )
        print("\n== pedidos da janela e a cor de cada um ==")
        for pd in lista if isinstance(lista, list) else []:
            situacao = str(pd.get("situacaoDelivery") or "").upper()
            if situacao not in ("PREPARO", "PRONTO"):
                continue
            idade = minutos_desde(pd.get("dataHoraPedido") or pd.get("dataVenda"))
            if idade is None or not prazo:
                continue
            pct = idade / prazo
            cor = "sem alerta"
            for nome, limite in LIMIARES:
                if pct >= limite:
                    cor = nome
            faltam = {
                nome: round(prazo * limite - idade)
                for nome, limite in LIMIARES
                if prazo * limite > idade
            }
            print(
                f"  {pd['preVendaID']} {situacao:<8} {str(pd.get('origem')):<18}"
                f" {round(idade)} min ({pct:.0%})  cor={cor:<10} faltam={faltam}"
            )

        browser.close()
