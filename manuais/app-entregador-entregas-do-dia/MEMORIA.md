# MEMÓRIA — #112 App do entregador: as entregas do dia e o histórico

## O recorte

Capítulos 03 (lista), 04 (detalhes) e 14 (histórico) do material do dono, num manual só. São as
três telas do **mesmo objeto**: a entrega. A lista é a entrega de longe, os detalhes são a entrega
de perto, e o histórico é a entrega depois de feita. Separá-los deixaria o entregador com três
páginas para entender um cartão.

Ficaram de fora, de propósito, duas coisas que aparecem nos prints:

| Fora | Onde está |
|---|---|
| O grupo de rota e a faixa **OUTRAS ENTREGAS ({N})** | #113 — a rota é assunto de lá |
| O botão **MELHOR ROTA GOOGLE MAPS** | citado aqui, explicado no #113 |

## A descoberta desta rodada: número contra número

A lista de entregas desenha os **próprios números** nos círculos das paradas. A primeira versão
pôs etiqueta verde numerada em cima disso, e a imagem ficou com **dois sistemas de numeração
concorrendo** — o leitor vê "1" verde apontando para "1" cinza e não sabe qual dos dois a tabela
está explicando.

Solução: a lista inteira entra por `passthrough()`, como contexto, e quem carrega as setas é um
**recorte de um cartão só**. O cartão isolado tem espaço para cinco etiquetas, e a numeração da
tela deixa de competir porque ela mesma virou o item 4 da tabela.

Vale para o histórico também, que numera do mesmo jeito. Lá eu mantive as setas porque são só
quatro e todas na margem, mas o texto avisa de quem é cada numeração.

## A margem da direita

O `!` vermelho de atraso vive na **coluna direita** do cartão do histórico. Alcançá-lo pela margem
esquerda obrigava a seta a atravessar o endereço inteiro na horizontal — a imagem ficava riscada.

Isso rendeu um `dire=` no `com_margem()` do miolo comum: margem clara também à direita, e a seta
entra por ali. A coluna direita da tela do app é onde moram a flecha `>`, o selo de estado e o
`!`, então a peça vai se repetir no #113, no #115 e no #116.

Na mesma rodada, `rec()` e `margem()` **saíram** dos arquivos de marcadores e foram para o miolo:
estavam copiados em dois manuais, e o terceiro ia copiar de novo.

## O que eu esperava e não era assim

| Eu esperava | O que é |
|---|---|
| A lista vir em ordem de chegada do pedido | Vem por **distância da loja**, crescente. Pedido sem coordenada cai no fim |
| O item preto ser só destaque visual de impressão | Ele **para o fluxo**: com destaque presente, cobrar e finalizar abrem primeiro uma folha de conferência |
| Campo sem valor aparecer com traço ou vazio | **Não aparece.** Sem complemento, sem observação e sem troco, a linha inteira desaparece — duas entregas têm alturas de tela bem diferentes |
| O histórico ter filtro de data | Não tem. O período vem do servidor; o aplicativo manda a data de hoje nos dois campos |
| A cobrança começar na lista | Não há botão de ação na lista, de propósito. Tudo mora nos detalhes |

O terceiro item foi o que mais mudou o texto: em vez de descrever a tela cheia e mencionar de
passagem, o manual mostra **as duas telas** — com complemento e sem — e diz a regra em negrito.
Entregador acostumado com a coluna TROCO acha que a tela quebrou quando ela não está lá.

## Decisões de imagem

- **Duas das dez imagens são recortes** de prints maiores: o cartão (da lista de quatro) e o
  rodapé escuro (dos detalhes). Nenhuma é captura nova, e nenhuma é montagem.
- **A folha de conferência vem antes do rodapé no texto**, embora o nome do arquivo seja `06` e o
  do rodapé `05`. A numeração dos arquivos seguiu a ordem de captura; a do texto segue o assunto.
  O `texto-documentation.ia.md` avisa disso explicitamente, porque quem publica tende a ordenar
  pelo nome.
- **Os nomes de cliente ficam visíveis.** Foram conferidos na base do sandbox antes de versionar:
  são sintéticos, semeados por script, sem telefone nem e-mail — laudo em
  [`../gestao-entregas/material-recebido/README.md`](../gestao-entregas/material-recebido/README.md).

## A segunda rodada trouxe uma seção inteira

Quatro prints da segunda rodada de capturas viraram a **seção 2 — A lista muda sozinha**, que não
existia. Eles não são variação das dez primeiras: são a lista **mudando**, e isso é um assunto, não
um detalhe de tela. Um quinto print chegou junto e **não virou imagem** — está em *As duas fotos que
saíram*.

| Print | O que mostra | Virou |
|---|---|---|
| `16-notificacoes/01-aviso-chegando` | o aviso do sistema por cima da lista | *O aviso de entrega nova* |
| `16-notificacoes/02-lista-depois-do-toque` | a lista recarregada, com o cartão novo | *Depois do toque* |
| `17-troca-de-entregador/01-aviso-de-remocao` | o aviso de que um pedido saiu | *O aviso de que uma entrega saiu* |
| `_triagem/lista-antes` + `17-.../02-lista-sem-o-pedido` | quatro cartões e três, lado a lado | *O que muda na lista* |
| `19-sem-internet/01-lista-sem-carregar` | a lista sem rede, sem erro nenhum | **texto só** — a imagem saiu |

Três coisas que só apareceram com as fotos na mão:

- **O aviso não diz qual pedido é.** Nem número, nem endereço, nem valor: *Novo pedido para você*
  e nada mais. A pergunta do FAQ mudou por causa disso — o entregador não tem como saber o que
  chegou sem abrir a lista.
- **Os círculos são renumerados quando alguém sai.** No par antes/depois, quem era 4 virou 3. Foi
  o argumento que faltava para a regra "combine pelo endereço, não pelo número da parada".
- **A pílula continua verde sem internet.** Achado que virou parágrafo, não imagem: a tela **não**
  avisa nada, o aplicativo repete o que carregou por último, e o jeito de descobrir de dentro do
  aplicativo é abrir um detalhe e ver se os itens do pedido vêm vazios.

**As duas imagens de notificação são as únicas do manual que guardam a barra do sistema.** Nelas a
barra não mostra relógio: mostra o ícone e o nome **BeeFood Entregador**, que é o que prova de quem
é o aviso. Nas outras o recorte começa abaixo dela.

## A data dos prints novos

Os prints da segunda rodada foram tirados na madrugada de 19/09/2026, dois dias depois dos
primeiros, e a lista mostra a previsão em letras vermelhas. Um manual que abre com `17/09/2026
23:44` na seção 1 e mostra `19/09/2026 01:50` na seção 2 não é o mesmo dia nem a mesma história.

[`../gestao-entregas/scripts/relogio.py`](../gestao-entregas/scripts/relogio.py) resolve
transplantando a linha de data do print da seção 1 para dentro dos novos — tinta do próprio
aplicativo, não texto redesenhado, porque a Roboto do Android não existe na máquina que monta as
imagens e qualquer `9` redesenhado apareceria como remendo. Só a linha da data muda.

## As duas fotos que saíram

`21-listas-vazias/02-historico-vazio` não é o histórico vazio: veio com **22 entregas em três
dias**. Seria uma boa segunda foto do histórico, e ficou fora por contradição — ela mostra
*Quinta 17/09 · 2 entregas* onde a imagem `08` deste manual mostra *3 entregas*. Entre os dois
prints o painel remanejou um pedido, e a diferença apareceria para quem comparasse as duas fotos.

O que ela ensinaria — **dia sem entrega não aparece na lista** — a imagem `08` já ensina: ela pula
15 e 16 de setembro.

`19-sem-internet/01-lista-sem-carregar` **entrou e saiu depois**, e essa é a parte que vale
guardar. Ela virou a imagem `15` e uma seção chamada *Quando a lista para de mudar*, com três
marcadores apontando a pílula verde, os cartões repetidos e o ATUALIZAR. O comentário que eu mesmo
escrevi no `annotate.py` dizia a verdade sem perceber: *"a imagem inteira é a mensagem: não há
mensagem"*. Uma foto de lista normal, com etiqueta explicando que ela é normal, não ensina nada —
o leitor não tem o que comparar, porque a tela sem rede e a tela com rede são a mesma tela.

O achado, que é bom, **ficou**: virou o parágrafo *Quando a lista não muda e você acha que
deveria*, com o teste dos itens do detalhe. Menos tela, mesma resposta.

> **O critério, que passou a valer para o bloco todo:** imagem entra quando o leitor **vê** algo
> que o texto não conta em duas linhas. Tela de erro com saída ganha imagem — a janela *Despacho
> não confirmado* do #113 ganhou, porque ela existe, é estranha e manda fazer algo. Tela de
> ausência e tela idêntica à normal, não ganham.

## O que falta

**Nada.** As duas capturas que este manual esperava chegaram na segunda rodada — a da entrega tirada
do entregador virou a seção 2 inteira, e a do histórico vazio veio com dado errado e está explicada
acima.

**E nada está pedido.** Chegou a existir uma segunda lista de capturas pedindo o histórico **realmente** vazio
e o aplicativo **abrindo** sem rede, e ela foi recusada na leitura, antes de virar trabalho de
alguém: *"que tipo de manual estamos fazendo? mostrar uma imagem de um aplicativo sem pedidos é
totalmente fora de realidade"*. Está certo, e vale para as duas. Quem procura o manual está com uma
entrega na mão; ninguém consulta manual para saber como é a tela quando não há nada nela, e ninguém
descobre pelo manual que está sem rede.

Para produzir a primeira dessas fotos eu tinha escrito dois comandos, `historico-zerar` e
`historico-voltar`, que **apagavam o histórico inteiro do entregador** e guardavam o desfazer em
arquivo. Funcionavam, e saíram junto com o pedido: reescrever o passado de um entregador de teste é
risco que uma imagem dessas não paga. O que sobrou é a correção que interessa, e ela está no
`smoke-app.js`: o caso `historico-vazio` só desatribui **o lote da execução**, e o Histórico do app
lê tudo o que aquele entregador já entregou, de qualquer dia. Foi por isso que o print voltou com 22
entregas.
