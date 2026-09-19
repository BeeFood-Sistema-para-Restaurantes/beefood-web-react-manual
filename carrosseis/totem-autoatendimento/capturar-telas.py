#!/usr/bin/env python3
"""Fotografa o Totem de Autoatendimento pedindo um lanche, do toque ao pagamento.

Rodar da raiz do repositório:
    python carrosseis/totem-autoatendimento/capturar-telas.py

Por que não é o `capturar-totem.py` da skill: aquele script existe para o
carrossel de **tradução** — ele injeta `aaTraducao: true` e o cardápio traduzido,
e a peça dele para no cardápio. Esta aqui é sobre o cliente pedir sozinho, e
precisa do que vem **depois** do cardápio: montar o lanche, a sacola, a
identificação e a confirmação. Ligar a tradução aqui seria pior: as bandeiras
apareceriam na tela de espera contando outra história.

O que se reaproveita de lá é o caro, e está copiado abaixo com o motivo:
contexto com `service_workers="block"`, rota no **contexto** e não na página, e
a troca da arte de fundo da loja pela nossa.

**Nenhum pedido é criado.** O roteiro para no botão `Ir para pagamento`, que é a
última tela antes de o totem chamar o pinpad. O telefone e o nome digitados são
de teste e só existem enquanto a aba está aberta: cliente e pedido nascem depois
do pagamento, e o script nunca chega lá.

## As telas que saem, e para que servem

| Arquivo | Slide | O que prova |
|---|---|---|
| `espera-720.png` | 1 | o aparelho parado, esperando o toque |
| `cardapio-720.png` | 8 | a tela inteira, para caber na moldura 9/16 do mockup |
| `cardapio-topo.png` | 3 | o cardápio com foto, setor e preço |
| `turbinar.png` | 4 | o adicional oferecido no meio do pedido, com preço |
| `peca-tambem.png` | 4 | a sugestão da sacola, com o selo `Gerada por IA` |
| `cupom-modal.png` | 5 | o cliente digita o código ou escolhe da lista, no aparelho |
| `cashback-telefone.png` | 6 | o totem oferece o cashback em troca do telefone |
| `como-sera.png` | 7 | comer aqui ou levar, escolhido pelo cliente |
| `ir-para-pagamento.png` | 7 | o pagamento termina no próprio totem |

## O cupom vem de `cupons.json`, e por quê

A loja de exemplo não tem cupom cadastrado: `venda2/cupomDescontoAtivo?tipo=totem`
responde `[]`, e sem lista o totem esconde a linha de cupom inteira. É o caso
que a skill já resolveu no carrossel da tradução — **recurso desligado na loja
de exemplo se liga na resposta da API** — e a rota devolve os cupons de
`cupons.json` no lugar da lista vazia. O que vem de fora é só o que o
restaurante escreveria no painel: código, título, benefício e regra. A tela, a
lista, o campo de código e os cartões são do aplicativo de produção.

O recorte do modal **começa abaixo do cabeçalho**, que traz o logotipo da loja:
cupom de exemplo não pode parecer promoção anunciada por um cliente nosso.

## Recorte por coordenada, e não por seletor

O totem é PWA compilado, sem `id` ou classe estável em que ancorar. Como a
janela é sempre 1080x1920 (a tela do aparelho do catálogo), a régua é a própria
janela: as faixas abaixo foram medidas nos prints e valem enquanto o layout do
aplicativo não mudar. Cada recorte sai em DPR 2 — reduzido para 600 px no slide,
DPR 1 sai pastoso.
"""

from __future__ import annotations

import json
from pathlib import Path

from playwright.sync_api import sync_playwright

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
PURAS = AQUI / "imagens-puras"
FUNDOS = RAIZ / ".cursor" / "skills" / "carrossel" / "assets" / "fundos"
CUPONS = json.loads((AQUI / "cupons.json").read_text(encoding="utf-8"))

TOTEM = ("https://totem.beefood.app/?empresaID=350&filialID=380"
         "&token=669461A4-1729-4E31-9BD2-8446993BBE7C")

# A loja de exemplo anuncia um pudim na tela de espera e na faixa do cardápio, e
# num carrossel sobre autoatendimento o olho lê o preço do pudim em vez da tela.
# Endereço que não existe: a rota `servir_fundo` responde com o arquivo local.
FUNDO_BASE = "https://carrossel.beefood.local/"
ARTES = {"AASLIDE": "-espera.png", "AACAPA": "-banner.png"}
NOME_FUNDO = "fundo-totem"

TELA = {"width": 1080, "height": 1920}
# A capa usa o totem com 420 px de largura. O aplicativo desenha o botão em px
# fixo, então capturar em 1080p e reduzir para 420 engole o `FAÇA SEU PEDIDO`:
# em 720p o botão ocupa 1,5x mais da imagem, com a mesma proporção 9/16.
TELA_MENOR = {"width": 720, "height": 1280}

# O botão da tela de espera pulsa para sempre, e o Playwright espera a
# estabilidade até estourar o tempo. Todo clique vai com force=True por isso.
CARGA = 6000

# Faixas medidas na janela de 1080x1920, de cima para baixo.
RECORTES = {
    # Para logo depois da primeira fileira de produtos, nos 14 px de fundo que
    # separam uma fileira da outra. Cortar no meio da segunda deixava meia foto
    # na borda do slide, e meia foto na borda lê como render que falhou.
    "cardapio-topo": (0, 0, 1080, 800),
    # Os dois momentos da venda sugestiva dividem um slide, então a faixa é
    # baixa: a pergunta e as duas primeiras fileiras de adicional. Para em 436,
    # que é o vão entre a segunda fileira e a terceira — a fileira tem 170 px.
    "turbinar": (0, 616, 1080, 436),
    # Para 1030 e não 1080: a lista da sacola é um carrossel horizontal, e na
    # borda da janela sobra uma lasca do cartão seguinte — nome e preço cortados
    # no meio. A grade é de 256 px com 12 px de vão, então 1030 cai no vão
    # depois do quarto cartão, qualquer que seja a sugestão daquele dia.
    "peca-tambem": (0, 370, 1030, 450),
    # Só a pergunta do consumo. Mais abaixo a tela lista nome, telefone e mesa,
    # e ali estão os dados de teste digitados aqui — recorte que os mostrasse
    # poria um "TESTE" no meio da arte.
    "como-sera": (0, 100, 1080, 300),
    "ir-para-pagamento": (0, 1650, 1080, 270),
    # Do "Adicionar cupom" até o fim do segundo cartão. Começa abaixo do
    # cabeçalho de propósito: lá está o logotipo da loja.
    "cupom-modal": (0, 110, 1080, 590),
    # O ícone, a pergunta, a faixa do cashback e o campo vazio. Para antes do
    # teclado, que é meia tela de tecla repetida.
    "cashback-telefone": (0, 150, 1080, 450),
}

# Cliente de teste. Nada disso é gravado: o pedido para antes do pagamento.
TELEFONE = "11987654321"
NOME = "TESTE"
MESA = "12"


def rotear_fundos(contexto) -> None:
    """Põe a nossa foto no lugar da arte de campanha da loja de exemplo.

    `imagens/slides` é o que passa na tela de espera e `imagens/empresa` traz a
    faixa do cardápio (`AACAPA`) e o logotipo da loja (`AALOGO`, que continua o
    dela — a tela é do cliente dele).
    """
    def trocar(rota):
        resposta = rota.fetch()
        dados = resposta.json()
        for item in dados:
            sufixo = ARTES.get(item.get("tipo"))
            if sufixo:
                item["s3Link"] = f"{FUNDO_BASE}{NOME_FUNDO}{sufixo}"
        rota.fulfill(response=resposta, json=dados)

    def servir(rota):
        arquivo = FUNDOS / rota.request.url.rsplit("/", 1)[-1]
        rota.fulfill(status=200, content_type="image/png",
                     body=arquivo.read_bytes())

    # Rota no **contexto**, e não na página: o totem é PWA e a foto de fundo é
    # pedida pelo service worker dele, que `page.route` não enxerga.
    contexto.route("**/api/totem2/imagens/**", trocar)
    contexto.route(f"{FUNDO_BASE}**", servir)


def rotear_cupons(contexto) -> None:
    """Devolve os cupons de `cupons.json` no lugar da lista vazia da loja.

    Com `[]` o totem não desenha nem a linha de cupom na confirmação, e a tela
    do recurso fica inalcançável. O aplicativo lê os campos da resposta sem
    traduzir nada, então o arquivo tem exatamente o que a API devolveria se a
    loja tivesse esses cupons cadastrados.
    """
    contexto.route("**/venda2/cupomDescontoAtivo/**",
                   lambda rota: rota.fulfill(status=200, json=CUPONS))


def abrir(navegador, tela: dict, escala: int):
    """Contexto do totem, com o service worker desligado.

    Sem `service_workers="block"` o PWA serve as imagens pelo próprio worker e o
    que a interceptação devolve não chega à página.
    """
    contexto = navegador.new_context(viewport=tela, device_scale_factor=escala,
                                     locale="pt-BR", service_workers="block")
    rotear_fundos(contexto)
    rotear_cupons(contexto)
    return contexto


def tocar(pagina, texto: str, minimo: int = 0, obrigatorio: bool = True) -> str | None:
    """Clica o botão cujo rótulo contém `texto`, da altura `minimo` para baixo.

    Por texto normalizado, e não por seletor: `Adicionar\\nR$ 24,00` é um botão
    só, e o `minimo` é o que separa a barra de ação de baixo dos cartões de
    produto, que repetem as mesmas palavras.

    `obrigatorio=False` devolve `None` em vez de parar: é como o laço dos grupos
    de complemento descobre que chegou no último — lá o botão deixa de ser
    `Pular` e vira `Adicionar`.
    """
    rotulo = pagina.evaluate("""([texto, minimo]) => {
      const ler = b => (b.innerText || '').replace(/\\s+/g, ' ').trim();
      const alvo = [...document.querySelectorAll('button')].find(b =>
        b.getBoundingClientRect().y >= minimo
        && ler(b).toUpperCase().includes(texto));
      if (!alvo) return null;
      alvo.click();
      return ler(alvo);
    }""", [texto.upper(), minimo])
    if rotulo is None:
        if obrigatorio:
            raise SystemExit(f"ERRO: não achei o botão {texto!r}. O aplicativo mudou?")
        return None
    pagina.wait_for_timeout(2500)
    return rotulo


def digitar(pagina, texto: str) -> None:
    """Teclado do próprio totem: uma tecla por caractere."""
    for caractere in texto:
        pagina.get_by_role("button", name=caractere, exact=True).first.click(force=True)
        pagina.wait_for_timeout(150)


def recortar(pagina, nome: str) -> None:
    x, y, largura, altura = RECORTES[nome]
    caminho = PURAS / f"{nome}.png"
    pagina.screenshot(path=str(caminho),
                      clip={"x": x, "y": y, "width": largura, "height": altura})
    print(f"OK  {caminho.relative_to(RAIZ)}")


def main() -> None:
    PURAS.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        navegador = pw.chromium.launch()

        # 1. As duas telas que vão DENTRO do mockup do aparelho, e por isso
        # inteiras e em 9/16: recorte com outra proporção entraria em
        # `object-fit: cover` e sairia com a terceira coluna de produtos
        # cortada no meio do nome.
        contexto = abrir(navegador, TELA_MENOR, 1)
        pagina = contexto.new_page()
        pagina.goto(TOTEM, wait_until="networkidle", timeout=90000)
        pagina.wait_for_timeout(CARGA)
        pagina.screenshot(path=str(PURAS / "espera-720.png"))
        print(f"OK  {(PURAS / 'espera-720.png').relative_to(RAIZ)}")
        tocar(pagina, "FAÇA SEU PEDIDO")
        pagina.wait_for_timeout(3000)
        pagina.screenshot(path=str(PURAS / "cardapio-720.png"))
        print(f"OK  {(PURAS / 'cardapio-720.png').relative_to(RAIZ)}")
        contexto.close()

        # 2. O pedido inteiro, na tela do aparelho e em DPR 2 para o recorte.
        contexto = abrir(navegador, TELA, 2)
        pagina = contexto.new_page()
        pagina.goto(TOTEM, wait_until="networkidle", timeout=90000)
        pagina.wait_for_timeout(CARGA)
        tocar(pagina, "FAÇA SEU PEDIDO")
        pagina.wait_for_timeout(3000)
        recortar(pagina, "cardapio-topo")

        # Hambúrguer avulso, e não combo: no combo o preço sai "A partir de
        # R$ 35,90", e o slide fala de preço fechado.
        pagina.get_by_text("ONE BURGER", exact=True).first.click(force=True)
        pagina.wait_for_timeout(3000)
        recortar(pagina, "turbinar")

        # `Pular` até o fim dos grupos, e então o item entra na sacola. O botão
        # de ação fica na barra de baixo; o filtro de altura evita os cartões.
        for _ in range(8):
            if tocar(pagina, "ADICIONAR R$", 1650, obrigatorio=False):
                break
            tocar(pagina, "PULAR", 1650)
        pagina.wait_for_timeout(2500)
        tocar(pagina, "VER SACOLA", 1650)
        pagina.wait_for_timeout(2500)
        recortar(pagina, "peca-tambem")

        tocar(pagina, "CONTINUAR", 1650)
        pagina.wait_for_timeout(3000)
        # Antes de digitar: é aqui que o totem oferece o cashback, e o recorte
        # precisa do campo vazio — com o número dentro, a arte levaria o
        # telefone de teste.
        recortar(pagina, "cashback-telefone")

        digitar(pagina, TELEFONE)
        tocar(pagina, "CONFIRMAR")
        pagina.wait_for_timeout(3000)
        digitar(pagina, NOME)
        tocar(pagina, "CONFIRMAR")
        pagina.wait_for_timeout(3000)
        digitar(pagina, MESA)
        tocar(pagina, "CONFIRMAR")
        pagina.wait_for_timeout(3500)

        recortar(pagina, "como-sera")
        recortar(pagina, "ir-para-pagamento")

        # A tela do cupom, que só existe porque a rota devolveu a lista. Abrir
        # não aplica nada: aplicar é um POST ao servidor da loja.
        tocar(pagina, "CUPOM DE DESCONTO", 300)
        pagina.wait_for_timeout(2500)
        recortar(pagina, "cupom-modal")
        # E para aqui: o próximo toque é o pagamento.
        navegador.close()


if __name__ == "__main__":
    main()
