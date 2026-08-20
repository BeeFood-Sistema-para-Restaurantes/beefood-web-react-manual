# MEMÓRIA — Manual #27 Cardápio: fundamentos

> Memória detalhada deste manual: decisões, cenário montado, descobertas e estado do ambiente.
> Ler antes de mexer neste manual **ou** antes de começar os manuais #28 a #31, que partem dele.

Última atualização: 2026-08-20 (manual concluído, aguardando publicação do dono)

---

## 1. Escopo

Manual base do bloco de cardápio (**#27 a #31**, plano em `PLANO-CARDAPIO.md`). Ensina o
percurso completo uma vez, para que os manuais de segmento só montem o cenário deles:

| Parte | Conteúdo |
|-------|----------|
| 1 | As três abas do Cardápio |
| 2 | Cadastrar complementos (com foto) |
| 3 | Criar o grupo de opções |
| 4 | Incluir as opções no grupo |
| 5 | Criar o setor e o produto |
| 6 | Vincular o grupo ao produto |
| 7 | Conferir no PDV + as quatro Formações de Preço |
| 8 | Filtro, edição e **edição em lote** na sub-aba Opções |

**Fora do escopo:** abas Estoque e Ficha Técnica do produto, Copiar do iFood, Copiar de
Imagem, Exibir/Ocultar, Rodízio, Cardápio Digital.

---

## 2. Cenário montado no sandbox

Base **limpa pelo dono** em 20/08/2026 antes de começar (setor, produto, complemento e grupo
de opções zerados) — confirmado pela API: `produtos=len(0)` e nenhum setor.

| Item | Valor |
|------|-------|
| Setor | **Lanches** |
| Produto | **Sanduíche Natural** — R$ 15,00, descrição *Pão integral, frango desfiado, alface e tomate.* |
| Grupo | **Adicionais** — Mín 0 / Máx 3, formação **Normal** |
| Opções | Bacon R$ 3,00 · Ovo R$ 4,00 · Queijo Extra R$ 2,00 |
| Teste no PDV | R$ 15,00 + Bacon + Queijo Extra = **R$ 20,00** |
| Reajuste em lote | +R$ 1,00 em todas → Bacon R$ 4,00 · Ovo R$ 5,00 · Queijo Extra R$ 3,00 |

**Estado em que o ambiente ficou:** cenário completo e funcional, com os preços das opções
**já reajustados** pela Parte 8. Os complementos seguem com o preço original (3,00 / 4,00 /
2,00) — o lote altera a **opção**, não o complemento. Isso não é inconsistência do produto: é
o comportamento real, e o manual explica na FAQ.

### Decisão: nomes reais, sem prefixo `[Manual]`

O plano previa prefixar tudo com `[Manual]`. **Não foi usado.** Com a base limpa e dedicada,
o prefixo só apareceria em todas as capturas, poluindo o exemplo sem ganho nenhum — a conta
inteira é do manual, não há o que separar. Vale para os #28 a #31: **usar nomes realistas**.

### Fotos

O dono pediu foto em todos os produtos e opções, sem documentar isso no texto. Foram usadas
**4 fotos** de comida (sanduíche, bacon, queijo, ovo), geradas para este manual, redimensionadas
para 900×900 e salvas como JPG (70–170 KB cada).

**Descoberta que economiza trabalho:** a **opção não tem foto própria** — ela herda a imagem
do complemento ou produto vinculado. Ou seja, basta fotografar os complementos: a imagem
reaparece na aba Opções, no modal do PDV e no cardápio digital. Nos manuais seguintes, só é
preciso uma foto por complemento e uma por produto.

O resultado ficou visível onde importa: o modal do PDV (imagem 17) abre com a foto do produto
em destaque e cada opção com a sua.

---

## 3. Descobertas (front)

### A edição em lote NÃO está dentro do modal do grupo

O pedido do dono foi *"na aba grupo de opções → opções temos filtro e edição em lote"*, e ele
está certo — mas o lugar exige atenção, porque existem **duas telas com o nome Opções**:

| Onde | O que tem |
|------|-----------|
| **Modal do grupo → aba Opções** (`GrupoOpcaoOpcoesTab.tsx`) | As opções **daquele grupo**. Filtro *Filtrar Texto*, edição **linha por linha**. **Sem** seleção múltipla. |
| **Aba Grupo de Opções → sub-aba Opções** (`CardapioOpcoesListTab.tsx`) | **Todas as opções do cardápio**, em tabela. Filtro por coluna (funil) e botão **Editar em Lote**. |

A Parte 8 documenta a **segunda**. A primeira aparece na Parte 4, para edição unitária.

### Formação de Preço: os textos de ajuda já vêm prontos

A tela mostra, embaixo de cada modo, a explicação e até a recomendação de uso:
*(Recomendado para Porções)* no **Valor da Maior** e *(Recomendado para Pizzas)* no
**Proporcional**. Isso poupou inventar explicação — o manual usa as mesmas palavras do produto.
A imagem **25** é a captura dessa área com as quatro setas, e é a peça que os manuais de pizza
e hambúrguer vão referenciar.

### Bug do F1 na aba Grupo de Opções

O listener de teclado em `Cardapio.tsx` chama sempre `handleNovoProduto()`. Na aba Grupo de
Opções, **F1 abre o modal de produto**, enquanto o botão **Novo Grupo (F1)** abre o de grupo.
O manual manda clicar no botão e avisa disso. Vale reportar ao time.

### ADICIONAR FOTO salva o registro antes de abrir o editor

Em item novo, clicar em **ADICIONAR FOTO** dispara um save (toast *Salvando produto para
adicionar foto...*). Com o **Nome** vazio, recusa com *Digite um nome para o produto antes de
adicionar foto*. O manual avisa em destaque, porque a ordem dos passos depende disso.

### Preço de Venda do complemento fica bloqueado depois de virar opção

Quando o complemento já participa das opções de um grupo, o campo **Preço de Venda** dele
aparece somente leitura. É proposital, e é a resposta da FAQ "mudei o preço do complemento e a
opção não mudou".

---

## 4. Como as capturas foram feitas

Playwright em script Python, sessão salva em `storage_state`, viewport 1440×900 com
`device_scale_factor=1.5` (imagens 2160×1350). Scripts curtos por etapa, em `/tmp/cap/`, fora
do repositório.

**Seletores que deram trabalho:**

| Situação | O que funciona |
|----------|----------------|
| Abrir um grupo na listagem | `page.locator("h4", has_text="Adicionais")` — `text=` casa também com o banner informativo, que cita "Adicionais" |
| Modal do produto | `div[role="dialog"]` filtrado por `"Restrições / Detalhes"`; com `.last` o popover do combobox de setor era pego no lugar do modal |
| Combobox de Setor | o botão traz o texto **Sem setor**; as opções são `[cmdk-item]`. Depois de escolher, **clicar num rótulo neutro** do modal para fechar o popover — ele ficava aberto na captura, cobrindo os campos ao lado |
| Checkbox de opção no PDV | clicar no `[role="checkbox"]` falha (*intercepts pointer events*); clicar no `p` com o nome da opção funciona |
| Checkbox da etapa 2 do lote | precisa de `click(force=True)`; clicar no `label` não marca |
| Filtro de coluna | `page.locator('th:has-text("Descrição") svg').last` abre o popover **Filtrar Descrição** |

**Esperas:** o modal do produto leva de 6 a 9 s para carregar; o upload de foto (S3 + vínculo)
pede ~9 s depois do **SALVAR (F2)**; o processamento do lote, ~12 s.

**Não precisou:** fechar banner promocional (não apareceu nesta conta) — o `prep()` tenta e
ignora. O widget flutuante de suporte foi escondido por CSS, como sempre.

---

## 5. Marcação das imagens

25 imagens, **68 setas** em 23 delas. Duas de contexto (`passthrough`): a listagem dos três
complementos e a listagem final de produtos — nas duas o ponto é o conjunto, não um controle.

A **25** sai da mesma captura pura da **07** (parâmetro `out_name` do `annotate`): o mesmo
modal, com setas nos quatro modos de Formação de Preço. Foi a forma de ter uma ilustração
própria para a Parte 7 sem repetir imagem.

### Três correções que só apareceram na conferência em tamanho real

1. **Ponta cobrindo o rótulo do botão.** Aconteceu em `PROCESSAR (F2)`, `PRÓXIMO`,
   `FECHAR (ESC)` e `Adicionar ao carrinho`. A correção é mirar a **borda direita** do botão
   (fração ~0.716 nos modais centralizados), não o meio.
2. **Seta atravessando a tabela.** Na **19**, as setas para o funil e para a coluna Valor
   cruzavam as três linhas de opções. Foram removidas — o filtro tem imagem própria (**20**) e
   o texto descreve o funil.
3. **Seta cruzando o rótulo vizinho.** Na **08**, a seta que apontava a aba **Opções** passava
   por cima de "Produtos". Removida: o sistema já destaca a aba ativa em vermelho.

Na **07**, os cinco badges foram para a margem escura da esquerda, empilhados, porque todos os
alvos ficam na coluna esquerda do modal — antes as setas cruzavam o modal inteiro e cobriam os
switches Ativo/Delivery/Presencial.

**Conferência automática:** um script comparou os marcadores do `annotate.py` com os números
citados nas tabelas do `.md` — 25 imagens, 0 divergência. Vale repetir nos próximos manuais.

---

## 6. Nada foi desfeito no ambiente

O cenário ficou de pé de propósito: os manuais #28 a #31 vão pedir base limpa de novo, e até lá
o cenário serve para conferir qualquer dúvida. O carrinho do PDV foi verificado e estava vazio
(o item montado no teste não persiste depois de sair da tela).

**Alterações reais feitas na conta:** 1 setor, 1 produto, 1 grupo, 3 complementos, 3 opções e
1 reajuste em lote de +R$ 1,00. Nenhuma venda foi finalizada.

---

## 7. O que os manuais #28 a #31 herdam daqui

| Item | Como reaproveitar |
|------|-------------------|
| Fluxo completo | Referenciar este manual em vez de repetir as Partes 1 a 6 |
| Formação de Preço | A imagem **25** e a tabela dos quatro modos |
| Dica extra de lote | Bloco pronto no fim da Parte 8; nos segmentos vira caixa curta apontando para cá |
| Fotos | Só complementos e produtos precisam de foto; opção herda |
| Seletores Playwright | Tabela da seção 4 desta memória |
| Nomes | Realistas, **sem** prefixo `[Manual]` |

**Antes de cada um deles: avisar o dono para limpar a base e esperar a confirmação.**
