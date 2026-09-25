# MEMÓRIA — #113 App do entregador: chegar no endereço

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `app-entregador-rota.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

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
- **As duas janelas modais (`10` e `12`) guardam o botão que as abriu no mesmo recorte.** Janela
  modal fotografada sozinha não diz de onde veio, e o leitor que chegou pelo FAQ precisa reconhecer
  a sequência — o toque, a folha, a janela — para saber que está na pergunta certa.
- **Nas duas janelas o botão da direita é alcançado pela direita.** CANCELAR/ABRIR MAPA e OK ficam
  no fim da linha de botões; seta entrando pela esquerda atravessaria o botão vizinho.
- **`11-duas-rotas.png` tem três marcadores por rota, nas mesmas três posições.** É a repetição que
  responde a pergunta sem precisar de frase: letra, contador e botão, duas vezes.

## As três fotos que chegaram depois, e o que elas mudaram no texto

As três capturas que faltavam vieram na segunda rodada
([`capturas-2/23-rota-com-problema/`](../gestao-entregas/material-recebido/app-entregador/capturas-2/README.md)),
e nenhuma das três entrou no FAQ: **nenhum manual deste repositório põe imagem em pergunta
frequente**, e abrir a exceção aqui deixaria o FAQ mais comprido que as três seções juntas. Cada
uma virou subseção onde o assunto já morava, e a pergunta do FAQ passou a apontar para a seção.

| Imagem | Onde entrou | O que o texto ganhou |
|---|---|---|
| `11-duas-rotas.png` | seção 2, *Duas rotas ao mesmo tempo* | a numeração das paradas **recomeça em cada rota** — dois cartões com o número 1 na mesma tela é esperado, e isso não estava escrito em lugar nenhum |
| `10-despacho-nao-confirmado.png` | seção 2, *Quando o restaurante não confirma a saída* | **não tocar em INICIAR ROTA de novo** antes de falar com a loja: se o primeiro toque chegou, o segundo avisa o cliente duas vezes |
| `12-melhor-rota-falhou.png` | seção 3, *Quando o cálculo não sai* | a mensagem é **Permissão necessária**, não *Ocorreu uma falha ao gerar a melhor rota* |

**A terceira é um achado, não um print errado.** Com o celular sem rede e a localização
concedida, o MELHOR ROTA responde *Permissão necessária · Permissão de localização é necessária
para continuar*. O `try/catch` do aplicativo embrulha a leitura do GPS **e** a chamada ao servidor
no mesmo `catch`, então falha de rede sai com o texto de permissão. O relatório de quem capturou
conferiu o outro caminho: quando o servidor responde e não consegue calcular, a janela é **Falha**
com a mensagem dele.

Resultado no manual: a seção 3 diz que a mensagem tem **duas** causas e manda conferir o sinal
antes da permissão, e o FAQ ganhou duas entradas no lugar de uma — *Permissão necessária* e
*Falha*, que são coisas diferentes com soluções diferentes.

> Vale um ajuste no aplicativo: separar o `catch` de rede do `catch` de GPS. Está registrado aqui
> porque é a única parte deste manual em que o texto tem de explicar um comportamento que é
> confuso por acidente, não por projeto.

## O que falta

Nada. As nove imagens da primeira rodada e as três da segunda cobrem as três seções e o FAQ.
