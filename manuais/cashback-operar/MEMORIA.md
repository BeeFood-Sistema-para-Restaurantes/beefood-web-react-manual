# MEMORIA.md — #20 Cashback operar

## Escopo
Histórico, saldo por cliente, ajuste manual (modal aberto e **cancelado**),
fila da madrugada, **Usar cashback** no PDV (modal aberto e **cancelado**) e
saldo na **sacola** do cardápio digital (fechamento).

## Origem
Item #20 do checklist. Produzido 29/08/2026 no sandbox BeeFood3, na sequência
do #19.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-historico.png` | setas | Resumo + gráfico; PII extra borrada |
| `02-saldo-clientes.png` | setas | Filtro `11111` → só Bruno XXX |
| `03-detalhe-cliente.png` | setas | Extrato R$ 1.233,21 (ajuste manual) |
| `04-modal-ajuste.png` | setas | Adicionar saldo (não gravado) |
| `05-fila-processamento.png` | setas | 259 na fila; pendente / sucesso / erro |
| `06-pdv-usar-cashback.png` | setas | Venda #886, cliente Bruno XXX |
| `07-pdv-modal-aplicar.png` | setas | Aplicar R$ 14,00 (não confirmado) |
| `08-cardapio-checkout-saldo.png` | pura | Fonte da tira (saldo) |
| `09-cardapio-checkout-usar.png` | pura | Fonte da tira (usando) |
| `08-cardapio-checkout.png` | setas | Dois celulares: saldo + uso |

## Decisões
- Telefone fake **(11) 11111-1122** em busca, PDV e cardápio.
- Histórico: blur nas linhas de Top clientes que não são o Bruno XXX.
- PDV: One Burger R$ 14,00, cliente selecionado; **Aplicar (F2) não foi clicado**.
- Fila tem 236 erros (vendas canceladas) — serve de exemplo, não limpamos.
- Checkout do cardápio validado com telefone fake: Combo One Burger R$ 39,
  **Retirar no estabelecimento** (não clicar Retirada na home — abre o mapa).
  O sistema **aplica o cashback sozinho**; **CANCELAR** mostra
  **R$ 1.233,21 de cashback disponível** + **Usar**. **Finalizar não foi tocado**.
  Cupom fica bloqueado enquanto o cashback está ativo.

## Status
Concluído — aguardando publicação. Borrão de PII aplicado na **pura** e na tratada.
