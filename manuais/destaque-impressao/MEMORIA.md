# MEMORIA.md — #99 Destaque na impressão

## Escopo

Campo **Destaque na impressão** (`destaqueImpressao`) no cadastro de produto e
de complemento, no **Editar em Lote**, e o efeito no **Cupom Pedido** e no
**Cupom Cozinha** (fundo escuro / letra clara).

Não cobre: o switch **Destaque** do cardápio digital, KDS, fichas do PDV.

## Origem

Pedido do dono (13/09/2026): funcionalidade nova no `beefood-web-react`
(exigiu `git pull`). Mostrar cadastro produto/complemento, lote, impressão
do pedido e da cozinha. A empresa de teste já tinha **todas as bebidas,
redução e molhos** ligados.

## Cenário

- Conta: `contato@beefood.com.br` (BeeFood3).
- Produto de cadastro: **Coca Cola 350ml** (setor Bebidas) — switch já ON.
- Complemento de cadastro: **Molho verde** — switch já ON.
- Lote: **Cardápio → Produtos → Bebidas → Editar em Lote** etapa 2
  (fotografado com o campo marcado em **Sim**; **não processado**).
- Pedido de prova no PDV: **Combo One Burger** (Coca Cola 350ml +
  Sem Maionese Verde) + **Mozza Sticks + Molho** (Molho verde).

## Imagens

| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-cadastro-produto.png` | setas | Cadastro da Coca, switch abaixo da Descrição |
| `02-cadastro-complemento.png` | setas | Cadastro do Molho verde, mesmo switch |
| `03-editar-lote.png` | setas | Etapa 2 do lote com o campo marcado |
| `04-detalhe-venda.png` | setas | Venda do combo + molho e ícones de impressão |
| `05-cupom-pedido.png` | setas | Cupom do cliente com linhas em destaque |
| `06-cupom-cozinha.png` | setas | Ficha da cozinha com as mesmas linhas |

## Decisões

- Não gravar lote nem alterar flags (já estavam ligadas).
- Um molho extra (**Mozza Sticks + Molho**) porque o Combo One Burger
  tem Bebidas e Redução, mas não tem grupo de molho.
- Destaque é por item (produto ou opção), não pelo combo pai.

## Status

Em execução.
