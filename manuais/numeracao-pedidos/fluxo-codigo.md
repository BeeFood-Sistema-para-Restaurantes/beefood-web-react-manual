# fluxo-codigo — Entendendo a numeração dos pedidos (#74)

Mapeamento técnico, a partir do código do `beefood-web-react` e de dado real do sandbox.
**Não publicar.** O manual do usuário é o `numeracao-pedidos.md`.

---

## Os campos

| Campo da API | Nome no manual | O que é |
|--------------|----------------|---------|
| `numeroPreVenda` | número da venda | Contador único da loja. Nunca reinicia |
| `numeroPedido` | número do pedido | Contador do caixa. Reinicia em 1 a cada caixa novo |
| `preVendaID` | — | Chave técnica do banco. Só aparece como reserva (ex.: `#{numeroPedido ?? preVendaID}` em Gestão de Entregas) |
| `referencia` / `ifoodShortReference` | — | Código curto do marketplace. No card do Delivery tem prioridade sobre os dois acima |
| `numeroVenda` | — | Apelido: no módulo de caixa é o número da venda; na resposta de `venda2/salvar` chega como sinônimo de `numeroPedido` (`PedidoFields.tsx`) |

---

## Quem gera

O painel **nunca** calcula número. `src/utils/pedidoBuilder.ts` envia só `numeroPreVenda`
(quando a venda já existe) e **nunca** envia `numeroPedido`. Os dois voltam na resposta de
`POST /api/venda2/salvar` e são apenas lidos:

```ts
// src/components/PedidoFields.tsx
const numeroPreVendaInfo = resultado?.numeroPreVenda ?? resultado?.result?.numeroPreVenda ?? numeroPreVenda ?? null;
const numeroVendaInfo =
  resultado?.numeroPedido ?? resultado?.result?.numeroPedido ??
  resultado?.numeroVenda ?? resultado?.result?.numeroVenda ?? null;
```

O PDV envia `numeroPedido: null` em **todos** os pontos, com comentário explícito:

```ts
// src/pages/PDV.tsx
numeroPreVenda: numeroPreVendaAtual || null,
numeroPedido: null, // PDV não tem numeroPedido
```

Por isso a tela do PDV mostra apenas `VENDA Nº {numeroPreVendaAtual}` — mesmo quando o servidor
atribuiu um número de pedido àquela venda.

**Consequências:** não há campo para digitar número; reabrir venda não renumera
(`docs/PDV_REABRIR_VENDA.md`: *"Reabrir ≠ criar"*); agrupar vendas manda só os `numeroPreVenda`
de origem (`src/lib/api/agruparVenda.ts`).

---

## O parâmetro do PDV

`pdvNumeroPedido`, boolean.

| Onde | Arquivo |
|------|---------|
| Tela (desktop) | `src/pages/Parametros.tsx` — card **PDV**, label *Número de Pedido no PDV*, ajuda *Exibir número do pedido nas vendas* |
| Tela (mobile) | `src/components/mobile/parametros/MobileParametrosPage.tsx` |
| GET / POST | `src/hooks/useEmpresaParametros.ts` → `/api/empresa2/empresaConfig` |
| Cache | `src/utils/configCache.ts` (`EmpresaConfigCache`) |

Auto-save de **500 ms** e `refreshCache()` depois do POST. Fallback de exibição `?? false`.

**O front não consome esse parâmetro em nenhum lugar** — nem no PDV, nem em Mesas, nem no
Delivery, nem na impressão. Quem decide atribuir o número é o **backend**. O parâmetro só existe
para o PDV: **não há** `mesaNumeroPedido` nem `deliveryNumeroPedido` no código.

---

## Onde os números aparecem

Regra geral: tem `numeroPedido`? Escreve `numeroPedido (numeroPreVenda)`. Não tem? Só o
`numeroPreVenda`. O que muda é o prefixo e a condição.

| Onde | Arquivo | Formato | Condição |
|------|---------|---------|----------|
| Cupom do cliente | `src/lib/cupom-pedido-utils.ts` | `Pedido #X (Y)` / `Venda Nº Y` | `numeroPedido > 0` |
| Cupom de divisão | `src/lib/cupom-divisao-utils.ts` | idem | idem |
| Impressão de cozinha (manual) | `src/components/VendaDetalhes.tsx` | idem | idem |
| Histórico de Vendas | `src/pages/HistoricoVendas.tsx` | `X (Y)` / `Y` | ambos truthy |
| Delivery (card) | `src/pages/Delivery.tsx` | `#X (Y)` / `#Y` | `numeroPedido !== numeroPreVenda` |
| Delivery (lista) | `src/components/delivery/DeliveryListView.tsx` | `#X` (coluna Pedido) | `??` |
| Detalhe da venda | `src/components/VendaDetalhes.tsx` | `Venda Nº Y` + ` • Pedido Nº X` | `numeroPedido > 0` |
| Fichas do PDV | `src/hooks/usePDVImpressaoFichas.ts` | `Venda Nº X (Y)` | ambos truthy |
| Vendas pendentes do caixa | `src/components/caixa/CaixaVendasPendentesModal.tsx` | colunas separadas *Nº Pedido* e *Nº PreVenda* | — |
| Layout da ficha de cozinha | `src/components/impressao/LayoutCozinhaEditor.tsx` | opções *Nº do pedido e venda* / *Nº do pedido* / *Nº da venda* | escolha do usuário |
| NF-e / NFC-e | `src/pages/NFe.tsx`, `NFCe.tsx` | *Nº Venda* = `Y` | só `numeroPreVenda` |
| Movimentações | `src/pages/Movimentacoes.tsx` | `Venda #Y` | só `numeroPreVenda` |
| Fiado | `src/components/fiado/*` | `Venda #Y` (reserva: `preVendaID`) | só `numeroPreVenda` |
| Excel do histórico | `src/utils/excelExport.ts` | coluna *Nº Pedido* = `numeroPedido \|\| numeroPreVenda` | — |
| Excel de cupons | `src/utils/excelExport.ts` | colunas *Nº Pedido* e *Nº Pré-Venda* separadas | — |

Duas armadilhas que **não** entraram no manual do usuário, mas valem para o suporte:

- **Busca do Delivery.** Usa um campo derivado (`numero = numeroPedido || numeroPreVenda`), então
  procurar pelo número da **venda** de um pedido que tem número de pedido pode não achar. No
  Histórico de Vendas a busca cobre os dois (`HistoricoVendas.tsx`).
- **Ordenação da coluna *Nº Pedido*** ordena por `numeroPedido` com reserva no `numeroPreVenda`.
  Como o número do pedido reinicia, vendas de caixas diferentes se embaralham nessa ordenação.

---

## A prova do reset (dado real, 01/09/2026)

Sandbox **BeeFood3 - Manual** (`empresaID` 38311). Levantamento por API autenticada, somente
leitura, cruzando `venda2/historicoVendas`, `caixa2/caixaListagem`, `venda2/vendaDetalhes` e
`empresa2/empresaConfig`.

### O número da venda não reinicia

304 vendas na faixa **627 a 930**: 304 números distintos, **zero repetido e zero buraco**. Um
contador que reiniciasse produziria número repetido; um que pulasse produziria buraco.

### O número do pedido reinicia por caixa

| Caixa | Abertura | Fechamento | Nº de pedido | Nº de venda |
|-------|----------|------------|--------------|-------------|
| 893187 | 18/06 21:29 | 01/07 16:08 | 41 … 50 | 627 … 633 |
| 907962 | 01/07 16:09 | 17/07 11:58 | *quase nenhum* | 630 … 719 |
| 927703 | 17/07 11:59 | 19/08 10:54 | **1 … 110** | 720 … 842 |
| 967508 | 19/08 10:35 | 01/09 16:39 | **1 … 60** | 843 … 930 |
| 983507 | 01/09 16:39 | *aberto* | **1 … 2** | 931 … 932 |

O caixa 927703 abriu em **17/07 11:59:02** e o **pedido nº 1 dele saiu em 11:59:06 — quatro
segundos depois**.

Virada reproduzida ao vivo para este manual, com o caixa 983507 recém-aberto pelo dono:

```
930 -> pedido 60   (caixa 967508, último antes do fechamento)
931 -> pedido  1   (caixa 983507, primeiro do caixa novo)
932 -> pedido  2
```

### Mesa não recebe e não consome

No caixa 927703: 123 vendas no período, **110 números de pedido usados na faixa 1..110, sem um
único buraco**, e 13 vendas sem número (5 de mesa e 8 de PDV, essas de antes do parâmetro ser
ligado). Se venda sem número consumisse um número, apareceriam buracos.

Confirmado também na tela (imagem 03 do manual): vendas de mesa 854–858 entre os pedidos 5 e 6.

### Quando o parâmetro do PDV foi ligado

```
última venda de PDV SEM número de pedido ..... 21/08/2026 16:21   venda 846
primeira venda de PDV COM número de pedido ... 21/08/2026 16:33   pedido 2, venda 847
```

Doze minutos entre as duas — foi durante a produção do manual **#44**, que é o manual desse
switch.

---

## Descoberta que ficou FORA do manual (decisão do dono, 01/09/2026)

**O caixa precisa ser aberto com o checkbox Delivery marcado** para os pedidos de delivery
receberem número.

| Caixa | Delivery marcado na abertura | Delivery com número | Delivery **sem** número |
|-------|------------------------------|--------------------:|------------------------:|
| 893187 | Sim | 5 | 0 |
| **907962** | **Não** | 2 | **79** |
| 927703 | Sim | 110 | **0** |

Setenta e nove pedidos de delivery em 16 dias ficaram sem número porque o caixa aberto não
contemplava delivery, e **a tela não avisa nada**. O dono decidiu não incluir no manual (mistura
o assunto com o de abrir caixa). Fica registrado aqui para o suporte e para um eventual
complemento no manual de Caixa.

> Ruído do sandbox a ignorar em qualquer novo levantamento: 17 vendas de delivery sem número no
> caixa 967508 foram criadas **em lote pela API** por scripts de manuais anteriores (10 delas no
> mesmo segundo, 29/08 14:53:21). Não são regra do produto.

---

## Duas armadilhas do levantamento

1. **Não use o `caixaID` gravado na venda** para associá-la a um caixa: ele fica `null` enquanto
   a venda não é liquidada (217 das 304 vinham `null`) e esconde o padrão. Associe pela **janela
   de tempo** do caixa (abertura → fechamento).
2. **Marketplace grava a hora fora de ordem.** Pedidos do AIQFome saem com `horaCadastro`
   desalinhado da ordem de criação (a venda 630 aparece depois da 633). Isso produz "reset"
   falso em análise cronológica. Reset real é o que cai **para 1**.

---

## Pergunta em aberto

**Com dois caixas abertos ao mesmo tempo, a contagem de pedido é por caixa ou única?** O sandbox
tem `caixaPorUsuario: true` e `qtdCaixas: 10`, mas nunca houve dois caixas abertos juntos, então
o dado não responde. O manual foi escrito **no singular** ("o caixa aberto") e não afirma nada
sobre caixas simultâneos.

---

## O que o backend não pôde confirmar

O repositório do servidor (`beetechbr/beetech-server-node-2.0`) **não clonou** na sessão deste
manual: o `BITBUCKET_TOKEN` não autentica mais (testadas as quatro combinações de usuário e
secret). Toda a regra do reset foi provada por **dado real**, não por leitura do código do
servidor. O objeto do caixa tem um campo `numeroPedido` (`src/hooks/useCaixaDetalhes.ts`), que é
o candidato natural a guardar o contador, mas ele volta `null` na listagem e o painel não o usa
— **não confirmado**.
