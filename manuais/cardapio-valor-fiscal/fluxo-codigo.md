# fluxo-codigo.md — #133 Valor fiscal por produto

> **Não publicar** — material interno. Leitura do `beefood-web-react` em 13/11/2026
> (`e434d07`, *"Novidade: Valor fiscal por produto (ajustes)"*), na cópia de referência
> `~/refs/beefood-web-react`.

## O nome do campo

| Onde | Como se chama |
|---|---|
| Na tela, para o usuário | **Valor fiscal** |
| No campo da API e no banco | `vendaFiscal` |
| Na edição em lote | `vendaFiscalCheck` + `vendaFiscal` |

O pedido que gerou este manual falava de *"campo venda fiscal"* — é o nome técnico do mesmo
campo. O manual usa **Valor fiscal** no corpo e cita *venda fiscal* no glossário, para a busca
achar pelos dois termos.

## Onde cada peça mora

| Peça | Arquivo |
|---|---|
| Normalização do valor | `src/utils/valorFiscal.ts` (`normalizarVendaFiscal`) |
| Teste da normalização | `src/utils/valorFiscal.test.js` |
| Campo no cadastro (desktop) | `src/components/ModalEditarProduto.tsx`, aba `produto`, bloco *Opções avançadas* |
| Campo no cadastro (celular) | `src/components/mobile/cardapio/MobileEditarProdutoPage.tsx` |
| Estado do formulário | `src/hooks/useEditarProdutoLogic.ts` (`ProdutoFormData.vendaFiscal`) |
| Leitura do produto | `src/hooks/useProdutoDetalhes.ts` |
| Gravação do produto | `src/hooks/useSalvarProduto.ts` |
| Campo na edição em lote | `src/components/cardapio/ModalEditarLote.tsx`, passo 2 |
| Envio do lote | `src/hooks/useEditarLote.ts` |
| Quem decide se o campo aparece | `src/lib/fiscalAutomatico.ts` (`empresaTemFiscalAtivo`) |

A conta da nota — repartir o total pago entre os itens — **não está no front**. Ela vive no
servidor, no momento da emissão; o front só guarda o número que o usuário digitou.

## A regra do valor

```ts
/** Valor fiscal do produto: só positivo vale; vazio, zero ou negativo viram null (emite pelo preço de venda). */
export const normalizarVendaFiscal = (v: number | null | undefined): number | null =>
  typeof v === 'number' && Number.isFinite(v) && v > 0 ? parseFloat(v.toFixed(4)) : null;
```

Três consequências que o manual precisa dizer em português:

| Digitado | Guardado | Efeito |
|---|---|---|
| vazio | `null` | emite pelo preço de venda |
| `R$ 0,00` ou negativo | `null` | idem — **não existe valor fiscal zero** |
| `R$ 8,00` | `8` | emite por R$ 8,00 |
| valor **maior** que o preço de venda | aceito | o front não barra; quem fecha a conta é o servidor |

O último caso é teste explícito do projeto: *"positivo é mantido, mesmo maior que a venda"*.
Essa é a brecha que o Passo 5 do manual cobre — o aviso de que a soma dos valores fiscais
não deve passar do total da nota, porque aí o servidor ajusta proporcionalmente.

`normalizarVendaFiscal` roda em quatro pontos: ao carregar o produto (`:317`), ao salvar
(`:444`), em cada tecla do campo (`handleCurrencyChange`, `:900`) e no lote. Ou seja, o valor
é normalizado na entrada e na saída — não há como gravar `0` por acidente.

## Quem vê o campo

```ts
/** A empresa tem fiscal quando alguma filial tem fiscal ativo. Sem isso, nada de fiscal é exibido. */
export const empresaTemFiscalAtivo = (filiais: FilialFiscal[]): boolean =>
  filiais.some(f => f.fiscalAtivo === true);
```

É **qualquer** filial, não a filial aberta na tela. Loja sem fiscal em nenhuma filial não vê o
campo — e é a primeira pergunta a fazer a quem disser *"não acho o campo Valor fiscal"*.

No cadastro de **complemento** o bloco *Opções avançadas* inteiro só existe por causa dele:

```tsx
{(!isComplemento || mostrarValorFiscal) && (
  <details className="group">
    <summary>… Opções avançadas</summary>
```

Logo: em complemento de loja sem fiscal não há nem *Opções avançadas*; em produto o bloco
aparece sempre, mas sem o campo dentro.

## Permissão

O campo é `readOnly={!podeEditar}` — a permissão **comum** de editar cardápio, e **não** a de
preço. Na edição em lote vale o mesmo, porque `vendaFiscalCheck` ficou fora de
`PRECO_FIELDS`:

```ts
const PRECO_FIELDS = new Set(['custoCheck', 'vendaCheck']);
…
// Demais campos seguem `editar`
return podeEditar;
```

Decisão de produto, e o commit diz isso no título: *"Valor fiscal na edição em lote (produtos
e complementos) e permissão de edição comum"*. Quem pode mexer no cardápio mexe no valor
fiscal, mesmo sem poder ver ou mudar preço.

## O campo na tela

```tsx
<Label>Valor fiscal</Label>
<Input
  value={formData.vendaFiscal ? formatCurrencyInput(formData.vendaFiscal) : ""}
  onChange={(e) => handleCurrencyChange("vendaFiscal", e.target.value)}
  className="text-right"
  placeholder="R$ 0,00"
  readOnly={!podeEditar}
/>
<p className="text-xs text-muted-foreground">Valor usado na emissão da nota fiscal, quando diferente do preço de venda. Deixe vazio para emitir pelo preço de venda.</p>
```

Caminho completo: **Cardápio → Produtos → (produto) → Editar → aba Produto → Opções
avançadas → Valor fiscal**. O `<details>` nasce **fechado**, e é por isso que a imagem 03 do
manual existe: sem abrir o bloco, o campo não aparece na tela.

No lote, o texto de apoio é outro e importa: *"Deixe vazio para **limpar** o valor fiscal dos
itens selecionados e emitir pelo preço de venda."* — marcar a caixa com o campo vazio é a
forma de apagar em massa.

## A API

| Operação | Chamada |
|---|---|
| Detalhes do produto (traz `vendaFiscal`) | `GET /api/produto2/cardapio/produto/{empresaID}/{usuarioID}/{produtoID}` |
| Gravar o produto | `POST /datasnap/rest/produto2/cardapio/produto` |
| Gravar vários | `POST /api/produto2/cardapio/editarLote` |

No lote, cada item do array vai com o par:

```ts
vendaFiscalCheck: config.vendaFiscalCheck,
vendaFiscal: config.vendaFiscalCheck ? normalizarVendaFiscal(config.vendaFiscal) : null,
```

**As listagens não devolvem o campo.** Conferido na sandbox: nem
`produto2/cardapio/produtos/{e}/{f}/{u}` nem `produto2/cardapio/produtosComp/{e}/{f}/{u}`
trazem `vendaFiscal`; só os detalhes. Por isso não existe coluna de valor fiscal na lista do
cardápio, e o manual não promete uma — para conferir, é abrir o produto.

## Como isto foi conferido no sandbox

A sandbox (empresa 38311, filial 39202) tem fiscal ativo, e o `GET` de detalhes já devolvia
`vendaFiscal: null` em todos os produtos antes de qualquer edição — o campo existe de ponta a
ponta em produção. O `capturar.py` desta pasta grava o exemplo pelos campos da própria tela,
fotografa, e o `python capturar.py limpar` devolve todo mundo para `null`.

O exemplo é um combo real da base:

| Item | ID | Preço de venda | Papel no combo |
|---|---|---|---|
| Combo Tasty Bacon — Burger + Batata + Bebida | 2698512 | R$ 60,00 | item pago |
| Batata Frita Especial One | 2698513 (complemento) | — | opção sem acréscimo do grupo *Escolha 1 acompanhamento* |
| Sprite 350ml | 2698520 (complemento) | — | opção do grupo *Escolha sua Bebida Gelada*, marcado **Brinde** |

O grupo da bebida vem com `agregaValor: false` e `statusTraduzido: "Brinde"` — é esse o
desenho em que os itens saíam de fora da nota, e que o campo novo resolve.

## O que ficou de fora do manual (e por quê)

- **Não emitimos NFC-e para provar a repartição.** A sandbox está em homologação
  (`nfceProd: false`) e com 0 emissões em 240 vendas; emitir nota é passo irreversível e, pela
  regra da casa, pede confirmação do dono. O manual mostra a conta como **exemplo
  ilustrativo**, no mesmo formato do #5 (reforma tributária), com aviso em negrito.
- **A fórmula exata do ajuste proporcional.** Ela está no servidor
  (`beetech-server-node-2.0`, que não está nesta máquina). O manual diz o que o dono publicou
  na novidade — *"ajusta os itens configurados proporcionalmente"* — e mostra o efeito com um
  exemplo redondo, sem inventar a fórmula.
