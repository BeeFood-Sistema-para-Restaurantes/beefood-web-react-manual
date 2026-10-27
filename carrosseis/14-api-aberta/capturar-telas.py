"""Captura as três telas reais da peça 14.

A peça é quase toda desenhada, porque o resultado da API Aberta acontece dentro
do sistema do outro. Sobraram três telas nossas, e cada uma prova uma coisa que
desenho nenhum provaria:

1. **as permissões**, na folha *Aplicativos → API Aberta*. É o slide 5, e o
   recorte começa em *Permissões* de propósito: acima dele ficam o Client ID e o
   campo do Client Secret, e **o repositório é público** — a loja de exemplo roda
   em produção, então credencial dela não entra em imagem versionada. O quadro
   fecha em *Avaliações*, a última área liberada: *Entregadores* e *Estoque*
   aparecem apagados, com a etiqueta **Em breve**, e promessa não é assunto de
   peça de lançamento (a #13 descartou as mesmas duas linhas pelo mesmo motivo);

2. **o exemplo pronto**, no portal `docs.beefood.app`. É o slide 6, e a largura
   da janela decide o que ele prova. O portal vira **duas colunas** a partir de
   1280 px, e aí o exemplo cai numa coluna de 230 px com cinco linguagens
   visíveis — em 1920 px continuam cinco, porque o limite é a coluna e não a
   janela. Abaixo de 1280 o layout empilha e o cartão ocupa **900 px**, com doze
   das treze linguagens na barra. Foi assim que a captura ficou em **1260 px**:
   é o último degrau antes de o portal se partir em duas colunas, e é o que põe
   o código numa caixa que cabe nos 904 px do slide sem ampliar nada.

3. **o cartão da API Aberta** na grade de *Aplicativos*. É a arte do CTA, pelo
   mesmo motivo da #13: o último slide manda abrir *Aplicativos → API Aberta*, e
   o cartão é a porta — o leitor vê na arte exatamente o que vai encontrar
   quando chegar lá.

Nada aqui escreve. O único clique que muda estado é o que abre a folha lateral.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from PIL import Image

sys.path.append(".cursor/skills/carrossel/scripts")
from capturar import esperar, limpar, sessao  # noqa: E402

AQUI = Path(__file__).resolve().parent
PURAS = AQUI / "imagens-puras"
PURAS.mkdir(exist_ok=True)

MEDIDAS: dict[str, dict] = {}

DOCS = "https://docs.beefood.app/docs/oauth/emitir-tokens"
DESCRICAO = "Integre seu sistema ao BeeFood via API REST"


def recortar(pagina, nome: str, de, ate=None, folga=14, lateral=None,
             folga_pe=None, folga_lado=None, pagina_inteira=False):
    """Recorta pela caixa medida no DOM, nunca estimada na miniatura.

    `pagina_inteira` existe por um defeito silencioso: `clip` sem `full_page`
    recorta **dentro da janela**, e o que passa da borda de baixo some sem erro
    nenhum. O bloco de exemplo do portal começa a 1135 px de rolagem e tem 414
    de altura; numa janela de 1300 o arquivo saiu com 164, só o cabeçalho, e o
    script seguiu dizendo RECORTE 414.
    """
    a = de.bounding_box()
    b = (ate or de).bounding_box()
    topo = max(0, a["y"] - folga)
    if lateral is None:
        x, largura = 0, pagina.viewport_size["width"]
    else:
        esq, dir_ = lateral if isinstance(lateral, tuple) else (lateral, lateral)
        lado = folga if folga_lado is None else folga_lado
        f_esq, f_dir = lado if isinstance(lado, tuple) else (lado, lado)
        c, d = esq.bounding_box(), dir_.bounding_box()
        x = max(0, c["x"] - f_esq)
        largura = (d["x"] + d["width"] + f_dir) - x
    pe = folga if folga_pe is None else folga_pe
    caixa = {"x": x, "y": topo, "width": largura,
             "height": b["y"] + b["height"] + pe - topo}
    pagina.screenshot(path=str(PURAS / nome), clip=caixa,
                      full_page=pagina_inteira)
    MEDIDAS[nome] = caixa
    largura, altura = Image.open(PURAS / nome).size
    escala = 2
    if (round(largura / escala), round(altura / escala)) != (
            round(caixa["width"]), round(caixa["height"])):
        raise SystemExit(
            f"ERRO: {nome} saiu {largura}x{altura} para uma caixa de "
            f"{round(caixa['width'])}x{round(caixa['height'])} em escala "
            f"{escala} — o recorte passou da borda da janela.")
    print("RECORTE", nome, {k: round(v) for k, v in caixa.items()})


def salvar_medidas():
    if not MEDIDAS:
        return
    arq = AQUI / "medidas.json"
    antigo = json.loads(arq.read_text()) if arq.is_file() else {}
    antigo.update({k: {c: round(v, 1) for c, v in cx.items()}
                   for k, cx in MEDIDAS.items()})
    arq.write_text(json.dumps(antigo, indent=2, ensure_ascii=False) + "\n")
    print("medidas.json:", len(antigo), "recortes")


def cartao():
    """O cartão da API Aberta na grade de *Aplicativos*, sem abrir a folha.

    O cartão é um `Card` comum — não tem classe própria como o do MCP, que o
    painel enfeita com a borda arco-íris. A âncora é a descrição, que é única
    na página, e dela se sobe até o `rounded-lg` do cartão.
    """
    with sessao("painel") as pagina:
        pagina.emulate_media(reduced_motion="reduce")
        pagina.goto("https://beefood.app/aplicativos",
                    wait_until="domcontentloaded", timeout=90000)
        esperar(pagina)
        limpar(pagina)
        quadro = pagina.get_by_text(DESCRICAO, exact=False).first.locator(
            "xpath=ancestor::div[contains(@class,'rounded-lg')][1]")
        if not quadro.count():
            raise SystemExit("ERRO: não achei o cartão da API Aberta na grade")
        quadro.scroll_into_view_if_needed()
        pagina.wait_for_timeout(1200)
        recortar(pagina, "rec-cartao-api.png", quadro, lateral=quadro, folga=12)
        salvar_medidas()


def permissoes():
    """A grade de Consultar/Alterar da folha *Aplicativos → API Aberta*."""
    with sessao("painel") as pagina:
        pagina.emulate_media(reduced_motion="reduce")
        pagina.goto("https://beefood.app/aplicativos",
                    wait_until="domcontentloaded", timeout=90000)
        esperar(pagina)
        limpar(pagina)
        pagina.get_by_text(DESCRICAO, exact=False).first.click()
        pagina.wait_for_timeout(9000)
        esperar(pagina)

        titulo = pagina.get_by_text("Permissões", exact=True).first
        # A última área liberada. `Avaliações` aparece também no texto de
        # resumo das credenciais adicionais, mais abaixo; `.first` pega a da
        # grade, que é a que está em cima na ordem do documento.
        ultima = pagina.get_by_text("Avaliações dos clientes", exact=True).first.locator(
            "xpath=ancestor::div[contains(@class,'rounded-2xl')][1]")
        if not ultima.count():
            raise SystemExit("ERRO: não achei o cartão de Avaliações na folha")
        recortar(pagina, "rec-permissoes.png", titulo, ultima,
                 lateral=ultima, folga=6, folga_lado=(2, 2), folga_pe=4)
        salvar_medidas()


def exemplo():
    """A barra de linguagens e o exemplo de requisição, no portal.

    Roda fora da `sessao()` porque o portal não é o painel: não tem login nem o
    spinner do painel, e a largura da janela é escolhida aqui (ver o cabeçalho
    do arquivo).
    """
    import re

    from playwright.sync_api import sync_playwright

    idiomas_re = re.compile(r"^(Node|Shell|Python|PHP|C#|Java|Go|Ruby|Kotlin|"
                            r"Swift|Rust|Dart|HTTP)$")

    with sync_playwright() as p:
        navegador = p.chromium.launch(args=["--no-sandbox"])
        contexto = navegador.new_context(locale="pt-BR", device_scale_factor=2,
                                         viewport={"width": 1260, "height": 1300})
        pagina = contexto.new_page()
        pagina.goto(DOCS, wait_until="networkidle", timeout=90000)
        pagina.wait_for_timeout(4000)
        pagina.evaluate("() => document.fonts.ready")
        # O botão flutuante da BeeFood IA pousa em cima da linha `Requisição`.
        pagina.add_style_tag(content=".agent-trigger { display: none !important; }")

        abas = pagina.locator("button, a").filter(has_text=idiomas_re)
        print("linguagens visíveis na barra:", abas.count(), "de 13")
        if abas.count() < 12:
            raise SystemExit("ERRO: a barra encolheu; confira a largura da janela")

        idiomas = pagina.get_by_text("Linguagem", exact=True).first
        codigo = pagina.get_by_text("POST /v1/oauth/token", exact=True).first.locator(
            "xpath=ancestor::div[contains(@class,'rounded')][1]")
        recortar(pagina, "rec-exemplo.png", idiomas, codigo,
                 lateral=codigo, folga=14, folga_lado=(0, 0), folga_pe=0,
                 pagina_inteira=True)
        salvar_medidas()
        navegador.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("alvos", nargs="*", default=[])
    alvos = ap.parse_args().alvos or ["cartao", "permissoes", "exemplo"]
    if "cartao" in alvos:
        cartao()
    if "permissoes" in alvos:
        permissoes()
    if "exemplo" in alvos:
        exemplo()


if __name__ == "__main__":
    main()
