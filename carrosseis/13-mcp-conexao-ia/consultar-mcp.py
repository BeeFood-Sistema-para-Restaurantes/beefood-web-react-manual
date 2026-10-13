"""Conecta ao MCP do BeeFood e grava, em `conversas.json`, as respostas reais.

É a procedência de **todo número** desta peça. As telas de conversa dos slides
são desenhadas, e desenho só pode mostrar o que foi medido: o que está aqui é o
que o servidor `beefood-api` respondeu para a conta sandbox (empresa 38311), na
mesma janela de tempo que o `rec-desempenho.png` fotografou no painel.

O caminho é o mesmo que o lojista percorre, sem atalho nenhum:

1. **registro dinâmico** do cliente em `/oauth/mcp/register` — é o que a
   ferramenta de IA faz sozinha quando recebe o *Link do MCP*;
2. **autorização** em `/oauth/mcp/authorize`, que manda para o login do painel
   e volta com a tela *Permitir*. O Chromium entra com a conta sandbox e
   clica, que é exatamente o passo que o release chama de "a IA passa a
   acessar o seu restaurante com a autorização da sua conta";
3. **troca do código por token** em `/oauth/mcp/token`, com PKCE;
4. **`tools/call`** em `https://docs.beefood.app/mcp`.

Sem o passo 2 o servidor responde `{"error":"unauthorized"}` a qualquer
chamada de `execute_beefood_request` — foi medido, e é o que sustenta a frase
do slide 2 sobre a autorização.

**Tudo é leitura.** Só entram `GET` de relatório; nenhuma rota de escrita é
chamada, embora o token da sandbox as traga no escopo.

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


def conectar() -> str:
    """Faz o OAuth inteiro e devolve o `access_token`."""
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
                                         viewport={"width": 1280, "height": 900})
        pagina = contexto.new_page()
        pagina.goto(endereco, wait_until="domcontentloaded", timeout=90000)
        pagina.wait_for_timeout(6000)
        if pagina.locator("input#emailOrWhatsapp").count():
            pagina.fill("input#emailOrWhatsapp", LOGIN)
            pagina.fill("input#password", SENHA)
            pagina.click("button:has-text('ENTRAR')")
            pagina.wait_for_timeout(15000)
        permitir = pagina.locator("button, a").filter(has_text="Permitir")
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
        if resposta.headers.get("Mcp-Session-Id"):
            self.sessao = resposta.headers["Mcp-Session-Id"]
        if avisar:
            return {}
        # A resposta vem como `text/event-stream`, uma linha `data:` só.
        for linha in resposta.text.splitlines():
            if linha.startswith("data: "):
                return json.loads(linha[6:])
        return resposta.json()

    def pedir(self, caminho: str, consulta: dict) -> dict:
        """Chama `execute_beefood_request`, que é o que fala com a API de verdade."""
        retorno = self._chamar("tools/call", {
            "name": "execute_beefood_request",
            "arguments": {"method": "GET", "path": caminho, "query": consulta},
        })
        estruturado = retorno.get("result", {}).get("structuredContent")
        if estruturado and estruturado.get("ok"):
            return estruturado["body"]
        raise SystemExit(f"ERRO em {caminho}: {json.dumps(retorno)[:400]}")


def reais(v: float) -> str:
    return "R$ " + f"{v:,.2f}".replace(",", "·").replace(".", ",").replace("·", ".")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=30,
                    help="a mesma janela que o Desempenho abre sozinho")
    args = ap.parse_args()

    hoje = dt.date.today()
    # O painel chama de "Últimos 30 dias (31 dias)": ele conta as duas pontas.
    # A conversa pergunta pela mesma janela, senão os dois números divergem e
    # a peça passa a ter dois jogos de número.
    de, ate = hoje - dt.timedelta(days=args.dias), hoje
    janela = {"saleDateFrom": de.isoformat(), "saleDateTo": ate.isoformat()}

    conversa = Conversa(conectar())
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
        "asSomasFecham": conferencia,
    }
    (AQUI / "conversas.json").write_text(
        json.dumps(saida, indent=2, ensure_ascii=False) + "\n")

    print(json.dumps(saida, indent=2, ensure_ascii=False))
    if not all(conferencia.values()):
        raise SystemExit("ERRO: a soma dos canais não fecha com o resumo")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
