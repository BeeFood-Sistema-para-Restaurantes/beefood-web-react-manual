# Ler o mapa e o painel de entregas

A **Gestão de Entregas** é uma tela só, com duas metades: o **mapa**, à esquerda, e a
**lista de rotas**, à direita. Tudo que o restaurante faz com entrega acontece aqui —
agrupar pedidos numa viagem, escolher quem sai, acompanhar quem está na rua e dar baixa em
quem chegou.

Este manual é o primeiro do grupo e não manda você mexer em nada: ele ensina a **ler** a
tela. Montar rota, despachar e fechar entrega têm manual próprio, e os três presumem que
você já sabe o que está vendo aqui.

## Para que serve

- Saber, numa olhada, quantos pedidos estão em preparo, prontos, na rua e entregues.
- Ver no mapa **onde** cada pedido precisa chegar e **onde** cada entregador está agora.
- Saber quais entregadores estão disponíveis, em pausa, na rua ou fora do turno.
- Encontrar um pedido específico sem procurar na lista.

## Antes de começar

- Você precisa de um usuário com acesso à tela **Gestão de Entregas**.
- O restaurante precisa ter o **endereço cadastrado com o pino no lugar certo**: é dele que
  saem a posição da loja no mapa e a distância de cada entregador até você. Se o pino
  estiver errado, tudo que este painel calcula sai errado —
  veja [Endereço do restaurante](../endereco-restaurante/endereco-restaurante.md).
- Os entregadores aparecem no mapa **só depois de entrar no aplicativo**. Entregador
  cadastrado que nunca usou o app aparece na lista, mas sem posição.
  [Liberar o entregador](../gestao-entregas-liberar-entregador/gestao-entregas-liberar-entregador.md)
  é o manual desse preparo.

---

## 1. Abrir o painel

O caminho é **Delivery**, e de lá o botão **Entregas (1)** na barra de cima.

![O botão Entregas na tela Delivery](imagens-tratadas/01-porta-delivery.png)

| Nº | Onde | O que faz |
|----|------|-----------|
| 1. | **Entregas** | Abre a Gestão de Entregas. A tela de Delivery continua existindo e serve para outra coisa: lá você mexe em **um** pedido; aqui você organiza a **viagem**. |

> **Deixe esta tela aberta durante o serviço.** Ela se atualiza sozinha a cada poucos
> segundos, e o **despacho automático** (quando ligado) só agrupa pedidos enquanto o painel
> estiver aberto em algum computador do restaurante.

---

## 2. As duas metades da tela

![O painel de Gestão de Entregas](imagens-tratadas/02-painel-inteiro.png)

| Nº | Onde | O que é |
|----|------|---------|
| 1. | **Pesquise por rota, pedido ou cliente** | Filtra a lista **e** o mapa ao mesmo tempo. Serve para achar um pedido pelo número, pelo nome do cliente ou pela letra da rota. |
| 2. | **Pedidos sem rota** | O grupo de quem ainda não entrou em nenhuma viagem. É daqui que sai toda rota nova. O número ao lado é a quantidade. |
| 3. | **Pino da loja** | Onde o sistema acha que o restaurante está. Toda distância e todo trajeto saem deste ponto. |
| 4. | **Contagem de entregadores** | Quantos estão disponíveis, na rua, em pausa e fora do turno. Clicando, abre a lista completa. |
| 5. | **Camada do mapa** | Troca o desenho do mapa: **Claro**, **Ruas**, **Humanitário** ou **Satélite**. |
| 6. | **Centralizar mapa** | Volta o mapa para o enquadramento que mostra a loja e os pedidos. Útil depois de arrastar ou dar muito zoom. |

Cada pedido aparece **duas vezes**: como cartão na lista da direita e como pino no mapa. É
a mesma informação em duas leituras — a lista responde "quais pedidos eu tenho", o mapa
responde "onde eles estão".

> Quando um pino fica fora do enquadramento, aparece uma **bolinha com número na borda do
> mapa**, apontando a direção e dizendo quantos pedidos estão para aquele lado. É o aviso
> de que existe entrega longe o bastante para sair da tela.

---

## 3. Os selos do topo

A faixa em cima do mapa é o resumo do dia e, ao mesmo tempo, o filtro.

![Os selos de situação e a pílula do despacho](imagens-tratadas/03-selos.png)

| Nº | Selo | O que conta |
|----|------|-------------|
| 1. | **em preparação** | Pedido aceito, ainda sendo feito na cozinha. |
| 2. | **prontos** | Pedido pronto, esperando alguém levar. **É o que você olha para montar rota.** |
| 3. | **em rota** | Pedido que já saiu com um entregador. |
| 4. | **entregues** | Pedido que chegou ao cliente hoje. |
| 5. | **Despacho desligado / ligado** | Diz se o sistema está agrupando pedidos sozinho. Clicando, abre as regras — está em [Despacho automático](../gestao-entregas-despacho-automatico/gestao-entregas-despacho-automatico.md). |
| 6. | **Recarregar** | Força uma atualização agora. Ao lado dele, o "há N s" mostra quanto tempo passou desde a última. |

**Os quatro primeiros selos são botões.** Clicar em um deles **esconde** aquela situação do
mapa e da lista; clicar de novo traz de volta. Num dia cheio, desligar *em preparação* e
*entregues* deixa na tela só o que precisa de decisão.

![Com "em preparação" desligado, os pedidos em preparo saem do mapa e da lista](imagens-tratadas/05-filtro-preparacao-off.png)

> O selo apagado fica com o texto mais claro e sem preenchimento. Se a tela parecer "vazia
> demais", confira aqui antes de achar que perdeu pedido: é o esconderijo mais comum.

---

## 4. Quem está na rua

Clique na contagem de entregadores (a seta 4 da imagem da seção 2) para abrir a lista
completa, agrupada por situação.

![A lista completa de entregadores](imagens-tratadas/04-lista-entregadores.png)

| Nº | Onde | O que lê |
|----|------|----------|
| 1. | **Entregadores (N)** | Todos os funcionários marcados como entregador, mesmo os que nunca usaram o app. |
| 2. | **Disponível (N)** | Está no turno e pode receber rota. |
| 3. | **Linha do entregador** | Quando a última posição chegou, a que distância do restaurante ele está e a bateria do celular. |
| 4. | **Offline (N)** | Encerrou o turno ou nunca entrou. |
| 5. | **Nunca usou o app** | Cadastrado, mas sem nenhum acesso ao aplicativo. Aparece aqui para você saber que falta liberar. |

As situações possíveis são quatro:

| Situação | Significa | Recebe rota? |
|----------|-----------|--------------|
| **Disponível** | No turno, sem viagem | sim |
| **Em rota** | Com viagem em andamento | depende da regra do despacho automático |
| **Em pausa** | No turno, em intervalo | não |
| **Offline** | Fora do turno | não |

**Quem muda essa situação é o entregador, no aplicativo dele** — não há como colocar alguém
disponível pelo painel. O que o painel faz é mostrar, e recusar dar rota a quem não está.

> **"há N min" é a idade da última posição, não do último toque.** Um número grande ali
> quer dizer que o celular parou de mandar GPS: sem sinal, sem bateria ou app fechado.
> Entregador com posição velha some do mapa mas continua na lista — e o despacho automático
> pode ignorá-lo, conforme a tolerância configurada.

---

## 5. Achar um pedido

Digite no campo de busca (a seta 1 da imagem da seção 2). Ele aceita:

- o **número do pedido**, com ou sem `#`;
- o **nome do cliente**, ou parte dele;
- a **letra da rota** (`A`, `B`, …).

![A busca filtrando a lista e o mapa](imagens-tratadas/07-busca.png)

A lista e o mapa reagem juntos: o que sobrar na lista é o que continua desenhado. Apague o
campo para ver tudo de novo.

---

## 6. Trocar o desenho do mapa

O botão no canto de baixo (a seta 5 da imagem da seção 2) tem quatro opções.

![As quatro camadas do mapa](imagens-tratadas/06-camadas-mapa.png)

| Camada | Quando ajuda |
|--------|--------------|
| **Claro** | Padrão. Menos informação no fundo, os pinos aparecem mais. |
| **Ruas** | Nome de rua legível — bom para conferir um endereço duvidoso. |
| **Humanitário** | Mais detalhe de caminho e acesso. |
| **Satélite** | Foto aérea. Ajuda em condomínio, chácara e endereço sem nome de rua. |

A escolha vale só para o seu computador.

---

## Dicas

- **A tela precisa ficar aberta.** O despacho automático agrupa enquanto o painel estiver
  aberto em algum computador. Fechada a tela, os pedidos esperam.
- **Pedido sem endereço geolocalizado não aparece no mapa** — só na lista. Quando a
  contagem do mapa não fecha com a da lista, é isso.
- **Distância é em linha reta**, não pela rua. Serve para comparar ("este está mais perto
  que aquele"), não para calcular tempo de viagem.
- **A bateria do celular do entregador aparece na lista** por um motivo prático: celular
  abaixo de 15% costuma parar de mandar GPS antes de a viagem terminar.
- **Não use o painel para um pedido só.** Para mexer em um pedido isolado — mudar endereço,
  trocar pagamento — o lugar continua sendo a tela de Delivery.

---

## Onde continuar

| Manual | O que cobre |
|--------|-------------|
| [Liberar o entregador](../gestao-entregas-liberar-entregador/gestao-entregas-liberar-entregador.md) | Cadastro, acesso ao app e código de barras no cupom |
| [Montar a rota](../gestao-entregas-montar-rota/gestao-entregas-montar-rota.md) | Juntar pedidos numa viagem e escolher quem leva |
| [Despachar e acompanhar](../gestao-entregas-despachar/gestao-entregas-despachar.md) | Mandar a rota para a rua e seguir o entregador |
| [Fechar a entrega no painel](../gestao-entregas-fechar-entrega/gestao-entregas-fechar-entrega.md) | Dar baixa quando o pedido chega |
| [Despacho automático](../gestao-entregas-despacho-automatico/gestao-entregas-despacho-automatico.md) | Deixar o sistema agrupar e escolher sozinho |
