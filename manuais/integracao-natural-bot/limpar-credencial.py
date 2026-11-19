"""Apaga a credencial de produção que o `capturar-beefood.py` criou para a foto.

O `clientSecret` aparece inteiro na imagem 06, e o repositório é público. Como no #129, a saída
é a credencial **deixar de existir**: terminadas as capturas, este script a acha pelo `clientId`
guardado em `/tmp/manual-134-cred.json`, apaga e confere que ela saiu da lista.

Quem conecta a Natural Bot de homologação é a credencial de **sandbox**, criada no portal e que
não aparece em imagem nenhuma — ela continua de pé.

Uso, de dentro da pasta do manual:

    python3 limpar-credencial.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "painel-entregador"))

from playwright.sync_api import sync_playwright  # noqa: E402

from beefood import abrir, after_click, limpar_tela  # noqa: E402

CRED = Path("/tmp/manual-134-cred.json")
client_id = json.loads(CRED.read_text())["clientId"]

with sync_playwright() as p:
    browser, ctx, page = abrir(p, "/aplicativos")
    limpar_tela(page)
    page.set_viewport_size({"width": 1440, "height": 1300})
    after_click(page, 3000)
    page.get_by_text("API Aberta", exact=True).first.click()
    after_click(page, 9000)

    linha = page.locator("div.rounded-2xl").filter(has_text=client_id).last
    linha.get_by_role("button", name="EXCLUIR").click()
    after_click(page, 2500)
    page.get_by_role("button", name="EXCLUIR (ENTER)").click()
    after_click(page, 7000)
    print("credencial da foto ainda existe?", page.get_by_text(client_id).count(),
          "(0 = apagada, estado original)")

    ctx.close()
    browser.close()
