#!/usr/bin/env python3
"""Capturas do carrossel do Painel para Entregadores.

O painel não tem endpoint próprio: ele lê a mesma listagem da tela de Delivery,

    GET /api/venda2/delivery/{empresa}/{filial}/{usuario}/6

com a janela fixa em 6 horas. Este script intercepta essa resposta e aplica o
`cena.json` — promove um pedido de Cardápio Digital para PREPARO e reescreve os
relógios de etapa. Nada é escrito no servidor; o `--cru` mostra a tela como ela
está agora, para conferir o que foi mexido.

    python capturar-telas.py
    python capturar-telas.py --cru        # sem a cena, para comparar
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.append(".cursor/skills/carrossel/scripts")
from capturar import esperar, limpar, sessao  # noqa: E402

FUSO = ZoneInfo("America/Sao_Paulo")

PASTA = Path(__file__).resolve().parent
PURAS = PASTA / "imagens-puras"
CENA = json.loads((PASTA / "cena.json").read_text(encoding="utf-8"))["minutos"]

PAINEL = "https://beefood.app/painel-entregador"
APLICATIVOS = "https://beefood.app/aplicativos"
LISTAGEM = "**/venda2/delivery/**"


def carimbo(minutos: int) -> str:
    """O carimbo é a hora de SÃO PAULO vestida de UTC, e não a hora UTC.

    O servidor devolve `...Z`, mas o front lê com `parseLocalDateTime`, que
    **ignora o sufixo** e trata a string como hora local. Medido no navegador da
    captura (que roda em `America/Sao_Paulo`): `2026-09-19T22:40:00.000Z` volta
    como 7 min atrás quando lido como UTC e como 173 min **no futuro** quando
    lido como local. Gravar `now(utc)` fazia todo cartão marcar "há 0min".
    """
    agora = datetime.now(FUSO).replace(tzinfo=None)
    return (agora - timedelta(minutes=minutos)).strftime("%Y-%m-%dT%H:%M:%S.000Z")


def montar(lista: list[dict]) -> list[dict]:
    # Fora da cena e já em PREPARO ou PRONTO, o pedido entraria no painel com a
    # hora real de criação — e apareceria vermelho, atrasado há horas, ao lado
    # dos que a cena controla. Some da listagem; a tela de Delivery não é
    # assunto desta captura.
    lista = [p for p in lista
             if str(p.get("numeroPedido")) in CENA
             or p.get("situacaoDelivery") not in ("PREPARO", "PRONTO")]

    for p in lista:
        regra = CENA.get(str(p.get("numeroPedido")))
        if not regra:
            continue
        p["situacaoDelivery"] = regra["etapa"]
        p["situacao"] = "ABERTO"
        quando = carimbo(regra["minutos"])
        if regra["etapa"] == "PREPARO":
            p["dataHoraEmPreparo"], p["dataHoraPronto"] = quando, None
            entrou = regra["minutos"] + 6
        else:
            # Pronto há N minutos, e em preparo um pouco antes disso: o cartão
            # lê `dataHoraPronto`, mas um pedido pronto sem hora de preparo é
            # um estado que não existe.
            p["dataHoraEmPreparo"] = carimbo(regra["minutos"] + 8)
            p["dataHoraPronto"] = quando
            entrou = regra["minutos"] + 14
        # O alerta de atraso é outra conta, e conta do PEDIDO: sem mexer aqui, os
        # sete cartões continuavam vermelhos por causa da hora de criação real.
        p["dataHoraPedido"] = p["dataVenda"] = carimbo(entrou)
    return lista


def rotear(pagina, aplicar: bool) -> None:
    if not aplicar:
        return

    def responder(rota):
        resposta = rota.fetch()
        try:
            corpo = resposta.json()
        except Exception:
            rota.fulfill(response=resposta)
            return
        if isinstance(corpo, list):
            corpo = montar(corpo)
        rota.fulfill(response=resposta, json=corpo)

    pagina.route(LISTAGEM, responder)


def cartao_de(pagina, numero: str, folga: int = 6) -> dict:
    """A caixa do cartão que mostra `numero`, para recortar só ele."""
    c = pagina.locator(f"text={numero}").first.locator(
        "xpath=ancestor::*[contains(@class,'rounded')][1]").bounding_box()
    return {"x": c["x"] - folga, "y": c["y"] - folga,
            "width": c["width"] + folga * 2, "height": c["height"] + folga * 2}


def faixa(pagina, nome: str) -> None:
    """Cabeçalho do painel mais a primeira linha de cartões."""
    try:
        primeiro = pagina.locator("text=Em preparo há").first.locator(
            "xpath=ancestor::*[contains(@class,'rounded')][1]").bounding_box()
        pagina.screenshot(path=PURAS / nome, type="png",
                          clip={"x": 0, "y": 0,
                                "width": pagina.viewport_size["width"],
                                "height": primeiro["y"] + primeiro["height"] + 18})
    except Exception as erro:
        print(nome, erro)


def caixa_de(pagina, seletor: str, folga: int = 0) -> dict:
    c = pagina.locator(seletor).first.bounding_box()
    return {"x": c["x"] - folga, "y": c["y"] - folga,
            "width": c["width"] + folga * 2, "height": c["height"] + folga * 2}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--cru", action="store_true",
                   help="sem a cena: a tela como a sandbox está agora")
    args = p.parse_args()

    PURAS.mkdir(exist_ok=True)
    sufixo = "-cru" if args.cru else ""

    with sessao(dispositivo="painel") as pagina:
        # Abaixo de 1500 px cada etapa fica em UMA coluna interna. É o que a
        # peça quer: em duas colunas o cartão estreita e "2740 - Coleta 6118"
        # sai cortado no meio, que num slide lê como bug. A tela larga da TV
        # cabe mais pedido, mas isso é vantagem de operação, não de imagem.
        #
        # 1280x720 e não 1200x700 porque a tela inteira entra numa moldura de
        # TV, que é 16/9: fora da proporção, o `object-fit: cover` do mockup
        # come uma faixa do painel.
        pagina.set_viewport_size({"width": 1280, "height": 720})
        rotear(pagina, aplicar=not args.cru)

        pagina.goto(PAINEL)
        esperar(pagina)
        limpar(pagina)
        pagina.screenshot(path=PURAS / f"painel-claro{sufixo}.png", type="png")

        # Só as duas colunas, sem cabeçalho: é o recorte que cabe legível no
        # slide, e o cabeçalho (busca, sol/lua) é assunto de outro slide.
        colunas = pagina.locator("main > div, div:has(> div:text-matches('EM PREPARO'))")
        try:
            topo = caixa_de(pagina, "text=EM PREPARO")["y"] - 22
            # A altura sai do último cartão, e não de um número fixo: mudar a
            # cena muda quantos cartões existem, e um clip fixo corta o de baixo
            # pela metade — que num slide lê como imagem mal recortada.
            def pe_do_ultimo(rotulo: str) -> float:
                c = pagina.locator(f"text={rotulo}").last.locator(
                    "xpath=ancestor::*[contains(@class,'rounded')][1]").bounding_box()
                return c["y"] + c["height"]

            fundo = max(pe_do_ultimo(r) for r in ("Em preparo há", "Pronto há"))
            largura = pagina.viewport_size["width"]
            pagina.screenshot(path=PURAS / f"colunas{sufixo}.png", type="png",
                              clip={"x": 14, "y": topo,
                                    "width": largura - 28, "height": fundo - topo + 44})
        except Exception as erro:
            print("colunas:", erro)

        if not args.cru:
            # Três cartões seguidos, de três origens: é o que prova "cada pedido
            # diz de onde veio". Um cartão só provaria um canal.
            try:
                primeiro = pagina.locator("text=#1137").first.locator(
                    "xpath=ancestor::*[contains(@class,'rounded')][1]").bounding_box()
                ultimo = pagina.locator("text=#1133").first.locator(
                    "xpath=ancestor::*[contains(@class,'rounded')][1]").bounding_box()
                pagina.screenshot(path=PURAS / "cartoes-origens.png", type="png",
                                  clip={"x": primeiro["x"] - 6, "y": primeiro["y"] - 6,
                                        "width": primeiro["width"] + 12,
                                        "height": ultimo["y"] + ultimo["height"]
                                                  - primeiro["y"] + 12})
            except Exception as erro:
                print("cartoes-origens:", erro)

            # O cartão atrasado, sozinho e grande: é o que o slide do alerta
            # precisa provar, e dentro do painel inteiro ele sai pequeno.
            try:
                atrasado = pagina.locator("text=Atrasado").first
                alvo = atrasado.locator(
                    "xpath=ancestor::*[contains(@class,'rounded')][1]")
                c = alvo.bounding_box()
                pagina.screenshot(path=PURAS / "cartao-atrasado.png", type="png",
                                  clip={"x": c["x"] - 6, "y": c["y"] - 6,
                                        "width": c["width"] + 12,
                                        "height": c["height"] + 12})
            except Exception as erro:
                print("cartao-atrasado:", erro)

            # A coluna Em preparo inteira, de pé. O slide do alerta diz duas
            # coisas — o cartão ganha borda E sobe para o topo — e o cartão
            # recortado sozinho só prova a primeira. De quebra, imagem vertical
            # preenche a faixa do slide, que com o cartão deitado ficava com
            # meia página vazia.
            try:
                c = caixa_de(pagina, "text=EM PREPARO")
                pe = pagina.locator("text=Em preparo há").last.locator(
                    "xpath=ancestor::*[contains(@class,'rounded')][1]").bounding_box()
                # A largura sai do CARTÃO, e não do título da coluna: alinhado
                # pelo título, o clip sobrava para a direita e entrava uma
                # listra verde da coluna Pronto no recorte.
                pagina.screenshot(path=PURAS / "coluna-preparo.png", type="png",
                                  clip={"x": pe["x"] - 16, "y": c["y"] - 26,
                                        "width": pe["width"] + 32,
                                        "height": pe["y"] + pe["height"] - c["y"] + 42})
            except Exception as erro:
                print("coluna-preparo:", erro)

            # O MESMO pedido nas duas colunas, em duas passadas: é assim que a
            # peça prova que o cartão anda sozinho. Dois pedidos diferentes lado
            # a lado provariam só que existem duas colunas, que é outro slide.
            try:
                c = cartao_de(pagina, "#1133")
                pagina.screenshot(path=PURAS / "andou-antes.png", type="png", clip=c)
                CENA["1133"] = {"etapa": "PRONTO", "minutos": 1}
                pagina.reload()
                esperar(pagina)
                limpar(pagina)
                pagina.screenshot(path=PURAS / "andou-depois.png", type="png",
                                  clip=cartao_de(pagina, "#1133"))
                CENA["1133"] = {"etapa": "PREPARO", "minutos": 4}
                # Recarregar não é zelo: sem isto o painel segue com o #1133 no
                # lado direito, e as capturas seguintes saem marcando "3 pedidos
                # / 4 pedidos" enquanto as anteriores marcam "4 / 3". Dois
                # slides da mesma peça discordando sobre a mesma tela.
                pagina.reload()
                esperar(pagina)
                limpar(pagina)
            except Exception as erro:
                print("andou:", erro)

            # Tema escuro: o botão de sol/lua troca só o painel.
            #
            # Além da tela inteira, uma FAIXA de cada tema: o slide que compara
            # os dois põe as telas inteiras com menos de 400 px de largura cada,
            # e aí nenhum número lê. A faixa é o cabeçalho (onde está o próprio
            # botão de sol e lua) mais a primeira linha de cartões.
            faixa(pagina, "tema-claro.png")
            try:
                pagina.locator("header button, button:near(:text('Buscar'))").first.click()
                pagina.wait_for_timeout(900)
                pagina.screenshot(path=PURAS / "painel-escuro.png", type="png")
                faixa(pagina, "tema-escuro.png")
            except Exception as erro:
                print("painel-escuro:", erro)

        # O caminho do release: Aplicativos → Entrega → Painel para Entregadores.
        # Largo de proposito: em 1440 o card trunca em "Painel para
        # Entregador..." e a descricao vira reticencias, e card cortado
        # dentro de um slide le como print mal feito.
        pagina.set_viewport_size({"width": 1920, "height": 1000})
        pagina.goto(APLICATIVOS)
        esperar(pagina)
        limpar(pagina)
        try:
            # A seção inteira, e não só o card: o que o slide precisa mostrar é
            # que o painel mora em **Entrega**, ao lado da Gestão de Entregas —
            # a mesma família, e a mesma permissão.
            titulo = pagina.locator("p:text-is('Entrega'), h2:text-is('Entrega'), "
                                    "h3:text-is('Entrega')").first
            titulo.scroll_into_view_if_needed()
            pagina.wait_for_timeout(600)
            # Só o card, e não a seção: a grade de Entrega tem uma dúzia de
            # cards de parceiro de entrega, e o recorte largo virava vitrine de
            # concorrente dentro do slide.
            alvo = pagina.locator("text=Painel para Entregador").first.locator(
                "xpath=ancestor::*[self::button or self::a or "
                "contains(@class,'cursor-pointer')][1]")
            c = alvo.bounding_box()
            pagina.screenshot(path=PURAS / f"card-aplicativos{sufixo}.png", type="png",
                              clip={"x": c["x"] - 10, "y": c["y"] - 10,
                                    "width": c["width"] + 20, "height": c["height"] + 20})
        except Exception as erro:
            print("aplicativos-entrega:", erro)

        # O cartão desta novidade no celular, para o CTA — a convenção das peças
        # anteriores. A data sai antes do print: ela está num `<time>`, e data
        # na arte faz o post parecer velho quando sai da fila de conteúdo.
        contexto = pagina.context.browser.new_context(**{
            "viewport": {"width": 390, "height": 844}, "device_scale_factor": 3,
            "is_mobile": True, "has_touch": True, "locale": "pt-BR"})
        celular = contexto.new_page()
        celular.goto("https://beefood.app/novidades/painel-para-entregadores",
                     wait_until="domcontentloaded", timeout=90000)
        celular.wait_for_timeout(8000)
        celular.add_style_tag(content="time{display:none !important}")
        celular.wait_for_timeout(1200)
        celular.screenshot(path=PURAS / "novidades-celular.png", type="png")
        contexto.close()

    for f in sorted(PURAS.glob("*.png")):
        print("OK", f.relative_to(PASTA))


if __name__ == "__main__":
    main()
