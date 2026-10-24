"""Captura o Clonar e importar (Configuração → Clonar e importar) para o #130.

Duas descobertas valem o registro, porque mudaram o script:

* **A própria empresa não serve de origem.** Tentar validar `contato@beefood.com.br` contra ela
  mesma devolve `422` com *"A empresa de origem é a mesma da empresa atual."* O subtítulo da
  página ("ou entre cardápios desta empresa") vale para as outras abas, não para o cardápio.
* **A origem é a conta `beefood1`**, a primeira conta de teste da casa (seção 5 da memória
  geral): empresa 107, *BeeFood - Cardápio Digital*, com 110 setores e 1190 produtos. Isso dá
  uma prévia com números de verdade, e o destino já populado dispara o aviso que o manual
  precisa mostrar.

Aqui a técnica do ensaio não é precaução, é o que mantém o resto do manual de pé: confirmar
copiaria 1190 produtos para cima do cardápio que as outras capturas acabaram de montar. O que o
leitor precisa ver é a prévia, o aviso de que o destino já tem cadastro e o pedido de
confirmação — o resultado está descrito no texto. Logo, este script **não grava nada**.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "painel-entregador"))

from playwright.sync_api import sync_playwright
from beefood import abrir, after_click, limpar_tela

AQUI = Path(__file__).resolve().parent
PURAS = AQUI / "imagens-puras"

# Conta de teste da casa, de outra empresa — a de origem. Credenciais de sandbox, versionáveis.
ORIGEM_USUARIO = "beefood1"
ORIGEM_SENHA = "beefood123"

with sync_playwright() as p:
    browser, ctx, page = abrir(p, "/clonagem", viewport=(1440, 900), escala=1.5)
    after_click(page, 8000)
    limpar_tela(page)

    # 16. O formulário de origem, preenchido. A senha é a da empresa de origem, não a desta.
    page.locator("input").nth(0).fill(ORIGEM_USUARIO)
    campos = page.locator('input[type="password"]')
    (campos.first if campos.count() else page.locator("input").nth(1)).fill(ORIGEM_SENHA)
    page.wait_for_timeout(800)
    page.screenshot(path=str(PURAS / "16-clonagem-credenciais.png"))
    print("16 credenciais")

    page.locator("button").filter(has_text="Continuar").first.click()
    after_click(page, 7000)
    limpar_tela(page)

    # 17. A prévia: o que existe na origem, o que já existe aqui e a opção dos impostos.
    page.screenshot(path=str(PURAS / "17-clonagem-previa.png"))
    print("17 prévia")
    print("texto da prévia:\n", page.locator("main, body").last.inner_text()[:900])

    # 18. O pedido de confirmação — e o script para aqui, sem clicar em COPIAR.
    page.locator("button").filter(has_text="Copiar cadastro").first.click()
    after_click(page, 3000)
    page.screenshot(path=str(PURAS / "18-clonagem-confirmacao.png"))
    print("18 confirmação")
    # O ConfirmationDialog da casa não é um `role="dialog"`; o texto sai do corpo da página.
    corpo = page.locator("body").inner_text()
    print("pedido de confirmação:", "Copiar cadastro" in corpo, "| COPIAR visível:", "COPIAR" in corpo)
    print(">>> PARANDO AQUI: não clico em COPIAR (técnica do ensaio)")
    browser.close()
print("fim")
