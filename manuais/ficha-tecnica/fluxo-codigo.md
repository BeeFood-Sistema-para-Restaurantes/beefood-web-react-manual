# Fluxo de código — #72 Ficha Técnica

Mapeamento técnico feito em `~/refs/beefood-web-react` (somente leitura) e confirmado no sandbox
BeeFood3 em 31/08–01/09/2026. Documento interno: **não publicar**.

## 1. Onde a funcionalidade vive

Não existe rota dedicada. A Ficha Técnica é sempre uma **aba** do modal de produto/complemento.

| Caminho no painel | Rota | Componente |
|-------------------|------|------------|
| Cardápio → Produtos → editar | `/cardapio?tab=produtos` | `src/pages/Cardapio.tsx` → `ModalEditarProduto` |
| Cardápio → Complementos → editar | `/cardapio?tab=complementos` | mesmo modal, `isComplemento` |
| Estoque → Meu Estoque → Produtos/Complementos | `/meu-estoque` | `src/pages/MeuEstoque.tsx`, `visibleTabs={['estoque','ficha-tecnica']}` |
| Mobile | `/cardapio`, `/meu-estoque` | `MobileFichaTecnicaTab` — **somente leitura** |

Abas do modal (`src/hooks/useEditarProdutoLogic.ts`, `allTabs`): Produto, Cardápios, Estoque,
Restrições / Detalhes, Grupo de Opções, **Ficha Técnica**. A de Ficha Técnica não tem
`hideForComplemento`, por isso aparece também no complemento.

**Permissão:** não existe permissão própria. Depende do submenu **Cardápio** ou **Estoque**
(`ProtectedRoute`). A aba **Estoque** do modal depende de `canEstoque`; a Ficha Técnica não.

## 2. Arquivos principais

| Papel | Arquivo |
|-------|---------|
| Aba (desktop) | `src/components/ProdutoFichaTecnicaTab.tsx` |
| Aba (mobile, leitura) | `src/components/mobile/cardapio/MobileFichaTecnicaTab.tsx` |
| Modal pai | `src/components/ModalEditarProduto.tsx` |
| Listagem da ficha | `src/hooks/useFichaTecnica.ts` |
| CRUD do vínculo | `src/hooks/useProdutoInsumo.ts` |
| Cache de insumos | `src/hooks/useInsumosCacheados.ts` |
| Cadastro de insumo | `src/components/estoque/ModalEditarInsumo.tsx` |
| Saldo manual | `src/hooks/useAlterarEstoque.ts` |
| Exclusão de insumo | `src/components/estoque/EstoqueInsumosTab.tsx` |
| Movimentações | `src/pages/Movimentacoes.tsx` |

## 3. Endpoints

| Operação | Método | Path |
|----------|--------|------|
| Listar a ficha de um produto | GET | `/api/estoque2/produtoInsumos/{empresaID}/{usuarioID}/{produtoID}` |
| Incluir / editar linha | POST | `/api/estoque2/insumoProduto` |
| Excluir linha | DELETE | `/api/estoque2/insumoProduto/{empresaID}/{usuarioID}/{produtoID}/{id}` |
| Produtos que usam um insumo | GET | `/api/estoque2/insumosProduto/{empresaID}/{usuarioID}/{insumoID}` |
| Listar insumos | GET | `/api/estoque2/insumos/{empresaID}/{usuarioID}` |
| Salvar insumo | POST | `/api/estoque2/insumo` |
| Excluir insumo | DELETE | `/api/estoque2/insumo/{empresaID}/{usuarioID}/{insumoID}` |
| Saldo manual (entrada/saída) | POST | `/api/estoque2/saldo` |
| Movimentações | GET | `/api/estoque2/movimentacoes/{empresaID}/{usuarioID}?dataInicio=…&dataFim=…` |
| Receitas | GET/POST/DELETE | `/api/estoque2/receita(s)/…` |

O produto traz o custo da ficha no campo **`custoComposicao`**, mapeado para
`formData.custoFichaTecnica` em `useProdutoDetalhes`.

## 4. Contas

Em `ProdutoFichaTecnicaTab.tsx`:

```
custoUnitario = item.custo ?? custo do insumo no cache
custoLinha    = item.qtd * custoUnitario
custoTotal    = Σ custoLinha
percentual    = (custoLinha / custoTotal) * 100
```

Em `ModalEditarProduto.tsx` (bloco inline por volta da linha 728):

```
custoTotal = formData.custo + formData.custoFichaTecnica
lucro      = valorProduto - custoTotal
margem     = lucro / valorProduto * 100     (0 quando valorProduto = 0)
```

A etiqueta só aparece se `custoTotal > 0`. Não há markup, preço sugerido, perda nem rendimento.

## 5. Validações e mensagens

| Situação | Mensagem |
|----------|----------|
| Produto ainda não salvo | *Salve o produto primeiro / A ficha técnica estará disponível após salvar o produto* |
| Insumo repetido | *Este insumo já foi adicionado à ficha técnica* |
| Quantidade vazia, zero ou inválida | *Informe uma quantidade válida* |
| Falha na API | *Erro ao adicionar insumo* / *Erro ao remover insumo* / *Erro ao atualizar quantidade* |
| Remoção | diálogo **Remover Insumo** → *Sim, remover* / *Não* |
| Exclusão de insumo em uso | HTTP 409 com `{resultado:false, emUso:true, mensagem, detalhes:{produtos, receitas, movimentacoes}}` |

Máscara da quantidade (`handleQuantidadeChange`): só dígitos, vírgula e ponto; ponto vira vírgula;
**máximo 4 casas decimais**.

## 6. Descobertas comprovadas no sandbox

Vendas de teste #925, #927 e #928 (31/08/2026), com as fichas deste manual.

1. **A baixa acontece no `Receber` (criação da pré-venda), antes do pagamento.** A venda #925 já
   tinha todas as movimentações antes de qualquer forma de pagamento ser escolhida.
2. **A ficha do complemento é baixada quando ele é escolhido como opção**, com trilha de três
   níveis no campo `origem`: `One Burger -> Carne 100g -> Blend bovino`. A ficha do produto usa
   dois níveis: `One Burger -> Pão brioche`.
3. **A opção escolhida duas vezes baixa duas vezes.** Com `qtdMax = 2` na opção *Carne 100g*, o
   pedido com 2 unidades gerou `-0,2` de blend (`origemQtd = 2`), somando `-0,3` com a linha do
   produto. **Isso libera o modelo Proporcional da pizza** (ficha do sabor em meia pizza), que
   estava em aberto no `PLANO-FICHA-TECNICA.md`.
4. **Insumo com `Controlar Estoque` desligado não gera movimentação.** A *Maionese da casa
   (sache)* está na ficha e entra no custo, mas não apareceu em Movimentações. O consumo dela
   simplesmente não é registrado.
5. **A quantidade do item multiplica**: duas linhas de Batata frita geraram dois conjuntos de
   baixas (`-0,2` batata, `-0,01` óleo, `-1` embalagem em cada).
6. **Estorno existe**: alterar/cancelar venda gera movimentação positiva do mesmo insumo
   (observado no histórico da conta, vendas #189 e #218).
7. **Insumo em uso por receita não pode ser excluído**, mesmo com a receita **inativa**. O 409
   continua vindo depois do soft delete da receita. Para liberar, é preciso trocar os itens da
   receita — e a API **recusa** `itens: []` (*"itens é obrigatório"*).
8. O produto com ficha passa a devolver `custo` e `insumos[]` na listagem de
   `/api/estoque2/produtos`, o que alimenta a coluna **Ficha Técnica = Sim/Não**.

## 7. Armadilhas do sandbox (para quem for recapturar)

- A base tem **produtos com nome repetido** (dois *One Burger*, duas *Batata frita*). O que tem
  grupos de opções e ficha é o `produtoID` **2515371** (One Burger) e **2515323** (Batata frita).
  O `capturar.py` resolve isso abrindo um por um até achar um `marcador` de texto.
- No PDV, o card do produto com grupos tem o selo **COMBO**; o duplicado sem grupos entra direto
  no carrinho, sem abrir o modal de opções.
- Preço no PDV (R$ 14,00) é diferente do **Preço de Venda** do cadastro (R$ 28,00): há um
  **Preço Programado** ativo (*Preço 24/08 13:35*, presencial, todos os dias) na conta.
- No modal do insumo, **trocar de aba já salva** o cadastro.
- O campo **Estoque Mínimo** é `input[type=number]`: precisa de ponto (`0.5`), não vírgula.
- Na linha em edição da ficha, **Esc fecha o modal inteiro** — quem cancela a edição é o ✗ da
  própria linha.
- Depois de **Adicionar**, o campo de busca reabre sozinho e tapa a tabela: mandar `Escape` antes
  do print.

## 8. IDs do cenário (sandbox BeeFood3)

`empresaID 38311` · `filialID 39202` · `usuarioID 88711`

| Item | ID |
|------|----|
| Produto One Burger (com grupos) | 2515371 |
| Produto Batata frita (com ficha) | 2515323 |
| Complemento Carne 100g | 2515336 |
| Complemento Bacon | 2515329 |
| Complemento Fatia de queijo | 2515342 |
| Grupo Adicionais do One Burger | 257195 (mín 0 / máx 2; opções com `qtdMax` 2) |
