# fluxo-codigo.md — #127 Entregas Expressas (uso interno, NÃO publicar)

O que a tela faz de verdade, lido no `beefood-web-react` em `725180a`. Serve para o manual
não repetir o que o artigo do parceiro diz e o BeeFood não faz mais.

## Onde mora

| Camada | Arquivo |
|---|---|
| Rota e permissão | `src/App.tsx` → `<ProtectedRoute menuKey="aplicativos">`, mapeada em `src/hooks/usePermissions.ts` (`'/aplicativos': 'aplicativos'`) |
| Lista de cards | `src/data/appCategories.ts` — categoria `api-mcp`, título **API e MCP** |
| Painel lateral | `src/components/apps/ApiAbertaSheet.tsx` (707 linhas) |
| Aba Webhooks | `src/components/apps/ApiAbertaWebhooks.tsx` (250 linhas) |
| Back-end | `supabase/functions/api-aberta/index.ts` — repassa para a API interna com `X-BeeFood-Panel-Secret` |

## O card não aparece para todo mundo

```ts
export const API_MCP_ALLOWED_EMPRESAS: number[] = [107, 38311];
export const API_ABERTA_ALLOWED_EMPRESAS: number[] = [...API_MCP_ALLOWED_EMPRESAS, 5687, 11543];
```

`Aplicativos.tsx` só mostra o card quando `app.allowedEmpresas` é ausente **ou** inclui a
`empresaID` da sessão. Hoje são **quatro empresas** — a 38311 é o sandbox dos manuais, e é por
isso que a captura existe. O manual precisa dizer que o card pode não estar lá, senão o leitor
fica procurando um botão que a conta dele não tem.

**Empresa em ambiente sandbox não usa o painel.** `isSandbox()` lê `config_cache.sandbox` e,
quando é `true`, o painel troca tudo por um bloco *Ambiente de testes* apontando para
`docs.beefood.app`. O back-end recusa do mesmo jeito (`index.ts:105`:
*"Empresa em ambiente sandbox: use o portal docs.beefood.app"*).

## A diferença que faz o manual existir: o painel não tem ambiente para errar

É a armadilha que o artigo do parceiro descreve em letras maiúsculas — *"o portal vem com
Sandbox selecionado… com uma credencial de Sandbox, os pedidos reais da sua loja não chegam ao
Entregas Expressas"*. Pelo painel, essa escolha **não existe**: as duas gravações forçam
produção no back-end.

```ts
// case 'create'
r = await chamarApi(empresaID, usuarioID, 'POST', '/credentials', {
  scopes: body.scopes, active: body?.active === true, sandbox: false,
});

// case 'webhookSave'
payload.sandbox = false;
r = await chamarApi(empresaID, usuarioID, 'POST', '/webhooks', payload);
```

E as duas listagens escondem o que é de teste: `lista.filter(c => !c.sandbox && !c.main …)` na
credencial e `brutos.filter(w => !w.sandbox)` no webhook. Quem cadastra pelo painel não
consegue criar, nem ver, credencial ou webhook de sandbox.

## Aba Credencial

- **A credencial principal já existe.** `chamar('main')` a traz pronta; não há passo de criação
  para quem só precisa de uma. O rodapé do cartão diz *"Esta é a credencial exibida no portal
  docs.beefood.app"* — é a mesma dos dois lugares.
- **O `clientSecret` pode ser revelado depois.** O ícone de olho chama `action: 'secret'` →
  `GET /credentials/<id>/secret`. O artigo do parceiro avisa que o segredo *"aparece uma única
  vez"*, o que vale para o portal; no painel não vale, e o manual diz isso.
- **Oito recursos, dois interruptores cada:**

  | Recurso (`id`) | Rótulo | Descrição na tela |
  |---|---|---|
  | `orders` | Pedidos | Consultar e criar pedidos |
  | `catalog` | Catálogo | Produtos, grupos e complementos |
  | `customers` | Clientes | Dados dos clientes |
  | `store` | Loja | Horários, entrega e pagamentos |
  | `coupons` | Cupons | Cupons de desconto |
  | `reviews` | Avaliações | Avaliações dos clientes |
  | `drivers` | Entregadores | **Em breve** (travado) |
  | `stock` | Estoque | **Em breve** (travado) |

  O que o Entregas Expressas pede — *Loja (leitura)* e *Pedidos (leitura e escrita)* — vira
  `store:read` e `orders:read`/`orders:write`.
- **Quem altera também consulta.** `comRead()` acrescenta o `:read` de todo `:write`, e o
  interruptor *Consultar* fica desabilitado quando *Alterar* está ligado (`disabled={… || writeOn}`),
  com o `title` *"Quem altera também consulta"*. Vale na vinda do servidor, na tela e no envio.
- **Credencial nova nasce com tudo ligado:** `SCOPES_PADRAO_NOVA` = todos os recursos não
  marcados como *em breve*, em `read` e `write`. Então o mínimo que o parceiro pede já vem
  satisfeito, e o manual não precisa ensinar a ligar nada.
- **`SALVAR PERMISSÕES` só habilita depois de mudar algo** (compara os scopes ordenados com os
  da credencial). É o que torna seguro fotografar a tela sem alterar nada.
- **RECICLAR (`rotate`) é o botão que derruba a integração.** Texto do diálogo: *"O Client ID e
  o Client Secret serão trocados e todas as conexões atuais param imediatamente. O parceiro
  precisará atualizar os dois valores."* Virou aviso no manual.
- **EXCLUIR não aparece na principal** (`{!c.main && …}`); a principal só pode ser desativada
  pela chave ou reciclada.

## Aba Webhooks

- **Cinco eventos**, e o back-end só aceita esses cinco (`EVENTOS` em `index.ts`):
  `order_created` (Pedido criado), `order_updated` (Pedido atualizado),
  `order_delivery_updated` (Entrega atualizada), `payment_created` (Pagamento criado),
  `payment_updated` (Pagamento atualizado).
- **Validações, todas no back-end além do front:** URL precisa casar `/^https:\/\//` e ter até
  2048 caracteres; ao menos um evento; `ownerEmail` com `@` e até 255; e `user`/`password`
  **viajam juntos ou nenhum** — *"Informe usuário e senha juntos, ou deixe os dois em branco"*.
  Na edição, deixar os dois em branco **mantém** o que já estava gravado.
- **O rótulo engana quem vem do artigo.** Os campos da autenticação Basic chamam-se
  `clientId (usuário)` e `clientSecret (senha)` na tela do BeeFood, e o Entregas Expressas
  mostra os mesmos dois valores como **Usuário** e **Senha**. São os valores do parceiro, não
  os da credencial da API — o manual precisa dizer isso com todas as letras, porque os nomes
  colidem.
- **O *Secret do webhook* é da BeeFood, não do parceiro.** `webhookSave` devolve `secret` e a
  tela o mostra uma vez, com *"Guarde este secret agora — ele não poderá ser exibido
  novamente"* e o botão **JÁ GUARDEI**. É o valor de quem recebe o aviso para conferir que ele
  é legítimo. O Entregas Expressas não pede esse valor: ele se identifica pelo usuário e senha
  do campo Basic.
- **A chave da linha desativa sem apagar** (`webhookSave` com `active: false`, mandando a URL e
  os eventos de volta). **EXCLUIR** é definitivo: *"As notificações para esta URL param
  imediatamente e a exclusão não pode ser desfeita."*

## Aba Avançado — o caminho que este manual não usa

*Aplicativos conectados* lista as conexões **OAuth** (`GET /credentials/oauth`), com
`clientName`, data e escopos, e um **CANCELAR ACESSO** por linha. É o caminho em que o parceiro
pede autorização e o lojista aprova, sem copiar e colar nada. O Entregas Expressas não usa isso
hoje: ele pede Client ID e Client Secret na própria tela. Fica registrado porque, no dia em que
usar, o passo 1 deste manual deixa de ser necessário.

## O que é do parceiro, e por isso entra no manual como informação dele

Estas afirmações vêm do artigo do Entregas Expressas e **não** foram verificadas aqui — a
lógica é do lado deles ou da API, não do painel:

- a BeeFood desativa o webhook depois de **5 falhas seguidas**;
- o Entregas Expressas faz uma **conferência a cada 10 minutos** para não perder pedido;
- a coleta passa o pedido a **despachado** e a entrega a **entregue** no BeeFood (é o que a
  opção *Atualizar o status do pedido na BeeFood* promete);
- pedido de **retirada, balcão ou mesa** não vira entrega, e nem pedido entregue pela logística
  do próprio marketplace.

No manual elas aparecem como comportamento da integração, com o cuidado de não prometer tela do
BeeFood que não foi fotografada.
