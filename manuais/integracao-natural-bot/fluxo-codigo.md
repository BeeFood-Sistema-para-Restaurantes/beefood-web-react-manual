# fluxo-codigo.md — #134 Natural Bot (uso interno, NÃO publicar)

O que as duas telas fazem de verdade. O lado BeeFood foi lido no `beefood-web-react` em
`0f825d5`; o lado Natural Bot foi medido no painel de homologação e conferido contra a API
pública, porque o código do parceiro não está aqui.

A tela da **API Aberta** já está documentada por inteiro no #127 (Entregas Expressas), e a
regra *quem altera também consulta* e o caminho **CRIAR CREDENCIAL** no #129 (Route Delivery).
Este arquivo registra só o que é específico da Natural Bot — e é bastante, porque esta é a
primeira integração do repositório em que **o parceiro cadastra o webhook sozinho**.

## Onde mora

| Camada | Arquivo |
|---|---|
| Lista de cards | `src/data/appCategories.ts` — categoria `api-mcp`, título **API e MCP** |
| Painel lateral | `src/components/apps/ApiAbertaSheet.tsx` |
| Aba Webhooks | `src/components/apps/ApiAbertaWebhooks.tsx` |
| Ponte do painel | `supabase/functions/api-aberta/index.ts` → `https://api.beefood.app/developer/v1` |
| API que o parceiro usa | `https://api.beefood.app/v1` (produção) e `https://api-sandbox.beefood.app/v1` (sandbox) |

## Os seis acessos, e por que são exatamente seis

O pedido do dono repete, palavra por palavra, a lista que a própria tela da Natural Bot mostra
antes do formulário. Cada um existe por um motivo, e os dois últimos são a diferença deste
manual:

| Acesso | Para que a Natural Bot usa | Onde isso aparece |
|---|---|---|
| `store:read` | listar os cardápios e as formas de pagamento da loja | etapa 2 do diálogo: o campo **Cardápio** e o de-para de pagamentos |
| `catalog:read` | importar o cardápio | **Cardápio → Produtos → Sinc. BeeFood** |
| `orders:write` | enviar o pedido para a loja | dia a dia |
| `orders:read` | conferir um pedido que a BeeFood não confirmou | dia a dia |
| `webhook:read` | conferir se o aviso de status continua ativo | linha *Webhook de status: ativo* |
| `webhook:write` | **cadastrar** o aviso que traz o status de volta | nada — acontece sozinho ao salvar |

No editor de permissões, `store:read` é o cartão **Loja** e `catalog:read` é o **Catálogo** (os
rótulos em português não batem com o nome do escopo, e é por isso que o passo dos seis acessos
confere pelo nome em mono, embaixo do interruptor):

```ts
{ id: 'orders',  label: 'Pedidos',  desc: 'Consultar e criar pedidos' },
{ id: 'catalog', label: 'Catálogo', desc: 'Produtos, grupos e complementos' },
{ id: 'store',   label: 'Loja',     desc: 'Horários, entrega e pagamentos' },
{ id: 'webhook', label: 'Webhooks', desc: 'Cadastro de webhooks' },
```

A credencial **nasce com tudo ligado** (`SCOPES_PADRAO_NOVA` é o produto cartesiano de todos os
recursos liberados), então o trabalho do leitor é **desligar**, não ligar. E desligar o
*Consultar* derruba o *Alterar* junto, pela regra do `alternar()`: é o que deixa a conta fechar
em seis cliques de desligar e nenhum de ligar.

## O webhook: a diferença em relação ao #127 e ao #129

Nos dois manuais anteriores de integração o lojista criava o webhook à mão, na aba **Webhooks**,
e mandava o *Secret do webhook* para o parceiro. Aqui **não há Parte 3**: com `webhook:write` na
credencial, a Natural Bot cadastra o próprio aviso quando você clica em **Salvar**. Medido na
sandbox, logo depois de salvar a integração:

```
GET /v1/webhooks
  id 98, active true, eventTypes [order_updated, order_delivery_updated],
  url https://dash-api-hml.naturalbot.com/api/v1/webhooks/beefood/<uuid por filial>,
  ownerEmail developer@naturalbot.com
```

Três consequências para o texto:

- o manual **não** ensina a criar webhook, e diz isso em voz alta, porque quem veio do #127 ou
  do #129 espera essa etapa;
- o endereço é **um por filial** (o `uuid` no fim) e o responsável é o e-mail do parceiro, não o
  do lojista — então quem recebe o aviso de webhook desativado é a Natural Bot;
- os eventos são **dois**, não os cinco: `order_updated` e `order_delivery_updated`. Pedido
  criado não interessa, porque o pedido nasce na Natural Bot e vai para a BeeFood por
  `orders:write`; o que volta é o andar do status.

A tela do parceiro resume isso em duas linhas que o manual aproveita: *"O status do pedido segue
a BeeFood sozinho quando a conexão com o webhook está ativa. Não há opção para mudar isso."* e
*"Webhook de status: ativo"*.

## A armadilha do ambiente, e o que ela custou nas capturas

A tela da Natural Bot avisa: *"Use o ambiente de produção, e não a sandbox: a credencial só
funciona no ambiente em que foi criada"*. É literal — são dois bancos de credenciais:

| | Produção | Sandbox |
|---|---|---|
| API | `api.beefood.app/v1` (`{"status":"ok","sandbox":false}`) | `api-sandbox.beefood.app/v1` (`…"sandbox":true`) |
| Onde se cria | painel (**Aplicativos → API Aberta**) **ou** portal | só no portal `docs.beefood.app`, escolhendo **Ambiente** |
| Empresa de testes | 38311 | 56179, com login `developer-contato@beefood.com.br` |

O painel **nunca** cria credencial de sandbox: `create` manda `sandbox: false`, e a listagem
filtra o que é de teste (`bruto.filter((c) => !c.sandbox && !c.main …)`) — ou seja, uma
credencial de sandbox existe, funciona e **não aparece** em *Todas as credenciais*. Empresa que
está ela mesma em sandbox não vê credencial nenhuma no painel: leva o bloco *Ambiente de testes*
apontando para o portal.

Isso define o manual (ensina o caminho do painel, que é sempre produção) e explicou um erro no
caminho: o painel de **homologação** da Natural Bot conversa com a sandbox da BeeFood, e recusou
a credencial de produção com *"Autenticação na BeeFood: A BeeFood recusou o client ID ou o
client secret"* — o mesmo 401 `Invalid client credentials` que a API devolve. Por isso as
capturas da Parte 2 usam credencial de sandbox, e só o formulário da imagem 06 mostra a de
produção, pela técnica do ensaio. Está registrado na `MEMORIA.md`.

## O que a tela do parceiro pede, e em que ordem

O diálogo **Configurar integração - BeeFood** tem duas etapas e uma tela de resultado:

1. **Credencial.** `Client ID` obrigatório, `Client secret` opcional **quando já existe um
   salvo** (*"Deixe o campo em branco para mantê-lo"*), e o botão vira **Conectar** quando os
   dois estão preenchidos. Para trocar de cardápio o secret tem de ser digitado de novo, porque
   a lista de cardápios sai de uma credencial validada (`store:read`).
2. **Cardápio e pagamentos.** Um `select` de cardápio da BeeFood e um de-para das três formas
   que a Natural Bot recebe online (Pix, crédito, débito). Ela sugere o par automaticamente e
   avisa que *"só vale depois que você salvar"*. Tem o interruptor **Ligar a integração ao
   salvar**, que já vem ligado.
3. **Verificação.** Depois de salvar, a Natural Bot consulta a BeeFood e mostra o que achou. Na
   captura veio *"Integração com a BeeFood configurada com sucesso"* **mais** um aviso:
   *"Canal de delivery: O canal delivery deste cardápio da BeeFood não aceita pedidos de entrega
   nem de retirada"* — sintoma da loja de sandbox, e por isso virou linha da tabela de problemas
   em vez de ser escondido da imagem.

Depois de configurada, o diálogo abre em modo resumo (**Integração já configurada**) com o
`Client ID` mascarado, o cardápio, o de-para e os dois interruptores de **Sincronização de
pedidos** — estes últimos atrás de um aviso: *"Feche a loja para alterar estas configurações"*.
Conectar e salvar funcionam com a loja aberta; mexer nos interruptores depois, não.

## A importação do cardápio

**Cardápio → Produtos → Sinc. BeeFood** abre *Importação de produtos — BeeFood*, com três
caixas **desmarcadas** e um resumo no fim (categorias, produtos, variações, opções). As três
caixas são destrutivas em graus diferentes, e o manual descreve cada uma sem mandar marcar
nenhuma na primeira vez:

| Opção | O que faz |
|---|---|
| Deixar a BeeFood controlar a disponibilidade | copia o ligado/desligado da BeeFood, **só nesta rodada** |
| Remover o que saiu da BeeFood | apaga daqui o que veio de lá e não existe mais lá; o que foi criado à mão fica |
| Sobrescrever as alterações feitas aqui | desfaz edições locais e ressuscita o que foi apagado |

Medido: a importação é **assíncrona** (*"processada em fila"*), mas na loja de teste terminou em
menos de 12 s, com `1 Categoria / 4 Produtos / 0 Variações / 0 Opções`. Rodar de novo é
idempotente nos produtos — **mas não nas categorias**: a filial já tinha uma categoria
*Bebidas* criada à mão, e a importação criou a sua, deixando duas abas com o mesmo nome na
página de Produtos. Virou linha da tabela de problemas.

A lista de produtos abre na **primeira** categoria, que pode ser uma vazia; quem mostra o que
chegou é a aba **Todos**. O manual não fotografa essa lista — o dono cortou, porque o que o
leitor precisa é do caminho da importação —, mas a pegadinha ficou como aviso no último passo.

## O que é informação do parceiro, e não foi verificado aqui

- *"Apenas um gestor de PDV pode estar ativo por vez. Ao ativar um novo gestor, o anterior será
  desativado automaticamente."* — o aviso é da tela; o efeito em quem já usa outro gestor não foi
  testado. Entrou no manual como alerta, com a palavra da tela.
- O interruptor *"Ative para que os pedidos cancelados na BeeFood sejam ignorados na Natural
  Bot"* e a explicação dele (*"alguns lojistas cancelam no gestor da BeeFood como etapa de
  fluxo"*) são regra do parceiro.
- Tudo que é uso diário — como o pedido entra, o que o robô responde, prazo, impressão — é
  assunto da Natural Bot, por decisão do dono: *"dúvidas de uso devem ser tiradas direto com a
  Natural Bot"*. O manual repete isso no fim.
