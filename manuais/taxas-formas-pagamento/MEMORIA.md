# MEMORIA.md — #65 Taxas das formas de recebimento

## Escopo
Taxa e dias em **Financeiro → Formas Pagamento → Formas de Recebimento
das Vendas**. Prova: débito geral 2,50% D+0, **Visa 2,19%** e
**Mastercard 2,89%**; crédito 3,49% D+30; vale 5% D+15; **duas vendas
Visa** e **uma Mastercard**; detalhe com taxa; **Desempenho → Vendas →
Resumo** do dia (não é Vendas → Recebimento).

Não cobre: cadastro novo de forma, TEF, desconto do cardápio (#64),
ajuste de sacola/PDV, DRE, Lançamentos. Sem exemplo de venda de débito
**sem bandeira** — se a bandeira está configurada, a venda preenche a
bandeira.

## Origem
Pedido do dono (30/08/2026) + follow-up: bandeiras fantasmas (ativas
sem taxa) sujavam a interpretação. Depois: ajuste no servidor para
taxa sem bandeira calcular sozinha — **não documentar** venda sem
bandeira no débito. Trocar por **mais uma venda da mesma bandeira**
(2ª Visa). Relatório só do dia, sem ensinar o filtro no texto. Sem
borrão.

Correção do dono: o relatório certo é **Vendas → Resumo** com a data
de hoje. **Vendas → Recebimento** lista o que **cai** no dia (só
débito D+0). O Resumo lista o que **vendeu** no dia: faturado de
todas as formas; realizado só do que entra na conta hoje.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-formas-pagamento.png` | setas | Menu + bloco das vendas |
| `02-debito-config.png` | setas | Geral 2,50% e 0 dias |
| `02b-debito-bandeiras.png` | setas | Visa 2,19% e Mastercard 2,89% |
| `03-credito-config.png` | setas | 3,49% e 30 dias |
| `04-vr-config.png` | setas | Vale 5% e 15 dias |
| `05-tabela-configurada.png` | setas | Busca Débito: MC, Visa, geral |
| `06-pdv-pago.png` | setas | #915 Débito Visa Pago + lupa |
| `07-detalhe-pagamento.png` | setas | #915 taxa 2,19%, líquido 13,69, D+0 |
| `07b-detalhe-mastercard.png` | setas | #916 taxa 2,89%, líquido 13,60, D+0 |
| `07c-detalhe-credito.png` | setas | #917 taxa 3,49%, líquido 13,92, D+30 |
| `07d-detalhe-vale.png` | setas | #914 taxa 5%, líquido 13,30, D+15 |
| `08-desemp-resumo.png` | setas | Vendas → Resumo: 183,26 × 95,56 |
| `09-desemp-pagamentos.png` | setas | Débito 98/95,56; crédito 43,26/0; vale 42/0 |

Sem borrão. 13 imagens.

## Decisões
- Taxas de bandeira diferentes da geral: Visa **2,19%** D+0;
  Mastercard **2,89%** D+0.
- Bandeira **ativa sem taxa** impede a geral de copiar no pagamento
  (vendas antigas #892–#897 e #895 nasceram assim; pagamentos
  **excluídos** para o relatório do dia ficar só com linhas certas).
- Sem exemplo de débito sem bandeira no PDV. Duas Visas mostram a
  mesma taxa duas vezes.
- Relatório do dia = **Vendas → Resumo**. Faturado de débito, crédito
  e vale. Realizado só o débito (D+0). Crédito e vale ficam com
  realizado **R$ 0,00** até a data de recebimento.

## Estado deixado no sandbox
- Débito geral: **2,50%**, **0** dias
- Débito Visa: **2,19%**, **0** dias (ativa)
- Débito Mastercard: **2,89%**, **0** dias (ativa)
- Crédito: **3,49%**, **30** dias
- Vale Refeição: **5,00%**, **15** dias; Visa desligada
- Vendas pagas com taxa (hoje): **#915** Visa, **#916** Mastercard,
  **#917** Crédito, **#914** Vale (e outras do mesmo dia: #894, #898,
  #899, #907, #908, #911–#913)
- Pagamentos das vendas sujas (#892, #893, #895, #896, #897, #902)
  excluídos (vendas ficaram em aberto — não pagar)
- Cashback Teste Manual: **R$ 5,00** intacto
- #886/#891 não pagas

## Status
Concluído — aguardando publicação.
