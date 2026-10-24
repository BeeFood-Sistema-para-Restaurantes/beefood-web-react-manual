"""Captura a digitalização de cardápio por imagem (Cardápio → Copiar de Imagem) para o #130.

A tela é um aplicativo separado (`foto-cardapio.beefood.com.br`) carregado dentro de um iframe
do painel, como o cardápio público do #125: o código não está no `beefood-web-react`, então tudo
o que o manual afirma sobre ela saiu da observação do produto no ar.

O insumo é um **cardápio impresso fictício** desenhado aqui mesmo, por três motivos: ele não tem
dado de ninguém, o resultado da extração é previsível (sabe-se de antemão o que a IA deveria
achar) e o script fica reproduzível sem depender de arquivo solto numa pasta.

Este script cadastra produtos de verdade no fim — autorizado pelo dono em 23/10/2026. A ordem
dos cliques segue a técnica do ensaio feita antes: o fluxo já havia sido percorrido inteiro até
o diálogo *Confirmar envio*, sem confirmar, para saber o que cada passo mostra.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "painel-entregador"))

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright
from beefood import abrir, after_click, limpar_tela

AQUI = Path(__file__).resolve().parent
PURAS = AQUI / "imagens-puras"
CARDAPIO_FOTO = Path("/tmp/cardapio-impresso-ficticio.png")

FONTES = (
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
)
FONTES_FINAS = (
    "/usr/share/fonts/truetype/croscore/Arimo-Regular.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
)

ITENS = [
    ("CAFÉS", [
        ("Café Expresso", "50ml, grão arábica torrado na casa", "6,50"),
        ("Café com Leite", "200ml, leite vaporizado", "9,00"),
        ("Cappuccino Italiano", "200ml, canela e cacau", "12,50"),
    ]),
    ("DOCES DA CASA", [
        ("Bolo de Cenoura com Chocolate", "fatia generosa, cobertura cremosa", "11,00"),
        ("Pão de Mel Recheado", "doce de leite, banhado no chocolate", "8,50"),
        ("Torta de Limão", "fatia, massa amanteigada e merengue", "14,00"),
    ]),
]


def fonte(tamanho, finas=False):
    for caminho in (FONTES_FINAS if finas else FONTES):
        if Path(caminho).exists():
            return ImageFont.truetype(caminho, tamanho)
    return ImageFont.load_default()


def montar_cardapio_impresso():
    """Desenha um cardápio impresso plausível — é o que entra como 'foto' na digitalização."""
    largura, altura = 1000, 1300
    img = Image.new("RGB", (largura, altura), (252, 247, 237))
    d = ImageDraw.Draw(img)

    d.rectangle([40, 40, largura - 40, altura - 40], outline=(176, 142, 94), width=4)
    d.text((largura / 2, 110), "CANTINHO DO CAFÉ", fill=(70, 48, 26), font=fonte(54), anchor="mm")
    d.text((largura / 2, 165), "cafeteria e confeitaria", fill=(140, 115, 86), font=fonte(26, True), anchor="mm")
    d.line([(300, 200), (700, 200)], fill=(176, 142, 94), width=2)

    y = 265
    for titulo, itens in ITENS:
        d.text((100, y), titulo, fill=(150, 60, 40), font=fonte(36))
        y += 70
        for nome, descricao, preco in itens:
            d.text((120, y), nome, fill=(50, 40, 30), font=fonte(30))
            preco_txt = f"R$ {preco}"
            caixa = d.textbbox((0, 0), preco_txt, font=fonte(30))
            d.text((largura - 130 - (caixa[2] - caixa[0]), y), preco_txt, fill=(50, 40, 30), font=fonte(30))
            y += 42
            d.text((120, y), descricao, fill=(130, 118, 104), font=fonte(23, True))
            y += 62
        y += 40

    d.text((largura / 2, altura - 90), "Rua das Flores, 123  •  todos os dias, 8h às 19h",
           fill=(150, 130, 108), font=fonte(22, True), anchor="mm")
    img.save(CARDAPIO_FOTO)
    print("cardápio fictício:", CARDAPIO_FOTO, img.size)


def quadro_foto(page):
    """O iframe do aplicativo de digitalização."""
    for f in page.frames:
        if "foto-cardapio" in f.url:
            return f
    raise RuntimeError("iframe foto-cardapio não encontrado")


def esperar_extracao(quadro, page, limite=60):
    for i in range(limite):
        page.wait_for_timeout(5000)
        texto = quadro.locator("body").inner_text()
        if "Processando" not in texto:
            print(f"  extração terminou em ~{(i + 1) * 5}s")
            return
    raise RuntimeError("a extração não terminou no tempo esperado")


montar_cardapio_impresso()

with sync_playwright() as p:
    browser, ctx, page = abrir(p, "/copiar-imagem", viewport=(1440, 1000), escala=1.5)
    after_click(page, 9000)
    limpar_tela(page)
    quadro = quadro_foto(page)

    # 8. O arquivo escolhido, antes de continuar: é aqui que se vê o que a tela aceita.
    quadro.locator('input[type="file"]').first.set_input_files(str(CARDAPIO_FOTO))
    after_click(page, 4000)
    page.screenshot(path=str(PURAS / "08-digitalizar-arquivo.png"))
    print("08 arquivo escolhido")

    quadro.locator("button").filter(has_text="Continuar").first.click()
    esperar_extracao(quadro, page)
    after_click(page, 4000)

    # 9. O que a IA leu, em formato de cardápio, para o cliente conferir antes de cadastrar.
    page.screenshot(path=str(PURAS / "09-digitalizar-revisao.png"))
    print("09 revisão")
    print("texto da revisão:\n", quadro.locator("body").inner_text()[:900])

    # 10. O assistente corrigindo um item por frase — é o que esta tela tem de diferente.
    campo = quadro.locator('input[placeholder*="adicione"], textarea[placeholder*="adicione"]')
    if campo.count():
        campo.first.fill("Mude o preço do Café Expresso para R$ 7,50")
        campo.first.press("Enter")
        for i in range(24):
            page.wait_for_timeout(5000)
            if "7,50" in quadro.locator("body").inner_text():
                print(f"  assistente respondeu em ~{(i + 1) * 5}s")
                break
        after_click(page, 3000)
        page.screenshot(path=str(PURAS / "10-digitalizar-assistente.png"))
        print("10 assistente")
    else:
        print("!! campo do assistente não encontrado")

    # 11. O aviso antes do cadastro — o único ponto sem volta deste caminho.
    quadro.locator("button").filter(has_text="Continuar").last.click()
    after_click(page, 5000)
    page.screenshot(path=str(PURAS / "11-digitalizar-confirmar.png"))
    print("11 confirmação")

    confirmar = quadro.locator("button").filter(has_text="Confirmar")
    confirmar.last.click()
    print(">> cadastro confirmado; acompanhando")
    for i in range(40):
        page.wait_for_timeout(5000)
        texto = quadro.locator("body").inner_text()
        print(f"  {(i + 1) * 5:3d}s", texto.replace("\n", " | ")[:160])
        if "sucesso" in texto.lower() or "cadastrad" in texto.lower() or "conclu" in texto.lower():
            break
    after_click(page, 4000)
    page.screenshot(path=str(PURAS / "12-digitalizar-resultado.png"))
    print("12 resultado")
    (Path("/tmp") / "digitalizar-final.txt").write_text(quadro.locator("body").inner_text(), encoding="utf-8")
    browser.close()
print("fim")
