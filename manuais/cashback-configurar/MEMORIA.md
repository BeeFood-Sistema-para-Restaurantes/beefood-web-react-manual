# MEMORIA.md — #19 Cashback configurar

## Escopo
Ativar o programa, validade, saldo mínimo, formas, canais, % fixo ou por dia,
exceções, aviso da tela antiga e **o que o cliente vê** no cardápio (faixa +
identificar com telefone fake).

Não cobre histórico, ajuste, fila nem aplicar na venda (#20).

## Origem
Itens #19 do checklist (aprovado 19/08/2026). Produzido 29/08/2026 no sandbox
BeeFood3. Artigo antigo do ajuda.beefood (2021) ficou superado pela tela CRM.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-crm-cashback-config.png` | setas | Menu + ativar + validade |
| `02-limites-canais.png` | setas | Validade, formas, mínimo, canais |
| `03-percentual-dias.png` | setas | % por dia, aviso, exceções |
| `04-cardapio-digital-redirect.png` | setas | Aviso “mudou de lugar” |
| `05-cardapio-banner.png` | setas | Faixa no cardápio público |
| `06-cardapio-identificar.png` | setas | WhatsApp (11) 11111-1122 |

## Decisões
- Não alteramos a config (já estava ativo, 3% todos os dias, 35 dias, todos os canais).
- Telefone de teste: **(11) 11111-1122** / Bruno XXX. Todos os eventos do cardápio.
- Cache do cardápio: até 1 min — a faixa já estava visível, sem precisar esperar.
- “Programa de fidelidade” no Perfil pede senha da conta; não entramos. A faixa +
  identificar bastam para o #19.
- Auto-save: nenhum switch foi invertido.

## Status
Concluído — aguardando publicação.
