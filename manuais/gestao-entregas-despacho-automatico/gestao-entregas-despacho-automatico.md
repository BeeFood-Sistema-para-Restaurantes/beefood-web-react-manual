# Despacho automático: as sete regras

O despacho automático faz duas coisas: **junta os pedidos em rotas** e **escolhe o
entregador**. Ele não manda ninguém para a rua — despachar continua sendo um clique seu.

Isso é de propósito, e é a primeira coisa a entender: uma rota que saísse sozinha avisaria o
cliente de que o pedido está em rota antes de alguém ter pegado as sacolas.

## Para que serve

- Poupar o operador de montar rota a rota em hora de pico.
- Agrupar pelo critério que **você** escolher: quantidade, distância e tempo de espera.
- Escolher o entregador por proximidade, em vez de por ordem de chegada.

## Antes de começar

- Você precisa de pedidos de delivery sem rota e de pelo menos um entregador **online e com
  GPS recente**.
- A tela de Gestão de Entregas precisa ficar **aberta** em algum computador da loja.
- Os pedidos precisam ter endereço com coordenada, se você usar a regra de distância.

---

## 1. O que ele é, e os dois avisos da janela

Clique na engrenagem ao lado do selo **Despacho** no topo da tela.

![A janela do despacho automático e os dois avisos](imagens-tratadas/01a-janela-avisos.png)

| Nº | Onde | O que diz |
|----|------|-----------|
| 1. | **Explicação do topo** | Os pedidos são agrupados e atribuídos a um entregador. **A rota não sai sozinha.** |
| 2. | **Interruptor** | Liga e desliga. Nasce desligado. |
| 3. | **Enquanto esta tela estiver aberta** | O agrupamento só roda com o painel aberto em algum computador do restaurante. Painel fechado, pedidos esperando. |
| 4. | **Pedidos com mais de 2 horas** | Pedido antigo **nunca** é agrupado, e esse limite não é configurável. |

> **Painel fechado, despacho parado.** Não é um serviço que roda no servidor da loja: quem dá
> o pulso é a tela aberta. Se a loja fecha o navegador no fim do almoço, o agrupamento para
> ali.

> **O limite de 2 horas protege você.** Ao ligar o interruptor numa loja com pedidos
> acumulados, sem ele a primeira rodada montaria rota com pedido de horas atrás — que na
> prática já foi resolvido por fora.

---

## 2. As sete regras

São sete campos, em duas colunas: o que **junta** os pedidos e o que **escolhe** o entregador.

![As sete regras do despacho automático](imagens-tratadas/01b-janela-regras.png)

| Nº | Regra | O que faz |
|----|-------|-----------|
| 1. | **Máximo de entregas por viagem** | Quantos pedidos cabem numa mesma rota. É o teto. |
| 2. | **Distância máxima para agrupar (metros)** | Distância entre os pedidos. Em branco, a regra não vale. |
| 3. | **Tempo máximo para agrupar (minutos)** | Diferença de tempo de espera entre os pedidos. Em branco, a regra não vale. |
| 4. | **Liberar o entregador quando os pedidos estiverem** | *Finalizados*: uma viagem por vez. *Em trânsito*: ele já recebe a próxima rota enquanto está na rua. |
| 5. | **Raio do restaurante (metros)** | O entregador precisa estar a essa distância da loja para receber rota. `0` não exige proximidade. |
| 6. | **Considerar a posição do entregador** | Escolhe quem está mais perto da **primeira parada**, e não apenas quem está mais perto da loja. |
| 7. | **Tolerância de GPS (minutos)** | Idade máxima da última posição recebida. Acima disso o entregador é ignorado. `0` não exige GPS recente. |

Três coisas que a janela não explica e mudam o resultado:

- **O agrupamento começa pelo pedido que espera há mais tempo.** Quem chegou primeiro sai
  primeiro, e por isso pedido em bairro vazio não fica para trás indefinidamente.
- **A distância é conferida contra todos os pedidos já no grupo**, não só contra o primeiro.
  Sem isso, três pedidos a 3 km um do outro formariam uma rota de 6 km de ponta a ponta.
- **A ordem das paradas é refeita depois de o grupo fechar**, pelo trajeto mais curto saindo
  da loja. A ordem de agrupamento não é a ordem de entrega.

---

## 3. Ligar

Vire o interruptor e salve.

![O interruptor ligado](imagens-tratadas/02-janela-ligada.png)

| Nº | Onde | O que faz |
|----|------|-----------|
| 1. | **Interruptor** | Ligado. |
| 2. | **Despacho automático ligado** | O texto ao lado confirma o estado — é o que você confere depois. |
| 3. | **SALVAR (F2)** | Grava as regras **e** o estado do interruptor. Sem salvar, nada vale. |

Com ele ligado, o selo do topo fica verde e o rodapé da lateral passa a dizer *Despacho
automático ligado*. São os dois lugares onde se confere sem abrir a janela.

---

## 4. A rota nasce sem entregador

Poucos segundos depois, a rota aparece na lateral — e ela **não tem dono ainda**.

![A rota criada automaticamente, ainda sem entregador](imagens-tratadas/03-rota-automatica.png)

| Nº | Onde | O que lê |
|----|------|----------|
| 1. | **Sem entregador** | Em itálico, com um ícone ao lado: foi o sistema que montou esta rota. |
| 2. | **Montando** | A situação da rota enquanto ela ainda não tem entregador. |
| 3. | **Pedidos sem rota** | Diminuiu: os pedidos agrupados saíram do grupo. |
| 4. | **Despacho ligado** | O selo verde do topo. |

Isso não é meio caminho nem falha: são **duas etapas separadas**, e você vê a rota se formando
antes de ela ganhar dono — dá tempo de intervir, mexer nas paradas ou escolher outra pessoa à
mão.

---

## 5. O entregador entra depois

A segunda etapa acontece quando as regras de entregador são satisfeitas.

![A rota com o entregador escolhido pelo sistema](imagens-tratadas/04-rota-associada.png)

| Nº | Onde | O que mudou |
|----|------|-------------|
| 1. | **Nome do entregador** | O sistema escolheu, e não está mais em itálico. |
| 2. | **Pronta para sair** | A rota saiu de *Montando*. |
| 3. | **Avião** | Apareceu — e **é aqui que o automático para**. Despachar é seu. |
| 4. | **prontos** | Os três pedidos ficaram prontos na cozinha, e foi isso que liberou a escolha. |

**Se a rota fica em *Montando* e não ganha entregador**, a causa é uma destas quatro, na
ordem em que aparecem na prática:

| Causa | Como conferir |
|---|---|
| Os pedidos ainda não estão prontos, com a regra em *Finalizados* | O selo **prontos** do topo, e a situação de cada pedido |
| A última posição do entregador é velha demais | A lista de entregadores mostra há quanto tempo ela chegou; compare com a **tolerância de GPS** |
| O entregador está longe da loja | A mesma lista mostra a distância; compare com o **raio do restaurante** |
| Ele já está com outra viagem, e a regra é *Finalizados* | O rodapé mostra quantos estão *em rota* |

> **Foi a tolerância de GPS que segurou a nossa rota.** Tudo estava pronto e o entregador
> estava na porta da loja, e a rota continuou sem dono: a última posição dele tinha mais de
> cinco minutos. Bastou o celular mandar posição nova para a escolha acontecer no minuto
> seguinte. Entregador com GPS velho é ignorado de propósito — o sistema não confia numa
> posição que pode ser de outro bairro.

---

## 6. Desligar

Mesma janela, mesmo interruptor, e **salve**. Desligar não desfaz nada do que já foi montado:
as rotas criadas continuam na tela, com entregador e tudo, esperando o seu despacho.

---

## Dicas

- **Comece com regra apertada.** Máximo de 2 entregas e distância curta produzem rotas que
  você consegue conferir. Depois vá afrouxando.
- **Deixe o *Tempo máximo* em branco no começo.** É a regra que mais barra agrupamento sem
  ficar claro por quê.
- **Use *Em trânsito* só com entregador sobrando.** Ele recebe a próxima rota ainda na rua, e
  isso é ótimo com fila de pedidos — e péssimo com um entregador só.
- **Raio do restaurante `0` combina com *Considerar a posição*.** Um libera quem está longe da
  loja, o outro garante que a escolha ainda faça sentido geográfico.
- **O automático não substitui o olho.** Ele agrupa por distância em linha reta, sem saber de
  rio, viaduto ou avenida sem retorno. Confira a rota antes de despachar.

---

## Onde continuar

| Manual | O que cobre |
|--------|-------------|
| [Despachar e acompanhar](../gestao-entregas-despachar/gestao-entregas-despachar.md) | O clique que o automático não dá |
| [Montar a rota](../gestao-entregas-montar-rota/gestao-entregas-montar-rota.md) | Fazer à mão o que ele faz sozinho |
| [Liberar o entregador](../gestao-entregas-liberar-entregador/gestao-entregas-liberar-entregador.md) | Cadastro e acesso ao aplicativo — sem isso não há GPS |
| [Ler o mapa e o painel de entregas](../gestao-entregas-mapa-painel/gestao-entregas-mapa-painel.md) | O vocabulário da tela |
