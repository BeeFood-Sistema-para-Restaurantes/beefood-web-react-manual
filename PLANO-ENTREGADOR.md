# Estudo — bloco do Entregador (taxa de entrega, pagamento e relatórios)

> Estudo pedido pelo dono em **05/09/2026**: *"quero um plano completo sobre entregador — manual 1
> cadastro entregador (com diária); manual 2 cadastro taxa de entrega na área de entrega (bem
> rápido e básico) + venda mostrando (são 3 áreas, mostre um exemplo de cada configuração, bairro,
> cep, mapa área e por km); manual 3 relatórios taxa de entrega do entregador + impressos (caixa e
> desempenho). Estude isso e valide se estou certo, ou temos algo a mais pra fazer."*
>
> **Resposta curta: a divisão em três está certa, mas dois escopos precisam mudar.** O manual 2,
> como foi descrito, **já existe quatro vezes** (#35–#38) — inclusive com a imagem do cardápio
    10|> mostrando a taxa. O manual 1 esbarra num furo do produto: **não existe tela para lançar a
> diária**. E o manual 3 é maior do que parece: são **duas telas, três modos de cálculo e três
> impressos**. Fora do pedido, sobrou uma tela inteira sem manual: a **Gestão de Entregas**.

Status: ⏳ **aguardando aprovação.** Proposta: manuais **#83, #84 e #85**, mais dois candidatos
para depois.

---

## 1. Resumo em cinco linhas

    20|O dinheiro da entrega tem **dois lados independentes** no BeeFood: a **taxa que o cliente paga**
(`Taxa de Entrega`, cadastrada na Área de Entrega) e o **valor que o entregador recebe**
(`Valor pago ao entregador`, cadastrado na mesma tela mas em outro campo — e que o cliente nunca
vê). O cadastro do entregador é um **funcionário** com a função *Entregador*, que tem dois campos
próprios de pagamento: **Valor Diária (R$)** e **Valor por KM (R$)**. No fim do mês, quem fecha a
conta é o relatório **Desempenho → Delivery → Entregador (Taxa / KM)**, que escolhe **qual dos
três critérios** usar, e o **Caixa → Resumo Frete**, que faz a mesma conta no escopo de um caixa.

---

    30|## 2. Como este estudo foi feito

| Fonte | O que rendeu |
|-------|--------------|
| `beefood-web-react` (clone de leitura) | Cadastro de funcionário, área de entrega, venda, despacho, caixa |
| `beefood-reports-hub` (clone de leitura) | O relatório do entregador e os impressos do Desempenho |
| API autenticada do sandbox (somente leitura) | Estado real: funcionários, as quatro áreas, o relatório e o caixa |
| Manuais já publicados | O que já está coberto (e o que ficou de fora) |

Nada foi alterado no ambiente.

    40|---

## 3. Validando o pedido, item a item

### Manual 1 — cadastro do entregador (com diária): **certo, com um furo pra resolver**

O cadastro é em **Cadastros → Funcionários** (não existe tela "Entregadores"; existe um **card de
filtro** chamado *Entregadores* na listagem). A função é escolhida na aba **Função**, num seletor
de **três opções mutuamente exclusivas**: **Garçom**, **Entregador**, **Outra Função**.

Marcando **Entregador**, aparecem exatamente dois campos:
    50|
| Campo | Unidade | Texto de ajuda na tela |
|-------|---------|------------------------|
| **Valor Diária (R$)** | R$ fixo | *"Valor fixo pago por diária trabalhada"* |
| **Valor por KM (R$)** | R$ por km | *"Valor pago por quilômetro rodado"* |

> **Comissão (%) não existe para entregador** — é campo exclusivo do Garçom. E trocar a função
> **zera** os campos da função anterior.

**O furo:** não achei, em nenhum lugar do painel, uma tela para **lançar a diária do dia** (marcar
que o entregador trabalhou hoje). O campo do cadastro é só o **valor**; as linhas de diária
    60|aparecem no relatório vindas do servidor (`qtdD` / `valorD`). No sandbox, **as diárias estão
zeradas em todos os 6 entregadores com movimento** — ou seja, nunca foi lançada nenhuma. Sem saber
como se lança, o manual 1 consegue explicar o campo, mas **não consegue mostrar a diária
funcionando** — e o relatório do manual 3 sai sem a coluna que mais interessa. **É a pergunta 1 da
seção 8.**

O que o **#57 (BeeFood Entregador)** já cobre: o passo *"Cadastrar o funcionário como Entregador"*,
com a frase *"Diária e valor por KM são opcionais (só para o seu controle)"*. O manual novo precisa
ir além disso — explicar **o que cada valor faz no relatório** — e não repetir o vínculo com o app
(usuário + switch Aplicativos + código de barras), que é do #57.

    70|### Manual 2 — taxa de entrega na área: **já existe, e não são 3 áreas**

Dois problemas no escopo como foi descrito:

**Primeiro: já está publicado, quatro vezes.**

| Manual | Modo | Já mostra a taxa no cardápio? |
|--------|------|------------------------------|
| **#35** `area-entrega-mapa` | Raio/Área (círculo e polígono) | Sim — busca, formulário e taxa |
| **#36** `area-entrega-km` | Quilometragem KM | Sim — *"Cardápio — endereço confirmado, taxa R$ 5,99"* |
| **#37** `area-entrega-bairro` | Bairro | Sim |
    80|| **#38** `area-entrega-cep-fixo` | CEP Único | Sim |

O #36 até já explica o campo do entregador: *"Valor pago ao Entregador — só no relatório Resumo
Taxa Entrega — o cliente não vê"*. E o **#34** (`endereco-restaurante`) é o pré-requisito dos
quatro. Refazer isso seria duplicar cinco manuais.

**Segundo: são quatro modos, e seis configurações.** O passo 2 da Área de Entrega tem **quatro
cards**: **Quilometragem KM**, **Raio/Área**, **Bairro e CEP** e **CEP Único**. Dentro de
*Bairro e CEP* existem **três subtipos** (**Bairro**, **CEP**, **Faixa CEP**) e dentro de
*Raio/Área* existem **dois desenhos** (**Círculo** e **Polígono**).

    90|| O que você chamou de | No sistema é | Manual existente |
|----------------------|--------------|------------------|
| bairro | *Bairro e CEP* → subtipo **Bairro** | #37 |
| cep | **dois lugares diferentes**: *CEP Único* (modo próprio) **e** *Bairro e CEP* → subtipos **CEP** e **Faixa CEP** | #38 cobre só o **CEP Único** |
| mapa área | *Raio/Área* → **Círculo** ou **Polígono** | #35 |
| por km | *Quilometragem KM* | #36 |

Ou seja: **falta manual do CEP e da Faixa de CEP** dentro de *Bairro e CEP* — o único dos seis que
ninguém documentou.

**O que realmente falta e vale um manual:** o caminho da taxa **depois** que ela sai do cadastro.
   100|Nenhum dos cinco manuais mostra que:

- a taxa aparece na venda como **Taxa de Entrega (+)**, e o operador pode **alterá-la** por três
  caminhos: o campo **Taxa de Entrega** no modal de endereço (com o botão **Calcular Taxa**), o
  modal **Editar Taxa de Entrega** no PDV, e o modal **Editar Valores Financeiros** na venda
  aberta;
- o modal de endereço tem também o campo **Valor Entregador**, que o operador pode editar **antes
  de salvar** o pedido;
- o sistema guarda o valor anterior a cada alteração (`taxaEntregaAnterior`);
- **frete grátis** é por faixa/bairro/região (**Frete grátis acima de**), e o **pedido mínimo** da
  loja é outra coisa, em Cardápio Digital → Configurações.
   110|
**Proposta para o manual 2:** virar um manual **curto de decisão + a taxa na venda**, que serve de
porta de entrada para os quatro que já existem, e que cobre o buraco do CEP/Faixa de CEP. Detalhe
na seção 5.

### Manual 3 — relatórios e impressos: **certo, e maior do que parece**

São **duas telas**, não uma:

**A) Desempenho → Delivery → Entregador (Taxa / KM)** — a tela de fechar a conta do mês.

   120|Três modos de cálculo, num seletor de rádio (o rótulo é exatamente este):

| Opção | O que soma |
|-------|-----------|
| **Valor da taxa paga pelo cliente** | Coluna **Taxa Cliente** |
| **Valor do entregador configurado na área de atendimento** | Coluna **Taxa Entregador** |
| **Valor pago por KM configurado no cadastro de funcionário** | Colunas **KM (Ida)** e, com ida e volta, **KM (Volta)** e **KM (I+V)** |

Mais o checkbox **Pagar KM de ida e volta**, que dobra as colunas. Cinco cartões no topo
(**Total Entregas**, **KM Total**, **Taxa Cliente Total**, **Taxa Entregador Total**, **Diárias**),
duas abas (**Resumo por Entregador** e **Todos os Detalhes**) e um **drill-down** por entregador
   130|com seis cartões, o card **Diárias registradas** e a lista de entregas. A escolha do modo e do
ida-e-volta fica **salva no navegador**.

**B) Caixa → Ver Caixa → seletor Resumo → Resumo Frete** — a mesma conta, no escopo de **um
caixa**. Aqui os três modos são botões curtos (**Cliente**, **Entreg.**, **KM**), o checkbox é
**Pagar ida e volta**, e existe uma diferença que vale aviso no manual: **o caixa não mostra as
colunas de diária**; o Desempenho mostra.

**Impressos (três, mais o Excel):**

| Onde | Botão | Formato | Detalhe |
|------|-------|---------|---------|
   140|| Desempenho | **Imprimir A4** | A4 | Cabeçalho com **Período** e **Cálculo:** (o modo escolhido) + **Ida e volta: Sim/Não**; seções por entregador; **RESUMO POR ENTREGADOR**; **TOTAIS GERAIS** com a linha **TOTAL A PAGAR** |
| Desempenho | **Imprimir Cupom** | Bobina 80 mm | Abre um **painel de configuração** com 7 opções (**Somente resumo por entregador**, **Incluir endereço**, **Incluir venda/pedido**, **Incluir KM**, **Incluir diárias**, **Resumo consolidado no final**, **Cabeçalho com período e filtros**), duas ordenações e a seleção de entregadores. Imprime pelo **navegador** ou pelo **servidor** (BeeImpressão) |
| Desempenho | **Excel** | `.xlsx` | Download direto |
| Caixa | **Imprimir Resumo** | Bobina 80 mm | Título muda com o modo: **RESUMO FRETE - TAXA CLIENTE** / **- TAXA ENTREGADOR** / **- KM ENTREGADOR** |

**Um terceiro lugar que o pedido não previa:** **Desempenho → Vendas → Resumo** tem uma grade
**Entregador** com as colunas **Qtd**, **Valor Entregador** e **Valor Frete** — e o filtro de
**Entregador** por venda. Vale uma seção curta no manual 3, porque é onde o gerente compara *o que
entrou de frete* com *o que saiu para o entregador*.

   150|---

## 4. O que falta e você não pediu

Três coisas apareceram no estudo e não estão em nenhum manual:

**1. Gestão de Entregas — uma tela inteira, sem manual.** Rota própria (`/gestao-entregas`), com
painel de rotas, **posições dos entregadores no mapa** (atualiza a cada 10 s), criação de rota com
vários pedidos, **ModalTrocarEntregador** (com os selos **Online**, **Offline**, **Sem app**,
**Nunca usou o app**), **despachar**, **finalizar** e um **Despacho Automático** configurável.
É o maior buraco do bloco e provavelmente rende **um ou dois manuais** próprios.
   160|
**2. Despachar o entregador próprio no Delivery.** O botão **Adicionar Entregador** / **Alterar
Entregador do Pedido #N**, o modal com duas colunas (**Entrega Terceirizada** × **Entregadores
Próprios**), o despacho **em lote** e o **CONFIRMAR E ALTERAR SITUAÇÃO**. Os manuais #59–#63
cobrem as **terceirizadas**; o entregador **próprio** ficou sem passo a passo.

**3. O lápis do "Valor do entregador" na venda.** No detalhe do pedido aparece
**Valor do entregador: Não definido** com um lápis que abre **edição na própria linha** (não é
modal). É por aí que se corrige o pagamento de um pedido específico — e ninguém documentou.

Achado que vale aviso em manual (e talvez conversa de produto): no relatório do sandbox existe a
   170|linha **"Sem entregador"** com **16 entregas** e **R$ 19,00 de taxa de entregador acumulada**. Ou
seja: a taxa do entregador é calculada pela **área de entrega**, mesmo quando ninguém foi
despachado — e o dinheiro fica somado num entregador que não existe.

---

## 5. Proposta final: três manuais (e dois candidatos)

### #83 — Cadastrar o entregador e definir o pagamento dele

   180|| Seção | Conteúdo | Imagens |
|-------|----------|--------:|
| 1 | Os dois lados do dinheiro da entrega (taxa do cliente × valor do entregador) — a tabela que abre o bloco | — |
| 2 | Onde fica: **Cadastros → Funcionários**, o card de filtro **Entregadores** e a coluna **Função** | 2 |
| 3 | Cadastrar: aba **Dados** (o que é obrigatório de verdade) | 2 |
| 4 | Aba **Função**: os três tipos, e por que trocar de tipo apaga o valor do anterior | 2 |
| 5 | **Valor Diária (R$)** e **Valor por KM (R$)**: o que cada um significa e **em qual relatório aparece** | 2 |
| 6 | Onde o valor por entrega é definido (área de entrega) e onde se corrige por pedido (o lápis na venda) | 2 |
| 7 | Ligar o entregador ao app — **remissivo ao #57**, sem repetir o passo a passo | — |
| 8 | Exemplo prático: cadastrar o entregador, dar diária e KM, despachar um pedido e ver o valor na venda | 2 |
   190|
**Total: 10 a 12 imagens.** Depende da resposta da pergunta 1 (diária).

### #84 — Taxa de entrega: qual modo usar, onde digitar e como ela cai na venda

Manual **curto e de decisão**, sem refazer os #35–#38.

| Seção | Conteúdo | Imagens |
|-------|----------|--------:|
| 1 | A tabela de decisão: os **quatro modos** e as **seis configurações**, com "use este quando…" e o link para o manual de cada um | 1 |
| 2 | Onde se digita a taxa em cada modo (quadro com os rótulos exatos: **Valor do frete**, **Valor frete**, **Taxa entrega (R$)**, **CEP Fixo Valor Frete**) | 4 recortes |
   200|| 3 | **CEP e Faixa de CEP** (o que falta manual): o modal, os subtipos e a validação de 8 dígitos | 2 |
| 4 | **Frete grátis acima de** × **pedido mínimo** da loja — não são a mesma coisa | 1 |
| 5 | **Valor pago ao entregador**: mesmo modal, outro campo, e o cliente não vê | 1 |
| 6 | A taxa na venda: **Taxa de Entrega (+)**, o **Calcular Taxa** do modal de endereço e os três jeitos de alterar | 3 |
| 7 | Exemplo prático: um pedido em cada configuração, com a taxa que o cliente vê e a que entra na venda | 2 a 4 |

**Total: 12 a 15 imagens.** O exemplo prático exige **trocar o modo ativo** da loja quatro vezes
(hoje o ativo é **Bairro e CEP**) — ver riscos na seção 7.

### #85 — Relatórios da taxa de entrega e do entregador (Desempenho e Caixa)
   210|
| Seção | Conteúdo | Imagens |
|-------|----------|--------:|
| 1 | Qual relatório usar para quê (Desempenho = período; Caixa = um caixa) | — |
| 2 | **Desempenho → Delivery → Entregador (Taxa / KM)**: a tela, os cinco cartões e as duas abas | 2 |
| 3 | Os **três modos de cálculo** e o **Pagar KM de ida e volta** — um recorte da tabela em cada modo | 3 |
| 4 | O drill-down de um entregador (seis cartões, **Diárias registradas**, lista de entregas) | 2 |
| 5 | **Imprimir A4**: o que sai, com destaque no **TOTAL A PAGAR** | 2 |
| 6 | **Imprimir Cupom**: o painel de 7 opções e a escolha navegador × servidor | 2 |
| 7 | **Caixa → Resumo Frete**: como chegar, os três botões, o **TOTAL** e o impresso 80 mm | 3 |
   220|| 8 | **Desempenho → Vendas → Resumo**, grade **Entregador** (frete que entrou × valor que saiu) | 1 |
| 9 | Exemplo prático: fechar o pagamento do mês de um entregador e imprimir o comprovante | 2 |

**Total: 15 a 18 imagens.**

### Candidatos para depois (fora deste bloco)

| Candidato | Por que | Tamanho |
|-----------|---------|---------|
| **Gestão de Entregas** | Tela inteira sem manual: rotas, mapa ao vivo, despacho automático | 1 a 2 manuais |
| **Despachar entregador no Delivery** | O passo a passo do entregador próprio, em lote e com troca de situação | 1 manual |
   230|
---

## 6. Estado do sandbox — dá para produzir?

| Item | Situação | Efeito no plano |
|------|----------|-----------------|
| Funcionários | 12, sendo **8 marcados como Entregador** | Ok, mas quase todos são das integrações (*99 Entrega*, *Machine*, *Uber Direct*, *Husky Sandbox*) |
| **Valor Diária / Valor por KM** | **null em todos os 8** | Preciso cadastrar um entregador de verdade para o #83 |
| Área de Entrega — modo ativo | **Bairro e CEP** | Trocar o ativo é o que permite o exemplo de cada modo no #84 |
   240|| Área por **KM** | 3 faixas: 3 km R$ 5,99 · 6 km R$ 8,99 · 10 km R$ 14,99, com entregador R$ 3 / R$ 5 / R$ 8 | Pronto para fotografar |
| Área por **Mapa** | 3 regiões: *Campolim* (polígono, R$ 7,90), *Até 2 km* (círculo, R$ 5,99), *Zona industrial* (sem valor) | Pronto — e a terceira serve de exemplo de **não entrega** |
| Área por **Bairro** | 1 grupo: R$ 6,50, frete grátis acima de R$ 45, entregador R$ 3,50 | Pronto |
| **CEP Único** | CEP 18035490, R$ 7,00 | Pronto |
| **CEP / Faixa de CEP** | **não existe nenhum cadastrado** | Preciso criar para o #84 |
| Relatório do entregador (01/08–05/09) | **41 entregas, 6 entregadores** | Pronto para o #85 |
| Colunas de **KM (Ida/Volta)** | **vazias** (nenhum funcionário tem Valor por KM) | Cadastrar o KM resolve — e é a validação da pergunta 2 |
| Colunas de **Diária** | **vazias** em tudo | Depende da pergunta 1 |
| Caixa para o Resumo Frete | **Caixa 967508** (fechado em 01/09) tem **12 entregas e 5 entregadores** | Melhor caixa para o #85 |
   250|| Caixa aberto (983507) | 1 entrega, *Sem entregador* | Serve para mostrar o caixa "do dia" |

---

## 7. Riscos da produção

1. **Trocar o modo ativo da Área de Entrega mexe no cardápio público.** Hoje a loja está em
   **Bairro e CEP**. Para o exemplo prático do #84 é preciso ativar cada modo, fotografar e voltar
   ao original. Trocar o tipo **não apaga** os cadastros dos outros, e o cardápio leva **1 a 2
   minutos** para refletir — foi assim nos #35–#38.
2. **Cadastrar diária e valor por KM altera o cálculo do relatório** daquele entregador. É
   reversível (zerar os campos), mas muda números que aparecem em outros relatórios.
   260|3. **O relatório do Desempenho abre num iframe** (`relatorios.beefood.com.br`) dentro do painel.
   A captura precisa considerar isso; o `beefood-reports-hub` roda local com um `?auth` gerado
   pelo `beecripto`, o que ajuda a **entender** a tela, mas o manual deve ser capturado no
   ambiente real.
4. **Impressão pelo servidor (BeeImpressão) não existe no Cloud Agent.** Os impressos serão
   capturados pelo caminho **navegador** (iframe oculto), como no cupom do #74.
5. **Nada de pedido novo sem necessidade.** As 41 entregas já existentes bastam para o #85; o #83
   e o #84 precisam de **um** pedido de exemplo cada.

---
   270|
## 8. Perguntas para o dono

1. **Como se lança a diária de um entregador?** Não achei tela no painel. É pelo app do
   entregador, por outro sistema, direto no banco, ou é um recurso que ainda não existe? Sem isso,
   o #83 explica o campo mas não mostra o efeito, e o #85 sai sem a coluna de diária.
2. **Posso cadastrar diária e valor por KM num entregador do sandbox** (por exemplo o
   *Funcionário 1*) para provar o efeito nas colunas **KM (Ida)** e **Valor Diária**?
3. **Concorda em trocar o escopo do manual 2** (decisão + CEP/Faixa de CEP + a taxa na venda), em
   vez de refazer o que os #35–#38 já cobrem?
   280|4. **Posso trocar o modo ativo da Área de Entrega** durante a captura, voltando para *Bairro e
   CEP* no fim?
5. **A Gestão de Entregas entra na fila agora** (como #86) ou fica para depois?
6. Existe algum critério de negócio que eu não deva contradizer no manual: o entregador é pago
   **por entrega**, **por KM**, **por diária** ou uma combinação? O relatório permite os três, e o
   manual precisa dizer qual é a recomendação da BeeFood.

---

## 9. Roteiro de captura (quando aprovado)
   290|
- **#83:** criar o entregador *Entregador Manual* com **Valor Diária R$ 60,00** e
  **Valor por KM R$ 1,50**; despachar um pedido para ele; editar o **Valor do entregador** pelo
  lápis; conferir no relatório.
- **#84:** um recorte do campo de taxa em cada um dos quatro modos (já cadastrados); criar um
  grupo de **CEP** e um de **Faixa CEP**; ativar cada modo e capturar a sacola do cardápio com a
  taxa; abrir a venda e mostrar **Taxa de Entrega (+)** e os três caminhos de alteração.
- **#85:** período **01/08 a 05/09** no Desempenho (41 entregas); os três modos de cálculo com e
  sem ida e volta; drill-down do *99 Entrega* (6 entregas); **Imprimir A4** e **Imprimir Cupom**
  capturados pelo iframe oculto; **Caixa 967508 → Resumo Frete** nos três botões + impresso.
   300|
Vale a regra permanente da `MEMORIA-GERAL.md` (esperar o spinner sumir + 5 s) e, para telas de
venda, os **14 segundos** que o #79 mediu.
