# Manual da Ficha Técnica — o custo do prato

A **ficha técnica** é a lista de ingredientes e embalagens que compõem um item do seu cardápio.
Ela faz duas coisas por você:

- **mostra quanto o prato custa** — e, com o preço de venda, qual é a sua margem;
- **baixa o estoque sozinha** a cada venda, ingrediente por ingrediente.

Este manual monta a ficha de uma hamburgueria do começo ao fim: o lanche, os adicionais e uma
porção. No final, uma venda de verdade no PDV prova que o estoque desceu certinho.

> As imagens têm **setas numeradas** (1, 2, 3…). Cada número indica o campo ou botão
> correspondente na tela. Campos com **\*** são **obrigatórios**.

---

## Não confunda com outras duas telas

| Nome | Onde fica | Para que serve |
|------|-----------|----------------|
| **Ficha Técnica** | Aba dentro do produto e do complemento | O que este manual ensina: composição, custo e baixa de estoque |
| **Receita** e **Produção** | Menu **Estoque → Receitas** / **Produção** | Insumo que vira **outro insumo** (a maionese da casa que você produz e depois usa nos lanches) |
| **Ficha de consumo** | Configuração → Parâmetros | Papel impresso no PDV, nada a ver com custo |

---

## Antes de começar

Duas coisas precisam estar prontas, nesta ordem:

1. **Os insumos cadastrados**, com custo e unidade. A ficha técnica só **escolhe** insumos que já
   existem — ela não cadastra.
2. **O produto salvo.** Em produto novo, a aba mostra *"Salve o produto primeiro"*. Preencha o
   nome, salve, e a aba libera.

A ficha técnica é editada **no computador**. No celular ela existe, mas só para consulta.

---

## Parte 1 — Cadastrar os insumos

Vá em **Estoque → Meu Estoque → Insumos**. Essa é a sua despensa: tudo que entra num prato mora
aqui — carne, pão, queijo, molho, e também **embalagem**, que muita gente esquece.

![Lista de insumos](imagens-tratadas/01-insumos-lista.png)

| Nº | Item | O que observar |
|----|------|----------------|
| 1 | **+ Insumo** | Cadastra um insumo novo. |
| 2 | **Custo** | O que você paga pela **unidade inteira** do insumo: R$ 42,00 o quilo do blend, R$ 1,80 o pão. É esse valor que a ficha usa na conta. |
| 3 | **Sem controle / Controla estoque** | Quantos insumos têm controle de saldo ligado. Só os que controlam estoque aparecem nas movimentações da venda. |

Clique em **+ Insumo** e preencha. No exemplo, o alface (1):

![Cadastro do insumo](imagens-tratadas/02-insumo-cadastro.png)

| Nº | Campo | O que preencher |
|----|-------|-----------------|
| 1 | **Descrição \*** | O nome como você compra: *Alface*, *Blend bovino*, *Embalagem do lanche*. Até 100 caracteres. |
| 2 | **Custo (R$)** | O preço da **unidade de compra**: R$ 8,00 o quilo do alface. |
| 3 | **Unidade** | UN, KG, GR, L ou ML. **Use KG para o que se compra por peso e L para líquido** — a próxima seção explica por quê. |
| 4 | **SALVAR E SAIR (F2)** | Grava o insumo. |

Na aba **Estoque** você decide se quer acompanhar o saldo desse insumo:

![Aba Estoque do insumo](imagens-tratadas/03-insumo-estoque.png)

| Nº | Campo | O que fazer |
|----|-------|-------------|
| 1 | **Controlar Estoque** | **Ligue.** Sem isso o insumo entra na conta do custo, mas **não é baixado na venda** e não aparece nas movimentações. |
| 2 | **Estoque Mínimo** | Quantidade que dispara o alerta de estoque baixo. No alface, `0,5` (meio quilo). |
| 3 | **ALTERAR ESTOQUE** | Lança a quantidade que você tem hoje. É por aqui que entra a compra do fornecedor. |

### ⚠️ A conta da unidade: gramas ÷ 1000

O BeeFood **não converte unidade**. Se o insumo está em **KG**, a ficha é preenchida em **fração
de quilo** — e é aqui que mora o erro mais caro deste manual.

| Você usa na receita | Insumo em **KG**, digite | Insumo em **L**, digite |
|---------------------|-------------------------:|------------------------:|
| 1 quilo / 1 litro | `1` | `1` |
| 500 g / 500 ml | `0,5` | `0,5` |
| 200 g / 200 ml | `0,2` | `0,2` |
| 100 g / 100 ml | `0,1` | `0,1` |
| 50 g / 50 ml | `0,05` | `0,05` |
| 20 g / 20 ml | `0,02` | `0,02` |
| 5 g / 5 ml | `0,005` | `0,005` |
| 1 g / 1 ml | `0,001` | `0,001` |

> **Divida a grama por 1000 e pronto.** O tropeço clássico é escrever `0,05` querendo dizer 5 g —
> são **50 g**, dez vezes mais. O campo aceita **4 casas decimais**, então dá para chegar a
> `0,0001` (um décimo de grama), o que cobre até tempero.

O sistema também aceita cadastrar o insumo em **GR** ou **ML**, e aí a quantidade vai inteira
(`100` para 100 g). Só que o custo passa a ser por grama — R$ 0,042 em vez de R$ 42,00 o quilo —,
o que arredonda mal e não bate com a nota do fornecedor. **Prefira KG e L.**

---

## Parte 2 — Montar a ficha do lanche

Vá em **Cardápio → Produtos**, abra o lanche e clique na aba **Ficha Técnica**. Escolha o insumo
(1), diga a quantidade (2), confira a unidade (3) e clique em **Adicionar** (4).

![Adicionar insumo à ficha](imagens-tratadas/04-ficha-adicionar.png)

| Nº | Campo | O que fazer |
|----|-------|-------------|
| 1 | **Insumo** | Clique em *Buscar insumo…* e digite parte do nome. A lista mostra unidade e custo de cada um. |
| 2 | **Quantidade** | Quanto **entra em um lanche**. Alface: `0,01` — dez gramas. **Enter** já adiciona. |
| 3 | **Un.** | Preenche sozinho com a unidade do insumo. Não dá para trocar aqui. |
| 4 | **Adicionar** | Inclui a linha. O campo de busca reabre para você emendar o próximo. |

Repita para cada item, sem esquecer a embalagem. A ficha completa do **One Burger** fica assim:

![Ficha técnica completa](imagens-tratadas/05-ficha-completa.png)

| Nº | Coluna | O que ela diz |
|----|--------|---------------|
| 1 | **Quantidade** | `0,1` KG de blend = 100 g de carne no lanche. |
| 2 | **%** | Quanto aquele insumo pesa no custo do prato. O blend sozinho é **52%** — é nele que um aumento de fornecedor dói. |
| 3 | **Custo Total** | **R$ 8,08.** É o custo do lanche pronto, embalagem incluída. |

A conta, linha por linha:

| Insumo | Quantidade | Equivale a | Custo do insumo | Custo na ficha | % |
|--------|-----------:|------------|----------------:|---------------:|--:|
| Alface | 0,01 KG | 10 g | R$ 8,00 / kg | R$ 0,08 | 1,0% |
| Blend bovino | 0,1 KG | 100 g | R$ 42,00 / kg | R$ 4,20 | 52,0% |
| Embalagem do lanche | 1 UN | 1 caixa | R$ 0,90 | R$ 0,90 | 11,1% |
| Maionese da casa | 0,02 KG | 20 g | R$ 10,19 / kg | R$ 0,20 | 2,5% |
| Pão brioche | 1 UN | 1 pão | R$ 1,80 | R$ 1,80 | 22,3% |
| Queijo prato fatiado | 0,02 KG | 20 g | R$ 39,00 / kg | R$ 0,78 | 9,6% |
| Tomate | 0,02 KG | 20 g | R$ 6,00 / kg | R$ 0,12 | 1,5% |
| | | | **Custo Total** | **R$ 8,08** | 100% |

> Cada insumo entra **uma vez** na ficha. Se você tentar repetir, o sistema avisa: *"Este insumo já
> foi adicionado à ficha técnica"*. Precisa de mais carne? Aumente a quantidade da linha.

---

## Parte 3 — Ler o custo e a margem

Volte para a aba **Produto**. Os três campos de custo ficam lado a lado:

![Custos e margem na aba Produto](imagens-tratadas/06-produto-custos.png)

| Nº | Campo | O que significa |
|----|-------|-----------------|
| 1 | **Custo** | Campo **livre**, digitado à mão. Deixe em **R$ 0,00** quando você usa ficha técnica. |
| 2 | **Custo Ficha Técnica** | Só leitura: é o Custo Total da ficha, R$ 8,08. |
| 3 | **Custo Total** | **Custo + Custo Ficha Técnica.** |
| 4 | **Lucro e margem** | R$ 19,92 (71,1%) sobre o Preço de Venda de R$ 28,00. Verde é lucro, vermelho é prejuízo. |

> ⚠️ **Não preencha o Custo à mão se você já tem ficha técnica.** Os dois campos **somam**. Quem
> digita R$ 8,00 no Custo e ainda monta a ficha fica com um prato que "custa" R$ 16,08, e a margem
> sai errada para menos.

As contas que o sistema faz, passando o mouse na etiqueta:

- **Lucro = Venda − Custo total** → 28,00 − 8,08 = **R$ 19,92**
- **Margem = Lucro ÷ Venda × 100** → 19,92 ÷ 28,00 = **71,1%**

Repare que é **margem sobre a venda**, não markup sobre o custo. E ela não considera impostos,
taxa de marketplace nem despesa operacional — é o **lucro bruto** do prato.

---

## Parte 4 — A ficha do adicional

O adicional não faz parte da ficha do lanche: **ele tem ficha própria**. Faz sentido — o cliente
que pede carne extra consome carne extra. Vá em **Cardápio → Complementos**, abra o adicional e
use a mesma aba.

![Ficha do adicional Carne 100g](imagens-tratadas/07-ficha-adicional-carne.png)

| Nº | Item | O que observar |
|----|------|----------------|
| 1 | **Aba Ficha Técnica** | O complemento tem exatamente a mesma aba do produto. |
| 2 | **A linha** | 0,1 KG de blend = **R$ 4,20**. O adicional vende por R$ 9,00, então sobram R$ 4,80. |
| 3 | **Alterações afetam 4 Grupos de Opções** | O mesmo complemento é usado em vários lanches. Cadastre a ficha **uma vez** e ela vale em todos. |

O adicional de bacon segue a mesma ideia, com 30 g de bacon:

![Ficha do adicional Bacon](imagens-tratadas/08-ficha-adicional-bacon.png)

| Adicional | Ficha | Custo | Preço | Sobra |
|-----------|-------|------:|------:|------:|
| **Carne 100g** | Blend bovino 0,1 KG | R$ 4,20 | R$ 9,00 | R$ 4,80 |
| **Bacon** | Bacon em fatias 0,03 KG | R$ 1,02 | R$ 4,00 | R$ 2,98 |
| **Fatia de queijo** | Queijo prato 0,02 KG | R$ 0,78 | R$ 3,00 | R$ 2,22 |

> É por isso que vale cadastrar ficha nos adicionais mesmo quando dá trabalho: eles costumam ter a
> **melhor margem da casa**, e sem ficha essa carne some do estoque sem explicação.

---

## Parte 5 — A porção: granel, litro e embalagem

A porção mostra os três tipos de insumo numa ficha só:

![Ficha da porção](imagens-tratadas/09-ficha-porcao.png)

| Nº | Linha | O que ela ensina |
|----|-------|------------------|
| 1 | **Batata congelada 0,2 KG** | Granel: 200 gramas de um pacote comprado por quilo. |
| 2 | **Óleo de fritura 0,01 L** | Líquido: 10 ml por porção. Parece pouco, e é — R$ 0,09. Mas some no fim do mês. |
| 3 | **Custo Total R$ 2,54** | Contra R$ 14,00 de venda: margem de 82%. |

> **Vale lançar o óleo?** Vale, se você quer saber quando ele acaba. O custo dele é irrelevante no
> prato; o consumo, não.

---

## Parte 6 — Ver quem já tem ficha

Em **Estoque → Meu Estoque → Produtos** (e na aba **Complementos**) existe uma coluna que responde
a pergunta "o que ainda falta cadastrar?".

![Coluna Ficha Técnica](imagens-tratadas/10-estoque-coluna-ficha.png)

| Nº | Coluna | O que mostra |
|----|--------|--------------|
| 1 | **Ficha Técnica** | **Sim** ou **Não** para cada item do cardápio. |
| 2 | **Sim** | O One Burger já tem ficha. |
| 3 | **Custo** | R$ 8,08 — o custo vem da ficha, sem você digitar nada. |

Use o funil ao lado da busca para filtrar direto pelos que ainda estão em **Não**. É a lista de
trabalho de quem está cadastrando o cardápio inteiro.

---

## Parte 7 — A prova: vender e ver o estoque baixar

Ficha técnica só está certa quando você vê o estoque descer. Abra o **PDV** e monte um pedido.
No exemplo, um One Burger com **dois adicionais de carne** — o smash duplo:

![Pedido no PDV com dois adicionais](imagens-tratadas/11-pdv-dois-adicionais.png)

| Nº | Item | O que confere |
|----|------|---------------|
| 1 | **Adicionais 2/2** | O grupo permite até dois. |
| 2 | **Carne 100g com quantidade 2** | O mesmo adicional escolhido duas vezes. |
| 3 | **Adicionar ao carrinho — R$ 32,00** | R$ 14,00 do lanche + R$ 18,00 dos dois adicionais. |

Depois de **Receber (F3)**, vá em **Estoque → Movimentações**:

![Movimentações geradas pela venda](imagens-tratadas/12-movimentacoes-venda.png)

| Nº | Linha | O que ela prova |
|----|-------|-----------------|
| 1 | **Blend bovino −0,2** | Os **dois** adicionais: 0,1 KG cada. A descrição diz *"Venda de 2 One Burger -> Carne 100g -> Blend bovino"*. |
| 2 | **A descrição** | Ela mostra o caminho da baixa: **produto → adicional → insumo**. É assim que você audita de onde saiu cada grama. |
| 3 | **Blend bovino −0,1** | A carne do lanche em si, em linha separada. |

Somando as duas linhas, saíram **0,3 KG de blend** — exatamente os três hambúrgueres do pedido.
As outras linhas seguem a ficha: pão −1, alface −0,01, tomate −0,02, queijo −0,02 e embalagem −1.

**Três coisas que essa tela ensina:**

1. **A baixa acontece no Receber**, quando a venda é registrada — não é preciso esperar o
   pagamento.
2. **A quantidade multiplica.** Duas porções de batata frita geram duas baixas de 0,2 KG cada.
3. **Insumo sem controle de estoque não aparece.** A maionese da casa está na ficha e entra no
   custo, mas como o **Controlar Estoque** dela está desligado, ela não gerou movimentação. Se
   você quer acompanhar o consumo, ligue o controle (Parte 1).

---

## Parte 8 — Manter a ficha viva

Preço de fornecedor muda, receita muda. Duas edições resolvem quase tudo.

**Mudou a quantidade?** Clique no lápis da linha:

![Editar a quantidade de uma linha](imagens-tratadas/13-ficha-editar-linha.png)

| Nº | Item | O que fazer |
|----|------|-------------|
| 1 | **Campo da quantidade** | Digite o novo valor. **Enter** confirma. |
| 2 | **✓ e ✗** | O visto grava; o xis cancela. Não use **Esc**: ele fecha o modal inteiro. |

**Saiu do cardápio?** Clique na lixeira e confirme:

![Confirmação de remoção](imagens-tratadas/14-ficha-remover.png)

| Nº | Botão | O que faz |
|----|-------|-----------|
| 1 | **Sim, remover** | Tira o insumo da ficha. O Custo Total se recalcula na hora. |

**Mudou o preço de compra?** Aí você não mexe na ficha: altere o **Custo** do insumo em
**Meu Estoque → Insumos**. Todos os pratos que usam aquele insumo passam a valer o preço novo, de
uma vez. É o melhor motivo para cadastrar embalagem e molho como insumo em vez de "chutar" um
custo no produto.

---

## Insumo que vem de uma receita

Se você **produz** um insumo — maionese da casa, molho especial, massa —, ele pode ser criado em
**Estoque → Receitas**. Nesse caso o custo dele é calculado pela receita e aparece travado:

![Insumo com custo controlado pela receita](imagens-tratadas/15-insumo-receita.png)

| Nº | Item | O que significa |
|----|------|-----------------|
| 1 | **Custo cinza** | Não dá para digitar: quem manda é a receita. |
| 2 | **Custo controlado pela receita** | O nome da receita que gera esse insumo. |

Na ficha técnica ele é usado como qualquer outro. A vantagem é que, quando o preço do óleo ou do
ovo da maionese subir, o custo do lanche sobe junto, sozinho. Receitas e Produção são assunto de
outro manual.

---

## Limites que você precisa conhecer

| Limite | O que fazer |
|--------|-------------|
| **Não converte unidade** | Insumo em KG, quantidade em fração de quilo (o quadro da Parte 1). |
| **Não tem perda nem rendimento** | Se a carne perde 10% na chapa, cadastre a quantidade **crua** que sai do estoque, não a que chega ao prato. |
| **Não sugere preço** | O painel calcula margem; o preço de venda continua sendo decisão sua. |
| **Não repete insumo** | Um insumo, uma linha. Precisa de mais, aumente a quantidade. |
| **Não soma o custo dos adicionais no produto** | O lanche mostra R$ 8,08; os adicionais têm custo próprio. O custo do pedido montado é uma conta sua. |
| **Não edita no celular** | A aba abre para consulta e avisa para usar o computador. |

---

## Perguntas frequentes

**Preciso de ficha técnica para refrigerante em lata?**
Não necessariamente. Para revenda, é mais simples controlar o estoque **do próprio produto**, na
aba Estoque. A ficha compensa quando o item é **montado** a partir de outras coisas.

**Cadastrei a ficha e o Custo Total do produto continua zerado.**
Confira se a aba **Ficha Técnica** foi aberta com o produto **salvo** e se as linhas aparecem na
tabela. O campo **Custo Ficha Técnica** é só leitura e reflete o rodapé da ficha.

**A margem do produto está vermelha.**
O custo total ficou maior que o preço de venda. Duas causas comuns: preço de venda **R$ 0,00**
(produto cujo preço vem dos grupos de opções, como pizza montada por sabores) ou o campo **Custo**
preenchido à mão **junto** com a ficha.

**Por que o preço no PDV é diferente do Preço de Venda do cadastro?**
Porque o balcão pode ter preço próprio — preço presencial, promoção ou uma tabela de **Preço
Programado** ativa. A margem que o cadastro mostra usa sempre o **Preço de Venda**.

**Se eu cancelar a venda, os insumos voltam?**
Sim: aparece uma movimentação positiva, do mesmo insumo, devolvendo a quantidade.

**O estoque pode ficar negativo?**
Pode, se o insumo estiver com **Aceita Estoque Negativo** ligado. Desligue se quiser que o sistema
segure a venda.

**Cadastro a ficha no produto ou no complemento?**
No que **consome** o ingrediente. O que é do lanche vai no produto; o que só entra quando o cliente
pede vai no complemento.

---

## Resumo do exemplo

| Item | Ficha | Custo | Preço | Margem |
|------|-------|------:|------:|-------:|
| **One Burger** | 7 insumos | R$ 8,08 | R$ 28,00 | 71,1% |
| **Carne 100g** (adicional) | blend 0,1 KG | R$ 4,20 | R$ 9,00 | 53,3% |
| **Bacon** (adicional) | bacon 0,03 KG | R$ 1,02 | R$ 4,00 | 74,5% |
| **Batata frita** (porção) | 3 insumos | R$ 2,54 | R$ 14,00 | 81,9% |

---

## Manuais relacionados

| Manual | O que traz |
|--------|------------|
| **Cardápio — fundamentos** | Produto, complemento e grupo de opções: o cadastro que vem antes da ficha |
| **Cardápio — hambúrguer** | Como montar os grupos de adicionais usados neste manual |
| **Preço Programado** | Tabela que muda o preço em horários e canais específicos |
