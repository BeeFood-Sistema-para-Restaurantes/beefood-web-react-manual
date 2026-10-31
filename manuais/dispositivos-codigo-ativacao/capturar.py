"""Captura a geração do código de ativação em Configuração -> Dispositivos (#131).

O modal `Ativar aparelho` gera o código **ao abrir** (`useEffect` -> `gerar()` em
`ModalAtivarDispositivo.tsx`), e não por um botão. Então cada print do modal consome uma
vaga do plano enquanto o código viver. O script fotografa e, no fim, cancela os códigos que
criou pelo `POST /api/dispositivos2/pareamento/cancelar` — a vaga volta na hora.

Três variações do modal entram no manual, porque o leitor vê uma delas:

* aparelho com câmera (App Entregador): QR ao lado do código;
* aparelho sem câmera (App Garçom): só o código;
* tipo sem vaga livre (Totem, 1 de 1 em uso): a tela de limite, com CONTRATAR MAIS.

Regra da casa: depois de cada clique, esperar o spinner sumir e mais 5 s. Aqui o modal tem
contagem regressiva correndo, então o print sai depois de o código já estar na tela.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "painel-entregador"))

from playwright.sync_api import sync_playwright
from beefood import abrir, after_click, api_get, api_post, limpar_tela, sessao

AQUI = Path(__file__).resolve().parent
PURAS = AQUI / "imagens-puras"
PURAS.mkdir(parents=True, exist_ok=True)


def secao(page, rotulo):
    """A <section> daquele tipo de aparelho, achada pelo H2 do cabeçalho."""
    return page.locator("section").filter(has=page.locator(f'h2:text-is("{rotulo}")')).first


def ativar(page, rotulo):
    alvo = secao(page, rotulo)
    alvo.scroll_into_view_if_needed()
    page.wait_for_timeout(600)
    alvo.locator('button:has-text("Ativar aparelho")').first.click()
    after_click(page, 3000)


def fechar(page):
    page.locator('[role="dialog"] button:has-text("FECHAR")').first.click()
    after_click(page, 2000)


def tirar(page, nome):
    page.screenshot(path=str(PURAS / nome))
    print("pura:", nome)


with sync_playwright() as p:
    browser, ctx, page = abrir(p, "/dispositivos")
    limpar_tela(page)
    after_click(page, 2000)
    s = sessao(page)
    criados = []

    # 01 - a tela como ela abre, com o menu Configuração aberto no item Dispositivos.
    secao(page, "App Garçom").scroll_into_view_if_needed()
    page.wait_for_timeout(600)
    tirar(page, "01-tela-dispositivos.png")

    # 02 - aparelho sem câmera: o modal traz só o código.
    ativar(page, "App Garçom")
    tirar(page, "02-modal-codigo-app-garcom.png")
    fechar(page)

    # 03 - aparelho com câmera: o mesmo modal traz o QR ao lado do código.
    ativar(page, "App Entregador")
    tirar(page, "03-modal-codigo-qr-app-entregador.png")
    fechar(page)

    # 04 - sem vaga: o Totem do sandbox usa 1 de 1, então cai na tela de limite.
    ativar(page, "Totem de autoatendimento")
    tirar(page, "04-modal-sem-vaga-totem.png")
    fechar(page)

    # 05 - a lista depois dos códigos gerados: o cartão aguardando ativação e o Cancelar.
    page.locator('button[aria-label="Atualizar dispositivos"]').click()
    after_click(page, 4000)
    # Sem isto o botão Atualizar sai pintado de foco/hover e rouba a atenção do print.
    page.evaluate("() => document.activeElement && document.activeElement.blur()")
    page.mouse.move(700, 870)
    secao(page, "App Garçom").scroll_into_view_if_needed()
    page.wait_for_timeout(800)
    tirar(page, "05-codigo-aguardando-ativacao.png")

    # Devolve as vagas: cancela os códigos que ficaram abertos.
    _, corpo = api_get(page, f"/api/dispositivos2/{s['empresaID']}/{s['usuarioID']}")
    for aberto in (corpo or {}).get("pareamentosAbertos", []):
        r = api_post(
            page,
            "/api/dispositivos2/pareamento/cancelar",
            {
                "empresaID": s["empresaID"],
                "usuarioID": s["usuarioID"],
                "usuario": s["usuario"],
                "pareamentoID": aberto["pareamentoID"],
            },
        )
        print("cancelado", aberto["pareamentoID"], aberto["codigoFormatado"], r[0])

    browser.close()
