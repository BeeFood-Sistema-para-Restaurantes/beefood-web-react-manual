# MEMORIA.md — #65 Taxas das formas de recebimento

## Escopo
Taxa e dias em **Financeiro → Formas Pagamento → Formas de Recebimento
das Vendas**. Prova: débito geral 2,50% D+0, **Visa 2,19%** e
**Mastercard 2,89%**; crédito 3,49% D+30; vale 5% D+15; **duas vendas
Visa** e **uma Mastercard**; detalhe com taxa; **Desempenho → Vendas →
Recebimento** do dia.

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

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-formas-pagamento.png` | setas | Menu + bloco das vendas |
| `02-debito-config.png` | setas | Geral 2,50% e 0 dias |
| `02b-debito-bandeiras.png` | setas | Visa 2,19% e Mastercard 2,89% |
| `03-credito-config.png` | setas | 3,49% e 30 dias |
| `04-vr-config.png` | setas | Vale 5% e 15 dias |
| `05-tabela-configurada.png` | setas | Busca Débito: MC, Visa, geral |
| `06-pdv-pago.png` | setas | #907 Débito Visa Pago + lupa |
| `07-detalhe-pagamento.png` | setas | #907 taxa 2,19%, líquido 13,69, D+0 |
| `08-desemp-recebimento.png` | setas | Resumo do dia: 42,00 × 40,98 |
| `09-desemp-dados.png` | setas | #898 e #907 −2,19%; #899 −2,89% |

Sem borrão.

## Decisões
- Taxas de bandeira diferentes da geral: Visa **2,19%** D+0;
  Mastercard **2,89%** D+0.
- Bandeira **ativa sem taxa** impede a geral de copiar no pagamento
  (vendas antigas #892–#897 e #895 nasceram assim; pagamentos
  **excluídos** para o relatório do dia ficar só com linhas certas).
- Sem exemplo de débito sem bandeira no PDV. Duas Visas (#898 e #907)
  mostram a mesma taxa duas vezes.
- Vale #908 herdou 5% / 15 dias (recebe 14/09). Crédito #894 3,49%
  D+30 (recebe 29/09). Os dois ficam de fora do relatório de hoje.

## Estado deixado no sandbox
- Débito geral: **2,50%**, **0** dias
- Débito Visa: **2,19%**, **0** dias (ativa)
- Débito Mastercard: **2,89%**, **0** dias (ativa)
- Crédito: **3,49%**, **30** dias
- Vale Refeição: **5,00%**, **15** dias; Visa desligada
- Vendas pagas com taxa: **#898** Visa, **#899** Mastercard, **#907**
  Visa, **#908** Vale, **#894** Crédito
- Pagamentos das vendas sujas (#892, #893, #895, #896, #897, #902)
  excluídos (vendas ficaram em aberto — não pagar)
- Cashback Teste Manual: **R$ 5,00** intacto
- #886/#891 não pagas

## Status
Concluído — aguardando publicação.
