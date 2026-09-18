# MEMÓRIA — #113 App do entregador: chegar no endereço

## O recorte

Capítulos 05 (ver no mapa), 06 (rota do restaurante) e 07 (melhor rota) do material do dono, num
manual só. O material os separa porque são três telas; o entregador não tem três dúvidas, tem uma:
**"como eu chego lá?"**. A resposta é que existem três botões e eles não são equivalentes.

Por isso a página abre com uma tabela de três linhas antes de qualquer imagem. É o único manual do
bloco do aplicativo que começa por comparação em vez de por "para que serve" — e foi deliberado:
quem lê só o começo precisa sair sabendo **qual botão tocar**.

## A descoberta desta rodada: o botão verde é o irreversível

**INICIAR ROTA** parece o botão de abrir o mapa da rota. Ele é o **despacho**: muda a situação dos
pedidos, aparece no painel na hora, notifica o cliente e informa o marketplace — e só depois abre o
Maps. Pelo aplicativo não há desfazer.

Pior: quando o servidor não confirma, o aplicativo **abre o mapa de qualquer jeito** e mostra
*Despacho não confirmado*. É boa decisão de produto (não travar o motoboy na porta da loja), mas
significa que o entregador pode sair com o pedido sem que a loja saiba. O manual manda avisar a
loja, porque o aplicativo não tem como saber.

O contraste com o **ABRIR NO MAPS** (azul, depois de iniciado) é o que fecha a explicação: mesmo
lugar na tela, mesma rota, e esse pode ser tocado à vontade.

## Texto contra coordenada

Um detalhe de implementação que virou instrução de rua: o **VER NO MAPA** de uma entrega manda o
**endereço escrito** para o mapa, e quem procura o ponto é o Google Maps. As duas rotas mandam
**coordenada**.

Efeito colateral visível na captura: bairro com nome parecido com o de um estabelecimento faz o
mapa propor rota para o estabelecimento. O manual não explica geocodificação — diz **"confie no
cartão"**. É a única frase acionável na porta do prédio.

## O que eu esperava e não era assim

| Eu esperava | O que é |
|---|---|
| Os três botões serem atalhos para a mesma navegação | Um não dispara nada, um **despacha**, e um **reordena** só os avulsos |
| MELHOR ROTA cobrir tudo que está na tela | Cobre **só os pedidos soltos**. Rota montada pelo operador é ignorada — e reordenar desfaria o trabalho dele |
| O contador do cabeçalho contar os cartões da tela | Conta as paradas **da rota**. Daí o "de 3" com dois cartões visíveis, que parece bug e virou pergunta do FAQ |
| O Waze aparecer em todas as opções de mapa | Só na entrega única. URL com várias paradas é recurso do Google Maps |
| O botão da melhor rota aparecer sempre | Some com **uma** entrega: não há o que ordenar |

## Decisões de imagem

- **Quatro das nove imagens são telas do Google Maps**, não do aplicativo. Entram porque a dúvida
  do entregador é o que ele vê *depois* de tocar. A anotação se limita ao bloco de origem/destino e
  ao tempo — nada do mapa em si, que muda a cada captura.
- **`07` vem antes de `06` no texto.** A numeração dos arquivos seguiu a ordem de captura; o texto
  mostra primeiro o que o toque abriu e depois o que sobrou na tela. O `texto-documentation.ia.md`
  avisa, porque quem publica tende a ordenar pelo nome.
- **A lista inteira (`03`) entra sem seta**, como contexto, pelo mesmo motivo registrado no #112:
  o aplicativo numera as próprias paradas e duas numerações na mesma imagem confundem.
- **A margem da direita ganhou uso de verdade aqui.** O contador do cabeçalho fica encostado na
  borda direita; alcançá-lo pela esquerda riscava o nome da rota. O `dire=` que nasceu no #112 já
  entrou pronto — foi a primeira vez que uma peça do miolo comum se pagou sem ajuste.

## O que falta

Nada para publicar. Três capturas pedidas em
[`../gestao-entregas/pedidos/capturas-app.md`](../gestao-entregas/pedidos/capturas-app.md)
melhoram este manual se chegarem:

| Captura pedida | Onde entraria |
|---|---|
| A mensagem **Despacho não confirmado** | a pergunta do FAQ com o mesmo nome |
| **Duas rotas na mesma lista** (A e B) | a pergunta *Tenho duas rotas na tela* |
| **Ocorreu uma falha ao gerar a melhor rota** | a pergunta sobre a falha do cálculo |

O texto já descreve as três; a foto só tornaria a leitura mais rápida.
