# MEMORIA.md — #65 Taxas das formas de recebimento

## Escopo
Taxa e dias em **Financeiro → Formas Pagamento → Formas de Recebimento
das Vendas**. Prova: débito geral 2,50% D+0, **Visa 2,19%** e
**Mastercard 2,89%**; crédito 3,49% D+30; vale 5% D+15; uma venda Visa
e uma Mastercard; detalhe com taxa; **Desempenho → Vendas →
Recebimento** do dia.

Não cobre: cadastro novo de forma, TEF, desconto do cardápio (#64),
ajuste de sacola/PDV, DRE, Lançamentos.

## Origem
Pedido do dono (30/08/2026) + follow-up: bandeiras fantasmas (ativas
sem taxa) sujavam a interpretação. Ajustar: no vale, só remover a
Visa fantasma; no débito, configurar Visa e Mastercard de verdade,
vender cada bandeira e enriquecer o manual. Sem borrão. Relatório só
do dia, sem ensinar o filtro no texto.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-formas-pagamento.png` | setas | Menu + bloco das vendas |
| `02-debito-config.png` | setas | Geral 2,50% e 0 dias |
| `02b-debito-bandeiras.png` | setas | Visa 2,19% e Mastercard 2,89% |
| `03-credito-config.png` | setas | 3,49% e 30 dias |
| `04-vr-config.png` | setas | Vale 5% e 15 dias |
| `05-tabela-configurada.png` | setas | Busca Débito: MC, Visa, geral |
| `06-pdv-pago.png` | setas | #898 Débito Visa Pago + lupa |
| `07-detalhe-pagamento.png` | setas | #898 taxa 2,19%, líquido 13,69, D+0 |
| `08-desemp-recebimento.png` | setas | Resumo do dia: 84,00 × 83,29 no débito |
| `09-desemp-dados.png` | setas | #898 −2,19% e #899 −2,89% |

Sem borrão.

## Decisões
- Taxas de bandeira diferentes da geral para a prova ficar óbvia:
  Visa **2,19%** D+0; Mastercard **2,89%** D+0.
- Bandeira **ativa sem taxa** impede a geral de copiar no pagamento
  (#892, #893, #895 nasceram assim).
- Vale: switch Visa **desligado**. A lista ainda pode mostrar uma
  linha Visa com travessão (registro antigo `formaPagamentoConfigID`
  11862); o GET não traz mais `ativo:true`. Não achamos DELETE da
  linha. Switch off + sem taxa na venda nova é o que o produto
  oferece.
- Vendas com taxa herdada: **#898 Visa** (14,00 → 13,69) e **#899
  Mastercard** (14,00 → 13,60). Crédito **#894** continua com 3,49%
  D+30 (não entra no relatório do dia).
- Relatório do dia: Débito 6 vendas / 84,00 faturado / 83,29
  realizado (só #898 e #899 têm taxa).

## Estado deixado no sandbox
- Débito geral: **2,50%**, **0** dias
- Débito Visa: **2,19%**, **0** dias (ativa)
- Débito Mastercard: **2,89%**, **0** dias (ativa)
- Crédito: **3,49%**, **30** dias
- Vale Refeição: **5,00%**, **15** dias; Visa desligada
- Vendas #898 (Visa) e #899 (Mastercard) pagas
- Cashback Teste Manual: **R$ 5,00** intacto
- #886/#891 não pagas

## Status
Concluído — aguardando publicação.
