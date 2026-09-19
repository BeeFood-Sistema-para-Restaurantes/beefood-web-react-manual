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
    python smoketeste.py semear          # cria todos os pedidos do cenário
    python smoketeste.py semear maduro   # só uma onda (ou um apelido)
    python smoketeste.py preparo         # move para Em preparo (sem ID = todos da janela)
    python smoketeste.py pronto 123      # move só esses preVendaID para Pronto
    python smoketeste.py arquivar 123    # tira do painel (volta a AGUARDANDO)
    python smoketeste.py limpar          # cancela o que este script criou

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

# Marcador nas observações: é por ele que `limpar` reconhece o que é deste script, e é
# a sentinela que o `marketplace-db.js` exige antes de gravar qualquer coluna no banco.
# Pedido de verdade não tem o marcador, então não há como o script alcançar um.
MARCADOR = "[SMOKE-PAINEL]"
# O primeiro lote do #120 saiu com o marcador antigo; `limpar` reconhece os dois.
MARCADORES = (MARCADOR, "[SMOKE-PAINEL-ENTREGADOR]")

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

# Pedidos lançados no balcão (telefone, WhatsApp) — a origem que sai é **Manual**,
# e o cartão do painel mostra o ícone da abelha. Os do **Cardápio Digital** vêm do
# `pedido_cardapio.py`, porque origem não é campo de entrada: ver `fluxo-codigo.md`.
#
# Os apelidos são agrupados em **ondas**, porque a cor do cartão depende da idade do
# pedido: o prazo do sandbox é de 53 min, e o alerta vira amarelo em 37 min, laranja
# em 45 e vermelho em 53 (`prazo.py` imprime a conta). Para a captura mostrar as três
# faixas, a onda `maduro` é semeada ~40 min antes e a `fresco` na hora.
CENARIO = [
    {
        "apelido": "maduro-1",
        "onda": "maduro",
        "cliente": "Marina Oliveira",
        "itens": [("crispy", 1), ("aneis", 1), ("cocazero", 1)],
        "pag": "Dinheiro",
        "frete": 6.5,
    },
    {
        "apelido": "maduro-2",
        "onda": "maduro",
        "cliente": "Rafael Dias",
        "itens": [("chicken", 2), ("batata", 1), ("coca", 2)],
        "pag": "Cartão de Crédito",
        "frete": 6.5,
    },
    {
        "apelido": "maduro-3",
        "onda": "maduro",
        "cliente": "Beatriz Lima",
        "itens": [("one_burger", 1), ("milkshake", 1)],
        "pag": "PIX",
        "frete": 6.5,
    },
    {
        "apelido": "fresco-1",
        "onda": "fresco",
        "cliente": "Paulo Sérgio Braga",
        "itens": [("crispy", 1), ("batata", 1), ("pudim", 1), ("coca", 1)],
        "pag": "Dinheiro",
        "frete": 6.5,
    },
    {
        "apelido": "fresco-2",
        "onda": "fresco",
        "cliente": "Helena Moraes",
        "itens": [("one_burger", 2), ("aneis", 1), ("cocazero", 2)],
        "pag": "PIX",
        "frete": 6.5,
    },
    {
        "apelido": "fresco-3",
        "onda": "fresco",
        "cliente": "Tiago Nunes",
        "itens": [("chicken", 1), ("brownie", 1)],
        "pag": "Cartão de Débito",
        "frete": 6.5,
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
    }
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


def cmd_semear(page, s: dict, alvos: list[str] | None = None):
    """`alvos` aceita apelido (`maduro-1`) ou nome de onda (`maduro`)."""
    antes = {p["preVendaID"] for p in pedidos_da_janela(page, s, 6)}
    criados = []
    for caso in CENARIO:
        if alvos and caso["apelido"] not in alvos and caso.get("onda") not in alvos:
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


def mover(page, s: dict, p: dict, destino: str):
    """Mesma rota que o operador aciona arrastando o cartão no kanban do Delivery."""
    corpo = {
        "empresaID": s["empresaID"],
        "filialID": s["filialID"],
        "usuarioID": s["usuarioID"],
        "usuario": s["usuario"],
        "clienteID": p.get("clienteID"),
        "situacaoDelivery": destino,
        "situacaoDeliveryAnterior": p.get("situacaoDelivery"),
        "preVendaID": p["preVendaID"],
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
    print(
        f"  {p['preVendaID']} {str(p.get('origem')):<18}"
        f" {p.get('situacaoDelivery')} -> {destino}  {st}"
        f" {json.dumps(resp, ensure_ascii=False)[:120]}"
    )


def cmd_mover(page, s: dict, destino: str, ids: list[str]):
    """`preparo`/`pronto`: sem IDs move todos os pedidos de delivery da janela."""
    alvos = {int(i) for i in ids} if ids else None
    for p in pedidos_da_janela(page, s, 6):
        if str(p.get("tipoPedido") or "").upper() != "DELIVERY":
            continue
        if str(p.get("situacaoDelivery") or "").upper() in ("CANCELADO", "ENTREGUE", destino):
            continue
        if alvos is not None and p["preVendaID"] not in alvos:
            continue
        mover(page, s, p, destino)


def cmd_arquivar(page, s: dict, ids: list[str]):
    """Tira o pedido do painel devolvendo-o a AGUARDANDO, sem cancelar nada.

    O painel só olha PREPARO e PRONTO, então AGUARDANDO some das duas colunas e o
    pedido continua existindo no `/delivery` e nos relatórios. É o que permite
    enxugar a fila do sandbox entre um ensaio e outro sem inventar cancelamento.
    """
    alvos = {int(i) for i in ids}
    for p in pedidos_da_janela(page, s, 6):
        if p["preVendaID"] not in alvos:
            continue
        mover(page, s, p, "AGUARDANDO")


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
        if any(m in obs for m in MARCADORES):
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
        elif comando in ("preparo", "pronto"):
            cmd_mover(page, s, comando.upper(), sys.argv[2:])
        elif comando == "arquivar":
            cmd_arquivar(page, s, sys.argv[2:])
        elif comando == "limpar":
            cmd_limpar(page, s)
        else:
            print("comando desconhecido:", comando)
        browser.close()
