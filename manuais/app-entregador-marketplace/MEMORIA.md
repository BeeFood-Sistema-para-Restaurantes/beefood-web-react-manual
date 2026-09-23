# MEMÓRIA — #115 App do entregador: pedido de iFood e de 99Food

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `app-entregador-marketplace.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

## O recorte

Capítulos 09 (iFood) e 10 (99Food) do material do dono, num manual só. O material os separa, e o
próprio capítulo 10 fecha com uma tabela "iFood e 99Food, lado a lado" — sinal de que os dois já
queriam ser um.

Juntar rendeu duas coisas que separados não davam: a **imagem da lista serve os dois** (o print do
material tem os dois pedidos, um embaixo do outro) e a **tabela comparativa** deixou de ser
apêndice para virar seção.

## A descoberta desta rodada: o código da tela pode não ser o código do site

No 99Food, a faixa do aplicativo mostra o código que **veio no pedido** — 6 dígitos na captura — e
a página da plataforma pede, com todas as letras, *um localizador de 8 dígitos, que está no
recibo*. Os dois números não são a mesma coisa.

O material do dono registrou isso em vez de esconder, e o manual promoveu a nota a aviso
destacado. É o erro que chega no suporte como "o 99Food diz que o código não existe".

No iFood o problema não existe: o localizador que chega no pedido tem 8 dígitos e é exatamente o
que a página pede.

## O que eu esperava e não era assim

| Eu esperava | O que é |
|---|---|
| O botão de confirmação aparecer em todo pedido de marketplace | Aparece só onde a plataforma exige prova de entrega própria. Keeta, por exemplo, traz **só o selo** |
| O aplicativo preencher o site da plataforma | Ele **copia** o código; quem cola é o entregador. Não há automação |
| Finalizar no aplicativo fechar também a plataforma | São **dois registros**. A confirmação é prova de entrega; o FINALIZAR é a baixa no restaurante e a sincronia de situação |
| O rodapé perder só o valor a cobrar | Perde o **bloco de ações inteiro**: sem INICIAR COBRANÇA e sem FINALIZAR SEM COBRAR, sobra FINALIZAR |
| A tela de confirmação ser uma tela do aplicativo | É um **site embutido**. Só a faixa de cima é do aplicativo — e é por isso que o manual descreve a página pelo texto que ela mostra, não por posição |

O último item mudou a forma de escrever a seção: nada de "toque no campo da direita", e sim "os
oito quadradinhos" e "o botão que a página chama de Continuar". Se a plataforma redesenhar a
página, o manual sobrevive.

## Decisões de imagem

- **Uma imagem para as duas plataformas** (`01`). Foi sorte do material: o print da lista tem o
  pedido de iFood e o de 99Food juntos, com os dois selos. Nenhuma montagem.
- **Cada tela de detalhes rendeu duas imagens** — o miolo (observação e selo) e o rodapé escuro.
  Na tela inteira, os dois assuntos ficam a 200 px de distância, e a imagem única obrigava a
  etiqueta a atravessar os itens do pedido.
- **`COBRAR R$ 0,00` é alcançado pela direita**, com o `dire=` do miolo comum. É a segunda coluna
  do rodapé: seta pela esquerda atravessaria o `TOTAL` e o valor do pedido, que é justamente o
  número que não se deve cobrar.
- **Os dois avisos de cópia entram lado a lado** (`09`), montados com `lado_a_lado()`. Separados,
  são "uma faixa verde de sucesso", duas vezes; juntos, mostram a única diferença que existe entre
  eles, que é o texto. As coordenadas dessa imagem são escritas à mão — `rec()` só sabe falar de
  um print.
- **A numeração dos arquivos segue a ordem do texto** (iFood inteiro, 99Food inteiro, comparação no
  fim). Nos dois manuais anteriores a ordem dos arquivos brigou com a do texto e o
  `texto-documentation.ia.md` precisou avisar; aqui não precisou.

## As duas que chegaram e viraram seção

As duas capturas pedidas chegaram na segunda rodada, e em vez de ilustrar duas perguntas do FAQ
viraram a **seção 6 — Dois casos fora do roteiro**. O motivo é o mesmo nos dois casos: a resposta
tem passo a passo, e passo a passo não cabe numa linha de pergunta.

| Print | Virou | O que a foto acrescentou |
|---|---|---|
| `19-sem-internet/02-plataforma-nao-carrega` | *A página da plataforma não abre* | a divisão da tela: **a faixa de cima é do aplicativo, o resto é do site**. É o que separa "pedido errado" de "sem sinal", e não estava escrito em lugar nenhum |
| `24-plataforma-sem-confirmacao/01-selo-keeta` | *O pedido de plataforma que não pede confirmação* | que **a cor do selo não identifica a plataforma**: o da Keeta é amarelo igual ao do 99Food, e quem identifica é a marca dentro do selo |

A segunda mudou também a seção 1, que descrevia os selos por cor. Ganhou uma linha dizendo que a
marca dentro do selo é o que vale.

Duas decisões de imagem:

- **A tela em branco entra recortada na metade.** A imagem inteira seria 70% de nada. O recorte
  guarda a faixa do aplicativo e um pedaço do branco — o suficiente para a etiqueta 2 apontar para
  o vazio, que é o assunto.
- **O pedido da Keeta começa abaixo da linha de *Realizado às***. Essa linha traz data e hora, e o
  print é de dois dias depois dos outros do manual. Cortando ali, nenhuma data aparece na imagem e
  nada precisou ser mexido — foi o caminho mais barato que o `relogio.py`.

## O que falta

Nada. As duas capturas que este manual esperava chegaram e estão publicadas.
