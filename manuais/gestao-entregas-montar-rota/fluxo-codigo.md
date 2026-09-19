# O que a tela faz de verdade — #106 Montar a rota

Lido em `beefood-web-react` (`src/lib/api/gestaoEntregasRota.ts`,
`src/types/gestaoEntregas.ts`) e em
`beetech-server-node-2.0/docs/gestao-entrega-2.0/12-roteirizacao-manual.md`, e conferido
contra a API da sandbox.

## As operações e as rotas de API

| Ação na tela | Chamada |
|---|---|
| Criar rota | `POST /api/entrega2/gestao/rota` |
| Adicionar pedido | `POST /api/entrega2/gestao/rota/:rotaID/parada` |
| Remover pedido | `DELETE /api/entrega2/gestao/rota/:rotaID/parada/:preVendaID` |
| Reordenar (arrastar e *Otimizar ordem*) | `PUT /api/entrega2/gestao/rota/:rotaID/ordem` |
| Trocar/remover entregador | `PUT /api/entrega2/gestao/rota/:rotaID/entregador` |
| Excluir rota | `DELETE /api/entrega2/gestao/rota/:rotaID` |
| Marcar prontos | `PUT /api/entrega2/gestao/pedidos/prontos` |

Tudo grava em `rota` e `rota_parada` no Aurora `beefood-entregas` e deixa linha em
`rota_evento`. **Nenhuma dessas operações mexe na situação do pedido no ERP** — a única que
mexe é despachar, e é por isso que ela tem manual próprio.

## Criar rota não despacha, e isso é a decisão central do módulo

`situacao` da rota nasce `MONTANDO`/`ASSOCIADA` (o painel mostra **Pronta para sair**).
Nada é notificado, nada é impresso, o cliente não sabe. O botão de despachar é outro, e a
tela diz isso no texto da própria janela — o manual repete de propósito.

Efeito prático que o manual usa: **montar rota com pedido em preparo é normal**. Quem
decide a hora de sair é o operador, com a cozinha em vista.

## A letra da rota é reaproveitada

`rota.codigo` é a **menor letra livre entre as rotas ativas** da filial, não uma sequência.
Rota concluída devolve a letra. O documento do backend explica os dois motivos: sequência
que só cresce chegaria a `BQ` numa sexta movimentada, e zerar por data exigiria o fuso da
filial (às 21h em Brasília já é o dia seguinte em UTC, e as letras reiniciariam no meio do
jantar). O `ix_rota_codigo` **não é único** exatamente por isso.

Consequência para o manual: a letra identifica a viagem **na tela agora**. Para se referir a
uma entrega passada, o que identifica é o pedido.

> Na sandbox há três rotas do dia, todas com `codigo = A`. Não é bug: duas estão concluídas.

## Adicionar pedido joga no fim da fila

`POST .../parada` grava `ordem = max(ordem) + 1`. Não há inserção no meio: para pôr o pedido
novo antes, é reordenar depois. É por isso que o **Otimizar ordem** reaparece logo após
adicionar.

O menu de escolha da rota lista **também as rotas concluídas** — a API aceita. O manual
avisa para não usar, porque é o caminho para um pedido entrar numa viagem que já acabou.

## Otimizar ordem é vizinho mais próximo, a partir da loja

A reordenação é feita no cliente, por distância em **linha reta** (Haversine), partindo da
coordenada da loja e sempre pegando a parada mais próxima ainda não visitada. Não usa malha
viária, não considera trânsito, mão de direção nem tempo.

O botão só aparece quando a ordem atual difere da calculada. Medido na captura:

```
antes:  1 #1039 / 2 #1038 / 3 #1044 / 4 #1037
depois: 1 #1037 / 2 #1038 / 3 #1044 / 4 #1039
```

**O app desfaz.** O aplicativo do entregador tem *melhor rota*, que reordena por conta dele
— então a ordem montada aqui é uma sugestão, não um contrato. O manual diz isso porque é a
reclamação óbvia ("montei na ordem e ele foi na outra").

## O backend não diz "não" — de propósito

A primeira versão do backend tinha sete travas (parada entregue não sai, rota despachada não
é excluída, rota concluída não aceita alteração, despachar exige tudo pronto, pedido não
entra em duas rotas, ordem divergente é recusada, despachar duas vezes é erro). **Todas
foram removidas por decisão do dono do produto**, com o raciocínio de que quem está no
balcão às 20h de sexta sabe coisas que o banco não sabe, e que trava não impede o problema —
só obriga a resolver por fora.

Isso muda a redação do manual de duas formas:

1. Não se pode escrever "o sistema não permite". Ele permite.
2. O aviso passa a ser de **consequência**, não de impedimento: adicionar parada em rota na
   rua funciona, e o entregador não é avisado sozinho.

## Concorrência

A leitura da letra roda **dentro da transação, com `FOR UPDATE`**. Sem isso, dois operadores
criando rota no mesmo instante pegariam a mesma letra. Vale saber para o caso de suporte de
restaurante com dois computadores no painel.

## O que a tela **não** faz

- **Não** despacha (seção própria, #107).
- **Não** insere parada no meio da sequência.
- **Não** avisa o entregador de mudança em rota já despachada.
- **Não** calcula rota por rua nem tempo de viagem — a distância é em linha reta.
- **Não** impede pedido sem coordenada de entrar na rota: ele entra e não aparece no mapa.

## Cenário para as capturas

Montado com `manuais/gestao-entregas/scripts/cenario.js`, e a rota da captura foi criada
**pela tela**, não pela API — é o que o manual mostra.

```bash
node cenario.js estado                  # conferir o que há na tela
node cenario.js rota-excluir --rota 123  # começar do zero: o fluxo inteiro numa passada
node cenario.js presenca --entregador 194115 --status DISPONIVEL
node cenario.js andar --entregador 194115 --para -23.5061438,-47.4657927 --passos 1
python3 /tmp/ge/cap106final.py          # as nove capturas, com geometria
```

Três armadilhas de captura que valem para os próximos manuais do bloco:

1. **Menu flutuante não abre com `element.click()` via `evaluate`** — o componente escuta
   `pointerdown`. Tem de ser o clique do Playwright, com `force=True`.
2. **Menu flutuante sobre o mapa não sai no print**: o Leaflet compõe por cima no headless.
   Em vez de esconder o mapa (metade da imagem branca), subir o `z-index` do popper e baixar
   o das `.leaflet-pane` — o mapa fica na foto.
3. **Parar o ponteiro antes do print.** Depois de *Otimizar ordem* o botão desaparece e a
   primeira parada nasce embaixo do cursor, que troca o visto pelo "x" de remover.
