# texto-documentation.ia.md — Vínculo Marketplace

## PROMPT (copiar e colar)

Em **Delivery**, crie um novo item de menu por último chamado **Vínculo Marketplace**.

Leia APENAS os arquivos abaixo (não varra o resto do projeto):

1. Conteúdo (use na íntegra):
    10|   `beefood-web-react-manual/manuais/vinculo-marketplace/vinculo-marketplace.md`
2. Imagens (nesta ordem), em `beefood-web-react-manual/manuais/vinculo-marketplace/imagens-tratadas/`:
   `01-delivery-menu.png`, `02-listagem.png`, `03-selecionar-item.png`,
   `04-selecionar-vinculo.png`, `05-vinculado.png`, `06-lote-selecao.png`,
   `07-lote-resultado.png`, `08-opcao-selecionar.png`, `09-criar-produto.png`,
   `10-cardapio-produto-criado.png`, `11-excluir-dialogo.png`, `12-venda-aviso.png`,
   `13-modo-venda.png`, `14-bloqueio-fiscal.png`

NÃO leia outros arquivos (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

    20|- Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. É um manual **de operação**: o leitor tem pedidos de marketplace entrando e
  precisa resolver os itens pendentes. Mantenha o passo a passo e as tabelas "Nº → o que fazer"
  logo depois de cada imagem.
- Manter a tabela **Com vínculo × Sem vínculo** da abertura: é ela que explica por que a tarefa
  importa.
- Manter os três avisos em destaque: (1) o **Confirmar Vínculo** grava sem segunda confirmação;
  (2) **procure antes de criar** produto, senão o cardápio duplica; (3) o produto criado nasce
  **sem preço** e precisa ter o cadastro completado.
- Manter a distinção **Produto × Grupo Opção**, inclusive a frase de que opção pendente não
    30|  bloqueia a nota fiscal.
- Não publicar nada do `fluxo-codigo.md`.

## Estrutura da página (na ordem do `.md`)

1. Por que vincular
2. Onde fica a tela
3. Entendendo a tela
4. Vincular um item
5. Vincular vários nomes no mesmo produto
    40|6. Vincular uma opção (adicional)
7. Criar produto e vincular
8. Excluir um vínculo
9. Resolver pelo próprio pedido
10. O bloqueio da nota fiscal
11. Resumo
12. Perguntas frequentes
13. Manuais relacionados

## Anexo — legendas das imagens (na ordem em que aparecem no texto)
    50|
| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|-------|----------------------------------|------|---------|
| 1 | `01-delivery-menu.png` | com setas | Delivery → botão **⋮** → **Vínculo Marketplace** |
| 2 | `02-listagem.png` | com setas | A tela: busca, filtro de status, contadores e as colunas Vínculo e Setor |
| 3 | `03-selecionar-item.png` | com setas | Item marcado na lista e o painel de ações do rodapé |
| 4 | `04-selecionar-vinculo.png` | com setas | Janela **Selecionar Vínculo**: escolher o produto do cardápio e confirmar |
| 5 | `05-vinculado.png` | com setas | Depois do vínculo: status **Vinculado**, produto, setor e contadores |
| 6 | `06-lote-selecao.png` | com setas | Dois nomes selecionados de uma vez |
| 7 | `07-lote-resultado.png` | com setas | Os dois nomes apontando para o mesmo produto |
| 8 | `08-opcao-selecionar.png` | com setas | Item **Grupo Opção**: a janela passa a oferecer produtos **e** opções de grupo |
    60|| 9 | `09-criar-produto.png` | com setas | **Criar produto e vincular** e o diálogo de confirmação |
| 10 | `10-cardapio-produto-criado.png` | com setas | O produto criado no Cardápio, no setor **Vínculo Marketplace** e sem preço |
| 11 | `11-excluir-dialogo.png` | com setas | **Excluir** e o aviso de que a ação não pode ser desfeita |
| 12 | `12-venda-aviso.png` | com setas | A faixa **Produto não associado no pedido - sem vínculo marketplace** dentro do pedido |
| 13 | `13-modo-venda.png` | com setas | O mesmo modal aberto por um pedido: título com o número e coluna **Nível** |
| 14 | `14-bloqueio-fiscal.png` | com setas | **Produtos sem vínculo marketplace**: a NFC-e barrada e o EMITIR FISCAL desabilitado |

## Observações de conteúdo

- A imagem **`02-listagem.png`** é a de referência da tela: publique grande o suficiente para o
  leitor ler as colunas **Vínculo** e **Setor**.
    70|- O par **`03` → `04` → `05`** é o passo a passo principal (selecionar → escolher → conferir).
  Não separe essas três em seções diferentes.
- Nas imagens **12** e **14** há regiões borradas de propósito (nome, telefone e endereço de
  cliente real). Não substituir nem tentar "limpar".
- Não publicar nomes de campo da API, rotas, IDs de produto/venda nem nomes de arquivo do código.
- Não entrar no assunto "de qual marketplace veio cada linha": a tela não mostra essa informação.
