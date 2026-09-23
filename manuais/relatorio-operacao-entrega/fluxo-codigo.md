# O que a tela faz de verdade — Relatório Operação de Entrega

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `relatorio-operacao-entrega.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Lido em `beefood-reports-hub/src/components/reports/OperacaoEntrega.tsx` (910 linhas),
`OperacaoMapa.tsx`, `OperacaoDados.tsx` e `OperacaoFiltrosBar.tsx`, mais o plano de origem em
`.lovable/plan/novo-relatório-delivery-operação-de-entrega-2026-09-15.md`. Conferido na
sandbox sobre as 13 entregas que os manuais #106 a #109 produziram no dia.

## Uma chamada, uma tela

O relatório é uma requisição só (`GET .../entregasOperacao/:empresa/:inicio/:fim`) com filial,
faixa de horário e período de comparação opcionais. **Não há drill-down**: trocar qualquer
filtro refaz a busca inteira. Isso explica a espera de alguns segundos a cada mudança e o
porquê de o manual insistir no *Confirmar* do período.

Período máximo de 366 dias. Faixa de horário e período comparativo têm de vir **em par**
(início e fim), senão a API recusa.

## As regras de exibição, e por que elas viram texto no manual

Estas cinco regras estão no código e mudam o que o lojista vê. Todas viraram frase no manual:

| Regra | Onde aparece |
|---|---|
| valor não medido vira **traço**, nunca zero | todos os cartões |
| média exige **20 pedidos**, senão mostra *Poucos pedidos* | cartões de etapa |
| toda média mostra a **cobertura** em cinza embaixo | cartões e tabelas |
| entrega **acima de 4 h** sai da média, e isso é dito | cartões de etapa |
| variação de valor absoluto em %, variação de % em pontos | cartões do topo |

O plano original previa cinco indicadores (Entregas, Tempo médio, Pontualidade, Ticket,
Cancelamento). A tela entregue tem **seis** e outros nomes: Entregas, Faturamento, Ticket
médio, Taxas de entrega, Taxas do entregador e Duração média. O manual segue a tela.

## O que cada bloco depende para existir

| Bloco | Depende de |
|---|---|
| Métricas de tempo | marcações de etapa nos pedidos (`confirmação`, `pronto`, `saiu`, `entregue`) |
| Onde o tempo é investido | **horário de saída** gravado; sem ele o bloco explica a ausência em vez de somir |
| Análise dos prazos | horário prometido, que chega do marketplace |
| Por loja | mais de uma filial no período (some com uma) |
| Por hora do dia | sempre 24 posições; com faixa de horário, as de fora ficam esmaecidas |
| Mapa | endereço geolocalizado; o rodapé diz quantos entraram |

## Duas contagens diferentes, e é de propósito

Medido no mesmo dia, com os mesmos pedidos:

| Relatório | Entregas | O que conta |
|---|---|---|
| Operação de Entrega | **13** | pedido **entregue** |
| Entregador (Taxa / KM) | **15** | pedido de entrega do período, entregue ou não (2 apareceram em *Sem entregador*) |

Não é divergência de cálculo: um mede operação concluída, o outro monta pagamento. Vale ter
isso no radar quando alguém comparar os dois números.

## O cartão *Taxas do entregador* ficou em traço — medido

Gravei valor do entregador (R$ 3,50) em três pedidos do dia pelo lápis da tela do pedido —
o que escreve o mesmo campo que a área de atendimento preenche — e **o cartão continuou em
traço**, nas duas janelas testadas (hoje e 30 dias). No mesmo dia, o relatório
**Entregador (Taxa / KM)** mostrou `Taxa Entregador Total R$ 10,50` para os mesmos pedidos.

Ou seja: o dado existe, e este cartão não o lê da mesma fonte. Como não tenho o código do
endpoint `entregasOperacao` no clone disponível, o manual **não afirma causa**: diz que traço
significa valor não lido dos pedidos e manda fechar pagamento no relatório vizinho, que lista
pedido por pedido. Se alguém for corrigir isso no servidor, o caso reproduzido está aqui.

## Cache

`ReportsCache` guarda por período + filial + faixa de horário. Trocar o período e voltar não
refaz a chamada — e por isso o botão de atualizar existe ao lado do funil.
