"""Conecta ao MCP do BeeFood e grava, em `conversas.json`, as respostas reais.

É a procedência de **todo número** desta peça. As telas de conversa dos slides
são desenhadas, e desenho só pode mostrar o que foi medido: o que está aqui é o
que o servidor `beefood-api` respondeu para a conta sandbox (empresa 38311), na
mesma janela de tempo que o `rec-desempenho.png` fotografou no painel.

O caminho é o mesmo que o lojista percorre, sem atalho nenhum:

1. **registro dinâmico** do cliente em `/oauth/mcp/register` — é o que a
   ferramenta de IA faz sozinha quando recebe o *Link do MCP*;
2. **autorização** em `/oauth/mcp/authorize`, que manda para o login do painel
   e volta com a tela *Conectar com BeeFood*. Ali há uma tabela de permissões
   com duas colunas, LEITURA e ESCRITA, e as doze caixas das seis áreas
   liberadas já vêm **marcadas** (Entregadores e Estoque estão como *em
   breve*, desligados). O Chromium entra com a conta sandbox e clica em
   *PERMITIR* — e, com `--retrato`, fotografa a tabela antes do clique: é a
   imagem do slide 6, e não há rota no painel que abra essa tela;
3. **troca do código por token** em `/oauth/mcp/token`, com PKCE;
4. **`tools/call`** em `https://docs.beefood.app/mcp`.

Sem o passo 2 o servidor responde `{"error":"unauthorized"}` a qualquer
chamada de `execute_beefood_request` — foi medido, e é o que sustenta a frase
do slide 6 sobre a permissão.

**Há escrita, e ela é o assunto do slide 4.** Vinte e nove das sessenta e uma
rotas alteram dado, e vinte e quatro delas são do cardápio: é a maior parte do
servidor, e não dava para vender o recurso como se ele só respondesse pergunta.
A demonstração é a menor possível e ela se desfaz:

    python consultar-mcp.py --escrever   # cria o produto de exemplo, imprime o id
    python consultar-mcp.py --apagar ID  # devolve o cardápio ao que era

Entre as duas, o `capturar-telas.py` fotografa o produto no painel. Nenhum dado
existente é tocado — nem preço, nem nome, nem pedido —, e o que entra sai.

O token é descartável e **não** é versionado: ele vive em `/tmp` e expira em
minutos. O que fica no repositório é a resposta.

Uso:
    python carrosseis/13-mcp-conexao-ia/consultar-mcp.py
    python carrosseis/13-mcp-conexao-ia/consultar-mcp.py --dias 30
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import hashlib
import json
import os
import secrets
import sys
import threading
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import requests

AQUI = Path(__file__).resolve().parent
SERVIDOR = "https://docs.beefood.app"
MCP = f"{SERVIDOR}/mcp"
PORTA = 8765
RETORNO = f"http://localhost:{PORTA}/callback"

LOGIN = os.environ.get("BEEFOOD_LOGIN", "contato@beefood.com.br")
SENHA = os.environ.get("BEEFOOD_SENHA", "1q2w3e4r")
TOKEN = Path(os.environ.get("BEEFOOD_MCP_TOKEN", "/tmp/beefood-mcp-token.json"))

# O produto da demonstração de escrita. É uma bebida porque o setor Bebidas da
# loja de exemplo é curto e o produto novo aparece sem rolagem na tela do
# Cardápio — e porque bebida não tem complemento, então criar e apagar não
# deixa grupo de opção órfão.
DEMO = {
    "name": "Limonada Suíça 500ml",
    "description": "Limão batido com leite condensado e gelo.",
    "sectorId": 224857,  # Bebidas
    "price": 12.9,
    "unit": "UN",
    "label": "new",
}

# Como o painel escreve cada canal de venda. A API devolve a chave em maiúscula
# (`DIGITAL_MENU`), e quem traduz para o lojista é a interface — a peça usa a
# palavra da interface, não a da API.
CANAIS = {
    "MANUAL": "Manual",
    "DIGITAL_MENU": "Cardápio Digital",
    "IFOOD": "iFood",
    "EXTERNAL": "Externo",
    "99FOOD": "99Food",
    "TOTEM": "Totem",
    "KEETA": "Keeta",
    "WHATSAPP": "WhatsApp",
    "AIQFOME": "aiqfome",
    "RAPPI": "Rappi",
}

recebido: dict[str, str] = {}


class Retorno(BaseHTTPRequestHandler):
    """Recebe o `code` que a autorização devolve ao cliente registrado."""

    def do_GET(self):
        consulta = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        recebido.update({k: v[0] for k, v in consulta.items()})
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<p>Pode fechar.</p>".encode())

    def log_message(self, *_):
        pass


def conectar(retrato: Path | None = None) -> str:
    """Faz o OAuth inteiro e devolve o `access_token`.

    Com `retrato`, fotografa a tabela de permissões da tela *Conectar com
    BeeFood* antes de clicar em *Permitir*. Essa tela só existe dentro do
    fluxo de autorização — não há rota no painel que a abra —, então a captura
    tem de acontecer aqui, no meio do caminho.
    """
    registro = requests.post(f"{SERVIDOR}/oauth/mcp/register", timeout=30, json={
        "client_name": "BeeFood Carrossel (sandbox)",
        "redirect_uris": [RETORNO],
        "grant_types": ["authorization_code", "refresh_token"],
        "response_types": ["code"],
        "token_endpoint_auth_method": "none",
        "scope": "mcp",
    })
    registro.raise_for_status()
    cliente = registro.json()["client_id"]

    verificador = base64.urlsafe_b64encode(secrets.token_bytes(48)).decode().rstrip("=")
    desafio = base64.urlsafe_b64encode(
        hashlib.sha256(verificador.encode()).digest()).decode().rstrip("=")
    endereco = f"{SERVIDOR}/oauth/mcp/authorize?" + urllib.parse.urlencode({
        "response_type": "code", "client_id": cliente, "redirect_uri": RETORNO,
        "scope": "mcp", "state": secrets.token_urlsafe(16),
        "code_challenge": desafio, "code_challenge_method": "S256",
        "resource": MCP,
    })

    servidor = HTTPServer(("localhost", PORTA), Retorno)
    threading.Thread(target=servidor.serve_forever, daemon=True).start()

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        navegador = p.chromium.launch(args=["--no-sandbox"])
        contexto = navegador.new_context(locale="pt-BR",
                                         viewport={"width": 1280, "height": 900},
                                         device_scale_factor=2 if retrato else 1)
        pagina = contexto.new_page()
        pagina.goto(endereco, wait_until="domcontentloaded", timeout=90000)
        pagina.wait_for_timeout(6000)
        if pagina.locator("input#emailOrWhatsapp").count():
            pagina.fill("input#emailOrWhatsapp", LOGIN)
            pagina.fill("input#password", SENHA)
            pagina.click("button:has-text('ENTRAR')")
            pagina.wait_for_timeout(15000)
        permitir = pagina.locator("button, a").filter(has_text="Permitir")
        if retrato:
            # Do cabeçalho `Permissão` sobe-se dois níveis: `span` -> linha do
            # cabeçalho -> a moldura que embrulha a tabela inteira. A linha de
            # baixo ("o acesso pode ser revogado...") é IRMÃ da moldura e fica
            # de fora de propósito: ela entra escrita no slide, onde se lê.
            tabela = pagina.locator('span:text-is("Permissão")').first.locator("xpath=../..")
            # O quadro fecha na última área LIBERADA. As duas linhas de baixo
            # (Entregadores e Estoque, "em breve", desligadas) ficam de fora
            # por aritmética de slide: com oito linhas a tabela chega ao feed
            # com 700 px de largura e letra de 22, e com seis cabe nos 904 e a
            # letra dobra. O que elas acrescentavam era promessa, e promessa
            # não é o assunto da página.
            ultima = pagina.locator('span:text-is("Avaliações")').first.locator("xpath=..")
            caixa, fim = tabela.bounding_box(), ultima.bounding_box()
            destino = retrato / "imagens-puras" / "rec-permissoes.png"
            pagina.screenshot(path=str(destino), clip={
                "x": caixa["x"], "y": caixa["y"], "width": caixa["width"],
                "height": fim["y"] + fim["height"] - caixa["y"]})
            print("-->", destino.name, "capturada")
        if permitir.count():
            permitir.first.click()
            pagina.wait_for_timeout(8000)
        navegador.close()
    servidor.shutdown()

    if "code" not in recebido:
        raise SystemExit("ERRO: a autorização não devolveu código")

    troca = requests.post(f"{SERVIDOR}/oauth/mcp/token", timeout=30, data={
        "grant_type": "authorization_code", "code": recebido["code"],
        "redirect_uri": RETORNO, "client_id": cliente,
        "code_verifier": verificador, "resource": MCP,
    })
    troca.raise_for_status()
    dados = troca.json()
    TOKEN.write_text(json.dumps(dados, indent=2))
    print("--> conectado; token descartável em", TOKEN)
    return dados["access_token"]


class Conversa:
    """Sessão MCP: `initialize`, `notifications/initialized` e `tools/call`."""

    def __init__(self, token: str):
        self.token = token
        self.sessao: str | None = None
        self.n = 0
        self.servidor = self._chamar("initialize", {
            "protocolVersion": "2025-06-18", "capabilities": {},
            "clientInfo": {"name": "carrossel-beefood", "version": "1"},
        })["result"]["serverInfo"]
        self._chamar("notifications/initialized", None, avisar=True)

    def _chamar(self, metodo: str, parametros, avisar: bool = False) -> dict:
        self.n += 1
        cabecalho = {"Content-Type": "application/json",
                     "Accept": "application/json, text/event-stream",
                     "Authorization": f"Bearer {self.token}"}
        if self.sessao:
            cabecalho["Mcp-Session-Id"] = self.sessao
        corpo: dict = {"jsonrpc": "2.0", "method": metodo}
        if not avisar:
            corpo["id"] = self.n
        if parametros is not None:
            corpo["params"] = parametros
        resposta = requests.post(MCP, headers=cabecalho, json=corpo, timeout=120)
        # O `text/event-stream` vem sem charset no cabeçalho, e aí o `requests`
        # assume ISO-8859-1: `Catálogo` chega como `CatÃ¡logo`. Enquanto a peça
        # só lia número isso passou despercebido; o nome do setor e o do
        # produto criado vêm da API, e com eles o defeito aparece no slide.
        resposta.encoding = "utf-8"
        if resposta.headers.get("Mcp-Session-Id"):
            self.sessao = resposta.headers["Mcp-Session-Id"]
        if avisar:
            return {}
        # A resposta vem como `text/event-stream`, uma linha `data:` só.
        for linha in resposta.text.splitlines():
            if linha.startswith("data: "):
                return json.loads(linha[6:])
        return resposta.json()

    def api(self, metodo: str, caminho: str, consulta: dict | None = None,
            corpo: dict | None = None) -> dict:
        """Chama `execute_beefood_request`, que é o que fala com a API de verdade."""
        argumentos: dict = {"method": metodo, "path": caminho}
        if consulta:
            argumentos["query"] = consulta
        if corpo:
            argumentos["body"] = corpo
        retorno = self._chamar("tools/call", {
            "name": "execute_beefood_request", "arguments": argumentos})
        estruturado = retorno.get("result", {}).get("structuredContent")
        if estruturado and estruturado.get("ok"):
            return estruturado.get("body") or {}
        raise SystemExit(f"ERRO em {metodo} {caminho}: {json.dumps(retorno)[:400]}")

    def pedir(self, caminho: str, consulta: dict) -> dict:
        return self.api("GET", caminho, consulta)

    def catalogo(self) -> dict:
        """O que o servidor publica sobre si: as ferramentas e as rotas."""
        ferramentas = [f["name"] for f in self._chamar("tools/list", {})["result"]["tools"]]
        retorno = self._chamar("tools/call", {
            "name": "listar_endpoints", "arguments": {"lang": "pt"}})
        rotas = json.loads(retorno["result"]["content"][0]["text"])
        grupos: dict[str, dict[str, int]] = {}
        for rota in rotas["items"]:
            g = grupos.setdefault(rota["group"], {"rotas": 0, "escrita": 0})
            g["rotas"] += 1
            if rota["method"] != "GET":
                g["escrita"] += 1
        return {
            "ferramentas": ferramentas,
            "rotas": rotas["total"],
            "rotasDeEscrita": sum(g["escrita"] for g in grupos.values()),
            "grupos": grupos,
        }


def reais(v: float) -> str:
    return "R$ " + f"{v:,.2f}".replace(",", "·").replace(".", ",").replace("·", ".")


def escrever(conversa: Conversa) -> dict:
    """Cria o produto da demonstração e confere que ele entrou no cardápio.

    Se a rodada anterior já criou um e ele continua lá, **reaproveita**. Medir
    de novo é comum — basta o fuso mudar a janela do relatório —, e cada nova
    medição não pode deixar uma limonada a mais no cardápio da loja.
    """
    anterior = (json.loads((AQUI / "conversas.json").read_text()).get("escrita")
                if (AQUI / "conversas.json").is_file() else None)
    if anterior:
        try:
            vivo = conversa.pedir(f"/v1/catalog/products/{anterior['produtoId']}", {})
            if vivo.get("name") == DEMO["name"]:
                print(f"--> produto {anterior['produtoId']} já existe; reaproveitado")
                return anterior
        except SystemExit:
            pass

    criado = conversa.api("POST", "/v1/catalog/products", corpo=DEMO)
    identificador = criado.get("productId") or criado.get("id")
    if not identificador:
        raise SystemExit(f"ERRO: a criação não devolveu id: {json.dumps(criado)[:300]}")
    lido = conversa.pedir(f"/v1/catalog/products/{identificador}", {})
    print(f"--> produto {identificador} criado: {lido.get('name')} "
          f"{reais(lido.get('price', 0))} em {lido.get('sectorName')}")
    print(f"--> para desfazer: python {Path(__file__).name} --apagar {identificador}")
    return {
        "produtoId": identificador,
        "nome": lido.get("name"),
        "preco": lido.get("price"),
        "precoEscrito": reais(lido.get("price", 0)),
        "setor": lido.get("sectorName"),
        "selo": DEMO["label"],
        "rota": "POST /v1/catalog/products",
        "escopo": "catalog:write",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=30,
                    help="a mesma janela que o Desempenho abre sozinho")
    ap.add_argument("--escrever", action="store_true",
                    help="cria o produto de exemplo no cardápio da sandbox")
    ap.add_argument("--apagar", type=int, metavar="ID",
                    help="apaga o produto criado e devolve o cardápio ao que era")
    ap.add_argument("--retrato", action="store_true",
                    help="fotografa a tela de autorização no caminho")
    args = ap.parse_args()

    if args.apagar:
        conversa = Conversa(conectar())
        conversa.api("DELETE", f"/v1/catalog/products/{args.apagar}")
        print(f"--> produto {args.apagar} apagado; o cardápio voltou ao que era")
        return 0

    # O "hoje" é o da LOJA, não o da máquina. O Cloud Agent roda em UTC, e
    # depois das 21h de Brasília `date.today()` já virou o dia seguinte: a
    # janela andava 24 horas, perdia o primeiro dia e o painel passava a
    # mostrar R$ 14.283,52 contra R$ 12.083,98 da conversa. Como os dois
    # números batem quando a captura é feita de tarde, o defeito só aparece
    # em rodada noturna — e aparece como se a loja tivesse recebido pedido.
    hoje = dt.datetime.now(dt.timezone(dt.timedelta(hours=-3))).date()
    # O painel chama de "Últimos 30 dias (31 dias)": ele conta as duas pontas.
    # A conversa pergunta pela mesma janela, senão os dois números divergem e
    # a peça passa a ter dois jogos de número.
    de, ate = hoje - dt.timedelta(days=args.dias), hoje
    janela = {"saleDateFrom": de.isoformat(), "saleDateTo": ate.isoformat()}

    conversa = Conversa(conectar(AQUI if args.retrato else None))
    print("servidor:", conversa.servidor)

    resumo = conversa.pedir("/v1/orders/summary", janela)
    canais = conversa.pedir("/v1/orders/summary/grouped",
                            {**janela, "groupBy": "salesChannel"})
    # `limit: 1` de propósito: o que interessa é o `total` da paginação, que é
    # a contagem que a pergunta do slide 5 faz. Puxar as 398 linhas para somar
    # na mão daria o mesmo número e gastaria a cota da API.
    produtos = conversa.pedir("/v1/catalog/products", {"limit": 1})
    setores = conversa.pedir("/v1/catalog/sectors", {"limit": 1})
    vendidos = conversa.pedir("/v1/orders/summary/products", {**janela, "limit": 1})
    # Só a contagem: a resposta de avaliações traz telefone de quem avaliou, e
    # nada além do `total` pode encostar nesta peça (o repositório é público).
    cupons = conversa.pedir("/v1/store/coupons", {"limit": 1})
    avaliacoes = conversa.pedir("/v1/store/reviews", {"limit": 1})

    linhas = [{"canal": CANAIS.get(g["key"], g["key"]),
               "chave": g["key"],
               "pedidos": g["orderCount"],
               "valor": g["totalRevenue"],
               "valorEscrito": reais(g["totalRevenue"])}
              for g in canais["groups"]]

    conferencia = {
        "pedidos": sum(l["pedidos"] for l in linhas) == resumo["orderCount"],
        "valor": round(sum(l["valor"] for l in linhas), 2)
                 == round(resumo["totalRevenue"], 2),
    }

    saida = {
        "lido_em": dt.datetime.now().isoformat(timespec="seconds"),
        "servidor": conversa.servidor,
        "conta": "sandbox BeeFood3 - Manual (empresa 38311)",
        "oQueOServidorPublica": conversa.catalogo(),
        "janela": {**janela, "comoAPerguntaDiz": f"últimos {args.dias} dias"},
        "resumo": {
            "pedidos": resumo["orderCount"],
            "valor": resumo["totalRevenue"],
            "valorEscrito": reais(resumo["totalRevenue"]),
            "ticket": resumo["averageOrderValue"],
            "ticketEscrito": reais(resumo["averageOrderValue"]),
        },
        "canais": linhas,
        "cardapio": {
            "produtos": produtos["total"],
            "setores": setores["total"],
            "produtosComVenda": vendidos["total"],
        },
        "cupons": cupons["total"],
        "avaliacoes": avaliacoes["total"],
        "asSomasFecham": conferencia,
    }
    if args.escrever:
        saida["escrita"] = escrever(conversa)

    (AQUI / "conversas.json").write_text(
        json.dumps(saida, indent=2, ensure_ascii=False) + "\n")

    print(json.dumps(saida, indent=2, ensure_ascii=False))
    if not all(conferencia.values()):
        raise SystemExit("ERRO: a soma dos canais não fecha com o resumo")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
