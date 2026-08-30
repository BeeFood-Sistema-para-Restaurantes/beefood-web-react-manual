# MEMORIA.md — #64 Desconto formas de recebimento

## Escopo
Desconto / acréscimo no **Cardápio Digital**: aba **Formas Recebimento**
(dinheiro, vale…) e aba **Pagamento Online** (PIX Online). Prova no cardápio
público em tira de três celulares.

Não cobre: contratar PIX Online, cadastrar forma nova, desconto do PDV
(Cadastros), Mercado Pago além de citar que aceita acréscimo.

## Origem
Pedido do dono (30/08/2026): Cardápio Digital → Desconto formas de
recebimento; mostrar no PIX Online e nas formas normais (desconto no
dinheiro + acréscimo no vale alimentação). Zerar tudo antes de estudar;
configurar no manual. Prova no padrão de tira de celulares.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-formas-vazias.png` | setas | Lista sem badge (estado zerado) |
| `02-editor-dinheiro.png` | setas | Desconto em % 5,00 + SALVAR |
| `03-editor-vale.png` | setas | Vale Alelo, Acréscimo 5%, Ativo |
| `04-formas-configuradas.png` | setas | Badges Dinheiro 5% e Vale +5% |
| `05-pix-online.png` | setas | PIX Online Desconto 5% (auto-save) |
| `06-cardapio-pix.png` | pura | Fonte da tira (PIX = R$ 37,05) |
| `07-cardapio-outras.png` | pura | Fonte da tira (lista com os três badges) |
| `08-cardapio-vale.png` | pura | Fonte da tira (Vale = R$ 40,95) |
| `06-cardapio-digital.png` | setas | Três celulares lado a lado |

## Decisões
- Antes de capturar: zeramos Dinheiro 5%, Débito 1%, Crédito +1,12%, PIX
  Online 3% e MP 0,01%. Cadastros / PDV **não** foram mexidos.
- Exemplo redondo: **5%** nos três casos. Combo One Burger **R$ 39,00**
  (batata + Coca), retirada. 5% = **R$ 1,95**.
- Vale: ativamos **Vale - Alelo Refeição / Visa Vale** (já vinculado a
  **Vale Alimentação**). Não criamos forma nova nem renomeamos.
- PIX Online: só **Sem desconto / Desconto % / Desconto R$**. Formas e MP:
  **Sem ajuste** + desconto/acréscimo % ou R$.
- Formas: modal com **SALVAR**. PIX/MP: **auto-save** no combo/campo.
- Cardápio: identificar (15) 99999-8888, **CANCELAR** o cashback de R$ 5
  para a conta do ajuste ficar limpa. **Não finalizar.**
- Não clicar **Retirada** na home (abre Leaflet). Modalidade = **Retirar
  no estabelecimento** dentro da sacola.
- Tira: 3 aparelhos (PIX / outras formas / Vale). Padrão documentado na
  `MEMORIA-GERAL.md`.

## Estado deixado no sandbox
- Dinheiro: Desconto 5%
- Vale Alelo: Ativo, Acréscimo 5%
- PIX Online: Desconto 5%
- Débito, crédito, MP: Sem ajuste
- Cashback do Teste Manual: **R$ 5,00** intacto

## Status
Concluído — aguardando publicação.
