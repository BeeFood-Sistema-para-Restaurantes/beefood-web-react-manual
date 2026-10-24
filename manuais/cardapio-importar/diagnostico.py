"""Diagnóstico do sandbox antes de capturar o #130 — importação de cardápio.

A regra da seção 6 da memória geral: diagnosticar o estado pela API antes de planejar imagem.
Aqui interessa saber três coisas, porque o dono limpou o ambiente para esta produção:

* quantos produtos o cardápio tem (precisa estar em zero, para a importação do iFood aparecer
  criando o cardápio inteiro, e não somando a 400 produtos antigos);
* quantas importações do iFood estão no histórico (zero mostra o estado vazio da tela, que é a
  primeira imagem do manual);
* quais filiais existem, porque o modal do iFood pede o **cardápio destino** e só preenche
  sozinho quando há uma filial só.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "painel-entregador"))

from playwright.sync_api import sync_playwright
from beefood import abrir, api_get, sessao

with sync_playwright() as p:
    browser, ctx, page = abrir(p, "/copiar-ifood", viewport=(1440, 900), escala=1)
    s = sessao(page)
    print("empresaID:", s["empresaID"], "| filialID da sessão:", s["filialID"], "| usuarioID:", s["usuarioID"])

    print("\nqtdProdutos:", api_get(page, f"/api/produto2/cardapio/qtdProdutos/{s['empresaID']}/{s['usuarioID']}"))

    st, importacoes = api_get(page, f"/api/produto2/cardapio/copiariFood/{s['empresaID']}/{s['usuarioID']}")
    if isinstance(importacoes, dict):
        lista = importacoes.get("dados") or importacoes.get("importacoes") or importacoes
        print("importações do iFood:", st, type(lista).__name__,
              len(lista) if isinstance(lista, list) else lista)
    else:
        print("importações do iFood:", st, importacoes)

    print("\ntexto da tela:\n", page.locator("body").inner_text()[:700])

    filiais = page.evaluate("() => localStorage.getItem('beefood_filiais') || ''")
    print("\nfiliais no localStorage:", filiais[:600])
    browser.close()
