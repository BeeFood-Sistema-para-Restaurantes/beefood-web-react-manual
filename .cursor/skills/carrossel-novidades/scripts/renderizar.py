#!/usr/bin/env python3
"""Transforma os slides HTML de um carrossel em PNG no tamanho exato do Instagram.

O contrato é o mesmo do open-carrusel: o slide é um **fragmento de body**
(sem `<html>`, `<head>` ou `<!DOCTYPE>`). Este script embrulha o fragmento num
documento completo com as @font-face da Mulish e o `base.css` da skill, abre no
Chromium num viewport do tamanho exato do formato e fotografa.

Por que embrulhar em vez de deixar cada slide ser um HTML inteiro: a pré-visualização
e o PNG final passam pelo mesmo embrulho, então o que você revisa é o que sai.
Mudar a fonte ou a margem em um lugar muda em todos os carrosséis.

Uso:
    python renderizar.py carrosseis/<slug>                  # todos os slides
    python renderizar.py carrosseis/<slug> --formato 1:1
    python renderizar.py carrosseis/<slug>/slides/03-como.html
    python renderizar.py carrosseis/<slug> --guias          # marca a zona segura
    python renderizar.py carrosseis/<slug> --contato        # folha de contato

Entrada : <pasta>/slides/*.html   (ordem alfabética — nomeie 01-, 02-, ...)
Saída   : <pasta>/png/*.png       (+ <pasta>/folha-de-contato.png com --contato)

## Duas formas de apontar para uma imagem

- **relativa**, como em qualquer HTML: `../imagens-puras/05-cadastro.png`. É o
  print que só existe naquele carrossel.
- **`skill:`**, que este script troca pelo caminho de `assets/` da skill:
  `skill:fotos/foto-batata.png`. É a biblioteca compartilhada — foto de produto,
  banner do totem, tela de espera. Assim um modelo de `assets/slides/` abre em
  qualquer pasta, e dois carrosséis usam a mesma foto sem copiar arquivo.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
MARCA = json.loads((SKILL / "assets" / "marca.json").read_text(encoding="utf-8"))
BASE_CSS = SKILL / "assets" / "slides" / "base.css"
FONTES = SKILL / "assets" / "fontes"
# Duas artes oficiais da marca, uma por tipo de fundo: a de fundo claro tem
# "BEE" em preto, a de fundo escuro tem "BEE" em branco e um contorno branco no
# selo. Nunca derive uma da outra por filtro — o selo não é o negativo dele
# mesmo (a asa continua branca e a cabeça continua preta nas duas).
LOGO_CLARO = SKILL / "assets" / MARCA["logo_fundo_claro"]
LOGO_ESCURO = SKILL / "assets" / MARCA["logo_fundo_escuro"]

MAX_SLIDES = MARCA["max_slides"]


def face_das_fontes() -> str:
    """@font-face apontando para os .ttf da skill.

    Fonte embutida em vez de Google Fonts: o render fica igual com ou sem rede,
    e não depende de a página carregar a tempo do screenshot.
    """
    regras = []
    for peso in MARCA["fontes"]["pesos"]:
        ttf = FONTES / f"Mulish-{peso}.ttf"
        if not ttf.is_file():
            sys.exit(f"ERRO: fonte ausente: {ttf}")
        regras.append(
            "@font-face{font-family:'Mulish';font-style:normal;"
            f"font-weight:{peso};src:url('{ttf.as_uri()}') format('truetype');}}"
        )
    return "".join(regras)


MARCA_GUIA = """
.zona-segura::before, .zona-segura::after {
  content: "";
  position: absolute;
  background: rgba(239, 66, 57, 0.16);
  border: 2px dashed rgba(239, 66, 57, 0.75);
}
"""

# No feed (4:5 e 1:1) o Instagram não cobre a imagem com barra nenhuma — o que
# ele desenha por cima é o **contador do carrossel**, no canto superior direito.
# No story (9:16) a conta é outra: o perfil no topo e a barra de resposta na base
# comem faixas largas.
GUIAS_FEED = MARCA_GUIA + """
.zona-segura::before { top: 0; right: 0; width: 200px; height: 110px; }
.zona-segura::after { display: none; }
"""

GUIAS_STORY = MARCA_GUIA + """
.zona-segura::before { top: 0; left: 0; right: 0; height: 250px; }
.zona-segura::after { bottom: 0; left: 0; right: 0; height: 250px; }
"""


ASSETS = SKILL / "assets"


def resolver_skill(fragmento: str) -> str:
    """Troca `skill:` pelo caminho de `assets/` da skill.

    `src="skill:fotos/foto-batata.png"` vira um `file://` absoluto. Existe para a
    biblioteca compartilhada: sem isso, ou cada carrossel copia as fotos de
    produto para dentro dele, ou os modelos de `assets/slides/` só abrem quando
    estão dentro de um carrossel que tenha os arquivos com o nome certo.
    """
    return fragmento.replace("skill:", f"{ASSETS.as_uri()}/")


def documento(fragmento: str, largura: int, altura: int, pasta: Path,
              guias: bool, formato: str) -> str:
    """Embrulha o fragmento. `pasta` vira o <base> para as imagens relativas."""
    fragmento = resolver_skill(fragmento)
    extra = ""
    if guias:
        extra = GUIAS_STORY if formato == "9:16" else GUIAS_FEED
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<base href="{pasta.as_uri()}/">
<style>{face_das_fontes()}</style>
<style>:root{{--largura:{largura}px;--altura:{altura}px;
--logo:url('{LOGO_CLARO.as_uri()}');
--logo-escuro:url('{LOGO_ESCURO.as_uri()}');}}</style>
<style>{BASE_CSS.read_text(encoding="utf-8")}</style>
<style>html,body{{width:{largura}px;height:{altura}px;overflow:hidden;}}{extra}</style>
</head>
<body>
{fragmento}
</body>
</html>"""


def slides_de(entrada: Path) -> tuple[Path, list[Path]]:
    """Devolve (pasta do carrossel, lista de fragmentos em ordem)."""
    entrada = entrada.resolve()
    if entrada.is_file():
        return entrada.parent.parent, [entrada]
    pasta_slides = entrada / "slides"
    if not pasta_slides.is_dir():
        sys.exit(f"ERRO: não achei {pasta_slides}")
    arquivos = sorted(pasta_slides.glob("*.html"))
    if not arquivos:
        sys.exit(f"ERRO: nenhum .html em {pasta_slides}")
    if len(arquivos) > MAX_SLIDES:
        sys.exit(f"ERRO: {len(arquivos)} slides; o Instagram aceita {MAX_SLIDES}")
    return entrada, arquivos


def renderizar(entrada: Path, formato: str, guias: bool, contato: bool) -> None:
    from playwright.sync_api import sync_playwright

    if formato not in MARCA["formatos"]:
        sys.exit(f"ERRO: formato {formato} — use {', '.join(MARCA['formatos'])}")
    largura, altura = MARCA["formatos"][formato]

    pasta, arquivos = slides_de(entrada)
    saida = pasta / "png"
    saida.mkdir(parents=True, exist_ok=True)

    # Formato alternativo e prova de zona segura não podem sobrescrever a arte
    # do formato padrão — foi fácil perder uma rodada inteira assim.
    sufixo = "" if formato == MARCA["formato_padrao"] else f"@{formato.replace(':', 'x')}"
    if guias:
        sufixo += "@guias"

    gerados: list[Path] = []
    tmp = Path(tempfile.mkdtemp(prefix="carrossel-"))
    try:
        with sync_playwright() as p:
            navegador = p.chromium.launch()
            ctx = navegador.new_context(
                viewport={"width": largura, "height": altura},
                device_scale_factor=1,
                locale="pt-BR",
            )
            pagina = ctx.new_page()
            for i, arquivo in enumerate(arquivos, start=1):
                html = documento(
                    arquivo.read_text(encoding="utf-8"),
                    largura, altura, arquivo.parent, guias, formato,
                )
                alvo = tmp / f"{arquivo.stem}.html"
                alvo.write_text(html, encoding="utf-8")
                pagina.goto(alvo.as_uri(), wait_until="load")
                if guias:
                    # A guia é injetada aqui, e não escrita no slide: prova de
                    # zona segura é conferência, não parte da arte.
                    pagina.evaluate(
                        "document.querySelectorAll('.slide').forEach(s =>"
                        " s.insertAdjacentHTML('beforeend',"
                        " '<div class=\"zona-segura\"></div>'))")
                # As fontes vêm de disco, mas o layout só é confiável depois de
                # o Chromium terminar de aplicá-las.
                pagina.evaluate("document.fonts.ready")
                pagina.wait_for_timeout(300)
                png = saida / f"{arquivo.stem}{sufixo}.png"
                pagina.screenshot(path=str(png), type="png")
                confere(png, largura, altura)
                gerados.append(png)
                print(f"OK  {png.relative_to(pasta)}  {largura}x{altura}"
                      f"  (slide {i}/{len(arquivos)})")
            navegador.close()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if contato:
        folha_de_contato(gerados, pasta, sufixo)


def confere(png: Path, largura: int, altura: int) -> None:
    """Um PNG fora da medida é recusado pelo Instagram sem aviso claro."""
    from PIL import Image

    with Image.open(png) as img:
        if img.size != (largura, altura):
            sys.exit(f"ERRO: {png.name} saiu {img.size}, esperado ({largura}, {altura})")


def folha_de_contato(pngs: list[Path], pasta: Path, sufixo: str = "",
                     colunas: int = 4) -> Path:
    """Todos os slides numa imagem só, para revisar o conjunto de uma vez.

    A memória dos manuais já ensina que revisão em miniatura esconde problema de
    detalhe: a folha serve para ver ritmo e repetição, não para aprovar tipografia.
    """
    from PIL import Image

    larg_mini = 320
    linhas = (len(pngs) + colunas - 1) // colunas
    with Image.open(pngs[0]) as primeira:
        alt_mini = round(larg_mini * primeira.height / primeira.width)

    pad = 16
    folha = Image.new(
        "RGB",
        (colunas * larg_mini + (colunas + 1) * pad,
         linhas * alt_mini + (linhas + 1) * pad),
        (244, 244, 245),
    )
    for i, png in enumerate(pngs):
        with Image.open(png) as img:
            mini = img.convert("RGB").resize((larg_mini, alt_mini), Image.LANCZOS)
        col, lin = i % colunas, i // colunas
        folha.paste(mini, (pad + col * (larg_mini + pad),
                           pad + lin * (alt_mini + pad)))
    destino = pasta / f"folha-de-contato{sufixo}.png"
    folha.save(destino)
    print(f"OK  {destino.relative_to(pasta)}  {folha.width}x{folha.height}")
    return destino


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("entrada", type=Path,
                    help="pasta do carrossel (carrosseis/<slug>) ou um slide .html")
    ap.add_argument("--formato", default=MARCA["formato_padrao"],
                    choices=list(MARCA["formatos"]))
    ap.add_argument("--guias", action="store_true",
                    help="desenha a zona que a interface do Instagram cobre")
    ap.add_argument("--contato", action="store_true",
                    help="monta a folha de contato depois de renderizar")
    args = ap.parse_args()

    if not args.entrada.exists():
        sys.exit(f"ERRO: não existe: {args.entrada}")

    renderizar(args.entrada, args.formato, args.guias, args.contato)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
