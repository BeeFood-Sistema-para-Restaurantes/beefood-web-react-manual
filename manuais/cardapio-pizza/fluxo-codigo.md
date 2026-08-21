# Fluxo de código — Pizza: Valor da Maior e Proporcional

> Mapeamento técnico do que o manual **#29 Cardápio — pizza** documenta.
> Fonte: `beefood-web-react` (front) e `beetech-server-node-2.0` (backend), somente leitura.
> Levantado em 20/08/2026, versão **v3.200826.1647** em produção.
> O cadastro em si (complementos, grupos, produto, vínculo) está em
> `manuais/cardapio-fundamentos/fluxo-codigo.md`. Aqui só o que é específico de pizza.

---

## 1. Não existe tela de pizza

O BeeFood **não tem** um cadastro dedicado a pizza. Sabor é opção dentro de um grupo, e
"meio a meio" é consequência de três coisas combinadas:

| Peça | Onde se define |
|------|----------------|
| Quantas frações a pizza tem | **Mínimo** e **Máximo** do grupo |
| Se o cliente pode repetir o mesmo sabor | **Máximo da opção** (dentro da linha da opção) |
| Como o preço dos sabores entra na conta | **Formação de Preço** do grupo |

Não há campo de "tamanho" nem de "fração". O que existe é quantidade de opções.

> O grupo tem os campos `pizza: boolean` e `proporcionalTipo: string | null` vindos da view
> SQL `funSelect_ViewAppProdutoGrupo`, mas **nenhum dos dois é usado** — não há controle na UI
> de cadastro e nenhuma referência no cálculo, nem no front nem no Node. São legado.

---

## 2. O cálculo, no front (o que o operador vê)

`src/components/ModalCombo.tsx`, `useMemo` **`calcularValorTotal`** (linhas ~854 a 921). É o
valor do botão **Adicionar ao carrinho**.

```
total = (preço base do produto + Σ valor de cada grupo) × quantidade do item
```

O preço base vem de `getProdutoPreco` (`src/pages/PDV.tsx`), na ordem
`vendaPromocao` → `vendaPresencial` → `venda`.

Por grupo:

| Formação | O que o front faz |
|----------|-------------------|
| **Normal** | `valorOpcoes += valorOpcao × quantidade` |
| **Brinde** | as opções não têm preço, então não somam |
| **Valor da Maior** | empilha os valores e soma **só** `Math.max(...)` |
| **Proporcional** | **cai no mesmo `else` do Normal** — soma `valorOpcao × quantidade` |

**Não existe ramo de Proporcional no cálculo do front.** É o achado que define este manual: o
`proporcional` **não divide nada** na tela de venda.

Ao confirmar (`adicionarAoCarrinho`, linhas ~1112 a 1134), para `valorDaMaior` o front zera o
`valor` das opções que não são a mais cara antes de mandar para o carrinho. Para
`proporcional` **não há ajuste equivalente**.

---

## 3. O cálculo, no backend

`beetech-server-node-2.0/src/models/pedido/pedidoPOST.js`, `processaGrupoOpcao`
(linhas ~759 a 813).

**Valor da Maior:** acha o maior `valor` do grupo, atribui a **uma** linha e zera (`null`) as
outras. Mesmo resultado do front.

**Proporcional:**

```js
gruposx.forEach(item => {
  if (item.produtoGrupoID == grupox.produtoGrupoID){
    vendaGrupoLocal += !!item.valor ? item.valor : 0.00;
    qtdGrupoLocal += 1
  }
});
objx.venda = parseFloat((vendaGrupoLocal / qtdGrupoLocal).toFixed(2))
```

Ou seja: o servidor grava em **cada linha** a **média** das opções do grupo. Depois,
`processaGruposValorTotal` faz `vendax += obj.venda * obj.qtd`.

Com N linhas de quantidade 1, o total é `média × N = soma`. **O total é o mesmo do front;
a média é o rateio por sabor, não um desconto.**

É para isso que serve o Proporcional: cada metade contabiliza o mesmo valor nos relatórios por
produto, mesmo quando os sabores têm preços diferentes.

### Arredondamento

`parseFloat((S / N).toFixed(2))`. Com 3 opções de R$ 40, R$ 45 e R$ 48, a média é
`round(133/3, 2) = 44,33` e o total no servidor fica **R$ 132,99**, enquanto o botão do modal
mostra R$ 133,00 — **1 centavo de diferença** quando N ≥ 3 e a divisão não é exata. Com 2
frações (o caso da pizza meio a meio) a divisão é sempre exata em centavos e não há
divergência.

---

## 4. Comprovação na prática

Executado no sandbox em 20/08/2026, lendo o valor do botão **Adicionar ao carrinho**.

### Produto com preço base R$ 0,00, sabores com preço INTEIRO

| Grupo | Seleção | Botão |
|-------|---------|-------|
| Valor da Maior (mín 1 / máx 2) | Calabresa R$ 40 | **R$ 40,00** |
| Valor da Maior | Calabresa + Portuguesa R$ 45 | **R$ 45,00** |
| Proporcional (mín 1 / máx 2) | Calabresa R$ 40 | **R$ 40,00** |
| Proporcional | Calabresa + Portuguesa R$ 45 | **R$ 85,00** |

O R$ 85,00 é a armadilha: quem escolhe Proporcional esperando média cobra o dobro.

### Produto com preço base R$ 0,00, sabores com preço de MEIA pizza

Grupo Proporcional, mín 2 / máx 2, cada opção com máximo 2. Valores: Calabresa R$ 20,00 e
Portuguesa R$ 22,50 (metade de R$ 40,00 e R$ 45,00).

| Seleção | Botão | Equivale a |
|---------|-------|-----------|
| Calabresa 1× | R$ 20,00 | meia pizza (pedido incompleto: o grupo exige 2) |
| **Calabresa 2×** | **R$ 40,00** | pizza inteira de calabresa |
| **Calabresa + Portuguesa** | **R$ 42,50** | meio a meio = média de R$ 40 e R$ 45 |
| Calabresa 3× | R$ 40,00 | bloqueado pelo máximo do grupo |
| Meio a meio + Borda Catupiry R$ 8,00 | **R$ 50,50** | a borda soma por cima |

---

## 5. Seleção única vs contador de quantidade

`ModalCombo.tsx`, linhas ~1489 a 1526:

| Condição | O que o PDV mostra |
|----------|--------------------|
| `opcao.qtdMax === 1` | caixa de seleção |
| `opcao.qtdMax > 1` | contador `− n +` |

**É o máximo DA OPÇÃO que decide**, não o do grupo. Por isso o modelo Proporcional precisa da
opção com máximo 2: sem isso não existe pizza inteira de um sabor só.

### O botão "+" do contador está desabilitado no código

```jsx
<Button
  size="sm"
  variant="outline"
  className="w-7 h-7 p-0 pointer-events-none opacity-50"
  disabled
>
  <Plus size={12} />
</Button>
```

O "+" é **decorativo**: `disabled` fixo e `pointer-events-none`. Quem aumenta a quantidade é o
**clique na própria linha** da opção (`increaseOption`); o "−" (`decreaseOption`) funciona
normalmente. Confirmado na prática: clicar duas vezes na linha da Calabresa levou o total de
R$ 20,00 para R$ 40,00.

Vale reportar ao time — é confuso ver um "+" que não clica.

---

## 6. O aviso do Valor da Maior

`ModalCombo.tsx`, linhas ~1316 a 1325. Faixa azul acima da lista de opções, texto exato:

> **Regra especial: Será cobrado apenas o valor da opção mais cara selecionada**

**Não há aviso equivalente para Proporcional** — nem faixa, nem tooltip. No cadastro, o único
sinal é o selo **Proporcional** no card do grupo (`CardapioGrupoOpcoesTab.tsx`).

---

## 7. Aviso de grupo compartilhado

Quando o grupo está vinculado a mais de um produto, o modal do grupo abre com uma faixa
amarela:

> Alterações neste grupo refletem em todos os **N** produtos vinculados.

Aparece no grupo **Borda** do cenário deste manual, que serve às duas pizzas.

---

## 8. Formação de Preço → API

`src/hooks/useGrupoOpcaoDetalhes.ts`, `formacaoPrecoToApi`:

| Rótulo na tela | `formacaoPreco` | `agregaValor` | `valorDaMaior` | `proporcional` |
|----------------|-----------------|---------------|----------------|----------------|
| Normal | `normal` | `true` | `false` | `false` |
| Brinde | `brinde` | `false` | `false` | `false` |
| Valor da Maior | `maior` | `true` | `true` | `false` |
| Proporcional | `proporcional` | `true` | `false` | `true` |

Textos de ajuda que a tela já mostra:

- **Valor da Maior** — *O preço é formado pelo maior valor selecionado (Recomendado para Porções)*
- **Proporcional** — *O preço é formado proporcionalmente pelas opções selecionadas (Recomendado para Pizzas)*

A recomendação "para Pizzas" **só se cumpre** se as opções tiverem o preço da fração. Com o
preço inteiro, o Proporcional se comporta como Normal.

---

## 9. Endpoints

Os mesmos do manual de fundamentos — nenhum endpoint é específico de pizza. Ver
`manuais/cardapio-fundamentos/fluxo-codigo.md`, seção 7.

---

## 10. Encoding: travessão vira "?"

O nome `Pizza Média — Proporcional`, salvo com travessão (em dash, U+2014), volta da API e
aparece na tela como `Pizza Média ? Proporcional` — no card do PDV, no cardápio e no modal de
busca de opções. Parênteses e acentos comuns funcionam.

Provável coluna `varchar` (não `nvarchar`) no SQL Server. Para o manual, os produtos foram
renomeados para `Pizza Média (Proporcional)` e `Pizza Média (Valor da Maior)`.

**Evitar travessão, en dash e outros caracteres fora do Latin-1 em nome de produto.**
