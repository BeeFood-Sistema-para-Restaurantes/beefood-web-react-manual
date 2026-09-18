#!/usr/bin/env python3
"""As telas deste carrossel, capturadas com UM exemplo montado no sandbox.

Os manuais #64 (`cardapio-digital-desconto-formas`) e #82 (`formas-recebimento`)
ja tem prints desta novidade, e eles foram lidos — e nao colados. Print de manual
vem com o estado e o ruido de que o manual precisava (a sacola dele tem o aviso
de cashback e o de cupom ocupando o terco de cima da tela) e com o exemplo dele
(5% em tudo, porque manual mostra um caminho). O carrossel precisa dos tres
eixos da novidade na mesma peca: desconto **e** acrescimo, em **%** e em **R$**.

Por isso o exemplo aqui e o da propria novidade, cadastrado antes de fotografar:

    PIX Online ........... 5% de desconto   (ja estava assim)
    Dinheiro ............. R$ 3,00 de desconto
    Cartao de Credito .... 2% de acrescimo

## Devolver o sandbox como estava

O sandbox e o mesmo em que os manuais capturam. A configuracao encontrada em
2026-09-17 esta em `ORIGINAL`, e o script **restaura** no fim, inclusive quando
a captura falha no meio. Se ele morrer antes disso, o terminal ja imprimiu o
que encontrou — e da para devolver na mao pelo painel.

## O pedido de exemplo

Combo One Burger + batata frita + Coca Cola = **R$ 39,55**, retirada, sem cupom
e sem cashback. Nao finalize o pedido: a captura para no fechamento.

Uso, da raiz do repositorio:
    python3 carrosseis/desconto-forma-pagamento/capturar-telas.py
    python3 carrosseis/desconto-forma-pagamento/capturar-telas.py --so-restaurar
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ / ".cursor/skills/carrossel-novidades/scripts"))

from capturar import sessao, esperar, limpar  # noqa: E402

SAIDA = Path(__file__).resolve().parent / "imagens-puras"
CARDAPIO = "https://menu.beefood.com.br/beefood3"

OPCOES = ("Sem ajuste", "Desconto em %", "Desconto em R$",
          "Acréscimo em %", "Acréscimo em R$")
CAIXA_VALOR = 'input[placeholder$="0,00"]'

# Como o sandbox estava antes deste carrossel (o que os manuais versionam).
ORIGINAL = {
    "Dinheiro": ("Desconto em %", "5,00"),
    "Cartão de Crédito": ("Sem ajuste", ""),
    "Vale - Alelo Refeição / Visa Vale": ("Acréscimo em %", "5,00"),
}

# O exemplo do carrossel, que e o exemplo da novidade.
EXEMPLO = {
    "Dinheiro": ("Desconto em R$", "3,00"),
    "Cartão de Crédito": ("Acréscimo em %", "2,00"),
    # Fora do exemplo: dois acrescimos diferentes na mesma lista leriam como
    # duas versoes do recurso.
    "Vale - Alelo Refeição / Visa Vale": ("Sem ajuste", ""),
}


# ----------------------------------------------------------------- painel

def abrir_formas(pagina) -> None:
    pagina.goto("https://beefood.app/cardapio-digital",
                wait_until="domcontentloaded", timeout=90000)
    esperar(pagina)
    limpar(pagina)
    pagina.click("button:has-text('Formas Recebimento')")
    esperar(pagina)


def _editor(pagina, forma: str):
    """Abre o editor da forma clicando no nome dela na lista."""
    pagina.locator("h4", has_text=forma).first.click()
    pagina.wait_for_timeout(3000)
    esperar(pagina)
    return pagina.locator('[role="dialog"]').last


def _campo_ajuste(dialogo):
    """O combobox do `Ajuste no pagamento`, achado pelo texto que ele mostra.

    Por indice nao serve: forma com `Vincular à Forma de Pagamento` tem um
    combobox antes, e forma sem vinculo nao tem.
    """
    campos = dialogo.locator('[role="combobox"]')
    for i in range(campos.count()):
        if campos.nth(i).inner_text().strip() in OPCOES:
            return campos.nth(i)
    raise SystemExit("ERRO: não achei o campo Ajuste no pagamento")


def ler_ajuste(pagina, forma: str) -> tuple[str, str]:
    dialogo = _editor(pagina, forma)
    tipo = _campo_ajuste(dialogo).inner_text().strip()
    valor = ""
    caixa = dialogo.locator(CAIXA_VALOR)
    if caixa.count() and caixa.first.is_visible():
        valor = caixa.first.input_value()
    dialogo.locator('button:has-text("CANCELAR")').first.click()
    pagina.wait_for_timeout(1500)
    return tipo, valor


def gravar_ajuste(pagina, forma: str, tipo: str, valor: str) -> None:
    dialogo = _editor(pagina, forma)
    campo = _campo_ajuste(dialogo)
    if campo.inner_text().strip() != tipo:
        campo.click()
        pagina.wait_for_timeout(900)
        pagina.locator('[role="option"]').filter(has_text=tipo).first.click()
        pagina.wait_for_timeout(2500)
    if valor:
        # Trocar o tipo esvazia e **renomeia** o campo: `Percentual (%)` com
        # placeholder `0,00` vira `Valor (R$)` com `R$ 0,00`. Casar pelo fim do
        # placeholder pega os dois.
        caixa = dialogo.locator(CAIXA_VALOR).first
        caixa.fill("")
        caixa.type(valor, delay=60)
        pagina.wait_for_timeout(600)
    dialogo.locator('button:has-text("SALVAR")').first.click()
    pagina.wait_for_timeout(3500)
    esperar(pagina)
    print(f"    {forma}: {tipo} {valor}".rstrip())


def aplicar(pagina, config: dict[str, tuple[str, str]]) -> None:
    for forma, (tipo, valor) in config.items():
        gravar_ajuste(pagina, forma, tipo, valor)


def capturar_painel(pagina) -> None:
    """A lista com um selo em cada forma, e o campo de ajuste com a lista aberta."""
    abrir_formas(pagina)
    pagina.screenshot(path=str(SAIDA / "painel-lista.png"), type="png")
    print("OK  painel-lista.png")

    dialogo = _editor(pagina, "Dinheiro")
    _campo_ajuste(dialogo).click()
    pagina.wait_for_timeout(1200)
    pagina.screenshot(path=str(SAIDA / "painel-ajuste.png"), type="png")
    print("OK  painel-ajuste.png")
    pagina.keyboard.press("Escape")
    pagina.wait_for_timeout(800)
    dialogo.locator('button:has-text("CANCELAR")').first.click()
    pagina.wait_for_timeout(1500)


# --------------------------------------------------------------- cardapio

LIVRE = "input:not([readonly]):not([disabled]):visible"
FONE = "11999990001"
NOME = "Cliente"


def _visivel(pagina, texto: str) -> bool:
    """Se **algum** nó com esse texto está visível.

    Olhar só o primeiro não serve: o cardápio monta a gaveta de formas de
    pagamento escondida no topo do DOM, então `.first` resolve para um nó
    invisível e a tela certa passa batida. Foi o que travou o laço numa rodada.
    """
    alvo = pagina.get_by_text(texto, exact=False)
    return any(alvo.nth(i).is_visible() for i in range(min(alvo.count(), 6)))


def _continuar(pagina) -> None:
    pagina.locator("button:has-text('Continuar')").last.click()
    pagina.wait_for_timeout(6500)


def montar_sacola(pagina) -> None:
    """Abre o cardapio, fecha a barra de cupom e poe o pedido de exemplo."""
    pagina.goto(CARDAPIO, wait_until="domcontentloaded", timeout=90000)
    pagina.wait_for_timeout(9000)

    # A barra verde "Você tem 8 cupons!" fica sobre o cabecalho e entra em toda
    # captura de topo. O botao dela e o unico dentro de `.promo-banner`.
    fechar = pagina.locator(".promo-banner button")
    if fechar.count():
        fechar.first.click()
        pagina.wait_for_timeout(1200)

    pagina.get_by_text("Combo One Burger", exact=True).first.click()
    pagina.wait_for_timeout(4500)
    dialogo = pagina.locator('[role="dialog"]').last
    # Dois grupos obrigatorios: acompanhamento e bebida.
    dialogo.get_by_text("Batata frita", exact=True).first.click()
    pagina.wait_for_timeout(1000)
    dialogo.get_by_text("Coca Cola 350ml", exact=True).first.click()
    pagina.wait_for_timeout(1200)
    dialogo.locator("button").filter(has_text="Adicionar R$").first.click()
    pagina.wait_for_timeout(5000)
    upsell = pagina.locator("button:has-text('CONTINUAR SEM ADICIONAR')")
    if upsell.count():
        upsell.first.click()
        pagina.wait_for_timeout(3000)


def ir_ate_o_pagamento(pagina) -> None:
    """Avanca o fechamento olhando a tela, e nao seguindo uma ordem fixa.

    A ordem muda: cliente que ja existe no sandbox pula o cadastro, e a tela de
    modo de entrega so aparece se a loja tem delivery e retirada. Sequencia
    fixa quebrou duas vezes antes deste laco existir.
    """
    pagina.locator(".cart-btn").first.click()
    pagina.wait_for_timeout(6000)
    _continuar(pagina)

    for volta in range(14):
        # `Finalizar` só existe no último passo, e é o sinal mais limpo de que
        # a tela de formas de pagamento está na frente.
        if pagina.locator("button:has-text('Finalizar')").count():
            print(f"    fechamento: pagamento na volta {volta}")
            return
        if _visivel(pagina, "número do WhatsApp"):
            passo = "whatsapp"
            pagina.locator(LIVRE).first.fill(FONE)
            pagina.wait_for_timeout(1500)
        elif _visivel(pagina, "Informações pessoais"):
            # O campo do telefone chega desabilitado aqui; o primeiro habilitado
            # e o nome.
            passo = "cadastro"
            livres = pagina.locator(LIVRE)
            if not livres.first.input_value().strip():
                livres.first.fill(NOME)
                pagina.wait_for_timeout(1200)
        elif _visivel(pagina, "Retirar no estabelecimento"):
            # Retirada em vez de entrega: sem endereco, sem taxa, e o ajuste
            # incide sobre o subtotal dos produtos de qualquer jeito.
            passo = "modo de entrega"
            pagina.get_by_text("Retirar no estabelecimento").first.click()
            pagina.wait_for_timeout(2500)
        else:
            passo = "tela não reconhecida"
        print(f"    fechamento: volta {volta} — {passo}")
        if not pagina.locator("button:has-text('Continuar')").count():
            raise SystemExit("ERRO: o fechamento parou numa tela sem Continuar")
        _continuar(pagina)
    raise SystemExit("ERRO: o fechamento não chegou nas formas de pagamento")


def abrir_gaveta(pagina) -> None:
    pagina.get_by_text("Outras formas de pagamento").first.click()
    pagina.wait_for_timeout(4000)


def escolher_forma(pagina, forma: str) -> None:
    """Toca numa forma da gaveta, o que seleciona e fecha a gaveta.

    Não tente fechar a gaveta pelo Escape para abri-la de novo: ela fica meio
    aberta e os seus próprios selos passam a interceptar o clique. Escolher uma
    forma é o jeito de sair dela.

    O `Dinheiro` ainda abre o `Troco para quanto?`, que deixa um véu sobre a
    página — sem dispensar, a próxima abertura da gaveta não acontece.
    """
    pagina.get_by_text(forma, exact=True).first.click()
    pagina.wait_for_timeout(5000)
    # `count()` não serve de teste aqui: o cardápio deixa o diálogo de troco
    # montado e escondido, então ele é contado mesmo quando não está na frente.
    troco = pagina.locator("button:has-text('NÃO QUERO TROCO')")
    if troco.count() and troco.first.is_visible():
        troco.first.click()
        pagina.wait_for_timeout(4000)


def capturar_resumo(pagina, nome: str) -> None:
    """Fotografa o cartão `Resumo de valores` como elemento.

    Elemento em vez de página: o recorte sai na borda do componente, sem conta
    de pixel, e sem o cartão de cupom que fica logo acima.
    """
    cartao = pagina.locator(".v-card").filter(has_text="Resumo de valores").last
    cartao.screenshot(path=str(SAIDA / nome), type="png")
    print(f"OK  {nome}")


def capturar_cardapio(pagina) -> None:
    """A lista de formas com os selos, e o mesmo pedido em duas formas."""
    montar_sacola(pagina)
    ir_ate_o_pagamento(pagina)

    abrir_gaveta(pagina)
    pagina.screenshot(path=str(SAIDA / "formas-lista.png"), type="png")
    print("OK  formas-lista.png")

    escolher_forma(pagina, "Dinheiro")
    capturar_resumo(pagina, "total-dinheiro.png")

    abrir_gaveta(pagina)
    escolher_forma(pagina, "Cartão de Crédito")
    capturar_resumo(pagina, "total-credito.png")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--so-restaurar", action="store_true",
                    help="devolve o sandbox ao estado de ORIGINAL e sai")
    ap.add_argument("--so-painel", action="store_true",
                    help="captura só as telas do painel")
    ap.add_argument("--so-cardapio", action="store_true",
                    help="captura só as telas do cardápio do cliente")
    args = ap.parse_args()

    SAIDA.mkdir(parents=True, exist_ok=True)

    if args.so_restaurar:
        with sessao("painel") as pagina:
            abrir_formas(pagina)
            print("--> restaurando")
            aplicar(pagina, ORIGINAL)
        return 0

    try:
        with sessao("painel") as pagina:
            abrir_formas(pagina)
            print("--> como encontrei o sandbox")
            for forma in ORIGINAL:
                print(f"    {forma}: {ler_ajuste(pagina, forma)}")
            print("--> montando o exemplo do carrossel")
            aplicar(pagina, EXEMPLO)
            if not args.so_cardapio:
                capturar_painel(pagina)

        if not args.so_painel:
            # O manual avisa que a mudança do painel leva **até 1 minuto** para
            # chegar no cardápio do cliente. Capturar antes disso fotografa a
            # configuração antiga, e o erro é silencioso: a tela sai certa, com
            # os números errados.
            print("--> esperando o cardápio receber a mudança (75 s)")
            time.sleep(75)
            with sessao("celular", publico=True) as pagina:
                capturar_cardapio(pagina)
    finally:
        # Sessao propria: o `sessao` abre o seu proprio Playwright e nao aceita
        # aninhamento, entao a devolucao nao cabe dentro do bloco de captura.
        with sessao("painel") as pagina:
            abrir_formas(pagina)
            print("--> devolvendo o sandbox")
            aplicar(pagina, ORIGINAL)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
