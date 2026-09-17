#!/usr/bin/env python3
"""Monta o fundo do totem a partir do vídeo de batata frita que o dono passou.

    python carrosseis/traducao-cardapio-presencial/preparar-fundo.py

Por que existe: o totem de exemplo é de um cliente de verdade, e a arte de
espera dele é um cartaz de "Pudim R$ 16,90". Num carrossel sobre tradução, esse
cartaz vira o assunto da imagem — o olho lê o preço, não o cardápio em inglês —
e ainda amarra a peça à promoção de uma loja só.

A saída são duas imagens **nossas**, que entram no aplicativo pela mesma
interceptação que injeta a tradução (`capturar-totem.py`):

| Arquivo | Onde o totem usa | Medida |
|---|---|---|
| `fundo-totem-espera.png` | tela de espera, atrás do botão | 1080x1920 (9/16) |
| `fundo-totem-banner.png` | faixa do topo do cardápio | 1444x577 (a medida do original) |

O véu escuro não é enfeite: o aplicativo desenha o botão vermelho e a pílula das
bandeiras **por cima** da foto, e vermelho sobre batata dourada perde contraste.
A faixa do meio é a que mais escurece, que é onde o botão cai.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from urllib.request import urlopen

PASTA = Path(__file__).resolve().parent
MIDIA = PASTA / "midia"

VIDEO = ("https://beetech-imagens.s3-sa-east-1.amazonaws.com/15852/34212806c.mp4")

# 3,2 s é onde a fumaça está aberta sobre as batatas. Antes disso ela cobre o
# terço de cima; depois, a coluna de vapor fecha no meio do quadro.
SEGUNDO = "3.2"

ESPERA = (1080, 1920)
BANNER = (1444, 577)


def quadro(destino: Path) -> "Image.Image":
    """Baixa o vídeo (uma vez) e devolve o quadro escolhido."""
    from PIL import Image

    bruto = destino / "video-fundo.mp4"
    if not bruto.is_file():
        destino.mkdir(parents=True, exist_ok=True)
        with urlopen(VIDEO) as fonte:
            bruto.write_bytes(fonte.read())
        print(f"OK  baixado {bruto.name}")
    png = destino / "quadro-video.png"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", SEGUNDO, "-i", str(bruto),
                    "-frames:v", "1", str(png)], check=True)
    return Image.open(png).convert("RGB")


def enquadrar(im, larg: int, alt: int, foco: float = 0.5):
    """Recorta cobrindo a medida pedida — é o `object-cover` do CSS.

    `foco` é a altura do quadro original que fica no centro do recorte. Numa
    faixa larga tirada de um vídeo em pé isso decide tudo: no meio sai só massa
    de batata, e mais em cima entra a ponta das batatas com a fumaça atrás.
    """
    from PIL import Image

    escala = max(larg / im.width, alt / im.height)
    nova = im.resize((round(im.width * escala), round(im.height * escala)), Image.LANCZOS)
    x = (nova.width - larg) // 2
    y = min(max(round(nova.height * foco - alt / 2), 0), nova.height - alt)
    return nova.crop((x, y, x + larg, y + alt))


def veu(im, topo: float, meio: float, base: float):
    """Escurece a foto em três faixas, com a transição borrada entre elas."""
    from PIL import Image, ImageFilter

    larg, alt = im.size
    tira = Image.new("L", (1, alt))
    for y in range(alt):
        t = y / alt
        tira.putpixel((0, y), int(255 * (topo if t < 0.4 else meio if t < 0.8 else base)))
    mascara = tira.resize((larg, alt)).filter(ImageFilter.GaussianBlur(alt * 0.06))
    return Image.composite(Image.new("RGB", im.size, (0, 0, 0)), im, mascara)


def main() -> None:
    try:
        from PIL import Image  # noqa: F401
    except ImportError:
        sys.exit("ERRO: falta o Pillow (pip install pillow)")

    MIDIA.mkdir(parents=True, exist_ok=True)
    base = quadro(MIDIA)

    espera = veu(enquadrar(base, *ESPERA), 0.35, 0.45, 0.25)
    espera.save(MIDIA / "fundo-totem-espera.png")

    # No banner o aplicativo põe CANCEL ORDER na esquerda e as bandeiras na
    # direita, os dois no alto: o topo escurece mais que o resto.
    banner = veu(enquadrar(base, *BANNER, foco=0.34), 0.45, 0.3, 0.3)
    banner.save(MIDIA / "fundo-totem-banner.png")

    for arquivo in ("fundo-totem-espera.png", "fundo-totem-banner.png"):
        print(f"OK  {(MIDIA / arquivo).relative_to(PASTA.parent.parent)}")


if __name__ == "__main__":
    main()
