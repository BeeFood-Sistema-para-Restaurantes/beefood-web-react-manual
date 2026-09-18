# Como a Gestão de Entregas 2.0 funciona

Leitura completa de `beetech-server-node-3.0/docs/gestao-entrega-2.0/` — 21 documentos de
backend, 13 prompts de frontend, 1 plano de teste e 14 scripts SQL, ~17.100 linhas.
No Cloud Agent a pasta está em `~/refs/beetech-server-node-2.0/docs/gestao-entrega-2.0/`
(o clone é do `2.0`, mas a documentação do módulo mora dentro dele).

Este arquivo é **entendimento**, não manual. Ele existe para que o recorte dos manuais saia do
que o sistema faz de verdade, e não do que a tela parece fazer. O que eu **medi** no sistema
está no arquivo vizinho, [`02-estado-medido.md`](02-estado-medido.md).

    10|---

## 1. Quatro programas, e só um é tela de restaurante

| Programa | O que é | Papel |
|---|---|---|
| `beefood-web-react` | o painel que o lojista usa | a tela `/gestao-entregas` — **é o que o manual fotografa** |
| `beetech-server-node-3.0` | API | recebe cada clique do painel e do app, decide e grava |
| `beefood3-server-entregas` | servidor de **instância única** | os crons: distância da loja, timeout de presença, despacho automático, aviso de proximidade |
| `beetech-entregador` | app React Native / Expo | o celular do motoboy |

    20|A separação em dois servidores não é detalhe de infra: ela **muda o que o manual pode prometer**.
Cron que roda em servidor único não escala, mas também não duplica — e é por isso que o despacho
automático agrupa uma vez, e não uma vez por réplica. O `beetech-server-node-2.0` está
**congelado** por regra do projeto: rotina nova não entra mais nele.

## 2. Dois bancos, e a divisão é rígida

| Banco | Dono de | Exemplos |
|---|---|---|
| **MSSQL `notafacilb`** (ERP, o mesmo do PDV) | pedido, cliente, endereço, funcionário, **taxa do entregador**, situação da entrega | `_PreVenda`, `_Cliente`, `_ClienteEndereco`, `_Funcionario` |
| **MySQL Aurora `entregas`** (novo) | **rota**, parada, presença, posição de GPS, configuração do despacho, token de push | `rota`, `rota_parada`, `entregador_status`, `posicao`, `despacho_config` |

    30|Nada é replicado de propósito. O que existe no Aurora são **fotografias** (`clienteNome`,
`enderecoResumo`, `valorTotal` na parada), só para o mapa não precisar fazer JOIN entre dois
servidores de banco a cada refresh. Quando painel e app mostram números diferentes do relatório,
a causa quase sempre é esta: o snapshot envelheceu e a verdade está no ERP.

O caso mais importante disso é a **taxa do entregador**. Ela nasceu como coluna no Aurora
(`rota_parada.valorEntregador`) e foi **removida** pelo script `007`, por decisão do dono: a taxa
mora em `_PreVenda.taxaServicoValorDinheiro`, no ERP, porque é **editável depois** de a rota estar
montada (é o que o `venda2/atualizaValorEntregador` existe para fazer). Um snapshot passaria a
mentir. Relatório que cruze rota e taxa junta os dois bancos pelo `preVendaID`.

    40|> ⚠️ Existem **dois** schemas chamados `entregas`, em clusters diferentes: o novo
> (`beefood-entregas`) e um antigo (`beetech-mysql`, com `procInsertOrUpdateEntrega`). Todo
> script SQL do módulo abre com esse aviso. Vale para quem for consultar: confira o host.

## 3. O ciclo de uma entrega, de ponta a ponta

É esta narrativa que o manual vai contar, e ela tem dois lados olhando para o mesmo pedido.

```
  o pedido entra            PREPARO            → aparece no painel, em "Pedidos sem rota"
  a cozinha termina         PRONTO             → "Marcar prontos" na barra de ações
  o operador monta a rota   rota CRIADA        → arrasta paradas, otimiza a ordem
    50|  escolhe o entregador      rota ASSOCIADA     → grava tambem no ERP (FuncionarioIDMotoboy)
  despacha                  rota EM_ROTA       → ERP vira ENTREGA: avisa cliente e marketplace
  o app recebe              lista de entregas  → o motoboy toca INICIAR ROTA
  o motoboy anda            pings de GPS       → pin no mapa + aviso de proximidade ao cliente
  entrega uma parada        parada ENTREGUE    → a proxima parada assume EM_ROTA
  cobra na porta            pagamento no caixa → só se houver caixa aberto na filial
  fecha a ultima            rota CONCLUIDA     → some da view de rota aberta
```

O **despacho** é o ponto de não-retorno e o manual tem de dizer isso com clareza: ele muda
`situacaoDelivery` para `ENTREGA` no ERP, e essa mudança passa pelo `SituacaoDeliveryUpdater`,
    60|que **notifica marketplace, imprime e enfileira WhatsApp**. Não é um rótulo de tela.

## 4. O painel: o que ele lê, e quando ele escreve

Dois endpoints, de propósito separados:

| Endpoint | Ritmo | O que traz | Por que separado |
|---|---|---|---|
| `GET /entrega2/gestao/painel` | ~30 s | pedidos (MSSQL) + rotas e entregadores (Aurora) + a loja | consulta pesada, toca o banco do PDV |
| `GET /entrega2/gestao/posicoes` | ~10 s | só a posição dos entregadores (Aurora) | barato, e é o que precisa ser fluido |

Além do polling, o painel ouve **WebSocket**: `DELIVERY_SITUACAO_` (pedido mudou de situação),
    70|`ENTREGA_PRESENCA_` (entregador ficou online/offline) e `ENTREGA_ROTA_` (rota mudou —
outro operador ou o despacho automático). O evento de rota faz o painel recarregar o snapshot,
com debounce, porque sem isso dois operadores trabalhavam 30 segundos em cima de dado velho.

Três consequências que aparecem na tela e precisam estar no manual:

1. **Pedido sem coordenada não vai para o mapa.** Ele cai num grupo próprio, *Pedidos sem
   localização*, que o painel mostra **primeiro** justamente para o operador resolver o endereço.
   A coordenada vem do cadastro de endereço do cliente, que depende da área de entrega — por isso
   os manuais de área (#35–#38) são pré-requisito deste.
2. **Rota sem parada não aparece.** É decisão deliberada; e é o que esconde do operador a
    80|   *rota fantasma* descrita no §7.
3. **Abrir a tela é um ato que o servidor registra.** O `GET /painel` grava
   `painel_heartbeat` (quem está com a tela aberta, quantos pedidos sem rota, idade do mais novo).
   É esse registro que **autoriza o despacho automático a agir** naquela filial.

## 5. Roteirização manual: dez operações, e todas escrevem nos dois bancos

`12-roteirizacao-manual.md` é a fase em que o painel deixa de ser visor e passa a escrever no ERP.

| Operação | O que muda |
|---|---|
| criar rota | `rota` + `rota_parada` no Aurora; nada no ERP ainda |
| associar / trocar entregador | Aurora **e** `_PreVenda.FuncionarioIDMotoboy` no ERP |
    90|| adicionar / remover parada | Aurora; remover devolve o pedido para "sem rota" |
| reordenar (arrastar) | só `rota_parada.ordem` — em lote, por isso `ordem` **não** é único |
| otimizar ordem | cálculo no navegador (Haversine, vizinho mais próximo), depois grava a ordem |
| marcar prontos | `situacaoDelivery = PRONTO` no ERP |
| **despachar** | `EM_ROTA` no Aurora, `ENTREGA` no ERP → **avisa cliente e marketplace** |
| entregar uma parada | parada `ENTREGUE`; a seguinte vira `EM_ROTA` |
| finalizar rota | fecha as paradas que sobraram e marca a rota `CONCLUIDA` |
| excluir rota | apaga rota e paradas (cascata); os pedidos voltam para "sem rota" |

Duas decisões de produto aqui mudam o texto do manual:

   100|- **As travas iniciais foram removidas.** A primeira versão só deixava despachar pedido
  `PRONTO` e só uma vez. O dono cortou: o operador tem mais contexto que o sistema, e trava que
  atrapalha vira ligação para o suporte. Em troca, **tudo vai para o log** (`beetech.log`).
  Então o manual descreve o caminho recomendado, mas não pode dizer "o sistema não permite".
- **`EM_ROTA` na parada é estado só do Aurora.** Ele diz *qual* parada o entregador está
  entregando agora. O ERP não tem equivalente: lá a rota inteira virou `ENTREGA` no despacho.

## 6. O vocabulário: dois dicionários para a mesma entrega

Esta é a parte que mais atrapalha quem escreve manual, porque a tela mistura os dois.

| Situação no ERP (`situacaoDelivery`) | O que o painel mostra |
|---|---|
   110|| `PREPARO` | em preparação |
| `PRONTO` | pronto |
| `ENTREGA` | em rota |
| `ENTREGUE` | entregue |

`TRANSPORTE` **não é valor válido** — estava no filtro da view por herança e foi removido pelo
script `004`. E a regra que o frontend centralizou em `src/lib/statusEntrega.ts` é que **status
não regride**: um evento de WebSocket atrasado não pode puxar um pedido de "entregue" para
"em rota".

> O script `004` é o mais perigoso da lista e vale conhecer o porquê: ele acrescenta `PRONTO` ao
   120|> filtro da `viewDeliveryFilaAguardandoEntrega`. **Sem ele, marcar prontos quebra o despacho**:
> o pedido sai da view, deixa de existir para o backend, e a rota vai para `EM_ROTA` sem nenhum
> cliente ter sido avisado. Não é um problema visual.

## 7. Despacho automático: sete regras, e o que ele deliberadamente não faz

O cron roda a cada minuto no `beefood3-server-entregas`, agrupa pedidos sem rota e associa
entregador. As sete regras da tela:

| Campo | Padrão | O que faz |
|---|---|---|
| Máximo de entregas por viagem | 2 | quantos pedidos cabem na mesma rota |
   130|| Distância máxima para agrupar (m) | 3000 | distância entre os pedidos; vazio = sem a regra |
| Tempo máximo para agrupar (min) | vazio | diferença de espera entre os pedidos; vazio = sem a regra |
| Liberar o entregador quando os pedidos estiverem | Finalizados | *Finalizados*: uma viagem por vez. *Em trânsito*: já recebe a próxima |
| Raio do restaurante (m) | 1000 | o entregador precisa estar a esta distância para receber rota; 0 = não exigir |
| Considerar a posição do entregador | ligado | escolhe quem está mais perto da **primeira parada**, não do restaurante |
| Tolerância de GPS (min) | 5 | posição mais velha que isso = entregador não confiável |

E o que ele **não** faz, que é a parte que mais gera expectativa errada:

- **Ele não despacha.** Agrupa e associa entregador, e para aí. Despachar continua sendo um
   140|  clique do operador — porque despachar avisa cliente e marketplace, e nenhum dono quer isso
  acontecendo sozinho de madrugada.
- **Ele não age com a tela fechada.** É o `painel_heartbeat` (§4): se ninguém está com a Gestão de
  Entregas aberta, o cron não consulta a filial. A alternativa era 1,4 milhão de consultas por dia
  ao banco do PDV, a maioria em loja fechada. Consequência aceita: quem liga o recurso e fecha a
  aba volta e encontra os pedidos sem rota. **Isso tem de estar no manual**, porque a tela diz
  "despacho automático ligado" e o operador vai supor que ligado significa sempre.
- **Pedido com mais de 2 horas de espera não é agrupado.** Freio de arranque, para o recurso não
  varrer a fila velha de uma filial no instante em que é ligado.

   150|**A rota fantasma.** Quando o `rotaIDAtual` do entregador aponta para uma rota que já não existe
(excluída, concluída), ele fica ocupado para sempre aos olhos do despacho e nunca mais recebe
rota. O `13-despacho-automatico.md` registra a correção — e eu encontrei **um caso vivo** na
sandbox, descrito no [`02-estado-medido.md`](02-estado-medido.md).

## 8. Presença: três estados, e o GPS muda de ritmo

O app tem um seletor de três posições, e cada um muda o que acontece no celular:

| Estado | No painel | GPS |
|---|---|---|
| **Disponível** | conta em "disponíveis", pode receber rota | cadência alta |
| **Pausa** | conta em "em pausa", não recebe rota | cadência reduzida |
   160|| **Offline** | conta em "offline" | cadência mínima |

A cadência adaptativa existe por bateria e dados do motoboy — e o `07-app-entregador.md` conta que
o envio precisou sair do `setInterval` e ir para dentro do `TaskManager`, porque no iOS com o app
minimizado o `setInterval` simplesmente não roda: a posição era capturada e nunca enviada.

Dois comportamentos que o manual tem de explicar porque parecem defeito:

- **Um cron derruba para offline quem passa 30 minutos sem mandar posição.** O app não é avisado;
  ele se realinha na próxima abertura. Então o motoboy pode ver "online" no celular enquanto o
  painel já o marcou offline.
   170|- **O painel distingue "nunca usou o app" de "está offline agora".** São dois textos diferentes
  na lista de entregadores, e a diferença importa: um é problema de cadastro, o outro é operação.

## 9. O app do entregador, do lado do servidor

| Recurso | Como funciona | Pegadinha |
|---|---|---|
| lista de entregas | `GET /entrega2/gestao/entregador/<empresa>/<filial>/<usuario>/<funcionario>` devolve **pedidos avulsos e rotas** | a retrocompatibilidade é o desenho: o app antigo continua vendo pedido solto |
| iniciar rota | `PUT /gestao/rota/:id/despachar`, chamado **pelo app** | o app despacha sem passar pelo painel |
| melhor rota | reordena por distância **a partir da loja** | **sobrescreve a ordem manual** que o operador montou no painel |
| baixa da entrega | `PUT .../paradas/:paradaID/entregar` | ver abaixo |
| código de barras | leitura no balcão → `POST tentrega/lerCodigoBarras` | é **ação de despacho**: dispara marketplace, impressão e WhatsApp |
   180|| pagamento na rua | usa as mesmas procedures do PDV | **exige caixa aberto na filial**, e o lançamento entra no caixa real |
| push | token `ExponentPushToken[...]` por `funcionarioID` | exige **build novo** do app, não atualização OTA |

**A autenticação é a costura torta do módulo, e é bom saber que é de propósito.** O app usa
**Basic Auth** (ele não emite JWT); o painel usa **JWT Bearer**. Quando o endpoint de baixa
precisou atender os dois, a decisão do dono foi **remover o `authMiddleware`** daquele endpoint,
aceitando o risco. Vale como contexto para quem for escrever sobre permissões: não há permissão
de usuário separando o que o app pode fazer.

No pagamento na rua, um detalhe que o manual de cobrança vai precisar: o servidor **não confere**
se a soma dos pagamentos fecha com o total. Quem valida é a tela do app. E o `funcionarioID` é
   190|obrigatório em toda escrita, justamente para a conciliação saber quem mexeu no dinheiro.

## 10. WhatsApp: quatro mensagens novas, e limites que decidem o texto

O script `008` criou quatro tipos, ligados por padrão em toda filial ativa:

| Tipo | Categoria | Para quem |
|---|---|---|
| 30 — Nova entrega | Entregador | o motoboy, quando um pedido vira dele |
| 31 — Entrega cancelada | Entregador | o motoboy, quando o pedido sai dele |
| 32 — Relatório diário | Entregador | resumo de ontem, com a lista de entregas |
| 33 — Entregador próximo | Delivery | **o cliente**, quando o motoboy entra no raio |

   200|Cinco limites da fila de WhatsApp que moldaram esses textos:

1. **Anti-ban:** a fila não manda para quem não escreveu de volta nos últimos 30 dias. Isso
   **bloquearia todas as mensagens de entregador** — foi preciso abrir exceção por categoria.
2. **Vazão de 5 mensagens por filial por minuto**, e mensagem expira em 5 horas.
3. **A fila é apagada todo dia às 10:00.** É por isso que o aviso de proximidade grava
   `rota_parada.dataHoraAvisoProximidade`: sem isso, a memória de "já avisei" morre na limpeza.
4. **A dedup ignorava o destinatário.** Pedido que troca de mão não avisava o segundo entregador.
   O script `013` criou uma procedure nova (`...MsgDelivery2`) com `funcionarioID` na chave —
   procedure MySQL não aceita parâmetro com valor padrão, e acrescentar um 15º parâmetro à antiga
   210|   quebraria sete projetos, dois deles congelados.
5. **Texto idêntico em massa é o que a Meta usa para detectar spam**, e o número bloqueado é o do
   restaurante. Por isso o tipo 33 tem **quatro variações** sorteadas a cada envio, mais spintax
   (`{a|b}`) por cima.

O "saiu para entrega" (tipo 4) **já existia** e não foi tocado. Quem quiser o nome do entregador
nele acrescenta `**ENTREGADOR_NOME**` ao próprio texto, na tela — o cron já sabe substituir.

O raio do aviso de proximidade ficou em `_WhatsappMsgTipoFilial.raioProximidadeMetros`, e não no
`despacho_config`, por um motivo que vale copiar: **o `despacho_config` não tem tela.** Mexer nele
é SQL; a distância é propriedade da mensagem, e a tela onde se edita o texto é onde o lojista vai
   220|procurar. O campo aparece em km, grava em metros, e o cron só relê a configuração a cada 30 min.

## 11. O que a documentação promete e ainda não existe

Registrar isto agora evita procurar na tela por meia hora:

| Assunto | Estado |
|---|---|
| **Insucesso de entrega** | `rota_parada.motivoInsucesso` e o valor `INSUCESSO` existem **sem produtor, de propósito** — não-entrega está fora de escopo em definitivo |
| **Veículo e capacidade do entregador** | a tabela `entregador` existe e **está vazia na base toda** (medido); `veiculoTipo` e `capacidadeMaxima` nunca são preenchidos |
| **`ModalWhatsApp` no app** | está completo no código do app e **não está montado em nenhuma tela** — as cinco mensagens prontas não têm porta de entrada |
| **Keeta** | aparece como etiqueta no card, sem botão de confirmação (iFood e 99Food têm) |
   230|| **Analytics / KPIs (Fase 7)** | é mapa de ideias, não plano. Só **35,2%** dos pedidos têm entregador atribuído e **17,1%** têm taxa definida — a base não sustenta KPI financeiro ainda |
| **Expurgo de GPS** | previsto (30 dias), **não implementado** — e o doc avisa: agregador de trajeto tem de vir **antes** do expurgo, ou o histórico se perde |

## 12. O que isto significa para o recorte dos manuais

O que a leitura mudou na minha cabeça, em cinco pontos:

1. **O painel não é um manual, são vários.** Ler o mapa; montar e despachar rota; despacho
   automático; e as mensagens de WhatsApp de entrega. Cada um tem cenário próprio e o despacho
   automático tem sete campos que pedem tabela.
2. **O manual do app já está escrito** — é o `material-recebido/`, 15 capítulos. O trabalho ali é
   240|   revisar, padronizar para o formato da casa e **trocar os prints velhos do #57**.
3. **A parte que ninguém cobriu é a costura.** O mesmo pedido visto dos dois lados: o operador
   despacha e o motoboy recebe; o motoboy dá baixa e o painel muda. É a parte que só existe com
   as duas fontes juntas, e é a que justifica o manual novo existir.
4. **Três frases do manual precisam ser precisas, porque contrariam a intuição:** despachar avisa
   cliente e marketplace; despacho automático não despacha e não age com a tela fechada; "melhor
   rota" no app desfaz a ordem que o operador montou.
5. **Cenário é o gargalo, não a escrita.** Toda tela interessante depende de pedido com
   coordenada, entregador com GPS recente e — para cobrança — caixa aberto. É sobre isso o
   [`02-estado-medido.md`](02-estado-medido.md).
