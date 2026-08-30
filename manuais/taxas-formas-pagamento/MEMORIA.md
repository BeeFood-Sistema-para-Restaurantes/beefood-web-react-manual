# MEMORIA.md — #65 Taxas das formas de recebimento

## Escopo
Taxa e dias de recebimento em **Financeiro → Formas Pagamento →
Formas de Recebimento das Vendas**. Prova: configurar débito D+0 2,50%,
crédito 3,49% D+30, vale refeição 5% D+15; **uma venda em cada forma**;
detalhe do pagamento com taxa; **Desempenho → Vendas → Recebimento**
do dia (faturado × realizado).

Não cobre: cadastro novo de forma, TEF, desconto do cardápio (#64),
ajuste de sacola/PDV, DRE, Lançamentos.

## Origem
Pedido do dono (30/08/2026): estudar o fluxo Formas Pagamento → taxas
de cartão → venda → detalhe com taxa → Relatório → Desempenho →
financeiro (faturado e realizado). Configurar crédito, débito e VR.
Prova preferida: débito com dias 0 e taxa 2–3%. Tabela de exemplo para
os que recebem em outros dias. Configurar pelo final da página de
Formas Pagamento. Taxas que façam sentido. Estudo + manual sem parar.

Follow-up: uma venda por forma; relatório só do dia (sem ensinar o
filtro no texto); sem borrão nas imagens.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-formas-pagamento.png` | setas | Menu + bloco Formas de Recebimento das Vendas |
| `02-debito-config.png` | setas | 2,50% e 0 dias + SALVAR |
| `03-credito-config.png` | setas | 3,49% e 30 dias |
| `04-vr-config.png` | setas | Vale Refeição 5% e 15 dias |
| `05-tabela-configurada.png` | setas | Crédito 30/3,49% e Débito 0/2,5% |
| `06-pdv-pago.png` | setas | Venda #894 Crédito Pago + lupa (sem cliente) |
| `07-detalhe-pagamento.png` | setas | #894 taxa 3,49%, líquido 13,92, receb. 29/09 |
| `08-desemp-recebimento.png` | setas | Resumo do dia: débito + vale |
| `09-desemp-dados.png` | setas | Dados do dia: #892, #893, #895 |

Sem borrão: vendas sem cliente (“Não informado” / “-”).

## Decisões
- Taxas redondas e reais: débito 2,50% D+0; crédito 3,49% D+30; VR 5%
  D+15. Exemplo da tabela em R$ 100 no dia 30/08/2026.
- Caminho do relatório no produto é **Desempenho → Vendas →
  Recebimento** (iframe `relatorios.beefood.com.br`). Não existe item
  "Financeiro" dentro do iframe. Financeiro → Recebimentos é outro
  painel (Previsto e Realizado).
- Relatório capturado em **Hoje (30/08/2026)** — não documentar o
  clique do período no `.md`.
- Vendas de prova (30/08/2026, sem cliente): **#892** débito,
  **#893** débito Visa, **#894** crédito R$ 14,42 (+3% do PDV),
  **#895** vale refeição. Não usamos cashback nem pagamos #886/#891.
- O detalhe **com taxa** ao vivo é o **crédito #894** (3,49% D+30,
  14,42 → 13,92, recebimento 29/09). Débito e vale nasceram sem
  `taxa`/`valorLiquido` no registro — o front só desenha o bloco se
  esses campos vêm da API. Não usamos mais o PIX #878.
- O `resumoPagamentos` **não lista o #894 no dia 30/08** (nem no mês):
  o pagamento ficou com recebimento em 29/09. O resumo do dia mostra
  débito e vale. O manual fala isso, sem ensinar filtro extra.
- Acréscimo +3% do crédito no PDV é do cadastro (#64), não da taxa
  da operadora. Não alteramos Cadastros além do SALVAR do modal.

## Estado deixado no sandbox
- Débito: taxa geral **2,50%**, **0** dias
- Crédito: **3,49%**, **30** dias
- Vale Refeição: **5,00%**, **15** dias
- PIX Manual: 1% D+0 (já estava; não mexemos)
- Vendas #892, #893 (débito), #894 (crédito), #895 (vale) pagas
- Cashback do Teste Manual: **R$ 5,00** intacto
- Descontos do #64 (Dinheiro 5%, Vale Alelo +5%, PIX Online 5%) intactos

## Status
Concluído — aguardando publicação.
