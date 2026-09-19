# Bastidores — #117 Uma entrega do começo ao fim

O que sustenta o texto do manual: os estados por onde o pedido passa, quem escreve cada um, e o que
cada escrita dispara. Este arquivo existe porque o #117 afirma coisas sobre **as duas telas ao mesmo
tempo**, e afirmação dessas só se defende olhando o que é gravado.

Fonte: `~/refs/beetech-server-node-2.0/docs/gestao-entrega-2.0/` (o clone é do `2.0`, a pasta é do
`3.0`), mais o que foi medido nas rodadas #104 a #116 e pela conferência do
[`smoke-app.js`](../gestao-entregas/scripts/smoke-app.js), que lê a API do próprio aplicativo.

## Dois bancos, dois vocabulários

O módulo vive em dois lugares, e é isso que explica quase todo desencontro entre as telas.

| Onde | O que guarda | Vocabulário |
|---|---|---|
| **MSSQL** (`notafacilb`), tabela `_PreVenda` | o pedido, que é documento fiscal | `situacaoDelivery`: `PREPARO` → `PRONTO` → `ENTREGA` → `ENTREGUE` |
| **Aurora** (`entregas`) | a rota, as paradas, a presença e a posição | `rota.status`: `CRIADA` → `ASSOCIADA` → `EM_ROTA` → `CONCLUIDA` / `CANCELADA` |

`situacaoDelivery = 'ENTREGA'` significa **saiu para entrega**, não entregue. É a confusão de nome
que a própria documentação do backend marca como armadilha, e a razão de o manual nunca usar a
palavra "entrega" sozinha.

O estado da **parada** (`PENDENTE` / `EM_ROTA` / `ENTREGUE`) vive só no Aurora: no ERP, o despacho já
valeu para a rota inteira, então não há equivalente do lado fiscal. É por isso que o contador *1 de 3*
existe no painel e no aplicativo, e não no relatório fiscal.

## O que põe o pedido na tela do celular

Uma coluna: **`_PreVenda.FuncionarioIDMotoboy`**. A lista do aplicativo sai da função
`funcSelect_Entregador_Pedidos3(empresaID, funcionarioID)`, e ela filtra por essa coluna e pela
situação — `AGUARDANDO` e `ENTREGUE` ficam fora.

Três consequências, e as três aparecem no texto do manual:

1. **Pedido pronto e sem entregador não existe para o aplicativo.** É o momento 1 do manual.
2. **A rota aparece no celular antes de qualquer despacho.** Criar a rota com entregador escolhido já
   grava a coluna, e a rota em `ASSOCIADA` é devolvida pela API do aplicativo. Conferido: o caso
   `rota-viva` do smoke test passa com `status` diferente de `DESPACHADA` e três paradas na tela.
3. **Tirar a entrega do entregador é apagar a coluna.** Não há cancelamento nem estado intermediário:
   o pedido desaparece da lista dele na próxima leitura.

## O despacho, e por que ele não tem volta

O despacho é uma chamada só — `PUT /gestao/rota/:rotaID/despachar` — que grava
`situacaoDelivery = 'ENTREGA'` em todos os pedidos da rota. E essa escrita passa pelo
`SituacaoDeliveryUpdater`, que é o orquestrador de 1.146 linhas do ERP:

| O orquestrador dispara | Consequência que não volta |
|---|---|
| notificação aos sete marketplaces integrados | a plataforma registra a baixa na hora |
| enfileiramento do WhatsApp de saída | o cliente recebe a mensagem |
| impressão de entrega | o cupom sai na impressora |
| socket para as telas abertas | o Delivery e o caixa mudam |
| log no `beetech.log` | uma linha por pedido |

**A mesma chamada é a do aplicativo.** O `INICIAR ROTA` foi aberto para o app em 29/08, por decisão
explícita de produto — *"como no concorrente"* —, e usa o mesmo endpoint. O risco foi aceito com o
argumento de que a alternativa era pior: o entregador na moto com o painel dizendo que nada saiu.

Por isso o manual diz que o botão verde do celular e o avião do painel são **a mesma coisa**. Não é
simplificação didática, é o mesmo `PUT`.

> Despachar duas vezes não reavisa ninguém: o `alterarSituacaoPedidos` conta como sucesso o pedido
> que já está no estado de destino. É o que permite acrescentar uma parada a uma rota já despachada.

### O terceiro caminho: o código de barras

Ler a etiqueta do cupom com a câmera chama o mesmo caminho de despacho. É o assunto do #114, e a
razão de o manual afirmar que **ler é despachar** — a leitura não confere nada, ela move o estado.

## A rua: a única fase sem escrita de estado

Entre o despacho e a porta do cliente, nada muda de estado. O que acontece é o aplicativo mandando
posição, que a Lambda de rastreamento grava em `entregas.posicao` e resume em
`entregas.entregador_status` (`ultimaLatitude`, `ultimaLongitude`, `dataHoraUltimaPosicao`,
`distanciaLojaMetros`).

O painel lê esse resumo. Daí as duas frases do manual:

- **pino parado não é entregador parado** — a lista mostra bateria e idade da última posição, e
  celular em economia de energia simplesmente para de mandar;
- o pino existir **depende do aplicativo rodando**. Despachar para quem está offline funciona; o
  mapa é que fica sem o pino.

O aviso de **entregador próximo** (WhatsApp tipo 33) sai de um cron que compara
`distanciaLojaMetros` com `_WhatsappMsgTipoFilial.raioProximidadeMetros`. Filial com raio `NULL` é
**pulada** — e o raio estava NULL em 56.633 das 56.639 filiais quando isso foi medido, inclusive na
sandbox. O campo mostra `2` na tela porque `2` é o padrão do código, não o que está gravado. Abrir o
aviso e salvar uma vez grava. É o achado do #110, e a razão de o manual dizer "pode sair" em vez de
"sai".

## A porta do cliente: cobrar é finalizar

No aplicativo, registrar o pagamento e dar baixa são uma transação só. A API de pagamento grava, no
mesmo caminho, o valor recebido, a forma e a baixa da parada — não existe estado "pago e não
entregue" que o entregador possa alcançar de propósito.

Existe por acidente: quando o pagamento entra e a baixa não volta. O aplicativo detecta e avisa que o
dinheiro já está no caixa, pedindo para finalizar. É a única situação em que as duas coisas se
separam, e é a pergunta *Registrou o pagamento e a entrega continuou na lista* do #116.

**A baixa pelo painel é mais pobre, de propósito.** Ela marca a parada como entregue e grava
`situacaoDelivery = 'ENTREGUE'`, mas não tem forma de pagamento nem valor recebido — o painel não
sabe o que o cliente entregou na mão do motoboy. Daí o conselho do manual: baixa pelo celular sempre
que possível, e pelo painel só quando o celular falhar.

### Pedido de plataforma

Pedido com `ifoodLocalizer`, `nnID` ou `keetaId` chega com `ValorPago` igual ao total, o que zera o
`cobrarDoCliente` calculado pela função da lista. O aplicativo troca o botão de cobrança pelo de
confirmação da plataforma — uma *WebView* para o site do parceiro — e a baixa acontece em duas etapas:
confirmar lá, finalizar aqui. Keeta é a exceção sem botão: o selo aparece e nada mais.

## O fim: por que a rota desaparece

`rota.status = 'CONCLUIDA'` tira a rota da `viewRotaAberta`, que é o que alimenta o painel lateral. A
rota continua no banco; ela sai **da tela**. É a dúvida mais comum do #108, e a razão de o manual
avisar antes de o operador procurar.

Finalizar a rota confirma todas as paradas pendentes de uma vez, sem janela de confirmação. Medido na
captura do #108: o script esperava um modal, não veio, e a rota fechou no clique. O rótulo do botão é
explícito — *"Finalizar rota A confirmando todas as entregas"* — e foi decisão de produto não pôr
trava, registrada no `lovable/08`.

## O dia seguinte: por que as duas telas concordam

O relatório **Operação de Entrega** e o **Histórico** do aplicativo leem a mesma data de entrega
(`DataHoraEntregue` / `dataEntrega`). Não há agregação intermediária nem cache entre eles — é a mesma
coluna, contada de dois jeitos.

É também o que torna a escrita dessa coluna a mais perigosa do `smoke-app.js`, e a razão de ela exigir
`--permitir-passado`: mover uma entrega para ontem tira ela do total de hoje, nas duas telas ao mesmo
tempo, sem nenhum aviso.

## O caminho sem operador

O despacho automático (`despacho_config`, uma linha na base inteira quando isso foi medido — a da
sandbox, desligada) faz os momentos 1 e 2 sozinho: agrupa pedidos prontos e associa um entregador
disponível. **Nada nessa fase toca `situacaoDelivery`**, e a decisão foi explícita: não levar as 1.146
linhas do orquestrador para um serviço que não tem WhatsApp, marketplace, socket nem impressão.

Consequência para o manual: ele agrupa e associa, o clique de despachar continua sendo do operador. E
ele só age em filial onde alguém está com o painel aberto, porque o gatilho é o `painel_heartbeat`
gravado pelo próprio `GET /painel`.

## O que existe no código e não tem tela

Vale registrar, para o manual não prometer:

| Existe no servidor | Não existe na tela |
|---|---|
| notificação *push* de entrega nova | a fase 8 não foi construída; o aviso que o apêndice descreve é o do FCM, sem tela própria |
| API de pagamento na rua com mais campos do que o app usa | o aplicativo usa o subconjunto que os capítulos 11 a 13 mostram |
| `rota_evento` no Aurora, com o histórico de cada operação | ninguém fora do painel lê, e ele **desce no CASCADE** ao excluir a rota — daí a auditoria ter passado a gravar também no `beetech.log` |
