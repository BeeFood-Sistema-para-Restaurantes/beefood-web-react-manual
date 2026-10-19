# fluxo-codigo.md — #129 Route Delivery (uso interno, NÃO publicar)

O que a tela faz de verdade, lido no `beefood-web-react` em `88c23df`. O #127 (Entregas
Expressas) já documentou a tela da **API Aberta** por inteiro, e nada nela mudou desde então —
este arquivo registra só **o que é específico do Route Delivery**, mais o caminho de criar
credencial, que no #127 era passo opcional e aqui é o caminho principal.

Para o resto (os dois portões de acesso, os oito recursos, a regra *quem altera também
consulta*, as validações do webhook, a aba Avançado), vale
[`../integracao-entregas-expressas/fluxo-codigo.md`](../integracao-entregas-expressas/fluxo-codigo.md).

## Onde mora

| Camada | Arquivo |
|---|---|
| Lista de cards | `src/data/appCategories.ts` — categoria `api-mcp`, título **API e MCP** |
| Painel lateral | `src/components/apps/ApiAbertaSheet.tsx` |
| Aba Webhooks | `src/components/apps/ApiAbertaWebhooks.tsx` |
| Back-end | `supabase/functions/api-aberta/index.ts` |

## Os dois portões continuam de pé

`API_ABERTA_ALLOWED_EMPRESAS` libera o card para **quatro empresas** (a 38311 é o sandbox dos
manuais), e empresa marcada como sandbox em `config_cache.sandbox` nem vê o painel — leva um
bloco *Ambiente de testes* apontando para `docs.beefood.app`. Os dois viraram linha da tabela
*Quando algo não funciona*.

## Criar credencial: o caminho que este manual ensina

O pedido do dono foi explícito — *"na hora de pedir a credencial ensinamos a fazer por
Aplicativos → API Aberta → Criar credencial, seguindo o fluxo mais amigável para o cliente"*.
No #127 esse era o Passo 4, opcional; aqui é a Parte 1 inteira. O que o código garante:

```ts
const SCOPES_PADRAO_NOVA = RECURSOS.filter((r) => !r.emBreve)
  .flatMap((r) => [`${r.id}:read`, `${r.id}:write`]);
...
<Button onClick={() => { setNovosScopes(SCOPES_PADRAO_NOVA); setCriarOpen(true); }}>CRIAR CREDENCIAL</Button>
```

- **Nasce com tudo ligado e ativa.** `criar()` chama `action: 'create'` com
  `{ scopes: comRead(novosScopes), active: true }`. Os três scopes que o Route Delivery pede —
  `store:read`, `orders:read`, `orders:write` — já vêm satisfeitos sem o leitor mexer em nada.
  É isso que torna o caminho mais curto que o do portal, onde ele teria de marcar permissão,
  trocar ambiente e conferir se ficou ativa.
- **São dois diálogos em sequência, e o segundo é a razão da foto.** O primeiro é *Nova
  credencial adicional* (*"Escolha as permissões da nova credencial. O Client Secret aparece uma
  única vez após a criação."*), com `CANCELAR (ESC)` / `CRIAR (F2)`. Depois de `create`
  responder, `setNovaCredencial({ clientId, clientSecret })` abre o segundo, *Credencial
  criada*, que mostra os dois valores em `<code>` com botão de copiar. **Esse diálogo não existe
  sem criar de verdade** — ver a nota na `MEMORIA.md` sobre como ele foi fotografado.
- **O segredo não se perde.** O rodapé do próprio diálogo diz: *"O clientSecret também pode ser
  revelado depois pelo ícone de olho no campo Client Secret do cartão da credencial."* O artigo
  do parceiro avisa o contrário (*"copie o Client ID e o Client Secret"*, uma vez só), e está
  certo — para o portal. No painel não vale, e o manual diz isso.
- **Credencial adicional pode ser excluída; a principal não.** O `EXCLUIR` da linha é
  `{!c.main && …}`, com confirmação *"Integrações que usam esta credencial deixarão de
  funcionar."* É o que sustenta a resposta *"como corto o acesso do Route Delivery?"* — e a
  razão de o manual preferir uma credencial dedicada à principal.
- **`RECICLAR` na principal segue sendo o botão perigoso** (*"O Client ID e o Client Secret
  serão trocados e todas as conexões atuais param imediatamente"*). No manual ele ganhou seta
  própria na imagem 03, com o rótulo de **não clique** — ele fica a um clique de distância do
  `CRIAR CREDENCIAL`, logo acima.

## O que muda no webhook em relação ao #127

| | Entregas Expressas (#127) | Route Delivery (#129) |
|---|---|---|
| Eventos | os **cinco** | **três**: `order_created`, `order_updated`, `order_delivery_updated` |
| Autenticação Basic | **Usuário e senha do parceiro** nos campos `clientId (usuário)` / `clientSecret (senha)` | **em branco** |
| *Secret do webhook* | gerado, guardado, e o parceiro **não pede** | gerado e **devolvido ao parceiro**, que o cola na linha da loja |
| Endereço | sai do painel do parceiro depois de salvar a integração | sai da coluna **Webhook** da tabela do ADM, e é **um por loja** |

As consequências para o texto:

- O aviso de nomes que colidem, que era central no #127, **não se aplica aqui** — e por isso
  virou o oposto: a tabela da imagem 13 diz para deixar os dois campos em branco. A validação
  `user`/`password` *"juntos ou nenhum"* continua no back-end, então preencher um só dá erro;
  esse é o único risco do campo, e está na FAQ.
- O *Secret do webhook* aqui é **a última etapa da integração**, não uma curiosidade. O texto da
  tela (*"Guarde este secret agora — ele não poderá ser exibido novamente"* + `JÁ GUARDEI`)
  deixou de ser só um cuidado e passou a ser instrução: sem mandá-lo ao parceiro, a linha da
  loja fica em *Falta o secret do webhook*.
- Os dois eventos de pagamento ficam **desligados** no formulário, o que no painel é só
  desligar o interruptor. O back-end aceita qualquer subconjunto dos cinco (`EVENTOS` em
  `index.ts`), desde que haja ao menos um.

## A armadilha do ambiente, de novo

O artigo do Route Delivery dedica uma caixa inteira a ela — *"o portal abre com Sandbox marcado…
com uma credencial de Sandbox, os pedidos reais da loja não chegam ao Route Delivery"* — e tem
uma pergunta na FAQ só para isso (*"a tela mostra sandbox ao lado do nome da loja"*). Pelo
painel a escolha não existe: `create` manda `sandbox: false`, `webhookSave` força
`payload.sandbox = false`, e as duas listagens filtram o que é de teste. Daí a linha da tabela
de problemas e o aviso da seta 4 do Passo 7: a caixa **Credencial do sandbox** do parceiro tem
de ficar **desmarcada**.

## O que é informação do parceiro, e não foi verificado aqui

Vem do artigo do Route Delivery; a lógica é do lado dele ou da API, não do painel:

- a BeeFood desativa o webhook depois de **5 tentativas sem sucesso** e avisa o e-mail
  cadastrado;
- **sem** webhook: busca a cada **5 s**, e só enquanto um painel ou o app de um entregador
  estiver aberto; **com** webhook: pedido em **1 a 2 s** e busca de reserva a cada **30 s**;
- na primeira busca entram os pedidos de entrega das **últimas 2 horas** ainda não despachados,
  entregues ou cancelados;
- o entregador sair marca **despachado** e finalizar marca **entregue** no BeeFood;
- o padrão é chamar os entregadores quando a loja marca **Pronto**;
- cancelar no BeeFood cancela a corrida, salvo se já entregue;
- pedido de **retirada, balcão ou mesa** não vira corrida;
- filiais que compartilham a mesma credencial caem todas no comércio escolhido no vínculo.

No manual elas aparecem como comportamento da integração, sem prometer tela do BeeFood que não
foi fotografada.
