"""Monta na sandbox o cenário que as capturas do #126 precisam.

Duas coisas faltavam para fotografar o programa de pontos ponta a ponta:

1. **Saldo no cliente de teste.** O crédito de pontos acontece no processamento da
   **madrugada** — a própria tela avisa: *"O saldo de pontos é processado toda madrugada
   para pedidos pagos e finalizados"*. Fechar um pedido agora não produz saldo hoje, e sem
   saldo não há o que fotografar no cardápio digital: nem extrato, nem resgate. O caminho
   que o produto oferece é o **ADICIONAR** da aba *Saldo por Cliente*, que é exatamente o
   que o manual ensina — ou seja, o cenário se monta pela tela, no primeiro degrau da
   `cenario-sandbox`, sem rota farejada e sem banco.
2. **Uma recompensa de produto com nome legível.** A recompensa que já existia aponta para
   o produto **2515303**, que não está na lista deste cardápio (os produtos da filial 39202
   vão de 2624013 a 2624160), então a linha sai como *Produto #2515303*. Isso é achado, não
   defeito, e o manual explica — mas a imagem precisava também de uma linha **com nome**.

Como todo script de cenário da casa, ele é **ensaio por padrão**: sem `VALENDO=1` percorre
o caminho inteiro, imprime o que leu e para antes do clique que grava.

    pontos      — credita pontos no cliente de teste até ele chegar em ALVO_PONTOS
    recompensa  — cadastra a recompensa de produto do CHICKEN DELUXE
    estado      — só lê: saldo do cliente e recompensas cadastradas

O comando `pontos` é **idempotente**: ele lê o saldo atual e credita só a diferença, então
rodar duas vezes não dobra o saldo. Sem essa trava, repetir o cenário estraga as capturas
que já existem.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "painel-entregador"))

from playwright.sync_api import sync_playwright  # noqa: E402

from beefood import abrir, after_click, limpar_tela  # noqa: E402

VALENDO = os.environ.get("VALENDO") == "1"

TELEFONE_TESTE = "(15) 99999-8888"
ALVO_PONTOS = 121          # 121 deixa R$ 5,00 (50) e R$ 10,00 (100) ao alcance e R$ 20,00 (180) fora
MOTIVO = "Credito de teste para as capturas do manual"

PRODUTO = "CHICKEN DELUXE"
PONTOS_PRODUTO = "80"      # abaixo do saldo, para a recompensa aparecer resgatável no cardápio


def aba(page, nome: str):
    page.get_by_role("button", name=nome, exact=True).first.click()
    after_click(page, 5000)
    limpar_tela(page)


def abrir_cliente(page):
    """Abre o painel lateral do cliente de teste pela aba Saldo por Cliente."""
    aba(page, "Saldo por Cliente")
    alvo = page.get_by_text(TELEFONE_TESTE, exact=False).first
    alvo.scroll_into_view_if_needed()
    # a linha é o primeiro ancestral que tem botão: o olho que abre o extrato
    linha = alvo.locator("xpath=ancestor::div[.//button][1]")
    linha.locator("button").last.click()
    after_click(page, 4000)
    return page.locator('[role="dialog"]').last


def saldo_atual(painel) -> int:
    texto = painel.inner_text()
    for linha in texto.splitlines():
        if linha.strip().endswith("pts"):
            try:
                return int(linha.strip().split()[0])
            except ValueError:
                continue
    return 0


def cmd_estado(page):
    painel = abrir_cliente(page)
    print("SALDO:", saldo_atual(painel), "pts")
    print(painel.inner_text()[:700])
    page.keyboard.press("Escape")
    after_click(page, 1500)
    aba(page, "Configuração")
    for titulo in ("Recompensas de desconto", "Recompensas de produto"):
        card = page.get_by_text(titulo, exact=True).first.locator(
            'xpath=ancestor::div[contains(@class,"rounded")][1]'
        )
        card.scroll_into_view_if_needed()
        print("=" * 20, titulo)
        print(card.inner_text())


def cmd_pontos(page):
    painel = abrir_cliente(page)
    atual = saldo_atual(painel)
    falta = ALVO_PONTOS - atual
    print(f"saldo atual {atual} pts; alvo {ALVO_PONTOS} pts; falta {falta}")
    if falta <= 0:
        print("nada a fazer — o cenário já está montado")
        return
    painel.get_by_role("button", name="ADICIONAR").first.click()
    after_click(page, 2500)
    form = page.locator('[role="dialog"]').last
    campos = form.locator("input, textarea")
    # ordem dos campos: Pontos, Expira em (dias) — opcional, Motivo *
    campos.nth(0).fill(str(falta))
    campos.nth(2).fill(MOTIVO)
    page.wait_for_timeout(600)
    print("formulário preenchido:", form.inner_text().replace("\n", " | ")[:200])
    if not VALENDO:
        print("ENSAIO — o CONFIRMAR (F2) não foi clicado. Rode com VALENDO=1 para gravar.")
        return
    form.locator("button").filter(has_text="CONFIRMAR").last.click()
    after_click(page, 6000)
    print("depois:", page.locator('[role="dialog"]').last.inner_text().replace("\n", " | ")[:220])


def cmd_recompensa(page):
    aba(page, "Configuração")
    card = page.get_by_text("Recompensas de produto", exact=True).first.locator(
        'xpath=ancestor::div[contains(@class,"rounded")][1]'
    )
    card.scroll_into_view_if_needed()
    if PRODUTO in card.inner_text().upper():
        print(f"{PRODUTO} já está cadastrado — nada a fazer")
        return
    card.get_by_text("Selecionar produto").first.click()
    after_click(page, 4000)
    modal = page.locator('[role="dialog"]').last
    modal.locator("input").first.fill(PRODUTO)
    page.wait_for_timeout(2500)
    item = modal.get_by_text(PRODUTO, exact=True).first
    print("produto encontrado:", item.inner_text())
    item.click()
    after_click(page, 2500)
    card.locator("input").last.fill(PONTOS_PRODUTO)
    page.wait_for_timeout(500)
    print("a cadastrar:", PRODUTO, "por", PONTOS_PRODUTO, "pontos")
    if not VALENDO:
        print("ENSAIO — o ADICIONAR não foi clicado. Rode com VALENDO=1 para gravar.")
        return
    card.get_by_role("button", name="ADICIONAR").first.click()
    after_click(page, 6000)
    print(card.inner_text())


COMANDOS = {"estado": cmd_estado, "pontos": cmd_pontos, "recompensa": cmd_recompensa}


def main():
    alvo = sys.argv[1] if len(sys.argv) > 1 else "estado"
    if alvo not in COMANDOS:
        print("uso: python3 cenario.py [estado|pontos|recompensa]   (VALENDO=1 para gravar)")
        raise SystemExit(2)
    with sync_playwright() as p:
        browser, ctx, page = abrir(p, "/programa-pontos", claro=True, viewport=(1440, 900))
        try:
            after_click(page, 7000)
            limpar_tela(page)
            COMANDOS[alvo](page)
        finally:
            ctx.close()
            browser.close()


if __name__ == "__main__":
    main()
