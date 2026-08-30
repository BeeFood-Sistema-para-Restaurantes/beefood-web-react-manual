# MEMORIA.md — #20 Cashback operar

## Escopo
Histórico, saldo por cliente, **ajuste manual (Adicionar e Remover)**,
fila da madrugada, **Usar cashback** no PDV (modal aberto e **cancelado**) e
saldo na **sacola** do cardápio digital (fechamento).

## Origem
Item #20 do checklist. Produzido 29/08/2026 e refeito 30/08/2026 no sandbox
BeeFood3, na sequência do #19 — telefone de teste trocado para valor realista.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-historico.png` | setas | Filtro `99999` → Teste Manual R$ 5 |
| `02-saldo-clientes.png` | setas | Cartão (15) 99999-8888 / R$ 5,00 |
| `03-detalhe-cliente.png` | setas | Extrato: Ajuste manual +R$ 5,00 |
| `04-modal-ajuste.png` | setas | Adicionar R$ 5,00 + motivo (não gravado de novo) |
| `05-modal-remover.png` | setas | Remover R$ 1,00 + motivo (não gravado) |
| `06-fila-processamento.png` | setas | Pendente / sucesso / erro |
| `07-pdv-usar-cashback.png` | setas | Venda #891, Teste Manual, saldo R$ 5 |
| `08-pdv-modal-aplicar.png` | setas | Aplicar R$ 5,00 (não confirmado) |
| `08-cardapio-checkout-saldo.png` | pura | Fonte da tira (saldo R$ 5) |
| `09-cardapio-checkout-usar.png` | pura | Fonte da tira (usando R$ 5, total R$ 34) |
| `09-cardapio-checkout.png` | setas | Dois celulares: saldo + uso |

## Decisões
- Telefone de teste **(15) 99999-8888** / **Teste Manual** / **R$ 5,00**.
  O crédito de R$ 5 foi inserido pelo dono (ajuste manual). Não usamos mais
  o (11) 11111-1122 / Bruno XXX / R$ 1.233,21.
- Histórico filtrado por `99999`: só o cliente de teste — sem PII de outros.
- Adicionar e Remover: formulários preenchidos e **cancelados**, para não
  alterar o R$ 5,00. O extrato já prova o crédito real.
- PDV: One Burger R$ 14,00, máximo aplicável R$ 5,00. **Aplicar (F2) não
  foi clicado.** Venda #891 ficou em andamento (não paga).
- Checkout do cardápio: Combo One Burger R$ 39, **Retirar no estabelecimento**
  (não clicar Retirada na home). Sistema aplica **R$ 5,00** sozinho
  (total **R$ 34,00**). **CANCELAR** mostra o saldo de novo.
  **Finalizar não foi tocado.**

## Status
Concluído — aguardando publicação.
