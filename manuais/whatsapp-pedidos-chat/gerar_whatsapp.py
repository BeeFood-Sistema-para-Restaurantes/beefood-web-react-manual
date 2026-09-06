"""Gera 4 prints de celular estilo WhatsApp com o texto real da API validaFluxo.

Viewport 390x844, device_scale_factor=2 -> 780x1688 (padrao da MEMORIA-GERAL).
"""
from pathlib import Path

from playwright.sync_api import sync_playwright

DIR = Path(__file__).resolve().parent
PURA = DIR / "imagens-puras"
PURA.mkdir(exist_ok=True)

HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=390, initial-scale=1"/>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { width: 390px; height: 844px; overflow: hidden; font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
  .phone { width: 390px; height: 844px; display: flex; flex-direction: column; background: #ECE5DD; }
  .status {
    height: 28px; background: #075E54; color: #fff; display: flex; align-items: center;
    justify-content: space-between; padding: 0 14px; font-size: 12px; font-weight: 600;
  }
  .header {
    height: 56px; background: #075E54; color: #fff; display: flex; align-items: center;
    gap: 10px; padding: 0 10px; box-shadow: 0 1px 2px rgba(0,0,0,.18);
  }
  .back { font-size: 22px; line-height: 1; opacity: .95; }
  .avatar {
    width: 36px; height: 36px; border-radius: 50%; background: #128C7E;
    display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 13px;
  }
  .who { display: flex; flex-direction: column; }
  .who strong { font-size: 15px; font-weight: 600; }
  .who span { font-size: 11px; opacity: .85; }
  .actions { margin-left: auto; letter-spacing: 8px; font-size: 16px; opacity: .9; }
  .chat {
    flex: 1; padding: 10px 10px 8px; overflow: hidden;
    background-color: #ECE5DD;
    background-image: radial-gradient(rgba(0,0,0,.035) 1px, transparent 1px);
    background-size: 18px 18px;
  }
  .row { display: flex; margin: 5px 0; }
  .row.out { justify-content: flex-end; }
  .bub {
    max-width: 82%; padding: 7px 8px 5px 9px; border-radius: 8px;
    font-size: 13.5px; line-height: 1.35; color: #111; white-space: pre-wrap; word-wrap: break-word;
    box-shadow: 0 1px 0.5px rgba(0,0,0,.13);
  }
  .in .bub { background: #fff; border-top-left-radius: 0; }
  .out .bub { background: #DCF8C6; border-top-right-radius: 0; }
  .bub b { font-weight: 700; }
  .time { display: block; text-align: right; font-size: 10.5px; color: #667781; margin-top: 3px; }
  .checks { color: #53bdeb; }
  .inputbar {
    height: 58px; background: #F0F0F0; display: flex; align-items: center; gap: 8px; padding: 8px 8px;
  }
  .pill {
    flex: 1; height: 42px; background: #fff; border-radius: 21px;
    display: flex; align-items: center; padding: 0 14px; color: #667781; font-size: 14px;
  }
  .mic {
    width: 42px; height: 42px; border-radius: 50%; background: #075E54; color: #fff;
    display: flex; align-items: center; justify-content: center; font-size: 18px;
  }
</style>
</head>
<body>
<div class="phone">
  <div class="status"><span>09:14</span><span>5G  100%</span></div>
  <div class="header">
    <div class="back">‹</div>
    <div class="avatar">BF</div>
    <div class="who"><strong>BeeFood</strong><span>online</span></div>
    <div class="actions">📞  ⋮</div>
  </div>
  <div class="chat">
    CHAT
  </div>
  <div class="inputbar">
    <div class="pill">Mensagem</div>
    <div class="mic">●</div>
  </div>
</div>
</body>
</html>
"""


def fmt(text: str) -> str:
    """*negrito* do WhatsApp vira <b>."""
    import re
    t = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    t = re.sub(r"\*([^*]+)\*", r"<b>\1</b>", t)
    return t


def bubble(side: str, text: str, hora: str, ticks: bool = False) -> str:
    tick = ' <span class="checks">✓✓</span>' if ticks else ""
    return (
        f'<div class="row {side}"><div class="bub">{fmt(text)}'
        f'<span class="time">{hora}{tick}</span></div></div>'
    )


PHONES = [
    (
        "w1-iniciar.png",
        [
            bubble("out", "fazer pedido", "09:14", True),
            bubble(
                "in",
                "🛒 Vamos iniciar seu pedido,\n"
                "🔎 Escolha um setor abaixo ou digite um produto para fazer uma busca.\n\n"
                "1 - Burger Artesanais\n"
                "2 - Saladas\n"
                "3 - Sobremesas\n"
                "4 - Pratos Feitos!\n"
                "5 - Sabor Nordestino\n"
                "6 - Pizzas Napopi\n\n"
                "*Dicas:*\n"
                "❌ Cancelar - cancelar o pedido atual\n"
                "⏮ Voltar - voltar uma etapa\n"
                "🤖 Ajuda - ver todas opções",
                "09:14",
            ),
        ],
    ),
    (
        "w2-produto.png",
        [
            bubble("out", "1", "09:15", True),
            bubble(
                "in",
                "🎉 Oba! Encontrei *5* produtos, escolha um para continuar:\n\n"
                "*1 - Baguete de costela* - R$ 35,00\n"
                "*2 - Baguete de frango cremoso* - R$ 26,80\n"
                "*3 - Junior Burger* - R$ 20,00\n"
                "*4 - Smash Salada* - R$ 30,00\n"
                "*5 - Bacon Burguer* - R$ 47,60",
                "09:15",
            ),
            bubble("out", "3", "09:15", True),
            bubble(
                "in",
                "*Qual o ponto da sua carne* ( *1* / *2* )\n"
                "Min.: *1* | Max.: *1*\n\n"
                "*1 - Bem passado*\n"
                "*2 - Ponto pra mais*\n"
                "*3 - Ao ponto*",
                "09:15",
            ),
        ],
    ),
    (
        "w3-carrinho.png",
        [
            bubble("out", "3", "09:16", True),
            bubble(
                "in",
                "*Escolha sua bebida* ( *2* / *2* )\n"
                "Min.: *1* | Max.: *1*\n\n"
                "*1 - Refrigerante Coca-Cola Original 350 Ml*\n"
                "*2 - Coca Cola Zero Lata 350Ml*",
                "09:16",
            ),
            bubble("out", "1", "09:16", True),
            bubble(
                "in",
                "1 (un) Junior Burger - R$ 20,00\n"
                "  ⩺ _1x Ao ponto_\n"
                "  ⩺ _1x Refrigerante Coca-Cola Original 350 Ml_\n"
                "Total por unidade:  *R$ 20,00*\n\n"
                "🛒 Quantas unidades deseja adicionar ao carrinho?",
                "09:16",
            ),
            bubble("out", "1", "09:16", True),
            bubble(
                "in",
                "🛒✔ produto *Junior Burger*, foi adicionado ao carrinho.\n\n"
                "Como deseja continuar?\n"
                "1 - Continuar pedido\n"
                "2 - Visualizar pedido\n"
                "3 - Finalizar pedido",
                "09:16",
            ),
        ],
    ),
    (
        "w4-resumo.png",
        [
            bubble("out", "3", "09:17", True),
            bubble(
                "in",
                "🙏 Tudo certo, vamos iniciar a finalização do seu pedido,\n"
                "Como prefere a entrega do pedido?\n\n"
                "1 - Entrega\n"
                "2 - Entrega - Minha Localização\n"
                "3 - Retirada",
                "09:17",
            ),
            bubble("out", "3", "09:17", True),
            bubble(
                "in",
                "Olá Testes 👋,\n"
                "seu pedido ficou assim:\n\n"
                "*▶ Detalhes*\n"
                "1 (un) Junior Burger - R$ 20,00\n"
                "  ⩺ _1x Ao ponto_\n"
                "  ⩺ _1x Refrigerante Coca-Cola Original 350 Ml_\n"
                "Subtotal: R$ 20,00\n"
                "*Total:* R$ 20,00\n"
                "*▶ Entrega*\n"
                "Retirar em: Rua Caramuru, 108 — Vila Leão, Sorocaba/SP\n"
                "*▶ Pagamento*\n"
                "Dinheiro\n"
                "-------------------\n"
                "*1 - Confirmar Pedido*\n"
                "*2 - Cancelar Pedido*",
                "09:18",
            ),
        ],
    ),
]


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 390, "height": 844},
            device_scale_factor=2,
            is_mobile=True,
            has_touch=True,
            locale="pt-BR",
        )
        page = context.new_page()
        for nome, rows in PHONES:
            html = HTML.replace("CHAT", "\n".join(rows))
            page.set_content(html, wait_until="domcontentloaded")
            page.wait_for_timeout(400)
            page.screenshot(path=str(PURA / nome), type="png")
            print("   ->", nome, page.viewport_size)
        browser.close()
    print("ok mockups")


if __name__ == "__main__":
    main()
