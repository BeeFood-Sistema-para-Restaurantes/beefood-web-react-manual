#!/usr/bin/env python3
"""As duas capturas deste carrossel que exigem clique.

O resto sai direto do `capturar-cardapio.py` (o cardápio modelo com a nossa
mídia injetada na resposta da API) e do `capturar.py`.

1. **A agenda com um dia só marcado** (`painel-dias.png`). O slide diz "combo de
   quarta aparece só na quarta", e o print do manual mostra os sete dias acesos
   — a arte contradizia a frase. Aqui o script abre o modal de Capas e
   Destaques no sandbox, expande a agenda da primeira mídia, apaga seis dias e
   fotografa só a linha. **Não salva**: fecha descartando, e o sandbox fica como
   estava.
2. **A página de novidades no CTA** (`novidades-celular.png`). A lista é
   ordenada por data, e a desta publicação é de agosto: aberta na home, a tela
   mostra outra novidade, e o CTA acabava com um print falando de outro
   assunto. O script filtra o aplicativo Cardápio Digital e rola até o
   **título** desta novidade encostar no cabeçalho fixo — parando no cartão
   inteiro, a data de publicação aparece na arte e data o post.

Uso:
    python3 carrosseis/cardapio-capas-destaques/capturar-telas.py
"""

from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ / ".cursor/skills/carrossel/scripts"))

from capturar import sessao, esperar, limpar  # noqa: E402

SAIDA = Path(__file__).resolve().parent / "imagens-puras"
TITULO = "Avisos, capas e destaques com imagem e vídeo"

# Altura do cabeçalho fixo da página, em px lógicos: sem esse desconto o título
# do cartão nasce embaixo dele.
CABECALHO = 64

# D S T Q Q S S: a quarta-feira é o quarto botão da fileira.
QUARTA = 3


def agenda_de_um_dia_so() -> None:
    """Fotografa a linha dos dias com só a quarta marcada, e não salva nada."""
    with sessao("painel") as pagina:
        pagina.goto("https://beefood.app/cardapio-digital",
                    wait_until="domcontentloaded", timeout=90000)
        esperar(pagina)
        limpar(pagina)

        botao = pagina.locator("button:has-text('CAPAS E DESTAQUES')").first
        botao.scroll_into_view_if_needed()
        pagina.wait_for_timeout(600)
        botao.click()
        pagina.wait_for_timeout(4000)

        pagina.locator("button:has-text('AGENDAR')").first.click()
        pagina.wait_for_timeout(1500)

        linha = pagina.locator("label:has-text('Dias da semana')").first.locator(
            "xpath=following-sibling::div[1]")
        dias = linha.locator("button").filter(has_not_text="TODOS")
        for i in range(dias.count()):
            if i != QUARTA:
                dias.nth(i).click()
                pagina.wait_for_timeout(200)
        # Sem isso o último dia clicado fica com o cinza de foco e o cursor
        # deixa o de baixo em hover — dois estados que não existem no print.
        pagina.evaluate("() => document.activeElement && document.activeElement.blur()")
        pagina.mouse.move(4, 4)
        pagina.wait_for_timeout(800)

        # O recorte vai do rótulo até a borda direita do TODOS: a caixa do
        # contêiner tem a largura do modal inteiro, e o vazio da direita
        # encolheria os dias na hora de entrar no slide.
        rotulo = pagina.locator("label:has-text('Dias da semana')").first.bounding_box()
        todos = linha.locator("button:has-text('TODOS')").first.bounding_box()
        fundo = linha.bounding_box()
        folga = 16
        arquivo = SAIDA / "painel-dias.png"
        pagina.screenshot(path=str(arquivo), type="png", clip={
            "x": rotulo["x"] - folga,
            "y": rotulo["y"] - folga,
            "width": todos["x"] + todos["width"] + folga - (rotulo["x"] - folga),
            "height": fundo["y"] + fundo["height"] + folga - (rotulo["y"] - folga)})

        # Sair sem gravar: o modal é sujo e pede confirmação.
        pagina.locator("button:has-text('FECHAR (ESC)')").first.click()
        pagina.wait_for_timeout(1200)
        descartar = pagina.locator("button:has-text('DESCARTAR')")
        if descartar.count():
            descartar.first.click()
            pagina.wait_for_timeout(800)
        print(f"OK  {arquivo.relative_to(RAIZ)}")


def pagina_de_novidades() -> None:
    with sessao("celular", publico=True) as pagina:
        pagina.goto("https://beefood.app/novidades",
                    wait_until="domcontentloaded", timeout=90000)
        esperar(pagina)
        limpar(pagina)

        pagina.click("button:has-text('Todos os aplicativos')")
        pagina.wait_for_timeout(1500)
        pagina.locator('[role="option"]').filter(
            has_text="Cardápio Digital").first.click()
        pagina.wait_for_timeout(2500)

        pagina.evaluate(
            """(dados) => {
              const titulo = [...document.querySelectorAll('h2, h3')]
                .find(e => (e.textContent || '').includes(dados.titulo));
              if (!titulo) throw new Error('cartão da novidade não encontrado');
              // A âncora é o título, não o cartão: encostando o cartão no
              // cabeçalho, a data de publicação entra no print e **data o
              // post** — carrossel aprovado sai da fila semanas depois. Parando
              // no título, as etiquetas e a data ficam atrás do cabeçalho fixo.
              const y = titulo.getBoundingClientRect().top + window.scrollY;
              window.scrollTo(0, y - dados.cabecalho - dados.folga);
            }""",
            {"titulo": TITULO, "cabecalho": CABECALHO, "folga": 12})
        pagina.wait_for_timeout(1500)

        arquivo = SAIDA / "novidades-celular.png"
        pagina.screenshot(path=str(arquivo), type="png")
        print(f"OK  {arquivo.relative_to(RAIZ)}")


def main() -> int:
    SAIDA.mkdir(parents=True, exist_ok=True)
    agenda_de_um_dia_so()
    pagina_de_novidades()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
