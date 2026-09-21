#!/usr/bin/env python3
"""As telas das Campanhas Inteligentes, para o carrossel 09.

Nada é salvo. O editor da campanha não tem auto-save — só grava no SALVAR (F2)
ou ao confirmar a ativação —, então abrir, andar pelos três passos e sair por
ESC deixa a conta como estava. Nenhuma chave de campanha é tocada.

O viewport é 1600x1000 e não o 1440x900 padrão por dois motivos: em 1600 as
**seis** campanhas cabem na mesma tela (em 1440 a segunda linha fica cortada),
e 16/10 é a proporção exata da tela do `.notebook`, que é o aparelho da capa —
assim o `object-fit: cover` da moldura não come faixa nenhuma.

Uso:
    python carrosseis/09-campanhas-inteligentes/capturar-telas.py
"""

from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ / ".cursor/skills/carrossel/scripts"))

from capturar import esperar, limpar, sessao  # noqa: E402

SAIDA = Path(__file__).resolve().parent / "imagens-puras"
ROTA = "https://beefood.app/food-marketing/campanhas-whatsapp?tab=automacao"
NOVIDADE = "https://beefood.app/novidades/whatsapp-campanhas-inteligentes"

# O card da campanha: o menor elemento que tem o nome, o selo do gatilho e a
# linha de receita. Medir no DOM em vez de estimar é regra da casa — recorte
# chutado corta cartão pela metade.
CAIXA_DO_CARD = """(nome) => {
  const todos = [...document.querySelectorAll('div')].filter(d => {
    const t = d.innerText || '';
    return t.includes(nome) && t.includes('Gatilho') && t.includes('receita gerada');
  });
  const menor = todos.sort((a, b) => a.innerText.length - b.innerText.length)[0];
  if (!menor) return null;
  const c = menor.closest('[class*="rounded"]') || menor;
  const r = c.getBoundingClientRect();
  return {x: r.x, y: r.y, width: r.width, height: r.height};
}"""

# O mesmo card, cortado logo acima da linha de receita. A loja de teste marca
# R$ 0,00 em quatro das seis campanhas — verdade de conta nova, e leitura
# péssima numa peça que vende marketing. O que o slide afirma são o nome, o
# selo do gatilho e o estado, e é até aí que o recorte vai.
CAIXA_ATE_RECEITA = """(nome) => {
  const todos = [...document.querySelectorAll('div')].filter(d => {
    const t = d.innerText || '';
    return t.includes(nome) && t.includes('Gatilho') && t.includes('receita gerada');
  });
  const menor = todos.sort((a, b) => a.innerText.length - b.innerText.length)[0];
  if (!menor) return null;
  const card = menor.closest('[class*="rounded"]') || menor;
  const receitas = [...card.querySelectorAll('div')].filter(
    d => (d.innerText || '').includes('de receita gerada'));
  const receita = receitas.sort(
    (a, b) => a.innerText.length - b.innerText.length)[0];
  // o corte é logo abaixo do selo do gatilho: três fileiras com a descrição
  // junto não cabem no slide, e o que ele afirma são o nome, o gatilho e o
  // estado — a descrição vira uma linha de texto na copy
  const selos = [...card.querySelectorAll('div, span')].filter(
    d => (d.innerText || '').trim().startsWith('Gatilho:'));
  const selo = selos.sort((a, b) => a.innerText.length - b.innerText.length)[0];
  const r = card.getBoundingClientRect();
  const corte = selo ? selo.getBoundingClientRect().bottom + 2 : r.bottom;
  return {x: r.x, y: r.y, width: r.width, height: corte - r.y};
}"""

CAIXA_DO_TEXTO = """(alvo) => {
  const todos = [...document.querySelectorAll('div')].filter(
    d => (d.innerText || '').includes(alvo));
  const menor = todos.sort((a, b) => a.innerText.length - b.innerText.length)[0];
  if (!menor) return null;
  const c = menor.closest('[class*="rounded"]') || menor;
  const r = c.getBoundingClientRect();
  return {x: r.x, y: r.y, width: r.width, height: r.height};
}"""


def recortar(pagina, caixa: dict, nome: str, folga: int = 0,
             subir_base: int = 0) -> None:
    """Fotografa uma região medida, com folga opcional em volta.

    `subir_base` encurta o recorte por baixo, para cortar antes de uma linha
    que não deve entrar — é como as fileiras de card param acima da receita.
    """
    clip = {
        "x": max(caixa["x"] - folga, 0),
        "y": max(caixa["y"] - folga, 0),
        "width": caixa["width"] + folga * 2,
        "height": caixa["height"] + folga * 2 - subir_base,
    }
    pagina.screenshot(path=str(SAIDA / f"{nome}.png"), type="png", clip=clip)
    print(f"OK  {nome}.png  {round(clip['width'])}x{round(clip['height'])}")


def abrir_lista(pagina):
    pagina.set_viewport_size({"width": 1600, "height": 1000})
    pagina.goto(ROTA, wait_until="domcontentloaded", timeout=90000)
    esperar(pagina)
    # os cards levam de 10 a 16 s para chegar (memória do manual)
    pagina.wait_for_timeout(7000)
    limpar(pagina)


def main() -> None:
    SAIDA.mkdir(parents=True, exist_ok=True)

    with sessao() as pagina:
        abrir_lista(pagina)

        # 1. a tela inteira, que é a da capa
        pagina.screenshot(path=str(SAIDA / "lista-campanhas.png"), type="png")
        print("OK  lista-campanhas.png  1600x1000")

        # 2. o card que tem número de verdade: 1 envio, 1 pedido, R$ 34,02.
        # A tela de Resultado não serve para isso: o ROI dela é dos últimos 31
        # dias, e o único envio da loja de teste é de julho.
        recortar(pagina, pagina.evaluate(CAIXA_DO_CARD, "Carrinho abandonado"),
                 "card-resultado", folga=14)

        # ------------------------------------------------ dentro da campanha
        pagina.get_by_text("Carrinho abandonado", exact=True).first.click()
        pagina.wait_for_timeout(9000)
        limpar(pagina)

        # A loja de teste ajustou a espera para 5 min, e o quadro logo acima
        # diz "dispara ~15 min após o abandono", que é o padrão de fábrica
        # (lido no código pelo manual). Os dois na mesma imagem se desmentem.
        # O campo volta ao valor de fábrica só para a foto: nada é salvo, e a
        # saída é por ESC — o editor só grava no SALVAR (F2).
        marcou = pagina.evaluate("""() => {
          const todos = [...document.querySelectorAll('div')].filter(
            d => (d.innerText || '').includes('Esperar antes de enviar'));
          const menor = todos.sort(
            (a, b) => a.innerText.length - b.innerText.length)[0];
          const input = menor && menor.querySelector('input');
          if (input) input.setAttribute('data-foto', '1');
          return !!input;
        }""")
        if marcou:
            pagina.fill('[data-foto="1"]', "15")
            # sem tirar o foco o campo sai com anel vermelho e setas de
            # spinner, e na arte isso lê como erro de validação
            pagina.evaluate(
                """() => document.querySelector('[data-foto="1"]').blur()""")
            pagina.mouse.move(20, 20)
            pagina.wait_for_timeout(1500)

        # 3. o passo 1 inteiro: o quadro do gatilho, a origem do público e a
        # frase-resumo que a tela monta com os dois campos de tempo. É a prova
        # de que é o cliente quem marca a hora — uma faixa fina não sustenta
        # o slide sozinha.
        alto = pagina.evaluate(CAIXA_DO_TEXTO, "Como esta automação funciona")
        baixo = pagina.evaluate(CAIXA_DO_TEXTO, "Envia para quem abandonou")
        recortar(pagina, {
            "x": alto["x"],
            "y": alto["y"],
            "width": alto["width"],
            "height": baixo["y"] + baixo["height"] - alto["y"],
        }, "passo-gatilho", folga=10)

        # 4. a variação com variação automática, no passo 2
        pagina.get_by_text("Mensagem (com variaç", exact=False).first.click()
        pagina.wait_for_timeout(4000)
        recortar(pagina, pagina.evaluate(CAIXA_DO_TEXTO, "Variação 1"),
                 "variacao", folga=10)

        # 5. o anti-banimento, no passo 3
        pagina.get_by_text("Agenda e anti-spam", exact=False).first.click()
        pagina.wait_for_timeout(4000)
        recortar(pagina, pagina.evaluate(CAIXA_DO_TEXTO,
                                         "Só enviar para quem já me mandou"),
                 "anti-banimento", folga=10)

        # sai sem salvar
        pagina.keyboard.press("Escape")
        pagina.wait_for_timeout(3000)

        # ---------------------------------------- 6. as seis, em pares
        # A 1600 px a grade tem três colunas, e três cartões lado a lado num
        # slide de 1080 deixam o nome da campanha com 9 px. A 1150 a mesma
        # grade passa a duas colunas: o par exibido a 960 px sai em escala 1,
        # que é onde o rótulo do sistema ainda se lê no feed.
        pagina.set_viewport_size({"width": 1150, "height": 1400})
        pagina.reload(wait_until="domcontentloaded", timeout=90000)
        esperar(pagina)
        pagina.wait_for_timeout(7000)
        limpar(pagina)

        pares = [("Cashback parado", "Recuperador de vendas"),
                 ("Recebeu o cardápio", "Carrinho abandonado"),
                 ("Boas-vindas", "Aniversário")]
        for indice, (esq, dir_) in enumerate(pares, start=1):
            a = pagina.evaluate(CAIXA_ATE_RECEITA, esq)
            b = pagina.evaluate(CAIXA_ATE_RECEITA, dir_)
            recortar(pagina, {
                "x": a["x"],
                "y": a["y"],
                "width": b["x"] + b["width"] - a["x"],
                "height": max(a["height"], b["height"]),
            }, f"fileira-{indice}", folga=12, subir_base=12)

    # 7. a página da novidade no celular, para o CTA (convenção da casa)
    with sessao("celular", publico=True) as pagina:
        pagina.goto(NOVIDADE, wait_until="domcontentloaded", timeout=90000)
        esperar(pagina)
        # a data sai antes do print (ela mora num `<time>`): data na arte faz o
        # post parecer velho quando ele sai da fila de conteúdo. O botão de
        # fechar sai junto — na arte ele lê como se a peça tivesse um X.
        pagina.add_style_tag(content="""
            time{display:none !important}
            button.absolute.right-4.top-4{display:none !important}
        """)
        pagina.wait_for_timeout(1200)
        pagina.screenshot(path=str(SAIDA / "novidades-celular.png"), type="png")
        print("OK  novidades-celular.png")


if __name__ == "__main__":
    main()
