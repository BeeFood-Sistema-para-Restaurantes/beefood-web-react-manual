# Montar a rota: agrupar pedidos e escolher o entregador

**Rota** é uma viagem: um entregador, uma sequência de paradas, um pedido em cada parada.
Montar a rota é o trabalho do operador — escolher quais pedidos saem juntos, em que ordem e
com quem.

A rota nasce **parada**. Montar não manda ninguém para a rua: dá para montar, olhar, mexer e
só depois despachar. Mandar para a rua é o assunto de
[Despachar e acompanhar](../gestao-entregas-despachar/gestao-entregas-despachar.md).

Este manual presume que você já sabe ler a tela —
[Ler o mapa e o painel de entregas](../gestao-entregas-mapa-painel/gestao-entregas-mapa-painel.md)
é o manual anterior.

## Para que serve

- Juntar num único percurso os pedidos que ficam perto um do outro.
- Escolher quem leva, vendo quem está disponível e a que distância está da loja.
- Ordenar as paradas, ou deixar o sistema ordenar.
- Juntar um pedido que chegou depois a uma rota que já está montada.

## Antes de começar

- Você precisa de pedidos de delivery na tela. Eles aparecem em **Pedidos sem rota**.
- O entregador precisa estar cadastrado e, para receber a viagem, **disponível no
  aplicativo** —
  [Liberar o entregador](../gestao-entregas-liberar-entregador/gestao-entregas-liberar-entregador.md).
- O pedido precisa ter **endereço com coordenada** para aparecer no mapa. Sem coordenada ele
  entra na rota, mas você não o vê no desenho.

---

## 1. Escolher os pedidos

Marque a caixinha de cada pedido em **Pedidos sem rota**. Ao marcar o primeiro, aparece a
**barra de ação** no pé da tela.

![Três pedidos marcados e a barra de ação](imagens-tratadas/01-selecao.png)

| Nº | Onde | O que faz |
|----|------|-----------|
| 1. | **Caixinha do grupo** | Marca e desmarca **todos** os pedidos sem rota de uma vez. |
| 2. | **N pedidos selecionados** | A conta do que você marcou: quantidade e valor somado. Serve para conferir antes de criar. |
| 3. | **Limpar** | Desmarca tudo e fecha a barra. |
| 4. | **Marcar N prontos** | Marca na cozinha os pedidos selecionados que ainda estão em preparo. Embaixo do botão o sistema avisa quantos **já** estão prontos ou na rua. |
| 5. | **Adicionar à rota** | Põe o que está marcado numa rota que **já existe** (seção 5). |
| 6. | **Criar rota** | Cria uma **viagem nova** com o que está marcado. |

Ao marcar um pedido, o pino dele **fica destacado no mapa**. É a conferência mais rápida de
que você juntou vizinhos e não pontas opostas da cidade.

> **Marcar prontos limpa a seleção.** O botão trabalha e desmarca tudo. Se a ideia era
> marcar prontos *e* criar a rota, marque prontos primeiro e selecione de novo.

---

## 2. Criar a rota

Com os pedidos marcados, clique em **Criar rota**.

![A janela de criar rota](imagens-tratadas/02-janela-criar-rota.png)

| Nº | Onde | O que é |
|----|------|---------|
| 1. | **A rota é criada parada** | O aviso da própria janela: criar **não** despacha. |
| 2. | **Lista das paradas** | Na ordem em que você marcou os pedidos. Dá para mudar depois. |
| 3. | **N paradas** | Quantidade e valor total da viagem. |
| 4. | **Sem entregador** | Criar sem escolher ninguém é permitido — a rota fica montada esperando alguém. |
| 5. | **Lista de entregadores** | Cada um com a situação e **a distância até o restaurante**. Só quem está *Disponível* é escolha sensata. |
| 6. | **Sem app** | Cadastrado e nunca entrou no aplicativo. Escolher este é montar uma viagem que ninguém vai ver. |
| 7. | **CRIAR ROTA (F2)** | Cria a viagem. |

Escolha o entregador clicando no nome dele.

![O entregador escolhido fica marcado](imagens-tratadas/03-entregador-escolhido.png)

| Nº | Onde | O que faz |
|----|------|-----------|
| 1. | **Entregador marcado** | A linha escolhida fica destacada. Clicando em outro, a escolha troca. |
| 2. | **CRIAR ROTA (F2)** | Confirma. |

Pronto: a rota aparece na lateral e os pinos daqueles pedidos ganham a letra da rota no
mapa.

![A rota criada, na lateral e no mapa](imagens-tratadas/04-rota-criada.png)

| Nº | Onde | O que mudou |
|----|------|-------------|
| 1. | **Letra da rota** | `A`, `B`, `C`… Identifica a viagem na tela e nos pinos do mapa. |
| 2. | **Pronta para sair** | A rota está montada e **ainda não saiu**. |
| 3. | **Paradas** | Os pedidos, agora na sequência da viagem. |
| 4. | **em rota** | O selo do topo **continua zerado**: para o restante do sistema, nada saiu ainda. |
| 5. | **Pedidos sem rota** | Diminuiu — os pedidos que entraram na rota saíram deste grupo. |

> **A letra é reaproveitada.** Ela é a menor letra livre entre as rotas **abertas**, não um
> número que só cresce. Rota concluída devolve a letra, então o `A` de agora não é o `A` de
> uma hora atrás. Para falar de uma viagem passada, use o pedido, não a letra.

---

## 3. Ler o grupo da rota

O grupo da rota na lateral tem tudo o que você precisa saber sobre a viagem.

![O cabeçalho da rota](imagens-tratadas/05a-cabecalho-rota.png)

| Nº | Onde | O que lê |
|----|------|----------|
| 1. | **Nome do entregador** | Quem leva. A bolinha ao lado mostra se ele está online no aplicativo. |
| 2. | **Letra** | A identificação curta da viagem, a mesma dos pinos do mapa. |
| 3. | **Pronta para sair · N de N entregues** | A situação da viagem e o andamento. Antes de despachar é sempre *0 de N*. |

Abaixo do cabeçalho vêm as paradas.

![As paradas da rota](imagens-tratadas/05b-paradas-da-rota.png)

| Nº | Onde | O que faz |
|----|------|-----------|
| 1. | **Linha da parada** | Um pedido: número, cliente, endereço, valor e forma de pagamento. O número na bolinha é a **ordem** da parada. |
| 2. | **Alça de arrastar** | Segure e arraste para mudar a ordem das paradas. |
| 3. | **Visto** | Dá baixa naquela entrega. Está em [Fechar a entrega no painel](../gestao-entregas-fechar-entrega/gestao-entregas-fechar-entrega.md). |

Clicando no cabeçalho, o grupo fecha e abre — útil quando há várias rotas na tela.

---

## 4. Ordenar as paradas

Há dois jeitos.

**À mão:** arraste pela alça (a seta 2 da imagem acima). Use quando você sabe algo que o
sistema não sabe — o cliente que pediu para chegar mais tarde, o prédio com portaria que
fecha, a rua que está em obra.

**Pelo sistema:** clique em **Otimizar ordem**. O sistema reordena as paradas pela
distância, começando do restaurante.

![Depois de otimizar, a ordem das paradas mudou](imagens-tratadas/08-otimizar-ordem.png)

| Nº | Onde | O que mudou |
|----|------|-------------|
| 1. | **Primeira parada** | Passou a ser a mais perto do restaurante. |
| 2. | **Última parada** | A mais longe foi para o fim. |

> **O botão Otimizar ordem só aparece quando há ordem melhor.** Depois de otimizar ele
> desaparece — não é erro, é o sistema dizendo que já está bom.

> **A ordem que você montar pode ser desfeita no celular.** O aplicativo do entregador tem
> um botão de *melhor rota* que reordena por conta dele. Se a sua ordem tem um motivo,
> combine com o motoboy para não usar aquele botão.

---

## 5. Juntar um pedido a uma rota que já existe

Chegou um pedido do mesmo bairro depois de a rota estar montada? Não precisa criar outra
viagem.

Marque o pedido e clique em **Adicionar à rota**.

![Escolhendo a rota que vai receber o pedido](imagens-tratadas/06-adicionar-a-rota.png)

| Nº | Onde | O que faz |
|----|------|-----------|
| 1. | **Pedido marcado** | O pedido que vai entrar. Dá para marcar mais de um. |
| 2. | **Adicionar à rota** | Abre a lista de rotas do dia. |
| 3. | **Rota aberta** | A viagem que ainda não terminou. **É esta que você quer.** |
| 4. | **Concluída** | Rotas já encerradas também aparecem na lista. Não use: o pedido entraria numa viagem que acabou. |

O pedido entra **no fim da fila**, como última parada.

![O pedido novo entrou como quarta parada](imagens-tratadas/07-rota-com-parada-nova.png)

| Nº | Onde | O que mudou |
|----|------|-------------|
| 1. | **Quarta parada** | O pedido novo, no fim. |
| 2. | **N de N entregues** | A contagem subiu de 3 para 4 paradas. |
| 3. | **Otimizar ordem** | Voltou a aparecer, porque a ordem deixou de ser a melhor. Clique se o novo pedido deveria ser visitado antes. |

> **Dá para adicionar pedido em rota que já saiu.** O sistema permite, e em dia cheio isso
> salva uma viagem — mas o entregador **não é avisado sozinho**: ligue para ele. Sem aviso,
> ele termina a última parada que conhece e volta.

---

## 6. Trocar o entregador e desfazer a rota

Os três pontos ao lado da rota abrem o que sobra das decisões.

![O menu da rota](imagens-tratadas/09-menu-da-rota.png)

| Nº | Onde | O que faz |
|----|------|-----------|
| 1. | **Três pontos** | Abre o menu da rota. |
| 2. | **Trocar entregador** | Escolhe outra pessoa para a mesma viagem. Serve antes e depois de despachar. |
| 3. | **Remover entregador** | Deixa a rota montada sem ninguém. As paradas continuam. |
| 4. | **Excluir rota** | Desfaz a viagem. Os pedidos **voltam** para *Pedidos sem rota* — nada é cancelado nem perdido. |

> **Excluir rota não cancela pedido.** É uma operação de organização: desmonta o grupo e
> devolve os pedidos para a lista. Cancelar um pedido continua sendo assunto da tela de
> Delivery.

---

## Dicas

- **Junte por bairro, não por hora de chegada.** Dois pedidos do mesmo condomínio numa
  viagem valem mais que dois pedidos "que chegaram juntos" em pontas opostas.
- **Olhe o mapa antes de criar.** Os pinos marcados mostram na hora se a viagem faz sentido.
- **Crie a rota mesmo com pedido em preparo.** Ela nasce parada: dá para montar agora e
  despachar quando a cozinha terminar. A janela de despacho avisa quantos ainda não estão
  prontos.
- **Rota com uma parada é válida.** Para pedido longe e sozinho, é o jeito de registrar a
  viagem e o entregador.
- **O sistema não diz "não".** Quase nada é bloqueado — adicionar pedido em rota na rua,
  trocar entregador no meio, excluir. É de propósito: quem está no balcão sabe coisas que o
  sistema não sabe. Em troca, **o cuidado é seu**.

---

## Onde continuar

| Manual | O que cobre |
|--------|-------------|
| [Despachar e acompanhar](../gestao-entregas-despachar/gestao-entregas-despachar.md) | Mandar a rota para a rua e seguir o entregador no mapa |
| [Fechar a entrega no painel](../gestao-entregas-fechar-entrega/gestao-entregas-fechar-entrega.md) | Dar baixa quando o pedido chega |
| [Despacho automático](../gestao-entregas-despacho-automatico/gestao-entregas-despacho-automatico.md) | Deixar o sistema agrupar e escolher sozinho |
| [Ler o mapa e o painel de entregas](../gestao-entregas-mapa-painel/gestao-entregas-mapa-painel.md) | O vocabulário da tela |
