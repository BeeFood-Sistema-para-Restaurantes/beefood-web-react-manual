# O que a tela faz de verdade — Quanto o entregador recebe

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `entregador-quanto-recebe.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Lido em `beefood-reports-hub/src/components/reports/RelatorioEntregador.tsx` (1.170 linhas),
`beefood-web-react/src/components/VendaDetalhes.tsx`, `PedidoFields.tsx` e os controladores de
área de atendimento do servidor. Conferido na sandbox gravando valor, entregando e fechando a
conta.

## Onde o valor mora de verdade

O valor do entregador **não é lido da área de atendimento na hora do relatório**. Ele é
copiado para o pedido quando o endereço é resolvido (a mesma chamada que calcula frete e
distância devolve `valorEntregador`), e o relatório lê o pedido.

Consequência prática, que virou aviso no manual: mudar a área hoje não mexe no histórico, e
pedido criado antes de a área ter valor fica sem valor para sempre — a não ser que alguém
edite o pedido.

**Detalhe de implementação que importa para o suporte:** no pedido, esse valor é gravado numa
coluna reaproveitada (`taxaServicoValorDinheiro`), e não numa coluna com nome de entregador. O
endpoint de edição é `atualizaValorEntregador`, chamado pelo lápis do bloco *Entregador* na
tela do pedido. Quem for procurar o dado no banco não vai achar por nome.

## Os três modos são a lógica do Delphi antigo

`TIPO_LABELS` tem três entradas e o `getVisibleColumns` liga colunas diferentes em cada uma:

| Modo | Coluna que aparece | De onde vem o número |
|---|---|---|
| 0 — taxa paga pelo cliente | `Taxa Cliente` | frete do pedido |
| 1 — área de atendimento | `Taxa Entregador` (+ `(V)` e `(I+V)` com ida e volta) | valor do entregador do pedido |
| 2 — cadastro do funcionário | `KM (Ida)` (+ `(V)` e `(I+V)`) | distância × valor por KM do funcionário |

A escolha fica em `localStorage` (`bee_entregador_tipo`, `bee_entregador_ida_volta`): ela
**sobrevive ao recarregar**, o que é ótimo para a rotina e péssimo para o suporte — dois
usuários da mesma loja podem ver totais diferentes na mesma tela. O manual resolve isso com um
conselho ("escolha um modelo e fique nele") em vez de explicar `localStorage`.

## A coluna `KM (Ida)` carrega dinheiro, não distância

Medido: 86,30 km e R$ 1,50 por KM produziram `129,45` na coluna `KM (Ida)`. A distância
continua na coluna `KM`. O rótulo é herança do relatório antigo; como não dá para renomear pela
tela, o manual avisa em destaque.

## A diária

Linha própria na tabela de detalhes, detectada por `venda == null && qtdD > 0`. Uma diária por
**dia com entrega** do funcionário, no valor de `Valor Diária` do cadastro. Ela entra no total
de qualquer modo, somada por cima do valor das entregas.

O campo aceita no máximo `999,99` — descobri digitando `6000` e recebendo `999.99` de volta.
Os dois campos usam ponto decimal no `input` e não têm máscara de moeda.

## As duas contagens

| Relatório | Entregas no mesmo dia | O que conta |
|---|---|---|
| Entregador (Taxa / KM) | **15** | pedido de entrega do período, com ou sem entregador |
| Operação de Entrega | **13** | pedido **entregue** |

Os 2 de diferença apareceram como `Sem entregador`: pedidos em preparo, que ninguém pegou. Não
é divergência de conta, é recorte diferente — e é bom saber antes de alguém abrir chamado.

## Impressão

`PrintReportA4` monta uma seção por entregador mais o total geral; `PrintCupom` tem um painel
lateral (`ConfigCupomEntregadorForm`) que escolhe quais colunas vão para o cupom e permite
filtrar entregador. O Excel sai com duas visões (agrupado e detalhes), cada uma num arquivo.

## Como o cenário foi montado

1. Área de atendimento da sandbox já tinha `R$ 3,50` de entregador na única faixa de bairro.
2. `cenario.js` semeou os pedidos; o seeder grava frete, **mas não** valor do entregador — por
   isso os pedidos nasceram com *Não definido*, e por isso a foto 04 existe.
3. Gravei R$ 3,50 em três pedidos pelo lápis da tela do pedido (o resto ficou sem valor de
   propósito: é o que mostra a diferença na coluna).
4. Cadastro do entregador: diária R$ 60,00 e KM R$ 1,50.
5. Rota despachada e entregue pelo painel, para as entregas entrarem no dia.
