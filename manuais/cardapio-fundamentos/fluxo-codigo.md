# Fluxo de código — Cardápio: produtos, grupos de opções e complementos

> Mapeamento técnico do que o manual **#27 Cardápio — fundamentos** documenta.
> Fonte: `beefood-web-react` (front) e `beetech-server-node-2.0` (backend), somente leitura.
> Levantado em 20/08/2026 na versão **v3.200826.1358** em produção.

---

## 1. Rota e abas

| Item | Valor |
|------|-------|
| Página | `src/pages/Cardapio.tsx` |
| Rota | `path="cardapio"` (`src/App.tsx`) → `https://beefood.app/cardapio` |
| Query param | `?tab=produtos` \| `grupoOpcoes` \| `complementos` |
| Aba padrão | `produtos` |

**Detalhe que importa para capturar telas:** a página lê `searchParams.get('tab')` na
montagem, mas o clique nas abas usa `useState` local (`handleTabChange`) e **não atualiza a
URL**. Ou seja: dá para entrar direto em `?tab=complementos`, mas depois de clicar numa aba a
URL fica velha.

### Rótulos exatos das abas

1. **Produtos**
2. **Grupo de Opções** — tem duas sub-abas: **Grupos** e **Opções**
3. **Complementos**

O menu lateral repete os três itens e acrescenta **Copiar do iFood**, **Copiar de Imagem**,
**Exibir / Ocultar** e **Rodízio** (fora do escopo deste manual).

### Botão primário do header (muda por aba)

| Aba | Rótulo |
|-----|--------|
| Produtos | **Novo Produto (F1)** |
| Grupo de Opções | **Novo Grupo (F1)** |
| Complementos | **Novo Complemento (F1)** |

> **Bug conhecido:** o listener de **F1** em `Cardapio.tsx` chama sempre
> `handleNovoProduto()`. Na aba Grupo de Opções, a tecla F1 abre o modal de **produto**,
> enquanto o botão abre o de **grupo**. O manual manda clicar no botão, não usar F1.

---

## 2. Complementos

| Item | Arquivo |
|------|---------|
| Aba | `src/components/cardapio/CardapioComplementosTab.tsx` |
| Hook | `src/hooks/useComplementosCardapio.ts` |
| Modal | `src/components/ModalEditarProduto.tsx` com `isComplemento={true}` |

A listagem é **grid de cards** (não tabela): foto, nome, preço, ícones de status e o texto
**Sem uso** / **Usado N vez(es)**.

### Abas do modal quando é complemento

`allTabs` em `src/hooks/useEditarProdutoLogic.ts` monta:

| Aba | Aparece? |
|-----|----------|
| **Complemento** | sempre (é a aba `produto` renomeada) |
| **Cardápios** | só em complemento **novo** |
| **Estoque** | se o usuário tem permissão de estoque |
| **Ficha Técnica** | sempre |
| Restrições / Detalhes | **oculta** |
| Grupo de Opções | **oculta** |

### Campos da aba Complemento

| Rótulo | Tipo | Obrigatório | Default |
|--------|------|-------------|---------|
| **ADICIONAR FOTO** | upload + crop | não | vazio |
| **Nome** | texto (`input#nome`) | **sim** | `""` |
| **Etiqueta** | select | não | Nenhuma Etiqueta |
| **Preço de Venda** | moeda | não | R$ 0,00 |
| **Código** / **Código de Barras** | texto | não | `""` |
| **Unidade** | select | não | UN - Unidade |
| **Custo** | moeda | não | R$ 0,00 |
| **Custo Ficha Técnica** / **Custo Total** | moeda | somente leitura | R$ 0,00 |
| **Descrição** | textarea + botão de IA | não | `""` |

O complemento **não** tem Setor, Destaque, Opções avançadas nem KDS — esses são só do produto.

> **Preço de Venda fica somente leitura** quando o complemento já participa das opções de
> algum grupo. Nesse caso o preço muda pela aba **Opções** ou pelo **Editar em Lote**.

---

## 3. Grupo de Opções

| Item | Arquivo |
|------|---------|
| Sub-aba Grupos | `src/components/cardapio/CardapioGrupoOpcoesTab.tsx` |
| Sub-aba Opções | `src/components/cardapio/CardapioOpcoesListTab.tsx` |
| Modal | `src/components/ModalEditarGrupoOpcao.tsx` |
| Aba Opções do modal | `src/components/GrupoOpcaoOpcoesTab.tsx` |

### Abas do modal

```
{ id: 'detalhes',  label: 'Detalhes do Grupo' }
{ id: 'opcoes',    label: 'Opções' }
{ id: 'produtos',  label: 'Produtos' }
```

Ganham contador quando têm conteúdo: **Opções (3)**, **Produtos (1)**.

### Campos de Detalhes do Grupo

| Rótulo | Tipo | Default |
|--------|------|---------|
| **Nome do Grupo de Opção** | texto (`input#descricao`) | `""` — obrigatório na prática |
| **Ativo** / **Delivery** / **Presencial** | switch | todos ligados |
| **Obrigatório** | checkbox | desmarcado |
| **Formação de Preço** | radio (4 opções) | **Normal** |
| **Quantidade → Mínimo** | número | **0** |
| **Quantidade → Máximo** | número | **1** |

Se **Obrigatório** é marcado com Mínimo 0, o save força Mínimo = 1.

### Formação de Preço — os quatro modos

Textos de ajuda exatamente como aparecem na tela:

| Rótulo | Valor interno | Texto de ajuda |
|--------|---------------|----------------|
| **Normal** | `normal` | O preço é formado pela soma das opções selecionadas |
| **Brinde** | `brinde` | Todas opções ficam sem preço |
| **Valor da Maior** | `maior` | O preço é formado pelo maior valor selecionado *(Recomendado para Porções)* |
| **Proporcional** | `proporcional` | O preço é formado proporcionalmente pelas opções selecionadas *(Recomendado para Pizzas)* |

Tradução para os campos da API (`src/hooks/useGrupoOpcaoDetalhes.ts`):

| Modo | `agregaValor` | `valorDaMaior` | `proporcional` |
|------|---------------|----------------|----------------|
| Normal | `true` | `false` | `false` |
| Brinde | `false` | `false` | `false` |
| Valor da Maior | — | `true` | `false` |
| Proporcional | — | `false` | `true` |

O cálculo final da venda roda no backend, em
`beetech-server-node-2.0/src/models/pedido/pedidoPOST.js` (`processaGrupoOpcao`).

### Aba Opções (dentro do modal do grupo)

Três formas de incluir opção:

| Botão | O que faz |
|-------|-----------|
| **BUSCAR E CADASTRAR** | Abre **Buscar e Cadastrar Opções** (`ModalSelecionarProdutosBusca`): busca, multiseleção, **Selecionar todos**, confirma em **Adicionar** |
| **CADASTRAR NOVA OPÇÃO** | Cria uma linha em branco com o autocomplete `SearchBoxOpcaoProduto` |
| **COPIAR DE OUTRO** | `ModalCopiarOpcoesDeOutroGrupo` — copia as opções de outro grupo |

A busca devolve **produtos e complementos** juntos (campo `tipo` da API). Digitar um nome que
não existe oferece *Criar nova* — nasce como produto novo, com `produtoID` nulo.

Atalhos de configuração no topo (**Como o cliente poderá selecionar as opções:**):

| Botão | Grupo | Cada opção |
|-------|-------|------------|
| **Pode selecionar apenas uma opção** | mín 1 / máx 1 | mín 1 / máx 1 |
| **Pode selecionar várias opções sem repetir** | mín 1 / máx 10 | mín 1 / máx 1 |
| **Poderá selecionar várias opções e repetir** | mín 1 / máx 10 | mín 1 / máx 10 |

Filtro da aba: campo **Filtrar Texto** (filtra `tipoDescricao`, `descricao` e `tipoStr`).

**A opção não tem foto própria** — a imagem vem do produto ou complemento vinculado
(`s3Link`). É por isso que o manual cadastra a foto no complemento: ela reaparece na opção,
no PDV e no cardápio digital de graça.

**Não existe edição em lote aqui.** Dentro do modal do grupo a edição é linha por linha:
clicar na linha expande e libera **Valor**, **V. Delivery**, **V. Presencial**, **Ativo**,
**Delivery**, **Presencial**, **Mínimo** e **Máximo**. Salva na própria linha (**SALVAR**) ou
no **SALVAR E SAIR (F2)** do modal, que grava todas as linhas modificadas.

### Aba Produtos (dentro do modal do grupo)

Visão inversa: lista os produtos que usam o grupo, com **BUSCAR PRODUTO E VINCULAR** e
remoção por lixeira. Não cria produto.

---

## 4. Sub-aba Opções e a edição em lote

É a tela central da Parte 8 do manual: `Cardápio → Grupo de Opções → Opções`.

| Item | Arquivo |
|------|---------|
| Listagem | `src/components/cardapio/CardapioOpcoesListTab.tsx` |
| Modal do lote | `src/components/cardapio/ModalEditarLoteOpcao.tsx` |
| Hook | `src/hooks/useEditarLoteOpcao.ts` |

Título em tela: **Todas as Opções**, com o total ao lado (**3 itens**).

### Colunas

`Descrição` · `Grupo` · `Tipo` · `Valor` · `Venda Del.` · `Venda Pres.` · `Qtd Min` ·
`Qtd Max` · `Status` · `Canais`

Cada uma tem ícone de **ordenação**; `Descrição`, `Grupo`, `Tipo` e `Status` têm também
**funil de filtro**, que abre um popover **Filtrar Descrição** com o campo *Digite para
filtrar...* e o link **Limpar**. Com filtro ativo, o header mostra **Limpar N filtro**.

Acima da tabela: **Todos / Ativos / Inativos** e o botão **Editar em Lote**
(permissão `editarLote`).

### As três etapas do lote

Título do modal: **Editar Opções em Lote**, com **Etapa N de 3**.

**Etapa 1 — seleção.** Campo *Buscar por nome...*, contador *N de N opções selecionadas*,
link **Marcar Todas** / **Desmarcar Todas**. Todas já vêm marcadas. Segue em **PRÓXIMO**.

**Etapa 2 — configuração.** *Marque os campos que deseja editar e configure os valores:*

| Campo | Sub-opções quando marcado |
|-------|---------------------------|
| **Preço de Venda** | qual preço (**Venda** / **Delivery** / **Presencial**) · tipo (**Novo Valor** / **Adicionar** / **Subtrair**) · unidade (**Valor (R$)** / **Porcentagem (%)**) · quanto |
| **Ativo** / **Ativo Delivery** / **Ativo Presencial** | Sim / Não |
| **Qtd Mínima** / **Qtd Máxima** | número |
| **Excluir Opções** | irreversível |

Confirma em **PROCESSAR (F2)**.

**Etapa 3 — resultado.** Barra de progresso, **Concluído**, contagem *N de N opções*,
resumo **N sucesso** e uma linha por opção com *Atualizado com sucesso*. Sai em
**FECHAR (ESC)**.

O hook processa em **lotes de 5** itens por requisição.

---

## 5. Produtos

| Item | Arquivo |
|------|---------|
| Aba | `src/components/cardapio/CardapioProdutosTab.tsx` |
| Grid | `src/components/cardapio/VirtualizedProductGrid.tsx` |
| Modal | `src/components/ModalEditarProduto.tsx` |
| Lógica | `src/hooks/useEditarProdutoLogic.ts` |
| Aba Grupo de Opções | `src/components/ProdutoGrupoOpcoesTab.tsx` |
| Vincular grupo | `src/components/ModalBuscarGrupoVincular.tsx` |
| Setor | `src/components/ModalEditarSetor.tsx` |

### Abas do modal de produto

**Produto** · **Cardápios** · **Estoque** *(se tem permissão)* · **Restrições / Detalhes** ·
**Grupo de Opções** · **Ficha Técnica**

O manual cobre **Produto** e **Grupo de Opções**; as demais ficam para manuais futuros.

### Campos usados no manual (aba Produto)

| Rótulo | Tipo | Obrigatório |
|--------|------|-------------|
| **ADICIONAR FOTO** | upload + crop | não |
| **Nome** | texto (`input#nome`) | **sim** |
| **Setor** | combobox com busca | não (default **Sem setor**) |
| **Preço de Venda** | moeda | não |
| **Descrição** | textarea | não |

### Setor

Não tem rota própria: é o modal **ModalEditarSetor**, aberto pelo botão **Novo Setor** na
barra lateral da aba Produtos. Campos: **Nome Interno do Setor** (obrigatório), **Ordem de
Exibição**, **Nome Público**, os switches **Delivery/Retirada** e **Presencial**, e
**Cardápios**.

> Não confundir com **Setor de produção**, que é da seção KDS dentro do produto.

### Aba Grupo de Opções do produto

Empty state: *Cadastre Grupo de Opções para compor a seleção do seu produto.* com
**BUSCAR GRUPO E VINCULAR** e **CADASTRAR NOVO GRUPO DE OPÇÕES**.

Depois de vincular, a linha mostra os switches **Ativo** / **Delivery** / **Presencial**,
setas de ordem, **# Descrição**, **Qtd. Mín.**, **Qtd. Máx.**, **Tipo** (a formação de preço
traduzida) e a lixeira.

O modal **Buscar e Vincular Grupo de Opções** lista os grupos com o resumo *0 a 3 opções* e o
selo da formação (**Agrega Valor**, **Proporcional**), com **Selecionar todos** e
**Vincular**.

---

## 6. Foto (produto, complemento e setor)

| Item | Valor |
|------|-------|
| Componentes | `ModalImagemEditor` → `ImageCropEditor` |
| Título do modal | **Foto do Produto** |
| Formatos | PNG, JPG/JPEG, WebP |
| Tamanho máximo | 5 MB |
| Controles | zoom, **Girar**, **Flip H**, **Flip V**, **Trocar imagem** |
| Botões | **CANCELAR (ESC)** · **SALVAR (F2)** |
| Upload | `POST https://utils.beetechapi.be/api/rest/tutils/uploadS3` |
| Vínculo | `POST /api/produto2/cardapio/produto/addImagem` (aceita `produtoID` **ou** `complementoID`) |
| Remover | `DELETE /api/produto2/cardapio/produto/imagem` |

**Pré-requisito escondido:** em item novo, clicar em **ADICIONAR FOTO** primeiro **salva** o
registro (toast *Salvando produto para adicionar foto...*) e só então abre o editor. Se o
**Nome** estiver vazio, aparece *Digite um nome para o produto antes de adicionar foto*.

---

## 7. Endpoints

Prefixo do ambiente via `createApiUrl()` / `createBeetechApiUrl()` (converte
`/datasnap/rest/` em `/api/`).

### Produto

| Operação | Método | Path |
|----------|--------|------|
| Listar | GET | `/api/produto2/cardapio/produtos/{empresaID}/{filialID}/{usuarioID}` |
| Detalhe | GET | `/api/produto2/cardapio/produto/{empresaID}/{usuarioID}/{produtoID}` |
| Criar / editar | POST | `/api/produto2/cardapio/produto` |
| Excluir | DELETE | `/api/produto2/cardapio/produto` |
| Clonar | POST | `/api/produto2/cardapio/produto/clonar` |
| Flags na listagem | POST | `/api/produto2/cardapio/atualizaFlags` |
| Editar em lote | POST | `/api/produto2/cardapio/editarLote` |

> Não há PUT: criar e editar usam o mesmo POST.

### Setor

| Operação | Método | Path |
|----------|--------|------|
| Listar | GET | `/api/produto2/cardapio/setores/{empresaID}/{filialID}/{usuarioID}` |
| Salvar | POST | `/api/produto2/cardapio/setor` |

### Complemento

| Operação | Método | Path |
|----------|--------|------|
| Listar | GET | `/api/produto2/cardapio/produtosComp/{empresaID}/{filialID}/{usuarioID}` |
| Criar / editar | POST | `/api/produto2/cardapio/produto` (com `comp: true`) |

### Grupo de opções e opções

| Operação | Método | Path |
|----------|--------|------|
| Listar grupos | GET | `/api/produto2/cardapio/grupoOpcoes/{empresaID}/{usuarioID}` |
| Detalhe do grupo | GET | `/api/produto2/cardapio/grupoOpcao/{empresaID}/{usuarioID}/{produtoGrupoID}` |
| Criar / editar grupo | POST | `/api/produto2/cardapio/grupoOpcao` |
| Excluir grupo | DELETE | `/api/produto2/cardapio/grupoOpcao` |
| Clonar grupo | POST | `/api/produto2/cardapio/grupoOpcao/clonar` |
| Opções de um grupo | GET | `/api/produto2/cardapio/grupoOpcao/opcoes/{empresaID}/{usuarioID}/{produtoGrupoID}` |
| **Todas** as opções | GET | `/api/produto2/cardapio/grupoOpcao/opcoes/{empresaID}/{usuarioID}/0` |
| Buscar itens para opção | GET | `/api/produto2/cardapio/grupoOpcao/opcoes/buscar/{empresaID}/{filialID}/{usuarioID}` |
| Criar / editar opção | POST | `/api/produto2/cardapio/grupoOpcao/opcao` |
| Excluir opção | DELETE | `/api/produto2/cardapio/grupoOpcao/opcao` |
| Copiar opções | POST | `/api/produto2/cardapio/grupoOpcao/opcao/clonar` |
| **Editar opções em lote** | POST | `/api/produto2/cardapio/grupoOpcao/opcao/editarLote` |

### Vínculo produto ↔ grupo

| Operação | Método | Path |
|----------|--------|------|
| Grupos do produto | GET | `/api/produto2/cardapio/produto/grupo/{empresaID}/{usuarioID}/{produtoID}` |
| Vincular | POST | `/api/produto2/cardapio/produto/grupo/vincular` |
| Ordenar | POST | `/api/produto2/cardapio/produto/grupo/ordem` |
| Flags do vínculo | POST | `/api/produto2/cardapio/produto/grupo/flags` |
| Desvincular | DELETE | `/api/produto2/cardapio/produto/grupo` |

---

## 8. Validações que travam o salvamento

| Onde | Condição | Mensagem |
|------|----------|----------|
| Produto / complemento | **Nome** vazio | `Digite um nome para o produto` — o botão **SALVAR E SAIR (F2)** também fica desabilitado |
| Trocar de aba em item novo | Nome vazio | `Digite um nome para o produto antes de trocar de aba` |
| Adicionar foto em item novo | Nome vazio | `Digite um nome para o produto antes de adicionar foto` |
| Upload | formato diferente de PNG/JPG/WebP | `Formato inválido. Use PNG, JPG ou WebP` |
| Upload | acima de 5 MB | `A imagem deve ter no máximo 5MB` |
| Setor | Nome vazio | `Digite um nome para o setor antes de continuar` |
| Converter combo em complemento | produto tem grupo vinculado | `Remova os grupos de opção antes de continuar.` |

---

## 9. Como o grupo aparece na venda (PDV)

| Item | Valor |
|------|-------|
| Componente | `src/components/ModalCombo.tsx` (PDV, Mesas e Delivery) |
| Documentação interna | `docs/pdv-modal-selecao-opcoes.md` |

O modal mostra a foto do produto, nome, descrição, preço base e um bloco por grupo, com o
contador **N/máx** e a frase *Escolha X a Y*. Cada opção exibe a própria foto e o acréscimo
(**+R$ 3,00**). O botão de confirmação carrega o total e recalcula a cada clique:
**Adicionar ao carrinho - R$ 20,00**.

Comportamentos que dependem da formação de preço:

- `qtdMax === 1` na opção → caixa de seleção; acima de 1 → contador de quantidade.
- `valorDaMaior` → faixa azul *Regra especial: Será cobrado apenas o valor da opção mais cara
  selecionada*, e o checkout zera as opções que não são a mais cara.
- `proporcional` → rateio entre as opções escolhidas (é o modo de pizza meio a meio).
- Grupo com `obrigatorio` ganha o selo **Obrigatório** e bloqueia o avanço sem seleção.

O cenário do manual (formação **Normal**, R$ 15,00 + Bacon R$ 3,00 + Queijo Extra R$ 2,00)
fecha em **R$ 20,00**, o que confirma a soma na prática.

---

## 10. Permissões

| Item | Observação |
|------|------------|
| Menu Cardápio | necessária para abrir a tela |
| `editarLote` | libera **Editar em Lote** nas três abas |
| `editarPreco` | libera os campos de preço na aba Opções |
| Estoque | controla se a aba **Estoque** aparece no modal |
