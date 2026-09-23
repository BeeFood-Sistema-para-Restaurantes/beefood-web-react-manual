#!/usr/bin/env python3
"""Capturas do carrossel do rastreio da entrega.

A tela é uma página pública do cardápio digital:

    https://menu.beefood.com.br/<cardapio>/rastreio/<token de 22 caracteres>

e ela lê um endpoint só:

    GET .../api/rest/tempresaDelivery/rastreio/{token}

Este script troca a resposta desse GET pelo `cena.json` e deixa o **cardápio de
produção** desenhar: o Leaflet com a camada da ArcGIS, o pino com a logo da
loja, a moto com o anel pulsando, o traço pontilhado da distância e a barra de
quatro etapas. Nada é escrito em servidor nenhum — a única chamada alterada é um
GET, dentro deste Chromium.

O formato da resposta saiu do bundle publicado, lido em
`manuais/gestao-entregas-rastreio-cliente/fluxo-codigo.md`. Formato adivinhado
devolve tela em branco.

    python3 capturar-telas.py                  # tudo
    python3 capturar-telas.py --so a-caminho   # uma tomada (pode repetir)
    python3 capturar-telas.py --cru            # sem a cena: o que o endereço responde hoje
    python3 capturar-telas.py --recortes       # só refaz os recortes, sem navegador

Três coisas que custaram rodada:

1. **`service_workers="block"`.** O cardápio é PWA. Sem bloquear, ele responde
   do cache e a interceptação não vê a chamada.
2. **A cor.** O layout `_rastreio` não preenche `--v-corPrimariaEmp`, então o
   CSS cai no fallback `#4caf50` e os pinos saem verdes. É o que todo cliente vê
   ao tocar no link do WhatsApp, e por isso nada é injetado aqui.
3. **A etapa atual pisca** (animação de opacidade de 1,4 s). A captura congela
   as animações antes do print, para as quatro barras saírem sempre iguais entre
   execuções.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

PASTA = Path(__file__).resolve().parent
PURAS = PASTA / "imagens-puras"
CENA = json.loads((PASTA / "cena.json").read_text(encoding="utf-8"))

# Sorteado, 22 caracteres, e não existe no servidor: `--cru` prova isso.
TOKEN = "Kq7Xb2Vn4pHs9dTmRcJw1e"
BASE = f"https://menu.beefood.com.br/{CENA['loja']['cardapio']}"
ROTA = "**/tempresaDelivery/rastreio/**"

APARELHOS = {
    "celular": {"viewport": {"width": 390, "height": 844}, "device_scale_factor": 3,
                "is_mobile": True, "has_touch": True},
    "pc": {"viewport": {"width": 1440, "height": 900}, "device_scale_factor": 2},
}

# As caixas dos recortes não são estimadas na miniatura nem chutadas em pixel:
# a captura mede no DOM (e mede o centro de cada pino do Leaflet) e grava tudo
# em `medidas.json`. Aqui ficam só as folgas, em pixel de CSS.
MEDIDAS = PASTA / "medidas.json"


def metros(a: tuple[float, float], b: tuple[float, float]) -> float:
    """Distância grande-círculo, que é a conta que o servidor faz."""
    r = 6371000.0
    p1, p2 = math.radians(a[0]), math.radians(b[0])
    h = (math.sin((p2 - p1) / 2) ** 2
         + math.cos(p1) * math.cos(p2) * math.sin(math.radians(b[1] - a[1]) / 2) ** 2)
    return 2 * r * math.asin(math.sqrt(h))


def rastreio(estado: str) -> dict:
    """Monta a resposta da rota de rastreio para um dos estados da cena.

    Os campos são os que o front lê, e só eles. O que não é enviado é o que o
    servidor também não mandaria naquele estado: sem entregador em PREPARANDO,
    sem `fila` fora de NA_FILA, sem `proximaLeituraSegundos` em ENTREGUE (é
    assim que o relógio da tela se encerra sozinho).
    """
    loja, dest, ent, ped = (CENA["loja"], CENA["destino"], CENA["entregador"],
                            CENA["pedido"])
    corpo = {
        "encontrado": True,
        "expirado": False,
        "estado": estado,
        "loja": {"nome": loja["nome"], "logo": loja["logo"],
                 "latitude": loja["latitude"], "longitude": loja["longitude"]},
        "destino": {"resumo": dest["resumo"], "latitude": dest["latitude"],
                    "longitude": dest["longitude"]},
        "pedido": {"numero": ped["numero"]},
    }
    moto = {"nome": ent["nome"], "atualizadoHaSegundos": ent["atualizadoHaSegundos"],
            "latitude": ent["latitude"], "longitude": ent["longitude"]}

    if estado == "PREPARANDO":
        corpo["pedido"]["situacao"] = "PREPARO"
        corpo["proximaLeituraSegundos"] = 20
    elif estado == "NA_FILA":
        corpo["pedido"]["situacao"] = "ENTREGA"
        corpo["entregador"] = moto
        corpo["fila"] = ped["fila"]
        corpo["proximaLeituraSegundos"] = 15
    elif estado == "A_CAMINHO":
        corpo["pedido"]["situacao"] = "ENTREGA"
        corpo["entregador"] = moto
        # Medida, não escolhida: o texto tem de concordar com o mapa.
        corpo["distanciaMetros"] = round(
            metros((ent["latitude"], ent["longitude"]),
                   (dest["latitude"], dest["longitude"])))
        corpo["proximaLeituraSegundos"] = 15
    elif estado == "ENTREGUE":
        corpo["pedido"]["situacao"] = "ENTREGUE"
        corpo["pedido"]["entregueEm"] = ped["entregueEm"]
    return corpo


TOMADAS = {
    "a-caminho": {"aparelho": "celular", "estado": "A_CAMINHO"},
    "preparo": {"aparelho": "celular", "estado": "PREPARANDO"},
    "fila": {"aparelho": "celular", "estado": "NA_FILA"},
    "entregue": {"aparelho": "celular", "estado": "ENTREGUE"},
    "pc-a-caminho": {"aparelho": "pc", "estado": "A_CAMINHO"},
}

CONGELAR = """() => {
  const e = document.createElement('style');
  e.textContent = '*,*::before,*::after{animation-play-state:paused !important;'
                + 'animation-delay:-0.7s !important;transition:none !important}';
  document.head.appendChild(e);
}"""


def responder(corpo: str):
    """Fábrica de interceptador com **um** parâmetro.

    Com dois, o Playwright entrega o `Request` no segundo e o valor padrão é
    ignorado — a resposta sai com o objeto errado dentro.
    """
    def interceptar(rota) -> None:
        rota.fulfill(status=200, content_type="application/json", body=corpo)
    return interceptar


def esperar_mapa(pagina, tentativas: int = 30) -> None:
    """Espera os quadrados do Leaflet pararem de chegar.

    Estado do mapa carregado, e não tempo fixo: o print cedo demais sai com
    faixa cinza no lugar de rua.
    """
    anterior, iguais = -1, 0
    for _ in range(tentativas):
        pagina.wait_for_timeout(1000)
        agora = pagina.evaluate(
            "() => document.querySelectorAll('.leaflet-tile-loaded').length")
        iguais = iguais + 1 if agora == anterior and agora > 0 else 0
        anterior = agora
        if iguais >= 3:
            break
    pagina.wait_for_timeout(2500)


MEDIR = """() => {
  const caixa = (sel) => {
    const e = document.querySelector(sel);
    if (!e) return null;
    const c = e.getBoundingClientRect();
    return {x: c.x, y: c.y, w: c.width, h: c.height};
  };
  const pinos = {};
  for (const e of document.querySelectorAll('.leaflet-marker-icon')) {
    const dentro = e.querySelector('.pino-loja, .pino-entregador, .pino-destino');
    const nome = ['pino-loja', 'pino-entregador', 'pino-destino']
        .find(c => dentro && dentro.classList.contains(c)) || 'pino-destino';
    const c = e.getBoundingClientRect();
    pinos[nome] = {x: c.x + c.width / 2, y: c.y + c.height / 2};
  }
  return {
    cabecalho: caixa('.rastreio-cabecalho'),
    titulo: caixa('.rastreio-titulo'),
    barra: caixa('.progresso-pedido'),
    cartao: caixa('.rastreio-entregador'),
    mapa: caixa('.rastreio-mapa'),
    pinos,
  };
}"""


def capturar(nomes: list[str], cru: bool) -> None:
    from playwright.sync_api import sync_playwright

    PURAS.mkdir(parents=True, exist_ok=True)
    medidas = json.loads(MEDIDAS.read_text(encoding="utf-8")) if MEDIDAS.is_file() else {}
    with sync_playwright() as p:
        navegador = p.chromium.launch()
        for nome in nomes:
            receita = TOMADAS[nome]
            corpo = json.dumps(rastreio(receita["estado"]), ensure_ascii=False)
            ctx = navegador.new_context(
                locale="pt-BR", timezone_id="America/Sao_Paulo",
                # PWA: sem isso o service worker responde do cache.
                service_workers="block",
                **APARELHOS[receita["aparelho"]],
            )
            if not cru:
                ctx.route(ROTA, responder(corpo))
            pagina = ctx.new_page()
            # `networkidle` não serve: a tela consulta o servidor a cada 15 s,
            # então a rede nunca fica parada. Espera-se o mapa, não a rede.
            pagina.goto(f"{BASE}/rastreio/{TOKEN}", wait_until="domcontentloaded",
                        timeout=120_000)
            esperar_mapa(pagina)
            pagina.evaluate(CONGELAR)
            pagina.wait_for_timeout(400)
            base = nome if receita["aparelho"] == "pc" else f"cel-{nome}"
            alvo = PURAS / f"{'cru-' if cru else ''}{base}.png"
            pagina.screenshot(path=str(alvo), type="png")
            if not cru:
                medidas[base] = {
                    "escala": APARELHOS[receita["aparelho"]]["device_scale_factor"],
                    **pagina.evaluate(MEDIR),
                }
            print(f"OK  {alvo.name}  ({receita['estado']})")
            ctx.close()
        navegador.close()
    if not cru:
        MEDIDAS.write_text(json.dumps(medidas, indent=1, ensure_ascii=False) + "\n",
                           encoding="utf-8")


def recortar() -> None:
    """Corta os recortes a partir das caixas medidas no DOM.

    A regra da skill é *coordenada medida, nunca estimada na miniatura*. Aqui a
    medida vem do próprio navegador da captura, então o corte se refaz igual
    mesmo quando a tela muda de altura entre estados — e ela muda: sem a linha
    de detalhe, *Pedido entregue às 20:12* sobe a barra de etapas.
    """
    from PIL import Image

    if not MEDIDAS.is_file():
        print("--  falta medidas.json: rode a captura antes")
        return
    medidas = json.loads(MEDIDAS.read_text(encoding="utf-8"))

    def corte(origem: str, caixa: tuple[float, float, float, float]) -> None:
        arquivo = PURAS / f"{origem[0]}.png"
        if not arquivo.is_file():
            print(f"--  {origem[1]}: falta {arquivo.name}")
            return
        e = medidas[origem[0]]["escala"]
        c = tuple(round(v * e) for v in caixa)
        Image.open(arquivo).crop(c).save(PURAS / f"{origem[1]}.png")
        print(f"OK  {origem[1]}.png  ({c[2] - c[0]}x{c[3] - c[1]})")

    # A frase e a barra de etapas, em cada estado: é o que muda de um para o
    # outro, e o cabeçalho da loja repetido três vezes seria ruído.
    for estado in ("preparo", "fila", "entregue", "a-caminho"):
        m = medidas.get(f"cel-{estado}")
        if not m:
            continue
        corte((f"cel-{estado}", f"recorte-{estado}"),
              (0, m["titulo"]["y"] - 14, m["cabecalho"]["w"],
               m["barra"]["y"] + m["barra"]["h"] + 16))

    # O cabeçalho inteiro: logo e nome da loja, número do pedido, a frase, a
    # distância e a barra. É o recorte de leitura do slide 3.
    if (m := medidas.get("cel-a-caminho")):
        corte(("cel-a-caminho", "recorte-cabecalho"),
              (0, 0, m["cabecalho"]["w"], m["cabecalho"]["h"]))
        corte(("cel-a-caminho", "recorte-cartao"),
              (m["cartao"]["x"] - 10, m["cartao"]["y"] - 10,
               m["cartao"]["x"] + m["cartao"]["w"] + 10,
               m["cartao"]["y"] + m["cartao"]["h"] + 10))
        # O mapa fechado no pino da loja e na moto, com folga para a rua em
        # volta: é a prova de que o pino é a logo do restaurante.
        loja, moto = m["pinos"]["pino-loja"], m["pinos"]["pino-entregador"]
        corte(("cel-a-caminho", "recorte-mapa"),
              (max(m["mapa"]["x"], min(loja["x"], moto["x"]) - 100),
               min(loja["y"], moto["y"]) - 60,
               min(m["mapa"]["x"] + m["mapa"]["w"], max(loja["x"], moto["x"]) + 150),
               max(loja["y"], moto["y"]) + 70))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--so", action="append", choices=sorted(TOMADAS),
                    help="só esta tomada (pode repetir)")
    ap.add_argument("--cru", action="store_true",
                    help="sem a cena: o que o endereço responde hoje")
    ap.add_argument("--recortes", action="store_true",
                    help="só refaz os recortes, sem abrir navegador")
    args = ap.parse_args()

    if args.recortes:
        recortar()
        return 0
    capturar(args.so or list(TOMADAS), args.cru)
    if not args.cru:
        recortar()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
