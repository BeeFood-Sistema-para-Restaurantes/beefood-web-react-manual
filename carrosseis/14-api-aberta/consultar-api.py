"""Chama a API Aberta de verdade e grava, em `chamadas.json`, o que ela respondeu.

É a procedência de **todo número e de todo campo** desta peça. O cartão do slide
2 é desenhado, e desenho só pode mostrar o que foi medido: o que está aqui é o
que `api.beefood.app` devolveu para a loja sandbox *BeeFood3 - Manual*
(empresa 38311).

O caminho é o mesmo que a documentação manda o parceiro percorrer, sem atalho:

1. **a credencial** sai de *Aplicativos → API Aberta*, no painel. O Client
   Secret fica mascarado na tela e só aparece pelo ícone de olho, que chama a
   rota `secret` da função `api-aberta`. O script abre a folha, clica no olho e
   guarda o par em `/tmp` — **nunca no repositório**: a loja de exemplo roda em
   produção, e credencial de produção não é credencial de sandbox descartável;
2. **o token** sai de `POST /v1/oauth/token` com `grantType:
   client_credentials`, e vale uma hora (a resposta diz o `expiresAt`);
3. **as chamadas** vão em `/v1/...` com `Authorization: Bearer`.

Nenhuma chamada desta peça escreve. São seis GETs, e o que eles trazem é o que
os slides afirmam:

| Chamada | Para que slide |
|---|---|
| `POST /v1/oauth/token` | o cartão do slide 2 começa no token |
| `GET /v1/orders` | é a resposta desenhada no slide 2 |
| `GET /v1/orders` sem `saleDateFrom` | o formato de erro, que a documentação promete igual em toda rota |
| `GET /v1/catalog/products` | o total do cardápio, que mede o tamanho do Catálogo |
| `GET /v1/catalog/sectors` | idem |
| `GET /v1/store/merchants` | confere que o token fala pela loja certa |

A contagem de rotas por grupo não sai daqui: ela vem do `listar_endpoints` do
servidor de documentação, que é público e não pede login — é a mesma medição da
peça 13, e é o que faz as duas não se contradizerem.

**A resposta de pedido desta loja não traz dado pessoal** — a listagem tem
`orderId`, `createdAt`, status, tipo e valor, e nada mais. Foi conferido campo a
campo antes de gravar: `chaves` registra a lista inteira, e o cartão do slide usa
cinco dos oito. O detalhe de um pedido (`GET /v1/orders/{id}`) traz nome e
telefone de quem pediu, e por isso **não é chamado aqui**.

Uso:
    python carrosseis/14-api-aberta/consultar-api.py
    python carrosseis/14-api-aberta/consultar-api.py --dias 7
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
from pathlib import Path

import requests

AQUI = Path(__file__).resolve().parent
BASE = "https://api.beefood.app"
CREDENCIAL = Path(os.environ.get("BEEFOOD_API_CRED", "/tmp/beefood-api-cred.json"))
DOCS_MCP = "https://docs.beefood.app/mcp"

# Os cinco campos que o cartão do slide 2 mostra, na ordem em que a API os
# devolve. Os outros três do item (`createdAt`, `deliveryType`, `paidAmount`)
# ficam de fora: o título do slide fala de status e de valor, e arte com data
# nasce velha.
CAMPOS_DO_CARTAO = ["orderId", "orderStatus", "deliveryStatus", "orderType",
                    "orderAmount"]


def credencial() -> dict:
    """Devolve `clientId` e `clientSecret`, revelando o segredo no painel.

    Fica em `/tmp` entre uma rodada e outra porque a folha demora ~25 s para
    abrir. Para forçar de novo, apague o arquivo.
    """
    if CREDENCIAL.is_file():
        return json.loads(CREDENCIAL.read_text())

    sys.path.append(".cursor/skills/carrossel/scripts")
    from capturar import esperar, limpar, sessao  # noqa: PLC0415

    with sessao("painel") as pagina:
        pagina.emulate_media(reduced_motion="reduce")
        pagina.goto("https://beefood.app/aplicativos",
                    wait_until="domcontentloaded", timeout=90000)
        esperar(pagina)
        limpar(pagina)
        pagina.get_by_text("Integre seu sistema ao BeeFood via API REST",
                           exact=False).first.click()
        pagina.wait_for_timeout(9000)
        esperar(pagina)

        cartao = pagina.get_by_text("Credencial principal", exact=True).first.locator(
            "xpath=ancestor::div[contains(@class,'rounded-2xl')][1]")
        identificador = cartao.locator("code").first.inner_text().strip()
        bloco = cartao.get_by_text("Client Secret", exact=True).locator("xpath=..")
        bloco.get_by_role("button").last.click()
        pagina.wait_for_timeout(4000)
        revelado = [c.inner_text().strip() for c in cartao.locator("code").all()]
        segredo = next((s for s in revelado
                        if s and "\u2022" not in s and s != identificador), None)
        if not segredo:
            raise SystemExit("ERRO: o olho não revelou o Client Secret")

    CREDENCIAL.write_text(json.dumps(
        {"clientId": identificador, "clientSecret": segredo}, indent=2))
    print("--> credencial lida do painel e guardada em", CREDENCIAL)
    return {"clientId": identificador, "clientSecret": segredo}


def rotas_por_grupo() -> dict:
    """Pergunta ao servidor de documentação quantas rotas existem, e quantas escrevem.

    O `listar_endpoints` é ferramenta pública do MCP da documentação: não pede
    login, porque ler a documentação não exige conta. Conta as rotas de
    **negócio** — as 7 de autenticação e o *health check* ficam de fora, e é por
    isso que o total aqui dá 61 enquanto a home do portal mostra 69.
    """
    sessao_http = requests.Session()
    cabecalho = {"Content-Type": "application/json",
                 "Accept": "application/json, text/event-stream"}
    identificador = {"n": 0, "sessao": None}

    def chamar(metodo: str, parametros, avisar: bool = False) -> dict:
        identificador["n"] += 1
        h = dict(cabecalho)
        if identificador["sessao"]:
            h["Mcp-Session-Id"] = identificador["sessao"]
        corpo: dict = {"jsonrpc": "2.0", "method": metodo}
        if not avisar:
            corpo["id"] = identificador["n"]
        if parametros is not None:
            corpo["params"] = parametros
        r = sessao_http.post(DOCS_MCP, headers=h, json=corpo, timeout=120)
        # `text/event-stream` chega sem charset, e aí o `requests` assume
        # ISO-8859-1: `Catálogo` viraria `CatÃ¡logo` no nome do grupo.
        r.encoding = "utf-8"
        identificador["sessao"] = r.headers.get("Mcp-Session-Id") or identificador["sessao"]
        if avisar:
            return {}
        for linha in r.text.splitlines():
            if linha.startswith("data: "):
                return json.loads(linha[6:])
        return r.json()

    servidor = chamar("initialize", {
        "protocolVersion": "2025-06-18", "capabilities": {},
        "clientInfo": {"name": "carrossel-beefood", "version": "1"},
    })["result"]["serverInfo"]
    chamar("notifications/initialized", None, avisar=True)
    retorno = chamar("tools/call", {"name": "listar_endpoints",
                                    "arguments": {"lang": "pt"}})
    lista = json.loads(retorno["result"]["content"][0]["text"])

    grupos: dict[str, dict[str, int]] = {}
    for rota in lista["items"]:
        g = grupos.setdefault(rota["group"], {"rotas": 0, "escrita": 0})
        g["rotas"] += 1
        if rota["method"] != "GET":
            g["escrita"] += 1
    return {
        "servidorDaDocumentacao": servidor,
        "rotasDeNegocio": lista["total"],
        "deEscrita": sum(g["escrita"] for g in grupos.values()),
        "grupos": grupos,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=7,
                    help="janela da consulta de pedidos")
    args = ap.parse_args()

    cred = credencial()
    inicio = requests.post(f"{BASE}/v1/oauth/token", timeout=40, json={
        "grantType": "client_credentials",
        "clientId": cred["clientId"], "clientSecret": cred["clientSecret"]})
    inicio.raise_for_status()
    emissao = inicio.json()
    print("--> token emitido; expira em", emissao["expiresAt"])
    autorizacao = {"Authorization": f"Bearer {emissao['accessToken']}"}

    def pedir(caminho: str, consulta: dict | None = None) -> tuple[int, dict]:
        r = requests.get(f"{BASE}{caminho}", headers=autorizacao,
                         params=consulta, timeout=60)
        return r.status_code, r.json()

    # O "hoje" é o da LOJA. O Cloud Agent roda em UTC, e depois das 21h de
    # Brasília `date.today()` já virou o dia seguinte — a janela andava 24 h e
    # a peça passava a ter dois jogos de número. É a lição da #13.
    hoje = dt.datetime.now(dt.timezone(dt.timedelta(hours=-3))).date()
    de = hoje - dt.timedelta(days=args.dias)
    janela = {"saleDateFrom": de.isoformat(), "saleDateTo": hoje.isoformat()}

    codigo, pedidos = pedir("/v1/orders", {**janela, "limit": 1})
    if codigo != 200 or not pedidos.get("items"):
        raise SystemExit(f"ERRO: /v1/orders devolveu {codigo}: "
                         f"{json.dumps(pedidos)[:300]}")
    item = pedidos["items"][0]

    pessoal = [c for c in item
               if any(p in c.lower() for p in ("name", "phone", "mail", "doc",
                                               "cpf", "address", "customer"))]
    if pessoal:
        raise SystemExit(f"ERRO: a listagem trouxe campo pessoal: {pessoal}. "
                         "Nada disso pode encostar numa peça de repositório público.")

    # O erro é de propósito: a documentação promete o mesmo corpo em toda rota
    # que falha, e isso se confere pedindo errado.
    codigo_erro, erro = pedir("/v1/orders", {"limit": 1})

    _, produtos = pedir("/v1/catalog/products", {"limit": 1})
    _, setores = pedir("/v1/catalog/sectors", {"limit": 1})
    _, lojas = pedir("/v1/store/merchants")
    loja = lojas["items"][0]

    saida = {
        "lido_em": dt.datetime.now().isoformat(timespec="seconds"),
        "base": BASE,
        "conta": f"sandbox {loja['tradeName'].strip()} (loja {loja['storeId']}, "
                 f"filial {loja['merchantId']})",
        "token": {
            "rota": "POST /v1/oauth/token",
            "grantType": "client_credentials",
            "campos": sorted(emissao.keys()),
            "validade": "1 hora, pelo expiresAt da resposta",
        },
        "oQueADocumentacaoPublica": rotas_por_grupo(),
        "pedidos": {
            "rota": "GET /v1/orders",
            "janela": {**janela, "comoAPerguntaDiz": f"últimos {args.dias} dias"},
            "total": pedidos["total"],
            "paginacao": {k: pedidos[k] for k in ("page", "limit", "total", "pages")},
            "chaves": list(item.keys()),
            "camposNoCartaoDoSlide": CAMPOS_DO_CARTAO,
            "itemNoCartaoDoSlide": {c: item[c] for c in CAMPOS_DO_CARTAO},
        },
        "erro": {
            "rota": "GET /v1/orders sem saleDateFrom",
            "status": codigo_erro,
            "corpo": erro,
        },
        "cardapio": {
            "produtos": produtos["total"],
            "setores": setores["total"],
        },
    }

    (AQUI / "chamadas.json").write_text(
        json.dumps(saida, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(saida, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
