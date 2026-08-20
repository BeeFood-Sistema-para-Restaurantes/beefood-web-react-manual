# MEMÓRIA — Manual #29 Cardápio: pizza

> Memória detalhada deste manual: decisões, cenário montado, descobertas e estado do ambiente.
> Ler antes de mexer neste manual **ou** de escrever qualquer coisa sobre Formação de Preço.

Última atualização: 2026-08-20 (manual concluído, aguardando publicação do dono)

---

## 1. A descoberta que definiu o manual

O plano original (`PLANO-CARDAPIO.md`) e o manual **#27** diziam que **Proporcional** calcula a
**média** das opções: dois sabores de R$ 40,00 e R$ 45,00 dariam R$ 42,50. **Está errado, e foi
comprovado no PDV.**

| Grupo | Seleção | Botão do PDV |
|-------|---------|--------------|
| Valor da Maior (preço inteiro nos sabores) | Calabresa R$ 40 | R$ 40,00 |
| Valor da Maior | Calabresa + Portuguesa R$ 45 | **R$ 45,00** |
| Proporcional (preço inteiro nos sabores) | Calabresa R$ 40 | R$ 40,00 |
| Proporcional | Calabresa + Portuguesa R$ 45 | **R$ 85,00** |

O Proporcional **soma**, igual ao Normal. No código do front (`ModalCombo.tsx`,
`calcularValorTotal`) **não existe ramo para `proporcional`** — ele cai no mesmo `else` do
Normal. A média existe no backend (`pedidoPOST.js`, `processaGrupoOpcao`), mas ela é gravada em
**cada linha** e depois multiplicada pelo número de linhas: `média × N = soma`. Ou seja, é
**rateio por sabor nos relatórios**, não desconto para o cliente.

### O modelo que faz o Proporcional funcionar

Testado e confirmado: cadastrar em cada opção o preço de **meia pizza**, com o grupo em
**mínimo 2 / máximo 2** e **cada opção com máximo 2**.

| Seleção | Botão |
|---------|-------|
| Calabresa 1× | R$ 20,00 (meia pizza — o grupo exige 2) |
| **Calabresa 2×** | **R$ 40,00** (pizza inteira) |
| **Calabresa + Portuguesa** | **R$ 42,50** (média de R$ 40 e R$ 45) |
| Calabresa 3× | R$ 40,00 (bloqueado pelo máximo do grupo) |
| Meio a meio + Borda Catupiry R$ 8,00 | **R$ 50,50** |

**O #27 foi corrigido** nesta mesma branch: a tabela das quatro formações agora diz que o
Proporcional soma, com o alerta e a explicação do preço da fração.

---

## 2. Escopo e estrutura

O manual apresenta **dois modelos** e recomenda o primeiro para quem está começando:

| | Modelo A — Valor da Maior | Modelo B — Proporcional |
|---|---|---|
| Preço na opção | inteiro | metade |
| Mín / Máx do grupo | 1 / 2 | 2 / 2 |
| Máximo da opção | 1 | 2 |
| Meio a meio (R$ 40 e R$ 45) | R$ 45,00 | R$ 42,50 |

Sete partes: sabores como complementos → grupo Valor da Maior → grupo Proporcional → borda →
produto com preço R$ 0,00 → vínculo → PDV.

**Fora do escopo:** tamanhos (média/grande/família), combo com bebida, rodízio, três ou mais
sabores como exemplo montado (só citados na FAQ).

---

## 3. Cenário montado no sandbox

Base **limpa pelo dono** em 20/08/2026 antes de começar.

| Item | Valor |
|------|-------|
| Setor | **Pizzas** |
| Sabores (complementos) | Calabresa R$ 40,00 · Marguerita R$ 42,00 · Portuguesa R$ 45,00 · Quatro Queijos R$ 48,00 |
| Bordas (complementos) | Borda Catupiry R$ 8,00 · Borda Cheddar R$ 6,00 |
| Grupo A | **Sabores (Valor da Maior)** — Valor da Maior, mín 1 / máx 2, opções com preço **inteiro**, opção máx 1 |
| Grupo B | **Sabores (Proporcional)** — Proporcional, mín 2 / máx 2, opções com preço **metade** (20 / 21 / 22,50 / 24), opção máx 2 |
| Grupo C | **Borda** — Normal, mín 0 / máx 1, compartilhado pelos dois produtos |
| Produtos | **Pizza Média (Valor da Maior)** e **Pizza Média (Proporcional)**, ambos com Preço de Venda **R$ 0,00** |

**Estado em que o ambiente ficou:** cenário completo e funcional, os dois produtos ativos no
setor Pizzas. Nenhuma venda foi finalizada.

### Fotos

7 imagens geradas para este manual (4 sabores, 2 bordas, 1 pizza meio a meio para os produtos),
900×900 JPG, 143 a 284 KB. Confirmado o aprendizado do #27: **a opção herda a foto do
complemento**, então bastou fotografar os 6 complementos e os 2 produtos.

O ganho aparece no modal do PDV: cada sabor entra com a própria foto, e a pizza abre com a
imagem grande no topo.

---

## 4. Descobertas técnicas

### O botão "+" do contador de quantidade é decorativo

`ModalCombo.tsx`, linhas ~1517 a 1524: o botão vem com `disabled` fixo e
`pointer-events-none`. Quem aumenta a quantidade é o **clique na linha** da opção; o "−"
funciona. Descoberto porque o script tentou clicar no "+" e ele estava sempre desabilitado —
inclusive com 0 selecionado.

Isso importa para o manual: **pizza inteira de um sabor se pede clicando duas vezes na linha**,
e o texto avisa que o "+" não funciona. Vale reportar ao time.

### O contador só aparece se o MÁXIMO DA OPÇÃO for maior que 1

`opcao.qtdMax === 1` → caixa de seleção; `> 1` → contador. É o máximo **da opção**, não o do
grupo. Sem isso não há como repetir o mesmo sabor, e o modelo Proporcional não fecha.

### Travessão no nome vira "?"

`Pizza Média — Proporcional` (em dash, U+2014) aparece na tela como `Pizza Média ? Proporcional`
— no card do PDV, na listagem e no modal de busca de opções. Provável coluna `varchar` no SQL
Server. Os produtos foram renomeados para usar **parênteses**.

**Regra para os próximos manuais: nada de travessão em nome de produto.** Acentos comuns
funcionam sem problema.

### Aviso de grupo compartilhado

Grupo vinculado a mais de um produto abre com faixa amarela: *Alterações neste grupo refletem em
todos os N produtos vinculados.* Apareceu no grupo Borda e virou a seta 1 da imagem 07 — reforça
o alerta que o #27 já dá em texto.

### Campos `pizza` e `proporcionalTipo` são legado

Vêm da view SQL, mas não têm controle na UI nem uso no cálculo. Não confundir com uma
"funcionalidade de pizza" escondida.

---

## 5. Automação das capturas

Mesmos padrões do #27, mais estes:

| Situação | O que funciona |
|----------|----------------|
| Editar preço/limite da opção | Linha compacta: clicar no `span` do nome. Expandida, `input[type=number]` na ordem `[0][1]` = mín/máx do **grupo**, `[2][3]` = mín/máx da **opção**, `[4]` = Valor, `[5][6]` = V. Delivery / V. Presencial. Confirmar no **SALVAR** da linha |
| Marcar itens em *Buscar e Cadastrar* | **Não use a busca**: limpar o campo desmarca tudo e o botão Adicionar volta a ficar desabilitado. Percorrer a lista completa e casar pelo texto do container do checkbox |
| Repetir opção no PDV | Clicar duas vezes na linha (o "+" é travado) |
| Modal rolado na captura | O modal do PDV rola sozinho ao selecionar opções e a captura perde o topo — inclusive o aviso azul do Valor da Maior. Zerar `scrollTop` de todos os filhos roláveis antes do screenshot |
| Atalhos de configuração rápida | *Poderá selecionar várias opções e repetir* sobrescreve mín/máx do grupo para 1 e 10. Configurar na mão quando o grupo precisa de 2/2 |

Esperas: modal do grupo 8 a 9 s; upload de foto ~9 s depois do SALVAR; salvar grupo com opções
modificadas ~10 s.

---

## 6. Marcação das imagens

15 imagens, **36 setas** em 14 delas. Uma de contexto (`passthrough`): o cardápio final com as
duas pizzas.

Várias imagens vêm **em par** (uma do grupo Valor da Maior, outra do Proporcional) com as setas
nas mesmas coordenadas — assim o leitor compara direto o que mudou. Vale repetir a ideia nos
próximos manuais quando houver dois caminhos.

Correções feitas na conferência em tamanho real:

1. **Pontas cobrindo valor de tabela.** Nas listagens de opções, mirar `y` da linha cobria o
   `R$ 40,00` e o `0 - 1`. Corrigido mirando ~0,02 abaixo do centro da linha.
2. **Três setas cruzadas na 09.** As setas para Tipo, Qtd. Mín./Máx. e a linha da Borda se
   cruzavam. Reduzido para duas; a linha da Borda ficou descrita no texto.
3. **Contadores do PDV.** Mirar o número da quantidade cobria o dígito; a seta passou a mirar a
   borda direita do contador (fração 0,700).

Conferência automática (`annotate.py` × `.md`): **15 imagens, 0 divergência**.

---

## 7. O que os próximos manuais herdam

| Item | Detalhe |
|------|---------|
| Proporcional | **Soma.** Só faz média se o preço da opção for o da fração |
| Valor da Maior | Cobra a opção mais cara e **avisa o operador** no PDV |
| Preço base do produto | Sempre **soma** ao que vem dos grupos; em pizza precisa ser R$ 0,00 |
| Contador de quantidade | Depende do **máximo da opção**; o "+" é travado, clique na linha |
| Nome de produto | Sem travessão |
| Buscar e Cadastrar | Não usar a busca antes de marcar |
| Captura de modal do PDV | Zerar o scroll antes do screenshot |

**Antes do #28 (hambúrguer): avisar o dono para limpar a base e esperar a confirmação.**
