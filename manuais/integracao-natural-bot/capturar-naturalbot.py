"""Captura as nove telas do painel da Natural Bot para o #134.

Duas credenciais entram aqui, e o motivo está no `MEMORIA.md`: o painel de **homologação** da
Natural Bot conversa com a **sandbox** da BeeFood (`api-sandbox.beefood.app`), que recusa
credencial de produção com *"A BeeFood recusou o client ID ou o client secret"*. Então:

* a credencial de **produção** criada pelo `capturar-beefood.py` entra no formulário só para a
  foto, pela técnica do ensaio — preenche, fotografa, **não** clica em *Conectar*. É a mesma que
  aparece na imagem 04, e é por isso que o `clientId` das duas imagens combina;
* a credencial de **sandbox** (criada no portal, em `docs.beefood.app`, com os mesmos seis
  acessos) é a que conecta de verdade, e segue daí para frente. Ela não aparece em imagem
  nenhuma: o campo de secret é de senha, e o `clientId` só reaparece mascarado na imagem 09.

Uso, de dentro da pasta do manual:

    NB_SENHA='...' BF_SANDBOX_CLIENT_ID='...' BF_SANDBOX_CLIENT_SECRET='...' \\
        python3 capturar-naturalbot.py
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from playwright.sync_api import sync_playwright  # noqa: E402

from naturalbot import abrir, card_integracao, esperar, limpar_tela, menu  # noqa: E402

SRC = Path(__file__).resolve().parent / "imagens-puras"
SRC.mkdir(exist_ok=True)
CRED_PRODUCAO = Path("/tmp/manual-134-cred.json")


def salvar(page, nome: str):
    limpar_tela(page)
    page.screenshot(path=str(SRC / nome))
    print("PURA", nome)


def sandbox() -> dict:
    cid = os.environ.get("BF_SANDBOX_CLIENT_ID")
    secret = os.environ.get("BF_SANDBOX_CLIENT_SECRET")
    if not cid or not secret:
        raise RuntimeError("defina BF_SANDBOX_CLIENT_ID e BF_SANDBOX_CLIENT_SECRET")
    return {"clientId": cid, "clientSecret": secret}


def preencher(page, dialogo, cred: dict):
    dialogo.locator("input#beefood-client-id").fill(cred["clientId"])
    dialogo.locator("input#beefood-client-secret").fill(cred["clientSecret"])
    esperar(page, 2000)


with sync_playwright() as p:
    browser, ctx, page = abrir(p)

    # --- aba Integrações: o aviso de um gestor de PDV por vez e os cards -----------------
    menu(page, "Configurações")
    page.locator('[role="tab"]', has_text="Integrações").first.click()
    esperar(page, 7000)
    salvar(page, "05a-nb-integracoes.png")

    botao = card_integracao(page, "BeeFood")
    salvar(page, "05b-nb-card-beefood.png")

    # --- o formulário da credencial -----------------------------------------------------
    botao.click()
    esperar(page, 8000)
    editar = page.get_by_role("button", name="Editar Integração")
    if editar.count():
        editar.first.click()
        esperar(page, 6000)
    dialogo = page.locator('[role="dialog"]').last

    # Ensaio: a credencial de produção da imagem 04 entra só para a foto.
    preencher(page, dialogo, json.loads(CRED_PRODUCAO.read_text()))
    salvar(page, "06-nb-form-credencial.png")

    # Daqui para frente é a credencial de sandbox, a única que o painel de homologação aceita.
    preencher(page, dialogo, sandbox())
    dialogo.get_by_role("button", name="Conectar").first.click()
    esperar(page, 18000)

    # --- cardápio e de-para de pagamentos ------------------------------------------------
    dialogo = page.locator('[role="dialog"]').last
    salvar(page, "07-nb-cardapio-pagamentos.png")

    dialogo.get_by_role("button", name="Salvar").first.click()
    esperar(page, 20000)
    salvar(page, "08-nb-verificacao.png")
    page.locator('[role="dialog"]').last.get_by_role("button", name="Concluir").click()
    esperar(page, 6000)

    # --- a tela de integração já configurada --------------------------------------------
    card_integracao(page, "BeeFood").click()
    esperar(page, 8000)
    salvar(page, "09-nb-integracao-configurada.png")
    page.locator('[role="dialog"]').last.get_by_role("button", name="Fechar").first.click()
    esperar(page, 4000)

    # --- Cardápio → Produtos → Sinc. BeeFood ---------------------------------------------
    menu(page, "Cardápio", "Produtos")
    esperar(page, 6000)
    salvar(page, "10-nb-produtos-sinc.png")

    page.get_by_role("button", name="Sinc. BeeFood").click()
    esperar(page, 8000)
    importar = page.locator('[role="dialog"]').last
    salvar(page, "11-nb-importacao-opcoes.png")

    importar.get_by_role("button", name="Importar").click()
    for _ in range(12):
        esperar(page, 10000)
        if "Importação concluída" in page.locator('[role="dialog"]').last.inner_text():
            break
    salvar(page, "12-nb-importacao-concluida.png")
    page.locator('[role="dialog"]').last.get_by_role("button", name="Fechar").first.click()
    esperar(page, 5000)

    # A lista com o cardápio importado não é foto do manual — o dono cortou: o que o leitor
    # precisa é do caminho da importação, não da prova de que ela trouxe algo. Fica a
    # conferência em tela, que é onde mora a pegadinha: a página abre na primeira categoria,
    # que pode estar vazia, e a aba **Todos** é a que mostra o que chegou.
    page.reload(wait_until="domcontentloaded")
    esperar(page, 12000)
    page.get_by_role("button", name="Todos").first.click()
    esperar(page, 8000)
    print("produtos na aba Todos:",
          page.locator("table tbody tr").count() or "confira na tela")

    ctx.close()
    browser.close()
