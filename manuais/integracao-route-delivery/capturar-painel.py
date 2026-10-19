"""Captura as telas do BeeFood para o #129 — integração com o Route Delivery.

São as sete imagens que o manual tem de próprio; as seis do painel do parceiro vêm do artigo
público dele, pelo `importar.py`.

O que este script faz de diferente do #127, e por quê:

* **A credencial é criada de verdade.** O #127 ensinava a copiar a credencial principal, que já
  existe, e fotografou o diálogo de criação pela técnica do ensaio — abre, fotografa, cancela.
  Aqui o pedido do dono é ensinar o caminho **CRIAR CREDENCIAL**, que é o mais amigável quando o
  parceiro vai guardar a credencial do lado dele: uma credencial por integração se desliga sem
  derrubar as outras. E esse caminho tem uma tela que só existe depois de criar — o diálogo
  **Credencial criada**, com o `clientId` e o `clientSecret` lado a lado. Sem criar, não há foto.
* **Por isso o script desfaz o que criou.** No fim ele apaga a credencial nova (achada pelo
  `clientId` que o próprio diálogo mostrou) e o webhook de exemplo, e confere os dois estados.
  O segredo que aparece na imagem é, então, de uma credencial que **não existe mais** — o mesmo
  cuidado que o #127 tomou com o secret do webhook.
* **Autenticação Basic fica em branco** no webhook: o Route Delivery não usa usuário e senha,
  ele confere o *Secret do webhook* que a BeeFood devolve. O campo aceita os dois em branco.

Uso, de dentro da pasta do manual:

    python3 capturar-painel.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "painel-entregador"))

from playwright.sync_api import sync_playwright  # noqa: E402

from beefood import abrir, after_click, limpar_tela  # noqa: E402

SRC = Path(__file__).resolve().parent / "imagens-puras"
SRC.mkdir(exist_ok=True)

# URL de exemplo, no formato que o Route Delivery mostra na tabela do ADM dele. A de verdade sai
# de lá; esta existe só para a captura, e o webhook é apagado no fim.
URL_EXEMPLO = "https://routedelivery.vercel.app/api/beefood/webhook/sua-loja-exemplo"
EMAIL = "contato@beefood.com.br"

# Os três eventos que o Route Delivery pede. Os de pagamento ficam desligados.
EVENTOS = ("Pedido criado", "Pedido atualizado", "Entrega atualizada")

ROLAR_PAINEL = """
(topo) => {
  const painel = document.querySelector('[role="dialog"]');
  if (!painel) return null;
  const d = [...painel.querySelectorAll('div')].find(
    (e) => String(e.className || '').includes('overflow-y-auto')
  );
  if (!d) return null;
  d.scrollTop = topo;
  return [d.scrollTop, d.scrollHeight, d.clientHeight];
}
"""


def salvar(page, nome: str):
    page.screenshot(path=str(SRC / nome))
    print("PURA", nome)


def switch_da_linha(escopo, rotulo: str):
    """O interruptor da linha que tem este texto (cada evento é um `label`)."""
    return escopo.locator("label").filter(has_text=rotulo).first.locator("button")


with sync_playwright() as p:
    browser, ctx, page = abrir(p, "/aplicativos")
    limpar_tela(page)
    after_click(page, 3000)
    salvar(page, "01-aplicativos-api-aberta.png")

    # --- painel lateral: viewport mais alto, para o painel caber inteiro ---------------
    page.set_viewport_size({"width": 1440, "height": 1300})
    after_click(page, 2000)

    page.get_by_text("API Aberta", exact=True).first.click()
    after_click(page, 8000)
    limpar_tela(page)
    print("rolagem do painel:", page.evaluate(ROLAR_PAINEL, 0))
    salvar(page, "02-painel-credencial.png")

    # --- o diálogo da nova credencial --------------------------------------------------
    page.get_by_role("button", name="CRIAR CREDENCIAL").click()
    after_click(page, 2500)
    nova = page.locator('[role="dialog"]').filter(has_text="Nova credencial adicional").last
    salvar(page, "04-nova-credencial.png")

    # --- criar de verdade: é a única forma de fotografar o diálogo com os dois valores --
    nova.get_by_role("button", name="CRIAR").click()
    after_click(page, 8000)
    criada = page.locator('[role="dialog"]').filter(has_text="Credencial criada").last
    print("diálogo Credencial criada:", criada.count())
    salvar(page, "05-credencial-criada.png")

    # o clientId fica no primeiro <code> do diálogo; é por ele que o desfazer acha a linha
    client_id = criada.locator("code").first.inner_text().strip()
    print("clientId criado:", client_id)
    criada.get_by_role("button", name="FECHAR").click()
    after_click(page, 3000)

    # --- aba Webhooks ------------------------------------------------------------------
    page.get_by_role("tab", name="Webhooks").click()
    after_click(page, 6000)
    salvar(page, "12-aba-webhooks.png")

    # --- o formulário do webhook: três eventos e Basic em branco -----------------------
    page.get_by_role("button", name="NOVO WEBHOOK").click()
    after_click(page, 2500)

    dialogo = page.locator('[role="dialog"]').filter(has_text="Novo webhook").last
    dialogo.locator('input[placeholder="https://..."]').fill(URL_EXEMPLO)
    for evento in EVENTOS:
        switch_da_linha(dialogo, evento).click()
        page.wait_for_timeout(250)
    dialogo.locator('input[type="email"]').fill(EMAIL)
    after_click(page, 2500)
    salvar(page, "13-novo-webhook.png")

    # --- salvar e fotografar o secret com a linha ativa --------------------------------
    dialogo.get_by_role("button", name="SALVAR").click()
    after_click(page, 8000)
    limpar_tela(page)
    print("secret na tela:", page.get_by_text("Secret do webhook").count())
    print("webhook na lista:", page.get_by_text(URL_EXEMPLO).count())
    salvar(page, "14-webhook-ativo.png")

    # --- desfazer 1: o webhook de exemplo ---------------------------------------------
    page.get_by_role("button", name="EXCLUIR").first.click()
    after_click(page, 2500)
    page.get_by_role("button", name="EXCLUIR (ENTER)").click()
    after_click(page, 6000)
    print("sobrou webhook?", page.get_by_text("Nenhum webhook cadastrado").count(),
          "(1 = lista vazia, estado original)")

    # --- desfazer 2: a credencial criada para a foto ----------------------------------
    page.get_by_role("tab", name="Credencial").click()
    after_click(page, 6000)
    linha = page.locator('div.rounded-2xl').filter(has_text=client_id).last
    linha.get_by_role("button", name="EXCLUIR").click()
    after_click(page, 2500)
    page.get_by_role("button", name="EXCLUIR (ENTER)").click()
    after_click(page, 6000)
    print("credencial da foto ainda existe?",
          page.get_by_text(client_id).count(), "(0 = apagada, estado original)")

    ctx.close()
    browser.close()
