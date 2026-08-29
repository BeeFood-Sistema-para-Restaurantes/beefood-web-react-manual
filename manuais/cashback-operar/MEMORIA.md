# MEMORIA.md — #20 Cashback operar

## Escopo
Histórico, saldo por cliente, ajuste manual (modal aberto e **cancelado**),
fila da madrugada, **Usar cashback** no PDV (modal aberto e **cancelado**) e
Perfil no cardápio digital.

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
| `08-cardapio-perfil.png` | setas | Faixa + Perfil + Programa de fidelidade |

## Decisões
- Telefone fake **(11) 11111-1122** em busca, PDV e cardápio.
- Histórico: blur nas linhas de Top clientes que não são o Bruno XXX.
- PDV: One Burger R$ 14,00, cliente selecionado; **Aplicar (F2) não foi clicado**.
- Fila tem 236 erros (vendas canceladas) — serve de exemplo, não limpamos.
- Checkout do cardápio (aplicar saldo no pedido) não foi fotografado: o clique
  em Retirada abriu o modal do mapa e o “Programa de fidelidade” pediu senha.
  A home + Perfil mostram o caminho do cliente; o aplicar no painel está no PDV.

## Status
Concluído — aguardando publicação. Borrão de PII aplicado na **pura** e na tratada.
