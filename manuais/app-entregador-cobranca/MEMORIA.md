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
- **A tela de pagamento (`03`) é a única inteira**, com nove etiquetas. Ela é o mapa da operação, e
  o vazio no meio dela é real: com uma pessoa pagando, a tela é assim.
- **A etiqueta 1 aponta o selo `PEDIDO #1030`**, acrescentada depois de fechar o #117: esta é a
  **única tela do aplicativo que mostra o número do pedido**, e a tabela não dizia nada sobre o selo
  que estava ali na imagem. O crachá do cartão e o dos detalhes leem `numeroPedido` (nulo em pedido
  do restaurante) e vêm só com o `#`; este selo lê `numeroPreVenda`. A seta vem pela direita porque
  o selo mora encostado na borda.
- **O rodapé usou as três margens ao mesmo tempo** (`01`), primeira vez no bloco: esquerda para a
  primeira coluna e os botões, direita para o `COBRAR` em verde, e uma margem **em cima** só para a
  coluna do meio (`TROCO`), que não tem lado livre nenhum. A seta dela desce vertical, por um
  corredor sem texto.
- **A tela de sucesso entra sem seta** (`08`). Uma marca verde e uma frase não pedem etiqueta, e a
  única etiqueta possível apontaria para o texto que a legenda já repete.
- **Duas setas foram remontadas** depois da primeira rodada: o tique da forma escolhida (`04`), que
  atravessava a folha inteira na horizontal e agora entra pela direita, e o contador de caracteres
  (`13`), cuja ponta cobria exatamente o número que ela explicava.
- **As três telas de resultado da seção 6 (`15`, `16` e `17`) entram inteiras, com o vão do meio.**
  Recortar o título e colar os botões embaixo deixaria a imagem mais compacta e mentiria sobre a
  tela: ela é uma marca, uma frase e um botão no pé, com muito espaço vazio entre eles — e é esse
  vazio que faz o entregador procurar um botão que não existe.
- **A `18` guarda o rodapé de propósito**, mesmo com a janela no alto: é o rodapé que faz cobrar em
  dobro, e ele é o quarto marcador da imagem.

## As quatro fotos de erro chegaram, e viraram uma seção nova

As quatro capturas pedidas vieram na segunda rodada, mais duas telas de trabalho que a IA que
capturou guardou por conta própria — as duas mais valiosas do lote. **O FAQ não recebeu imagem
nenhuma:** nenhum manual do repositório põe foto em pergunta frequente, e quatro fotos ali deixariam
o FAQ maior que as quatro seções juntas. Nasceu a **seção 6, *Quando a cobrança não fecha***, e cada
pergunta do FAQ passou a apontar para ela.

| Imagem | De onde veio | Onde entrou |
|---|---|---|
| `14-soma-nao-fecha.png` | `22-erros-de-cobranca/01` | seção 4, embaixo do bloco de aviso da soma |
| `15-erro-no-pagamento.png` | `22-erros-de-cobranca/02` | seção 6 |
| `16-pedido-ja-pago.png` | `22-erros-de-cobranca/03` | seção 6 |
| `17-pagamento-sem-baixa.png` | `22-erros-de-cobranca/04` | seção 6, primeira das três da sequência |
| `18-pagamento-registrado.png` | `_triagem/pos22.png` | seção 6, segunda |
| `19-nao-foi-possivel-dar-baixa.png` | `_triagem/pos22d.png` | seção 6, terceira |

### As três coisas que as fotos ensinaram, e que o texto não sabia

**A tela de sucesso do caso sem baixa é igual à do pagamento normal.** Mesma marca verde, mesmo
*Pagamento Confirmado!*. A única diferença é a frase de baixo: *Finalize a entrega — o dinheiro já
está no caixa* em lugar de *registrado com sucesso*. Sem a foto lado a lado com a `08` isso não
apareceria, e é a informação que decide o que o entregador faz em seguida.

**O rodapé não recarrega.** Ao reabrir os detalhes da entrega paga-e-não-baixada, o `COBRAR` continua
mostrando o valor cheio em verde e o `INICIAR COBRANÇA` continua clicável. **É o caminho que cobra em
dobro**, e virou o aviso mais forte da seção nova. Só se vê na `18`.

**A primeira tentativa de FINALIZAR falha.** O `pos22d` mostra *Não foi possível dar baixa* com o
FINALIZAR atrás — e a pergunta do leitor nesse ponto é "eu apertei o botão errado?". A resposta é
não: a lista do aplicativo está velha. A saída é atualizar a lista e finalizar de novo, o que o
relatório de captura confirmou.

**A soma que não fecha rendeu uma regra a mais:** editar o valor de uma pessoa **não** reajusta o da
outra. O aplicativo divide em partes iguais uma vez, quando as pessoas são criadas; depois disso a
conta é do entregador. É por isso que o print tem R$ 5,00 + R$ 9,95 e o aviso vermelho embaixo.

### Como a foto do `22/04` foi produzida

Está no relatório de quem capturou, e vale registrar porque o pedido a marcava como "talvez não
saia": em vez de tentar cortar a rede entre dois pedidos HTTP, **a rota foi excluída no painel** com
a folha *Confirmar cobrança?* aberta no celular. O pagamento entrou (rota não tem nada com o caixa) e
a baixa falhou, porque o aplicativo mandou o identificador de uma rota que não existia mais. O
estado é exatamente o que o FAQ descrevia: dinheiro no caixa, entrega aberta.

## 2026-09-25 — o parâmetro chegou, e virou a seção 1

O sistema ganhou **Entregador registra pagamento**, no card **Delivery** de Configuração →
Parâmetros. Desligado, o aplicativo do entregador não tem tela de pagamento. Pedido do dono:
*"além de incluir essa sessão no manual devemos tbm incluir na FAQ para o SEO do MCP encontrar a
informação"* e *"é bom ja começar esse manual com a configuração no topo, pra ficar bem claro"*.

**A configuração foi para a frente de tudo, como seção 1**, e as seis seções antigas andaram uma
casa (2 a 7). Foi a decisão mais barata e a mais certa: o manual todo descreve um modo de operar
que pode estar desligado, e descobrir isso no fim da página é descobrir tarde. A seção 2 abre com
um bloco dizendo, em uma linha, que dali em diante o manual fala do modo ligado.

**A seção 1 fala com outro leitor.** O resto do manual é para o entregador, na porta do cliente;
esta é para quem configura, no computador. Em vez de criar um manual novo, o texto assume a troca
de interlocutor e volta ao entregador no fim da seção — o parâmetro é curto demais para uma página
inteira, e separá-lo deixaria o manual do dinheiro sem dizer se a tela existe.

### O FAQ ganhou um bloco com nome

Dez perguntas novas, agrupadas sob o subtítulo **A tela de pagamento do aplicativo**, e o FAQ antigo
virou **A cobrança, no dia a dia**. As dez são, de propósito, **a mesma pergunta de dez jeitos** —
"como desativar", "como liberar de novo", "não abre a tela", "o aplicativo diz que está desativado",
"dá para desligar só para um" —, porque é assim que o dono e o entregador procuram, e é o que o
prompt de publicação agora manda não juntar.

Duas delas responderam a perguntas que o texto da seção não responderia sozinho: **desliguei e o
entregador continua vendo o valor** (está certo, e é de propósito) e **desliguei e ele cobrou mesmo
assim** (o aplicativo estava aberto desde antes).

### A vigésima imagem, e o que ela não é

Uma só, e do navegador: o card **Delivery** inteiro, com as **duas** chaves. Fotografar só a nova
economizaria espaço e perderia o ponto — os nomes são parecidos, a de cima tem manual próprio
(#43), e confundir as duas é o erro previsível. Por isso a etiqueta 2 aponta a vizinha para dizer
*não é esta*.

**Nenhuma imagem nova do aplicativo.** O dono cortou: *"não precisamos de nenhuma imagem do
aplicativo entregador android/ios extra"*. A tela que o aplicativo mostra com a chave desligada é
descrita em texto, e o `fluxo-codigo.md` registra que ela veio de print do dono e não de leitura de
código — o repositório do aplicativo não está ao nosso alcance.

**A captura é somente leitura.** Na sandbox a chave já estava desligada, provavelmente pelo dono
testando o aplicativo, e o `capturar-parametro.py` não toca em interruptor nenhum: a foto saiu como
estava e o texto diz que o padrão de fábrica é ligado. O prompt de publicação avisa que isso não é
erro de captura, para ninguém "consertar" a imagem depois.

**O `annotate.py` ganhou margem em memória** para esta imagem. O ajudante antigo, `margem()`, grava
a margem dentro da pura — inofensivo nas dezenove do aplicativo, porque o `copiar()` reconstrói a
pura do material versionado a cada execução, e defeito nesta, que é capturada e não se reconstrói. É
o mesmo defeito encontrado no #125.

## O que falta

Nada. Vinte imagens, as quatro perguntas mais usadas pelo suporte com tela, e a configuração que
liga tudo isso na frente da página.
