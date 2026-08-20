# Prompt para publicar o manual — Cardápio: fundamentos (#27)

> Cole o texto abaixo na IA de documentação do app, junto com as 25 imagens da pasta
> `imagens-tratadas/`, na ordem da tabela do fim.

---

## Instrução

Publique um manual de usuário final chamado **"Cardápio — fundamentos"**, na seção
**Cardápio**. Use o conteúdo de `manuais/cardapio-fundamentos/cardapio-fundamentos.md` como
fonte, **sem reescrever o texto** — ele já está no padrão dos outros manuais publicados
(tom didático, tabelas "Nº → o que fazer" logo abaixo de cada imagem, campos obrigatórios
marcados com asterisco).

Este é o **manual base do bloco de cardápio**. Os manuais de hambúrguer, pizza, açaí e comida
japonesa (a publicar depois) apontam para ele, então ele precisa ficar publicado primeiro e
com URL estável.

### Estrutura a preservar

1. As três peças do cardápio (complemento → grupo → produto) e o diagrama do caminho
2. Pré-requisitos
3. Parte 1 — Onde tudo acontece (as três abas)
4. Parte 2 — Cadastrar os complementos (com o editor de foto)
5. Parte 3 — Criar o grupo de opções
6. Parte 4 — Incluir as opções no grupo
7. Parte 5 — Cadastrar o produto (setor + produto)
8. Parte 6 — Vincular o grupo ao produto
9. Parte 7 — Conferir na venda (PDV) + as quatro Formações de Preço
10. Parte 8 — Filtrar, editar e reajustar preços em lote
11. Resumo do caminho (bloco de código com os 7 passos)
12. Perguntas frequentes
13. Próximos manuais do cardápio

### Pontos que devem continuar em destaque

- **Comece pelos complementos** — cadastrar na ordem inversa funciona, mas é mais lento.
- **Preencha o Nome antes de clicar em ADICIONAR FOTO**: em item novo o sistema salva o
  registro antes de abrir o editor e recusa com nome vazio.
- **Nome é o único campo obrigatório** do produto e do complemento.
- **Preço de Venda do produto é o preço base** — o que vem dos grupos é somado em cima.
- **O grupo é compartilhado:** alterar um grupo afeta **todos** os produtos vinculados; para
  regra própria, clonar o grupo.
- **Mínimo/Máximo do grupo ≠ Mínimo/Máximo da opção.**
- **As quatro Formações de Preço** com o exemplo numérico de dois sabores (R$ 40 e R$ 45):
  Normal R$ 85,00 · Brinde R$ 0,00 · Valor da Maior R$ 45,00 · Proporcional R$ 42,50.
- **Filtre antes de alterar em lote** — em cardápio grande é a diferença entre reajuste seguro
  e acidente.
- **Excluir Opções no lote não tem volta.**
- Na aba Grupo de Opções, usar o **botão Novo Grupo (F1)**, não a tecla F1 (o atalho abre o
  cadastro de produto).

### Conferência do exemplo

O manual monta um caso completo e fecha a conta na tela de venda. Não altere os números:

| Item | Valor |
|------|-------|
| Setor | Lanches |
| Produto | Sanduíche Natural — R$ 15,00 |
| Grupo | Adicionais — Mín 0 / Máx 3 / **Normal** |
| Opções | Bacon R$ 3,00 · Queijo Extra R$ 2,00 · Ovo R$ 4,00 |
| Total no PDV | R$ 15,00 + R$ 3,00 + R$ 2,00 = **R$ 20,00** |
| Reajuste em lote | +R$ 1,00 → Bacon R$ 4,00 · Ovo R$ 5,00 · Queijo Extra R$ 3,00 |

---

## Imagens, na ordem

Todas em `manuais/cardapio-fundamentos/imagens-tratadas/`.

| # | Arquivo | Tipo | Legenda / o que mostra |
|---|---------|------|------------------------|
| 1 | `01-cardapio-produtos-vazio.png` | setas | Tela Cardápio e as três abas: 1 Produtos · 2 Grupo de Opções · 3 Complementos |
| 2 | `02-aba-complementos.png` | setas | Aba Complementos vazia · 1 Novo Complemento (F1) |
| 3 | `03-modal-complemento.png` | setas | Cadastro do complemento Bacon · 1 Nome · 2 Preço de Venda · 3 ADICIONAR FOTO · 4 SALVAR E SAIR (F2) |
| 4 | `04-foto-editor.png` | setas | Editor de imagem · 1 Girar/Flip/Trocar · 2 SALVAR (F2) |
| 5 | `05-complementos-lista.png` | contexto | Os três complementos com foto e preço, todos marcados **Sem uso** |
| 6 | `06-aba-grupo-opcoes.png` | setas | Aba Grupo de Opções vazia · 1 Novo Grupo (F1) |
| 7 | `07-grupo-detalhes.png` | setas | Detalhes do Grupo · 1 Nome · 2 Obrigatório · 3 Formação de Preço · 4 Mínimo · 5 Máximo |
| 8 | `08-grupo-aba-opcoes-vazia.png` | setas | Aba Opções do grupo · 1 BUSCAR E CADASTRAR · 2 CADASTRAR NOVA OPÇÃO · 3 COPIAR DE OUTRO · 4 Filtrar Texto |
| 9 | `09-buscar-cadastrar.png` | setas | Buscar e Cadastrar Opções · 1 busca · 2 Selecionar todos · 3 Adicionar |
| 10 | `10-grupo-opcoes-lista.png` | setas | As três opções no grupo · 1 opção (foto/nome herdados) · 2 Valor · 3 SALVAR E SAIR (F2) |
| 11 | `11-novo-setor.png` | setas | Novo Setor · 1 Nome Interno do Setor · 2 SALVAR E SAIR (F2) |
| 12 | `12-modal-produto.png` | setas | Cadastro do produto · 1 ADICIONAR FOTO · 2 Nome · 3 Setor · 4 Preço de Venda · 5 Descrição · 6 SALVAR E SAIR (F2) |
| 13 | `13-produto-grupo-vazio.png` | setas | Aba Grupo de Opções do produto · 1 aba · 2 BUSCAR GRUPO E VINCULAR · 3 CADASTRAR NOVO GRUPO DE OPÇÕES |
| 14 | `14-vincular-grupo.png` | setas | Buscar e Vincular Grupo de Opções · 1 marcar o grupo · 2 Vincular |
| 15 | `15-produto-grupo-vinculado.png` | setas | Grupo vinculado · 1 Qtd. Mín. · 2 Qtd. Máx. · 3 Tipo · 4 SALVAR E SAIR (F2) |
| 16 | `16-produtos-lista.png` | contexto | O produto no cardápio, dentro do setor Lanches, com o selo COMBO |
| 17 | `17-pdv-modal-opcoes.png` | setas | PDV, seleção das opções · 1 grupo, contador 2/3 e "Escolha 0 a 3" · 2 opção marcada · 3 Adicionar ao carrinho - R$ 20,00 |
| 18 | `18-pdv-carrinho-total.png` | setas | Carrinho · 1 item com os adicionais listados · 2 Valor Final R$ 20,00 |
| 19 | `25-formacao-preco.png` | setas | Os quatro modos de Formação de Preço · 1 Normal · 2 Brinde · 3 Valor da Maior · 4 Proporcional |
| 20 | `19-subaba-opcoes.png` | setas | Sub-aba Opções (Todas as Opções) · 1 sub-aba Opções · 2 Editar em Lote |
| 21 | `20-filtro-opcoes.png` | setas | Filtro da coluna Descrição · 1 Digite para filtrar... · 2 Limpar 1 filtro |
| 22 | `21-lote-selecao.png` | setas | Editar Opções em Lote, etapa 1 · 1 Buscar por nome · 2 Desmarcar Todas · 3 contador 3 de 3 · 4 PRÓXIMO |
| 23 | `22-lote-config.png` | setas | Etapa 2 · 1 Preço de Venda · 2 Venda · 3 Adicionar · 4 Valor (R$) · 5 quanto · 6 PROCESSAR (F2) |
| 24 | `23-lote-concluido.png` | setas | Etapa 3 · 1 Concluído 3 de 3 · 2 "3 sucesso" · 3 FECHAR (ESC) |
| 25 | `24-opcoes-atualizadas.png` | setas | Listagem com os preços reajustados · 1 coluna Valor |

> A imagem 19 da lista (`25-formacao-preco.png`) é a **mesma captura** da imagem 7
> (`07-grupo-detalhes.png`), com setas diferentes: ali nos campos do grupo, aqui nos quatro
> modos de preço. Publicar as duas.

---

## Observações para quem publica

- Manual **somente desktop**: todo o cadastro de cardápio é feito no painel web.
- A Parte 8 executa uma alteração **real e imediata** de preço em todos os produtos que usam os
  grupos afetados. O texto já avisa; mantenha o alerta.
- Não há dado de cliente em nenhuma captura — nada a mascarar.
- Publique antes dos manuais de segmento (hambúrguer, pizza, açaí, japonesa), que apontam para
  este.
