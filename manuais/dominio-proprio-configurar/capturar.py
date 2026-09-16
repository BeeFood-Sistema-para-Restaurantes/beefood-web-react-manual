#!/usr/bin/env python3
"""Captura #101 — Domínio próprio e subdomínio pela tela (sandbox BeeFood3).

A tela nova (`DominioAutoatendimentoModal`) já está em produção para a empresa do
sandbox (`dominioAcesso.ts` libera a 38311), então tudo é capturado em
`https://beefood.app`.

    python3 capturar.py apex        # 1.1 até a instrução de DNS (cadastra de verdade)
    python3 capturar.py instrucao   # 1.1 recaptura a instrução de DNS inteira
    python3 capturar.py verificar   # 1.1 pede a verificação e espera o No ar
    python3 capturar.py no-ar       # 1.1 final: domínio No ar
    python3 capturar.py dns         # 1.2 aba DNS (cria um registro de verdade)
    python3 capturar.py excluir     # 1.3 exclusão
    python3 capturar.py sub         # 2.1 subdomínio até a instrução de CNAME
    python3 capturar.py sub-no-ar    # 2.1 final: subdomínio No ar

DRY=1 faz o caminho inteiro e para antes do clique que grava.
Depois de cada clique: espera o spinner sumir e só então 5 s.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

DIR = Path(__file__).resolve().parent
PURA = DIR / "imagens-puras"
PURA.mkdir(exist_ok=True)
BASE = os.environ.get("BASE", "https://beefood.app")
STATE = Path("/tmp/bf3-auth.json")
WAIT = 5000
DRY = os.environ.get("DRY") == "1"
DOMINIO_APEX = "cardapioteste.com.br"
DOMINIO_SUB = "cardapio.cardapioteste.com.br"
CARDAPIO = "BeeFood3 - Manual"


def after_click(page, extra_ms: int = WAIT):
    for _ in range(30):
        busy = (
            page.locator("text=Carregando...").count()
            or page.locator("text=Atualizando...").count()
            or page.locator("text=Calculando").count()
        )
        if not busy:
            break
        page.wait_for_timeout(1000)
    page.wait_for_timeout(extra_ms)


def limpar(page):
    page.add_style_tag(content="div.fixed.bottom-6 { display:none !important }")
    for _ in range(2):
        nps = page.locator('[role="dialog"]').filter(has_text="Como está sendo sua experiência")
        if nps.count():
            btn = nps.last.get_by_role("button", name="FECHAR")
            if btn.count():
                try:
                    btn.click(timeout=1500)
                    after_click(page)
                except Exception:
                    pass
        disp = page.locator('button[aria-label="Dispensar"]')
        if disp.count():
            try:
                disp.first.click(timeout=1200)
                after_click(page, 1500)
            except Exception:
                pass


def tema_claro(page):
    cls = page.locator("html").get_attribute("class") or ""
    if "dark" in cls:
        alvo = page.locator('span.sr-only:has-text("Alterar tema")')
        if alvo.count():
            alvo.first.locator("xpath=ancestor::button").first.click()
            page.wait_for_timeout(1000)


def login(page, context):
    page.goto(BASE + "/", wait_until="domcontentloaded")
    after_click(page, 7000)
    if page.locator("input#emailOrWhatsapp").count():
        page.fill("input#emailOrWhatsapp", "contato@beefood.com.br")
        page.fill("input#password", "1q2w3e4r")
        page.get_by_role("button", name="ENTRAR").click()
        after_click(page, 12000)
        context.storage_state(path=str(STATE))
    tema_claro(page)
    limpar(page)


def shot(page, nome):
    page.wait_for_timeout(400)
    page.screenshot(path=str(PURA / nome), type="png")
    print("  shot", nome)


def sheet(page):
    return page.locator('[role="dialog"]').filter(has_text="Use o seu endereço no lugar").last


def abrir_modal(page, foto_card: str | None = None):
    page.goto(BASE + "/aplicativos", wait_until="domcontentloaded")
    after_click(page, 6000)
    limpar(page)
    tema_claro(page)
    card = page.locator("text=Domínio Próprio").first
    card.scroll_into_view_if_needed()
    page.wait_for_timeout(800)
    if foto_card:
        shot(page, foto_card)
    card.click()
    after_click(page, 6000)
    return sheet(page)


def escolher_cardapio(page, s, espera: int = 2500):
    s.get_by_text(CARDAPIO, exact=False).first.click()
    after_click(page, espera)


def escolher_tipo(page, s, apex: bool):
    rotulo = "seurestaurante.com.br" if apex else "cardapio.seurestaurante.com.br"
    s.get_by_text(rotulo, exact=True).first.click()
    after_click(page, 2500)


def digitar_endereco(page, s, valor: str):
    campo = s.locator('input[placeholder*="seurestaurante"]')
    campo.first.click()
    campo.first.fill(valor)
    after_click(page, 7000)


def esperar_instrucao(page, s, limite_s: int = 300) -> bool:
    """A instrução de DNS é preparada no servidor (~1 minuto)."""
    for _ in range(limite_s // 5):
        texto = s.inner_text()
        if "Copiar todos" in texto or "Já configurei" in texto:
            after_click(page, 3000)
            return True
        page.wait_for_timeout(5000)
    return False


# --------------------------------------------------------------------------- #
def cap_apex(page):
    s = abrir_modal(page, "01-aplicativos-dominio.png")
    shot(page, "02-escolher-cardapio.png")
    escolher_cardapio(page, s)
    shot(page, "03-escolher-tipo.png")
    escolher_tipo(page, s, apex=True)
    digitar_endereco(page, s, DOMINIO_APEX)
    print(s.inner_text()[:2000])
    shot(page, "04-endereco-conferido.png")
    if DRY:
        print("DRY: paro antes de CADASTRAR DOMÍNIO")
        return
    s.get_by_role("button", name="CADASTRAR DOMÍNIO").click()
    after_click(page, 8000)
    shot(page, "05-cadastrado-preparando.png")
    if esperar_instrucao(page, s):
        shot(page, "06-instrucao-ns.png")
    print("=== SITUACAO ===")
    print(s.inner_text()[:3000])


def cap_instrucao(page):
    """A instrução de DNS é mais alta que o painel: rola até o botão de verificar."""
    s = abrir_modal(page)
    escolher_cardapio(page, s, 7000)
    alvo = s.get_by_role("button", name="Já configurei, verificar agora")
    alvo.first.scroll_into_view_if_needed()
    after_click(page, 2500)
    print(s.inner_text()[:2500])
    shot(page, "06-instrucao-ns.png")


def cap_verificar(page):
    """Clica em 'Já configurei, verificar agora' e acompanha até o domínio ficar No ar."""
    s = abrir_modal(page)
    escolher_cardapio(page, s, 7000)
    botao = s.get_by_role("button", name="Já configurei, verificar agora")
    if botao.count():
        botao.first.scroll_into_view_if_needed()
        botao.first.click()
        after_click(page, 6000)
        print("verificação pedida")
    for i in range(60):  # a tela se atualiza sozinha (8 s / 30 s)
        texto = s.inner_text()
        estado = "No ar" if "https://cardapioteste.com.br" in texto else "aguardando"
        print(f"  [{i:02d}] {estado}")
        if estado == "No ar":
            after_click(page, 4000)
            print(texto[:2500])
            shot(page, "07-dominio-no-ar.png")
            return
        page.wait_for_timeout(20000)
    print("ainda não subiu; rode de novo mais tarde")
    print(s.inner_text()[:2500])


def cap_no_ar(page):
    s = abrir_modal(page)
    escolher_cardapio(page, s, 7000)
    print(s.inner_text()[:3000])
    shot(page, "07-dominio-no-ar.png")


MX_VALORES = ["1 aspmx.l.google.com", "5 alt1.aspmx.l.google.com"]


def escolher_opcao(page, combo, nome: str):
    """Select do shadcn: abre o gatilho e clica na opção (que vive fora do modal)."""
    combo.click()
    page.wait_for_timeout(700)
    page.get_by_role("option", name=nome, exact=True).first.click()
    page.wait_for_timeout(700)


def cap_dns(page):
    s = abrir_modal(page)
    escolher_cardapio(page, s, 7000)
    s.get_by_role("tab", name="DNS").click()
    after_click(page, 6000)
    print("=== ABA DNS ===")
    print(s.inner_text()[:3000])
    shot(page, "08-aba-dns.png")

    s.get_by_role("button", name="Adicionar registro").click()
    after_click(page, 2500)
    form = page.locator('[role="dialog"]').filter(has_text="Os dados do registro").last
    combos = form.get_by_role("combobox")
    escolher_opcao(page, combos.nth(0), "MX (e-mail)")          # tipo
    campos = form.locator('input[placeholder="10 mx.provedor.com"]')
    campos.first.fill(MX_VALORES[0])
    form.get_by_role("button", name="Adicionar valor").click()
    page.wait_for_timeout(600)
    campos.nth(1).fill(MX_VALORES[1])
    escolher_opcao(page, combos.nth(1), "1 hora")               # ttl
    after_click(page, 1500)
    print("=== FORM DNS ===")
    print(form.inner_text()[:1500])
    shot(page, "09-form-registro.png")
    if DRY:
        print("DRY: paro antes de SALVAR o registro")
        return

    form.get_by_role("button", name="SALVAR (F2)").click()
    page.wait_for_timeout(3000)
    shot(page, "10-registro-criado.png")
    print("=== DEPOIS DE SALVAR ===")
    print(s.inner_text()[:3000])


def cap_dns_editar(page):
    """Altera o TTL do registro MX: é a alteração que faz aparecer o aviso de propagação."""
    s = abrir_modal(page)
    escolher_cardapio(page, s, 7000)
    s.get_by_role("tab", name="DNS").click()
    after_click(page, 6000)
    linha = s.locator("tr", has_text="MX").first
    linha.locator("button").filter(has=page.locator("svg")).nth(-2).click()
    after_click(page, 2500)
    form = page.locator('[role="dialog"]').filter(has_text="Para mudar o nome ou o tipo").last
    print("=== FORM EDICAO ===")
    print(form.inner_text()[:1200])
    escolher_opcao(page, form.get_by_role("combobox").nth(1), "5 minutos")
    if DRY:
        print("DRY: paro antes de SALVAR a alteração")
        return
    form.get_by_role("button", name="SALVAR (F2)").click()
    page.wait_for_timeout(4000)
    shot(page, "11-propagacao.png")
    print("=== DEPOIS DA ALTERACAO ===")
    print(s.inner_text()[:1500])

    hist = s.get_by_role("button", name="Histórico de alterações")
    hist.scroll_into_view_if_needed()
    hist.click()
    after_click(page, 2000)
    linhas = s.locator('button:has-text("Alterou")')
    if linhas.count():
        linhas.first.click()
        after_click(page, 1500)
    cap_historico(page, s)


def cap_historico(page, s):
    """O histórico fica no pé da lista: rola o painel até o fim antes de fotografar."""
    ultima = s.locator('button:has-text("Criou")').last
    if ultima.count():
        ultima.scroll_into_view_if_needed()
    for _ in range(6):
        page.mouse.wheel(0, 600)
        page.wait_for_timeout(300)
    page.wait_for_timeout(1200)
    shot(page, "12-historico-dns.png")
    print(s.inner_text()[-1200:])


def cap_dns_hist(page):
    """Só o histórico: abre a aba DNS, expande e rola até o fim."""
    s = abrir_modal(page)
    escolher_cardapio(page, s, 7000)
    s.get_by_role("tab", name="DNS").click()
    after_click(page, 6000)
    hist = s.get_by_role("button", name="Histórico de alterações")
    hist.scroll_into_view_if_needed()
    hist.click()
    after_click(page, 2000)
    for rot in ("Alterou", "Criou"):
        linha = s.locator(f'button:has-text("{rot}")').first
        if linha.count():
            linha.click()
            after_click(page, 1200)
    cap_historico(page, s)


def cap_excluir(page):
    s = abrir_modal(page)
    escolher_cardapio(page, s, 7000)
    s.get_by_role("button", name="Excluir domínio").click()
    after_click(page, 2500)
    shot(page, "14-confirmar-exclusao.png")
    if DRY:
        print("DRY: paro antes de confirmar a exclusão")
        return
    page.get_by_role("button", name="Excluir (ENTER)").click()
    after_click(page, 8000)
    shot(page, "15-apos-exclusao.png")


def cap_pos_exclusao(page):
    """A exclusão roda em segundo plano: espera o cartão voltar a ficar livre."""
    s = abrir_modal(page)
    for i in range(30):
        texto = s.inner_text()
        print(f"  [{i:02d}]", "removendo" if "Removendo" in texto else "livre")
        if "Removendo" not in texto:
            break
        page.wait_for_timeout(15000)
        page.reload(wait_until="domcontentloaded")
        after_click(page, 6000)
        limpar(page)
        s = abrir_modal(page)
    removidos = s.get_by_role("button", name="Domínios removidos anteriormente")
    if removidos.count():
        removidos.first.click()
        after_click(page, 2000)
    print(s.inner_text()[:1500])
    shot(page, "15-apos-exclusao.png")


def cap_sub(page):
    s = abrir_modal(page)
    escolher_cardapio(page, s)
    escolher_tipo(page, s, apex=False)
    digitar_endereco(page, s, DOMINIO_SUB)
    print(s.inner_text()[:2000])
    shot(page, "16-subdominio-conferido.png")
    if DRY:
        print("DRY: paro antes de CADASTRAR DOMÍNIO")
        return
    s.get_by_role("button", name="CADASTRAR DOMÍNIO").click()
    after_click(page, 8000)
    if esperar_instrucao(page, s):
        shot(page, "17-instrucao-cname.png")
    print("=== SITUACAO ===")
    print(s.inner_text()[:3000])


def cap_sub_no_ar(page):
    s = abrir_modal(page)
    escolher_cardapio(page, s, 7000)
    print(s.inner_text()[:3000])
    shot(page, "18-subdominio-no-ar.png")


ETAPAS = {
    "apex": cap_apex,
    "instrucao": cap_instrucao,
    "verificar": cap_verificar,
    "no-ar": cap_no_ar,
    "dns": cap_dns,
    "dns-editar": cap_dns_editar,
    "dns-hist": cap_dns_hist,
    "excluir": cap_excluir,
    "pos-exclusao": cap_pos_exclusao,
    "sub": cap_sub,
    "sub-no-ar": cap_sub_no_ar,
}


def main():
    pedidos = sys.argv[1:] or ["apex"]
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True,
                              env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"})
        args = dict(viewport={"width": 1440, "height": 900}, device_scale_factor=1.5,
                    locale="pt-BR", timezone_id="America/Sao_Paulo")
        if STATE.exists():
            args["storage_state"] = str(STATE)
        ctx = b.new_context(**args)
        pg = ctx.new_page()
        login(pg, ctx)
        for nome in pedidos:
            print("==>", nome, "(DRY)" if DRY else "")
            ETAPAS[nome](pg)
        ctx.storage_state(path=str(STATE))
        b.close()


if __name__ == "__main__":
    main()
