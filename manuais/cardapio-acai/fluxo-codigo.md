# Fluxo de código — Açaí: inclusos com limite e grupos compartilhados

> Mapeamento técnico do que o manual **#30 Cardápio — açaí** documenta.
> Fonte: `beefood-web-react`, somente leitura. Levantado em 20/08/2026, versão
> **v3.200826.1841** em produção.
> O cadastro básico está em `manuais/cardapio-fundamentos/fluxo-codigo.md`; as fórmulas de preço
> em `manuais/cardapio-pizza/fluxo-codigo.md`; o Brinde e o Obrigatório em
> `manuais/cardapio-hamburguer/fluxo-codigo.md`. Aqui só o que é específico deste manual.

---

## 1. Não existe "N primeiros grátis"

O grupo de opções tem **limite de quantidade** (`qtdMin` / `qtdMax`), não limite de valor. Não há
nenhum campo que signifique "cobre a partir do quarto item". Procurado em
`ModalEditarGrupoOpcao.tsx`, `useGrupoOpcaoDetalhes.ts` e no cálculo de
`ModalCombo.tsx` — não existe.

A regra comercial da açaiteria se traduz com **dois grupos**:

| Grupo | `formacaoPreco` | `qtdMax` | Efeito |
|-------|-----------------|----------|--------|
| Acompanhamentos inclusos | `brinde` | 3 | até 3 escolhas, nenhuma soma |
| Acompanhamentos extras | `normal` | 5 | cada escolha soma o valor da opção |

O que cria a sensação de "3 inclusos" é o **`qtdMax` do primeiro grupo**, que trava a quarta
seleção.

---

## 2. Como o limite trava a seleção

`ModalCombo.tsx`, na renderização de cada opção:

```jsx
<Checkbox
  checked={selected}
  disabled={!selected && !canSelectOption(grupo, opcao)}
  className="w-5 h-5 pointer-events-none"
/>
```

`canSelectOption` compara o total já selecionado no grupo com o `qtdMax` do grupo. Quando o
limite é atingido:

- as opções **não** selecionadas ficam com o checkbox `disabled`;
- as já selecionadas continuam clicáveis (para desmarcar);
- o contador ao lado do nome do grupo mostra **3/3** e ganha destaque verde.

Confirmado no sandbox: com Granola, Banana e Paçoca marcados, o checkbox de *Leite em pó*
retornou `unchecked (bloqueado)` — atributo `data-disabled` presente.

**Não há mensagem de erro** nesse caso: o controle simplesmente não responde. É diferente do
grupo **Obrigatório**, que emite toast ao tentar adicionar (ver manual do hambúrguer).

---

## 3. A lista pode ser maior que o limite

Nada impede um grupo com 20 opções e `qtdMax` 3. O limite é de **seleção**, não de cadastro. No
cenário deste manual o grupo dos inclusos tem **4 opções** e limite **3**.

---

## 4. Grupo compartilhado por vários produtos

Os três grupos deste manual foram vinculados aos **três tamanhos**. O que se observa:

| Onde | O que aparece |
|------|---------------|
| Modal do grupo | Faixa amarela *Alterações neste grupo refletem em todos os 3 produtos vinculados.* |
| Aba **Produtos** do grupo | Contador **Produtos (3)** e a lista dos três tamanhos, com lixeira para desvincular |
| Card do complemento | **Usado 1 vez: Acompanhamentos inclusos** — o rastro é por **grupo**, não por produto |

**Efeito de layout que atinge as capturas:** a faixa amarela empurra todo o conteúdo do modal
cerca de 0,07 (em fração da altura) para baixo. Num viewport de 900 px isso é suficiente para os
campos **Mínimo** e **Máximo** saírem da área visível. As coordenadas do `annotate.py` para a
imagem 06 são próprias por causa disso.

Endpoints de vínculo: `POST /api/produto2/cardapio/produto/grupo/vincular` e
`DELETE /api/produto2/cardapio/produto/grupo`.

---

## 5. Tamanho como produto vs tamanho como opção

Os dois funcionam. Comparação a partir do que o código faz:

| | Um produto por tamanho | Um produto + grupo "Tamanho" |
|---|---|---|
| Preço na listagem | cada card mostra o seu preço | todos mostram R$ 0,00 (ou "A partir de", se `valorMinimo` estiver preenchido) |
| Relatório por produto | separa as vendas por tamanho | agrupa tudo num produto |
| Cadastro | três produtos, mesmos grupos vinculados | um produto, um grupo a mais |
| Preço do acompanhamento por tamanho | dá para variar (clonando o grupo) | mesmo preço para todos os tamanhos |

O manual recomenda **um produto por tamanho**, principalmente pela referência de preço no
cardápio e pelo relatório.

> `VirtualizedProductGrid.tsx` mostra **A partir de …** quando o produto é combo e tem
> `valorMinimo` / `valorMinimoPresencial` preenchidos. É o que permite exibir um preço mínimo em
> produto de preço zero — sem alterar o cálculo.

---

## 6. Cenário conferido no PDV

Produto **Açaí 500 ml**, preço base **R$ 22,00**, três grupos vinculados.

| Passo | Total no botão |
|-------|----------------|
| Modal aberto | R$ 22,00 |
| Granola + Banana + Paçoca (grupo Brinde, 3/3) | **R$ 22,00** — não somou |
| Tentar o 4º incluso (*Leite em pó*) | checkbox **bloqueado** |
| + Creme de avelã R$ 6,00 e Morango R$ 3,00 (grupo Normal) | **R$ 31,00** |
| + Calda de chocolate R$ 2,00 (grupo Normal, máx 1) | **R$ 33,00** |
| Tentar a 2ª calda | checkbox **bloqueado** |

No carrinho, o item sai com as seis escolhas listadas — as de Brinde inclusive.

---

## 7. Endpoints

Os mesmos do manual de fundamentos. Nada específico deste manual. Ver
`manuais/cardapio-fundamentos/fluxo-codigo.md`, seção 7.
