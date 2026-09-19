# Despachar a rota e acompanhar no mapa

**Despachar** é dizer ao sistema que o entregador saiu com os pedidos. É um clique, e é o
clique mais importante do módulo: ele não organiza a tela, ele **avisa o mundo**. O cliente
recebe mensagem, o marketplace recebe a baixa, a impressora imprime e a contabilidade do
pedido muda de estado.

Este manual começa onde
[Montar a rota](../gestao-entregas-montar-rota/gestao-entregas-montar-rota.md) parou: a rota
`A` montada, com quatro paradas e um entregador escolhido.

## Para que serve

- Mandar a rota para a rua e, com isso, avisar o cliente de que o pedido saiu.
- Acompanhar o entregador no mapa enquanto ele roda.
- Trocar o entregador depois de a rota já ter saído.
- Desfazer uma rota que saiu errada.

## Antes de começar

- A rota precisa estar montada, com pelo menos uma parada — veja
  [Montar a rota](../gestao-entregas-montar-rota/gestao-entregas-montar-rota.md).
- O entregador precisa estar **online no aplicativo** para você ver o percurso dele no mapa.
  Despachar para quem está offline funciona, mas o mapa fica sem o pino dele.
- Confira a cozinha. Despachar pedido que ainda está em preparo é permitido, e o resultado é
  o entregador esperando no balcão.

---

## 1. Leia isto antes de clicar

Despachar dispara, de uma vez, para **todos** os pedidos da rota:

| O que acontece | Quem sente |
|---|---|
| O pedido passa para **Em entrega** | A tela de Delivery, o caixa e o fechamento do dia |
| Sai a mensagem de **"pedido saiu para entrega"** | O cliente |
| O marketplace é avisado | iFood, Rappi, aiqfome, 99Food e os demais canais |
| A impressão de entrega é disparada | A impressora da loja |

> **Não existe botão de desfazer.** O cliente que recebeu "saiu para entrega" não recebe
> nenhuma correção depois, e o marketplace registra a baixa na hora. Despachar por engano se
> conserta por telefone, não pela tela.

Por isso a ordem certa é: cozinha pronta → entregador na porta → despachar. Nunca o
contrário.

---

## 2. Despachar a rota

No cabeçalho do grupo da rota há um botão de avião.

![A rota pronta para sair e o botão de despachar](imagens-tratadas/01-rota-pronta.png)

| Nº | Onde | O que é |
|----|------|---------|
| 1. | **Pronta para sair** | A rota está montada e ainda não saiu. |
| 2. | **Avião** | Despacha a rota. É o botão desta seção. |
| 3. | **em rota** | O selo do topo ainda está zerado: para o resto do sistema, nada saiu. |

O avião abre uma janela de confirmação. **Leia a janela** — ela é a última tela antes do
disparo, e é onde o sistema mostra o que você talvez não tenha olhado.

![A janela de confirmação do despacho](imagens-tratadas/02-confirmar-despacho.png)

| Nº | Onde | O que lê |
|----|------|----------|
| 1. | **O entregador X vai sair com N pedidos** | Quem leva e quantas paradas. Confira o nome: é ele que vai aparecer na mensagem do cliente. |
| 2. | **Lista das paradas** | Os pedidos na ordem da viagem, com cliente e endereço. |
| 3. | **Em preparo / Pronto** | A situação de **cada** pedido na cozinha. |
| 4. | **N pedidos ainda não estão prontos** | O aviso que aparece quando falta a cozinha terminar. Despachar assim fará o entregador esperar no restaurante. |
| 5. | **Os clientes serão avisados** | A frase que resume o disparo: a mensagem sai para todos os clientes da rota. |
| 6. | **DESPACHAR (F2)** | Confirma. Daqui em diante não volta. |

> **O sistema não impede despachar pedido em preparo.** Ele avisa e obedece. A decisão é sua
> — e às vezes é a certa, quando falta um item de dois minutos e o motoboy já está na porta.

---

## 3. O que muda no painel

No segundo seguinte, o painel inteiro muda de figura.

![A rota na rua](imagens-tratadas/03-rota-na-rua.png)

| Nº | Onde | O que mudou |
|----|------|-------------|
| 1. | **Na rua** | A situação da rota. Antes era *Pronta para sair*. |
| 2. | **Entregando agora** | O selo da parada que o entregador está fazendo **neste momento**. É sempre uma só. |
| 3. | **Botão de finalizar** | O avião deu lugar a ele. Está em [Fechar a entrega no painel](../gestao-entregas-fechar-entrega/gestao-entregas-fechar-entrega.md). |
| 4. | **em rota** | Subiu para o total de pedidos da rota. |
| 5. | **em preparação** | Desceu na mesma medida: os pedidos saíram da cozinha para a rua. |

Quatro coisas nesta tela contam a mesma história de ângulos diferentes — os selos do topo, a
situação da rota, o selo da parada atual e o pino no mapa. Quando uma delas discordar das
outras, o painel está com dado velho: use o botão de recarregar do topo.

---

## 4. Acompanhar o entregador no mapa

Com a rota na rua, o pino do entregador começa a andar. Ele vem do aplicativo: a posição é
enviada pelo celular dele, e o painel a lê a cada atualização.

![O entregador andando, a caminho da primeira parada](imagens-tratadas/04-entregador-na-rua.png)

| Nº | Onde | O que lê |
|----|------|----------|
| 1. | **Pino do entregador** | Onde ele está agora. Ao lado do pino aparecem o nome e há quanto tempo a posição foi recebida. |
| 2. | **N de N entregues · há X min** | O andamento da viagem e quanto tempo ela já leva. |
| 3. | **Entregando agora** | A parada atual. O mapa se reposiciona nela quando a anterior é dada como entregue. |
| 4. | **Rodapé de entregadores** | O contador mudou: quem estava *disponível* agora está *em rota*. |

Clicando no rodapé você vê a lista completa, agrupada por situação.

![A lista de entregadores com ele em rota](imagens-tratadas/05-lista-em-rota.png)

| Nº | Onde | O que lê |
|----|------|----------|
| 1. | **Em rota (N)** | Quem está com viagem aberta agora. |
| 2. | **Linha do entregador** | Há quanto tempo a posição chegou, a que distância do restaurante ele está e a bateria do celular dele. |

> **Sem aplicativo aberto não há pino.** A posição depende do celular do entregador enviando
> localização. Se o pino não anda e o horário ao lado dele envelhece, o problema é o
> aplicativo — não o painel. A bateria na lista costuma explicar.

---

## 5. Trocar o entregador com a rota na rua

O motoboy quebrou a moto, passou mal ou pegou a rota errada. Os três pontos da rota
resolvem.

![O menu da rota já despachada](imagens-tratadas/06-menu-na-rua.png)

| Nº | Onde | O que faz |
|----|------|-----------|
| 1. | **Três pontos** | Abre o menu da rota. |
| 2. | **Trocar entregador** | Passa a mesma viagem para outra pessoa. |
| 3. | **Remover entregador** | Deixa a rota na rua sem ninguém. Use quando não há substituto ainda. |
| 4. | **Excluir rota** | Desfaz a viagem inteira (seção 6). |

Em **Trocar entregador** você escolhe quem assume.

![Trocando o entregador de uma rota que já saiu](imagens-tratadas/07-trocar-entregador.png)

| Nº | Onde | O que faz |
|----|------|-----------|
| 1. | **Sem entregador** | Deixa a rota sem ninguém, sem apagar as paradas. |
| 2. | **Entregador atual** | Fica marcado, com a situação e a distância dele até o restaurante. |
| 3. | **A rota já está na rua** | O aviso da própria janela: a troca **reatribui os pedidos**, e é isso que vale no fechamento por entregador. |
| 4. | **SALVAR (F2)** | Confirma a troca. |

> **Trocar não avisa ninguém.** Nem o motoboy que perdeu a viagem, nem o que ganhou. O
> aplicativo mostra a lista dele atualizada na próxima vez que ele abrir a tela — e é por
> isso que trocar entregador é sempre dois passos: trocar na tela **e** ligar para os dois.

---

## 6. Quando a rota precisa ser desfeita

**Excluir rota** funciona mesmo depois de despachada. Existe de propósito: sem isso, uma rota
despachada por engano ficaria para sempre na tela.

O que acontece ao excluir uma rota que já saiu:

- Os pedidos **voltam** para *Pedidos sem rota*. Nada é cancelado.
- O entregador é liberado e volta a contar como disponível.
- **A situação do pedido não volta atrás.** Quem já foi avisado continua avisado; o pedido
  segue *Em entrega* no Delivery.
- O vínculo do motoboy com aqueles pedidos é apagado — some do fechamento por entregador.

> **Excluir não desfaz o despacho, desfaz o agrupamento.** Para o cliente e para o
> marketplace, o pedido continua tendo saído para entrega. Se ele na verdade não saiu, quem
> corrige isso é a tela de Delivery, pedido por pedido.

---

## Dicas

- **Despache com o motoboy na sua frente.** O disparo diz ao cliente que o pedido saiu; se o
  entregador ainda está tomando café, você já mentiu para o cliente.
- **Use o aviso de "não estão prontos" como conferência**, não como obstáculo. Ele existe
  para você descobrir agora, e não quando o motoboy voltar para buscar o que faltou.
- **Despachar duas vezes não faz nada.** O segundo clique é ignorado pelo sistema — não há
  risco de mandar duas mensagens ao cliente por clique repetido.
- **Confira o nome na janela.** O entregador que aparece ali é o que vai no aviso do cliente
  e no fechamento do dia.
- **Se o pino não anda, olhe a bateria.** A lista de entregadores mostra a bateria e a idade
  da última posição. Celular em economia de energia para de mandar localização.

---

## Onde continuar

| Manual | O que cobre |
|--------|-------------|
| [Fechar a entrega no painel](../gestao-entregas-fechar-entrega/gestao-entregas-fechar-entrega.md) | Dar baixa em cada parada e encerrar a rota |
| [Montar a rota](../gestao-entregas-montar-rota/gestao-entregas-montar-rota.md) | Agrupar os pedidos e escolher quem leva |
| [Despacho automático](../gestao-entregas-despacho-automatico/gestao-entregas-despacho-automatico.md) | Deixar o sistema agrupar sozinho — e por que ele **não** despacha |
| [Ler o mapa e o painel de entregas](../gestao-entregas-mapa-painel/gestao-entregas-mapa-painel.md) | O vocabulário da tela |
