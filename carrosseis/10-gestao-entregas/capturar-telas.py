#!/usr/bin/env python3
"""Capturas do carrossel da Gestão de Entregas.

A tela é uma só — `/gestao-entregas` —, e ela lê dois endpoints:

    GET /api/entrega2/gestao/painel/{empresa}/{filial}/{usuario}    a cada 30 s
    GET /api/entrega2/gestao/posicoes/{empresa}/{filial}/{usuario}  a cada 10 s

Este script intercepta os dois e aplica o `cena.json`: as rotas A e B, os
entregadores com posição recente e os pedidos de exemplo que a fila da sandbox
não tem. Nada é escrito no servidor.

    python capturar-telas.py                 # todas as telas
    python capturar-telas.py --só mapa       # uma etapa
    python capturar-telas.py --cru           # sem a cena, para comparar
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.append(".cursor/skills/carrossel/scripts")
from capturar import esperar, limpar, sessao  # noqa: E402

PASTA = Path(__file__).resolve().parent
PURAS = PASTA / "imagens-puras"
CENA = json.loads((PASTA / "cena.json").read_text(encoding="utf-8"))

PAINEL = "https://beefood.app/gestao-entregas"
APLICATIVOS = "https://beefood.app/aplicativos"
ROTA_PAINEL = "**/entrega2/gestao/painel/**"
ROTA_POSICOES = "**/entrega2/gestao/posicoes/**"
ROTA_DESPACHO = "**/entrega2/gestao/despacho/config/**"

# O dispositivo `painel` do `capturar.py` é 1440×900 com DPR 2 — é a medida em
# que o recorte de meia tela chega ao slide em escala 1.
ZOOM_EXTRA = 1


def montar_pedidos() -> list[dict]:
    """O payload de pedido que o front espera, a partir do `cena.json`."""
    pedidos = []
    for p in CENA["pedidos"]:
        rota_id = None
        for rota in CENA["rotas"]:
            if any(par["preVendaID"] == p["preVendaID"] for par in rota["paradas"]):
                rota_id = rota["rotaID"]
        pedidos.append({
            "preVendaID": p["preVendaID"],
            "numero": p["numero"],
            "numeroPreVenda": str(p["numero"]),
            "numeroPedido": str(p["numero"]),
            "cliente": p["cliente"],
            "clienteID": None,
            "status": p["status"],
            "latitude": p["latitude"],
            "longitude": p["longitude"],
            "semLocalizacao": p["latitude"] is None,
            "enderecoResumo": p["enderecoResumo"],
            "complemento": None,
            "cep": None,
            "formaPagamento": p["formaPagamento"],
            "origem": p["origem"],
            "marketplaceID": None,
            "idadeMinutos": p["idadeMinutos"],
            "rotaID": rota_id,
        })
    return pedidos


def montar_entregadores() -> list[dict]:
    return [{
        "funcionarioID": e["funcionarioID"],
        "nome": e["nome"],
        "telefone": None,
        "veiculoTipo": None,
        "capacidadeMaxima": None,
        "online": e["online"],
        "status": e["status"],
        "rotaIDAtual": e["rotaIDAtual"],
        "latitude": e["latitude"],
        "longitude": e["longitude"],
        "posicaoIdadeMinutos": e["posicaoIdadeMinutos"],
        "distanciaLojaMetros": e["distanciaLojaMetros"],
        "bateria": e["bateria"],
        "semRegistroDeUso": e.get("semRegistroDeUso", False),
    } for e in CENA["entregadores"]]


def montar_rotas() -> list[dict]:
    por_id = {p["preVendaID"]: p for p in CENA["pedidos"]}
    rotas = []
    for rota in CENA["rotas"]:
        paradas = [{
            "preVendaID": par["preVendaID"],
            "numeroPedido": str(por_id[par["preVendaID"]]["numero"]),
            "ordem": par["ordem"],
            "status": par["status"],
            "clienteNome": por_id[par["preVendaID"]]["cliente"],
            "enderecoResumo": por_id[par["preVendaID"]]["enderecoResumo"],
            "latitude": por_id[par["preVendaID"]]["latitude"],
            "longitude": por_id[par["preVendaID"]]["longitude"],
            "valorTotal": por_id[par["preVendaID"]]["valorTotal"],
            "formaPagamento": por_id[par["preVendaID"]]["formaPagamento"],
            "motivoInsucesso": None,
        } for par in rota["paradas"]]
        rotas.append({
            "rotaID": rota["rotaID"],
            "codigo": rota["codigo"],
            "funcionarioID": rota["funcionarioID"],
            "status": rota["status"],
            "origem": rota["origem"],
            "qtdParadas": len(paradas),
            "qtdEntregues": rota["qtdEntregues"],
            "distanciaTotalMetros": rota["distanciaTotalMetros"],
            "idadeMinutos": rota["idadeMinutos"],
            "paradas": paradas,
        })
    return rotas


def resumo_pedidos(pedidos: list[dict]) -> dict:
    conta = lambda s: sum(1 for p in pedidos if p["status"] == s)  # noqa: E731
    return {
        "emPreparo": conta("EM_PREPARO"),
        "pronto": conta("PRONTO"),
        "emRota": conta("EM_ROTA"),
        "entregue": conta("ENTREGUE"),
        "semLocalizacao": sum(1 for p in pedidos if p["semLocalizacao"]),
        "total": len(pedidos),
    }


def resumo_entregadores(entregadores: list[dict]) -> dict:
    conta = lambda s: sum(1 for e in entregadores if e["status"] == s)  # noqa: E731
    return {
        "disponiveis": conta("DISPONIVEL"),
        "emRota": conta("EM_ROTA"),
        "emPausa": conta("PAUSA"),
        "offline": conta("OFFLINE"),
        "total": len(entregadores),
    }


def painel_da_cena() -> dict:
    pedidos = montar_pedidos()
    entregadores = montar_entregadores()
    return {
        "resultado": True,
        "loja": {
            "filialID": CENA["loja"]["filialID"],
            "nome": CENA["loja"]["nome"],
            "latitude": CENA["loja"]["latitude"],
            "longitude": CENA["loja"]["longitude"],
        },
        "pedidos": pedidos,
        "resumoPedidos": resumo_pedidos(pedidos),
        "entregadores": entregadores,
        "resumoEntregadores": resumo_entregadores(entregadores),
        "rotas": montar_rotas(),
    }


def ligar_cena(pagina) -> None:
    """Reescreve as duas respostas do painel com a cena."""
    painel = painel_da_cena()
    posicoes = {
        "resultado": True,
        "entregadores": painel["entregadores"],
        "resumoEntregadores": painel["resumoEntregadores"],
    }

    despacho = {k: v for k, v in CENA["despacho"].items() if k != "nota"}
    config = {"resultado": True, "existe": True, "config": despacho}

    def responder(rota, corpo):
        # O PUT desta mesma rota grava de verdade: só o GET é reescrito, e o
        # resto segue para o servidor.
        if rota.request.method != "GET":
            rota.continue_()
            return
        rota.fulfill(status=200, content_type="application/json",
                     body=json.dumps(corpo, ensure_ascii=False))

    pagina.route(ROTA_PAINEL, lambda r: responder(r, painel))
    pagina.route(ROTA_POSICOES, lambda r: responder(r, posicoes))
    pagina.route(ROTA_DESPACHO, lambda r: responder(r, config))


def abrir_painel(pagina, cru: bool) -> None:
    if not cru:
        ligar_cena(pagina)
    # O mapa lembra zoom e centro no localStorage e, com eles gravados, ele
    # NÃO enquadra os pinos: abre no último quadro que alguém deixou — que, na
    # sessão reaproveitada do `capturar.py`, é a cidade inteira. Apagadas as
    # duas chaves, o `fitBounds` das coordenadas da cena volta a valer.
    pagina.add_init_script("""
        try {
          localStorage.removeItem('gestaoEntregas.mapaZoom');
          localStorage.removeItem('gestaoEntregas.mapaCentro');
        } catch (e) {}
    """)
    pagina.goto(PAINEL)
    esperar(pagina, 9000)
    limpar(pagina)
    # O mapa carrega os quadrados do OpenStreetMap depois do resto da tela.
    pagina.wait_for_timeout(6000)

    # A tela abre em zoom 14 centrada na loja — é o padrão do sistema, e nele
    # os 500 m entre duas paradas viram 50 px: a linha tracejada da rota
    # desaparece atrás dos pinos. Um passo de zoom põe a cena inteira na tela
    # com o traço legível.
    if ZOOM_EXTRA:
        for _ in range(ZOOM_EXTRA):
            pagina.click("a.leaflet-control-zoom-in")
            pagina.wait_for_timeout(2500)
        pagina.wait_for_timeout(4000)


def salvar(pagina, nome: str, seletor: str | None = None, **kwargs) -> None:
    destino = PURAS / f"{nome}.png"
    alvo = pagina.locator(seletor) if seletor else pagina
    alvo.screenshot(path=str(destino), type="png", **kwargs)
    print("·", destino.relative_to(PASTA.parent.parent))


def tela_inteira(pagina, cru: bool) -> None:
    """A tela completa: mapa com as duas rotas à esquerda, lista à direita."""
    abrir_painel(pagina, cru)
    salvar(pagina, "painel-cru" if cru else "painel-inteiro")


def mapa(pagina, cru: bool) -> None:
    """Só a metade do mapa — é o que vai para a capa."""
    abrir_painel(pagina, cru)
    caixa = pagina.evaluate("""() => {
        const mapa = document.querySelector('.leaflet-container');
        const r = mapa.getBoundingClientRect();
        return { x: r.x, y: r.y, width: r.width, height: r.height };
    }""")
    salvar(pagina, "mapa-rotas", clip=caixa)


def lista_rotas(pagina, cru: bool) -> None:
    """O painel lateral com as duas rotas e as paradas."""
    abrir_painel(pagina, cru)
    caixa = pagina.evaluate("""() => {
        // O painel lateral do computador é a coluna fixa de 380 px.
        const alvo = document.querySelector('[class*="w-[380px]"]');
        const r = alvo.getBoundingClientRect();
        return { x: r.x, y: r.y, width: r.width, height: r.height };
    }""")
    salvar(pagina, "lista-rotas", clip=caixa)


def despacho(pagina, cru: bool) -> None:
    """A janela do despacho automático, com as sete regras."""
    abrir_painel(pagina, cru)
    pagina.click('button[title="Configurar despacho automático"]')
    pagina.wait_for_timeout(2500)
    janela = '[role="dialog"]'
    pagina.wait_for_selector(janela)
    salvar(pagina, "despacho-regras", seletor=janela)
    pagina.keyboard.press("Escape")
    pagina.wait_for_timeout(1200)


def entregadores(pagina, cru: bool) -> None:
    """A lista completa de entregadores: posição, distância e bateria."""
    abrir_painel(pagina, cru)
    pagina.click('button[title="Ver lista completa de entregadores"]')
    pagina.wait_for_timeout(2500)
    janela = '[role="dialog"]'
    pagina.wait_for_selector(janela)
    salvar(pagina, "lista-entregadores", seletor=janela)
    pagina.keyboard.press("Escape")
    pagina.wait_for_timeout(1200)


def avisos(pagina, cru: bool) -> None:
    """Os quatro avisos de WhatsApp da entrega, em WhatsApp → Notificações."""
    pagina.goto("https://beefood.app/whatsapp")
    esperar(pagina, 7000)
    limpar(pagina)
    pagina.click('text=Notificações')
    esperar(pagina, 6000)
    # O grupo Entregador é o último da lista: rola até ele e fotografa a faixa
    # com os três avisos do entregador mais o de proximidade, que é do cliente.
    pagina.evaluate("""() => {
        const alvo = Array.from(document.querySelectorAll('*'))
            .find((e) => e.children.length === 0 && e.textContent.trim() === 'Entregador');
        if (alvo) alvo.scrollIntoView({ block: 'center' });
    }""")
    pagina.wait_for_timeout(2500)
    salvar(pagina, "avisos-whatsapp")


def app_lojas(pagina, cru: bool) -> None:
    """A janela do BeeFood Entregador: Android e iOS, com as duas lojas."""
    pagina.goto(APLICATIVOS)
    esperar(pagina, 7000)
    limpar(pagina)
    pagina.click("text=BeeFood Entregador")
    pagina.wait_for_timeout(2500)
    janela = '[role="dialog"]'
    pagina.wait_for_selector(janela)
    salvar(pagina, "app-lojas", seletor=janela)
    pagina.keyboard.press("Escape")
    pagina.wait_for_timeout(1000)


ETAPAS = {
    "painel": tela_inteira,
    "mapa": mapa,
    "lista": lista_rotas,
    "despacho": despacho,
    "entregadores": entregadores,
    "avisos": avisos,
    "app": app_lojas,
}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cru", action="store_true", help="sem a cena")
    ap.add_argument("--so", "--só", dest="so", action="append",
                    choices=sorted(ETAPAS), help="só estas etapas")
    args = ap.parse_args()

    PURAS.mkdir(parents=True, exist_ok=True)
    etapas = args.so or list(ETAPAS)

    with sessao() as pagina:
        for nome in etapas:
            ETAPAS[nome](pagina, args.cru)


if __name__ == "__main__":
    main()
