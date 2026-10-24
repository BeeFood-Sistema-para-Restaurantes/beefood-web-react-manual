"""Captura a importação do iFood para o #130, do cardápio vazio ao cardápio pronto.

Este é o único script do manual que **não** é idempotente: ele cria o cardápio inteiro a partir
da loja do iFood, e o dono autorizou em 23/10/2026 (*"pode copiar o ifood do one stand burger
nosso cliente base... pode simular todas as outras importações sem medo"*) depois de limpar o
cardápio e o histórico de importações do sandbox.

Por que ele acompanha a importação em laço, em vez de tirar um print por etapa: os estados de
**fila** e de **processamento** duram pouco e não voltam. A tela os mostra por alguns segundos
cada e segue para o seguinte, então o script fotografa a cada poucos segundos durante toda a
importação, grava os candidatos em `/tmp/cap-ifood/` e imprime o estado que a API devolveu em
cada rodada. Depois se escolhe, com calma, o melhor print de cada estado e só ele vira pura.

Regra da casa que vale aqui também: depois de cada clique, esperar o spinner sumir e mais 5 s.
No laço de acompanhamento isso não se aplica (a tela está, por definição, em movimento), mas o
print do estado **Concluído** espera a tela parar antes de ser tirado.
"""
import shutil
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "painel-entregador"))

from playwright.sync_api import sync_playwright
from beefood import abrir, after_click, api_get, limpar_tela, sessao

URL_IFOOD = (
    "https://www.ifood.com.br/delivery/sao-paulo-sp/"
    "one-stand-hamburgueria-parque-america/e66b1d8a-dff2-4b80-afed-36ed3c8dbc1a"
)
CARDAPIO_DESTINO = "BeeFood3 - Manual"

AQUI = Path(__file__).resolve().parent
PURAS = AQUI / "imagens-puras"
CAND = Path("/tmp/cap-ifood")
CAND.mkdir(parents=True, exist_ok=True)


def estado(page, s):
    st, corpo = api_get(page, f"/api/produto2/cardapio/copiariFood/{s['empresaID']}/{s['usuarioID']}")
    if isinstance(corpo, list) and corpo:
        i = corpo[0]
        return i.get("status"), i.get("processed_items"), i.get("total_items"), i.get("importado")
    return None, None, None, None


with sync_playwright() as p:
    browser, ctx, page = abrir(p, "/copiar-ifood", viewport=(1440, 900), escala=1.5)
    s = sessao(page)
    after_click(page)
    limpar_tela(page)

    # 1. O estado vazio: é o que o cliente novo vê, e já traz o botão único da tela.
    page.screenshot(path=str(PURAS / "01-copiar-ifood-vazio.png"))
    print("01 estado vazio")

    # 2. O modal, com a URL da loja e o cardápio destino escolhidos.
    page.locator("button").filter(has_text="Copiar Cardápio do iFood").last.click()
    after_click(page, 2000)
    dialogo = page.locator('div[role="dialog"]').filter(has_text="Copiar Cardápio do iFood").last
    dialogo.locator("input#ifood-url").fill(URL_IFOOD)
    page.wait_for_timeout(600)

    combo = dialogo.locator('[role="combobox"]')
    if combo.count():
        combo.first.click()
        page.wait_for_timeout(900)
        opcao = page.locator('[role="option"]').filter(has_text=CARDAPIO_DESTINO)
        (opcao.first if opcao.count() else page.locator('[role="option"]').first).click()
        page.wait_for_timeout(900)
    print("modal preenchido:", dialogo.inner_text().replace("\n", " | ")[:300])
    page.screenshot(path=str(PURAS / "02-modal-url-ifood.png"))
    print("02 modal preenchido")

    # 3. Confirma — daqui para frente a importação é real.
    dialogo.locator("button").filter(has_text="CONFIRMAR").first.click()
    t0 = time.time()
    print(">> CONFIRMAR clicado; acompanhando a importação")

    vistos = {}
    for rodada in range(220):
        page.wait_for_timeout(4000)
        st, feitos, total, importado = estado(page, s)
        seg = int(time.time() - t0)
        chave = st if st != "done" else ("done-ok" if importado == 1 else "done-parcial")
        arquivo = CAND / f"{chave}-{seg:04d}s.png"
        try:
            page.screenshot(path=str(arquivo))
        except Exception as e:
            print("  print falhou:", e)
        vistos.setdefault(chave, []).append(arquivo.name)
        print(f"  {seg:4d}s  {st}  {feitos}/{total}  importado={importado}")
        if st == "done" and importado == 1:
            break

    # O print do Concluído é o único que pode (e deve) esperar a tela parar de se mexer:
    # o confete da conclusão dura 2,5 s e a faixa verde de destaque, 3 s.
    page.wait_for_timeout(9000)
    page.reload(wait_until="domcontentloaded")
    after_click(page, 8000)
    limpar_tela(page)
    page.screenshot(path=str(PURAS / "05-importacao-concluida.png"))
    print("05 concluído")

    print("\ncandidatos por estado:")
    for k, v in vistos.items():
        print(f"  {k}: {len(v)} -> {v[:6]}")

    print("\nqtdProdutos depois:", api_get(page, f"/api/produto2/cardapio/qtdProdutos/{s['empresaID']}/{s['usuarioID']}"))
    browser.close()
print("fim")
