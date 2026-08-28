# MEMORIA.md — #21 Cupom de Desconto (campos + cardápio)

## Escopo
Manual de **funcionamento dos campos** em **CRM → Cupom de Desconto** e de **como o
cliente vê** no cardápio digital (faixa verde + lista ADICIONAR CUPOM).

Não cobre: aplicar/remover no PDV/Delivery/Mesas; estratégias de campanha
(manuais futuros); aba Histórico (tem nome de cliente — não printamos).

## Origem
Novidade 27/08/2026 (`changelog` seq 101). Recorte do dono: um manual de campos
+ cardápio; estratégias depois. Produzido em 28/08/2026 no sandbox BeeFood3.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-lista-cupons.png` | setas | Menu CRM + Adicionar Cupom |
| `02-modal-novo-topo.png` | setas | Código, tipo, valor, validade, dias |
| `03-modal-novo-regras.png` | setas | Canais, regras, SMS |
| `04-modal-avancado.png` | setas | Formas de pagamento + três modos |
| `05-cardapio-banner.png` | setas | Faixa “Você tem N cupons” |
| `06-cardapio-lista-cupons.png` | setas | Digitar código + lista visível |

## Decisões
- Aba **Promoções** do cardápio é **produto em promoção**, não cupom. O manual
  avisa para não confundir.
- Accordion avançado só abre com click via `evaluate` no botão (Playwright
  `get_by_text` não expandia o Radix).
- Não gravamos cupom novo nem ligamos SMS de verdade.
- Não printamos Histórico (PII).
- Aplicar cupom no checkout do cardápio falhou (overlay / visibilidade). A lista
  ADICIONAR CUPOM já mostra o fluxo do cliente.

## Status
Concluído — aguardando publicação. Estratégias de cupom ficam como ideia.
