# Produto só com agendamento (encomenda)

Bolo de festa, torta inteira, kit churrasco: tem item que a cozinha
não entrega em 30 minutos. Para esses, existe um interruptor no
**cadastro do produto** — **Somente agendamento**.

Ligado, o produto continua no cardápio digital, ganha a etiqueta
vermelha **Encomenda** e **não sai para agora**: quando o cliente
coloca esse item na sacola, o **pedido inteiro** vira agendado, mesmo
que ele tenha marcado **Hoje**.

Este manual é o complemento do **Agendamento do cardápio digital**.
Lá você define *quando* a loja aceita agendamento (dias, horários,
intervalos). Aqui você diz *quais produtos* só saem assim — e faz
isso em **lote**, sem abrir produto por produto.

---

## Antes de começar

1. O **Agendamento** da aba **Cardápio Digital → Agendamento**
   precisa estar **ligado**. É de lá que saem os dias e horários.
   **Com ele desligado a marca de encomenda não segura nada:** a
   etiqueta continua no cardápio, mas o botão **Agendar** desaparece e
   o cliente fecha o pedido para agora, como qualquer outro item.
2. Vale **só para o cardápio digital**, nas modalidades **Entrega** e
   **Retirada**. No presencial (mesa / QR Code) e no PDV o produto é
   vendido normalmente.
3. Para usar o **Editar em Lote** é preciso a permissão de **editar
   em lote** no seu grupo de acesso.
4. O cardápio do cliente pode levar **até 5 minutos** para mostrar a
   mudança.

O interruptor **não** deixa o produto inativo e **não** muda preço:
ele só troca a regra de entrega daquele item.

---

## Parte 1 — Os dois caminhos

O mesmo campo tem dois lugares:

| Caminho | Onde | Quando usar |
|---------|------|-------------|
| **Editar em Lote** | **Cardápio → Produtos → Editar em Lote** | Vários produtos de uma vez (todas as sobremesas, todos os bolos) |
| **Cadastro do produto** | **Cardápio → Produtos** → clique no produto → **Opções avançadas** | Um produto só |

O nome muda um pouco: no lote é **Somente Agendamento**; no cadastro,
**Somente agendamento (Cardápio Digital Delivery Entrega /
Retirada)**. É o mesmo campo.

> **Marque no produto, não no complemento.** O campo também aparece no
> **Editar em Lote** da aba **Complementos**, mas complemento não é
> vendido sozinho — ele entra no pedido como opção de um produto, e o
> cadastro dele nem tem esse interruptor. Quem manda na encomenda é o
> **produto**.

---

## Parte 2 — Marcar vários de uma vez

O exemplo deste manual: as **Sobremesas** da loja têm três pudins que
são feitos por encomenda, e um brownie que sai na hora. Só os pudins
devem virar encomenda.

**Filtre antes de abrir o assistente.** Clique no setor
**Sobremesas** (1) na coluna da esquerda e depois em **Editar em
Lote** (2). O assistente já abre com **essa** lista — é o que evita
marcar o cardápio inteiro sem perceber.

![Aba Produtos filtrada no setor Sobremesas](imagens-tratadas/01-lista-antes.png)

| Nº | Item | O que faz |
|----|------|-----------|
| 1. | Setor **Sobremesas** | Filtra a lista. O título passa a mostrar *Sobremesas · 4 produtos* |
| 2. | **Editar em Lote** | Abre o assistente de 3 etapas |

### Etapa 1 — escolher os produtos

**Todos já vêm marcados.** Desmarque o que não entra: aqui, o
**Brownie** (3). O contador (2) confirma *3 de 4 produtos
selecionados*.

![Editar em Lote — etapa 1, seleção dos três pudins](imagens-tratadas/02-lote-selecao.png)

| Nº | Item | O que fazer |
|----|------|-------------|
| 1. | **Todos os setores** / **Buscar por nome...** | Filtram dentro do assistente, se você não filtrou antes |
| 2. | Contador | Confira o número **antes** de seguir |
| 3. | Caixa do produto | Clique para desmarcar (aqui, o Brownie) |
| 4. | **PRÓXIMO** | Vai para a configuração |

> Se você filtrou dentro do assistente e ainda há itens marcados fora
> do filtro, o sistema pede confirmação antes de seguir: a edição vale
> para **todos os selecionados**, não só para os que estão na tela.

### Etapa 2 — ligar o Somente Agendamento

Nesta etapa **só o que você marcar é alterado**. O resto do cadastro
não é tocado.

Marque **Somente Agendamento** (1). Aparece um botão ao lado: deixe em
**Sim** (2). Depois, **PROCESSAR** (3).

![Editar em Lote — etapa 2, Somente Agendamento em Sim](imagens-tratadas/03-lote-campo.png)

| Nº | Campo | O que fazer |
|----|-------|-------------|
| 1. | Caixa **Somente Agendamento** | Marque para liberar o botão Sim / Não |
| 2. | **Sim** | **Sim** = só encomenda. **Não** = volta ao normal |
| 3. | **PROCESSAR (F2)** | Aplica em todos os selecionados |

> **É por aqui que se desfaz também.** Para tirar a marca de encomenda
> de um grupo de produtos, faça o mesmo caminho e deixe o botão em
> **Não**. Marcar o campo e esquecer o botão em **Não** desliga a
> encomenda dos produtos escolhidos — é o comportamento esperado, mas
> pega desprevenido quem só queria "conferir".

### Etapa 3 — conferir o resultado

O assistente processa em blocos e mostra linha por linha.

![Editar em Lote — etapa 3, três produtos atualizados](imagens-tratadas/04-lote-resultado.png)

| Nº | Item | O que confere |
|----|------|---------------|
| 1. | **Concluído — 3 de 3 produtos** | Todos foram processados |
| 2. | **3 sucesso** | Quantos deram certo; cada linha diz *Atualizado com sucesso* |
| 3. | **FECHAR (ESC)** | Fecha e atualiza a listagem |

Se algum produto falhar, a linha dele aparece em vermelho com o erro.
Repita o lote só para esse produto.

---

## Parte 3 — Como saber quais produtos estão marcados

Na lista de produtos, quem só sai por encomenda ganha um **ícone de
calendário azul** na linha de ícones do card (1). O Brownie, que
continua normal, não tem esse ícone (2).

![Lista de Sobremesas com o ícone de calendário nos pudins](imagens-tratadas/05-lista-depois.png)

| Nº | Item | O que indica |
|----|------|--------------|
| 1. | Calendário azul | *Aceita somente agendamento no cardápio digital* |
| 2. | Card sem o ícone | Produto normal, sai para agora |

Passe o mouse sobre o ícone para ver o texto. É a forma mais rápida de
auditar o cardápio depois de um lote grande.

---

## Parte 4 — Um produto só

Para um item isolado não vale abrir o assistente. Clique no produto,
abra **Opções avançadas** (1) na aba **Produto** e ligue **Somente
agendamento** (2).

![Cadastro do produto — Opções avançadas com o switch ligado](imagens-tratadas/06-produto-switch.png)

| Nº | Item | O que fazer |
|----|------|-------------|
| 1. | **Opções avançadas** | Clique para abrir a seção |
| 2. | **Somente agendamento** | Ligue. O texto abaixo já avisa: *ao adicioná-lo, o pedido inteiro será agendado* |
| 3. | **SALVAR E SAIR (F2)** | **Aqui existe botão de salvar.** Sem ele nada é gravado |

Diferença que vale lembrar: o **lote** grava ao clicar em
**PROCESSAR**; o **cadastro do produto** só grava em **SALVAR E
SAIR**.

---

## Parte 5 — O que o cliente vê

Marcado no painel, o produto ganha a etiqueta **Encomenda** no
cardápio digital. Ele continua na vitrine, com preço e foto.

![Somente Agendamento no painel → etiqueta Encomenda no cardápio](imagens-tratadas/07-par-encomenda.png)

No celular, o caminho é este: (1) a etiqueta na lista, (2) o **?** ao
lado dela explica — *Produto disponível apenas por agendamento* —, e
(3) ao tocar **Continuar** na sacola o cardápio abre sozinho a tela
**AGENDAR PEDIDO**.

![Cardápio digital: etiqueta, explicação e a tela AGENDAR PEDIDO](imagens-tratadas/08-cardapio-digital.png)

| Nº | O que o cliente vê |
|----|--------------------|
| 1. | **Encomenda** — etiqueta vermelha com o ícone de calendário |
| 2. | **Mais informações** — *Produto disponível apenas por agendamento* |
| 3. | **AGENDAR PEDIDO** — abre ao continuar, com a faixa **Dia** e a **Hora Aproximada** |

**O detalhe mais importante:** o botão **Hoje** continua na tela da
retirada e o cliente pode até deixá-lo marcado. Não muda nada. Como
existe um item de encomenda na sacola, ao tocar **Continuar** o
cardápio pula para o agendamento e só libera o pagamento depois que o
cliente escolher **dia e hora**. Com um produto normal, o mesmo
**Continuar** vai direto para as formas de pagamento.

Os dias e horários que aparecem ali **não** são deste manual: saem da
aba **Agendamento** (mínimo e máximo de dias, intervalo, limite por
faixa) cruzada com o **Horário de Atendimento**. No exemplo, o mínimo
de 2 dias é o que faz a lista começar em **QUA 02**.

---

## Problemas comuns

| Sintoma | O que verificar |
|---------|-----------------|
| Marquei e o cardápio não mudou | Espere **5 minutos** e recarregue |
| A etiqueta **Encomenda** aparece, mas o pedido sai para agora | O **Agendamento** da aba está desligado. Ligue: sem ele não existe botão **Agendar** |
| Não aparece nenhum horário para escolher | A grade de **Horário de Atendimento** não tem faixa disponível nos dias permitidos pelo mínimo / máximo de dias |
| Cliente pede o produto para agora | O item não está marcado. Confira o ícone de calendário na lista |
| Marquei o setor errado | Refaça o lote com o campo em **Não** |
| O lote não deixa clicar **PROCESSAR** | Nenhum campo foi marcado na etapa 2 |
| Sumiu o campo **Somente Agendamento** do lote | Falta permissão de **editar** no grupo de acesso |
| No presencial o produto sai na hora | Correto. A regra é só do cardápio digital (Entrega / Retirada) |
| Liguei no cadastro e não gravou | Faltou **SALVAR E SAIR (F2)** |

---

## O que este campo não é

- **Só aceita agendamento** (aba **Cardápio Digital →
  Agendamento**): aquele desliga o pedido imediato da **loja
  inteira**. Este vale **item a item**.
- **Exibir / Ocultar:** esconde o produto em certos dias e horários.
  A encomenda não esconde nada — o produto continua visível.
- **Estoque:** produto sem estoque some ou bloqueia. Encomenda não
  mexe em quantidade.
- **Preço Programado:** muda o preço por período, não a regra de
  entrega.

---

*Última atualização: agosto/2026 — BeeFood · Produto só com agendamento*
