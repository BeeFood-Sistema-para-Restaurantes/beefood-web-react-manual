"""Captura #78 Classificação RFV — sandbox BeeFood3.

Rodar na pasta do manual:
  python capturar.py diag        # só imprime a API (sem print)
  python capturar.py             # diagnóstico + todas as capturas
  python capturar.py lista       # uma etapa

Regra permanente: spinner some, depois 5 s, só então screenshot.
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter
from pathlib import Path

from playwright.sync_api import sync_playwright

DIR = Path(__file__).resolve().parent
PURA = DIR / "imagens-puras"
PURA.mkdir(exist_ok=True)
STATE = Path("/tmp/beefood3-storage.json")

LOGIN_EMAIL = "contato@beefood.com.br"
LOGIN_SENHA = "1q2w3e4r"
WAIT = 5000
API = "https://app3.beetechapi.be"


def after_click(page, extra_ms: int = WAIT):
    for _ in range(40):
        busy = (
            page.locator("text=Carregando...").count()
            or page.locator("text=Atualizando...").count()
            or page.locator("text=Calculando").count()
            or page.locator("text=Carregando parâmetros").count()
        )
        if not busy:
            break
        page.wait_for_timeout(1000)
    page.wait_for_timeout(extra_ms)


def limpar_tela(page):
    page.add_style_tag(
        content="""
        div.fixed.bottom-6 { display:none !important }
        div.fixed.bottom-4.right-4 { display:none !important }
        """
    )
    nps = page.locator('[role="dialog"]').filter(has_text="Como está sendo sua experiência")
    if nps.count():
        try:
            nps.locator("button").filter(has_text="FECHAR").first.click(timeout=1500)
            page.wait_for_timeout(400)
        except Exception:
            pass
    for sel in ('button[aria-label="Dispensar"]',):
        b = page.locator(sel)
        if b.count():
            try:
                b.first.click(timeout=1200)
                page.wait_for_timeout(300)
            except Exception:
                pass


def tema_claro(page):
    cls = page.locator("html").get_attribute("class") or ""
    if "dark" in cls:
        alvo = page.locator('span.sr-only:has-text("Alterar tema")')
        if alvo.count():
            alvo.first.locator("xpath=ancestor::button").first.click()
            page.wait_for_timeout(800)


def login(page):
    page.goto("https://beefood.app/login", wait_until="domcontentloaded")
    after_click(page, 2500)
    if "login" in page.url.lower():
        page.fill("input#emailOrWhatsapp", LOGIN_EMAIL)
        page.fill("input#password", LOGIN_SENHA)
        page.locator("button", has_text="ENTRAR").first.click()
        after_click(page, 9000)


def sessao(page):
    """empresaID / usuarioID / token da sessão já autenticada."""
    return page.evaluate(
        """() => {
          const raw = localStorage.getItem('beefood_user_session')
            || localStorage.getItem('userData')
            || localStorage.getItem('user');
          let data = {};
          try { data = raw ? JSON.parse(raw) : {}; } catch (e) { data = {}; }
          const inner = data.user || data.usuarioLogado || data;
          const token = localStorage.getItem('beefood_auth_token')
            || localStorage.getItem('token')
            || (data && (data.token || data.accessToken))
            || '';
          return {
            empresaID: inner.empresaID || inner.empresaId || data.empresaID || null,
            usuarioID: inner.usuarioID || inner.usuarioId || data.usuarioID || null,
            usuario: inner.usuario || inner.nome || data.usuario || '',
            token,
            keys: Object.keys(localStorage),
          };
        }"""
    )


def auth_headers(page):
    s = sessao(page)
    headers = {"ngrok-skip-browser-warning": "true"}
    if s.get("token"):
        headers["Authorization"] = f"Bearer {s['token']}"
    return s, headers


def tirar(page, nome: str, full: bool = False):
    limpar_tela(page)
    page.screenshot(path=str(PURA / nome), type="png", full_page=full)
    print("   ->", nome, PURA / nome)


def abrir_clientes(page):
    page.goto("https://beefood.app/clientes", wait_until="domcontentloaded")
    after_click(page, 8000)
    limpar_tela(page)
    tema_claro(page)
    after_click(page, 2000)


def diagnosticar(page):
    abrir_clientes(page)
    s, headers = auth_headers(page)
    print("SESSAO", json.dumps({k: s[k] for k in s if k != "token"}, ensure_ascii=False))
    print("TOKEN_LEN", len(s.get("token") or ""))
    emp, usr = s.get("empresaID"), s.get("usuarioID")

    if emp and usr:
        url = f"{API}/api/cliente2/rfvParametro/{emp}/{usr}"
        try:
            resp = page.request.get(url, headers=headers)
            print("RFV_PARAM", resp.status, url)
            print(resp.text()[:4000])
        except Exception as e:
            print("RFV_PARAM ERRO", e)

        url_cad = f"{API}/datasnap/rest/cliente2/cadastro/{emp}/{usr}/0/1"
        try:
            resp = page.request.get(url_cad, headers=headers)
            print("CADASTRO", resp.status, url_cad)
            corpo = resp.json()
            # Datasnap às vezes envolve em result
            lista = corpo
            if isinstance(corpo, dict):
                lista = corpo.get("result") or corpo.get("clientes") or corpo.get("data") or []
                if isinstance(lista, list) and lista and isinstance(lista[0], list):
                    lista = lista[0]
            if not isinstance(lista, list):
                print("CADASTRO_TIPO", type(corpo), str(corpo)[:400])
                lista = []
            print("CADASTRO_N", len(lista))
            cont = Counter()
            notas = {"recencia": [], "frequencia": [], "valorMonetario": []}
            for c in lista:
                if not isinstance(c, dict):
                    continue
                cont[c.get("classificacao") or "(sem)"] += 1
                for k in notas:
                    v = c.get(k)
                    if v is not None:
                        notas[k].append(v)
            print("CLASSIFICACOES", json.dumps(dict(cont.most_common()), ensure_ascii=False, indent=2))
            for k, vals in notas.items():
                print(k, "n", len(vals), "min", min(vals) if vals else None, "max", max(vals) if vals else None)
        except Exception as e:
            print("CADASTRO ERRO", e)

        url_campos = f"{API}/api/cliente2/segmentacao/campos/{emp}/{usr}"
        try:
            resp = page.request.get(url_campos, headers=headers)
            print("CAMPOS_SEG", resp.status)
            j = resp.json()
            grupos = j.get("grupos") or j.get("campos") or []
            if isinstance(grupos, dict):
                print("CAMPOS_KEYS", list(grupos.keys())[:20])
            else:
                rfv = [
                    c
                    for c in (grupos if isinstance(grupos, list) else [])
                    if isinstance(c, dict)
                    and (
                        (c.get("grupo") or "").upper() == "RFV"
                        or "rfv" in (c.get("label") or "").lower()
                        or "classificacao" in (c.get("chave") or "")
                    )
                ]
                print("RFV_CAMPOS", json.dumps(rfv, ensure_ascii=False, indent=2)[:2500])
        except Exception as e:
            print("CAMPOS_SEG ERRO", e)

    print("TELA", page.inner_text("body")[:1800])


def cap_menu(page):
    page.goto("https://beefood.app/", wait_until="domcontentloaded")
    after_click(page, 4000)
    limpar_tela(page)
    tema_claro(page)
    after_click(page, 2000)
    tirar(page, "01-menu-clientes.png")


def clicar_chip(page, nome: str):
    candidatos = [nome, nome.replace("éis", "eis").replace("é", "e")]
    chip = None
    for cand in candidatos:
        loc = page.locator("button").filter(has_text=cand)
        if loc.count():
            chip = loc
            break
    if chip is None:
        raise RuntimeError(f"chip RFV não encontrado: {nome}")
    chip.first.click()
    after_click(page, 3000)


def cap_lista(page):
    abrir_clientes(page)
    # Fiéis deixa a lista curta e com o emoji da classificação na linha
    clicar_chip(page, "Fiéis")
    tirar(page, "02-lista-rfv-chips.png")


def cap_parametros(page):
    abrir_clientes(page)
    page.locator("button", has_text="RFV").first.click()
    after_click(page, 5000)
    page.wait_for_selector("text=Editar Parâmetros RFV", timeout=20000)
    after_click(page, 2000)
    tirar(page, "03-parametros-rfv.png")
    page.keyboard.press("Escape")
    page.wait_for_timeout(600)


def cap_ajuda(page):
    abrir_clientes(page)
    grupo = page.locator("div").filter(has=page.locator("button", has_text="RFV")).filter(
        has=page.locator("button").nth(1)
    )
    # o botão de ajuda é o irmão do botão RFV
    btn_rfv = page.locator("button", has_text="RFV").first
    ajuda = btn_rfv.locator("xpath=following-sibling::button")
    if ajuda.count():
        ajuda.first.click()
    else:
        page.locator("button").filter(has=page.locator("svg")).nth(0).click()
    after_click(page, 3000)
    page.wait_for_selector("text=Classificação RFV", timeout=15000)
    page.set_viewport_size({"width": 1440, "height": 1400})
    page.add_style_tag(
        content="""
        [role=dialog] { max-height: none !important; }
        [data-radix-scroll-area-viewport] { max-height: none !important; height: auto !important; }
        """
    )
    after_click(page, 2500)
    tirar(page, "04-classificacoes.png")
    page.set_viewport_size({"width": 1440, "height": 900})
    page.keyboard.press("Escape")
    page.wait_for_timeout(600)


def cap_ficha(page):
    abrir_clientes(page)
    clicar_chip(page, "Fiéis")
    rows = page.locator("table tbody tr")
    if rows.count() == 0:
        raise RuntimeError("lista de clientes vazia")
    rows.first.click()
    after_click(page, 4000)
    tab = page.locator("button, [role=tab]").filter(has_text="Indicadores")
    if tab.count():
        tab.first.click()
        after_click(page, 3000)
    else:
        print("   aviso: aba Indicadores não encontrada")
        after_click(page, 2000)
    tirar(page, "05-ficha-indicadores.png")
    page.keyboard.press("Escape")
    page.wait_for_timeout(600)


def cap_seg(page):
    page.goto("https://beefood.app/food-marketing/segmentacao-cliente", wait_until="domcontentloaded")
    after_click(page, 6000)
    limpar_tela(page)
    tema_claro(page)
    after_click(page, 2000)
    page.locator("button", has_text="Nova segmentação").first.click()
    after_click(page, 4000)
    # o seletor de campo abre sozinho; expandir a categoria RFV
    rfv = page.get_by_text("RFV", exact=True)
    if rfv.count():
        rfv.first.click()
        after_click(page, 2000)
    else:
        # fallback: buscar pelo rótulo do filtro
        busca = page.get_by_placeholder("Buscar")
        if busca.count():
            busca.first.fill("classifica")
            after_click(page, 2000)
    tirar(page, "06-segmentacao-rfv.png")
    page.keyboard.press("Escape")
    page.wait_for_timeout(400)
    page.keyboard.press("Escape")
    page.wait_for_timeout(400)


def cap_inteligente(page):
    page.goto(
        "https://beefood.app/food-marketing/campanhas-whatsapp?tab=automacao",
        wait_until="domcontentloaded",
    )
    after_click(page, 7000)
    limpar_tela(page)
    tema_claro(page)
    after_click(page, 2000)
    # Recuperador usa origem SEGMENTACAO — mostra o campo Segmentação
    alvo = page.get_by_text("Recuperador de vendas")
    if not alvo.count():
        alvo = page.get_by_text("Cashback parado")
    if not alvo.count():
        alvo = page.get_by_text("Aniversário")
    if not alvo.count():
        raise RuntimeError("nenhuma campanha inteligente por segmentação visível")
    alvo.first.click()
    after_click(page, 4000)
    # garantir que o passo 1 está aberto
    if page.get_by_text("Segmentação").count() == 0:
        passo = page.get_by_text("Identificação")
        if passo.count():
            passo.first.click()
            after_click(page, 2000)
    tirar(page, "07-campanha-inteligente-segmentacao.png")
    page.keyboard.press("Escape")
    page.wait_for_timeout(600)


ETAPAS = {
    "menu": cap_menu,
    "lista": cap_lista,
    "parametros": cap_parametros,
    "ajuda": cap_ajuda,
    "ficha": cap_ficha,
    "seg": cap_seg,
    "inteligente": cap_inteligente,
}


def main():
    pedidos = sys.argv[1:] or ["diag", *ETAPAS]
    with sync_playwright() as p:
        browser = p.chromium.launch(
            env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"}
        )
        args = dict(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=1.5,
            locale="pt-BR",
            timezone_id="America/Sao_Paulo",
        )
        if STATE.exists():
            args["storage_state"] = str(STATE)
        ctx = browser.new_context(**args)
        page = ctx.new_page()
        login(page)
        tema_claro(page)
        if "diag" in pedidos:
            print("== diag")
            diagnosticar(page)
            pedidos = [x for x in pedidos if x != "diag"]
        for nome in pedidos:
            if nome not in ETAPAS:
                print("etapa desconhecida:", nome)
                continue
            print("==", nome)
            ETAPAS[nome](page)
        ctx.storage_state(path=str(STATE))
        browser.close()


if __name__ == "__main__":
    main()
