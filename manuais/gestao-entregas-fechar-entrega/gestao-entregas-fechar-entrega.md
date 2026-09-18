# Fechar a entrega no painel

O entregador chegou, entregou e ligou avisando. Alguém precisa dizer isso ao sistema — e é
esse alguém que este manual atende.

Fechar a entrega tem dois tamanhos: **uma parada por vez**, que é o uso normal, e **a rota
inteira de uma vez**, que é o atalho de fim de viagem. Os dois estão aqui.

Este manual começa onde
[Despachar e acompanhar](../gestao-entregas-despachar/gestao-entregas-despachar.md) parou: a
rota `A` na rua, com quatro paradas e nenhuma baixa.

## Para que serve

- Marcar cada pedido como entregue, na hora em que ele é entregue.
- Encerrar a rota e liberar o entregador para a próxima viagem.
- Achar depois o que já foi entregue, sem depender da memória de ninguém.

## Antes de começar

- A rota precisa estar na rua. Dar baixa em rota que nunca saiu é aceito pelo sistema, mas
  significa que o pedido nunca foi anunciado ao cliente como "saiu para entrega".
- Dar baixa **muda a situação do pedido** para *Entregue* no Delivery, no caixa e no
  marketplace. É o mesmo peso do despacho, e também não tem desfazer.

---

## 1. Dar baixa em uma parada

Cada linha de parada tem um **visto** à direita. Ele é a baixa daquela entrega.

![A rota na rua, antes de qualquer baixa](imagens-tratadas/01-antes-da-baixa.png)

| Nº | Onde | O que faz |
|----|------|-----------|
| 1. | **Visto da parada** | Confirma a entrega **daquele** pedido. Está sempre visível, em todas as paradas pendentes. |
| 2. | **N de N entregues** | O andamento da viagem. Começa em *0 de N*. |
| 3. | **Botão de finalizar** | Fecha a rota inteira de uma vez (seção 3). Fica no lugar onde antes estava o avião de despachar. |
| 4. | **entregues** | O selo do topo, com o total de pedidos entregues no dia. |

O visto **age no clique, sem janela de confirmação**. Não é descuido do sistema: finalizar a
rota inteira, que é a ação maior, também não pede confirmação — pedir para a menor seria
incoerente. O retorno é a linha mudando na sua frente.

![A primeira parada entregue](imagens-tratadas/02-uma-entregue.png)

| Nº | Onde | O que mudou |
|----|------|-------------|
| 1. | **Parada entregue** | Ficou apagada, com um visto verde. Ela não aceita mais baixa. |
| 2. | **1 de 4 entregues** | A contagem subiu. |
| 3. | **Entregando agora** | Pulou para a parada seguinte — e o mapa se reposicionou nela. |
| 4. | **entregues** | Subiu de 6 para 7. |
| 5. | **em rota** | Desceu de 4 para 3. Os dois selos se movem juntos, em direções contrárias. |

> **A ordem não é obrigatória.** Dá para dar baixa na parada 3 antes da 1. O sistema aceita de
> propósito: o entregador desvia da sequência a toda hora, e recusar só geraria chamado de
> suporte.

> **Entregando agora é sempre uma só.** Ela só pula para a próxima quando a atual sai do
> caminho. Dar baixa fora de ordem não muda quem está sendo entregue agora.

---

## 2. Quando falta uma parada

Três entregues, uma pendente: é o retrato de uma viagem quase acabada.

![Três paradas entregues, uma pendente](imagens-tratadas/03-tres-entregues.png)

| Nº | Onde | O que lê |
|----|------|----------|
| 1. | **3 de 4 entregues** | Quanto já foi baixado. |
| 2. | **Botão de finalizar** | Ainda está ali, e agora é o atalho: um clique baixa a que falta e encerra a rota. |
| 3. | **Entregando agora** | A última parada pendente. |
| 4. | **entregues** | Subiu junto com as baixas. |

> **A última baixa encerra a rota sozinha.** Você não precisa clicar em finalizar depois: ao
> confirmar a última parada, a rota conclui e o entregador é liberado.

---

## 3. Finalizar a rota inteira

O botão do cabeçalho — o que ficou no lugar do avião — **confirma todas as paradas pendentes
de uma vez** e encerra a viagem.

Ele serve para o fim normal do dia: o entregador voltou, confirmou de boca que entregou tudo,
e você fecha a viagem num clique em vez de quatro.

> **Um clique, sem confirmação, e todas as paradas viram *Entregue*.** Inclusive a que talvez
> não tenha sido entregue. Se houver dúvida sobre alguma parada, dê baixa nas outras uma por
> uma e resolva a duvidosa por último — depois de fechar, não há como separar.

Assim que a rota conclui, o painel muda:

![O painel depois de a rota fechar](imagens-tratadas/04-depois-de-fechar.png)

| Nº | Onde | O que mudou |
|----|------|-------------|
| 1. | **em rota** | Voltou a zero: não há mais ninguém na rua. |
| 2. | **entregues** | Ficou com o total do dia. |
| 3. | **Pedidos sem rota** | Só os pedidos que ainda não entraram em viagem nenhuma. |
| 4. | **Rodapé de entregadores** | O entregador voltou a contar como **disponível**. |

A rota desapareceu da lateral — e é aqui que a maioria das dúvidas nasce. Ela não foi apagada:
está escondida atrás do selo **entregues**, que nasce desligado.

---

## 4. Achar o que já foi entregue

Clique no selo **entregues**, no topo.

![O selo entregues ligado, e o grupo que ele revela](imagens-tratadas/05-chip-entregues.png)

| Nº | Onde | O que faz |
|----|------|-----------|
| 1. | **entregues** | Liga e desliga a exibição do que já foi entregue — na lateral **e** no mapa. |
| 2. | **Entregues (N)** | O grupo com tudo o que saiu hoje. Nasce fechado. |

Abrindo o grupo, a viagem reaparece inteira.

![O grupo Entregues aberto, com a rota concluída](imagens-tratadas/05b-grupo-entregues.png)

| Nº | Onde | O que lê |
|----|------|----------|
| 1. | **Entregues (N)** | Quantos pedidos entregues estão sendo mostrados. |
| 2. | **Rota concluída** | A viagem, em verde: entregador, *Concluída*, *N de N entregues* e há quanto tempo. Abrindo, você vê as paradas na ordem em que foram feitas. |
| 3. | **entregues** | O selo ligado — é ele que sustenta tudo o que está sendo mostrado. |

Nesta foto aparecem **duas rotas concluídas com a mesma letra `A`**. Não é erro: a letra é
reaproveitada assim que uma viagem termina. Para falar de uma entrega passada, use o número do
pedido.

> **A rota concluída fica por cerca de duas horas.** Depois disso ela sai da tela, mesmo com o
> selo ligado. Os pedidos entregues continuam aparecendo um pouco mais, soltos no grupo. Para
> conferência de fim de turno, o lugar certo é o relatório
> [Operação de entrega](../relatorio-operacao-entrega/relatorio-operacao-entrega.md).

E o entregador volta para a lista, disponível.

![O entregador disponível de novo](imagens-tratadas/06-entregador-de-volta.png)

| Nº | Onde | O que lê |
|----|------|----------|
| 1. | **Disponível (N)** | Ele saiu do grupo *Em rota*. |
| 2. | **Linha do entregador** | A distância mostrada é a da última posição recebida — se ele ainda está voltando, é onde ele estava. |

---

## 5. Onde o pedido vai dar no Delivery

A baixa não é só do painel de entregas. O pedido muda de coluna na tela de Delivery.

![O pedido na coluna ENTREGUE do Delivery](imagens-tratadas/07-pedido-no-delivery.png)

| Nº | Onde | O que lê |
|----|------|----------|
| 1. | **EM ENTREGA** | Esvaziou: era onde os pedidos ficavam entre o despacho e a baixa. |
| 2. | **ENTREGUE** | Os pedidos baixados, com o total do dia. |
| 3. | **O pedido** | O mesmo número que estava na rota, agora fechado. |

É a mesma informação vista de outro lugar, e é a que o caixa e o fechamento usam.

---

## Dicas

- **Dê baixa na hora, não no fim do turno.** Baixa em lote, de memória, é como nascem pedidos
  marcados como entregues que nunca chegaram.
- **O visto não pede confirmação.** Antes de clicar, confira o número do pedido na linha.
- **Use o finalizar só quando a viagem acabou de verdade.** Ele confirma tudo o que estiver
  pendente, sem perguntar.
- **Não existe "não entregue".** O sistema só sabe registrar entrega. Pedido que não pôde ser
  entregue se resolve na tela de Delivery, como cancelamento ou reentrega.
- **Se a rota sumiu, ligue o selo entregues.** É a dúvida mais comum deste manual, e a resposta
  é um clique.

---

## Onde continuar

| Manual | O que cobre |
|--------|-------------|
| [Despachar e acompanhar](../gestao-entregas-despachar/gestao-entregas-despachar.md) | Mandar a rota para a rua e seguir o entregador |
| [Relatório Operação de entrega](../relatorio-operacao-entrega/relatorio-operacao-entrega.md) | O fechamento do dia: tempos, entregas por entregador e quilometragem |
| [Quanto o entregador recebe](../entregador-quanto-recebe/entregador-quanto-recebe.md) | A taxa por entrega e o relatório Taxa/KM |
| [Montar a rota](../gestao-entregas-montar-rota/gestao-entregas-montar-rota.md) | Agrupar os pedidos e escolher quem leva |
