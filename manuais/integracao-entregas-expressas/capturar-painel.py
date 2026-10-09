"""Captura as telas do BeeFood para o #127 — integração com o Entregas Expressas.

São as cinco imagens que o manual tem de próprio. As outras quatro vêm do artigo público
do Entregas Expressas e entram por `importar.py`.

Três decisões que valem explicar:

* **Viewport alto só para o painel lateral.** A tela de Aplicativos sai no padrão da casa
  (1440x900 em DPR 1.5 = 2160x1350), mas o painel da API Aberta é mais alto que isso: a
  lista de permissões tem oito recursos, e com 900 px de altura o `SALVAR PERMISSÕES` fica
  abaixo da dobra. Com 1440x1300 o painel inteiro cabe numa captura só, e o `annotate.py`
  tira dela os dois recortes que o manual usa (a credencial e as permissões). Recorte é
  decisão de anotação, não de captura — é o padrão do painel lateral do #101.
* **O webhook é criado e apagado na mesma execução.** O manual precisa da tela com um
  webhook cadastrado, e a conta é a sandbox dos manuais, que fica num BeeFood de produção.
  Deixar um webhook ativo apontando para fora mandaria pedido de verdade para o parceiro,
  então o script apaga o que criou antes de fechar o navegador, e confere que a lista voltou
  a *Nenhum webhook cadastrado*. A URL é de exemplo e nenhum pedido é feito aqui, então nada
  chega a ser enviado.
* **Nada é alterado na credencial.** As permissões entram na foto como estão, e o diálogo da
  nova credencial é fotografado pela **técnica do ensaio**: abre, fotografa e cancela. Criar
  credencial de verdade obrigaria a apagá-la depois, e apagar credencial numa empresa que
  tem integração ativa é risco sem ganho — o `clientSecret` desta tela pode ser revelado
  depois pelo ícone de olho, então a foto do diálogo de criação não é o único caminho para
  ele. Mexer nas permissões também não acontece: o `SALVAR PERMISSÕES` só habilita depois de
  uma mudança, e por isso fotografar é seguro.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "painel-entregador"))

from playwright.sync_api import sync_playwright  # noqa: E402

from beefood import abrir, after_click, limpar_tela  # noqa: E402

SRC = Path(__file__).resolve().parent / "imagens-puras"
SRC.mkdir(exist_ok=True)

# URL de exemplo. A de verdade sai da tela do Entregas Expressas; esta existe só para a
# captura e o webhook é apagado no fim.
URL_EXEMPLO = "https://webhook.entregasexpressas.com.br/beefood/exemplo"
EMAIL = "contato@beefood.com.br"
USUARIO = "entregasexpressas"
SENHA = "s3nh4-do-parceiro"

# O conteúdo do painel rola por dentro; a página atrás tem o seu próprio scroll.
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


def switch_da_linha(page, rotulo: str):
    """O interruptor da linha que tem este texto (cada evento é um `label`)."""
    return page.locator("label").filter(has_text=rotulo).first.locator("button")


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
    salvar(page, "02-painel-api-aberta.png")

    # --- o diálogo da nova credencial, em ensaio: abre, fotografa e cancela ------------
    page.get_by_role("button", name="CRIAR CREDENCIAL").click()
    after_click(page, 2500)
    nova = page.locator('[role="dialog"]').filter(has_text="Nova credencial adicional").last
    salvar(page, "04-nova-credencial.png")
    nova.get_by_role("button", name="CANCELAR").click()
    after_click(page, 2000)
    print("diálogo fechado sem criar:",
          page.locator('[role="dialog"]').filter(has_text="Nova credencial adicional").count() == 0)

    # --- aba Webhooks ------------------------------------------------------------------
    page.get_by_role("tab", name="Webhooks").click()
    after_click(page, 6000)
    salvar(page, "08-aba-webhooks.png")

    # --- o formulário do webhook ------------------------------------------------------
    page.get_by_role("button", name="NOVO WEBHOOK").click()
    after_click(page, 2500)

    dialogo = page.locator('[role="dialog"]').filter(has_text="Novo webhook").last
    dialogo.locator('input[placeholder="https://..."]').fill(URL_EXEMPLO)
    for evento in ("Pedido criado", "Pedido atualizado", "Entrega atualizada",
                   "Pagamento criado", "Pagamento atualizado"):
        switch_da_linha(dialogo, evento).click()
        page.wait_for_timeout(250)
    dialogo.locator('input[type="email"]').fill(EMAIL)
    dialogo.locator('input[placeholder="clientId"]').fill(USUARIO)
    dialogo.locator('input[placeholder="clientSecret"]').fill(SENHA)
    after_click(page, 2500)
    salvar(page, "09-novo-webhook.png")

    # --- salvar e fotografar a lista com o webhook ativo ------------------------------
    dialogo.get_by_role("button", name="SALVAR").click()
    after_click(page, 8000)
    limpar_tela(page)
    print("secret na tela:", page.get_by_text("Secret do webhook").count())
    print("webhook na lista:", page.get_by_text(URL_EXEMPLO).count())
    salvar(page, "10-webhook-ativo.png")

    # --- desfazer: a sandbox não fica com webhook apontando para fora -----------------
    page.get_by_role("button", name="EXCLUIR").first.click()
    after_click(page, 2500)
    page.get_by_role("button", name="EXCLUIR (ENTER)").click()
    after_click(page, 6000)
    print("sobrou webhook?", page.get_by_text("Nenhum webhook cadastrado").count(),
          "(1 = lista vazia, estado original)")

    ctx.close()
    browser.close()
