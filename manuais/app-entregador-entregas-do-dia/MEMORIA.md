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

## O que falta

Nada para publicar. Duas capturas pedidas em
[`../gestao-entregas/pedidos/capturas-app.md`](../gestao-entregas/pedidos/capturas-app.md) melhoram
este manual se chegarem:

| Captura pedida | Onde entraria |
|---|---|
| **Histórico vazio** (*Nenhuma entrega no período*) | a pergunta *O histórico está vazio* |
| **Entrega tirada do entregador** pelo painel | a pergunta *Uma entrega desapareceu sem eu fazer nada* |

O texto já descreve as duas situações; a foto só tornaria a leitura mais rápida.
