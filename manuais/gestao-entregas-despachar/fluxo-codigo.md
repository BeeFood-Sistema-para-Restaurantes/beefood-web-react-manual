# O que a tela faz de verdade — #107 Despachar e acompanhar

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `gestao-entregas-despachar.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Lido em `beetech-server-node-2.0/docs/gestao-entrega-2.0/12-roteirizacao-manual.md` e
`14-pedido-entregue-no-painel.md`, e conferido contra a sandbox no dia da captura.

## A operação

| Ação na tela | Chamada |
|---|---|
| Despachar | `PUT /api/entrega2/gestao/rota/:rotaID/despachar` |
| Trocar/remover entregador | `PUT /api/entrega2/gestao/rota/:rotaID/entregador` |
| Excluir rota | `DELETE /api/entrega2/gestao/rota/:rotaID` |

Despachar é a **única** operação de roteirização que mexe na situação do pedido no ERP. Criar,
adicionar, remover, reordenar e trocar entregador não mexem — é a fronteira que separa este
manual do #106.

## Por que o manual abre com uma seção de aviso

`situacaoDelivery` nunca é um `UPDATE` direto. A alteração passa pelo orquestrador
(`alteraSituacaoDelivery.js`, 1.146 linhas), que no mesmo caminho dispara:

- WhatsApp para o cliente;
- fila de impressão;
- baixa de estoque;
- socket para as telas abertas;
- sincronia com iFood, Rappi, aiqfome, UaiRango, DeliveryMuch, 99food e Keeta;
- integradoras de entrega (Foody, LetsExpress, PickNGo, Agilizone, Machine, UberDirect);
- caixa e cartão.

Ou seja: o clique de despachar é o clique com mais efeito colateral do módulo, e o manual não
teria como ser honesto colocando isso numa nota de pé de página. Daí a seção 1 vir **antes**
das instruções.

O alcance é a **rota inteira, de uma vez**: `ENTREGA` é gravado para todos os pedidos da rota.
Não existe despachar meia rota.

## Despachar não confere se os pedidos estão prontos

Decisão de produto registrada no backend: a checagem ficou **na tela**, como aviso. O modal
traduz o `status` de cada pedido que o painel já tem em mãos e conta quantos não estão
prontos; o servidor não recusa. É o que o manual chama de "o sistema avisa e obedece".

## O que o despacho faz nas paradas

- Todas as paradas vão para `DESPACHADO`.
- A primeira da ordem é promovida a `EM_ROTA` — é o selo **Entregando agora**.
- `EM_ROTA` não sobe para o ERP: ele existe só no Aurora, porque o ERP não tem como dizer
  "esta é a parada de agora" quando `ENTREGA` já valeu para as dez.

Quem move o `EM_ROTA` daí em diante é a baixa por parada, do #108.

## Repetir a operação não é erro

Despachar duas vezes é no-op: sem parada pendente para promover, o backend não reescreve nada
e não chama o orquestrador de novo. O manual promete isso ("despachar duas vezes não faz
nada") porque é a defesa contra clique duplo — não há modal de "tem certeza?" para isso.

## Excluir rota despachada é permitido de propósito

Era o único beco sem saída de verdade do módulo: rota na rua que não podia ser desfeita. A
trava caiu. O efeito prático que o manual descreve:

- os pedidos voltam para *Pedidos sem rota*, sem cancelar nada;
- o `FuncionarioIDMotoboy` no ERP é limpo — o vínculo com o entregador desaparece do
  fechamento;
- a `situacaoDelivery` **não** volta atrás. Quem foi avisado continua avisado.

## Trocar entregador com a rota na rua

A tela avisa que "reatribui os pedidos no ERP", e é literal: o motoboy gravado no pedido
muda. Nada é notificado ao aplicativo — **push é Fase 8 e não existe**. O aplicativo do
entregador descobre a mudança quando ele reabre a lista, por polling.

É por isso que o manual manda ligar para os dois entregadores. Não é zelo: é a única forma de
o motoboy saber.

## O pino do entregador

A posição vem do app, é gravada pela Lambda de rastreamento em `entregas.posicao` e o painel a
lê junto com o resto. O rótulo ao lado do pino mostra a **idade** da última posição, e a
lista de entregadores mostra bateria e distância até o restaurante.

Consequência que o manual usa como dica: pino parado com idade crescendo é problema de
celular, não de painel.

## Como o cenário foi montado

O entregador da sandbox é simulado. Quem move o pino é
`manuais/gestao-entregas/scripts/cenario.js andar`, que escreve em `entregas.posicao` e
atualiza `entregador_status` — exatamente o que a Lambda faz quando o app manda posição. Sem
isso não haveria como fotografar o mapa em movimento.
