#!/usr/bin/env python3
"""Captura #102 — Cardápio em PDF (produção, sandbox BeeFood3 / empresa 38311).

  python capturar.py                      # tudo
  python capturar.py menu acoes etapa1    # só algumas etapas
  DRY=1 python capturar.py pdf            # não baixa o arquivo

O gerador só aparece para empresas liberadas em `cardapioPdfAcesso.ts`
(38311 em produção). Depois de cada clique: espera o spinner sair e mais 5 s
(regra da MEMORIA-GERAL); a prévia do PDF é desenhada em canvas pelo pdf.js e
demora, por isso as esperas dela são maiores.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

DIR = Path(__file__).resolve().parent
PURA = DIR / "imagens-puras"
PURA.mkdir(exist_ok=True)
STATE = Path("/tmp/bf3-auth.json")
PDF_BAIXADO = Path("/tmp/cardapio-pdf-manual.pdf")
WAIT = 5000
PREVIA = 14000
LOGIN_EMAIL = "contato@beefood.com.br"
LOGIN_SENHA = "1q2w3e4r"
DRY = os.environ.get("DRY") == "1"


def after_click(page, extra_ms: int = WAIT):
    for _ in range(30):
        ocupado = (
            page.locator("text=Carregando...").count()
            or page.locator("text=Atualizando...").count()
            or page.locator("text=Montando a prévia...").count()
        )
        if not ocupado:
            break
        page.wait_for_timeout(1000)
    page.wait_for_timeout(extra_ms)


def limpar(page):
    page.add_style_tag(content="div.fixed.bottom-6 { display:none !important }")
    nps = page.locator('[role="dialog"]').filter(has_text="Como está sendo sua experiência")
    if nps.count():
        botao = nps.last.get_by_role("button", name="FECHAR")
        if botao.count():
            try:
                botao.click(timeout=1500)
                after_click(page)
            except Exception:
                pass
    dispensar = page.locator('button[aria-label="Dispensar"]')
    if dispensar.count():
        try:
            dispensar.first.click(timeout=1200)
            after_click(page)
        except Exception:
            pass


def tema_claro(page):
    classes = page.locator("html").get_attribute("class") or ""
    if "dark" in classes:
        alvo = page.locator('span.sr-only:has-text("Alterar tema")')
        if alvo.count():
            alvo.first.locator("xpath=ancestor::button").first.click()
            page.wait_for_timeout(800)


def login(page, contexto):
    page.goto("https://beefood.app/", wait_until="domcontentloaded")
    after_click(page)
    if page.locator("input#emailOrWhatsapp").count():
        page.fill("input#emailOrWhatsapp", LOGIN_EMAIL)
        page.fill("input#password", LOGIN_SENHA)
        page.get_by_role("button", name="ENTRAR").click()
        after_click(page, 9000)
        contexto.storage_state(path=str(STATE))
    tema_claro(page)
    limpar(page)


def shot(page, nome: str):
    destino = PURA / nome
    page.screenshot(path=str(destino), type="png")
    print("SHOT", destino.name, destino.stat().st_size)


def caixa(page, rotulo: str, seletor, indice: int = 0):
    """Imprime a caixa do elemento já na escala da imagem (device_scale 1.5).

    É daqui que saem as coordenadas de `annotate.py` — medir na tela evita
    chutar pixels olhando o PNG reduzido.
    """
    loc = seletor if hasattr(seletor, "nth") else page.locator(seletor)
    if not loc.count():
        print(f"  CAIXA {rotulo}: NÃO ENCONTRADA")
        return
    b = loc.nth(indice).bounding_box()
    if not b:
        print(f"  CAIXA {rotulo}: sem caixa")
        return
    f = 1.5
    print(
        f"  CAIXA {rotulo}: ({round(b['x'] * f)}, {round(b['y'] * f)}, "
        f"{round((b['x'] + b['width']) * f)}, {round((b['y'] + b['height']) * f)})"
    )


def abrir_cardapio(page):
    page.goto("https://beefood.app/cardapio?tab=produtos", wait_until="domcontentloaded")
    after_click(page, 8000)
    limpar(page)


def abrir_editor(page):
    """Abre a página cheia do gerador (menu Cardápio → Cardápio em PDF)."""
    page.goto("https://beefood.app/cardapio-pdf", wait_until="domcontentloaded")
    after_click(page, 12000)
    limpar(page)
    print("titulo:", page.locator("h1").first.inner_text())
    esperar_previa(page)


def esperar_previa(page, tentativas: int = 12):
    """A prévia é gerada em canvas; espera aparecer a imagem da primeira página."""
    for i in range(tentativas):
        if page.locator('img[alt="Página 1 do cardápio"]').count():
            page.wait_for_timeout(2500)
            print("  prévia pronta")
            return
        page.wait_for_timeout(3000)
    print("  prévia NÃO ficou pronta")


def etapa(page, numero: int):
    page.get_by_role("button", name=f"{numero}.").first.click()
    after_click(page, 3000)


# ---------------------------------------------------------------- caminhos


def cap_menu(page):
    """Menu lateral Cardápio, com o item Cardápio em PDF."""
    abrir_cardapio(page)
    itens = page.locator('a:has-text("Cardápio em PDF")')
    print("itens de menu Cardápio em PDF:", itens.count())
    if itens.count():
        itens.first.scroll_into_view_if_needed()
        page.wait_for_timeout(600)
    caixa(page, "item Cardapio em PDF", 'a:has-text("Cardápio em PDF")')
    caixa(page, "botao mais opcoes", page.locator("button").filter(has=page.locator("svg.lucide-ellipsis-vertical")))
    shot(page, "01-menu-cardapio-pdf.png")


def cap_acoes(page):
    """Atalho Gerar cardápio em PDF no menu de ações da tela Cardápio."""
    abrir_cardapio(page)
    gatilho = page.locator("button").filter(has=page.locator("svg.lucide-ellipsis-vertical"))
    if not gatilho.count():
        gatilho = page.get_by_role("button", name="Mais opções")
    gatilho.first.click()
    after_click(page, 2500)
    print(page.locator('[role="menu"]').last.inner_text()[:400].replace("\n", " | "))
    caixa(page, "item gerar pdf", '[role="menuitem"]:has-text("Gerar cardápio em PDF")')
    caixa(page, "menu inteiro", '[role="menu"]')
    shot(page, "02-acoes-gerar-pdf.png")
    page.keyboard.press("Escape")
    page.wait_for_timeout(800)


# ---------------------------------------------------------------- etapa 1


def cap_etapa1(page):
    abrir_editor(page)
    print("=== ETAPA 1 ===")
    caixa(page, "bloco cardapios", 'div:has(> div > label:has-text("CARDÁPIOS NO IMPRESSO"))')
    caixa(page, "chip cardapio", 'button:has-text("BeeFood3 - Manual")', 1)
    caixa(page, "select preco", page.get_by_role("combobox"))
    caixa(page, "switch descricao", "#mostrar-descricao")
    caixa(page, "busca", 'input[placeholder="Buscar produto..."]')
    caixa(page, "secao bebidas", 'button:has-text("Bebidas")', 0)
    caixa(page, "linha vinculo", 'button:has-text("Vínculo Marketplace")')
    caixa(page, "etapas", 'button:has-text("1. Cardápios e itens")')
    caixa(page, "previa", 'img[alt="Página 1 do cardápio"]')
    caixa(page, "avancar", 'button:has-text("AVANÇAR")')
    shot(page, "03-etapa1-cardapios-itens.png")


def cap_etapa1_secao(page):
    """Abre uma seção para mostrar os itens editáveis."""
    abrir_editor(page)
    alvo = page.get_by_role("button", name="Bebidas", exact=False)
    print("candidatos Bebidas:", alvo.count())
    for i in range(alvo.count()):
        texto = alvo.nth(i).inner_text()
        if "/" in texto:  # o botão da seção mostra "visíveis/total"
            alvo.nth(i).click()
            break
    after_click(page, 3500)
    linha = page.locator('input[value="Coca Cola 350ml"]').first
    caixa(page, "input nome", linha)
    caixa(page, "input descricao", 'input[value="Coca Cola Lata 350ml"]')
    caixa(page, "input preco", 'input[type="number"]')
    caixa(page, "checkbox item", '[role="checkbox"]', 3)
    caixa(page, "alca arrastar", "div.cursor-grab", 0)
    caixa(page, "titulo bebidas", 'button:has-text("Bebidas")', 0)
    shot(page, "04-etapa1-itens-editaveis.png")


# ---------------------------------------------------------------- etapa 2


def cap_etapa2_modelo(page):
    abrir_editor(page)
    etapa(page, 2)
    combo = page.get_by_role("combobox").first
    combo.click()
    after_click(page, 2000)
    print(page.locator('[role="listbox"]').last.inner_text()[:600].replace("\n", " | "))
    caixa(page, "listbox", '[role="listbox"]')
    for nome in ("Clássico", "Elegante", "Fotográfico", "Compacto", "Quadro"):
        caixa(page, f"opcao {nome}", f'[role="option"]:has-text("{nome}")')
    shot(page, "05-etapa2-modelos.png")
    page.keyboard.press("Escape")
    page.wait_for_timeout(800)


def cap_etapa2_layout(page):
    abrir_editor(page)
    etapa(page, 2)
    print("=== ETAPA 2 ===")
    caixa(page, "modelo", page.get_by_role("combobox"), 0)
    caixa(page, "tamanho", page.get_by_role("combobox"), 1)
    caixa(page, "orientacao", page.get_by_role("combobox"), 2)
    caixa(page, "colunas", page.get_by_role("combobox"), 3)
    caixa(page, "espacamento", page.get_by_role("combobox"), 4)
    caixa(page, "texto", page.get_by_role("combobox"), 5)
    caixa(page, "switch fotos", "#mostrar-fotos")
    caixa(page, "tamanhos foto", 'button:has-text("Média")')
    caixa(page, "formato foto", 'button:has-text("Arredondada")')
    shot(page, "06-etapa2-pagina-fotos.png")


def cap_etapa2_mostrar(page):
    """Rola até o bloco O que mostrar."""
    abrir_editor(page)
    etapa(page, 2)
    alvo = page.get_by_text("Repetir os dados da loja no topo das páginas", exact=True)
    alvo.first.evaluate("el => el.scrollIntoView({block:'center'})")
    page.wait_for_timeout(1500)
    for campo in ("paginaPorSetor", "mostrarDescricao", "mostrarPreco", "mostrarSimboloMoeda",
                  "nomeMaiusculo", "mostrarCabecalho", "mostrarNumeroPagina"):
        caixa(page, f"switch {campo}", f"#{campo}")
    shot(page, "07-etapa2-o-que-mostrar.png")


# ---------------------------------------------------------------- etapa 3


def cap_etapa3_marca(page):
    abrir_editor(page)
    etapa(page, 3)
    print("=== ETAPA 3 ===")
    caixa(page, "campo nome", page.locator("input").nth(0))
    caixa(page, "campo telefone", page.locator("input").nth(1))
    caixa(page, "campo endereco", page.locator("input").nth(2))
    caixa(page, "campo redes", 'input[placeholder="@seurestaurante"]')
    caixa(page, "bloco logo", 'div:has(> label:has-text("LOGO DO RESTAURANTE"))')
    caixa(page, "botao usar logo", 'button:has-text("Usar a logo da loja")')
    caixa(page, "campo qr", 'input[value*="presencial.beefood"]')
    caixa(page, "paletas", 'button:has-text("Papel")')
    caixa(page, "cor destaque", 'input[type="color"]', 2)
    caixa(page, "previa qr", 'img[alt="Página 1 do cardápio"]')
    shot(page, "08-etapa3-marca.png")


def cap_etapa3_capa(page):
    abrir_editor(page)
    etapa(page, 3)
    alvo = page.get_by_text("Modelo da capa", exact=True)
    alvo.first.evaluate("el => el.scrollIntoView({block:'center'})")
    page.wait_for_timeout(1500)
    caixa(page, "switch capa", "#capa-ativa")
    caixa(page, "modelos capa", 'button:has-text("Clássica")')
    caixa(page, "modelo minimalista", 'button:has-text("Minimalista")')
    caixa(page, "titulo capa", 'input[value="Cardápio"]')
    caixa(page, "fonte", 'button:has-text("Sem serifa")')
    caixa(page, "texto extra", "textarea")
    caixa(page, "previa capa", 'img[alt="Página 1 do cardápio"]')
    shot(page, "09-etapa3-capa.png")


# ---------------------------------------------------------------- etapa 4 + PDF


def cap_etapa4(page):
    abrir_editor(page)
    etapa(page, 3)          # passa pela etapa 3 para a capa já sair com o QR Code
    after_click(page, 4000)
    etapa(page, 4)
    after_click(page, 4000)
    print("=== ETAPA 4 ===")
    caixa(page, "resumo", 'div:has-text("cardápio(s) •")', -1)
    caixa(page, "baixar", 'button:has-text("BAIXAR PDF (F2)")', 0)
    caixa(page, "recomecar", 'button:has-text("Recomeçar do zero")')
    caixa(page, "previa", 'img[alt="Página 1 do cardápio"]')
    shot(page, "10-etapa4-revisar-baixar.png")


def baixar(page, destino: Path):
    with page.expect_download(timeout=180000) as info:
        page.get_by_role("button", name="BAIXAR PDF (F2)").first.click()
    info.value.save_as(str(destino))
    print("  PDF salvo:", destino.name, destino.stat().st_size, "bytes")
    after_click(page, 4000)


def cap_pdf(page):
    """Baixa o PDF de verdade em três modelos (viram as imagens do manual).

    Passa pela etapa 3 antes de baixar: é lá que o QR Code do cardápio é
    montado, então uma capa baixada sem abrir a etapa 3 sai sem o quadradinho.
    """
    abrir_editor(page)
    etapa(page, 3)          # monta o QR Code da capa
    after_click(page, 4000)
    etapa(page, 4)
    after_click(page, 4000)
    if DRY:
        print("DRY: paro antes de baixar")
        return

    baixar(page, PDF_BAIXADO)
    shot(page, "11-pdf-baixado.png")

    for modelo, arquivo in (("Fotográfico", "fotografico"), ("Quadro", "quadro")):
        etapa(page, 2)
        combo = page.get_by_role("combobox").first
        combo.click()
        page.wait_for_timeout(1200)
        page.get_by_role("option", name=modelo, exact=False).first.click()
        after_click(page, 3000)
        esperar_previa(page)
        etapa(page, 4)
        after_click(page, 4000)
        print("modelo", modelo)
        baixar(page, Path(f"/tmp/cardapio-{arquivo}.pdf"))


def cap_pdf_sem_fotos(page):
    """Clássico só com texto: é o modelo com a linha pontilhada até o preço."""
    abrir_editor(page)
    etapa(page, 3)
    after_click(page, 4000)
    etapa(page, 2)
    page.get_by_role("switch").filter(has_not_text="x").first.wait_for(state="attached")
    switch = page.locator("#mostrar-fotos")
    switch.scroll_into_view_if_needed()
    switch.click()
    after_click(page, 3000)
    esperar_previa(page)
    shot(page, "12-etapa2-so-texto.png")
    etapa(page, 4)
    after_click(page, 4000)
    if DRY:
        print("DRY: paro antes de baixar")
        return
    baixar(page, Path("/tmp/cardapio-classico-texto.pdf"))


def cap_render(_page=None):
    """Transforma os PDFs baixados nas páginas-fonte das imagens 11 e 12.

    Não usa o navegador: renderiza com PyMuPDF em 110 dpi (o suficiente para a
    página caber na largura do manual sem serrilhar).
    """
    import pymupdf  # dependência só desta etapa

    fontes = {
        "pdf-capa.png": (PDF_BAIXADO, 0),
        "pdf-pagina.png": (PDF_BAIXADO, 1),
        "pdf-modelo-classico.png": (Path("/tmp/cardapio-classico-texto.pdf"), 1),
        "pdf-modelo-fotografico.png": (Path("/tmp/cardapio-fotografico.pdf"), 1),
        "pdf-modelo-quadro.png": (Path("/tmp/cardapio-quadro.pdf"), 1),
    }
    for nome, (arquivo, pagina) in fontes.items():
        if not arquivo.exists():
            print("FALTA", arquivo, "— rode as etapas pdf / pdf_sem_fotos antes")
            continue
        doc = pymupdf.open(arquivo)
        doc[pagina].get_pixmap(dpi=110).save(str(PURA / nome))
        doc.close()
        print("RENDER", nome)


ETAPAS = {
    "menu": cap_menu,
    "acoes": cap_acoes,
    "etapa1": cap_etapa1,
    "etapa1_secao": cap_etapa1_secao,
    "etapa2_modelo": cap_etapa2_modelo,
    "etapa2_layout": cap_etapa2_layout,
    "etapa2_mostrar": cap_etapa2_mostrar,
    "etapa3_marca": cap_etapa3_marca,
    "etapa3_capa": cap_etapa3_capa,
    "etapa4": cap_etapa4,
    "pdf": cap_pdf,
    "pdf_sem_fotos": cap_pdf_sem_fotos,
    "render": cap_render,
}


def main():
    pedidos = sys.argv[1:] or list(ETAPAS)
    if pedidos == ["render"]:  # não precisa de navegador
        cap_render()
        return
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"},
        )
        kwargs = {
            "viewport": {"width": 1440, "height": 900},
            "device_scale_factor": 1.5,
            "locale": "pt-BR",
            "timezone_id": "America/Sao_Paulo",
            "accept_downloads": True,
        }
        if STATE.exists():
            kwargs["storage_state"] = str(STATE)
        contexto = browser.new_context(**kwargs)
        page = contexto.new_page()
        page.on("console", lambda m: print("  [console]", m.type, m.text[:160]) if m.type == "error" else None)
        login(page, contexto)
        for nome in pedidos:
            print("==", nome)
            ETAPAS[nome](page)
        contexto.storage_state(path=str(STATE))
        browser.close()
    print("rode o annotate.py depois de conferir as puras")


if __name__ == "__main__":
    main()
