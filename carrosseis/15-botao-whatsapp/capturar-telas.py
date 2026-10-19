#!/usr/bin/env python3
"""Capturas do carrossel do botão de WhatsApp no cardápio digital.

A tela é o **cardápio digital público**, e o botão vem de uma chave só da
resposta da loja:

    POST .../api/rest/tempresaDelivery/validaDelivery/1   →  whatsappJson

Este script busca a resposta de verdade, troca **só** essa chave pelo documento
da tomada e devolve. Quem desenha o botão é o cardápio publicado — a pílula que
recolhe na rolagem, as folgas do rodapé, o selo dentro da sacola, a cor do tema.
Nenhuma loja é alterada: a troca acontece dentro deste Chromium.

O formato do documento saiu do bundle publicado, em
`manuais/cardapio-digital-botao-whatsapp/fluxo-codigo.md`. Campo adivinhado não
devolve tela errada, devolve tela **sem botão**: `v > 1` e `on !== true` fazem o
cardápio devolver `null` e não desenhar nada.

    python3 capturar-telas.py                    # tudo
    python3 capturar-telas.py --so cel-flutuante # uma tomada (pode repetir)
    python3 capturar-telas.py --cru              # sem a cena: o que a loja responde hoje
    python3 capturar-telas.py --recortes         # só refaz os recortes, sem navegador

Quatro coisas que custaram rodada:

1. **A resposta é comprimida.** O corpo é uma *string* JSON com zlib em base64
   (`eJ…`), não um objeto. Lido como objeto, o script morre em `'str' object
   does not support item assignment`.
2. **`service_workers="block"`.** O cardápio é PWA, e sem isso o service worker
   responde do cache e a interceptação não vê a chamada (lição da #11).
3. **O botão é conferido antes do print.** `a.be-wa__alvo` tem de existir; sem
   ele o script avisa em vez de gravar uma tela sem o assunto.
4. **A sacola é estado local.** Pôr um item nela não chama servidor nenhum — o
   cardápio só grava no fechamento do pedido, que este script nunca faz.
"""
from __future__ import annotations

import argparse
import base64
import json
import zlib
from pathlib import Path

PASTA = Path(__file__).resolve().parent
PURAS = PASTA / "imagens-puras"
MEDIDAS = PASTA / "medidas.json"
CENA = json.loads((PASTA / "cena.json").read_text(encoding="utf-8"))

BASE = f"https://menu.beefood.com.br/{CENA['loja']['cardapio']}"
ROTA = "**/tempresaDelivery/validaDelivery/**"

APARELHOS = {
    "celular": {"viewport": {"width": 390, "height": 844}, "device_scale_factor": 3,
                "is_mobile": True, "has_touch": True},
    # 1152x720 é 16/10, a proporção da tela do `.notebook` e da do `.navegador`.
    "pc": {"viewport": {"width": 1152, "height": 720}, "device_scale_factor": 2},
}

# Cada tomada é a configuração da cena com os ajustes dela. `fechada` manda
# também o estado da loja, que é a única condição em que aquele botão aparece.
#
# `altura` encurta o viewport do celular. A capa precisa disso: o flutuante mora
# no pé da tela, e numa captura de 844 px o mockup em sangria corta justamente
# os últimos 23% — ou seja, o assunto. Com 660 px de tela o botão sobe para 80%
# da altura e fica dentro do slide, com a capa, o logotipo e o nome da loja
# ainda na imagem.
#
# `item` é o produto que entra na sacola, e ele é escolhido a dedo: **um produto
# sem grupo obrigatório**. A primeira rodada clicou no COMBO CASAL, que pede dois
# hambúrgueres e duas porções, e a tela respondeu *"Verifique a quantidade do
# grupo ESCOLHA OS BURGERS"* em faixa vermelha — a captura saiu com uma mensagem
# de erro no lugar do assunto. O pudim fecha em um clique.
ITEM = "PUDIM - BRIGADEIRO"
# No computador o clique no cartão abre o produto como **janela sobre a home**, e
# a janela cobre o canto em que o botão mora. Entrando direto pelo endereço, a
# mesma página se serve inteira — e é esse endereço que `{link}` carrega.
URL_ITEM = f"{BASE}/pudim---brigadeiro/"

TOMADAS = {
    "cel-flutuante": {"aparelho": "celular", "cfg": {}, "altura": 660},
    "pc-home": {"aparelho": "pc", "cfg": {}},
    "cel-produto": {"aparelho": "celular", "cfg": {}, "url": URL_ITEM},
    "cel-topo": {"aparelho": "celular", "cfg": {"pos": "topo", "lay": "cardLogo"}},
    "cel-carrinho": {"aparelho": "celular", "cfg": {"pos": "carrinho", "lay": "card"},
                     "item": ITEM, "abrir_sacola": True},
    "cel-sacola-cheia": {"aparelho": "celular", "cfg": {}, "item": ITEM},
    "cel-fechada": {"aparelho": "celular", "cfg": {"quando": "fechada"}, "fechada": True},
    "cel-tema": {"aparelho": "celular", "cfg": {"cor": "tema"}},
}

CONGELAR = """() => {
  const e = document.createElement('style');
  e.textContent = '*,*::before,*::after{animation:none !important;'
                + 'transition:none !important}';
  document.head.appendChild(e);
}"""

MEDIR = """() => {
  const caixa = (sel) => {
    const e = document.querySelector(sel);
    if (!e) return null;
    const c = e.getBoundingClientRect();
    return {x: c.x, y: c.y, w: c.width, h: c.height};
  };
  // A caixa do MENOR elemento cujo texto é exatamente este. Serve para medir
  // pedaço de tela que não tem classe própria — o aviso de loja fechada, por
  // exemplo — sem estimar pixel na miniatura.
  const caixaTexto = (txt) => {
    const achados = Array.from(document.querySelectorAll('div,span,p,h1,h2,h3,strong'))
      .filter(e => (e.innerText || '').trim() === txt);
    const e = achados[achados.length - 1];
    if (!e) return null;
    const c = e.getBoundingClientRect();
    return {x: c.x, y: c.y, w: c.width, h: c.height};
  };
  const alvo = document.querySelector('a.be-wa__alvo');
  return {
    botao: caixa('a.be-wa__alvo'),
    fechado: caixaTexto('Indisponível para pedidos'),
    nomeLoja: caixaTexto('ONE STAND HAMBURGUERIA'),
    sacola: caixaTexto('Ver sacola'),
    classe: alvo ? alvo.className : null,
    rotulo: alvo ? alvo.innerText.trim() : null,
    href: alvo ? alvo.getAttribute('href') : null,
    endereco: location.href,
    pagina: {w: document.documentElement.clientWidth,
             h: document.documentElement.clientHeight},
  };
}"""


def documento(ajustes: dict) -> str:
    cfg = {**CENA["configuracao"], **ajustes}
    return json.dumps(cfg, ensure_ascii=False)


def trocar(whatsapp: str, fechada: bool):
    """Fábrica de interceptador: troca uma chave e devolve o resto intacto.

    A resposta vem como *string* JSON contendo base64 de zlib. O caminho é
    descomprimir, mexer na chave e comprimir de volta, mantendo tudo o mais —
    cor, horários, formas de pagamento, cardápio — como o servidor mandou.
    """
    def interceptar(rota) -> None:
        resposta = rota.fetch()
        bruto = resposta.text()
        miolo = json.loads(bruto)
        comprimido = isinstance(miolo, str)
        if comprimido:
            miolo = json.loads(zlib.decompress(base64.b64decode(miolo)).decode("utf-8"))
        alvo = miolo[0] if isinstance(miolo, list) else miolo
        alvo["whatsappJson"] = whatsapp
        if fechada:
            # O estado em que esta loja entra todo dia à meia-noite, e a única
            # condição em que o botão de `quando: fechada` aparece.
            for chave in ("aberto", "abertoDelivery", "abertoPresencial"):
                alvo[chave] = False
        saida = json.dumps(miolo, ensure_ascii=False)
        if comprimido:
            saida = json.dumps(base64.b64encode(
                zlib.compress(saida.encode("utf-8"))).decode("ascii"))
        rota.fulfill(response=resposta, body=saida)

    return interceptar


def esperar(pagina, segundos: int = 16) -> None:
    """Espera a tela e **a fonte**: os ícones do cardápio são glifos de webfont."""
    pagina.wait_for_timeout(segundos * 1000)
    try:
        pagina.wait_for_function("() => document.fonts && document.fonts.status === 'loaded'",
                                 timeout=15_000)
    except Exception:
        pass
    pagina.wait_for_timeout(1500)


def fechar_avisos(pagina) -> None:
    """Fecha a faixa de cupom, que é o que qualquer visitante faz.

    Ela tem um X próprio (`.promo-banner button`) e ocupa a primeira faixa da
    tela — numa peça sobre outro recurso, é o ruído que a #4 trouxe junto com o
    print do manual.
    """
    for seletor in (".promo-banner button", 'button[aria-label="Fechar"]',
                    'button:has-text("AGORA NÃO")'):
        alvo = pagina.locator(seletor)
        if alvo.count():
            try:
                alvo.first.click(timeout=2500)
                pagina.wait_for_timeout(900)
            except Exception:
                pass


def abrir_item(pagina, nome: str) -> bool:
    """Abre a página de um produto.

    O cardápio não tem `<a href>` nos cartões — a navegação é por clique, e a
    rota vira `/<cardapio>/<slug-do-produto>/`. É desse endereço que `{link}`
    se serve, então ele tem de ser o de uma página de produto de verdade.
    """
    alvo = pagina.get_by_text(nome, exact=True)
    if not alvo.count():
        return False
    alvo.first.click()
    pagina.wait_for_timeout(4500)
    return "/" in pagina.url.rstrip("/").rsplit("/", 1)[-1] or pagina.url != BASE


def pedir_item(pagina, nome: str) -> bool:
    """Põe um item na sacola. Estado local: não chama servidor nenhum.

    O cardápio só grava no fechamento do pedido, e este script nunca fecha.
    """
    if not abrir_item(pagina, nome):
        return False
    botao = pagina.locator("button:has-text('Adicionar')")
    if not botao.count():
        return False
    botao.last.click(timeout=5000)
    pagina.wait_for_timeout(4000)
    return pagina.get_by_text("Ver sacola").count() > 0


def abrir_sacola(pagina) -> bool:
    alvo = pagina.get_by_text("Ver sacola")
    if not alvo.count():
        return False
    alvo.first.click(timeout=4000)
    pagina.wait_for_timeout(5000)
    return True


def capturar(nomes: list[str], cru: bool) -> None:
    from playwright.sync_api import sync_playwright

    PURAS.mkdir(parents=True, exist_ok=True)
    medidas = json.loads(MEDIDAS.read_text(encoding="utf-8")) if MEDIDAS.is_file() else {}
    with sync_playwright() as p:
        navegador = p.chromium.launch()
        for nome in nomes:
            receita = TOMADAS[nome]
            aparelho = {**APARELHOS[receita["aparelho"]]}
            if receita.get("altura"):
                aparelho["viewport"] = {**aparelho["viewport"],
                                        "height": receita["altura"]}
            ctx = navegador.new_context(
                locale="pt-BR", timezone_id="America/Sao_Paulo",
                service_workers="block", **aparelho)
            if not cru:
                ctx.route(ROTA, trocar(documento(receita["cfg"]),
                                       receita.get("fechada", False)))
            pagina = ctx.new_page()
            pagina.goto(receita.get("url", BASE), wait_until="domcontentloaded",
                        timeout=120_000)
            esperar(pagina)
            fechar_avisos(pagina)

            if receita.get("abrir_item") and not abrir_item(pagina, receita["abrir_item"]):
                print(f"--  {nome}: não consegui abrir a página do produto")
            if receita.get("item") and not pedir_item(pagina, receita["item"]):
                print(f"--  {nome}: não consegui pôr item na sacola")
            if receita.get("abrir_sacola") and not abrir_sacola(pagina):
                print(f"--  {nome}: não consegui abrir a sacola")
            if receita.get("abrir_item") or receita.get("item"):
                esperar(pagina, 6)
                fechar_avisos(pagina)

            pagina.evaluate(CONGELAR)
            pagina.wait_for_timeout(600)
            lido = pagina.evaluate(MEDIR)
            if not lido["botao"]:
                print(f"ATENÇÃO {nome}: o botão não está na tela — confira o documento")
            else:
                print(f"OK  {nome}  {lido['rotulo']!r}  {lido['classe']}")
            alvo = PURAS / f"{'cru-' if cru else ''}{nome}.png"
            pagina.screenshot(path=str(alvo), type="png")
            if not cru:
                medidas[nome] = {
                    "escala": aparelho["device_scale_factor"],
                    "viewport": aparelho["viewport"],
                    "cfg": receita["cfg"], **lido}
            ctx.close()
        navegador.close()
    if not cru:
        MEDIDAS.write_text(json.dumps(medidas, indent=1, ensure_ascii=False) + "\n",
                           encoding="utf-8")


def recortar() -> None:
    """Corta os recortes a partir da caixa do botão, medida no DOM.

    A regra da skill é *coordenada medida, nunca estimada na miniatura*. Aqui a
    medida vem do próprio navegador da captura, então o corte se refaz igual
    mesmo quando a página muda de altura entre tomadas.
    """
    from PIL import Image

    if not MEDIDAS.is_file():
        print("--  falta medidas.json: rode a captura antes")
        return
    medidas = json.loads(MEDIDAS.read_text(encoding="utf-8"))

    # (tomada, nome do recorte, alvo medido, folga esquerda/cima/direita/baixo)
    #
    # A folga da esquerda é generosa nos recortes do flutuante porque o botão
    # mora encostado na borda direita: cortar rente a ele deixaria uma tira de
    # 200 px, e o que prova "ele flutua por cima do cardápio" é justamente o
    # cardápio aparecendo atrás. Folga de 300 em tela de 390 é o jeito de dizer
    # "a largura inteira" sem repetir o número da tela.
    #
    # A ALTURA DO RECORTE É ORÇAMENTO DE SLIDE, e é ela que manda nas folgas.
    # Posto em 904 px de largura, o recorte cresce na proporção: a 390 px de
    # tela, cada 100 px de altura capturada viram 232 px de slide. Um slide de
    # miolo com chapéu, título de duas linhas e corpo de três tem ~614 px para
    # imagem — ou seja, dois recortes empilhados pedem ~110 px de altura cada.
    # Foi essa conta que encolheu as folgas da primeira rodada pela metade.
    CORTES = (
        # Dentro da sacola: o corte começa no vão abaixo dos cartões de sugestão
        # (cortá-los ao meio lê como render quebrado) e vai até o pé da tela,
        # porque o que prova "dentro da sacola" é o `Total do pedido` e o
        # `Continuar` embaixo do botão.
        ("cel-carrinho", "rec-sacola", "botao", (16, 8, 16, 200)),
        # Loja fechada, em duas faixas contínuas da MESMA captura — nunca uma
        # montagem: o aviso mora no cabeçalho e o botão no pé, com 470 px de
        # cardápio entre os dois.
        # O corte de cima começa 1 px abaixo do logotipo da loja: logotipo
        # cortado ao meio lê como render quebrado, e incluí-lo inteiro custaria
        # 100 px de altura capturada — 230 px de slide — para mostrar de novo a
        # marca que a capa já mostrou. O de baixo termina no pé da tela, com a
        # barra de navegação inteira, pelo mesmo motivo ao contrário: cortada
        # na metade dos ícones, ela é que viraria o defeito.
        ("cel-fechada", "rec-fechada-aviso", "fechado", (999, 58, 999, 20)),
        ("cel-fechada", "rec-fechada-botao", "botao", (300, 14, 16, 68)),
    )
    for tomada, saida, qual, folga in CORTES:
        m = medidas.get(tomada)
        arquivo = PURAS / f"{tomada}.png"
        if not m or not m.get(qual) or not arquivo.is_file():
            print(f"--  {saida}: falta a medida '{qual}' ou o arquivo de {tomada}")
            continue
        b, e = m[qual], m["escala"]
        largura, altura = m["pagina"]["w"], m["pagina"]["h"]
        caixa = (max(0, b["x"] - folga[0]), max(0, b["y"] - folga[1]),
                 min(largura, b["x"] + b["w"] + folga[2]),
                 min(altura, b["y"] + b["h"] + folga[3]))
        corte = tuple(round(v * e) for v in caixa)
        imagem = Image.open(arquivo)
        assert corte[2] <= imagem.width and corte[3] <= imagem.height, (
            f"{saida}: o corte {corte} passa da imagem {imagem.size}")
        imagem.crop(corte).save(PURAS / f"{saida}.png")
        print(f"OK  {saida}.png  ({corte[2] - corte[0]}x{corte[3] - corte[1]})")


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--so", action="append", choices=sorted(TOMADAS),
                    help="só esta tomada (pode repetir)")
    ap.add_argument("--cru", action="store_true",
                    help="sem a cena: o que a loja responde hoje")
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
