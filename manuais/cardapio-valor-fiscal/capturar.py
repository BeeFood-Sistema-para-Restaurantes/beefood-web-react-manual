"""Captura o campo **Valor fiscal** do cadastro de produto e de complemento (#133).

O campo (`vendaFiscal` na API) mora em **Cardápio → Produtos → produto → aba Produto →
Opções avançadas**, e o mesmo campo existe no cadastro de complemento e na **Edição em
Lote**. Ele só aparece para empresa com fiscal ativo em alguma filial
(`empresaTemFiscalAtivo`, em `src/lib/fiscalAutomatico.ts`).

O exemplo do manual é um combo real do sandbox, com os dois brindes que o campo veio
resolver:

    Combo Tasty Bacon ............ R$ 60,00 de venda  → valor fiscal R$ 42,00
    Batata Frita Especial One ..... brinde (R$ 0,00)  → valor fiscal R$  8,00
    Sprite 350ml .................. brinde (R$ 0,00)  → valor fiscal R$ 10,00
                                                        soma ....... R$ 60,00

Tudo é escrito pela própria tela (o `SALVAR E SAIR` do cadastro e o `PROCESSAR` do lote),
nunca por SQL. O `estado` mostra o que está gravado agora e o `limpar` devolve os cinco
itens tocados para vazio, que é como o sandbox estava.

Comandos:

    python3 capturar.py estado      # o que está gravado em cada item do exemplo
    python3 capturar.py capturar    # grava o exemplo, fotografa as sete telas
    python3 capturar.py capturar produto complemento   # repete só parte
    python3 capturar.py limpar      # devolve todos os valores fiscais para vazio

Trava de segurança: só a sandbox 38311/39202.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "painel-entregador"))

from playwright.sync_api import sync_playwright
from beefood import abrir, after_click, api_get, limpar_tela, sessao

AQUI = Path(__file__).resolve().parent
PURAS = AQUI / "imagens-puras"
PURAS.mkdir(parents=True, exist_ok=True)
ANTES = Path("/tmp/valor-fiscal-antes.json")

EMPRESA_PERMITIDA = 38311
FILIAL_PERMITIDA = 39202
PAINEL = "https://beefood.app"

# O combo do exemplo e os dois brindes dele.
COMBO = {"id": 2698512, "nome": "Combo Tasty Bacon", "fiscal": "4200"}
BATATA = {"id": 2698513, "nome": "Batata Frita Especial One", "fiscal": "800"}
SPRITE = {"id": 2698520, "nome": "Sprite 350ml", "fiscal": "1000"}
# Dois produtos quaisquer para a imagem do lote (nomes únicos na base).
LOTE = [{"id": 2698555, "nome": "Combo One Burger"}, {"id": 2698556, "nome": "Combo One Cheddar"}]
LOTE_BUSCA = "Combo One "
LOTE_FISCAL = "3000"

TOCADOS = [COMBO, BATATA, SPRITE] + LOTE


# ----------------------------------------------------------------- utilidades


def travar(page):
    s = sessao(page)
    if s["empresaID"] != EMPRESA_PERMITIDA or s["filialID"] != FILIAL_PERMITIDA:
        raise SystemExit(f"recusado: sessão em {s['empresaID']}/{s['filialID']}, não é o sandbox")
    return s


def valor_fiscal(page, s, produto_id: int):
    """`vendaFiscal` como os detalhes do produto devolvem (a listagem não traz o campo)."""
    st, d = api_get(page, f"/api/produto2/cardapio/produto/{s['empresaID']}/{s['usuarioID']}/{produto_id}")
    if st != 200 or not isinstance(d, dict):
        return f"erro {st}"
    return d.get("vendaFiscal")


def foto(page, nome: str):
    destino = PURAS / nome
    page.screenshot(path=str(destino), type="png")
    print("  FOTO", destino.name, destino.stat().st_size)


def caixa(page, rotulo: str, alvo):
    """Caixa do elemento em fração 0..1 da imagem, que é o que o annotate.py usa."""
    loc = alvo if hasattr(alvo, "bounding_box") else page.locator(alvo).first
    if not loc.count():
        print(f"  CAIXA {rotulo}: não encontrada")
        return
    b = loc.bounding_box()
    if not b:
        print(f"  CAIXA {rotulo}: sem caixa")
        return
    v = page.viewport_size
    print(
        f"  CAIXA {rotulo}: centro ({(b['x'] + b['width'] / 2) / v['width']:.3f}, "
        f"{(b['y'] + b['height'] / 2) / v['height']:.3f})  "
        f"x {b['x'] / v['width']:.3f}..{(b['x'] + b['width']) / v['width']:.3f}  "
        f"y {b['y'] / v['height']:.3f}..{(b['y'] + b['height']) / v['height']:.3f}"
    )


def ir_para(page, aba: str):
    page.goto(f"{PAINEL}/cardapio?tab={aba}", wait_until="domcontentloaded")
    after_click(page, 7000)
    limpar_tela(page)


def abrir_item(page, nome: str):
    """O cartão do cardápio abre o cadastro no clique do próprio nome."""
    titulo = page.get_by_text(nome, exact=False).first
    titulo.scroll_into_view_if_needed()
    page.wait_for_timeout(600)
    titulo.click()
    after_click(page, 4000)
    return page.locator('[role="dialog"]').last


def campo_fiscal(dlg):
    return dlg.locator("label:has-text('Valor fiscal')").first.locator("xpath=following::input[1]")


def abrir_avancadas(page, dlg):
    """O <details> nasce fechado: sem este clique o campo não existe na tela."""
    s = dlg.locator("summary").first
    if "Opções avançadas" not in s.inner_text():
        raise RuntimeError("primeiro <details> não é o Opções avançadas")
    if not dlg.locator("details[open]").count():
        s.click()
        after_click(page, 1800)
    return s


def escrever_fiscal(page, dlg, centavos: str):
    inp = campo_fiscal(dlg)
    inp.scroll_into_view_if_needed()
    page.wait_for_timeout(800)
    inp.click()
    inp.press("Control+a")
    inp.press("Delete")
    if centavos:
        inp.type(centavos, delay=110)
    after_click(page, 1500)
    print("  campo:", repr(inp.input_value()))
    return inp


def salvar(page, dlg):
    dlg.get_by_role("button", name="SALVAR E SAIR").first.click()
    after_click(page, 6000)


# -------------------------------------------------------------------- etapas


def cap_lista(page):
    """01 — a tela Cardápio na aba Produtos, com o combo do exemplo."""
    ir_para(page, "produtos")
    caixa(page, "aba Produtos", '[role="tab"]:has-text("Produtos"), button:has-text("Produtos")')
    caixa(page, "cartao do combo", page.get_by_text(COMBO["nome"], exact=False).first)
    caixa(page, "botao Editar em Lote", 'button:has-text("Editar em Lote")')
    foto(page, "01-cardapio-produtos.png")


def cap_produto(page):
    """02 e 03 — o cadastro do produto: onde o bloco mora e o campo preenchido."""
    ir_para(page, "produtos")
    dlg = abrir_item(page, COMBO["nome"])
    caixa(page, "preco de venda", dlg.locator("label:has-text('Preço de Venda')").first
          .locator("xpath=following::input[1]"))
    caixa(page, "summary Opcoes avancadas", dlg.locator("summary").first)
    foto(page, "02-produto-opcoes-avancadas.png")

    abrir_avancadas(page, dlg)
    inp = escrever_fiscal(page, dlg, COMBO["fiscal"])
    caixa(page, "campo Valor fiscal", inp)
    caixa(page, "texto de apoio", dlg.locator("text=Valor usado na emissão da nota fiscal").first)
    caixa(page, "botao salvar", dlg.get_by_role("button", name="SALVAR E SAIR").first)
    foto(page, "03-produto-valor-fiscal.png")
    salvar(page, dlg)


def cap_complemento(page):
    """04 — o mesmo campo no cadastro do complemento que sai de brinde."""
    ir_para(page, "complementos")
    dlg = abrir_item(page, BATATA["nome"])
    abrir_avancadas(page, dlg)
    inp = escrever_fiscal(page, dlg, BATATA["fiscal"])
    # O "Preço de Venda" fica fora do quadro quando o bloco abre; o que prova o brinde na
    # mesma foto são os dois preços vazios do quadro Delivery/Presencial.
    caixa(page, "precos vazios", dlg.locator("label:has-text('Delivery')").first
          .locator("xpath=following::input[1]"))
    caixa(page, "campo Valor fiscal", inp)
    caixa(page, "botao salvar", dlg.get_by_role("button", name="SALVAR E SAIR").first)
    foto(page, "04-complemento-valor-fiscal.png")
    salvar(page, dlg)

    # O refrigerante fecha a conta do exemplo, mas não precisa de foto: é a mesma tela.
    dlg = abrir_item(page, SPRITE["nome"])
    abrir_avancadas(page, dlg)
    escrever_fiscal(page, dlg, SPRITE["fiscal"])
    salvar(page, dlg)


def cap_lote(page):
    """05, 06 e 07 — Editar em Lote: seleção, campo marcado e resultado."""
    ir_para(page, "produtos")
    page.get_by_role("button", name="Editar em Lote").first.click()
    after_click(page, 3000)
    dlg = page.locator('[role="dialog"]').last

    # A etapa 1 abre com **todos** marcados: o "Marcar Todos" é alterna-tudo e serve para
    # zerar a seleção. Depois, cada linha liga no clique do próprio nome.
    if "0 de" not in dlg.inner_text():
        dlg.get_by_text("Marcar Todos", exact=False).first.click()
        after_click(page, 1500)
    dlg.locator('input[placeholder*="Buscar"]').first.fill(LOTE_BUSCA)
    after_click(page, 2500)
    for item in LOTE:
        dlg.get_by_text(item["nome"], exact=True).first.click()
        page.wait_for_timeout(800)
    after_click(page, 1200)
    print("  selecionados:", [l for l in dlg.inner_text().split("\n") if "selecionado" in l])
    caixa(page, "busca", dlg.locator('input[placeholder*="Buscar"]').first)
    caixa(page, "contador", dlg.get_by_text("selecionados", exact=False).first)
    caixa(page, "botao proximo", dlg.get_by_role("button", name="PRÓXIMO").first)
    foto(page, "05-lote-selecao.png")

    dlg.get_by_role("button", name="PRÓXIMO").first.click()
    after_click(page, 3000)
    dlg = page.locator('[role="dialog"]').last
    # O rótulo do FieldGroup não tem `htmlFor`: clicar no texto não marca nada, e o campo
    # só é desenhado depois que a caixinha liga.
    rotulo = dlg.locator("label:has-text('Valor fiscal')").first
    caixa(page, "linha Valor fiscal", rotulo)
    rotulo.locator("xpath=preceding::button[@role='checkbox'][1]").click()
    after_click(page, 1500)
    inp = campo_fiscal(dlg)
    inp.click()
    inp.type(LOTE_FISCAL, delay=110)
    after_click(page, 1200)
    print("  campo do lote:", repr(inp.input_value()))
    caixa(page, "campo do lote", inp)
    caixa(page, "texto de apoio", dlg.locator("text=Deixe vazio para limpar").first)
    caixa(page, "botao processar", dlg.get_by_role("button", name="PROCESSAR").first)
    foto(page, "06-lote-valor-fiscal.png")

    dlg.get_by_role("button", name="PROCESSAR").first.click()
    after_click(page, 9000)
    dlg = page.locator('[role="dialog"]').last
    print("  etapa 3:", dlg.inner_text()[:300].replace("\n", " | "))
    foto(page, "07-lote-resultado.png")


ETAPAS = {
    "lista": cap_lista,
    "produto": cap_produto,
    "complemento": cap_complemento,
    "lote": cap_lote,
}


# ------------------------------------------------------------------ comandos


def cmd_estado(page):
    s = travar(page)
    agora = {}
    for item in TOCADOS:
        v = valor_fiscal(page, s, item["id"])
        agora[str(item["id"])] = v
        print(f"  {item['id']} {item['nome']:<30} vendaFiscal = {v!r}")
    if not ANTES.exists():
        ANTES.write_text(json.dumps(agora, indent=2, ensure_ascii=False), encoding="utf-8")
        print("  guardado o estado de partida em", ANTES)


def cmd_capturar(page, pedidas):
    travar(page)
    cmd_estado(page)
    for nome in pedidas or list(ETAPAS):
        print(f"== {nome}")
        ETAPAS[nome](page)
    print("== conferência")
    cmd_estado(page)


def cmd_limpar(page):
    s = travar(page)
    for item in TOCADOS:
        aba = "complementos" if item in (BATATA, SPRITE) else "produtos"
        ir_para(page, aba)
        dlg = abrir_item(page, item["nome"])
        abrir_avancadas(page, dlg)
        escrever_fiscal(page, dlg, "")
        salvar(page, dlg)
        print(f"  {item['nome']}: vendaFiscal = {valor_fiscal(page, s, item['id'])!r}")


def main():
    argv = sys.argv[1:] or ["estado"]
    comando, resto = argv[0], argv[1:]
    with sync_playwright() as p:
        browser, ctx, page = abrir(p, "/cardapio?tab=produtos")
        after_click(page, 4000)
        limpar_tela(page)
        if comando == "estado":
            cmd_estado(page)
        elif comando == "capturar":
            cmd_capturar(page, [r for r in resto if r in ETAPAS])
        elif comando == "limpar":
            cmd_limpar(page)
        else:
            raise SystemExit(f"comando desconhecido: {comando}")
        browser.close()


if __name__ == "__main__":
    main()
