#!/usr/bin/env python3
"""Fotografa o painel Cardápio no Tablet e recorta os prints do aplicativo.

Rodar da raiz do repositório:
    python carrosseis/07-cardapio-digital-tablet/capturar-telas.py

São duas origens, porque o recurso tem dois lados e só um deles roda aqui:

- **o painel** (`beefood.app/cardapio-digital-tablet`) é web, abre no Playwright
  e é a tela do leitor desta peça — dono de restaurante escolhendo sistema. As
  quatro capturas de painel são feitas para este carrossel;
- **o aplicativo do tablet** é Android (`Cardápio Mesa/Comanda`) e não roda no
  Cloud Agent. O que entra é o print de produção que o dono já mandou para o
  manual do modo kiosk, recortado aqui. Ele tem 2560x1600 — 16/10, a mesma
  proporção da tela do mockup `.tablet`.

## As telas que saem, e para que servem

| Arquivo | Slide | O que prova |
|---|---|---|
| `tablet-home.png` | 1, 8 | a tela inicial de verdade, inteira, para a moldura do mockup |
| `tablet-vitrine.png` | 3 | o banner e a faixa `Recomendados`, ampliados |
| `garcom-opcoes.png` | 4 | as dezesseis chamadas que o cliente pode fazer da mesa |
| `funcionalidades.png` | 5 | as chaves de Pix online, chamar garçom e fechar conta |
| `frota.png` | 7 | os contadores e os cartões dos aparelhos, com mesa e bateria |

## A frota vem de `tablets.json`, e por quê

O sandbox tem **um** aparelho, offline e sem mesa. "Controle todos os tablets em
uma única tela" com um cartão só mostra o contrário do que diz — é o mesmo caso
do cupom no totem: o recurso está ligado e a **vitrine** é que falta. A rota
`tablet2/aparelhos/{empresa}/{usuario}` passa a responder a lista deste arquivo.

O formato não foi adivinhado: saiu da resposta real (guardada em
`api-aparelho.json`) e do próprio JavaScript do painel, que lê `mesa`, `brand`,
`model`, `bateria`, `pingDif` e `versao` direto, sem mapear nada. Quem conta os
cinco cartões, pinta o status e escolhe o ícone de bateria continua sendo o
painel: o status sai do `ping2` comparado com o relógio do navegador, então o
script grava o horário em **America/Sao_Paulo**, que é o fuso do contexto.

## As chaves são ligadas na tela, e não salvas

Os interruptores da aba `Garçom Opções` chegam desligados no sandbox, e lista
inteira em cinza não mostra recurso nenhum. O script liga na interface — que é
o estado de quem está configurando — e **nunca toca em `SALVAR`**. O sandbox
fica como estava.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from PIL import Image

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
PURAS = AQUI / "imagens-puras"
MANUAL = RAIZ / "manuais" / "cardapio-digital-tablet-modo-kiosk" / "imagens-puras"

sys.path.append(str(RAIZ / ".cursor" / "skills" / "carrossel" / "scripts"))
from capturar import esperar, limpar, sessao  # noqa: E402

PAINEL = "https://beefood.app/cardapio-digital-tablet"
FUSO = ZoneInfo("America/Sao_Paulo")

# Campos do aparelho de verdade que a lista injetada repete sem mexer.
MOLDE = {
    "empresaID": 38311,
    "filialID": 39202,
    "usuarioID": 88711,
    "usuario": "",
    "funcionarioID": 194115,
    "funcionario": "",
    "serialNumber": "unknown",
    "systemVersion": "11",
    "apiLevel": 30,
    "brand": "samsung",
    "versao": "1.0.3.3",
    "memoria": "0.35/1.80 GB",
    "hd": "20.55/26.26 GB",
}

# As chamadas que ficam ligadas no print, todas na coluna da esquerda, que é a
# que aparece. Lista inteira em verde vira parede verde e não mostra escolha
# nenhuma; quatro ligadas em cinco mostram que a lista é do restaurante.
LIGAR = ["Copo", "Gelo", "Ketchup", "Limpar Mesa"]

# Folga em volta do recorte, em pixels lógicos. O painel não tem `id` estável
# para ancorar, mas tem caixa: cada recorte é medido no DOM na hora da captura,
# e não decorado em coordenada — modal que rola um pouco mais na próxima versão
# não leva o corte junto. Onde o vão entre fileiras é menor que a folga, ela
# cai (a lista de chamadas tem 12 px entre cartões, e 16 mostraria a fileira
# seguinte pela metade).
FOLGA = 16


def duracao(minutos: int) -> str:
    """O texto que o servidor manda em `pingDif` ("52 horas e 46 minutos")."""
    horas, resto = divmod(minutos, 60)
    m = f"{resto} minuto" + ("s" if resto != 1 else "")
    h = f"{horas} hora" + ("s" if horas != 1 else "")
    if not horas:
        return m
    return h if not resto else f"{h} e {m}"


def montar_frota() -> list[dict]:
    agora = datetime.now(FUSO)
    frota = []
    for i, linha in enumerate(json.loads((AQUI / "tablets.json").read_text("utf-8"))):
        minutos = linha["minutos"]
        visto = agora - timedelta(minutes=minutos)
        aparelho = dict(MOLDE)
        aparelho.update({
            "id": 11290 + i,
            "uniqueId": f"{11290 + i} (38311ca38592fb7840{80 + i:02d})",
            "mesa": linha["mesa"],
            "mesaID": i + 1,
            "model": linha["model"],
            "versao": linha.get("versao", MOLDE["versao"]),
            "bateria": f"{linha['bateria']:.2f} %",
            "ping2": visto.strftime("%Y-%m-%d %H:%M:%S"),
            "pingDif": duracao(minutos),
            "ultimaAtualizacao2": visto.strftime("%Y-%m-%d %H:%M:%S"),
            "ultimaAtualizacaoDif": duracao(minutos),
            "eventos": "0/0",
        })
        frota.append(aparelho)
    return frota


def rotear_frota(contexto, frota: list[dict]) -> None:
    def responder(rota):
        rota.fulfill(status=200, content_type="application/json",
                     body=json.dumps(frota, ensure_ascii=False))

    contexto.route("**/api/tablet2/aparelhos/**", responder)


def rolar_modal(pagina, quanto: int) -> None:
    """Rola o corpo do modal, que é o que tem barra — o fundo da página não."""
    pagina.evaluate("""(quanto) => {
        const d = document.querySelector('[role=dialog]');
        const corpo = [...d.querySelectorAll('*')].find(
            n => n.scrollHeight > n.clientHeight + 20) || d;
        corpo.scrollTop += quanto;
    }""", quanto)
    pagina.wait_for_timeout(700)


def ligar_chave(pagina, rotulo: str) -> None:
    """Liga o interruptor da linha daquele rótulo, se já não estiver ligado.

    A lista não tem `id` nem `for` ligando rótulo e chave: as duas coisas são
    irmãs dentro do cartão da opção, então o caminho é subir do texto até o
    cartão e procurar o `role=switch` de lá.
    """
    pagina.evaluate("""(rotulo) => {
        const textos = [...document.querySelectorAll('[role=dialog] *')]
            .filter(n => n.childElementCount === 0
                         && n.textContent.trim() === rotulo);
        if (!textos.length) throw new Error('rótulo não achado: ' + rotulo);
        let no = textos[0];
        while (no && !no.querySelector('button[role=switch]')) {
            no = no.parentElement;
        }
        const chave = no && no.querySelector('button[role=switch]');
        if (!chave) throw new Error('chave não achada: ' + rotulo);
        if (chave.getAttribute('data-state') !== 'checked') chave.click();
    }""", rotulo)
    pagina.wait_for_timeout(250)


def caixa_de(pagina, seletores: str, folga: int = FOLGA) -> dict:
    """A caixa que embrulha todos os elementos pedidos, com folga.

    `seletores` é JavaScript que devolve uma lista de nós; a caixa é a união
    das caixas deles.
    """
    medida = pagina.evaluate("""(codigo) => {
        const nos = eval(codigo);
        if (!nos.length) throw new Error('nada casou: ' + codigo);
        const caixas = nos.map(n => n.getBoundingClientRect());
        return {
            x: Math.min(...caixas.map(c => c.left)),
            y: Math.min(...caixas.map(c => c.top)),
            direita: Math.max(...caixas.map(c => c.right)),
            base: Math.max(...caixas.map(c => c.bottom)),
        };
    }""", seletores)
    return {
        "x": medida["x"] - folga,
        "y": medida["y"] - folga,
        "width": medida["direita"] - medida["x"] + folga * 2,
        "height": medida["base"] - medida["y"] + folga * 2,
    }


def fotografar(pagina, nome: str, seletores: str, folga: int = FOLGA) -> None:
    caixa = caixa_de(pagina, seletores, folga)
    pagina.screenshot(path=PURAS / f"{nome}.png", clip=caixa)
    largura, altura = Image.open(PURAS / f"{nome}.png").size
    print(f"OK  {nome}.png  {largura}x{altura}")


def do_manual() -> None:
    """A tela do aplicativo: print de produção, recortado sem reeditar cor."""
    home = Image.open(MANUAL / "03-home-logo.png")
    home.save(PURAS / "tablet-home.png")
    print(f"OK  tablet-home.png  {home.size[0]}x{home.size[1]}")

    # A vitrine: tudo o que é conteúdo, sem a barra do topo e sem a coluna de
    # atalhos — do banner ao fim da faixa `Recomendados`. As bordas foram
    # medidas no arquivo com uma régua desenhada por cima, e não estimadas: a
    # coluna acaba em 200, o banner vai de 220 a 2517, e o último cartão fecha
    # em 1580.
    vitrine = home.crop((210, 108, 2530, 1592))
    vitrine.save(PURAS / "tablet-vitrine.png")
    print(f"OK  tablet-vitrine.png  {vitrine.size[0]}x{vitrine.size[1]}")


def do_painel() -> None:
    frota = montar_frota()

    with sessao() as pg:
        # A rota vai no contexto, e não na página: o painel refaz a chamada
        # sozinho a cada 60 s, e rota de página não pega o que vem depois.
        rotear_frota(pg.context, frota)

        # A frota é fotografada numa janela mais estreita de propósito. Em
        # 1440 a grade abre em quatro colunas e o recorte sai com 1056 px
        # lógicos de largura — o dobro do que a régua da skill admite dentro
        # da margem, e a mesa some no feed. Em 900 a grade vira três colunas,
        # o cartão continua do mesmo tamanho e o recorte encolhe para 660:
        # a mesma tela, 1,4 vez maior na arte.
        pg.set_viewport_size({"width": 900, "height": 1000})
        pg.goto(PAINEL)
        esperar(pg)
        limpar(pg)
        # Dos cinco contadores ao último cartão de aparelho.
        fotografar(pg, "frota", """[
            document.querySelector('[class*=grid-cols-5]'),
            ...[...document.querySelectorAll('h4')]
                .map(n => n.closest('div[class*=overflow-hidden]'))
        ].filter(Boolean)""")

        # O modal tem largura fixa e precisa da janela larga para abrir em duas
        # colunas — é de lá que sai a coluna única dos dois recortes seguintes.
        pg.set_viewport_size({"width": 1440, "height": 900})
        pg.goto(PAINEL)
        esperar(pg)
        pg.click("text=Layout", timeout=15000)
        pg.wait_for_timeout(3000)
        pg.click("text=Configurar", timeout=15000)
        pg.wait_for_timeout(3500)
        limpar(pg)
        # Só a coluna da esquerda, que é onde estão as duas chaves deste slide:
        # `Pix online` e `Solicitar Fechamento de Conta`. A da direita é o
        # chamar garçom, que já tem slide próprio — e cortar o recorte pela
        # metade da largura é o que dobra o tamanho da letra na arte.
        # A segunda chave nasce por baixo do rodapé do modal, então o corpo
        # rola antes; o quanto rolar não vira coordenada, porque a caixa é
        # medida depois.
        rolar_modal(pg, 160)
        fotografar(pg, "funcionalidades", """
            [...document.querySelectorAll('[role=dialog] button[role=switch]')]
                .filter((_, i) => i % 2 === 0)
                .map(c => c.closest('div[class*=rounded]') || c.parentElement)
        """, folga=5)

        pg.click("[role=dialog] >> text=Garçom Opções", timeout=15000)
        pg.wait_for_timeout(2500)
        rolar_modal(pg, -400)
        for opcao in LIGAR:
            ligar_chave(pg, opcao)
        pg.wait_for_timeout(1200)
        limpar(pg)
        # Cinco chamadas da coluna da esquerda, e não as dezesseis. Duas
        # razões, e as duas são de leitura: metade da largura é o dobro da
        # letra na arte; e cinco linhas com quatro ligadas mostram que a lista
        # é uma **escolha**, que é o assunto do slide. A frase que explica a
        # tela cruza as duas colunas e ficaria cortada — ela foi para o texto.
        fotografar(pg, "garcom-opcoes", """
            [...document.querySelectorAll('[role=dialog] button[role=switch]')]
                .filter((_, i) => i % 2 === 0).slice(0, 5)
                .map(c => c.parentElement)
        """, folga=5)
        # Sem SALVAR: o que foi ligado morre com a aba.


def main() -> None:
    PURAS.mkdir(parents=True, exist_ok=True)
    do_manual()
    do_painel()


if __name__ == "__main__":
    main()
