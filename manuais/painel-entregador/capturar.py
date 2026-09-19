"""Capturas do #120 — Painel para Entregadores, em produção.

Quatro imagens, na ordem do manual:

    01-painel-completo        o painel aberto, as duas colunas e os cartões
    02-abrir-pela-tela-delivery  o menu de ações do Delivery com "Painel Entregador"
    03-abrir-por-aplicativos     o card do app em /aplicativos, com a janela de apresentação
    04-detalhe-do-pedido         o cartão clicado, mostrando itens e endereço

Regras do projeto que este arquivo respeita: tema **claro**, espera do spinner **mais
5 segundos** depois de cada clique, widget de suporte escondido, NPS fechada antes de
fotografar (e filtrada pelo título, para não fechar o modal que é o assunto da foto).

    python capturar.py           # as quatro
    python capturar.py 01 04     # só algumas
"""
from __future__ import annotations

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

from beefood import APP, after_click, abrir, api_get, limpar_tela

PURAS = Path(__file__).resolve().parent / "imagens-puras"
PURAS.mkdir(exist_ok=True)


def cobrir_dados_pessoais(page):
    """Desfoca nome e telefone de cliente **antes** do print.

    O repositório é público e a `imagens-puras/` também é versionada, então a cobertura
    não pode ficar para a etapa de anotação. Quem diz o que cobrir é a própria API: a
    lista de `venda2/delivery` traz o `nome` de cada pedido, e o desfoque cai em toda
    folha do DOM cujo texto seja um desses nomes — ou um telefone.

    Desfoque, e não tarja: a caixa continua ocupando o mesmo espaço, e a tela do print
    fica igual à que o leitor vê.
    """
    bruto = page.evaluate("() => JSON.parse(localStorage.getItem('beefood_user_session') || '{}')")
    _, lista = api_get(
        page,
        f"/api/venda2/delivery/{bruto['empresaID']}/{bruto['filialID']}/{bruto['usuarioID']}/12",
    )
    nomes = sorted({
        (p.get("nome") or "").strip()
        for p in (lista if isinstance(lista, list) else [])
        if (p.get("nome") or "").strip()
    })
    # A varredura é por **nó de texto**, não por elemento: no detalhe do pedido o nome
    # divide a caixa com o ícone de pessoa, então o elemento tem filho e a busca por
    # folha passava batido — mediu 0 cobertos numa tela que mostrava o nome.
    quantos = page.evaluate(
        """(nomes) => {
            const alvos = new Set(nomes);
            const telefone = /^\\(?\\d{2}\\)?\\s?\\d{4,5}-?\\d{4}$/;
            const passo = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
            const marcar = [];
            while (passo.nextNode()) {
                const t = (passo.currentNode.nodeValue || '').trim();
                if (t && (alvos.has(t) || telefone.test(t))) marcar.push(passo.currentNode);
            }
            for (const no of marcar) {
                const capa = document.createElement('span');
                capa.style.filter = 'blur(5px)';
                no.parentNode.replaceChild(capa, no);
                capa.appendChild(no);
            }
            return marcar.length;
        }""",
        nomes,
    )
    print(f"   cobertos: {quantos} trechos ({len(nomes)} nomes na fila)")
    after_click(page, 600)


def foto(page, nome: str, **kwargs):
    destino = PURAS / f"{nome}.png"
    page.screenshot(path=str(destino), type="png", **kwargs)
    print("   gravada", destino.name)


def forcar_tema_claro(page):
    """Grava o tema claro no `localStorage` do next-themes e recarrega.

    Clicar no botão de tema é uma corrida perdida: a classe do `html` só aparece depois
    da hidratação, então a leitura de `class` logo após o `goto` às vezes diz `light`
    quando a tela ainda vai virar escura. Gravar a chave e recarregar é determinístico —
    e o painel **segue o tema do site** (`resolvedTheme`, em `PainelEntregadorConteudo`).
    """
    page.evaluate("() => localStorage.setItem('theme', 'light')")
    page.reload(wait_until="domcontentloaded")
    after_click(page, 7000)
    limpar_tela(page)
    classe = page.locator("html").get_attribute("class") or ""
    print("   tema:", classe or "(vazio)")
    if "dark" in classe:
        raise RuntimeError("a tela continuou escura — o print não serve para o manual")


def esperar_painel(page):
    """O cabeçalho mostra um spinner enquanto `useDeliveryPedidos` carrega."""
    page.wait_for_selector("text=EM PREPARO", timeout=30000)
    for _ in range(30):
        if not page.locator("svg.animate-spin").count():
            break
        page.wait_for_timeout(1000)
    after_click(page)


def cap_01_painel(page):
    print("== 01 painel completo ==")
    page.goto(f"{APP}/painel-entregador", wait_until="domcontentloaded")
    after_click(page, 8000)
    forcar_tema_claro(page)
    esperar_painel(page)
    colunas = page.locator("section h2")
    print("   colunas:", [colunas.nth(i).inner_text() for i in range(colunas.count())])
    cartoes = page.locator('section button[type="button"]')
    print("   cartões:", cartoes.count())
    # O cartão do painel não mostra nome nem telefone — a chamada fica como rede de
    # segurança, para o dia em que o cartão passar a mostrar.
    cobrir_dados_pessoais(page)
    foto(page, "01-painel-completo")


def cap_02_delivery(page):
    print("== 02 abrir pela tela Delivery ==")
    page.goto(f"{APP}/delivery", wait_until="domcontentloaded")
    after_click(page, 9000)
    forcar_tema_claro(page)
    # O ⋮ do cabeçalho e o ⋮ de cada cartão usam o mesmo ícone: são 28 botões iguais na
    # tela. O do cabeçalho é o **mais alto** — os outros vivem dentro das colunas do
    # kanban, que ainda rolam na horizontal. Pegar `.last` abre o menu de um cartão.
    botoes = page.locator("button", has=page.locator("svg.lucide-ellipsis-vertical"))
    alturas = [(botoes.nth(i).bounding_box() or {}).get("y", 9e9) for i in range(botoes.count())]
    indice = min(range(len(alturas)), key=lambda i: alturas[i])
    print(f"   ⋮ do cabeçalho: botão {indice} em y={alturas[indice]}")
    botoes.nth(indice).click()
    after_click(page, 2000)
    item = page.locator('[role="menuitem"]', has_text="Painel Entregador")
    print("   item no menu:", item.count(), "|", item.first.inner_text() if item.count() else "-")
    if not item.count():
        raise RuntimeError("o menu aberto não é o do cabeçalho")
    cobrir_dados_pessoais(page)
    foto(page, "02-abrir-pela-tela-delivery")
    page.keyboard.press("Escape")
    after_click(page, 800)


def cap_03_aplicativos(page):
    print("== 03 abrir por /aplicativos ==")
    page.goto(f"{APP}/aplicativos", wait_until="domcontentloaded")
    after_click(page, 9000)
    forcar_tema_claro(page)
    card = page.get_by_text("Painel para Entregadores", exact=True).first
    card.scroll_into_view_if_needed()
    after_click(page, 1200)
    card.click()
    after_click(page, 3000)
    limpar_tela(page)
    janela = page.locator('[role="dialog"]').filter(has_text="Painel para Entregadores")
    print("   janela aberta:", janela.count())
    foto(page, "03-abrir-por-aplicativos")
    page.keyboard.press("Escape")
    after_click(page, 800)


def cap_04_detalhe(page):
    print("== 04 detalhe do pedido ==")
    page.goto(f"{APP}/painel-entregador", wait_until="domcontentloaded")
    after_click(page, 8000)
    forcar_tema_claro(page)
    esperar_painel(page)
    # O primeiro cartão de "Em preparo" é o mais antigo da coluna (o painel ordena assim).
    cartao = page.locator('section button[type="button"]').first
    print("   cartão:", cartao.inner_text().replace("\n", " | "))
    cartao.click()
    # O detalhe chama `venda2/vendaDetalhes` e monta devagar: espera o fim do spinner.
    page.wait_for_selector("text=Itens do pedido", timeout=30000)
    after_click(page, 6000)
    cobrir_dados_pessoais(page)
    foto(page, "04-detalhe-do-pedido")
    page.keyboard.press("Escape")
    after_click(page, 800)


PASSOS = {
    "01": cap_01_painel,
    "02": cap_02_delivery,
    "03": cap_03_aplicativos,
    "04": cap_04_detalhe,
}

if __name__ == "__main__":
    escolhidos = sys.argv[1:] or list(PASSOS)
    with sync_playwright() as p:
        browser, ctx, page = abrir(p, "/delivery")
        for chave in escolhidos:
            PASSOS[chave](page)
        browser.close()
