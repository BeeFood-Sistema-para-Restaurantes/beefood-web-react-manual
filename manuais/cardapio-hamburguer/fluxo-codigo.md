# Fluxo de código — Hambúrguer: Brinde e grupo obrigatório

> Mapeamento técnico do que o manual **#28 Cardápio — hambúrguer** documenta.
> Fonte: `beefood-web-react`, somente leitura. Levantado em 20/08/2026, versão
> **v3.200826.1841** em produção.
> O cadastro básico está em `manuais/cardapio-fundamentos/fluxo-codigo.md`; as fórmulas de
> preço, em `manuais/cardapio-pizza/fluxo-codigo.md`. Aqui só o que é específico deste manual:
> a formação **Brinde** e o checkbox **Obrigatório**.

---

## 1. Brinde

`src/hooks/useGrupoOpcaoDetalhes.ts`, `formacaoPrecoToApi`:

| Rótulo na tela | `formacaoPreco` | `agregaValor` | `valorDaMaior` | `proporcional` |
|----------------|-----------------|---------------|----------------|----------------|
| **Brinde** | `brinde` | **`false`** | `false` | `false` |

É o único modo em que `agregaValor` vai como `false`. Texto de ajuda na tela:
*Todas opções ficam sem preço*.

### Como o preço fica zero

Não é o `agregaValor` que zera o valor na tela de venda. No PDV
(`ModalCombo.tsx`, `calcularValorTotal`) o cálculo por opção é:

```js
const valorRaw = isDelivery ? opcao.vendaDelivery : opcao.vendaPresencial;
if (valorRaw !== null && valorRaw !== undefined && valorRaw > 0) {
  valorOpcao = valorRaw;
} else if (opcao.valor !== null && opcao.valor !== undefined && opcao.valor > 0) {
  valorOpcao = opcao.valor;
}
```

Ou seja: o total soma o **valor da opção**, e num grupo Brinde esse valor é zero. O efeito
prático é o mesmo, mas a consequência importa: **se você marcar Brinde e a opção tiver preço
cadastrado, o preço continua somando na tela de venda.** O `brinde` é a intenção declarada; o
que garante o zero é o valor da opção estar em R$ 0,00.

Confirmado no sandbox: as opções dos dois grupos Brinde (`Ponto da carne` e
`Retirar ingredientes`) ficaram com **R$ 0,00** ao serem incluídas, porque os complementos de
origem foram cadastrados sem preço.

### O que o PDV mostra

Opção de grupo Brinde aparece **sem** a linha `+R$ x,xx` embaixo do nome — o campo só é
renderizado quando há valor. Não há faixa de aviso como a do **Valor da Maior**.

---

## 2. Obrigatório

Campo `obrigatorio` do grupo, checkbox **Obrigatório** na aba Detalhes do Grupo. Texto auxiliar
que acompanha:

> O cliente deve selecionar **{qtdMin}** ou mais opção para adicionar o pedido ao carrinho

Ao salvar, se **Obrigatório** está marcado e o Mínimo é 0, o hook força **Mínimo = 1**.

### O que ele faz na venda — testado

| Situação | Comportamento |
|----------|---------------|
| Grupo obrigatório sem seleção | O selo **Obrigatório** aparece em **vermelho** ao lado do nome do grupo |
| Botão **Adicionar ao carrinho** | **Continua habilitado** (não fica cinza) |
| Clicar em Adicionar sem escolher | Toast vermelho **Seleção obrigatória** / *Por favor, selecione as opções do grupo "Ponto da carne".* e o modal **permanece aberto** |
| Depois de escolher | O selo vermelho é substituído por um **ícone verde de check** |

Isso é diferente do que se poderia supor: a validação é **no clique**, não por desabilitar o
botão. O manual mostra as duas telas (selo vermelho e selo verde) e o aviso.

---

## 3. Ordem dos grupos no produto

`src/components/ProdutoGrupoOpcoesTab.tsx`. Cada linha tem setas ↑↓ (`chevron-up` /
`chevron-down`) e arrasto; a coluna **# Descrição** mostra o número de ordem.

Endpoint: `POST /api/produto2/cardapio/produto/grupo/ordem`.

**Detalhe observado:** ao vincular vários grupos de uma vez, todos entram com ordem `1` e a
listagem sai em ordem alfabética (*Adicionais*, *Ponto da carne*, *Retirar ingredientes*).
Depois de usar a seta uma vez, os números passam a `1`, `2`, `3` e a ordem vale para o PDV.

Para o cliente, a ordem que faz sentido é a da pergunta do atendente: **ponto da carne** antes
dos **adicionais**.

---

## 4. Grupo compartilhado entre produtos

Os grupos **Adicionais** e **Retirar ingredientes** foram vinculados ao **X-Burger** e ao
**X-Salada**. Efeitos confirmados:

| Onde | O que aparece |
|------|---------------|
| Card do complemento (aba Complementos) | **Usado 1 vez: Adicionais** — o rastro de uso é por **grupo**, não por produto |
| Modal do grupo, quando tem 2+ produtos | Faixa amarela *Alterações neste grupo refletem em todos os N produtos vinculados.* |
| Aba **Produtos** do grupo | Lista os produtos que usam o grupo |

---

## 5. Complemento sem foto

O upload de imagem é opcional. Complemento sem foto aparece com um ícone de imagem riscada
(`ImageOff`) na listagem e no PDV. Foi o caso escolhido para os itens de **retirada** (*Sem
cebola*, *Sem tomate*, *Sem alface*): não existe imagem que faça sentido para eles, e a
listagem mostra bem a diferença ao lado dos complementos que têm foto.

---

## 6. Cenário conferido no PDV

Produto **X-Burger**, preço base **R$ 28,00**, com três grupos.

| Passo | Total no botão |
|-------|----------------|
| Modal aberto, nada escolhido | R$ 28,00 |
| **Ao ponto** (grupo Brinde, obrigatório) | **R$ 28,00** — não somou |
| **+ Bacon** R$ 3,00 e **+ Cheddar** R$ 2,00 (grupo Normal) | **R$ 33,00** |
| **+ Sem cebola** (grupo Brinde) | **R$ 33,00** — não somou |

No carrinho, o item sai como `X-Burger — R$ 33,00` com as quatro escolhas listadas
(`1x Ao ponto`, `1x Bacon`, `1x Cheddar`, `1x Sem cebola`). **As opções de Brinde aparecem no
pedido** — elas vão para a cozinha —, apenas não entram na conta.

---

## 7. Endpoints

Os mesmos do manual de fundamentos. Nada específico deste manual. Ver
`manuais/cardapio-fundamentos/fluxo-codigo.md`, seção 7.
