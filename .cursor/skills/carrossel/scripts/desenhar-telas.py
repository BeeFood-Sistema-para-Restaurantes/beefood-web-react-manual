#!/usr/bin/env python3
"""Desenha a tela de resultado que o sandbox não consegue mostrar.

Segundo degrau da imagem — **resultado capturado > resultado desenhado**, e
nunca tela de configuração — e ele existe por casos concretos: a peça de dark
kitchen precisa de uma operação com três marcas e o sandbox é uma loja só; a
Gestão de Entregas precisa de um relatório com volume e o sandbox só tem traço.
Sem este degrau, a saída seria recortar a ilustração da página de vendas, que é
marketing, ou publicar o formulário de configuração, que é manual.

Desenhar **não** é o porão. Quando o fato é uma regra — sete campos numa
janela —, este script é o único caminho para a imagem mostrar o efeito da regra
em vez do painel de controle dela.

Desenhar **não** é inventar produto. O que entra no fragmento é o que o sistema
mostra: `Aguardando`, `Preparo`, `Pronto/Entrega`, `Entregue` e `Cancelado` são
os nomes das colunas do Delivery porque é assim na tela; `Por Cardápio` é o
rótulo do painel inicial porque é assim no painel. Número é exemplo, e é um jogo
só na peça inteira — nem o do release, nem o `R$ 298.921,66` da arte do site, que
na nossa arte viraria promessa de resultado.

Entrada : carrosseis/<slug>/telas/*.html   (fragmento de body)
Saída   : carrosseis/<slug>/imagens-puras/<nome>.png

O fragmento declara a própria medida no elemento raiz:

    <div class="tela" data-medida="1280x760"> … </div>

Ele é fragmento como o slide: o embrulho (Mulish de disco, `painel.css`,
`skill:` resolvido) é deste script, e a medida vira `--largura`/`--altura`. Sai
em DPR 2, porque a tela desenhada entra no slide reduzida — e texto de interface
reduzido a partir de 1x fica sujo.

Uso:
    python desenhar-telas.py <slug>
    python desenhar-telas.py <slug> --tela painel-por-cardapio
    python desenhar-telas.py <slug> --listar
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from renderizar import face_das_fontes, resolver_skill  # noqa: E402

SKILL = Path(__file__).resolve().parent.parent
RAIZ = SKILL.parents[2]
PAINEL_CSS = SKILL / "assets" / "telas" / "painel.css"
MEDIDA_PADRAO = (1280, 760)
DPR = 2


def medida_de(fragmento: str) -> tuple[int, int]:
    achado = re.search(r'data-medida="(\d+)x(\d+)"', fragmento)
    if not achado:
        return MEDIDA_PADRAO
    return int(achado.group(1)), int(achado.group(2))


def documento(fragmento: str, largura: int, altura: int, pasta: Path) -> str:
    fragmento = resolver_skill(fragmento)
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<base href="{pasta.as_uri()}/">
<style>{face_das_fontes()}</style>
<style>:root{{--largura:{largura}px;--altura:{altura}px;}}</style>
<style>{PAINEL_CSS.read_text(encoding="utf-8")}</style>
<style>html,body{{width:{largura}px;height:{altura}px;overflow:hidden;}}</style>
</head>
<body>
{fragmento}
</body>
</html>"""


def desenhar(slug: str, so: str | None) -> None:
    from playwright.sync_api import sync_playwright

    pasta = RAIZ / "carrosseis" / slug
    telas = pasta / "telas"
    if not telas.is_dir():
        sys.exit(f"ERRO: não achei {telas}")

    arquivos = sorted(telas.glob("*.html"))
    if so:
        arquivos = [a for a in arquivos if a.stem == so]
        if not arquivos:
            sys.exit(f"ERRO: não achei telas/{so}.html")

    saida = pasta / "imagens-puras"
    saida.mkdir(parents=True, exist_ok=True)

    tmp = Path(tempfile.mkdtemp(prefix="telas-"))
    try:
        with sync_playwright() as p:
            navegador = p.chromium.launch()
            for arquivo in arquivos:
                fragmento = arquivo.read_text(encoding="utf-8")
                largura, altura = medida_de(fragmento)
                ctx = navegador.new_context(
                    viewport={"width": largura, "height": altura},
                    device_scale_factor=DPR,
                    locale="pt-BR",
                )
                pagina = ctx.new_page()
                alvo = tmp / f"{arquivo.stem}.html"
                alvo.write_text(documento(fragmento, largura, altura, arquivo.parent),
                                encoding="utf-8")
                pagina.goto(alvo.as_uri(), wait_until="load")
                pagina.evaluate("document.fonts.ready")
                pagina.wait_for_timeout(200)
                png = saida / f"{arquivo.stem}.png"
                pagina.screenshot(path=str(png), type="png")
                ctx.close()
                print(f"OK  {png.relative_to(RAIZ)}  "
                      f"{largura * DPR}x{altura * DPR}  (desenho)")
            navegador.close()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("slug", help="pasta em carrosseis/")
    p.add_argument("--tela", help="desenha só esta (nome do arquivo, sem .html)")
    p.add_argument("--listar", action="store_true")
    args = p.parse_args()

    telas = RAIZ / "carrosseis" / args.slug / "telas"
    if args.listar:
        for a in sorted(telas.glob("*.html")):
            l, h = medida_de(a.read_text(encoding="utf-8"))
            print(f"{a.stem:<32}{l}x{h}")
        return

    desenhar(args.slug, args.tela)


if __name__ == "__main__":
    main()
