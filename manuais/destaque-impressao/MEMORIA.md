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
- Conferido pela API (`cardapio2/cardapio` e `cardapio2/grupoOpcoes`):
  **11 produtos** marcados (refrigerantes e sucos) e **24 opções** distintas
  (reduções `Sem …`, molhos e as bebidas dentro dos combos).
- Lote: **Cardápio → Produtos → Bebidas → Editar em Lote** etapa 2
  (fotografado com o campo marcado em **Sim**; **não processado**).
- Pedido de prova no PDV: venda **#968** / pedido **32** /
  `preVendaID` 59204137. **Combo One Burger** R$ 39,00 (Coca +
  Sem Maionese Verde) + **Mozza Sticks + Molho** R$ 35,90
  (Molho verde) = **R$ 74,15** (dinheiro). Sem taxa de serviço.

## Imagens

| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-cadastro-produto.png` | setas | Cadastro da Coca, switch abaixo da Descrição |
| `02-cadastro-complemento.png` | setas | Cadastro do Molho verde, mesmo switch |
| `03-editar-lote.png` | setas | Etapa 2 do lote com o campo marcado |
| `04-detalhe-venda.png` | moldura | Venda #968 (contexto dos itens do pedido) |
| `05-cupom-pedido.png` | setas | Cupom do cliente com linhas em destaque |
| `06-cupom-cozinha.png` | setas | Ficha da cozinha com as mesmas linhas |
| `07-cupom-delivery.png` | setas | Venda **936** (delivery / Cardápio Digital) com a Coca destacada |

## Decisões

- Não gravar lote nem alterar flags (já estavam ligadas).
- Um molho extra (**Mozza Sticks + Molho**) porque o Combo One Burger
  tem Bebidas e Redução, mas não tem grupo de molho.
- Destaque é por item (produto ou opção), não pelo combo pai.
- O manual **não ensina a imprimir** (pedido do dono): os cupons entram
  apenas como resultado prático. A tela da venda ficou só como contexto,
  sem setas nos botões de impressora/cozinha.
- Anotação (2ª rodada, pedido do dono): setas **curtas** e horizontais,
  coordenadas em **pixels** no `annotate.py` (não mais frações estimadas).
  Nos cupons o `pad_right` cria uma faixa branca à direita para os números,
  então a seta encosta na borda da faixa escura sem cruzar o texto.

## SEO (13/09, pedido do dono)

Base: a discussão **Destaque de bebida** (Restaurante Figueriana #41686,
12/05/2026, 24 empresas votando, resposta oficial *Planejada*). O vocabulário
real dos comentários entrou no manual: *destacar bebidas*, *destacar produtos
no impresso*, *esquecimento de bebida na bag*, *grifar o refrigerante com
canetinha*, *durex colorido na comanda*, *fundo preto nas bebidas*.

- H1 e os H2 das partes 1 a 3 passaram para a forma de busca
  (“Como destacar…”). Título curto do menu segue **Destaque na impressão**.
- **Perguntas frequentes** (pergunta completa, padrão do #33/#86) cobrem as
  dúvidas do tópico, incluindo as duas que **não** existem no produto:
  aviso **TEM BEBIDA no rodapé** (não existe; o que existe é a linha com
  fundo + o Texto Padrão do #98) e destaque **só no delivery** (não existe;
  o interruptor é único por item).
- **Problemas comuns** com as três armadilhas reais: `SALVAR E SAIR`, lote
  que nasce em **Não** e a bebida do combo, que é **opção** (complemento).
- Prova nova do delivery (imagem 07): venda **936** de 02/09, origem
  **Cardápio Digital**, Combo One Burger com **Coca Cola 350ml** destacada.
  Escolhida por ser `tipo=DELIVERY` com bebida marcada; o sandbox **não** tem
  venda de delivery com `tipoPedido=DELIVERY` (entrega) e bebida marcada — as
  candidatas são balcão/retirada, e a de entrega com bebida (959) está
  cancelada. Nenhuma venda nova foi criada nesta rodada.
- Nessa imagem a linha **Obs** também sai invertida (é o destaque da
  observação, `obsNegrito`). O manual explica, para não parecer erro.

## Status

Concluído — aguardando publicação.
