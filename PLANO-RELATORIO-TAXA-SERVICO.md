# Proposta — manual #94: relatório de Taxa de Serviço

> Primeiro manual do bloco de relatórios, escolhido pelo dono em **01/09/2026**.
> Decisão do dono: **não usar o histórico** — o cenário é **construído por nós**, e o relatório
> é lido com o filtro em **hoje** (no máximo hoje + amanhã).
>
> Este documento é a **proposta**. Nada foi criado no sandbox e nenhum manual foi escrito.

Status: ⏸️ **aguardando aprovação**.

---

## 1. Por que construir o dado é a decisão certa aqui

Inspecionei o que o relatório devolve hoje no sandbox: **38 pedidos com taxa**, e eles são
inúteis para ensinar o relatório.

| O que o histórico tem | Por que atrapalha |
|-----------------------|-------------------|
| **34 dos 38 com "Sem garçom"** | O agrupamento **principal** do relatório é *por Garçom*, e o clique numa linha abre o detalhe daquele garçom. Com 89% sem garçom, a tela ensina o contrário do que deveria |
| **Só 1 garçom cadastrado** (*Funcionário 4*) | Sem dois ou mais garçons não existe comparação, nem ranking, nem drill-down interessante |
| **Taxa sempre 10%** nos 38 | O agrupamento *Tipo Taxa* existe justamente para separar **% (Percentual)** de **R$ (Fixo)**. Com o histórico ele mostra uma linha só |
| **Nenhum pedido com taxa zero** | Perde-se a lição de que o pedido sem taxa aparece na lista mas **não** entra nos totais |
| Valores quebrados (R$ 1.427,47, R$ 238,04) | O leitor não consegue conferir a conta de cabeça |

Com o cenário construído, o manual mostra números que o leitor **soma junto** — e é isso que
faz um manual de relatório ser útil.

---

## 2. A descoberta que vira o coração do manual

Lendo o código e conferindo nos dados reais, achei um comportamento que **vai gerar chamado de
suporte** e que nenhum manual explica hoje:

> **Uma taxa de 10% aparece no relatório como 9,09%.**

Não é bug. A coluna **% Taxa** divide a taxa pelo **Valor Total**, e o Valor Total **já inclui a
taxa**. Conferido em três pedidos reais do sandbox:

| Pedido | Produtos | Taxa (R$) | Valor Total | Taxa ÷ Total |
|--------|---------:|----------:|------------:|-------------:|
| 842 | 54,00 | 5,40 | 59,40 | **9,09%** |
| 854 | 1.297,70 | 129,77 | 1.427,47 | **9,09%** |
| 383 | 216,40 | 21,64 | 238,04 | **9,09%** |

A taxa é **10% do consumo**, mas **9,09% da conta fechada**. Uma seção do manual vai ser só
sobre isso, com a conta escrita — e é o tipo de coisa que justifica o manual existir.

**Segunda descoberta, menor mas real:** na tabela **Taxa Serviço por Pagamento**, quando um
pedido é pago em duas formas, o relatório divide a taxa pelo **número de formas**, não pelo valor
de cada uma. Um pedido pago R$ 24,00 em dinheiro e R$ 20,00 em débito tem a taxa rateada
**50/50**. O cenário abaixo inclui um pedido assim, de propósito, para o manual poder avisar.

---

## 3. O cenário proposto — 8 pedidos, todos de hoje

Valores escolhidos para o leitor conferir de cabeça: consumo em números redondos, taxa padrão de
**10%** (que já é o parâmetro da loja) e um pedido com **taxa fixa em R$** para o *Tipo Taxa* ter
duas linhas.

| # | Mesa / Comanda | Garçom | Consumo | Taxa | Total | Pagamento | Situação |
|---|----------------|--------|--------:|------|------:|-----------|----------|
| 1 | Mesa 1 | **Ana Souza** | 100,00 | 10% = **10,00** | 110,00 | Dinheiro | RECEBIDO |
| 2 | Mesa 2 | **Ana Souza** | 60,00 | 10% = **6,00** | 66,00 | Débito | RECEBIDO |
| 3 | Mesa 3 | **Bruno Lima** | 80,00 | 10% = **8,00** | 88,00 | Pix | RECEBIDO |
| 4 | Comanda 1 | **Bruno Lima** | 50,00 | **R$ 15,00 fixo** | 65,00 | Dinheiro | RECEBIDO |
| 5 | Comanda 2 | **Carla Dias** | 40,00 | 10% = **4,00** | 44,00 | **Dinheiro 24,00 + Débito 20,00** | RECEBIDO |
| 6 | Mesa 4 | *(sem garçom)* | 30,00 | 10% = **3,00** | 33,00 | Débito | RECEBIDO |
| 7 | Mesa 5 | **Carla Dias** | 20,00 | **desligada** | 20,00 | Dinheiro | RECEBIDO |
| 8 | Mesa 6 | **Ana Souza** | 70,00 | 10% = **7,00** | 77,00 | — | **ABERTO** |

Nomes de garçom são **fictícios** — o repositório é público e não entra nome de pessoa real.

### O que cada pedido está exercitando

| Pedido | Serve para mostrar |
|--------|--------------------|
| 1, 2 | Dois pedidos do mesmo garçom: o resumo soma, o drill-down lista |
| 3, 4 | Segundo garçom, para a tabela ter ranking e comparação |
| **4** | **Taxa fixa em R$** — dá a segunda linha do *Tipo Taxa* e puxa a média para cima |
| **5** | **Duas formas de pagamento** — expõe o rateio 50/50 da seção 2 |
| **6** | **Sem garçom** — mostra a linha *Sem Funcionário*, que o cliente vai ver na conta dele |
| **7** | **Taxa desligada** — aparece na lista de pedidos e **não** nos totais nem nos resumos |
| **8** | **ABERTO** — some da tela por causa do filtro padrão, e é o gancho para ensinar o filtro |

### Os números que o manual vai explicar

Com o filtro em **hoje** e o padrão do relatório (**apenas RECEBIDO**), a tela mostra:

| Indicador do topo | Valor | Conta |
|-------------------|------:|-------|
| **Total Taxa Serviço** | R$ 46,00 | 10 + 6 + 8 + 15 + 4 + 3 |
| **Faturamento Total** | R$ 426,00 | soma dos 7 pedidos recebidos, **inclusive o de taxa zero** |
| **Total Pago** | R$ 426,00 | todos quitados |
| **Taxa Média** | R$ 7,67 | 46,00 ÷ **6** pedidos com taxa (o de taxa zero não conta) |
| **% Média** | 11,42% | média dos percentuais por pedido — puxada para cima pela taxa fixa |

**Taxa Serviço por Garçom:**

| Garçom | Qtd | Valor Total | Taxa Total | Taxa Média | % Taxa |
|--------|----:|------------:|-----------:|-----------:|-------:|
| Ana Souza | 2 | 176,00 | 16,00 | 8,00 | 9,09% |
| Bruno Lima | 2 | 153,00 | 23,00 | 11,50 | 15,03% |
| Carla Dias | 1 | 44,00 | 4,00 | 4,00 | 9,09% |
| Sem Funcionário | 1 | 33,00 | 3,00 | 3,00 | 9,09% |

Repare no que essa tabela ensina sozinha: **Bruno tem a mesma quantidade de pedidos que Ana e
quase o dobro de taxa**, porque um dos pedidos dele tem taxa **fixa**. É exatamente a leitura
errada que um dono de restaurante faria ("Bruno vende mais"), e o manual vai desarmar.

**Taxa Serviço por Pagamento** (com o rateio da seção 2):

| Pagamento | Taxa | De onde vem |
|-----------|-----:|-------------|
| Dinheiro | 27,00 | 10,00 + 15,00 + **2,00** (metade da taxa do pedido 5) |
| Débito | 11,00 | 6,00 + **2,00** (a outra metade) + 3,00 |
| Pix | 8,00 | 8,00 |

**Tipo Taxa:** *% (Percentual)* R$ 31,00 · *R$ (Fixo)* R$ 15,00.

---

## 4. O que precisa ser criado antes

| Passo | O que | Onde |
|-------|-------|------|
| 1 | **3 garçons** (Ana Souza, Bruno Lima, Carla Dias) com **Tipo de Função = Garçom** | Cadastros → Funcionários |
| 2 | Confirmar **Taxa de Serviço Padrão** ligada em **10%** | Configuração → Parâmetros (já está assim: `taxaServicoPadrao: true`, `taxaServicoValor: 10`) |
| 3 | Os **8 pedidos** da tabela acima | Mesas/Comandas → Novo Pedido (F1) |
| 4 | **Pagar 7 deles** (deixar o pedido 8 aberto) | Pagamento no próprio pedido |

Hoje existe **1 garçom** cadastrado (*Funcionário 4*) — os três novos são necessários.

### Como criar: recomendo o caminho híbrido

| Caminho | Prós | Contras |
|---------|------|---------|
| **Só pela tela** (Novo Pedido F1 × 8 + pagamentos) | Fiel ao que o cliente faz; garante que o servidor grava igual | Lento e frágil de automatizar: 8 pedidos × (mesa + garçom + produto + taxa + salvar + pagar) |
| **Só por POST** (`venda2/salvar` + `venda2/pagamentoPago`) | Rápido e com valores exatos | Risco de gravar diferente do fluxo da tela. Já vi isso neste sandbox: vendas criadas em lote pela API ficaram **sem número de pedido** |
| **Híbrido — recomendado** | Criar o **pedido 1 pela tela**, conferir pela API que `taxaServico`, `taxaServicoValor` e `funcionarioID` gravaram certo, e só então repetir os outros 7 por POST **copiando o payload que a tela mandou** | — |

O híbrido resolve o risco sem pagar o custo de 8 fluxos manuais. **Precisa da sua aprovação**,
porque envolve criar dado no sandbox.

### Três coisas que preciso resolver na execução

1. **Preços do cardápio.** A base tem **nomes de produto repetidos** e um **Preço Programado
   ativo** (o Milk Shake de Morango sai 15,12 em vez de 18,90). Vou fixar os produtos por ID,
   não por nome, e conferir o valor gravado antes de escrever qualquer número no manual.
2. **Hora dos pedidos.** Os 8 vão nascer no mesmo intervalo de minutos, então o gráfico
   *Taxa Serviço por período* na granularidade **Horário** vai mostrar **um pico só**, não a
   curva de almoço e jantar. Se você quiser a curva, preciso saber se o payload aceita definir a
   data/hora do pedido — senão sugiro **não usar** essa imagem no manual.
3. **O pedido 5 (duas formas de pagamento)** precisa ser pago em dois lançamentos. Vou validar
   que a API aceita o pagamento parcial antes de contar com ele.

---

## 5. Estrutura proposta do manual

Pasta: `manuais/relatorio-taxa-servico/`. Item de menu: **Relatório: Taxa de Serviço**.

1. **Para que serve** — quanto de taxa a casa cobrou, e quem atendeu.
2. **Onde fica** — Desempenho → Presencial → Taxa Serviço.
3. **O exemplo deste manual** — a tabela dos 8 pedidos, para o leitor conferir as contas.
4. **Os cinco números do topo** — o que cada card soma, e por que a Taxa Média divide por 6 e não por 7.
5. **Por que 10% aparece como 9,09%** — a seção-chave, com a conta escrita.
6. **Taxa de serviço por garçom** — a tabela e o clique que abre o detalhe do garçom.
7. **Os outros jeitos de agrupar** — Situação, Mesa, Comanda, Tipo Taxa e Pagamento; inclui o aviso do rateio 50/50.
8. **A lista de pedidos** — todas as colunas, e o pedido de taxa zero que aparece aqui mas não nos totais.
9. **Os filtros** — começando pela armadilha: **o relatório abre mostrando só os pedidos RECEBIDO**.
10. **Exportar para Excel**.
11. **Perguntas frequentes**.

### Imagens (8)

| Nº | Imagem | Para que serve |
|----|--------|----------------|
| 1 | Menu Desempenho → Presencial → Taxa Serviço | Onde fica |
| 2 | Os cinco cards do topo | Os totais, com as contas da seção 4 |
| 3 | Tabela *Taxa Serviço por Garçom* | O coração operacional: 4 linhas, uma delas *Sem Funcionário* |
| 4 | Detalhe de um garçom, aba *Análise por Venda* | O drill-down e as 13 colunas do pedido |
| 5 | Pizza + *Dados por Tipo Taxa* | As duas linhas: % e R$ fixo |
| 6 | *Dados por Pagamento* | O rateio 50/50 do pedido pago em duas formas |
| 7 | A lista de pedidos, com o de taxa zero visível | O que entra na lista e não nos totais |
| 8 | Modal *Filtros do Resumo* com o Tipo em **RECEBIDO** | A armadilha do filtro padrão |

### As perguntas frequentes que o manual já tem resposta para

1. *"Cobro 10% e o relatório mostra 9,09%. Está errado?"* — não; a conta é sobre o total, que já inclui a taxa.
2. *"Um pedido não aparece."* — provavelmente está **ABERTO**, e o relatório abre filtrado em RECEBIDO.
3. *"Um garçom aparece como Sem Funcionário."* — o pedido foi lançado sem garçom; dá para atribuir depois no detalhe da venda.
4. *"A soma por forma de pagamento não bate com o que recebi."* — pedido com duas formas tem a taxa dividida por igual, não proporcional.
5. *"A taxa média de um garçom está muito alta."* — confira se algum pedido dele tem taxa **fixa em R$** em vez de percentual.
6. *"O total de faturamento inclui pedido sem taxa?"* — sim; só a taxa e a média olham apenas os pedidos com taxa.
7. *"Mudei um pedido e o relatório não mudou."* — cache de 5 minutos.
8. *"Não vejo esse relatório no menu."* — depende do grupo de acesso do usuário.

---

## 6. O que este cenário faz pelos próximos manuais

Os 8 pedidos não servem só ao #94. Eles são vendas **presenciais de hoje, com taxa, garçom,
mesa, comanda e formas de pagamento variadas** — exatamente o que os próximos manuais precisam:

| Manual | Aproveita |
|--------|-----------|
| #77 Resumo de vendas | Os agrupamentos por situação, pagamento e funcionário |
| #79 Descontos | Se eu incluir um desconto num dos pedidos (**posso, se você quiser**) |
| #95 Pedidos no mobile e comissão | Os mesmos garçons |
| #75 Resumo geral / #76 Vendas por origem | Movimento presencial no dia |

Se a ideia é construir o dado de cada relatório, vale eu **já plantar aqui** o que os vizinhos
vão precisar, em vez de criar venda nova a cada manual. Isso é uma decisão sua — me diz se
prefere cenário mínimo por manual ou um cenário do dia que sirva a vários.

---

## 7. O que preciso que você decida

1. **Aprovar o cenário dos 8 pedidos** (seção 3) — ou ajustar valores, nomes de garçom e quantidade.
2. **Aprovar o caminho híbrido de criação** (seção 4) — pedido 1 pela tela, os outros por POST.
3. **O gráfico por horário:** aceito o pico único, ou tiro essa imagem do manual?
4. **Cenário compartilhado ou mínimo?** (seção 6) — já plantar o que os próximos relatórios usam?
5. **Nome do item de menu:** *Relatório: Taxa de Serviço* — ou você prefere só *Taxa de Serviço*?
