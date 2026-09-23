# fluxo-codigo.md — Venda Sugestiva (UpSell) (#103)

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `venda-sugestiva-upsell.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Mapeamento técnico feito no `beefood-web-react` (commit `029145e`, 17/09/2026), no
`beefood-reports-hub` e no bundle do cardápio público (`menu.beefood.com.br`).
**Documento interno — não publicar.**

## 1. Onde mora

| Arquivo | Papel |
|---------|-------|
| `src/utils/vendaSugestivaAcesso.ts` | Liberação (`podeUsarVendaSugestiva`) |
| `src/hooks/useProdutoUpsell.ts` | GET/POST da configuração + `MAX_UPSELL = 6` |
| `src/components/cardapio/ModalVendaSugestivaGeral.tsx` | Janela **geral**: lista de produtos (três pontinhos da tela Cardápio) |
| `src/components/cardapio/ModalVendaSugestiva.tsx` | Janela **de escolha**: até 6 produtos de um produto |
| `src/components/cardapio/ProdutoVendaSugestivaTab.tsx` | Aba **Venda Sugestiva** dentro do cadastro do produto |
| `src/components/cardapio/FiltroSetoresPopover.tsx` | Filtro de setores + ordenação igual à grade de `/cardapio` |
| `src/pages/Cardapio.tsx` / `MobileCardapioPage.tsx` | Item do menu de ações da página |
| `src/components/cardapio/VirtualizedProductGrid.tsx` / `MobileCardapioProdutos.tsx` | Item no menu de três pontinhos do produto |
| `src/hooks/useEditarProdutoLogic.ts` | Registro da aba (`allTabs`) |
| `beefood-reports-hub/src/components/reports/DigitalMenuSuggestions.tsx` | Relatório de Sugestões (delivery e presencial) |

## 2. Liberação

```ts
const VENDA_SUGESTIVA_EMPRESAS = [107, 38311];
export const podeUsarVendaSugestiva = (): boolean => {
  if (isDevelopment) return true;
  const empresaID = Number(getUserSession()?.empresaID);
  return VENDA_SUGESTIVA_EMPRESAS.includes(empresaID);
};
```

Sem a liberação **nada aparece**: nem o item no menu da página, nem no menu do
produto, nem a aba do cadastro (`allTabs.filter(t => t.id !== 'venda-sugestiva' || canUpsell)`).
Não existe permissão nova de grupo de acesso — acompanha quem já edita produto.
O sandbox dos manuais (**38311**) está na lista, por isso a captura sai de produção.

## 3. API

| Verbo | Rota | Retorno |
|-------|------|---------|
| GET | `/datasnap/rest/produto2/cardapio/produto/upsell/{empresaID}/{filialID}/{usuarioID}/{produtoID}` | `{ resultado, produtoID, filialID, produtos: number[] }` |
| POST | `/datasnap/rest/produto2/cardapio/produto/upsell` | `{ resultado, msg }` |

Corpo do POST: `{ empresaID, filialID, usuarioID, produtoID, produtos, descricao,
nomeFantasia, usuario }`.

Regras do `useProdutoUpsell`:

- `filialID = filialAtual?.filialID || userData.filialID` → **a configuração é por
  cardápio (filial)**. Trocar de cardápio mostra outra seleção.
- Antes de enviar: remove duplicados e o **próprio `produtoID`**, e corta em `MAX_UPSELL` (6).
- **`produtos: []` limpa** a configuração — não existe DELETE.
- A **ordem do array é a ordem de exibição** ao cliente. Nada é reordenado por nome.
- Toast só no POST; erro de GET fica como lista vazia na tela.
- Sem cache: nada em `localStorage`.

A listagem `produto2/cardapio` traz o campo `upsell` (objeto `{"produtos":[...]}` ou
nulo) — é o que acende o selo **Configurado** e o contador **Somente configurados**.

## 4. Os três caminhos

### 4.1 Três pontinhos da tela Cardápio (`ModalVendaSugestivaGeral`)

- Só na aba **Produtos** (`activeTab === 'produtos' && podeUsarVendaSugestiva()`),
  rótulo **Venda Sugestiva (UpSell)** com o ícone `Sparkles` violeta.
- Carrega o catálogo por conta própria (`useProdutosCardapio`) e, **em lotes de 4**,
  chama `buscarUpsell` de cada produto que já tem `upsell` — é daí que saem as fotos
  da linha *Sugere:*.
- Filtros: busca (nome ou código), **filtro de setores** e botão
  **Somente configurados (n)**.
- Clicar na linha abre a janela de escolha. Ao salvar, a lista de trás é atualizada
  **em silêncio** (`onSalvo` + `refreshProdutos`): mantém busca, filtro e rolagem.
- Rodapé só com **FECHAR (ESC)**.

### 4.2 Três pontinhos do produto (`ModalVendaSugestiva`)

- No desktop entra entre **Clonar** e **Converter em Complemento**; no celular, no
  menu que sobe de baixo, no mesmo lugar (e o menu fecha ao abrir a janela).
- Rótulo curto: **Venda Sugestiva**.
- Faixa de **chips** dos selecionados (foto + nome + X), fora da rolagem, contador
  `{n}/6`; chip inteiro clicável remove.
- Lista: checkbox + foto + nome + setor + preço, **sem o próprio produto**, com
  produto **inativo** presente e marcado com o selo *Inativo*.
- Limite: com 6 marcados os checkboxes dos outros ficam desabilitados e aparece
  *"Limite de 6 atingido. Remova um para escolher outro."*
- **SALVAR (F2)** e **CANCELAR (ESC)**. Fechar sem salvar descarta sem confirmação.
  Salvar com zero selecionados é válido (limpa).
- Ordenação: `criarComparadorOrdemCardapio` → setores na ordem da grade de
  `/cardapio` (`ordem` asc, nulo por último, desempate por título) e, dentro do
  setor, `ordemProduto`.

### 4.3 Aba do cadastro do produto (`ProdutoVendaSugestivaTab`)

- Aba **Venda Sugestiva**, a última de `allTabs`; **não existe para complemento**
  (`hideForComplemento`).
- Produto novo, ainda sem `produtoID`: *"Salve o produto antes de configurar a venda
  sugestiva."*
- **Salva sozinho** a cada clique (`salvarUpsell({ silencioso: true })`): a etiqueta
  alterna entre *Salvo automaticamente* e *Salvando...*, e o item volta ao estado
  anterior se a API recusar. Não há botão de salvar próprio da aba.
- Só busca a configuração quando a aba está ativa (`isActive`).

## 5. O que o cliente vê (cardápio público)

Bundle Nuxt de `menu.beefood.com.br` (store `upsell`, componente `ModalUpsell`,
classes `modal-upsell__*`). A action `openUpsell` roda depois de o item entrar no
carrinho e:

1. Lê o `upsell` do produto (aceita array ou `{"produtos":[...]}`, em JSON ou string).
2. Descarta o próprio produto, **o que já está no carrinho**, o inativo e o
   `disabled`.
3. Corta em **6** e, se sobrar alguém, abre a janela; senão não abre nada.

A janela mostra a foto do produto que acabou de entrar, *"Você adicionou
&lt;produto&gt;."*, o título **Que tal levar junto?**, os cards (nome, descritivo e
preço já com desconto/preço programado) e o rodapé **CONTINUAR SEM ADICIONAR**.
Tocar num card **fecha a sugestão e abre o produto normal** (foto, observação,
cashback, quantidade) — quem confirma é o **Adicionar** do produto.

Testado em 17/09/2026 em `menu.beefood.com.br/beefood3` (delivery) e
`menu.beefood.com.br/beefood3/?tipo=p` (presencial): mesma janela nos dois.
O tablet e o totem são aplicativos (APK), fora do alcance do Cloud Agent.

> Não confundir com as **sugestões automáticas**, que são outra coisa no mesmo
> bundle: `recalculateSuggestions` lê o campo `sugestoes` de cada item do carrinho
> (histórico de vendas) e monta uma lista **dentro do carrinho**, sem configuração
> no painel. O manual não fala disso.

## 6. Relatório

`DigitalMenuSuggestions.tsx` no `beefood-reports-hub`:

- `GET {REPORT_API}/api/relatorio2/relatorioSugestao/{empresaID}/{inicio}/{fim}/{tipo}`
  com `tipo = 1` (delivery) e `tipo = 2` (presencial) — as duas abas **Sugestões** do
  Desempenho usam o mesmo componente.
- Cada linha é um item sugerido e aceito: `preVendaID`, `numeroPreVenda`,
  `dataVenda`, `horaCadastro`, `descricao`, `vendaUnt`, `qtd`, `composicao`, `origem`.
- A tela monta: três cards (**Valor Total de Sugestões**, **Quantidade de Sugestões**,
  **Valor Médio por Sugestão**, cada um comparado com o período anterior de mesmo
  tamanho), o gráfico por dia, **Mais Sugeridos por Valor**, **Mais Sugeridos por
  Quantidade** (top 10 cada) e três cards de insight.
- **Exportar Excel** (`sugestoes_cardapio_digital_<Delivery|Presencial>_<dd-mm-aaaa>_<dd-mm-aaaa>.xlsx`)
  é o único lugar que mostra a coluna **Origem** de cada linha.
- Permissão do menu: `['delivery','items','sugestoes']` e
  `['presencial','items','sugestoes']` (`accessControl.ts`).

O relatório **não separa** upsell de sugestão automática na tela: os dois entram
juntos nos mesmos números.

**O relatório é processado uma vez por dia — até 24 horas de atraso** (informação do
dono, 17/09/2026). `relatorioSugestao` chama a proc `procRelatorio_BeeFood_Sugestao`, que
lê a base já processada, e não a venda ao vivo.

Foi o que a medição do mesmo dia mostrou, com duas vendas do sandbox: a **809** (13/08,
`situacao FECHADO`, `esteira=1`) aparece com as 4 linhas que somam os R$ 44,00 da imagem
09; a **1013** (17/09, feita para este manual, upsell aceito, `situacao RECEBIDO`,
`valorPago 51,94`, `esteira=0`) **não** aparece. O `tipo=2` (presencial) devolve `null`
para `2026-01-01..2026-12-31` — nunca houve sugestão aceita no presencial deste sandbox.

> Correção: a primeira leitura deste documento atribuía a ausência da 1013 ao **caixa
> ainda aberto** (esteira). A causa é o **processamento diário**. Não há necessidade de
> fechar caixa para conferir relatório — basta esperar o processamento.

O item aceito é marcado no `pedidoPOST.js` do backend:
`{ name: "sugestao", sqltype: sql.Bit, value: !!prod.sugestao ? true : null }`.

## 7. Armadilhas de captura

- Produto do combo já vem com a **única opção do primeiro grupo obrigatório
  pré-selecionada**. Clicar nela *desmarca* e o **Adicionar** devolve *"Verifique a
  quantidade do grupo &lt;nome&gt;"*. Só marque grupo cujo cabeçalho ainda mostra
  **OBRIGATÓRIO**.
- A janela de sugestão é `fullscreen`: o print do celular pega ela inteira, sem o
  cardápio atrás.
- A base do sandbox tem **21 nomes de produto repetidos**. Os combos e as sobremesas
  têm nome único — foi por isso que o exemplo do manual usa **Combo One Burger**.
- Cache do cardápio público: até **1 minuto** depois de salvar.
