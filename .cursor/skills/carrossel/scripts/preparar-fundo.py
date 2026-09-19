#!/usr/bin/env python3
"""Tira de um vídeo de comida as duas artes de fundo do totem.

    # as artes que já estão na biblioteca (assets/fundos/)
    python preparar-fundo.py

    # outro vídeo, outro nome
    python preparar-fundo.py --video https://.../massa.mp4 --nome fundo-massa \
        --segundo 2.5

Por que existe: o totem de exemplo é de um cliente de verdade, e a arte de espera
dele é um cartaz de promoção — na primeira versão do carrossel da tradução, a
única coisa legível na tela do totem era "Pudim R$ 16,90". Campanha de uma loja
**rouba o assunto** da peça e ainda amarra o post àquela promoção.

A saída são duas imagens **nossas**, que entram no aplicativo pela mesma
interceptação que injeta a tradução (`capturar-totem.py`):

| Arquivo | Onde o totem usa | Medida |
|---|---|---|
| `<nome>-espera.png` | tela de espera, atrás do botão | 1080x1920 (9/16) |
| `<nome>-banner.png` | faixa do topo do cardápio | 1444x577 (a medida do original) |

O véu escuro não é enfeite: o aplicativo desenha o botão vermelho e a pílula das
bandeiras **por cima** da foto, e vermelho sobre batata dourada perde contraste.
Na tela de espera a faixa do meio é a que mais escurece, que é onde o botão cai;
no banner é o topo, onde ficam o `CANCEL ORDER` e as bandeiras.

O vídeo bruto e o quadro extraído vão para a pasta temporária do sistema: são
material de trabalho, não entram no repositório.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlopen

SKILL = Path(__file__).resolve().parent.parent
FUNDOS = SKILL / "assets" / "fundos"

# O vídeo que o dono mandou para o carrossel da tradução: batata frita saindo da
# fritadeira, com fumaça. Serve de padrão porque é o fundo que está na
# biblioteca — trocar de vídeo é passar --video.
VIDEO = "https://beetech-imagens.s3-sa-east-1.amazonaws.com/15852/34212806c.mp4"

# 3,2 s é onde a fumaça está aberta sobre as batatas. Antes disso ela cobre o
# terço de cima; depois, a coluna de vapor fecha no meio do quadro. Vídeo novo
# pede olhar o quadro antes de aceitar o valor.
SEGUNDO = "3.2"

ESPERA = (1080, 1920)
BANNER = (1444, 577)


def quadro(video: str, segundo: str):
    """Baixa o vídeo (uma vez por sessão) e devolve o quadro escolhido."""
    from PIL import Image

    trabalho = Path(tempfile.gettempdir()) / "carrossel-fundos"
    trabalho.mkdir(parents=True, exist_ok=True)
    origem = Path(video)
    if origem.is_file():
        bruto = origem
    else:
        bruto = trabalho / Path(urlparse(video).path).name
        if not bruto.is_file():
            with urlopen(video) as fonte:
                bruto.write_bytes(fonte.read())
            print(f"OK  baixado {bruto}")
    png = trabalho / f"{bruto.stem}-{segundo}.png"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", segundo, "-i", str(bruto),
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
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--video", default=VIDEO, help="URL ou arquivo local")
    ap.add_argument("--segundo", default=SEGUNDO, help="tempo do quadro (s)")
    ap.add_argument("--nome", default="fundo-totem", help="prefixo dos arquivos")
    ap.add_argument("--saida", type=Path, default=FUNDOS)
    args = ap.parse_args()

    try:
        from PIL import Image  # noqa: F401
    except ImportError:
        sys.exit("ERRO: falta o Pillow (pip install pillow)")

    args.saida.mkdir(parents=True, exist_ok=True)
    base = quadro(args.video, args.segundo)

    veu(enquadrar(base, *ESPERA), 0.35, 0.45, 0.25).save(
        args.saida / f"{args.nome}-espera.png")
    veu(enquadrar(base, *BANNER, foco=0.34), 0.45, 0.3, 0.3).save(
        args.saida / f"{args.nome}-banner.png")

    for sufixo in ("espera", "banner"):
        print(f"OK  {args.saida / f'{args.nome}-{sufixo}.png'}")


if __name__ == "__main__":
    main()
