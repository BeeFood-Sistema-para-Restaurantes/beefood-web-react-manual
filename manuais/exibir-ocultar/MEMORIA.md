# MEMORIA.md — #68 Exibir / Ocultar

## Escopo
Esconder produto por tabela (dias, horário, canais) sem apagar o
cadastro. Prova no cardápio público: Brownie some da Sobremesas.

Não cobre: Preço Programado, Rodízio, apagar produto, reordenar.

## Origem
Pedido do dono (30/08/2026): teste de campo em Exibir/Ocultar **e**
Preço Programado com resultado no cardápio digital (cache até 5 min).
Se algum caso passasse, fazer os dois manuais do início ao fim.

Teste: **os dois passaram**. Hide ~2 min; preço ~1 min.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-lista-exibir-ocultar.png` | setas | Lista + menu + card Ocultar Brownie |
| `02-modal-config.png` | setas | Ocultar Item, Ativo, canais, dias |
| `03-modal-produtos.png` | setas | Brownie na aba Produtos |
| `04-cel-antes.png` | pura | Fonte da tira — Brownie visível |
| `05-cel-depois.png` | pura | Fonte da tira — Brownie oculto |
| `04-cardapio-digital.png` | setas | Dois celulares: antes × depois |

## Decisões
- Produto: **Brownie** (Sobremesas, R$ 11,90). Não usar Combo One
  Burger (cashback #20).
- Tabela: **Ocultar Brownie (manual)**, canais Delivery + Presencial
  + Cardápio Digital, 7 dias (horário vazio = dia inteiro).
- Botão da tela: **Nova Tabela (F1)** — `filter(has_text="Novo")` não
  casa. Comportamento fixo **Ocultar Item** (`ocultar=0`).
- Aba Produtos numa tabela nova **salva a config sozinha**.
- “Antes” da tira: desativamos a tabela, esperamos o Brownie voltar
  (até 5 min), print, **reativamos**, esperamos sumir de novo.
- Tira: 2 aparelhos, padrão `montar_celulares` (#19/#20/#64).
- Cache do menu público: o dono pediu até **5 minutos** (outros
  manuais falavam ~1 min).

## Estado deixado no sandbox
- Tabela **Ocultar Brownie (manual)** **ativa** — Brownie oculto no
  cardápio digital.
- Tabelas antigas intactas: `Tabela 18/06 18:06` (0 produtos, 0d),
  dois `testes` (0d). Não apagar.
- Preço Programado do #69 e cashback/descontos/taxas/lançamentos
  intactos.

## Status
Concluído — aguardando publicação.
