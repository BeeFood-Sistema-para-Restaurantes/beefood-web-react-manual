# MEMORIA.md — #19 Cashback configurar

## Escopo
Ativar o programa, validade, saldo mínimo, formas, canais, % fixo ou por dia,
exceções, aviso da tela antiga e **o que o cliente vê** no cardápio (faixa +
identificar com telefone de teste).

Não cobre histórico, ajuste, fila nem aplicar na venda (#20).

## Origem
Itens #19 do checklist (aprovado 19/08/2026). Produzido 29/08/2026 e
telefone de teste atualizado em 30/08/2026 no sandbox BeeFood3.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-crm-cashback-config.png` | setas | Menu + ativar + validade |
| `02-limites-canais.png` | setas | Validade, formas, mínimo, canais |
| `03-percentual-dias.png` | setas | % por dia, aviso, exceções |
| `04-cardapio-digital-redirect.png` | setas | Aviso “mudou de lugar” |
| `05-cardapio-banner.png` | pura | Fonte da tira (home) |
| `06-cardapio-identificar.png` | pura | Fonte da tira (identificar) |
| `05-cardapio-digital.png` | setas | Dois celulares lado a lado |

## Decisões
- Não alteramos a config (já estava ativo, 3% todos os dias, 35 dias, todos os canais).
- Telefone de teste: **(15) 99999-8888** / Teste Manual. Digite 11 dígitos
  `15999998888` no `input[type=tel]`.
- Cache do cardápio: até 1 min — a faixa já estava visível.
- “Programa de fidelidade” no Perfil pede senha da conta; não entramos. A faixa +
  identificar bastam para o #19; o saldo no fechamento da sacola está no #20.
- Auto-save: nenhum switch foi invertido.

## Status
Concluído — aguardando publicação.
