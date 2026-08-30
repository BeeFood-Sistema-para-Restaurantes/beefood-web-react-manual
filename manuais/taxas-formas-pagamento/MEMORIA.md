# MEMORIA.md — #65 Taxas das formas de recebimento

## Escopo
Taxa e dias de recebimento em **Financeiro → Formas Pagamento →
Formas de Recebimento das Vendas**. Prova: configurar débito D+0 2,50%,
crédito 3,49% D+30, vale refeição 5% D+15; vender no PDV; detalhe do
pagamento; **Desempenho → Vendas → Recebimento** (faturado × realizado).

Não cobre: cadastro novo de forma, TEF, desconto do cardápio (#64),
ajuste de sacola/PDV, DRE, Lançamentos.

## Origem
Pedido do dono (30/08/2026): estudar o fluxo Formas Pagamento → taxas
de cartão → venda → detalhe com taxa → Relatório → Desempenho →
financeiro (faturado e realizado). Configurar crédito, débito e VR.
Prova preferida: débito com dias 0 e taxa 2–3%. Tabela de exemplo para
os que recebem em outros dias. Configurar pelo final da página de
Formas Pagamento. Taxas que façam sentido. Estudo + manual sem parar.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-formas-pagamento.png` | setas | Menu + bloco Formas de Recebimento das Vendas |
| `02-debito-config.png` | setas | 2,50% e 0 dias + SALVAR |
| `03-credito-config.png` | setas | 3,49% e 30 dias |
| `04-vr-config.png` | setas | Vale Refeição 5% e 15 dias |
| `05-tabela-configurada.png` | setas | Crédito 30/3,49% e Débito 0/2,5% |
| `06-pdv-pago.png` | setas | Venda #893 Débito Visa Pago + lupa |
| `07-detalhe-pagamento.png` | setas | PIX #878 com taxa 1%, líquido 63,26, D+0 (borrao no nome) |
| `08-desemp-recebimento.png` | setas | Resumo faturado/realizado |
| `09-desemp-dados.png` | setas | Dados: #892/#893 mesmo dia + #878 com −1% (borrao clientes) |

Puras extras (não referenciadas): `06-desemp-recebimento.png` antigo,
`07b-*`, `07c-*`.

## Decisões
- Taxas redondas e reais: débito 2,50% D+0; crédito 3,49% D+30; VR 5%
  D+15. Exemplo da tabela em R$ 100 no dia 30/08/2026.
- Caminho do relatório no produto é **Desempenho → Vendas →
  Recebimento** (iframe `relatorios.beefood.com.br`). Não existe item
  "Financeiro" dentro do iframe. Financeiro → Recebimentos é outro
  painel (Previsto e Realizado).
- Vendas de prova: **#892** (débito sem bandeira) e **#893** (débito
  Visa), One Burger R$ 14,00. Não usamos cashback nem pagamos #886/#891.
- O detalhe **com taxa preenchida** no sandbox é o **PIX Manual #878**
  (1% D+0, 63,90 → 63,26). As vendas novas de cartão nasceram com
  vencimento D+0, mas `taxa`/`valorLiquido` ainda vazios no registro —
  o front só desenha o bloco se esses campos vêm da API. O manual usa
  o PIX para mostrar o bloco e o relatório; o débito para o D+0 no
  mesmo dia.
- Borrão no nome da Fernanda (#878) e na coluna Cliente do Dados.
- Não alteramos Cadastros além do que o SALVAR do modal já regrava.
  Crédito manteve o acréscimo +3% do PDV que já existia.

## Estado deixado no sandbox
- Débito: taxa geral **2,50%**, **0** dias
- Crédito: **3,49%**, **30** dias
- Vale Refeição: **5,00%**, **15** dias
- PIX Manual: 1% D+0 (já estava; não mexemos)
- Vendas #892 e #893 pagas no débito (R$ 14,00 cada)
- Cashback do Teste Manual: **R$ 5,00** intacto
- Descontos do #64 (Dinheiro 5%, Vale Alelo +5%, PIX Online 5%) intactos

## Status
Concluído — aguardando publicação.
