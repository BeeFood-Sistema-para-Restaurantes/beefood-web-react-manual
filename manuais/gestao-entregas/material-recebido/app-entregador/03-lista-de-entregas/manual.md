# Manual 03 — A lista de entregas

Esta é a tela onde você passa o turno. Cada cartão é uma entrega no seu nome, e a ordem em
que eles aparecem já é a ordem que faz sentido rodar.

O cenário deste capítulo: quatro entregas abertas, todas com o mesmo pedido —
`1x Combo One Burger`, com One Burger, batata frita e Coca Cola 350ml dentro.

---

## A lista

[Entender a lista](01-lista-quatro-entregas.md)

![Quatro entregas na lista](prints/01-lista-quatro-entregas.png)

## Como ler um cartão

| Onde | O que é |
|---|---|
| **#1026**, etiqueta laranja | o número do pedido |
| **Previsão Entrega** com o relógio vermelho | quando o pedido está prometido ao cliente |
| **O endereço**, em preto e grande | rua, número, bairro, cidade, CEP e complemento |
| **Cobrar R$ 46,00**, em verde | o que você recebe na porta |
| **O número no círculo**, à esquerda | a posição da entrega na sequência |
| **A flecha `>`**, à direita | abre os detalhes ([manual 04](../04-detalhes-da-entrega/manual.md)) |

A **faixa vermelha** e a linha que ligam os círculos desenham a sequência: é a mesma ideia de
um roteiro, de cima para baixo.

## A ordem não é por chegada

A lista vem **ordenada pela distância da loja**, do mais perto para o mais longe. No exemplo:
1 km, 1,4 km, 1,8 km e 2,7 km. Pedido sem coordenada cai no fim.

Isso significa que a lista já é uma sugestão de roteiro, e não a ordem em que os pedidos
foram feitos.

> Quando o restaurante monta uma rota para você, a ordem passa a ser a que **ele** definiu —
> veja o [manual 06](../06-rota-do-restaurante/manual.md).

## O fim da lista

[Entender o rodapé](02-fim-da-lista.md)

![Fim da lista](prints/02-fim-da-lista.png)

Depois do último cartão aparece o **ATUALIZAR** cinza, e o botão azul **MELHOR ROTA GOOGLE
MAPS (4)** fica fixo acima das abas — o número entre parênteses é a quantidade de paradas que
ele vai abrir de uma vez ([manual 07](../07-melhor-rota/manual.md)).

## O que a lista não mostra

Ela mostra o endereço e o valor, mas **não** os itens do pedido, o telefone do cliente nem a
forma de pagamento. Isso está nos detalhes, a um toque de distância.

Também não aparece aqui nenhum botão de finalizar ou cobrar: essas ações vivem dentro dos
detalhes, para você não baixar a entrega errada com um toque no lugar errado.

## Atualizar

Três formas, todas equivalentes: puxar a tela para baixo, tocar em **ATUALIZAR**, ou sair e
voltar para a aba **Entregas** (o app recarrega sozinho ao voltar).

Quando chega pedido novo pela notificação, o app já faz isso por você: abre em Entregas, fecha
o detalhe que estiver aberto e recarrega a lista.

## Se algo não funcionar

**Uma entrega que você já fez continua na lista.** Provavelmente a finalização não chegou ao
servidor. Abra o detalhe e confira; se o botão de finalizar ainda estiver lá, ela não foi
baixada.

**Uma entrega desapareceu sem você fazer nada.** O restaurante pode tê-la passado para outro
entregador ou cancelado o pedido. O histórico só guarda o que **você** entregou.

**A lista está vazia e você espera pedido.** Veja o [manual 01](../01-primeiros-passos/09-entregas-vazia.md):
o app mostra apenas o que está atribuído ao seu nome.
