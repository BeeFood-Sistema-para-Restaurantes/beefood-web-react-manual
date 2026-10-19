"""Importa as capturas do artigo público do Route Delivery para o #129.

O artigo é `routedelivery-loja.vercel.app/ajuda/integrar-beefood.html`, e as seis capturas do
painel ADM dele **não são arquivos**: vêm embutidas no próprio HTML como `data:image/png;base64`.
Então importar aqui não é baixar imagem, é ler o HTML, achar cada `<figure>`, decodificar o
base64 e gravar com o nome que o manual usa. A legenda (`<figcaption>`) é o que amarra cada
figura ao passo certo, e por isso o mapa abaixo é por legenda, não por posição.

Duas figuras do artigo **não** são importadas de propósito: as duas marcadas
*"Ilustração dos campos a preencher"* são maquetes em HTML da tela do **portal de desenvolvedor**
da BeeFood (`docs.beefood.app`) — justamente o caminho que este manual troca por
**Aplicativos → API Aberta**. Elas nem têm `<img>`; são `div` montadas na página.

Nenhum dado pessoal aparece nas seis: o artigo usa *Sua Loja*, Client ID de exemplo e segredos
em bolinhas. Então não há o que cobrir antes de gravar — diferente do #127, em que a captura do
pedido trazia telefone e e-mail e o importador borrava as três regiões.

Sem rede, o script **avisa e segue**: as puras ficam versionadas, e o `annotate.py` não depende
de o artigo continuar no ar.

Uso, de dentro da pasta do manual:

    python3 importar.py
"""

from __future__ import annotations

import base64
import re
import urllib.error
import urllib.request
from pathlib import Path

ARTIGO = "https://routedelivery-loja.vercel.app/ajuda/integrar-beefood.html"
DEST = Path(__file__).resolve().parent / "imagens-puras"

# O servidor devolve 403 para o agente padrão do urllib (o mesmo tropeço do #127).
AGENTE = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
          "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# Trecho da legenda -> nome da pura. A ordem é a do manual, não a do artigo.
MAPA = {
    "cartão BeeFood": "06-rd-cartao-beefood.png",
    "Vincular loja": "07-rd-vincular-loja.png",
    "situação da integração": "08-rd-integracao-ativa.png",
    "Quadro Credenciais": "09-rd-liberar-na-chegada.png",
    "Receber os pedidos": "10-rd-canais-marketplace.png",
    "Copiar o endereço do webhook": "11-rd-endereco-webhook.png",
}


def baixar() -> str | None:
    pedido = urllib.request.Request(ARTIGO, headers={"User-Agent": AGENTE})
    try:
        with urllib.request.urlopen(pedido, timeout=30) as resposta:
            return resposta.read().decode("utf-8", "replace")
    except (urllib.error.URLError, TimeoutError) as erro:
        print(f"AVISO sem o artigo ({erro}). As puras versionadas continuam valendo.")
        return None


def limpar(html: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html)).strip()


def main() -> None:
    html = baixar()
    if html is None:
        return
    DEST.mkdir(exist_ok=True)
    achadas = 0
    for figura in re.findall(r"<figure.*?</figure>", html, re.S):
        imagem = re.search(r'src="data:image/png;base64,([^"]+)"', figura)
        legenda = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", figura, re.S)
        if not imagem or not legenda:
            continue
        texto = limpar(legenda.group(1))
        nome = next((v for k, v in MAPA.items() if k in texto), None)
        if nome is None:
            print(f"IGNORADA  {texto[:70]}")
            continue
        dados = base64.b64decode(imagem.group(1))
        (DEST / nome).write_bytes(dados)
        achadas += 1
        print(f"PURA {nome}  {len(dados) // 1024} KB  <- {texto[:60]}")
    print(f"{achadas} de {len(MAPA)} capturas do parceiro importadas")
    if achadas != len(MAPA):
        print("ATENÇÃO o artigo mudou: confira o MAPA das legendas antes de anotar.")


if __name__ == "__main__":
    main()
