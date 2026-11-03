"""Captura a configuração e o uso do código de barras que manda o pedido para PRONTO (#132).

São duas peças que o manual precisa fotografar juntas:

* a caixinha **Código de barras envia pedido para PRONTO**, no layout do *Cupom Pedido*,
  que põe o EAN-13 do `preVendaID` no cupom de **qualquer** pedido do módulo Delivery;
* o leitor da tela `/delivery`, que já existe e está sempre ligado, movendo o pedido de
  AGUARDANDO ou PREPARO para **PRONTO**.

Cenário: a fila do sandbox abre vazia, então o script semeia dois pedidos pela mesma rota
que a tela usa (`POST /api/venda2/salvar`) — um de **retirada** e um de **entrega**. A prova
que interessa é a do pedido de retirada: a flag antiga (*Código de Barras App Entrega*) só
imprime em entrega com endereço, então um código de barras no cupom de retirada só pode ter
vindo da flag nova.

Identificação do lixo que este script cria, para o `limpar` não encostar em pedido de
verdade: o `semear` anota em `/tmp` os `preVendaID` que acabou de criar, e cada um ainda
precisa casar com um dos nomes fictícios do `CENARIO` e com `origem = Manual`. As
observações ficam **vazias** de propósito — elas saem impressas no cupom, e o cupom é uma
das imagens do manual.

A leitura é simulada pelo teclado, porque o leitor é um teclado: `useLeitorCodigoBarras`
exige menos de 50 ms entre dígitos e fecha no Enter, com o foco **fora** de campo de texto.
`page.keyboard.type(codigo, delay=10)` cumpre as duas condições.

Comandos:

    python3 capturar.py estado     # flags do layout e fila de hoje
    python3 capturar.py semear     # cria os dois pedidos já em PREPARO
    python3 capturar.py capturar   # cupom antes, liga a flag, fotografa, bipa e erra
    python3 capturar.py capturar cupom leitura   # repete só parte das imagens
    python3 capturar.py rebobinar  # devolve os pedidos para PREPARO e repete a leitura
    python3 capturar.py limpar     # cancela os pedidos e devolve as flags como estavam

Trava de segurança: só a sandbox 38311/39202.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "painel-entregador"))

from playwright.sync_api import sync_playwright
from beefood import abrir, after_click, api_get, api_post, limpar_tela, sessao

AQUI = Path(__file__).resolve().parent
PURAS = AQUI / "imagens-puras"
PURAS.mkdir(parents=True, exist_ok=True)
ESTADO = Path("/tmp/barras-pronto-estado.json")

EMPRESA_PERMITIDA = 38311
FILIAL_PERMITIDA = 39202

PAINEL = "https://beefood.app"

# Produtos reais do cardápio do sandbox.
P = {
    "chicken": (2659733, "Chicken Deluxe", 29.0),
    "batata": (2659761, "Batata Frita Crocante da One - Porção Média 150 g", 14.0),
    "coca": (2659705, "Coca Zero 350ml", 9.0),
    "brownie": (2659770, "Brownie da One", 14.0),
}

ENDERECO = {
    "clienteEnderecoID": None, "cep": "18085-000", "endereco": "Avenida Ipanema",
    "numero": "3000", "bairro": "Jardim Piratininga", "complemento": None,
    "cidade": "Sorocaba", "cidadeID": None, "estado": "SP", "estadoID": None,
    "latitude": None, "longitude": None, "km": None, "google_place_id": None,
}

# Um de cada tipo: a flag nova vale para os dois, e é isso que a diferencia da antiga.
CENARIO = [
    {
        "apelido": "retirada",
        "tipoPedido": "RETIRADA",
        "cliente": "Marina Oliveira",
        "itens": [("chicken", 1), ("batata", 1), ("coca", 1)],
        "pag": "PIX",
        "frete": 0.0,
    },
    {
        "apelido": "entrega",
        "tipoPedido": "DELIVERY",
        "cliente": "Rafael Dias",
        "itens": [("chicken", 2), ("brownie", 1)],
        "pag": "Dinheiro",
        "frete": 6.5,
    },
]


def conferir_alvo(s: dict):
    if int(s["empresaID"]) != EMPRESA_PERMITIDA or int(s["filialID"]) != FILIAL_PERMITIDA:
        raise SystemExit(
            f"ABORTADO: alvo {s['empresaID']}/{s['filialID']} fora da sandbox "
            f"{EMPRESA_PERMITIDA}/{FILIAL_PERMITIDA}"
        )


def ean13(valor: int | str) -> str:
    """O mesmo cálculo de `gerarEAN13SVG`, em `src/lib/impressao-service.ts`."""
    base = str(valor).rjust(12, "0")[-12:]
    soma = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(base))
    return base + str((10 - soma % 10) % 10)


def montar_payload(s: dict, caso: dict) -> dict:
    agora = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    produtos, total = [], 0.0
    for chave, qtd in caso["itens"]:
        pid, nome, preco = P[chave]
        total += round(preco * qtd, 2)
        produtos.append({
            "preVendaServicoID": None, "preVendaID": None, "usuarioID": s["usuarioID"],
            "produtoID": pid, "qtd": float(qtd), "custo": 0, "venda": preco,
            "descricao": nome, "obsVenda": None, "semTaxaServico": False,
            "dataHoraLancamento": agora, "impresso": None, "mobile": True,
            "valorOpcoes": 0,
        })
    total = round(total, 2)
    frete = caso["frete"]
    entrega = caso["tipoPedido"] == "DELIVERY"
    return {
        "preVendaID": None, "numeroPreVenda": None, "esteira": False,
        "empresaID": s["empresaID"], "filialID": s["filialID"], "filialIDOrigem": None,
        "usuarioID": s["usuarioID"], "funcionarioID": None,
        "tipo": "DELIVERY", "situacao": "ABERTO", "nomeAvulso": None,
        "obsx": None,
        "pdvImprimirCozinhaAposPagamento": False,
        "delivery": {
            "situacaoDelivery": "PREPARO",
            "tipoPedido": caso["tipoPedido"],
            "agendamento": None, "funcionarioID": None,
            "tipoPagStr": caso["pag"], "tipoPagBandeiraStr": None, "troco": None,
        },
        "mesa": None, "produtos": produtos,
        "valores": {
            "produtos": total, "acrescimo": 0, "taxaEntrega": frete,
            "valorEntregador": 0,
            "taxaServico": {"tipo": "R$", "valor": 0, "total": 0},
            "desconto": {"tipo": "R$", "valor": 0},
            "valorTotal": round(total + frete, 2), "valorPago": 0,
        },
        "cliente": {
            "clienteID": None, "nome": caso["cliente"], "cpf_cnpj": None,
            "telefone": None,
            "endereco": dict(ENDERECO) if entrega else None,
        },
    }


def pedidos_da_janela(page, s: dict, horas: int = 12) -> list:
    st, lista = api_get(
        page, f"/api/venda2/delivery/{s['empresaID']}/{s['filialID']}/{s['usuarioID']}/{horas}"
    )
    if st != 200:
        raise SystemExit(f"listagem falhou: {st} {lista}")
    return lista if isinstance(lista, list) else []


def estado_salvo() -> dict:
    return json.loads(ESTADO.read_text(encoding="utf-8")) if ESTADO.exists() else {}


def meus_pedidos(page, s: dict) -> list:
    ids = set(estado_salvo().get("pedidos") or [])
    nomes = {c["cliente"] for c in CENARIO}
    return [
        p for p in pedidos_da_janela(page, s)
        if p.get("preVendaID") in ids
        and p.get("nome") in nomes
        and str(p.get("origem")) == "Manual"
    ]


def layout_delivery(page, s: dict) -> dict:
    _, lista = api_get(
        page, f"/api/empresa2/impressaoLayout/{s['empresaID']}/{s['usuarioID']}"
    )
    for l in lista if isinstance(lista, list) else []:
        if str(l.get("tipo")).upper() == "DELIVERY":
            return l
    raise SystemExit("layout DELIVERY não encontrado")


def rotulo_cartao(p: dict) -> str:
    """O cartão da fila mostra `#<numeroPedido> (<numeroPreVenda>)`."""
    return f"#{p.get('numeroPedido')} ({p.get('numeroPreVenda')})"


# ---------------------------------------------------------------- estado / semear / limpar

def cmd_estado(page, s: dict):
    l = layout_delivery(page, s)
    print("layout DELIVERY: beeEntregaCodigoBarras=%r beeCodigoBarrasPronto=%r"
          % (l.get("beeEntregaCodigoBarras"), l.get("beeCodigoBarrasPronto")))
    for p in pedidos_da_janela(page, s):
        print(f"  {p['preVendaID']:>9}  {str(p.get('situacaoDelivery')):<11}"
              f" {str(p.get('tipoPedido')):<9} {rotulo_cartao(p):<14} {p.get('nome')}")


def cmd_semear(page, s: dict):
    """Guarda as flags originais antes de qualquer escrita, para o `limpar` devolvê-las."""
    l = layout_delivery(page, s)
    anotado = estado_salvo()
    anotado.setdefault("beeEntregaCodigoBarras", l.get("beeEntregaCodigoBarras"))
    anotado.setdefault("beeCodigoBarrasPronto", l.get("beeCodigoBarrasPronto"))
    anotado.setdefault("pedidos", [])
    ESTADO.write_text(json.dumps(anotado), encoding="utf-8")
    print("estado original guardado em", ESTADO, ESTADO.read_text())

    for caso in CENARIO:
        st, resp = api_post(page, "/api/venda2/salvar", montar_payload(s, caso))
        print(f"\n== {caso['apelido']} ==\n   POST salvar {st}",
              json.dumps(resp, ensure_ascii=False)[:160])
        if st == 200 and isinstance(resp, dict) and resp.get("preVendaID"):
            anotado["pedidos"].append(int(resp["preVendaID"]))
            ESTADO.write_text(json.dumps(anotado), encoding="utf-8")
    print()
    for p in meus_pedidos(page, s):
        print(f"   {p['preVendaID']} {p.get('situacaoDelivery')} {p.get('tipoPedido')}"
              f" {rotulo_cartao(p)} -> EAN {ean13(p['preVendaID'])}")


def cmd_limpar(page, s: dict):
    for p in meus_pedidos(page, s):
        if str(p.get("situacaoDelivery")) == "CANCELADO":
            continue
        st, r = api_post(page, "/datasnap/rest/venda2/atualizaSituacaoDelivery", {
            "empresaID": s["empresaID"], "filialID": s["filialID"],
            "usuarioID": s["usuarioID"], "usuario": s["usuario"], "clienteID": None,
            "situacaoDelivery": "CANCELADO",
            "situacaoDeliveryAnterior": p.get("situacaoDelivery"),
            "preVendaID": p["preVendaID"], "numeroPreVenda": p.get("numeroPreVenda"),
            "numeroPedido": p.get("numeroPedido"), "tipoPedido": p.get("tipoPedido"),
            "origem": p.get("origem"), "tipoPagStr": p.get("tipoPagStr"),
            "tipo": "DELIVERY", "esteira": False,
            "funcionarioID": s.get("funcionarioID"),
            "motivoCancelamento": "Limpeza do cenário do manual #132",
        })
        print("cancelar", p["preVendaID"], st, json.dumps(r, ensure_ascii=False)[:120])

    salvo = estado_salvo()
    if "beeCodigoBarrasPronto" in salvo:
        l = layout_delivery(page, s)
        l["beeEntregaCodigoBarras"] = salvo["beeEntregaCodigoBarras"]
        l["beeCodigoBarrasPronto"] = salvo["beeCodigoBarrasPronto"]
        st, r = api_post(page, "/api/empresa2/impressaoLayout",
                         dict(l, empresaID=s["empresaID"], usuarioID=s["usuarioID"],
                              usuario=s["usuario"], log={}))
        print("devolver flags", st, json.dumps(r, ensure_ascii=False)[:120])
        l = layout_delivery(page, s)
        print("confere: beeEntregaCodigoBarras=%r beeCodigoBarrasPronto=%r"
              % (l.get("beeEntregaCodigoBarras"), l.get("beeCodigoBarrasPronto")))


# ---------------------------------------------------------------------------- capturas

def tirar(page, nome):
    page.screenshot(path=str(PURAS / nome))
    print("pura:", nome)


def descansar_foco(page):
    """Sem foco e sem mouse em cima de botão: o leitor exige foco fora de campo, e a
    captura não pode mostrar elemento pintado de hover."""
    page.evaluate("() => document.activeElement && document.activeElement.blur()")
    page.mouse.move(720, 860)
    page.wait_for_timeout(600)


def gancho_cupom(page):
    """O cupom do navegador é escrito num iframe oculto (`imprimirViaIframe`).

    O gancho guarda o HTML e neutraliza o `print()`, senão o diálogo nativo do sistema
    trava o Playwright. Técnica herdada do manual #99.
    """
    page.evaluate(
        """() => {
          window.__cupomHTML = null;
          const pegar = () => {
            const f = document.getElementById('beefood-print-frame');
            if (!f) return;
            try {
              const doc = f.contentDocument;
              if (doc && doc.body && (doc.body.innerText || '').trim().length > 20) {
                window.__cupomHTML = doc.documentElement.outerHTML;
                if (f.contentWindow) f.contentWindow.print = () => {};
              }
            } catch (e) {}
          };
          new MutationObserver(pegar).observe(document.documentElement,
                                              { childList: true, subtree: true });
          setInterval(pegar, 40);
        }"""
    )


def render_cupom(ctx, html: str, nome: str, pe: str | None = None):
    """Fotografa o cupom inteiro e, se `pe` vier, também o pé dele de perto.

    A viewport fica perto do conteúdo porque `full_page` herda a altura dela, e um cupom
    numa janela alta sai com um palmo de branco embaixo. O recorte do pé é uma captura
    com `clip`, não um corte da pura: nada se edita depois de gravado.
    """
    cupom = ctx.new_page()
    cupom.set_viewport_size({"width": 420, "height": 480})
    cupom.set_content(html, wait_until="domcontentloaded")
    cupom.wait_for_timeout(1500)
    cupom.screenshot(path=str(PURAS / nome), full_page=True)
    print("pura:", nome, "| tem código de barras:", "<svg" in html)
    if pe:
        barras = cupom.locator("svg").first
        if barras.count():
            caixa = barras.bounding_box()
            altura = cupom.evaluate("() => document.documentElement.scrollHeight")
            # 85 px acima do código entra a linha inteira do "Cobrar do Cliente"; menos
            # que isso corta a linha no meio da letra.
            y = max(0, caixa["y"] - 85)
            cupom.screenshot(
                path=str(PURAS / pe), full_page=True,
                clip={"x": 0, "y": y, "width": 420,
                      "height": min(altura - y, caixa["height"] + 185)},
            )
            print("pura:", pe)
        else:
            print("AVISO: cupom sem <svg>, recorte do pé não foi feito")
    cupom.close()


def abrir_fila(page):
    page.goto(f"{PAINEL}/delivery", wait_until="domcontentloaded")
    after_click(page, 9000)
    limpar_tela(page)
    descansar_foco(page)


def imprimir_cupom(page, ctx, alvo: dict) -> str:
    """Abre o pedido na fila, aperta a impressora do painel e devolve o HTML do cupom.

    São dois botões de impressora na tela: o `h-5` do painel do pedido, que é este, e o
    `h-4 text-red-500` do alto, que é o status do BeeImpressão e abre outra janela.
    """
    abrir_fila(page)
    gancho_cupom(page)
    page.get_by_text(rotulo_cartao(alvo), exact=True).first.click()
    after_click(page, 9000)
    page.evaluate("() => { window.__cupomHTML = null; }")
    page.locator("button:has(svg.lucide-printer.h-5)").first.click()
    for _ in range(80):
        html = page.evaluate("() => window.__cupomHTML")
        if html:
            return html
        page.wait_for_timeout(250)
    raise SystemExit("o cupom do navegador não apareceu")


def cap_cupom_sem(page, ctx, alvo: dict):
    """04: o mesmo cupom antes de ligar a caixinha — o lado 'antes' do par."""
    html = imprimir_cupom(page, ctx, alvo)
    if "<svg" in html:
        raise SystemExit("ABORTADO: a flag já estava ligada, o par antes/depois não vale")
    render_cupom(ctx, html, "04-cupom-sem-codigo-barras.png")


def cap_botao_imprimir(page, alvo: dict):
    """03: de onde o cupom sai quando se imprime um pedido pela tela."""
    abrir_fila(page)
    page.get_by_text(rotulo_cartao(alvo), exact=True).first.click()
    after_click(page, 9000)
    descansar_foco(page)
    tirar(page, "03-botao-imprimir-cupom.png")


def cap_configuracao(page, s: dict):
    """01 e 02: onde a caixinha mora, e a caixinha marcada."""
    page.goto(f"{PAINEL}/impressao", wait_until="domcontentloaded")
    after_click(page, 10000)
    limpar_tela(page)
    page.get_by_role("button", name="Layout", exact=True).click()
    after_click(page, 5000)
    descansar_foco(page)
    tirar(page, "01-aba-layout-cupom-pedido.png")

    page.get_by_text("Cupom Pedido", exact=True).first.click()
    after_click(page, 6000)
    dlg = page.locator('[role="dialog"]').last
    dlg.get_by_text("Texto Padrão", exact=True).first.click()
    after_click(page, 4000)
    caixa = dlg.get_by_text("Código de barras envia pedido para PRONTO", exact=True).first
    caixa.click()
    page.wait_for_timeout(1200)
    page.mouse.move(1150, 300)
    page.wait_for_timeout(600)
    tirar(page, "02-caixinha-codigo-barras-pronto.png")

    dlg.get_by_role("button", name="SALVAR E FECHAR").click()
    after_click(page, 7000)
    print("flag depois de salvar:",
          layout_delivery(page, s).get("beeCodigoBarrasPronto"))


def cap_cupom_com(page, ctx, alvo: dict):
    """05 e 06: o cupom depois de ligar a caixinha, inteiro e com o pé de perto."""
    html = imprimir_cupom(page, ctx, alvo)
    if "<svg" not in html:
        raise SystemExit("ABORTADO: cupom saiu sem código de barras, confira a flag")
    render_cupom(ctx, html, "05-cupom-com-codigo-barras.png",
                 pe="06-codigo-no-pe-do-cupom.png")
    (Path("/tmp") / "cupom-retirada-flag-on.html").write_text(html, encoding="utf-8")


def cap_leitura(page, s: dict, alvo: dict):
    """07 e 08: a fila antes e depois de bipar o código."""
    abrir_fila(page)
    tirar(page, "07-fila-antes-da-leitura.png")

    codigo = ean13(alvo["preVendaID"])
    print("bipando", codigo, "(preVendaID", alvo["preVendaID"], ")")
    page.keyboard.type(codigo, delay=10)
    page.keyboard.press("Enter")
    # O aviso entra deslizando da direita: espera ele aparecer e só então assenta.
    page.get_by_text("marcado como Pronto").first.wait_for(timeout=20000)
    page.wait_for_timeout(2000)
    tirar(page, "08-pedido-em-pronto.png")
    print("fila depois:",
          [(p["preVendaID"], p.get("situacaoDelivery")) for p in meus_pedidos(page, s)])


def cap_aviso(page, codigo: str, trecho: str, nome: str):
    """09 e 10: os dois avisos que a tela dá quando o bipe não move nada.

    Recarrega a fila antes de cada bipe porque o aviso anterior pode ainda estar na
    tela, e duas tarjas empilhadas não explicam nada.
    """
    abrir_fila(page)
    print("bipando", codigo, "esperando:", trecho)
    page.keyboard.type(codigo, delay=10)
    page.keyboard.press("Enter")
    page.get_by_text(trecho).first.wait_for(timeout=20000)
    page.wait_for_timeout(1800)
    tirar(page, nome)


def cmd_rebobinar(page, s: dict):
    """Devolve os pedidos do cenário para PREPARO, para repetir a captura da leitura."""
    for p in meus_pedidos(page, s):
        if str(p.get("situacaoDelivery")) in ("PREPARO", "CANCELADO"):
            continue
        st, r = api_post(page, "/datasnap/rest/venda2/atualizaSituacaoDelivery", {
            "empresaID": s["empresaID"], "filialID": s["filialID"],
            "usuarioID": s["usuarioID"], "usuario": s["usuario"], "clienteID": None,
            "situacaoDelivery": "PREPARO",
            "situacaoDeliveryAnterior": p.get("situacaoDelivery"),
            "preVendaID": p["preVendaID"], "numeroPreVenda": p.get("numeroPreVenda"),
            "numeroPedido": p.get("numeroPedido"), "tipoPedido": p.get("tipoPedido"),
            "origem": p.get("origem"), "tipoPagStr": p.get("tipoPagStr"),
            "tipo": "DELIVERY", "esteira": False,
            "funcionarioID": s.get("funcionarioID"),
        })
        print("voltar para PREPARO", p["preVendaID"], st,
              json.dumps(r, ensure_ascii=False)[:120])


def cmd_capturar(page, ctx, s: dict, passos: set[str]):
    # Rodada anterior deixa os pedidos cancelados anotados no estado; eles não servem
    # de alvo, e o cartão deles nem aparece na fila.
    pedidos = [p for p in meus_pedidos(page, s)
               if str(p.get("situacaoDelivery")) != "CANCELADO"]
    if not pedidos:
        raise SystemExit("nenhum pedido vivo do cenário na janela — rode `semear` primeiro")
    por_tipo = {str(p.get("tipoPedido")).upper(): p for p in pedidos}
    # BALCAO é como a API grava o pedido de retirada.
    alvo = por_tipo.get("BALCAO") or por_tipo.get("RETIRADA") or pedidos[0]
    print("pedido alvo:", alvo["preVendaID"], alvo.get("tipoPedido"), rotulo_cartao(alvo))

    # A ordem aqui não é a ordem do manual: o cupom "antes" só existe enquanto a
    # caixinha está desligada, então ele tem que ser fotografado antes do passo config.
    if "antes" in passos:
        if layout_delivery(page, s).get("beeCodigoBarrasPronto"):
            raise SystemExit("ABORTADO: caixinha já ligada — o cupom 'antes' não sai")
        cap_cupom_sem(page, ctx, alvo)
    if "config" in passos:
        cap_configuracao(page, s)
    if "botao" in passos:
        cap_botao_imprimir(page, alvo)
    if "cupom" in passos:
        cap_cupom_com(page, ctx, alvo)
    if "leitura" in passos:
        cap_leitura(page, s, alvo)
    if "avisos" in passos:
        cap_aviso(page, ean13(alvo["preVendaID"]), "já está em",
                  "09-pedido-ja-esta-em-pronto.png")
        cap_aviso(page, "999999999", "não encontrado",
                  "10-pedido-nao-encontrado.png")


if __name__ == "__main__":
    comando = sys.argv[1] if len(sys.argv) > 1 else "estado"
    with sync_playwright() as p:
        browser, ctx, page = abrir(p, "/delivery")
        s = sessao(page)
        s["usuario"] = s.get("usuario") or "Principal"
        conferir_alvo(s)
        print("SESSAO", {k: v for k, v in s.items() if k != "token"}, "\n")
        if comando == "estado":
            cmd_estado(page, s)
        elif comando == "semear":
            cmd_semear(page, s)
        elif comando == "capturar":
            pedidos = set(sys.argv[2:]) or {"antes", "config", "botao", "cupom",
                                            "leitura", "avisos"}
            cmd_capturar(page, ctx, s, pedidos)
        elif comando == "rebobinar":
            cmd_rebobinar(page, s)
        elif comando == "limpar":
            cmd_limpar(page, s)
        else:
            print("comando desconhecido:", comando)
        browser.close()
