# MEMÓRIA — #116 App do entregador: receber na porta

## O recorte

Capítulos 11 (cobrança), 12 (divisão de conta) e 13 (finalizar sem cobrar) do material do dono,
num manual só. São os três desfechos possíveis do **mesmo momento**: o entregador na porta, com a
sacola entregue e o dinheiro por resolver.

Separá-los criaria a pior das páginas: um manual de cobrança que não diz o que fazer quando não há
o que cobrar. O material já apontava para a junção — o capítulo 13 começa mandando o leitor ao 11,
e o 12 diz que "tudo acontece na mesma tela do 11".

Treze imagens, o maior do bloco do aplicativo. Se algum manual merece esse tamanho é este: é o
único em que um toque errado move dinheiro.

## A frase que organizou o manual

**"Cobrar é finalizar."** Não é didática, é literal: o envio do pagamento dá a baixa da entrega na
mesma operação. Ela virou o primeiro bloco de aviso da página, antes de qualquer imagem, porque
explica de uma vez:

- por que a tela de sucesso diz *Pagamento Confirmado!* e a entrega desaparece da lista;
- por que não existe "cobro agora e finalizo depois";
- e por que o estado *"o pagamento foi registrado, finalize a entrega"* é a exceção, não a regra.

## O que eu esperava e não era assim

| Eu esperava | O que é |
|---|---|
| A forma de pagamento ser escolhida sempre no mesmo lugar | Com **uma** pessoa, a folha de formas abre **depois** do CONFIRMAR PAGAMENTO. Na **divisão**, cada bloco tem o campo na tela. Muda a ordem do caminho, não só o layout |
| A forma prevista vir marcada também na divisão | **Não vem.** Com a conta dividida o aplicativo não tenta adivinhar quem paga como |
| Existir trava de pagamento repetido | **Não existe** no servidor. A proteção é o botão bloqueado durante o envio — e é por isso que o manual manda *conferir no histórico*, nunca "tentar de novo" |
| A bandeira do cartão ser obrigatória | É **opcional**, e a própria folha diz que a taxa se resolve pela forma. O manual vai além e dá a regra: na dúvida, siga sem |
| O troco ser só informação | Vem **preenchido** com o que o cliente pediu, e é editável na hora — é o campo mais provável de precisar correção na calçada |
| Fiado aparecer na lista de formas | Fica fora **de propósito**, com Pix automático e as formas de marketplace. Não é dinheiro trocando de mão na calçada |

O item da trava foi o que mais mudou o texto. A instrução natural depois de um erro é "tente de
novo"; aqui ela produziria uma segunda cobrança. O manual diz o contrário, em negrito.

## Decisões de imagem

- **Quase toda imagem é um recorte de folha.** A cobrança acontece em folhas que sobem por cima da
  tela de pagamento, e a parte de cima da tela aparece escurecida em todos os prints. Recortar a
  folha, e não a tela inteira, foi o que deixou o texto legível em treze imagens seguidas.
- **A tela de pagamento (`03`) é a única inteira**, com oito etiquetas. Ela é o mapa da operação, e
  o vazio no meio dela é real: com uma pessoa pagando, a tela é assim.
- **O rodapé usou as três margens ao mesmo tempo** (`01`), primeira vez no bloco: esquerda para a
  primeira coluna e os botões, direita para o `COBRAR` em verde, e uma margem **em cima** só para a
  coluna do meio (`TROCO`), que não tem lado livre nenhum. A seta dela desce vertical, por um
  corredor sem texto.
- **A tela de sucesso entra sem seta** (`08`). Uma marca verde e uma frase não pedem etiqueta, e a
  única etiqueta possível apontaria para o texto que a legenda já repete.
- **Duas setas foram remontadas** depois da primeira rodada: o tique da forma escolhida (`04`), que
  atravessava a folha inteira na horizontal e agora entra pela direita, e o contador de caracteres
  (`13`), cuja ponta cobria exatamente o número que ela explicava.

## O que falta

Nada para publicar. Quatro capturas melhorariam o manual, e estão pedidas em
[`../gestao-entregas/pedidos/capturas-app.md`](../gestao-entregas/pedidos/capturas-app.md):

| Captura pedida | Onde entraria |
|---|---|
| **A soma precisa ser R$ …** (aviso vermelho da divisão) | o bloco de aviso da seção 3 |
| **Não foi possível cobrar**, com mensagem do servidor | a pergunta *Erro ao confirmar* |
| **Pedido já pago** | a pergunta com o mesmo nome |
| **Pagamento registrado, falta finalizar** | a pergunta *Registrou o pagamento e a entrega continuou na lista* |

As quatro são telas de erro, e o texto já descreve todas. Nenhuma é bloqueante — mas as quatro
juntas transformariam o FAQ numa seção ilustrada, que é o formato que o suporte usa.
