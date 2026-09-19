"""Sessão autenticada no BeeFood de produção, compartilhada pelos scripts do #104.

Login com Playwright, token lido do localStorage (XOR + base64, chave
`bf2024_secure_key_token` — ver `src/lib/api.ts`) e chamadas à API pelo próprio
contexto da página, para herdar a origem e o CORS do app.

Uso:
    from beefood import abrir, api_get, api_post, sessao
"""
from __future__ import annotations

import json
from pathlib import Path

LOGIN_EMAIL = "contato@beefood.com.br"
LOGIN_SENHA = "1q2w3e4r"
API = "https://app3.beetechapi.be"
APP = "https://beefood.app"
STATE = Path("/tmp/beefood3-storage.json")
WAIT = 5000

# Mesma chave do front (src/lib/api.ts)
CHAVE_TOKEN = "bf2024_secure_key_token"


def after_click(page, extra_ms: int = WAIT):
    """Espera o spinner sumir e só então conta os 5 s da regra do projeto."""
    for _ in range(40):
        busy = (
            page.locator("text=Carregando...").count()
            or page.locator("text=Atualizando...").count()
            or page.locator("text=Calculando").count()
        )
        if not busy:
            break
        page.wait_for_timeout(1000)
    page.wait_for_timeout(extra_ms)


def limpar_tela(page):
    """Esconde widget de suporte, fecha NPS e banner promocional."""
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
    b = page.locator('button[aria-label="Dispensar"]')
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
    page.goto(f"{APP}/login", wait_until="domcontentloaded")
    after_click(page, 2500)
    if "login" in page.url.lower():
        page.fill("input#emailOrWhatsapp", LOGIN_EMAIL)
        page.fill("input#password", LOGIN_SENHA)
        page.locator("button", has_text="ENTRAR").first.click()
        after_click(page, 9000)


def sessao(page) -> dict:
    """empresaID / filialID / usuarioID / funcionarioID / token já decifrado."""
    return page.evaluate(
        """(chave) => {
          const atobSafe = (s) => { try { return atob(s); } catch (e) { return ''; } };
          const bruto = localStorage.getItem('beefood_auth_token') || '';
          const cifrado = atobSafe(bruto);
          let token = '';
          for (let i = 0; i < cifrado.length; i++) {
            token += String.fromCharCode(
              cifrado.charCodeAt(i) ^ chave.charCodeAt(i % chave.length)
            );
          }
          let s = {};
          try { s = JSON.parse(localStorage.getItem('beefood_user_session') || '{}'); } catch (e) {}
          return {
            empresaID: s.empresaID ?? null,
            filialID: s.filialID ?? null,
            usuarioID: s.usuarioID ?? null,
            funcionarioID: s.funcionarioID ?? null,
            usuario: s.usuario ?? s.nome ?? '',
            token: token || bruto,
          };
        }""",
        CHAVE_TOKEN,
    )


def headers(page) -> dict:
    return {
        "Authorization": f"Bearer {sessao(page)['token']}",
        "Content-Type": "application/json",
    }


def api_get(page, caminho: str):
    """GET na API autenticada. `caminho` começa com /api/..."""
    resp = page.request.get(f"{API}{caminho}", headers=headers(page))
    corpo = resp.text()
    try:
        return resp.status, json.loads(corpo)
    except Exception:
        return resp.status, corpo


def api_post(page, caminho: str, corpo: dict):
    resp = page.request.post(f"{API}{caminho}", headers=headers(page), data=json.dumps(corpo))
    texto = resp.text()
    try:
        return resp.status, json.loads(texto)
    except Exception:
        return resp.status, texto


def abrir(p, rota: str = "/delivery", claro: bool = True, viewport=(1440, 900), escala=1.5):
    """Abre o navegador já logado na rota pedida. Devolve (browser, context, page)."""
    import os

    browser = p.chromium.launch(
        env={**os.environ, "LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"},
    )
    ctx = browser.new_context(
        viewport={"width": viewport[0], "height": viewport[1]},
        device_scale_factor=escala,
        locale="pt-BR",
        timezone_id="America/Sao_Paulo",
        storage_state=str(STATE) if STATE.exists() else None,
    )
    page = ctx.new_page()
    login(page)
    page.goto(f"{APP}{rota}", wait_until="domcontentloaded")
    after_click(page, 8000)
    limpar_tela(page)
    if claro:
        tema_claro(page)
        after_click(page, 1500)
    ctx.storage_state(path=str(STATE))
    return browser, ctx, page
