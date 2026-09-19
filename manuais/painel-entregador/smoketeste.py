"""Smoke teste do #120 — monta o cenário do Painel para Entregadores na sandbox.

O painel só mostra pedido de **delivery** nas situações **PREPARO** e **PRONTO**, das
últimas **6 horas** (`useDeliveryPedidos(..., 6)`). Num sandbox parado a tela abre
vazia, então o cenário é montado aqui, sempre pelas mesmas rotas que o próprio
sistema usa quando o operador mexe na tela `/delivery`:

    POST /api/venda2/salvar                    cria o pedido
    POST /api/venda2/atualizaSituacaoDelivery  move entre Preparo e Pronto

Comandos:

    python smoketeste.py estado       # o que o painel enxerga agora
    python smoketeste.py catalogo     # produtos e clientes disponíveis
    python smoketeste.py ensaio       # monta os payloads e NÃO envia (técnica do ensaio)
    python smoketeste.py semear       # cria os pedidos do cenário
    python smoketeste.py situacao     # aplica Preparo/Pronto do cenário
    python smoketeste.py limpar       # cancela o que este script criou

Trava de segurança: só a sandbox 38311/39202. Qualquer outra empresa aborta.
"""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from datetime import datetime

from playwright.sync_api import sync_playwright

from beefood import abrir, api_get, api_post

EMPRESA_PERMITIDA = 38311
FILIAL_PERMITIDA = 39202

# Marcador nas observações: é por ele que `limpar` reconhece o que é deste script.
MARCADOR = "[SMOKE-PAINEL-ENTREGADOR]"

# Produtos reais do cardápio da sandbox (conferidos em `catalogo`).
P = {
    "one_burger": (2515371, "One Burger", 28.0),
    "crispy": (2515302, "Crispy Bbq", 36.0),
    "chicken": (2515303, "Chicken Deluxe", 29.0),
    "batata": (2515323, "Batata frita", 14.0),
    "aneis": (2515373, "Anéis de Cebola Empanada", 17.6),
    "coca": (2515308, "Coca Cola 350ml", 8.9),
    "cocazero": (2515311, "Coca Zero 350ml", 8.9),
    "milkshake": (2515382, "Milk Shake de Morango", 18.9),
    "brownie": (2515384, "Brownie", 11.9),
    "pudim": (2515385, "Pudim - Leite Condensado", 19.9),
}

# O cenário do manual: quatro origens, pedidos em preparo e prontos.
# `ref` é o identificador que o marketplace manda e que o cartão mostra embaixo do logo.
CENARIO = [
    {
        "apelido": "ifood-preparo",
        "origem": "iFood",
        "ref": "4821",
        "etapa": "PREPARO",
        "itens": [("one_burger", 1), ("batata", 1), ("coca", 2)],
        "pag": "PAGO ONLINE",
        "frete": 8.0,
    },
    {
        "apelido": "ifood-pronto",
        "origem": "iFood",
        "ref": "4817",
        "etapa": "PRONTO",
        "itens": [("crispy", 1), ("aneis", 1)],
        "pag": "PAGO ONLINE",
        "frete": 8.0,
    },
    {
        "apelido": "keeta-preparo",
        "origem": "Keeta",
        "ref": "K7204",
        "etapa": "PREPARO",
        "itens": [("chicken", 2), ("cocazero", 1)],
        "pag": "PAGO ONLINE",
        "frete": 9.9,
    },
    {
        "apelido": "99food-preparo",
        "origem": "99Food",
        "ref": "9F23",
        "etapa": "PREPARO",
        "itens": [("crispy", 1), ("milkshake", 1)],
        "pag": "PIX",
        "frete": 10.0,
    },
    {
        "apelido": "99food-pronto",
        "origem": "99Food",
        "ref": "9F19",
        "etapa": "PRONTO",
        "itens": [("one_burger", 1), ("brownie", 1)],
        "pag": "PIX",
        "frete": 10.0,
    },
    {
        "apelido": "cardapio-preparo",
        "origem": "Cardápio Digital",
        "ref": None,
        "etapa": "PREPARO",
        "itens": [("chicken", 1), ("batata", 1), ("pudim", 1)],
        "pag": "Dinheiro",
        "frete": 7.0,
    },
    {
        "apelido": "cardapio-pronto",
        "origem": "Cardápio Digital",
        "ref": None,
        "etapa": "PRONTO",
        "itens": [("one_burger", 2), ("coca", 2)],
        "pag": "Cartão de Crédito",
        "frete": 7.0,
    },
]

ENDERECO = {
    "clienteEnderecoID": None,
    "cep": "18085-000",
    "endereco": "Avenida Ipanema",
    "numero": "3000",
    "bairro": "Jardim Piratininga",
    "complemento": None,
    "cidade": "Sorocaba",
    "cidadeID": None,
    "estado": "SP",
    "estadoID": None,
    "latitude": None,
    "longitude": None,
    "km": None,
    "google_place_id": None,
}


def conferir_alvo(s: dict):
    if int(s["empresaID"]) != EMPRESA_PERMITIDA or int(s["filialID"]) != FILIAL_PERMITIDA:
        raise SystemExit(
            f"ABORTADO: alvo {s['empresaID']}/{s['filialID']} fora da sandbox "
            f"{EMPRESA_PERMITIDA}/{FILIAL_PERMITIDA}"
        )


def pedidos_da_janela(page, s: dict, horas: int = 6) -> list:
    st, lista = api_get(
        page, f"/api/venda2/delivery/{s['empresaID']}/{s['filialID']}/{s['usuarioID']}/{horas}"
    )
    if st != 200:
        raise SystemExit(f"listagem falhou: {st} {lista}")
    return lista if isinstance(lista, list) else []


def montar_payload(s: dict, caso: dict) -> dict:
    """JSON do `venda2/salvar`, no formato do `src/utils/pedidoBuilder.ts`."""
    agora = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    produtos, total = [], 0.0
    for chave, qtd in caso["itens"]:
        pid, nome, preco = P[chave]
        total += round(preco * qtd, 2)
        produtos.append({
            "preVendaServicoID": None,
            "preVendaID": None,
            "usuarioID": s["usuarioID"],
            "produtoID": pid,
            "qtd": float(qtd),
            "custo": 0,
            "venda": preco,
            "descricao": nome,
            "obsVenda": None,
            "semTaxaServico": False,
            "dataHoraLancamento": agora,
            "impresso": None,
            "mobile": True,
            "valorOpcoes": 0,
        })
    total = round(total, 2)
    frete = caso["frete"]

    pedido = {
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
        "obsx": f"{MARCADOR} {caso['apelido']} {datetime.now():%d/%m %H:%M}",
        "pdvImprimirCozinhaAposPagamento": False,
        "delivery": {
            # Nasce em Preparo; `situacao` move para Pronto depois, pela rota da tela.
            "situacaoDelivery": "PREPARO",
            "tipoPedido": "DELIVERY",
            "agendamento": None,
            "funcionarioID": None,
            "tipoPagStr": caso["pag"],
            "tipoPagBandeiraStr": None,
            "troco": None,
        },
        "mesa": None,
        "produtos": produtos,
        "valores": {
            "produtos": total,
            "acrescimo": 0,
            "taxaEntrega": frete,
            "valorEntregador": 0,
            "taxaServico": {"tipo": "R$", "valor": 0, "total": 0},
            "desconto": {"tipo": "R$", "valor": 0},
            "valorTotal": round(total + frete, 2),
            "valorPago": 0,
        },
        "cliente": {
            "clienteID": None,
            "nome": caso.get("cliente") or "Cliente de teste",
            "cpf_cnpj": None,
            "telefone": None,
            "endereco": dict(ENDERECO),
        },
        # Campos de marketplace. O `pedidoBuilder` do front não os manda (a origem
        # de verdade é gravada pela integração), então aqui eles são um teste:
        # `ensaio` mostra o payload e `semear` confere na listagem o que pegou.
        "origem": caso["origem"],
        "marketPlace": caso["origem"] != "Cardápio Digital",
    }
    if caso["origem"] == "iFood":
        pedido["ifoodShortReference"] = caso["ref"]
        pedido["correlationId"] = f"smoke-{caso['apelido']}"
    elif caso["origem"] == "Keeta":
        pedido["keetaId"] = caso["ref"]
    elif caso["origem"] == "99Food":
        pedido["nnID"] = caso["ref"]
        pedido["ifoodShortReference"] = caso["ref"]
    return pedido


def cmd_estado(page, s: dict):
    lista = pedidos_da_janela(page, s, 6)
    print(f"janela de 6 h: {len(lista)} pedidos")
    matriz = defaultdict(Counter)
    for p in lista:
        matriz[p.get("origem") or "(vazio)"][p.get("situacaoDelivery")] += 1
    for origem, cont in sorted(matriz.items()):
        print(f"  {origem:<20} {dict(cont)}")

    print("\n== o que o Painel para Entregadores mostraria ==")
    for etapa in ("PREPARO", "PRONTO"):
        alvo = [
            p for p in lista
            if str(p.get("tipoPedido") or "").upper() == "DELIVERY"
            and str(p.get("situacaoDelivery") or "").upper() == etapa
        ]
        print(f"  {etapa}: {len(alvo)}")
        for p in alvo:
            print(
                f"     #{p.get('numeroPedido') or p.get('numeroPreVenda')}"
                f"  origem={str(p.get('origem')):<18}"
                f"  ref={p.get('ifoodShortReference') or p.get('keetaId') or p.get('nnID')}"
                f"  preVendaID={p['preVendaID']}"
            )


def cmd_catalogo(page, s: dict):
    st, prods = api_get(
        page,
        f"/api/produto2/cardapio/produtos/{s['empresaID']}/{s['filialID']}/{s['usuarioID']}",
    )
    lista = prods if isinstance(prods, list) else (prods or {}).get("produtos") or []
    print("produtos", st, "n =", len(lista))
    for p in lista:
        if isinstance(p, dict) and p.get("ativo"):
            print(
                "  ", p.get("produtoID"), "|", p.get("descricao"),
                "| venda", p.get("venda"), "| combo", p.get("combo"),
            )


def cmd_ensaio(s: dict):
    print("ENSAIO — nada é enviado. Payload de cada pedido do cenário:\n")
    for caso in CENARIO:
        print("---", caso["apelido"], "---")
        print(json.dumps(montar_payload(s, caso), ensure_ascii=False, indent=2))


def cmd_semear(page, s: dict, apelidos: list[str] | None = None):
    antes = {p["preVendaID"] for p in pedidos_da_janela(page, s, 6)}
    criados = []
    for caso in CENARIO:
        if apelidos and caso["apelido"] not in apelidos:
            continue
        st, resp = api_post(page, "/api/venda2/salvar", montar_payload(s, caso))
        ok = st == 200 and not (isinstance(resp, dict) and resp.get("resultado") is False)
        print(f"{caso['apelido']:<18} {st} {'OK' if ok else 'FALHOU'} {json.dumps(resp, ensure_ascii=False)[:260]}")
        if ok:
            criados.append(caso["apelido"])
    print(f"\n{len(criados)} de {len(CENARIO)} enviados")

    print("\n== conferência na listagem (o que a API devolveu de verdade) ==")
    depois = pedidos_da_janela(page, s, 6)
    for p in depois:
        if p["preVendaID"] in antes:
            continue
        print(
            f"  preVendaID={p['preVendaID']}"
            f"  nº {p.get('numeroPedido')} ({p.get('numeroPreVenda')})"
            f"  origem={str(p.get('origem')):<18}"
            f"  marketPlace={p.get('marketPlace')}"
            f"  ifoodShortReference={p.get('ifoodShortReference')}"
            f"  keetaId={p.get('keetaId')}  nnID={p.get('nnID')}"
            f"  situacao={p.get('situacaoDelivery')}"
        )


def cmd_situacao(page, s: dict):
    """Move para PRONTO os pedidos do cenário que devem aparecer prontos."""
    prontos = {c["apelido"] for c in CENARIO if c["etapa"] == "PRONTO"}
    lista = pedidos_da_janela(page, s, 6)
    st_det = {}
    for p in lista:
        if str(p.get("situacaoDelivery")).upper() != "PREPARO":
            continue
        _, det = api_get(
            page, f"/api/venda2/vendaDetalhes/{s['empresaID']}/{s['usuarioID']}/{p['preVendaID']}/0"
        )
        obs = ((det or {}).get("venda") or {}).get("observacoes") or ""
        if MARCADOR not in obs:
            continue
        apelido = obs.replace(MARCADOR, "").strip().split()[0]
        st_det[p["preVendaID"]] = (p, apelido)

    for pid, (p, apelido) in st_det.items():
        if apelido not in prontos:
            continue
        corpo = {
            "empresaID": s["empresaID"],
            "filialID": s["filialID"],
            "usuarioID": s["usuarioID"],
            "usuario": s["usuario"],
            "clienteID": p.get("clienteID"),
            "situacaoDelivery": "PRONTO",
            "situacaoDeliveryAnterior": p.get("situacaoDelivery"),
            "preVendaID": pid,
            "numeroPreVenda": p.get("numeroPreVenda"),
            "numeroPedido": p.get("numeroPedido") or 0,
            "tipoPedido": p.get("tipoPedido"),
            "correlationId": p.get("correlationId"),
            "nnID": p.get("nnID"),
            "keetaId": p.get("keetaId"),
            "tipoPagStr": p.get("tipoPagStr"),
            "filialIDOrigem": p.get("filialIDOrigem"),
            "consumoLocal": p.get("consumoLocal"),
            "tipo": "DELIVERY",
            "esteira": False,
        }
        st, resp = api_post(page, "/api/venda2/atualizaSituacaoDelivery", corpo)
        print(f"  {apelido:<18} {pid} -> PRONTO  {st} {json.dumps(resp, ensure_ascii=False)[:180]}")


def cmd_limpar(page, s: dict):
    """Cancela os pedidos com o marcador deste script."""
    lista = pedidos_da_janela(page, s, 24)
    alvo = []
    for p in lista:
        if str(p.get("situacaoDelivery")).upper() in ("CANCELADO", "ENTREGUE"):
            continue
        _, det = api_get(
            page, f"/api/venda2/vendaDetalhes/{s['empresaID']}/{s['usuarioID']}/{p['preVendaID']}/0"
        )
        obs = ((det or {}).get("venda") or {}).get("observacoes") or ""
        if MARCADOR in obs:
            alvo.append(p)
    print(f"{len(alvo)} pedidos deste script para cancelar")
    for p in alvo:
        corpo = {
            "empresaID": s["empresaID"],
            "filialID": s["filialID"],
            "usuarioID": s["usuarioID"],
            "usuario": s["usuario"],
            "clienteID": p.get("clienteID"),
            "situacaoDelivery": "CANCELADO",
            "situacaoDeliveryAnterior": p.get("situacaoDelivery"),
            "preVendaID": p["preVendaID"],
            "numeroPreVenda": p.get("numeroPreVenda"),
            "numeroPedido": p.get("numeroPedido") or 0,
            "tipoPedido": p.get("tipoPedido"),
            "motivoCancelamento": "Limpeza do smoke teste do manual",
            "tipo": "DELIVERY",
            "esteira": False,
        }
        st, resp = api_post(page, "/api/venda2/atualizaSituacaoDelivery", corpo)
        print(f"  {p['preVendaID']} -> CANCELADO {st} {json.dumps(resp, ensure_ascii=False)[:160]}")


if __name__ == "__main__":
    comando = sys.argv[1] if len(sys.argv) > 1 else "estado"
    with sync_playwright() as p:
        browser, ctx, page = abrir(p, "/delivery")
        bruto = page.evaluate("() => JSON.parse(localStorage.getItem('beefood_user_session') || '{}')")
        s = {
            "empresaID": bruto.get("empresaID"),
            "filialID": bruto.get("filialID"),
            "usuarioID": bruto.get("usuarioID"),
            "usuario": bruto.get("usuario") or bruto.get("nome") or "Principal",
            "funcionarioID": bruto.get("funcionarioID"),
        }
        conferir_alvo(s)
        print("SESSAO", json.dumps(s, ensure_ascii=False), "\n")

        if comando == "estado":
            cmd_estado(page, s)
        elif comando == "catalogo":
            cmd_catalogo(page, s)
        elif comando == "ensaio":
            cmd_ensaio(s)
        elif comando == "semear":
            cmd_semear(page, s, sys.argv[2:] or None)
        elif comando == "situacao":
            cmd_situacao(page, s)
        elif comando == "limpar":
            cmd_limpar(page, s)
        else:
            print("comando desconhecido:", comando)
        browser.close()
