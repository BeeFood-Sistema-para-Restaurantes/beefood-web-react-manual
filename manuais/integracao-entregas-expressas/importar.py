"""Traz para `imagens-puras/` as quatro capturas do artigo público do Entregas Expressas.

O manual mostra as duas pontas da integração, e só uma delas é fotografável aqui: o painel do
Entregas Expressas é de outra empresa. Essas quatro imagens vêm do artigo
`ajuda.entregasexpressas.com.br/hc/articles/5/75/388/como-integrar-a-beefood-ao-entregas-expressas`,
que é público, e os endereços exatos estão em `ORIGEM`.

Duas regras da casa comandam este arquivo:

* **O importador nunca escreve em `imagens-tratadas/`.** Ele só repõe a pura; as setas são do
  `annotate.py`. É a mesma separação do #24 e do #125 — se o importador mexesse na tratada, a
  próxima execução apagaria a anotação.
* **Dado pessoal sai coberto na pura**, porque a pura também é versionada e o repositório é
  público. A captura do pedido traz telefone e e-mail; eles são cobertos aqui, antes de a pura
  ser gravada. Os nomes (*ESTABELECIMENTO TESTE*, *Cliente Teste Entregas*) ficam: são
  rótulos de teste do próprio artigo, e borrar o que é evidentemente falso só piora a imagem.

Ele **avisa e segue** quando não há rede: as puras versionadas bastam para rodar o
`annotate.py`, e é de propósito que o manual não dependa de o artigo continuar no ar.
"""

from __future__ import annotations

import urllib.error
import urllib.request
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageFilter

SRC = Path(__file__).resolve().parent / "imagens-puras"
SRC.mkdir(exist_ok=True)

BASE = "https://ajuda.entregasexpressas.com.br/storage/article-images"

# O servidor devolve 403 para o agente padrão do urllib. Com um agente de navegador ele
# responde normalmente — o mesmo que o `curl` já fazia na mão.
AGENTE = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129 Safari/537.36"

# nome da pura -> (arquivo na origem, regiões a cobrir em pixel da imagem baixada)
ORIGEM: dict[str, tuple[str, tuple[tuple[int, int, int, int], ...]]] = {
    "05-ee-cadastrar-integracao.png": ("049a5fc0-c0e7-4ec5-a3f9-cf5439df0769.png", ()),
    "06-ee-colar-credencial.png": ("4e532f1d-c25a-4ce3-a97c-d3227c093b08.png", ()),
    "07-ee-quando-vira-entrega.png": ("1793fc8d-356e-49da-8527-9914b5cd4ed2.png", ()),
    "11-ee-pedido-no-painel.png": (
        "af7a2fd1-460c-4d67-afd8-fac84695e7bd.png",
        (
            (244, 520, 345, 537),   # telefone do estabelecimento
            (235, 537, 415, 554),   # e-mail do estabelecimento
            (583, 650, 668, 674),   # telefone do destinatário
        ),
    ),
}


def cobrir(img: Image.Image, regioes) -> Image.Image:
    """Borra as regiões pedidas. Raio alto de propósito: borrão fraco ainda se lê."""
    for caixa in regioes:
        pedaco = img.crop(caixa).filter(ImageFilter.GaussianBlur(9))
        img.paste(pedaco, caixa[:2])
    return img


def baixar(nome: str, arquivo: str, regioes) -> None:
    destino = SRC / nome
    try:
        pedido = urllib.request.Request(f"{BASE}/{arquivo}", headers={"User-Agent": AGENTE})
        with urllib.request.urlopen(pedido, timeout=30) as resp:
            bruto = resp.read()
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        if destino.exists():
            print("PULA", nome, f"({e}; usando a pura versionada)")
        else:
            print("FALTA", nome, f"({e}; e não há pura versionada)")
        return
    img = cobrir(Image.open(BytesIO(bruto)).convert("RGB"), regioes)
    img.save(destino)
    print("PURA", nome, img.size, f"({len(regioes)} região(ões) coberta(s))")


if __name__ == "__main__":
    for nome, (arquivo, regioes) in ORIGEM.items():
        baixar(nome, arquivo, regioes)
