# fluxo-codigo.md — Programa de pontos (#126)

Estudo do código e das rotas por trás do manual. **Não é material de publicação**: serve para a
próxima pessoa que mexer no assunto não precisar redescobrir nada, e para o time de produto ler os
três defeitos da última seção.

Lido em duas frentes:

- **Painel** — `beefood-web-react` em `~/refs/beefood-web-react` (commit `4fc5d6c`).
- **Cardápio digital** — o repositório é um Nuxt 2 que não se consegue clonar deste ambiente, então
  o código foi lido no **bundle publicado** de `menu.beefood.com.br` (198 chunks baixados para
  `/tmp/cd-bundle`). É a mesma técnica do #125, e continua sendo o caminho mais curto quando a tela
  é do cardápio público.

## Onde fica cada coisa

| Camada | Arquivo |
|---|---|
| Página, com as quatro abas | `src/pages/ProgramaPontos.desktop.tsx` |
| Aba Configuração | `src/components/crm/pontos/ProgramaPontosConfiguracaoTab.tsx` |
| Recompensas (desconto e produto) | `src/components/crm/pontos/ProgramaPontosRecompensas.tsx` |
| Seletor de produto da recompensa | `src/components/crm/pontos/ModalSelecionarProdutoRecompensa.tsx` |
| Aba Histórico | `src/components/crm/pontos/ProgramaPontosHistoricoTab.tsx` |
| Aba Saldo por Cliente | `src/components/crm/pontos/ProgramaPontosSaldoClienteTab.tsx` |
| Aba Fila Processamento | `src/components/crm/pontos/ProgramaPontosFilaTab.tsx` |
| Extrato do cliente (painel lateral) + ADICIONAR/REMOVER/TRANSFERIR | `src/components/cardapio-digital/ModalExtratoPontosCliente.tsx` |
| Migração de programa | `src/components/crm/pontos/ModalMigrarCashback.tsx` e `ModalMigrarPontos.tsx` |
| Diálogo de exclusividade | `src/components/crm/ConfirmarExclusividadeFidelidade.tsx` |
| Estado e gravação da configuração | `src/hooks/useProgramaPontos.ts` |
| Produtos para a recompensa | `src/hooks/useProdutosCardapio.ts` |

**Rota e permissão.** A rota é `/programa-pontos` (`src/App.tsx`), e o `ProtectedRoute` usa
`submenuKey="crm"` com `submenuItemKey="cashback"` — ou seja, **a permissão é a mesma do
Cashback**, não existe item de permissão próprio para os pontos. Quem vê um, vê o outro.

## Gravação da configuração: auto-save com 600 ms

`useProgramaPontos.ts` guarda os itens por `filialID` e agenda a gravação:

```ts
const agendar = useCallback((filialID: number, immediate?: boolean) => {
  const prev = timers.current.get(filialID);
  if (prev) clearTimeout(prev);
  timers.current.delete(filialID);
  if (immediate) { persist(filialID); return; }
  timers.current.set(filialID, setTimeout(() => {
    timers.current.delete(filialID);
    persist(filialID);
  }, 600));
}, [persist]);
```

Não há botão de salvar, e o switch de ativação grava com `immediate = true` (seguido de um
`refetch` 600 ms depois), porque ligar o programa tem efeito colateral — desligar o cashback.

## Exclusividade com o cashback

Está no front, nos dois sentidos. Ligar os pontos com `cashBackAtivo` mostra o aviso no cartão e,
no clique, o `ConfirmarExclusividadeFidelidade` com `programaAtivar="pontos"`; o espelho disso
está em `CashbackConfiguracaoCRMTab.tsx` com `programaAtivar="cashback"`. O texto do diálogo e o
rótulo do botão (`ATIVAR E DESATIVAR O CASHBACK`) saem desse componente, montados por template —
é por isso que o manual pôde citá-los palavra por palavra.

A conversão de saldo é outra coisa, e é de servidor:

| Botão | Rota |
|---|---|
| **TRAZER PARA PONTOS** | `POST /api/empresaDelivery2/cardapioDigital/pontos/migrarPontos` com `pontosPorReal` |
| **MIGRAR PARA CASHBACK** | a irmã, com `centavosPorPonto` e `tetoCashback` |

A resposta traz `clientesAfetados` e `pontosGerados`, que viram o texto do aviso de sucesso. Nada
disso foi executado na sandbox: as duas ações zeram saldo de todos os clientes e são irreversíveis.

## Recompensas

Duas listas no mesmo cartão, lidas e gravadas em `crm.beetechapi.be`:

```
GET  https://crm.beetechapi.be/api/rest/pontos/recompensas/<filialID>
POST https://crm.beetechapi.be/api/rest/pontos/recompensas
```

Cada recompensa tem `tipo` (`desconto` ou `produto`), `pontos` e, no caso de produto, `produtoID`.
A equivalência em reais que aparece em cinza (*≈ R$ 100,00 em compras*) é calculada no front, com
o `pontosPorReal` atual — ela muda se você mudar a régua, sem ninguém editar a recompensa.

O nome do produto na lista vem de um `Map` montado com o cardápio atual, e o fallback é o que
produz a linha `Produto #<id>`:

```tsx
const nomeProduto = useMemo(() => {
  const m = new Map(produtos.map((p) => [p.produtoID, p.descricao]));
  return (id: number) => m.get(id) ?? `Produto #${id}`;
}, [produtos]);
```

## O cardápio digital

Tudo gira em volta de `dadosEmpresa.pontosAtivo` e de `isPresencial`. As quatro aparições, com a
condição de cada uma — medidas no bundle, não deduzidas:

| O que | Condição |
|---|---|
| Faixa amarela *Acumule pontos a cada compra 🎁* na home | `1 == dadosEmpresa.pontosAtivo` — **só isso**. Não depende de recompensa nem de login |
| Item **Programa de pontos** no menu do Perfil | `showPontos: pontosAtivo && !isPresencial` |
| Janela **Meus pontos** / **O que você pode ganhar** | a mesma janela, com `view === 'extrato'` alternando o título. Sem recompensa: *"Nenhuma recompensa disponível no momento."* |
| Cartão **Troque pontos por recompensas**, na sacola | `!isPresencial && pontosAtivo && (recompensasDesconto.length > 0 \|\| produtosResgataveis.length > 0)` |

O `!isPresencial` é o que tira o programa inteiro do cardápio de mesa (QR Code): a venda presencial
acumula, se o canal estiver ligado, mas o cliente não vê nada na tela.

E é aqui que mora o defeito principal:

```js
produtosResgataveis: function () {
  var t = this;
  return this.recompensasProduto
    .map(function (o) { var s = t.encontrarProduto(o.produtoID); return s ? { ... } : null })
    .filter(function (o) { return null !== o });
}
```

A recompensa de produto só entra na vitrine se `encontrarProduto(produtoID)` achar o item **no
catálogo público**. Quando não acha, a recompensa é descartada em silêncio.

## Os três defeitos encontrados

### 1. Recompensa de produto cadastrada pelo painel não chega ao cliente

O seletor do painel lista produtos de
`/api/produto2/cardapio/produtos/38311/39202/88711`, onde o CHICKEN DELUXE é o `produtoID`
**2624069** (todo o cardápio está na faixa 2624013–2624160). O catálogo público do cardápio usa
**2515303** para o mesmo produto.

Medido com as duas recompensas cadastradas no sandbox:

```
GET https://crm.beetechapi.be/api/rest/pontos/recompensas/39202
→ { tipo: "produto", produtoID: 2515303, pontos: 100 }   aparece no cardápio
→ { tipo: "produto", produtoID: 2624069, pontos:  80 }   NÃO aparece no cardápio
```

A segunda foi cadastrada por nós, pelo painel, pelo caminho que o lojista usa. A primeira já
existia na base, com o id do catálogo público.

O mesmo desencontro, visto do outro lado, é o que faz a linha `Produto #2515303` aparecer no
painel: o id público não está na lista do cardápio que o painel carregou, então o nome não resolve.
**As duas anomalias são o mesmo bug**, e ele tem um sinal fácil de reconhecer: a recompensa que o
painel mostra com código é a que funciona; a que ele mostra com nome é a que o cliente não vê.

O manual não esconde isso — a seção 5 manda conferir no cardápio depois de cadastrar, e explica o
sintoma. Mas a correção é no produto: ou o painel grava o id do catálogo público, ou o cardápio
passa a resolver os dois.

### 2. A hora do painel está três horas à frente

O mesmo lançamento, nas duas telas:

| Tela | Texto |
|---|---|
| Painel (Histórico e extrato do cliente) | `07/10/26 15:23` |
| Cardápio (Meus pontos) | `07/10/2026 às 12:23` |

E o anterior: `05/10/26 23:31` no painel, `05/10/2026 às 20:31` no cardápio. A diferença é
constante de três horas — o painel está mostrando a hora do servidor (UTC) sem converter para
`America/Sao_Paulo`, e o cardápio converte. Quem compara as duas telas na frente do cliente vê
duas horas diferentes para o mesmo crédito.

### 3. Os sinais do extrato do cliente estão com as cores trocadas

Na janela **Meus pontos**, *Ganhou* vem com um ícone **+ vermelho** e *Usou* com um ícone
**− verde**. No painel é o contrário, e corretamente: crédito em verde, débito em vermelho. É
cosmético, e está no FAQ do manual para quem for perguntado.

## O totem não tem tela de pontos

Procurado no bundle do totem: **zero** ocorrência de "pontos". O totem é `?tipo=p`
(`isPresencial`), e as três aparições que dependem de `!isPresencial` — item do Perfil, cartão da
sacola e, portanto, o resgate — ficam de fora por construção. A modalidade **Pedidos via Totem**
existe na configuração e faz o acúmulo acontecer; o que não existe é a tela.

O **cardápio digital tablet** é um APK Android, que não se instala nem se fotografa neste ambiente
(regra da seção 6 da `MEMORIA-GERAL.md`). O que o manual afirma sobre ele é o que se deduz da
arquitetura: ele registra pedido por um dos canais, e o acúmulo segue o canal da venda.

## A fila da madrugada

A aba **Fila Processamento** lê uma fila de vendas aguardando crédito, com `status`
(`Pendente` / `Sucesso` / `Erro`), `tentativas` e `mensagem`. A mensagem mais comum no sandbox é
`Venda sem consumidor (tentativas: 1)` — venda sem cliente identificado não tem a quem creditar.

Isso explica a arquitetura do recurso: **o crédito não é síncrono com o fechamento da venda**. Um
processo diário varre as vendas pagas e finalizadas e credita; a fila é a janela desse processo. O
crédito **manual** (ADICIONAR no extrato) não passa pela fila e vale na hora — é a diferença que o
manual usa para explicar cortesia.

## Tipos de lançamento no histórico

Os quatro primeiros foram vistos na sandbox; **EXPIROU** saiu do código
(`ModalExtratoPontosCliente.tsx`), porque nenhum lote venceu durante a produção do manual:

| Tipo | Significado |
|---|---|
| **Ganhou** | crédito, por venda ou por ajuste manual |
| **Usou** | débito por resgate ou por remoção manual |
| **CANCELOU** | estorno de resgate — pedido cancelado devolve os pontos (`Estorno de resgate (remoção na venda)`) |
| **Migrou** | saldo convertido de cashback, pela migração em massa ou pelo TRANSFERIR de um cliente |
| **EXPIROU** | lote vencido. O extrato do cliente conta esses no cartão **Expirado** |

A coluna **Validade** é a data de expiração daquele lote, e vem vazia quando o programa está com
validade 0 ou quando o lançamento é débito.
