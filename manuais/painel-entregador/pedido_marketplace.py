"""Insere pedido de iFood, 99Food, Keeta e AIQFome na sandbox, para o painel mostrar o canal.

## Por que este arquivo existe

O cartão do Painel para Entregadores mostra o **ícone do canal** e a **referência do
marketplace** (`CartaoPedido.tsx` + `origemIcon.ts`). Sem pedido de marketplace na
sandbox o manual não consegue fotografar justamente o que diferencia o painel.

E marketplace não se cria pela tela: ensaiado em `exp_origem.py`, o
`POST /api/venda2/salvar` — a rota que a tela `/delivery` usa — **descarta** `origem`,
`marketPlace`, `ifoodShortReference`, `keetaId` e `nnID` nas três posições possíveis
(raiz, `delivery` e `cliente`) e grava sempre `origem = "Manual"`.

## A rota que grava a origem

Quem grava origem diferente de Manual é a rota do **cardápio público**, descoberta
farejando a rede em `pedido_cardapio.py`:

    POST https://app.beetechapi.be/datasnap/rest/tmesa/pedido

É o mesmo endpoint do ERP que as integrações usam para entregar o pedido que
receberam da plataforma. Este script repete o corpo daquele pedido trocando o cliente,
os itens e os campos do canal — ou seja, insere pelo mesmo caminho do produto, sem
`UPDATE` em tabela nenhuma.

## Uso

    python pedido_marketplace.py molde      # grava o molde limpo a partir da captura
    python pedido_marketplace.py sondar     # ensaio: manda UM pedido e lê o que gravou
    python pedido_marketplace.py semear     # os quatro canais
    python pedido_marketplace.py semear ifood keeta
    python pedido_marketplace.py estado     # o que o painel enxerga agora

Trava de segurança: só a sandbox 38311/39202.
"""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

from beefood import abrir, api_get, api_post
from smoketeste import EMPRESA_PERMITIDA, FILIAL_PERMITIDA, conferir_alvo

ERP = "https://app.beetechapi.be/datasnap/rest/tmesa/pedido"
ORIGEM_CARDAPIO = "https://menu.beefood.com.br"
PASTA = Path(__file__).resolve().parent
MOLDE = PASTA / "molde-pedido.json"
CAPTURA = Path("/tmp/painel-entregador-pedidos/1-tmesa-pedido.json")
CAPTURA_CABECALHOS = Path("/tmp/painel-entregador-pedidos/1-tmesa-pedido-headers.json")

MARCADOR = "[SMOKE-PAINEL]"

# Os quatro canais pedidos, com o campo de identificação que cada um usa. Os valores
# imitam o que o `diagnostico.py` leu dos pedidos que já existiam na base:
# iFood tem `ifoodShortReference` ("1851 - Coleta 3983") e `correlationId`;
# 99Food tem `nnID` (id longo) e usa `ifoodShortReference` como número curto;
# Keeta tem `keetaId` de 16 dígitos; AIQFome tem `aiqfomeId`.
CANAIS = {
    "ifood": {
        "origem": "iFood",
        "cliente": "Juliana Castro Alves",
        "pagamento": "PAGO ONLINE",
        "frete": 8.0,
        "campos": {
            "ifoodShortReference": "4821 - Coleta 7312",
            "ifoodLocalizer": "48739120",
            "correlationId": "5f21a7c4-9b30-4d6e-8a15-73c0e2b41d99",
        },
    },
    "99food": {
        "origem": "99Food",
        "cliente": "Marcelo Tavares Pinto",
        "pagamento": "PIX",
        "frete": 10.0,
        "campos": {
            "ifoodShortReference": "254118",
            "nnID": "5764687241800912734",
        },
    },
    "keeta": {
        "origem": "Keeta",
        "cliente": "Patrícia Souza Correia",
        "pagamento": "PAGO ONLINE",
        "frete": 14.0,
        "campos": {"keetaId": "4900112233449871"},
    },
    "aiqfome": {
        "origem": "AIQFome",
        "cliente": "Rodrigo Menezes Prado",
        "pagamento": "PAGO ONLINE",
        "frete": 7.0,
        "campos": {"aiqfomeId": "9820451"},
    },
}

# Campos que o `vendaDetalhes` devolve e que provam se a origem pegou.
CONFERIR = [
    "preVendaID", "numeroPreVenda", "origem", "marketPlace", "ifoodShortReference",
    "ifoodLocalizer", "correlationId", "keetaId", "nnID", "aiqfomeId",
    "tipoPedido", "situacaoDelivery", "nome", "tipoPagStr", "observacoes",
]


def carregar_molde() -> dict:
    if MOLDE.exists():
        return json.loads(MOLDE.read_text(encoding="utf-8"))
    raise SystemExit(
        f"molde ausente: {MOLDE.name}\n"
        f"  rode `python pedido_cardapio.py 1` e depois `python pedido_marketplace.py molde`"
    )


def cmd_molde():
    """Limpa a captura do cardápio e grava o molde versionável.

    O repositório é público, então o CPF e o nome do consumidor de teste saem do
    arquivo. O `consumidorID` fica: ele é o cliente de teste da sandbox e é o que
    faz o pedido nascer com endereço válido dentro da área de entrega.
    """
    if not CAPTURA.exists():
        raise SystemExit(f"captura ausente: {CAPTURA}\n  rode `python pedido_cardapio.py 1`")
    corpo = json.loads(CAPTURA.read_text(encoding="utf-8"))
    if corpo.get("empresaID") != EMPRESA_PERMITIDA:
        raise SystemExit("a captura não é da sandbox")

    d = corpo.get("delivery") or {}
    d["cpf"] = None
    d["email"] = None
    d["nome_razaosocial"] = "Cliente de teste"
    corpo["obs"] = ""
    corpo.pop("pedido_original", None)
    MOLDE.write_text(json.dumps(corpo, ensure_ascii=False, indent=1), encoding="utf-8")
    print("molde gravado em", MOLDE)
    print("  itens:", [p.get("descricao") for p in corpo.get("pedidos") or []])
    print("  telefone:", d.get("telefonePrincipal"), "| cpf:", d.get("cpf"))


def montar(canal: str) -> dict:
    """Molde do cardápio + os campos do canal, na raiz e dentro de `delivery`.

    As duas posições vão juntas de propósito: o ensaio (`sondar`) é que diz qual
    delas o ERP lê, e mandar as duas não atrapalha quando só uma vale.
    """
    cfg = CANAIS[canal]
    corpo = carregar_molde()
    marca = {"origem": cfg["origem"], "marketPlace": True, **cfg["campos"]}

    corpo.update(marca)
    corpo["obs"] = f"{MARCADOR} {cfg['origem']}"
    d = corpo["delivery"]
    d.update(marca)
    d["nome_razaosocial"] = cfg["cliente"]
    d["tipoPagamento"] = cfg["pagamento"]
    d["valorFrete"] = cfg["frete"]
    d["tipoPedido"] = "Entrega"
    # Sem desconto/acréscimo de forma de pagamento: eles vinham do Dinheiro do cardápio
    # e desalinham o total quando a forma muda.
    d["descontoFormaPagamento"] = 0
    d["acrescimoFormaPagamento"] = 0
    d["troco"] = None

    # Varia a quantidade para os cartões não saírem idênticos na foto.
    for item in corpo.get("pedidos") or []:
        item["qtd"] = random.choice([1, 1, 2])
    return corpo


def autorizacao() -> str:
    """O `Basic` que o cardápio público manda para o ERP, lido da captura.

    **Não entra no repositório.** Ele não é credencial da sandbox: é a autenticação
    que o cardápio usa para falar com o ERP de qualquer loja, e este repositório é
    público. O valor vive só em `/tmp`, gravado por `pedido_cardapio.py`, e some
    junto com a máquina.
    """
    if not CAPTURA_CABECALHOS.exists():
        raise SystemExit(
            f"cabeçalhos ausentes: {CAPTURA_CABECALHOS}\n"
            f"  rode `python pedido_cardapio.py 1` — sem o Authorization do cardápio a\n"
            f"  rota do ERP responde 401."
        )
    cab = json.loads(CAPTURA_CABECALHOS.read_text(encoding="utf-8"))
    valor = cab.get("authorization") or cab.get("Authorization")
    if not valor:
        raise SystemExit("a captura não tem o cabeçalho Authorization")
    return valor


def enviar(page, corpo: dict):
    resp = page.request.post(
        ERP,
        headers={
            "Content-Type": "application/json",
            "Authorization": autorizacao(),
            "Origin": ORIGEM_CARDAPIO,
            "Referer": f"{ORIGEM_CARDAPIO}/",
        },
        data=json.dumps(corpo),
    )
    texto = resp.text()
    try:
        return resp.status, json.loads(texto)
    except Exception:
        return resp.status, texto[:400]


def pre_venda_de(resp) -> int | None:
    """O ERP responde uma **lista** com um objeto, por isso a busca é recursiva."""
    if isinstance(resp, list):
        for item in resp:
            achado = pre_venda_de(item)
            if achado:
                return achado
        return None
    if not isinstance(resp, dict):
        return None
    for chave in ("preVendaID", "prevendaID", "PreVendaID"):
        if resp.get(chave):
            return int(resp[chave])
    for valor in resp.values():
        achado = pre_venda_de(valor)
        if achado:
            return achado
    return None


def conferir_pedido(page, s: dict, pre: int) -> dict:
    _, det = api_get(
        page, f"/api/venda2/vendaDetalhes/{s['empresaID']}/{s['usuarioID']}/{pre}/0"
    )
    venda = (det or {}).get("venda") or {}
    print("   gravado:", json.dumps({k: venda.get(k) for k in CONFERIR}, ensure_ascii=False))
    return venda


def mover(page, s: dict, venda: dict, destino: str):
    corpo = {
        "empresaID": s["empresaID"], "filialID": s["filialID"],
        "usuarioID": s["usuarioID"], "usuario": s["usuario"],
        "clienteID": venda.get("clienteID"),
        "situacaoDelivery": destino,
        "situacaoDeliveryAnterior": venda.get("situacaoDelivery"),
        "preVendaID": venda["preVendaID"],
        "numeroPreVenda": venda.get("numeroPreVenda"),
        "numeroPedido": venda.get("numeroPedido") or 0,
        "tipoPedido": venda.get("tipoPedido") or "DELIVERY",
        "correlationId": venda.get("correlationId"),
        "nnID": venda.get("nnID"), "keetaId": venda.get("keetaId"),
        "tipoPagStr": venda.get("tipoPagStr"),
        "filialIDOrigem": venda.get("filialIDOrigem"),
        "consumoLocal": venda.get("consumoLocal"),
        "tipo": "DELIVERY", "esteira": False,
    }
    st, r = api_post(page, "/api/venda2/atualizaSituacaoDelivery", corpo)
    print(f"   {destino}: {st} {json.dumps(r, ensure_ascii=False)[:80]}")


def cmd_sondar(page, s: dict, canal: str = "ifood"):
    print(f"ENSAIO — um pedido de {CANAIS[canal]['origem']}, para ler o que o ERP gravou\n")
    st, resp = enviar(page, montar(canal))
    print("  POST tmesa/pedido", st, json.dumps(resp, ensure_ascii=False)[:400])
    pre = pre_venda_de(resp)
    print("  preVendaID", pre)
    if pre:
        conferir_pedido(page, s, pre)


def cmd_semear(page, s: dict, canais: list[str], prontos: list[str]):
    for canal in canais:
        cfg = CANAIS[canal]
        print(f"\n== {cfg['origem']} ==")
        st, resp = enviar(page, montar(canal))
        print("   POST", st, json.dumps(resp, ensure_ascii=False)[:240])
        pre = pre_venda_de(resp)
        if not pre:
            print("   sem preVendaID na resposta — nada a conferir")
            continue
        venda = conferir_pedido(page, s, pre)
        venda.setdefault("preVendaID", pre)
        # O pedido do cardápio nasce AGUARDANDO; o painel só olha PREPARO e PRONTO.
        mover(page, s, venda, "PREPARO")
        if canal in prontos:
            venda["situacaoDelivery"] = "PREPARO"
            mover(page, s, venda, "PRONTO")


def cmd_estado(page, s: dict):
    _, lista = api_get(
        page, f"/api/venda2/delivery/{s['empresaID']}/{s['filialID']}/{s['usuarioID']}/6"
    )
    lista = lista if isinstance(lista, list) else []
    for etapa in ("PREPARO", "PRONTO"):
        alvo = [
            p for p in lista
            if str(p.get("tipoPedido") or "").upper() == "DELIVERY"
            and str(p.get("situacaoDelivery") or "").upper() == etapa
        ]
        print(f"{etapa}: {len(alvo)}")
        for p in alvo:
            print(
                f"   {p['preVendaID']}  {str(p.get('origem')):<18}"
                f" nº {p.get('numeroPedido') or p.get('numeroPreVenda')}"
                f"  ref={p.get('ifoodShortReference') or p.get('keetaId') or p.get('nnID')}"
                f"  {p.get('nome')}"
            )


if __name__ == "__main__":
    comando = sys.argv[1] if len(sys.argv) > 1 else "estado"
    argumentos = [a for a in sys.argv[2:] if not a.startswith("--")]

    if comando == "molde":
        cmd_molde()
        raise SystemExit(0)

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
        print("SESSAO", json.dumps(s, ensure_ascii=False), "\n")

        if comando == "sondar":
            cmd_sondar(page, s, argumentos[0] if argumentos else "ifood")
        elif comando == "semear":
            canais = argumentos or list(CANAIS)
            desconhecidos = [c for c in canais if c not in CANAIS]
            if desconhecidos:
                raise SystemExit(f"canal desconhecido: {desconhecidos} — use {list(CANAIS)}")
            prontos = [c for c in ("keeta", "99food") if c in canais]
            cmd_semear(page, s, canais, prontos)
        elif comando == "estado":
            cmd_estado(page, s)
        else:
            print("comando desconhecido:", comando)
        browser.close()
