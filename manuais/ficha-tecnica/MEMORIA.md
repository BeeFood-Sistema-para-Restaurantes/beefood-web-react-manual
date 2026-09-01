# MEMÓRIA — #72 Ficha Técnica

Status: ✅ Concluído em 01/09/2026. **15 imagens**, 41 setas.
Estudo que originou: [`PLANO-FICHA-TECNICA.md`](../../PLANO-FICHA-TECNICA.md).

## Como o manual nasceu

O dono pediu um estudo de "como cadastrar ficha técnica" com exemplo de **pizza**. O estudo mostrou
que a pizza tem uma armadilha (a ficha do sabor precisa ser de **meia** pizza, e isso só fecha no
modelo Proporcional do #29), e o dono decidiu: **corrigir a pizza depois** e fazer o primeiro
manual em outro segmento. Escolhemos **hambúrguer**, porque:

- o sandbox já é uma hamburgueria completa (7 setores, 67 produtos, 41 complementos);
- os adicionais **Carne 100g** e **Bacon** já vêm com **máximo 2** por opção, o que permitiu rodar
  no hambúrguer o teste que a pizza precisava;
- o lanche tem preço próprio, então a margem aparece verde e faz sentido didático (a pizza tem
  preço R$ 0,00 e mostra margem negativa).

Decisão do dono sobre unidade (01/09/2026): **insumo em KG/L e quantidade em fração**. Virou o
quadro "gramas ÷ 1000" da Parte 1 — com o alerta de que `0,05` é 50 g e 5 g é `0,005`.

## Limpeza da base

O dono pediu para **apagar todos os insumos** antes de começar. Dos 21 existentes, 20 foram
apagados. Sobrou **Maionese da casa (sache)**, que não sai: três receitas antigas (já usadas em
produções, portanto só desativáveis por *soft delete*) travam a exclusão, e a API **recusa**
salvar receita com `itens: []`. A saída foi apontar as três receitas para esse único insumo e
apagar o resto — e ele acabou virando conteúdo do manual (a Parte "Insumo que vem de uma receita").

## Cenário montado

| Insumo | Un. | Custo | Estoque inicial | Mínimo |
|--------|-----|------:|----------------:|-------:|
| Pão brioche | UN | R$ 1,80 | 100 | 20 |
| Blend bovino | KG | R$ 42,00 | 10 | 2 |
| Queijo prato fatiado | KG | R$ 39,00 | 5 | 1 |
| Bacon em fatias | KG | R$ 34,00 | 5 | 1 |
| Alface | KG | R$ 8,00 | 3 | 0,5 |
| Tomate | KG | R$ 6,00 | 3 | 0,5 |
| Embalagem do lanche | UN | R$ 0,90 | 200 | 50 |
| Batata congelada | KG | R$ 10,00 | 20 | 5 |
| Óleo de fritura | L | R$ 9,00 | 20 | 5 |
| Embalagem da porção | UN | R$ 0,45 | 200 | 50 |
| Maionese da casa (sache) | KG | R$ 10,19 | — (**sem controle**, vem de receita) | — |

Fichas: **One Burger** 7 insumos = **R$ 8,08** (venda R$ 28,00 → 71,1%); **Carne 100g** R$ 4,20;
**Bacon** R$ 1,02; **Fatia de queijo** R$ 0,78; **Batata frita** R$ 2,54.

O **Alface** foi deixado de fora do cadastro por API de propósito: ele é criado **pela interface**
durante a captura (imagens 02 e 03) e adicionado à ficha ao vivo (imagem 04).

## Provas

| Venda | Pedido | O que provou |
|-------|--------|--------------|
| **#925** | One Burger + 2× Carne 100g | Baixa já no **Receber**; blend −0,1 (produto) + −0,2 (adicional 2×) |
| **#927** | 2× Batata frita | Ficha de porção (granel + litro + embalagem) e multiplicação por quantidade |
| **#928** | One Burger + 2× Carne 100g | A venda da imagem 12, já com o alface na ficha |

## Descobertas

1. **Opção repetida baixa em dobro** (`origemQtd = 2`). Era a pergunta em aberto do estudo da
   pizza: com isso, o modelo **Proporcional** com ficha de meia pizza funciona.
2. **A baixa acontece no `Receber`**, na criação da pré-venda — antes do pagamento.
3. **Insumo sem `Controlar Estoque` não movimenta.** Ele entra no custo e some do relatório. Foi
   comprovado com a maionese da casa, que ficou de fora das 7 linhas da venda #928.
4. **A trilha da baixa tem dois ou três níveis** (`One Burger -> Pão brioche` /
   `One Burger -> Carne 100g -> Blend bovino`), e é o que permite auditar de onde saiu cada grama.
5. **Custo e Custo Ficha Técnica somam.** Quem preenche os dois dobra o custo do prato.
6. **Insumo em uso por receita não é excluível nem com a receita inativa.**

## Captura (`capturar.py`)

Playwright 1440×900, DPR 1,5, tema claro, `LANG=pt_BR.UTF-8`, espera do spinner + 5 s.
Etapas separadas (`insumos`, `ficha`, `outras`, `estoque`, `pdv`, `mov`, `editar`, `receita`) para
repetir só o que falhar. A etapa `pdv` **registra uma venda de verdade** — não é idempotente.

Armadilhas (as mesmas listadas no `fluxo-codigo.md`, seção 7):

| Problema | Solução |
|----------|---------|
| Dois produtos com o mesmo nome | `abrir_produto(..., marcador="Blend bovino")` abre um por um até achar |
| Popover de busca tapa a tabela depois de Adicionar | `Escape` antes do print |
| `Esc` na linha em edição fecha o modal | cancelar pelo ✗ da própria linha |
| Estoque Mínimo não aceita vírgula | `input[type=number]` → `0.5` |
| Trocar de aba no modal do insumo já salva | contar com isso ao repetir a captura |

## Anotação

15 imagens, 41 setas, 1 de contexto (`08`). Ajustes feitos depois de conferir em tamanho real:

1. A seta do **Custo Total** na 05 apontava de baixo e a bolha cobria *FECHAR (ESC)*: bolha movida
   para a esquerda do rodapé.
2. Na 06 as três bolhas de custo cobriam o texto da **Descrição**: descidas para dentro da caixa,
   abaixo da linha de texto; e a seta da margem passou a mirar **acima** da etiqueta, para não
   tapar o "R$ 19,92 (71,1%)".
3. Na 12 as bolhas foram subidas para a faixa do cabeçalho da tabela — em tabela densa não há
   espaço vazio, e cobrir rótulo de coluna é menos danoso que cobrir dado.

## Estado em que o ambiente ficou

- 11 insumos (10 novos + a maionese da receita), todos com saldo, exceto a maionese.
- Fichas cadastradas em One Burger, Carne 100g, Bacon, Fatia de queijo e Batata frita.
- Três vendas pagas em dinheiro (#925, #927, #928).
- Três receitas antigas **inativas**, todas apontando para a maionese da casa.

## Fora do escopo

Receitas e Produção (manual próprio), importação de NF-e, movimentação manual de estoque como
assunto, inventário, e a **pizza** — que volta quando o dono avisar (seção 9 do
`PLANO-FICHA-TECNICA.md`).
