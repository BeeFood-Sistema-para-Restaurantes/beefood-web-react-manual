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
DESEMPENHO = "https://beefood.app/desempenho"
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

    # O mapa do Leaflet passa POR CIMA das janelas do painel. `.leaflet-container`
    # é `position: relative` sem `z-index`, então não abre contexto de
    # empilhamento e os painéis de dentro dele (`z-index: 400`) disputam o
    # desenho com a janela do Radix, que é `z-index: 50` — os quadrados do mapa e
    # os pinos ganham. Só aparece com o mapa carregado: no print do manual, em
    # que os quadrados não chegaram, a janela sai inteira. Um `z-index: 0` no
    # contêiner fecha o contexto e devolve a ordem certa, sem tocar no conteúdo.
    pagina.add_style_tag(content=".leaflet-container { z-index: 0 }")
    pagina.wait_for_timeout(500)


def salvar(pagina, nome: str, seletor: str | None = None, **kwargs) -> None:
    destino = PURAS / f"{nome}.png"
    alvo = pagina.locator(seletor) if seletor else pagina
    alvo.screenshot(path=str(destino), type="png", **kwargs)
    print("·", destino.relative_to(PASTA.parent.parent))


def tela_inteira(pagina, cru: bool) -> None:
    """A tela completa: mapa com as duas rotas à esquerda, lista à direita."""
    abrir_painel(pagina, cru)
    nome = "painel-cru" if cru else "painel-inteiro"
    salvar(pagina, nome)
    recortar(nome)


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


# A janela aberta é fotografada inteira e recortada depois, com a caixa medida
# no arquivo. Medir no DOM não serviu aqui: `[role="dialog"]` casa com mais de um
# elemento na página (a janela da tela inteira fica montada mesmo fechada) e o
# `getBoundingClientRect` do que casa primeiro devolve uma caixa que não é a da
# janela que apareceu — o recorte saía sobre o mapa. Estas caixas estão em pixel
# de arquivo (viewport 1440×900 com DPR 2, logo 2880×1800).
CORTES = {
    # A tela inteira menos o cromo: fora a barra de cima (que leva o nome da
    # loja de teste) e a coluna de ícones da esquerda. O que sobra é 16/10, que
    # é a proporção da tela do `.navegador` em sangria.
    "painel-inteiro": (101, 87, 2880, 1800),
    "despacho-regras": (674, 298, 2208, 2038),
    # A janela inteira, com o grupo `Offline` no pé. Cortar ali deixava o título
    # `Entregadores (5)` em cima de quatro linhas, e contador que não fecha com a
    # lista é o tipo de detalhe que o leitor pega.
    "lista-entregadores": (928, 386, 1950, 1416),
    "app-lojas": (930, 441, 1950, 1359),
    # Os dois relatórios param de afirmar em pontos diferentes, e o corte é onde
    # eles param — ver `roteiro.md`, seção *o recorte do relatório de acerto*.
    # O pé fecha logo abaixo de "A rua responde por 13% do tempo até a entrega":
    # a linha seguinte é "medido em 56 de 210 pedidos (27%)", que é ressalva de
    # amostra e lê como dado fraco ao lado da barra que ela mesma sustenta.
    "relatorio-operacao": (1004, 765, 2816, 1345),
    "relatorio-entregador": (965, 273, 2816, 759),
}


MEDIR = False


def tirar_foco(pagina) -> None:
    """Tira o anel de foco da janela recém-aberta.

    Abrir uma janela com clique deixa o foco no primeiro botão dela, e o
    `focus-visible` do sistema é um anel vermelho — no print ele lê como campo
    destacado, ou como erro de validação.
    """
    pagina.evaluate("() => document.activeElement && document.activeElement.blur()")
    pagina.wait_for_timeout(600)


def recortar(nome: str) -> None:
    """Aplica em `imagens-puras/<nome>.png` o corte medido em `CORTES`.

    Com `--medir` o corte é pulado: é a passada que produz a tela inteira, de
    onde as caixas de `CORTES` são medidas.
    """
    from PIL import Image

    caixa = CORTES.get(nome)
    if not caixa or MEDIR:
        return
    destino = PURAS / f"{nome}.png"
    with Image.open(destino) as imagem:
        imagem.crop(caixa).save(destino)


def despacho(pagina, cru: bool) -> None:
    """A janela do despacho automático, com as regras do agrupamento."""
    # A janela tem 700 px de altura e o teto dela é `90vh`: nos 900 px do
    # dispositivo `painel` ela abre rolada, sem o título em cima e sem a
    # tolerância de GPS embaixo — recorte nenhum devolve o que não foi desenhado.
    pagina.set_viewport_size({"width": 1440, "height": 1160})
    abrir_painel(pagina, cru)
    pagina.click('button:has-text("Despacho automático")')
    pagina.wait_for_timeout(3000)
    tirar_foco(pagina)
    salvar(pagina, "despacho-regras")
    recortar("despacho-regras")
    pagina.keyboard.press("Escape")
    pagina.wait_for_timeout(1200)
    pagina.set_viewport_size({"width": 1440, "height": 900})


def entregadores(pagina, cru: bool) -> None:
    """A lista completa de entregadores: posição, distância e bateria."""
    abrir_painel(pagina, cru)
    pagina.click('button[title="Ver lista completa de entregadores"]')
    pagina.wait_for_timeout(3000)
    tirar_foco(pagina)
    salvar(pagina, "lista-entregadores")
    recortar("lista-entregadores")
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
    tirar_foco(pagina)
    salvar(pagina, "app-lojas")
    recortar("app-lojas")
    pagina.keyboard.press("Escape")
    pagina.wait_for_timeout(1000)


def abrir_relatorio(pagina, item: str) -> None:
    """Desempenho → Delivery → `item`, dentro do iframe dos relatórios.

    O relatório vive num iframe de `relatorios.beefood.com.br`, que é outro
    domínio: `contentDocument` é `null` e não há como medir nem rolar por dentro.
    O clique passa pelo `frame_locator` e a rolagem pela roda do mouse, que é
    evento de navegador e atravessa a fronteira.
    """
    pagina.goto(DESEMPENHO)
    esperar(pagina, 9000)
    limpar(pagina)
    quadro = pagina.frame_locator("iframe")
    quadro.locator('button:has-text("Delivery")').first.click()
    pagina.wait_for_timeout(1500)
    quadro.locator(f'button:has-text("{item}")').first.click()
    pagina.wait_for_timeout(10000)


def rolar_relatorio(pagina, quanto: int) -> None:
    pagina.mouse.move(1000, 600)
    pagina.mouse.wheel(0, quanto)
    pagina.wait_for_timeout(1500)
    # A roda deixa o cursor sobre o gráfico, e o gráfico abre a caixinha de
    # valor debaixo do ponteiro — que no print lê como clique de alguém.
    pagina.mouse.move(180, 820)
    pagina.wait_for_timeout(1200)


def relatorio_operacao(pagina, cru: bool) -> None:
    """Operação de Entrega: as etapas de tempo e a divisão loja × rua."""
    abrir_relatorio(pagina, "Operação de Entrega")
    rolar_relatorio(pagina, 500)
    salvar(pagina, "relatorio-operacao")
    recortar("relatorio-operacao")


def relatorio_entregador(pagina, cru: bool) -> None:
    """Entregador (Taxa / KM): os quatro modos de pagar e o total do período."""
    abrir_relatorio(pagina, "Entregador (Taxa / KM)")
    salvar(pagina, "relatorio-entregador")
    recortar("relatorio-entregador")


ETAPAS = {
    "painel": tela_inteira,
    "mapa": mapa,
    "lista": lista_rotas,
    "despacho": despacho,
    "entregadores": entregadores,
    "avisos": avisos,
    "app": app_lojas,
    "operacao": relatorio_operacao,
    "acerto": relatorio_entregador,
}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cru", action="store_true", help="sem a cena")
    ap.add_argument("--medir", action="store_true",
                    help="não recorta: entrega a tela inteira, para medir o corte")
    ap.add_argument("--so", "--só", dest="so", action="append",
                    choices=sorted(ETAPAS), help="só estas etapas")
    args = ap.parse_args()

    global MEDIR
    MEDIR = args.medir

    PURAS.mkdir(parents=True, exist_ok=True)
    etapas = args.so or list(ETAPAS)

    with sessao() as pagina:
        for nome in etapas:
            ETAPAS[nome](pagina, args.cru)


if __name__ == "__main__":
    main()
