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

Cinco prints da segunda rodada de capturas viraram a **seção 2 — A lista muda sozinha**, que não
existia. Eles não são variação das dez primeiras: são a lista **mudando**, e isso é um assunto, não
um detalhe de tela.

| Print | O que mostra | Virou |
|---|---|---|
| `16-notificacoes/01-aviso-chegando` | o aviso do sistema por cima da lista | *O aviso de entrega nova* |
| `16-notificacoes/02-lista-depois-do-toque` | a lista recarregada, com o cartão novo | *Depois do toque* |
| `17-troca-de-entregador/01-aviso-de-remocao` | o aviso de que um pedido saiu | *O aviso de que uma entrega saiu* |
| `_triagem/lista-antes` + `17-.../02-lista-sem-o-pedido` | quatro cartões e três, lado a lado | *O que muda na lista* |
| `19-sem-internet/01-lista-sem-carregar` | a lista sem rede, sem erro nenhum | *Quando a lista para de mudar* |

Três coisas que só apareceram com as fotos na mão:

- **O aviso não diz qual pedido é.** Nem número, nem endereço, nem valor: *Novo pedido para você*
  e nada mais. A pergunta do FAQ mudou por causa disso — o entregador não tem como saber o que
  chegou sem abrir a lista.
- **Os círculos são renumerados quando alguém sai.** No par antes/depois, quem era 4 virou 3. Foi
  o argumento que faltava para a regra "combine pelo endereço, não pelo número da parada".
- **A pílula continua verde sem internet.** É a foto que resolve a pergunta mais frequente do
  suporte, e ela resolve dizendo que a tela **não** avisa: o aplicativo repete o que carregou por
  último. Os dois sinais que sobraram — itens vazios no detalhe, pílula que não responde — são a
  única forma de descobrir de dentro do aplicativo.

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

## O print que não entrou

`21-listas-vazias/02-historico-vazio` não é o histórico vazio: veio com **22 entregas em três
dias**. Seria uma boa segunda foto do histórico, e ficou fora por contradição — ela mostra
*Quinta 17/09 · 2 entregas* onde a imagem `08` deste manual mostra *3 entregas*. Entre os dois
prints o painel remanejou um pedido, e a diferença apareceria para quem comparasse as duas fotos.

O que ela ensinaria — **dia sem entrega não aparece na lista** — a imagem `08` já ensina: ela pula
15 e 16 de setembro.

## O que falta

**Nada que impeça publicar.** As duas capturas que este manual esperava chegaram na segunda rodada —
a da entrega tirada do entregador virou a seção 2 inteira, e a do histórico vazio veio com dado
errado e está explicada acima.

**Duas melhoras estão pedidas, e nenhuma bloqueia:** as pastas 27 e 28 de
[`capturas-app-2.md`](../gestao-entregas/pedidos/capturas-app-2.md) pedem o histórico **realmente**
vazio e o aplicativo **abrindo** sem rede. Hoje as duas perguntas são respondidas por texto, e o
texto está certo — *O histórico está vazio* descreve uma frase no meio de uma tela branca, e *A lista
não carrega* descreve o aplicativo já aberto, que é o caso comum. O que falta nos dois é imagem, não
resposta.

A pasta 27 é a única da rodada que sai **só de emulador e banco**. A 28 depende de um **build de
release** do repositório do app: release embute o bundle JavaScript no APK e não procura o Metro, então
o aplicativo abre sem rede — no build de desenvolvimento ele morre antes de qualquer tela, que é o
motivo registrado no relatório da rodada passada. A primeira versão do pedido mandava buscar o APK na
Play Store, o que não cabe no que a outra ponta tem.

A pasta 29 pede os fontes de `views/historico/index.js` e `views/entregas/index.js`, para conferir de
primeira mão duas coisas que hoje este manual afirma pelo estudo do material: que a tela do histórico
**não tem filtro de data** e o que a lista faz sem rede.

O pedido da pasta 27 só existe porque o da rodada passada voltou errado, e o erro era do pedido: o
caso `historico-vazio` desatribui os pedidos **do lote da execução**, e a tela lê tudo o que aquele
entregador já entregou. Daí os comandos `historico-zerar` e `historico-voltar` do
[`smoke-app.js`](../gestao-entregas/scripts/smoke-app.js), que zeram o histórico inteiro e guardam o
desfazer — exercitados aqui de ponta a ponta antes de virar pedido.
