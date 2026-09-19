# Apêndice 01 — Notificações

Como o app avisa que chegou entrega nova, e o que muda quando você toca no aviso.

## Quando chega uma notificação

O restaurante dispara a notificação quando um pedido ou uma rota é **atribuída a você** — e
também quando é **tirada de você**, o que acontece numa troca de entregador. É por isso que às
vezes chegam duas de uma vez.

O aviso aparece **mesmo com o app aberto**. Foi uma escolha: você pode estar no histórico ou
parado na lista sem perceber que ela mudou.

Não há contador no ícone do app. Ele envelheceria rápido — o pedido pode ser reatribuído em
segundos — e nada o zeraria.

## O que o app faz sozinho

Chegou a notificação, o app **recarrega a lista de entregas por baixo do aviso**, sem você pedir.
Quando você olha a tela, ela já está certa.

A notificação avisa *que* mudou; *o que* mudou vem do servidor. O app não usa o conteúdo do aviso
para alterar a lista — ele vai buscar a lista inteira de novo. Duas notificações juntas geram um
único carregamento.

## Ao tocar no aviso

Três coisas, nesta ordem:

1. Se havia uma tela de detalhes aberta, ela **fecha**.
2. A aba **Entregas** ganha o foco.
3. A lista recarrega.

A lista é o único destino possível, e não é limitação: é lá que estão tanto o pedido avulso
quanto a rota. O app não tem tela própria de rota.

**Com o app fechado**, o toque abre o app e você cai no fluxo normal — splash, lista. O atalho
para a aba pode não acontecer, porque o app ainda estava subindo quando o toque foi registrado.
O destino é o mesmo; você só não é levado direto.

## Se as notificações não chegam

1. Confira o cartão **Notificações** em Ajustes → Permissões (capítulo 15). Precisa estar
   **Ativa**.
2. Confira se você está **online** (capítulo 02). Offline, o restaurante não atribui entrega a
   você — e sem atribuição não existe notificação.
3. Economia de bateria agressiva, comum em Xiaomi, Samsung e Motorola, mata o app em segundo
   plano. Nas configurações do aparelho, marque o BeeFood Entregador como **sem restrição de
   bateria**.

Mesmo sem notificação alguma, **a lista não fica velha**: ela recarrega toda vez que você abre a
aba Entregas, e o botão de recarregar no cabeçalho força a atualização a qualquer momento.
