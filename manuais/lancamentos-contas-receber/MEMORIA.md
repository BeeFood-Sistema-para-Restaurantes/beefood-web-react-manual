# MEMORIA.md — #67 Lançamentos: contas a receber

## Escopo
O receber que a **venda paga** já lança sozinha + uma **receita
extra** à mão + a aba **Todos lançamentos**. Prova: venda **#915**
Débito Visa (original 14,00 / líquido **13,69** / taxa **2,19%**)
e **Patrocínio da festa junina** R$ 200 Pix, já recebido,
categoria **Outras Receitas**.

Não cobre: despesa (#66), Relatório Recebimentos, DRE, cadastros,
taxa da maquininha (só o efeito — o valor nasce líquido).

## Origem
Pedido do dono (30/08/2026) depois do merge do #65: fechar o par
**#66 / #67**.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-receber-vendas.png` | setas | Aba receber + #915 R$ 13,69 |
| `02-detalhe-venda.png` | setas | Original 14,00 / líquido 13,69 / 2,19% |
| `03-receita-extra.png` | setas | Patrocínio 200 Pix, Recebido, Outras Receitas |
| `04-lista-receita.png` | setas | Patrocínio recebido na lista |
| `05-todos.png` | setas | Aba Todos filtrada por Aluguel |

Sem borrão. 5 imagens. Print 04 ficou com o checkbox da linha
marcado (barra de lote no rodapé) — não ensina ação em lote.

## Decisões
- Venda paga **já** vira receber: categoria **Receita de Pedidos**,
  valor = líquido da taxa #65. Não lançar de novo.
- Modal da venda: lápis `button.h-8.w-8` (não o checkbox).
- Receita manual: categoria fixa **Outras Receitas** (campo
  desabilitado).
- Formas da receita extra = topo de Formas Pagamento.
- Aba Todos: busca pela descrição; o filtro **Este mês** esconde
  a parcela 2/2 do #66.

## Estado deixado no sandbox
- Venda **#915** intacta (receber automático)
- **Patrocínio da festa junina** — receita R$ 200 Pix, **recebida**
  em 30/08/2026, categoria Outras Receitas
- Lançamentos do #66 permanecem
- Cashback Teste Manual: **R$ 5,00** intacto
- #886/#891 não pagas

## Status
Concluído — aguardando publicação.
