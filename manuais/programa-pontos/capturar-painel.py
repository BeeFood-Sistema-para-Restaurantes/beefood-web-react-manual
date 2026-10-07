"""Captura as telas do painel para o #126 — programa de pontos.

Somente **leitura**: o script navega, espera e fotografa. Nada aqui altera configuração.
O que o cenário precisava gravar (saldo no cliente de teste e uma recompensa de produto
com nome legível) está no `cenario.py`, separado de propósito — a regra da casa é deixar o
que grava longe do que é idempotente, para repetir a captura sem repetir a escrita.

Três decisões que valem explicar:

* **Card por `locator.screenshot()`, não recorte de viewport.** A Configuração é uma coluna
  de cards num container com rolagem própria (`div.flex-1.overflow-y-auto.min-h-0`), e o
  print do viewport inteiro deixaria metade da imagem com o menu lateral e o resto do card
  cortado no meio. Fotografar o card devolve 992x<altura> em DPR 1.5, com margem de
  respiro, e o Playwright rola até ele sozinho.
* **O telefone do cliente sai coberto na pura.** O repositório é público, e a `MEMORIA-GERAL`
  é explícita: nome, telefone e e-mail de cliente saem cobertos **na imagem pura**, porque
  ela também é versionada. Por isso o borrão é aplicado **no navegador**, com CSS, antes do
  print — e não com Pillow depois, que sujaria a pura ou obrigaria o `annotate.py` a
  transformá-la. O telefone de teste `(15) 99999-8888` fica visível: ele é versionado na
  seção 5 da memória e é parte do roteiro.
* **Espera do projeto em todo clique.** `after_click()` espera o spinner sumir e só então
  conta os 5 segundos. A aba *Saldo por Cliente* e a *Fila Processamento* chegam com
  contadores que entram depois da tabela, então essas duas levam mais tempo.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "painel-entregador"))

from playwright.sync_api import sync_playwright  # noqa: E402

from beefood import abrir, after_click, limpar_tela  # noqa: E402

SRC = Path(__file__).resolve().parent / "imagens-puras"
SRC.mkdir(exist_ok=True)

TELEFONE_TESTE = "(15) 99999-8888"

# A Configuração é uma coluna de cards dentro deste container, que tem rolagem própria: a
# página em si não rola, e `window.scrollTo` não faz nada aqui.
SCROLL = "div.flex-1.overflow-y-auto.min-h-0"

# Cobre telefone de cliente que não seja o de teste. Roda no navegador, antes do print, para
# a pura já nascer coberta.
COBRIR = """
(permitido) => {
  const re = /\\(\\d{2}\\)\\s?\\d{4,5}-\\d{4}/;
  const candidatos = [...document.querySelectorAll('span, p, div, td')].filter((e) => {
    const t = (e.textContent || '').trim();
    return re.test(t) && !t.includes(permitido);
  });
  // só o mais interno de cada cadeia: borrar o ancestral apagaria a linha inteira
  let n = 0;
  candidatos.forEach((e) => {
    if (candidatos.some((o) => o !== e && e.contains(o))) return;
    e.style.filter = 'blur(5px)';
    n += 1;
  });
  return n;
}
"""


def aba(page, nome: str, espera: int = 6000):
    page.get_by_role("button", name=nome, exact=True).first.click()
    after_click(page, espera)
    limpar_tela(page)
    print("telefones cobertos:", page.evaluate(COBRIR, TELEFONE_TESTE))


def card(page, titulo: str):
    """O card que contém este título: o primeiro ancestral arredondado do texto."""
    return page.get_by_text(titulo, exact=True).first.locator(
        'xpath=ancestor::div[contains(@class,"rounded")][1]'
    )


def tirar(alvo, nome: str):
    caminho = SRC / nome
    alvo.screenshot(path=str(caminho))
    print("PURA", nome)


def bloco(page, titulos, nome: str, folga: int = 16):
    """Recorte que cobre dois cards vizinhos, com uma folga em volta.

    *Bônus de boas-vindas* e *Entrega grátis com pontos* são dois cards curtos e irmãos:
    cada um sozinho renderia uma tira de 210 px, que é o "super zoom" que o dono recusou no
    #101. Juntos eles contam a mesma história — os dois acréscimos opcionais do programa.

    **As duas caixas são medidas na mesma rolagem.** Medir uma, rolar, e medir a outra
    devolve coordenada de quadro diferente: a primeira versão desta imagem saiu com o card
    de cima cortado fora, porque a caixa dele era de antes da rolagem.
    """
    primeiro = card(page, titulos[0])
    primeiro.scroll_into_view_if_needed()
    page.wait_for_timeout(600)
    topo = primeiro.bounding_box()["y"]  # 118 px deixa o card abaixo da barra de abas
    page.evaluate("([s, d]) => { document.querySelector(s).scrollTop += d }",
                  [SCROLL, topo - 118])
    page.wait_for_timeout(900)
    caixas = [card(page, t).bounding_box() for t in titulos]
    x = min(c["x"] for c in caixas) - folga
    y = min(c["y"] for c in caixas) - folga
    x1 = max(c["x"] + c["width"] for c in caixas) + folga
    y1 = max(c["y"] + c["height"] for c in caixas) + folga
    page.screenshot(path=str(SRC / nome),
                    clip={"x": x, "y": y, "width": x1 - x, "height": y1 - y})
    print("PURA", nome, "(recorte de", len(titulos), "cards)")


def main():
    with sync_playwright() as p:
        browser, ctx, page = abrir(p, "/programa-pontos", claro=True, viewport=(1440, 900))
        try:
            after_click(page, 9000)
            limpar_tela(page)
            print("telefones cobertos:", page.evaluate(COBRIR, TELEFONE_TESTE))

            # 01 — a tela inteira: onde o programa mora no menu, as quatro abas e a chave
            tirar(page, "01-ativar-programa-pontos.png")

            # 02 a 05 — os cards da Configuração, um a um
            tirar(card(page, "Regras de acúmulo"), "02-regras-de-acumulo.png")
            bloco(page, ["Bônus de boas-vindas", "Entrega grátis com pontos"],
                  "03-bonus-e-taxa-de-entrega.png")
            tirar(card(page, "Recompensas de desconto"), "04-recompensas-de-desconto.png")
            tirar(card(page, "Recompensas de produto"), "05-recompensas-de-produto.png")

            # 06 — Histórico
            aba(page, "Histórico", 7000)
            tirar(page, "13-historico-de-pontos.png")

            # 07 — Saldo por Cliente
            aba(page, "Saldo por Cliente", 8000)
            tirar(page, "14-saldo-por-cliente.png")

            # 08 — o extrato de um cliente, no painel lateral.
            # O padrão da casa para painel lateral manda **recortar no painel**: no viewport
            # de 1440x900 ele começa depois da metade, e o resto é a tela escurecida. A faixa
            # das etiquetas numeradas entra depois, em memória, no `annotate.py`.
            alvo = page.get_by_text(TELEFONE_TESTE, exact=False).first
            alvo.scroll_into_view_if_needed()
            alvo.locator("xpath=ancestor::div[.//button][1]").locator("button").last.click()
            after_click(page, 5000)
            limpar_tela(page)
            print("telefones cobertos:", page.evaluate(COBRIR, TELEFONE_TESTE))
            painel = page.locator('[role="dialog"]').last
            # Corta na altura logo depois da última linha do extrato: abaixo dela sobram
            # ~290 px de branco até o rodapé fixo, que na página publicada só empurram o
            # texto para baixo.
            cx = painel.bounding_box()
            ultima = painel.get_by_text("Migração de cashback", exact=False).last.bounding_box()
            page.screenshot(path=str(SRC / "15-extrato-do-cliente.png"), clip={
                "x": cx["x"], "y": cx["y"], "width": cx["width"],
                "height": ultima["y"] + ultima["height"] + 22 - cx["y"],
            })
            print("PURA 15-extrato-do-cliente.png (painel, cortado na altura)")

            # 09 — o formulário que credita pontos na mão.
            # Diálogo no centro da tela não está dentro do painel: recorte próprio, com o
            # painel visível atrás como contexto.
            painel.get_by_role("button", name="ADICIONAR").first.click()
            after_click(page, 3000)
            caixa = page.locator('[role="dialog"]').last.bounding_box()
            folga_x, folga_y = 230, 90
            page.screenshot(path=str(SRC / "16-adicionar-pontos.png"), clip={
                "x": max(0, caixa["x"] - folga_x),
                "y": max(0, caixa["y"] - folga_y),
                "width": caixa["width"] + 2 * folga_x,
                "height": caixa["height"] + 2 * folga_y,
            })
            print("PURA 16-adicionar-pontos.png (recorte do diálogo)")
            page.keyboard.press("Escape")
            after_click(page, 2000)
            page.keyboard.press("Escape")
            after_click(page, 2000)

            # 10 — Fila Processamento.
            # A fila é curta de propósito (só o que ainda não foi processado), e a metade de
            # baixo do viewport sai vazia. O corte na altura para logo depois da tabela.
            aba(page, "Fila Processamento", 8000)
            tabela = page.get_by_text("Última tentativa", exact=True).first.locator(
                "xpath=ancestor::table[1]"
            ).bounding_box()
            page.screenshot(path=str(SRC / "17-fila-de-processamento.png"),
                            clip={"x": 0, "y": 0, "width": 1440,
                                  "height": tabela["y"] + tabela["height"] + 24})
            print("PURA 17-fila-de-processamento.png (cortada na altura)")
        finally:
            ctx.close()
            browser.close()


if __name__ == "__main__":
    main()
