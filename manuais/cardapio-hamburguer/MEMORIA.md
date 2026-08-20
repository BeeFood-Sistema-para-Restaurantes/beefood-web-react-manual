# MEMÓRIA — Manual #28 Cardápio: hambúrguer

> Memória detalhada deste manual: decisões, cenário montado, descobertas e estado do ambiente.

Última atualização: 2026-08-20 (manual concluído, aguardando publicação do dono)

---

## 1. Escopo

Terceiro manual do bloco de cardápio. O assunto novo é a formação **Brinde** — opção que o
cliente escolhe e que **não altera o preço** — e o checkbox **Obrigatório**. Nenhum dos dois
tinha sido demonstrado na prática nos manuais anteriores.

O hambúrguer é o caso em que os três tipos de grupo aparecem juntos:

| Pergunta | Grupo | Formação | Efeito no preço |
|----------|-------|----------|-----------------|
| Qual o ponto? | Ponto da carne | **Brinde** + **Obrigatório**, 1/1 | nenhum |
| Quer adicional? | Adicionais | **Normal**, 0/5 | soma |
| Quer tirar algo? | Retirar ingredientes | **Brinde**, 0/3 | nenhum |

Oito partes: complementos → grupo Brinde obrigatório → grupo Normal → grupo Brinde opcional →
produto → vínculo com ordenação → PDV → reaproveitar grupos em outro lanche.

**Fora do escopo:** combo com bebida, carne dupla como exemplo montado (só na FAQ), estoque.

---

## 2. Cenário montado no sandbox

Base **limpa pelo dono** em 20/08/2026, confirmado pela API antes de começar (0 setores,
0 produtos, 0 grupos, 0 opções).

| Item | Valor |
|------|-------|
| Setor | **Lanches** |
| Ponto da carne | Mal passado · Ao ponto · Bem passado — **R$ 0,00**, com foto |
| Adicionais | Bacon R$ 3,00 · Cheddar R$ 2,00 · Ovo R$ 4,00 · Cebola caramelizada R$ 5,00 |
| Retirar | Sem cebola · Sem tomate · Sem alface — **R$ 0,00**, **sem foto** |
| Grupos | Ponto da carne (Brinde + Obrigatório, 1/1) · Adicionais (Normal, 0/5) · Retirar ingredientes (Brinde, 0/3) |
| Produtos | **X-Burger** R$ 28,00 (três grupos) e **X-Salada** R$ 26,00 (dois grupos, compartilhados) |

**Conta conferida no PDV:** R$ 28,00 → com *Ao ponto* segue **R$ 28,00** → com Bacon e Cheddar
vai a **R$ 33,00** → com *Sem cebola* fica em **R$ 33,00**.

**Estado em que o ambiente ficou:** cenário completo, com um X-Burger de R$ 33,00 adicionado ao
carrinho do PDV no último teste (não finalizado — o carrinho não persiste depois de sair da
tela).

### Fotos

9 imagens: 3 pontos de carne (patty cortado mostrando o cozimento), 4 adicionais e 2 lanches.
**Bacon, Cheddar e Ovo foram reaproveitados do #27** — os complementos são os mesmos, e não fez
sentido gerar outra vez.

**Os itens de retirada ficaram sem foto de propósito.** Não existe imagem que faça sentido para
"Sem cebola", e a listagem lado a lado (uns com foto, outros sem) virou material didático: é a
seta 3 da imagem 01. Vale a mesma decisão para grupos de remoção nos próximos manuais.

---

## 3. Descobertas

### Brinde não é o que zera o preço — o valor da opção é

O modo Brinde manda `agregaValor: false` para a API, mas o cálculo do PDV soma o **valor da
opção**. Ou seja: **se a opção tiver preço cadastrado, num grupo Brinde ela ainda soma**. O que
garante o zero é o complemento ter sido cadastrado sem preço.

O manual avisa isso em destaque, porque é uma armadilha silenciosa: o cadastro parece certo e a
conta sai errada.

### Obrigatório valida no clique, não desabilitando o botão

Testado: com o grupo obrigatório sem seleção, o botão **Adicionar ao carrinho** **continua
habilitado**. Ao clicar, aparece um toast vermelho:

> **Seleção obrigatória** — *Por favor, selecione as opções do grupo "Ponto da carne".*

e o modal permanece aberto. Depois de escolher, o **selo vermelho Obrigatório** ao lado do nome
do grupo é substituído por um **ícone verde de check**. As duas telas entraram no manual
(imagens 09, 14 e 10).

### Ordem dos grupos: todos entram como 1

Ao vincular três grupos de uma vez, todos ficam com ordem `1` e a listagem sai em **ordem
alfabética** — *Adicionais* apareceu antes de *Ponto da carne*, o que não é a ordem em que o
atendente pergunta. Uma clicada na seta ↑ renumera para `1`, `2`, `3` e a ordem vale no PDV.

Ficou como seta 2 da imagem 08 e como aviso no texto.

### O rastro de uso do complemento é por grupo

O card do complemento mostra **Usado 1 vez: Adicionais**, não "usado em 2 produtos". Como o
grupo Adicionais serve ao X-Burger e ao X-Salada, o número 1 se refere ao **grupo**. Bom saber
para não interpretar errado.

---

## 4. Automação das capturas

Mesmos padrões dos #27 e #29. Dois pontos novos:

| Situação | O que funciona |
|----------|----------------|
| Marcar o checkbox **Obrigatório** | `page.locator('div[role="dialog"] [role="checkbox"]').first.click(force=True)` — é o primeiro checkbox do modal; sem `force` não marca |
| Reordenar grupo no produto | As setas `chevron-up` estão na ordem visual das linhas: `nth(1)` é a segunda linha. **Não** tente casar pelo texto do ancestral — a tabela inteira contém o nome de todos os grupos, e o seletor cai na primeira linha (cuja seta está desabilitada) |
| Capturar grupo abaixo do dobrão | `scroll_into_view_if_needed()` no nome da opção. Sem isso, o grupo Adicionais ficava fora da captura e a imagem provava o total sem mostrar o que foi marcado |

Cadastrar 10 complementos com 7 fotos levou ~5 min de execução; os três grupos, ~3,5 min.

---

## 5. Marcação das imagens

16 imagens, **32 setas** em 15 delas. Uma de contexto (`passthrough`): o cardápio com os dois
lanches.

O manual repete o mesmo alvo em pontos diferentes de propósito, porque o assunto é um só
(o Brinde não cobra): o R$ 0,00 no cadastro (03), a opção sem `+R$` no PDV (10), o total que não
muda (10 e 12) e o item aparecendo no carrinho sem somar (13).

**Correção feita na conferência:** na imagem 01, as três setas saíam de badges posicionados na
área dos cards de baixo e cruzavam os cards que são o assunto da imagem. Refeito com os alvos na
**primeira coluna**, um por linha, e os badges na faixa da sidebar — três setas horizontais
curtas. Os badges cobrem parcialmente itens do menu lateral, que não são o assunto.

Conferência automática (`annotate.py` × `.md`): **16 imagens, 0 divergência**.

---

## 6. O que os próximos manuais herdam

| Item | Detalhe |
|------|---------|
| Brinde | Declara a intenção; o **valor da opção** é o que garante o preço zero |
| Obrigatório | Bloqueia no clique com toast, não desabilita o botão; selo vermelho vira check verde |
| Ordem dos grupos | Vinculados em lote entram todos como `1`, em ordem alfabética — reordenar na mão |
| Fotos | Grupos de remoção não precisam de foto, e o contraste na listagem é didático |
| Preço base | No hambúrguer fica **no produto** (diferente da pizza, que é R$ 0,00) |
| Seletores | Checkbox Obrigatório com `force=True`; setas de ordem por posição, não por texto |

**Antes do #30 (açaí): avisar o dono para limpar a base e esperar a confirmação.**
