"""Mede a API de Estoque pelas duas portas e grava tudo em `chamadas.json`.

É a procedência de **todo número, todo campo e toda frase de resposta** desta
peça. Quase tudo aqui vira desenho, e desenho só pode mostrar o que foi medido.

As duas portas são o assunto do carrossel, e por isso as duas são percorridas:

| Porta | Caminho |
|---|---|
| **API Aberta** | credencial de *Aplicativos → API Aberta* → `POST /v1/oauth/token` → `Authorization: Bearer` |
| **MCP** | registro dinâmico → autorização com PKCE → `tools/call execute_beefood_request` |

E uma terceira fonte, que não pede login: o `listar_endpoints` do servidor de
documentação, que é quem diz **quantas** rotas o grupo Estoque tem e quais
escrevem. É a mesma medição das peças 13 e 14, e é o que faz as três não se
contradizerem.

**A escrita é feita, não desenhada.** É a lição da #13, e aqui ela cabe melhor
ainda: o exemplo que o próprio release dá — *"dê entrada de 20 unidades de
refrigerante"* — é reversível, porque `new` grava o saldo informado no lugar do
atual. O script dá a entrada pelo MCP, lê o saldo de volta e **devolve o saldo
ao que era**, no mesmo arranque:

    python consultar-estoque.py --escrever

Fica registrado em `chamadas.json`, em *escrita*, com o saldo antes, o corpo que
foi enviado, a resposta linha a linha e a confirmação de que o saldo voltou. Se
alguma coisa falhar no meio, o `--restaurar` devolve o saldo sozinho.

**O que não entra aqui:** nenhuma rota que traga nome, telefone ou documento de
cliente. Estoque não tem dado pessoal — o campo mais próximo é o `userId` de
quem moveu, que é um número e fica de fora dos arquivos de arte.

A credencial vive em `/tmp` e **nunca** no repositório: a loja de exemplo roda
em produção, e credencial de produção não é credencial de sandbox descartável.

Uso:
    python carrosseis/16-api-estoque/consultar-estoque.py
    python carrosseis/16-api-estoque/consultar-estoque.py --escrever
    python carrosseis/16-api-estoque/consultar-estoque.py --retrato
    python carrosseis/16-api-estoque/consultar-estoque.py --restaurar
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
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import requests

AQUI = Path(__file__).resolve().parent
API = "https://api.beefood.app"
SERVIDOR = "https://docs.beefood.app"
MCP = f"{SERVIDOR}/mcp"
PORTA = 8765
RETORNO = f"http://localhost:{PORTA}/callback"

LOGIN = os.environ.get("BEEFOOD_LOGIN", "contato@beefood.com.br")
SENHA = os.environ.get("BEEFOOD_SENHA", "1q2w3e4r")
CREDENCIAL = Path(os.environ.get("BEEFOOD_API_CRED", "/tmp/beefood-api-cred.json"))

# O item da demonstração de escrita. É um refrigerante porque é o exemplo que o
# próprio release dá, e porque produto de bebida não tem receita: dar entrada
# nele não mexe em saldo de insumo nenhum por tabela.
DEMO = {"type": "product", "productId": 2659780, "nome": "Coca Cola 350ml"}
ENTRADA = 20

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


def conectar(retrato: Path | None = None) -> str:
    """Faz o OAuth do MCP inteiro e devolve o `access_token`.

    Com `retrato`, fotografa a tabela de permissões da tela *Conectar com
    BeeFood* antes de clicar em *Permitir*. Essa tela só existe dentro do fluxo
    de autorização — não há rota no painel que a abra —, então a captura tem de
    acontecer aqui, no meio do caminho. É a lição da #13.
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
                                         viewport={"width": 1280, "height": 1000},
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
            _fotografar_permissoes(pagina, retrato)
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
    print("--> MCP conectado (token descartável, fora do repositório)")
    return troca.json()["access_token"]


def _fotografar_permissoes(pagina, destino: Path) -> None:
    """Recorta a linha de Estoque da tabela de autorização, e só ela.

    A #13 fotografou a tabela inteira e **fechou o quadro em Avaliações**,
    deixando de fora as duas linhas que a tela mostrava apagadas, com a
    etiqueta *Em breve*: Entregadores e Estoque. Uma delas saiu do em breve, e
    é o assunto desta peça — então aqui o recorte é o contrário: a linha do
    Estoque com o cabeçalho em cima, para as colunas LEITURA e ESCRITA serem
    lidas.
    """
    cabecalho = pagina.locator('span:text-is("Permissão")').first.locator("xpath=..")
    linha = pagina.locator('span:text-is("Estoque")').first.locator("xpath=..")
    alto, baixo = cabecalho.bounding_box(), linha.bounding_box()
    if not alto or not baixo:
        raise SystemExit("ERRO: não achei a linha de Estoque na tela de autorização")

    # Onde o quadro FECHA tem resposta exata, e não é folga arbitrária. Rente
    # ao texto do Estoque, a moldura da linha sai cortada e lê como render
    # quebrado; com 16 px de sobra, aparece a primeira fatia da linha seguinte,
    # e meia linha lê como tela cortada. O fecho certo é o **fio** entre as
    # duas, que é o topo da linha de baixo.
    seguinte = pagina.locator('span:text-is("Entregadores")').first
    if seguinte.count() and seguinte.bounding_box():
        pe = seguinte.locator("xpath=..").bounding_box()["y"] - 1
    else:
        pe = baixo["y"] + baixo["height"] + 16

    arquivo = destino / "imagens-puras" / "rec-autorizacao.png"
    pagina.screenshot(path=str(arquivo), clip={
        "x": alto["x"], "y": alto["y"], "width": alto["width"],
        "height": pe - alto["y"]})
    print("-->", arquivo.name, "capturada no meio do fluxo de autorização")


class Conversa:
    """Sessão MCP: `initialize`, `notifications/initialized` e `tools/call`."""

    def __init__(self, token: str | None = None):
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
                     "Accept": "application/json, text/event-stream"}
        if self.token:
            cabecalho["Authorization"] = f"Bearer {self.token}"
        if self.sessao:
            cabecalho["Mcp-Session-Id"] = self.sessao
        corpo: dict = {"jsonrpc": "2.0", "method": metodo}
        if not avisar:
            corpo["id"] = self.n
        if parametros is not None:
            corpo["params"] = parametros
        resposta = requests.post(MCP, headers=cabecalho, json=corpo, timeout=120)
        # `text/event-stream` chega sem charset, e aí o `requests` assume
        # ISO-8859-1: `movimentações` viraria `movimentaÃ§Ãµes`.
        resposta.encoding = "utf-8"
        self.sessao = resposta.headers.get("Mcp-Session-Id") or self.sessao
        if avisar:
            return {}
        for linha in resposta.text.splitlines():
            if linha.startswith("data: "):
                return json.loads(linha[6:])
        return resposta.json()

    def ferramentas(self) -> list[str]:
        return [f["name"] for f in self._chamar("tools/list", {})["result"]["tools"]]

    def estoque_publicado(self) -> dict:
        """O que a documentação publica sobre o grupo Estoque.

        Não pede login: ler a documentação não exige conta.
        """
        retorno = self._chamar("tools/call", {"name": "listar_endpoints",
                                              "arguments": {"lang": "pt"}})
        lista = json.loads(retorno["result"]["content"][0]["text"])

        grupos: dict[str, dict[str, int]] = {}
        for rota in lista["items"]:
            g = grupos.setdefault(rota["group"], {"rotas": 0, "escrita": 0})
            g["rotas"] += 1
            if rota["method"] != "GET":
                g["escrita"] += 1
        estoque = [r for r in lista["items"] if r["group"] == "Estoque"]
        return {
            "rotasDeNegocio": lista["total"],
            "grupos": grupos,
            "estoque": {
                "rotas": len(estoque),
                "deEscrita": sum(1 for r in estoque if r["method"] != "GET"),
                "escopos": sorted({r["scope"] for r in estoque}),
                "lista": [{k: r[k] for k in ("method", "path", "title", "scope")}
                          for r in estoque],
            },
        }

    def api(self, metodo: str, caminho: str, consulta: dict | None = None,
            corpo=None) -> dict:
        """Chama `execute_beefood_request` — é ela que fala com a API de verdade."""
        argumentos: dict = {"method": metodo, "path": caminho}
        if consulta:
            argumentos["query"] = consulta
        if corpo is not None:
            argumentos["body"] = corpo
        retorno = self._chamar("tools/call", {
            "name": "execute_beefood_request", "arguments": argumentos})
        estruturado = retorno.get("result", {}).get("structuredContent")
        if estruturado and estruturado.get("ok"):
            return estruturado.get("body")
        raise SystemExit(f"ERRO em {metodo} {caminho}: {json.dumps(retorno)[:400]}")


def saldo_de(conversa: Conversa, item: dict) -> dict:
    """Lê a linha de um item pela rota de listagem, que é a que tem o saldo.

    A demonstração de escrita lê o mesmo item três vezes — antes, depois e
    depois de desfazer —, e a API devolve `429` para requisição **idêntica**
    enviada em menos de quatro segundos. A pausa é o limite publicado do
    servidor, não contorno: `docs.beefood.app/docs/limites`.
    """
    chave = next(k for k in ("productId", "supplyId", "complementId") if k in item)
    time.sleep(5)
    resposta = conversa.api("GET", "/v1/stock/items",
                            {chave: item[chave], "type": item["type"], "limit": 1})
    linha = next((i for i in resposta["items"] if i.get(chave) == item[chave]), None)
    if not linha:
        raise SystemExit(f"ERRO: {item['nome']} não apareceu na listagem de estoque")
    return linha


def mover(conversa: Conversa, item: dict, operacao: str, quantidade: float) -> list:
    """Manda uma linha de `PATCH /v1/stock/items` e devolve a resposta."""
    chave = next(k for k in ("productId", "supplyId", "complementId") if k in item)
    corpo = [{"type": item["type"], chave: item[chave],
              "operation": operacao, "stockQuantity": quantidade}]
    resposta = conversa.api("PATCH", "/v1/stock/items", corpo=corpo)
    if not resposta or not resposta[0].get("success"):
        raise SystemExit(f"ERRO: a movimentação falhou: {json.dumps(resposta)}")
    return corpo, resposta



def escrever(conversa: Conversa) -> dict:
    """Dá a entrada do exemplo do release e devolve o saldo ao que era.

    O `new` grava o saldo informado no lugar do atual, então a volta é exata:
    não sobra quantidade e não fica configuração mexida. O que sobra são duas
    linhas no histórico de movimentações, que é justamente o que a rota de
    histórico existe para mostrar — e é sandbox.
    """
    antes = saldo_de(conversa, DEMO)
    inicial = antes["stockQuantity"]
    print(f"--> {DEMO['nome']}: saldo antes = {inicial}")

    corpo, resposta = mover(conversa, DEMO, "add", ENTRADA)
    depois = saldo_de(conversa, DEMO)
    print(f"--> entrada de {ENTRADA}: saldo agora = {depois['stockQuantity']}")

    _, volta = mover(conversa, DEMO, "new", inicial)
    final = saldo_de(conversa, DEMO)

    if final["stockQuantity"] != inicial:
        raise SystemExit(f"ERRO: o saldo NÃO voltou ({final['stockQuantity']} "
                         f"!= {inicial}). Rode --restaurar {inicial}")
    print(f"--> saldo devolvido ao que era = {final['stockQuantity']}")

    return {
        "comoOReleaseDiz": "dê entrada de 20 unidades de refrigerante",
        "item": {"nome": DEMO["nome"], "tipo": DEMO["type"], "unidade": antes["unit"]},
        "rota": "PATCH /v1/stock/items",
        "escopo": "stock:write",
        "porOndeFoi": "MCP, pela ferramenta execute_beefood_request",
        "saldoAntes": inicial,
        "corpoEnviado": corpo,
        "respostaDaEntrada": resposta,
        "saldoDepois": depois["stockQuantity"],
        "desfeito": {"corpo": "operation new com o saldo original",
                     "resposta": volta,
                     "saldoFinal": final["stockQuantity"]},
        "oSaldoVoltou": final["stockQuantity"] == inicial,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--escrever", action="store_true",
                    help="dá a entrada do exemplo do release e a desfaz")
    ap.add_argument("--retrato", action="store_true",
                    help="fotografa a linha de Estoque na tela de autorização")
    ap.add_argument("--restaurar", type=float, metavar="SALDO",
                    help="devolve o saldo do item da demonstração a um valor")
    ap.add_argument("--meses", type=int, default=6,
                    help="janela do histórico; o servidor aceita no máximo 6")
    args = ap.parse_args()

    conversa = Conversa(conectar(AQUI if args.retrato else None))

    if args.restaurar is not None:
        mover(conversa, DEMO, "new", args.restaurar)
        print(f"--> saldo de {DEMO['nome']} devolvido a {args.restaurar}")
        return 0

    # O "hoje" é o da LOJA. O Cloud Agent roda em UTC, e depois das 21h de
    # Brasília `date.today()` já virou o dia seguinte — a janela andaria 24 h.
    hoje = dt.datetime.now(dt.timezone(dt.timedelta(hours=-3))).date()
    de = hoje - dt.timedelta(days=30 * args.meses - 5)

    publicado = conversa.estoque_publicado()

    # A mesma pergunta do release — "quais insumos estão abaixo do mínimo?" —
    # é UM filtro de UMA rota. É o fato do slide da consulta.
    baixos = conversa.api("GET", "/v1/stock/items",
                          {"stockSituation": "low", "limit": 20})
    controlados = conversa.api("GET", "/v1/stock/items",
                               {"stockControl": "true", "limit": 1})
    porTipo = {t: conversa.api("GET", "/v1/stock/items", {"type": t, "limit": 1})["total"]
               for t in ("supply", "product", "complement")}
    tudo = conversa.api("GET", "/v1/stock/items", {"limit": 1})
    categorias = conversa.api("GET", "/v1/stock/categories", {"limit": 50})
    historico = conversa.api("GET", "/v1/stock/movements",
                             {"fromDate": de.isoformat(), "toDate": hoje.isoformat(),
                              "limit": 3})

    # O limite de 6 meses é promessa do release; aqui ele é MEDIDO, pedindo
    # uma janela maior de propósito e guardando o que o servidor responde.
    largo = requests.get(
        f"{API}/v1/stock/movements", timeout=60,
        headers={"Authorization": "Bearer invalido-de-proposito"},
        params={"fromDate": (hoje - dt.timedelta(days=200)).isoformat(),
                "toDate": hoje.isoformat()})

    cred = credencial()
    emissao = requests.post(f"{API}/v1/oauth/token", timeout=40, json={
        "grantType": "client_credentials",
        "clientId": cred["clientId"], "clientSecret": cred["clientSecret"]})
    emissao.raise_for_status()
    porta_direta = requests.get(
        f"{API}/v1/stock/movements", timeout=60,
        headers={"Authorization": f"Bearer {emissao.json()['accessToken']}"},
        params={"fromDate": (hoje - dt.timedelta(days=200)).isoformat(),
                "toDate": hoje.isoformat()})

    pessoal = [c for i in baixos["items"] for c in i
               if any(p in c.lower() for p in ("name", "phone", "mail", "cpf",
                                               "doc", "customer"))
               and c != "name" and c != "categoryName"]
    if pessoal:
        raise SystemExit(f"ERRO: campo pessoal na resposta: {pessoal}")

    saida = {
        "lido_em": dt.datetime.now().isoformat(timespec="seconds"),
        "conta": "sandbox BeeFood3 - Manual (empresa 38311)",
        "asDuasPortas": {
            "apiAberta": {"base": API, "token": "POST /v1/oauth/token",
                          "permissao": "Aplicativos → API Aberta, Consultar e Alterar"},
            "mcp": {"servidor": conversa.servidor, "endereco": MCP,
                    "ferramentas": conversa.ferramentas(),
                    "permissao": "Aplicativos → MCP, autorizar Estoque"},
        },
        "oQueADocumentacaoPublica": publicado,
        "oQueALojaTem": {
            "itens": tudo["total"],
            "porTipo": porTipo,
            "comControleLigado": controlados["total"],
            "categoriasDeInsumo": [c["name"] for c in categorias["items"]],
        },
        "abaixoDoMinimo": {
            "comoAPerguntaDoReleaseDiz": "quais insumos estão abaixo do mínimo?",
            "rota": "GET /v1/stock/items?stockSituation=low",
            "total": baixos["total"],
            "itens": baixos["items"],
        },
        "historico": {
            "rota": "GET /v1/stock/movements",
            "janela": {"fromDate": de.isoformat(), "toDate": hoje.isoformat()},
            "total": historico["total"],
            "primeiros": historico["items"],
            "limiteDeJanela": {
                "pedido": "200 dias",
                "status": porta_direta.status_code,
                "resposta": porta_direta.json(),
                "semToken": largo.status_code,
            },
        },
    }
    if args.escrever:
        saida["escrita"] = escrever(conversa)

    (AQUI / "chamadas.json").write_text(
        json.dumps(saida, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(saida, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
