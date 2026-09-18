# O que a tela faz de verdade — #108 Fechar a entrega no painel

Lido em `beetech-server-node-2.0/docs/gestao-entrega-2.0/12-roteirizacao-manual.md`,
`14-pedido-entregue-no-painel.md` e `lovable/08-baixa-por-parada.md`, e conferido na sandbox
fechando a rota de verdade.

## As operações

| Ação na tela | Chamada |
|---|---|
| Visto da parada | `PUT /api/entrega2/gestao/rota/:rotaID/paradas/:preVendaID/entregar` |
| Botão de finalizar | `PUT /api/entrega2/gestao/rota/:rotaID/finalizar` |

As duas gravam `ENTREGUE` no ERP pelo mesmo orquestrador do despacho. A diferença é o alcance:
uma parada contra todas as paradas pendentes.

## Nenhuma das duas tem modal, e isso é decisão registrada

O prompt que criou a baixa por parada diz, em "o que não fazer": *"Nenhum modal de confirmação.
Finalizar a rota inteira, que é a ação maior, não tem modal; pedir confirmação para a menor
seria incoerente."*

Foi o que a sandbox confirmou: o clique no visto age, e o clique no finalizar age — a rota
fechou sem nenhuma pergunta. O manual não pode prometer uma rede de segurança que não existe, e
por isso o aviso do finalizar está em destaque.

Contra clique duplo existem duas defesas, nenhuma delas visual: a trava do hook no navegador e
o `jaEntregue: true` do backend, que responde sem reescrever nada.

## O que a baixa move além da parada

- `rota_parada.status` = `ENTREGUE`, com `dataHoraEntrega`.
- A próxima parada pendente é promovida a `EM_ROTA` — **e só quando nenhuma outra está
  `EM_ROTA`**. Daí a frase do manual: dar baixa fora de ordem não muda quem está sendo
  entregue agora.
- Quando não sobra parada pendente, a rota vai a `CONCLUIDA` com `dataHoraConclusao`, e o
  entregador é liberado. É por isso que o manual avisa que a última baixa encerra a rota
  sozinha.
- A tela seleciona a `proximaParada` que o backend devolve, e é isso que reposiciona o mapa.

## Entregar fora de ordem e em rota não despachada

Duas permissões deliberadas:

- **fora de ordem**: a sequência é sugestão, não contrato;
- **rota não despachada**: "quem entregou já entregou, e recusar obrigaria a despachar de
  mentira antes".

## Não existe insucesso

`INSUCESSO` existe no ENUM de `rota_parada` desde o schema inicial e **nada grava nele**. O
manual afirma isso como limite ("não existe 'não entregue'") em vez de sugerir um caminho que
a tela não tem.

## Por que a rota desaparece — e por que ela volta com o selo ligado

Duas peças que se somam, e juntas explicam a dúvida mais comum do manual:

1. `lerRotas` traz rota `CONCLUIDA` por uma **janela de 2 horas** depois da conclusão
   (`JANELA_CONCLUIDA_HORAS = 2`). Ela não é apagada da tela no ato.
2. O painel **esconde rota sem nenhuma parada visível**. Com o selo `entregues` desligado —
   que é o estado inicial — todas as paradas da rota concluída estão invisíveis, e a rota
   inteira desaparece com elas.

Medido na sandbox: com o selo ligado, o grupo *Entregues* mostrou **duas rotas concluídas, as
duas com código `A`** (uma de 109 min, outra de 56 min), mais os pedidos entregues soltos.
Confirma de uma vez a janela de 2 h, o reaproveitamento da letra e o motivo do desaparecimento.

Depois das 2 h a rota sai, mas o pedido entregue continua chegando por cerca de 6 h (janela da
view legada do ERP). Nesse intervalo ele fica no grupo *Entregues* sem rota — é o que o grupo
existe para resolver.

## O pedido no Delivery

`ENTREGUE` no ERP move o pedido para a coluna **ENTREGUE** do kanban de Delivery. O painel de
entregas e o kanban leem a mesma situação; não há sincronia separada para manter.

## Como o cenário foi montado

A rota `A` do #107 foi fechada de verdade: três baixas pelo visto (#1037, #1038, #1044) e o
botão de finalizar para a última (#1039). O clique no finalizar foi o que revelou a ausência de
modal — o script esperava uma janela de confirmação, ela não veio, e a rota fechou. O texto do
manual nasceu desse erro de expectativa.
