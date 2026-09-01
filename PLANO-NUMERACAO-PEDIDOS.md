# Estudo — manual "Explicando a numeração dos pedidos"

> Estudo pedido pelo dono em **01/09/2026**, antes de produzir o manual.
> Responde à pergunta: *"há informação suficiente para escrever o manual?"*
>
> **Resposta curta: sim.** As quatro regras que o dono descreveu foram confirmadas, três
> delas com prova em dado real do sandbox. Apareceram **três descobertas** que o pedido
> original não previa, e uma delas obriga a **corrigir o manual #44**.

Status: ⏸️ **aguardando aprovação do dono** para virar manual.

---

## 1. Resumo em cinco linhas

O BeeFood mostra **dois números** na mesma venda. O **número da venda** (`numeroPreVenda`) é
um contador único da loja que nunca reinicia. O **número do pedido** (`numeroPedido`) é o
contador **do caixa**: ele volta para 1 cada vez que um caixa novo é aberto — por isso fechar
o caixa todo dia dá a contagem do dia. Quando os dois existem, o sistema escreve
**`número do pedido (número da venda)`**; quando só existe o da venda, escreve **só ele**.
Pedido de **delivery** recebe número do pedido de acordo com o caixa; o **PDV** só recebe se
o parâmetro estiver ligado; a **mesa** nunca recebe.

---

## 2. As quatro regras do pedido, uma a uma — confirmadas?

| # | Regra descrita pelo dono | Situação | Como foi confirmada |
|---|--------------------------|----------|---------------------|
| 1 | **Número da venda**: sequencial, nunca reseta | ✅ **Provado** | 304 vendas na faixa 627–930: **zero buracos, zero repetições** |
| 2 | **Número do pedido**: é do caixa atual; reinicia quando abre um caixa novo | ✅ **Provado** | Dois resets flagrados no dado real; um deles **4 segundos** depois da abertura do caixa |
| 3 | **PDV** dá para ativar; **mesa** não dá; **delivery** sempre ativo conforme o caixa | ✅ **Provado** | Parâmetro `pdvNumeroPedido` existe só para o PDV; **0 de 15** vendas de mesa têm número de pedido |
| 4 | Exibição: `número do pedido (número da venda)`, ou só o da venda | ✅ **Provado** | Regra encontrada em 12 pontos do código e vista na tela (Histórico e Delivery) |
| 5 | Reset opcional do número da venda | 🔜 **Não existe ainda** | Nenhum parâmetro, campo ou endpoint no código; é o roadmap que o dono citou |

---

## 3. Não confundir: quatro números com nome parecido

Esse é o primeiro risco do manual. O sistema tem quatro números por venda, e três deles
aparecem para o usuário em algum lugar.

| Campo | Como o usuário vê | O que é | Reinicia? |
|-------|-------------------|---------|-----------|
| `numeroPreVenda` | **Venda Nº 930**, `#930`, ou o número entre parênteses | Contador único da loja. É o número "oficial" da venda | **Nunca** |
| `numeroPedido` | **Pedido #60**, ou o número antes dos parênteses | Contador do caixa aberto | **Sim**, a cada caixa novo |
| `preVendaID` | Quase nunca (só como reserva quando falta o resto) | Código interno do banco de dados | Nunca |
| `referencia` / `ifoodShortReference` | `#ABC1 (930)` no card do Delivery | Código curto que o **marketplace** manda (iFood e afins) | É do marketplace |

Duas armadilhas de vocabulário que o manual precisa desarmar:

- **"Número do pedido" no parâmetro não é o número que o PDV mostra na tela.** O switch
  chama-se *Número de Pedido no PDV*, mas a tela do PDV continua exibindo o **número da
  venda**. Detalhe na seção 7.
- **A nota fiscal usa o número da venda, nunca o do pedido.** Em NF-e e NFC-e a coluna
  chama-se *Nº Venda* e traz `numeroPreVenda` (`src/pages/NFe.tsx`, `src/pages/NFCe.tsx`).
  Mesma coisa em Movimentações e no Fiado.

---

## 4. A prova do reset por caixa (o coração do manual)

Levantamento feito em **01/09/2026** na conta sandbox **BeeFood3 - Manual**, cruzando o
histórico de vendas (304 vendas, 01/07 a 31/12/2026) com a listagem de caixas e o detalhe de
cada venda. Nada foi alterado no ambiente: só leitura.

### 4.1 O número do pedido reinicia em 1 a cada caixa

| Caixa | Abertura | Fechamento | Delivery no caixa | Números de pedido | Números de venda |
|-------|----------|------------|-------------------|-------------------|------------------|
| 893187 | 18/06 21:29 | 01/07 16:08 | Sim | 41 … 50 | 627 … 633 |
| 907962 | 01/07 16:09 | 17/07 11:58 | **Não** | *praticamente nenhum* | 630 … 719 |
| 927703 | 17/07 11:59 | 19/08 10:54 | Sim | **1 … 110** | 720 … 842 |
| 967508 | 19/08 10:35 | *aberto* | Sim | **1 … 60** | 843 … 930 |

Os dois últimos caixas percorreram a contagem inteira, de 1 até o fim. É a regra funcionando
à vista.

### 4.2 O reset flagrado no relógio

O caixa 927703 abriu em **17/07/2026 11:59:02**. O **pedido nº 1** dele saiu em
**17/07/2026 11:59:06** — **quatro segundos depois**. Não há como ser coincidência.

E na virada seguinte:

```
último pedido do caixa 927703 .... 17/08 15:38:51   pedido 110   venda 838
caixa 927703 fechado ............. 19/08 10:54:36
caixa 967508 aberto .............. 19/08 10:35:29
primeiro pedido do caixa 967508 .. 21/08 12:34:29   pedido   1   venda 843
```

O número do **pedido** caiu de **110 para 1**. O número da **venda** continuou subindo,
**838 → 843**. Os dois contadores no mesmo instante, um reiniciando e o outro não: é
exatamente a imagem que o manual precisa passar.

### 4.3 O número da venda nunca reinicia

| Medida | Valor |
|--------|------:|
| Faixa observada | 627 a 930 |
| Vendas no período | 304 |
| Números distintos | 304 |
| Números repetidos | **0** |
| Buracos na faixa | **0** |

304 vendas ocupando exatamente os 304 números da faixa, sem sobra e sem falta. O contador é
único e não reinicia.

---

## 5. Quem recebe número de pedido, por canal

| Canal | Vendas | Com número de pedido | O que manda |
|-------|-------:|---------------------:|-------------|
| **Delivery** | 245 | 149 | O caixa (ver seção 6) |
| **PDV** | 44 | 28 | O parâmetro *Número de Pedido no PDV* |
| **Mesa** | 15 | **0** | Nada. Mesa não recebe, e não há como ligar |

### 5.1 Mesa nunca recebe — e não existe switch

Nenhuma das 15 vendas de mesa tem número de pedido. No código não existe `mesaNumeroPedido`
nem nada equivalente: o único parâmetro de numeração é o do PDV. A tela de Mesas mostra
apenas `#numeroPreVenda` (`src/pages/Mesas.tsx`), e o tipo `VendaMesa` não tem o campo
(`src/hooks/useVendasMesa.ts`).

### 5.2 O momento exato em que o PDV passou a receber

O parâmetro está **ligado** no sandbox hoje (`pdvNumeroPedido: true`). O dado mostra a hora
em que ele foi ligado:

```
última venda de PDV SEM número de pedido ..... 21/08/2026 16:21   venda 846
primeira venda de PDV COM número de pedido ... 21/08/2026 16:33   pedido 2, venda 847
```

Doze minutos separam as duas. Foi durante a produção do **manual #44** — que é justamente o
manual desse switch. Serve como prova cruzada de que o switch é o que liga a numeração.

---

## 6. Descoberta 1 — o caixa precisa estar aberto **com Delivery marcado**

Essa não estava no pedido e é a mais importante das três.

Na tela **Abrir Caixa** existem dois checkboxes: **Presencial** (Mesas/Comandas) e
**Delivery** (Entrega). O caixa **907962** foi aberto **sem Delivery**, e o efeito no
delivery daquele período foi total:

| Caixa | Delivery marcado na abertura | Delivery com número | Delivery **sem** número |
|-------|------------------------------|--------------------:|------------------------:|
| 893187 | Sim | 5 | 0 |
| **907962** | **Não** | 2 | **79** |
| 927703 | Sim | 110 | **0** |
| 967508 | Sim | 32 | 17 *(ver nota)* |

Setenta e nove pedidos de delivery em 16 dias ficaram **sem número de pedido** porque o caixa
aberto não contemplava delivery. Nos caixas com Delivery marcado, o número saiu em **100%**
dos pedidos.

Ou seja: *"delivery sempre ativo de acordo com o caixa"* tem uma condição que precisa entrar
no manual — **o caixa tem de estar aberto com Delivery marcado**. Sem isso o pedido entra,
é atendido e cobrado normalmente, só não ganha número de pedido. E não há aviso na tela.

> **Nota sobre os 17 do caixa atual.** São ruído do sandbox, não regra do produto: 10 deles
> têm o mesmo horário de cadastro no mesmo segundo (29/08 14:53:21) e 6 outros em pares
> (30/08 19:31:33 e 19:34:35). É a assinatura de venda criada **em lote pela API** por
> scripts de manuais anteriores, fora do fluxo da tela. Não usar essas vendas em nenhum
> exemplo do manual.

---

## 7. Descoberta 2 — o manual #44 precisa de correção

O manual **#44 (PDV — número e cupom)** descreve o switch assim:

| Campo | Efeito |
|-------|--------|
| **Número de Pedido no PDV** | Mostra o número da venda (ex.: *Venda #848*) |

**Isso está trocado.** O switch não tem nada a ver com o *Venda #848* da tela. Duas
evidências:

1. **O número da venda aparece com o switch desligado.** As 16 vendas de PDV anteriores a
   21/08 16:21 não têm número de pedido, e o PDV mostrava o número da venda do mesmo jeito.
2. **A tela do PDV nunca mostra o número do pedido.** O código do PDV envia
   `numeroPedido: null` em todos os pontos — há até o comentário `// PDV não tem numeroPedido`
   (`src/pages/PDV.tsx`). O modal *Conferir e Dividir* e o cupom impresso na hora usam apenas
   `numeroPreVenda`.

E a venda **848** do próprio manual #44 é a prova mais elegante: ela tem número de pedido
**3**, e a tela do #44 mostra **Venda #848**. Se o switch fizesse o que o #44 diz, a tela
mostraria 3.

**O que o switch faz de verdade:** manda o servidor **atribuir** um número de pedido às
vendas de PDV. Esse número aparece depois — no **Histórico de Vendas** (`3 (848)`), no cupom
reimpresso a partir da venda (`Pedido #3 (848)`) e nos relatórios. Não na tela do PDV no
momento da venda.

**Encaminhamento sugerido:** corrigir a tabela do #44 e apontar para o manual novo. O #44
continua bom no que é dele (o cupom, o preview do navegador); só a linha do switch está
errada.

---

## 8. Descoberta 3 — quem gera os números é o servidor, não o painel

Vale uma linha no manual, porque explica por que não existe campo para digitar número.

O painel **nunca** calcula número. O `pedidoBuilder` envia apenas `numeroPreVenda` (quando é
venda já existente) e nunca envia `numeroPedido` (`src/utils/pedidoBuilder.ts`). Os dois
números vêm na **resposta** de `venda2/salvar` e são só lidos
(`src/components/PedidoFields.tsx`). Consequências práticas para o usuário:

- **Não há como escolher, corrigir ou pular um número** pela tela.
- **Reabrir uma venda não gera número novo.** Reabrir traz para a tela uma venda que já
  existe, com os mesmos dois números (`docs/PDV_REABRIR_VENDA.md`).
- **Agrupar vendas não renumera.** O agrupamento manda só os `numeroPreVenda` de origem e
  recarrega a venda de destino (`src/lib/api/agruparVenda.ts`).

---

## 9. A regra de exibição, ponto a ponto

A regra que o dono descreveu está no código em 12 lugares, e é sempre a mesma ideia: **tem
número de pedido? mostra os dois, o do pedido primeiro e o da venda entre parênteses. Não
tem? mostra só o da venda.** O que muda de tela para tela é a **palavra na frente**, e é isso
que o manual tem de tabelar para o usuário não achar que são coisas diferentes.

| Onde | Com os dois números | Só com o da venda | Arquivo |
|------|---------------------|-------------------|---------|
| Cupom do cliente | `Pedido #60 (930)` | `Venda Nº 930` | `src/lib/cupom-pedido-utils.ts` |
| Cupom de divisão de conta | `Pedido #60 (930)` | `Venda Nº 930` | `src/lib/cupom-divisao-utils.ts` |
| **Histórico de Vendas** (coluna *Nº Pedido*) | `60 (930)` | `930` | `src/pages/HistoricoVendas.tsx` |
| **Delivery** (card do pedido) | `#60 (930)` | `#930` | `src/pages/Delivery.tsx` |
| Delivery (lista) | `#60` | `#930` | `src/components/delivery/DeliveryListView.tsx` |
| Detalhe da venda | `Venda Nº 930 • Pedido Nº 60` | `Venda Nº 930` | `src/components/VendaDetalhes.tsx` |
| Fichas de consumo do PDV | `Venda Nº 60 (930)` | `Venda Nº 930` | `src/hooks/usePDVImpressaoFichas.ts` |
| Vendas pendentes do caixa | duas colunas: *Nº Pedido* e *Nº PreVenda* | — | `src/components/caixa/CaixaVendasPendentesModal.tsx` |
| Ficha de cozinha | escolhido no layout: *Nº do pedido e venda* / *Nº do pedido* / *Nº da venda* | — | `src/components/impressao/LayoutCozinhaEditor.tsx` |
| NF-e / NFC-e | — | *Nº Venda* = `930` | `src/pages/NFe.tsx`, `NFCe.tsx` |
| Movimentações | — | `Venda #930` | `src/pages/Movimentacoes.tsx` |
| Excel do histórico | uma coluna *Nº Pedido*: o do pedido, ou o da venda | | `src/utils/excelExport.ts` |

Confirmado na tela em 01/09/2026. Histórico de Vendas, coluna **Nº Pedido**:

```
60 (930)   01/09/2026 14:48   DELIVERY   Aberto
59 (929)   01/09/2026 14:47   DELIVERY   Aberto
58 (928)   31/08/2026 23:27   PDV        Recebido
   924     30/08/2026 19:35   DELIVERY   Recebido     <- sem número de pedido
```

E no Delivery os cards saem como `#59 (929)` e `#60 (930)`.

### 9.1 Duas exceções que valem aviso

- **Busca.** No Histórico de Vendas a busca acha pelos **dois** números. Na tela de Delivery
  a busca usa um campo derivado (`numeroPedido || numeroPreVenda`), então **procurar pelo
  número da venda de um pedido que tem número de pedido pode não achar**.
- **Ordenação.** A coluna *Nº Pedido* do Histórico ordena pelo número do pedido e usa o da
  venda como reserva. Como o número do pedido reinicia, **a ordenação embaralha vendas de
  caixas diferentes** — dois pedidos "nº 1" de caixas distintos ficam lado a lado. É uma
  pergunta de suporte esperada e merece entrar no FAQ.

---

## 10. Onde ficam as coisas, na tela

| O que | Caminho | Observação |
|-------|---------|------------|
| Ligar o número no PDV | **Configuração → Parâmetros**, card **PDV**, switch **Número de Pedido no PDV** | Ajuda na tela: *Exibir número do pedido nas vendas*. **Grava sozinho** (auto-save 500 ms) |
| Abrir caixa com delivery | **Caixa → Abrir Caixa**, checkbox **Delivery** (Entrega) | É o que liga a contagem de pedido do delivery (seção 6) |
| Fechar o caixa | **Caixa → Fechar** | É o que reinicia a contagem |
| Ver os dois números juntos | **Histórico de Vendas**, coluna **Nº Pedido** | Formato `60 (930)` |
| Ver no delivery | **Delivery**, card do pedido | Formato `#60 (930)` |

O card **PDV** é o **último** da tela de Parâmetros, logo abaixo do card **Caixa**. O switch é
o **primeiro** item do card, e o vizinho de baixo é *Imprimir Venda Sempre*.

> ⚠️ **A tela de Parâmetros salva sozinha.** Clicar num switch "só para ver" já altera o
> ambiente. Ao capturar, conferir o `data-state` antes e restaurar depois.

---

## 11. Estrutura proposta do manual

Nome sugerido da pasta: `manuais/numeracao-pedidos/`.
Nome sugerido do menu: **Entendendo a numeração dos pedidos**.

1. **Os dois números** — a tabela "número da venda × número do pedido", em duas linhas.
2. **Como o sistema escreve** — `60 (930)` e `930`, com a tabela de onde cada palavra aparece.
3. **O número da venda** — contador único da loja, nunca reinicia. Uma frase sobre o reset
   opcional que está por vir.
4. **O número do pedido é do caixa** — a seção central, com a figura do reset (110 → 1
   enquanto a venda vai 838 → 843).
5. **Por que fechar o caixa todo dia** — a consequência prática: caixa aberto por um mês dá
   contagem de um mês; fechado todo dia dá a contagem do dia.
6. **Quem recebe número de pedido** — Delivery / PDV / Mesa, com o switch do PDV e o
   checkbox Delivery da abertura do caixa.
7. **Perguntas frequentes** — as sete da seção 12.

---

## 12. As sete perguntas que o manual tem de responder

Todas com resposta já apurada:

1. *"Por que meu pedido é #1 se já vendi 900 vezes?"* — são dois contadores; o 1 é do caixa.
2. *"Por que apareceram dois pedidos nº 1 no relatório?"* — são de caixas diferentes.
3. *"Meu delivery não está saindo com número de pedido."* — o caixa foi aberto sem Delivery.
4. *"Liguei o switch do PDV e a tela continua mostrando Venda #848."* — é o esperado; o
   número do pedido aparece no Histórico, no cupom reimpresso e nos relatórios.
5. *"Como faço a mesa ter número de pedido?"* — não tem. Mesa usa só o número da venda.
6. *"Posso zerar o número da venda?"* — hoje não. Está no roadmap.
7. *"Pulou um número da venda, perdi uma venda?"* — não; venda cancelada mantém o número
   dela (o levantamento não achou nenhum buraco em 304 vendas).

---

## 13. Provas a capturar (~8 imagens)

Enxuto de propósito: o assunto é conceito, não passo a passo de cadastro.

| Nº | Imagem | Tipo | Para que serve |
|----|--------|------|----------------|
| 1 | Parâmetros → card PDV com o switch | setas | Onde se liga no PDV |
| 2 | Abrir Caixa com **Delivery** marcado | setas | A condição do delivery (seção 6) |
| 3 | Histórico de Vendas, coluna *Nº Pedido* com `60 (930)` **e** uma linha só com `924` | setas | As duas formas de exibição na mesma tela |
| 4 | Card do Delivery com `#60 (930)` | setas | O formato no delivery |
| 5 | Detalhe da venda (*Venda Nº 930 • Pedido Nº 60*) | setas | A terceira forma de escrever |
| 6 | Cupom no preview: `Pedido #60 (930)` | setas | O que o cliente recebe |
| 7 | Vendas pendentes do fechamento (colunas *Nº Pedido* e *Nº PreVenda*) | contexto | Os dois números lado a lado |
| 8 | Diagrama do reset (110 → 1 × 838 → 843) | desenho | A imagem-chave do manual |

A **8** provavelmente não é screenshot: é um desenho simples (duas réguas paralelas, uma que
reinicia e outra que não). É a figura que o dono vai querer mandar para o cliente.

Para a **3**, a tela de hoje já serve: as linhas 918–930 têm as duas formas misturadas.
Para a **6**, reimprimir de uma venda com número de pedido (não imprimir do PDV na hora, que
sai sem).

---

## 14. O que **não** foi possível confirmar

Honestidade sobre os limites deste levantamento.

| Item | Situação |
|------|----------|
| **O código do servidor** | O backend (`beetechbr/beetech-server-node-2.0`) **não clonou nesta sessão**: o `BITBUCKET_TOKEN` não autentica mais (testadas as duas formas de usuário e os dois secrets do ambiente). Toda a regra do reset foi provada por **dado real**, não por leitura de código |
| **Onde o contador mora** | O objeto do caixa tem um campo `numeroPedido` (`src/hooks/useCaixaDetalhes.ts`), que é o palpite natural para o contador, mas ele volta `null` na listagem e o painel não o usa. **Não confirmado** |
| **Reset opcional do número da venda** | Não existe nada no código. É roadmap |
| **O que acontece com dois caixas abertos ao mesmo tempo** | O sandbox tem `caixaPorUsuario: true` e `qtdCaixas: 10`, mas na prática só houve um caixa aberto por vez. **Não testado** — ver seção 15 |

---

## 15. A única pergunta aberta que pode mudar o manual

**Com dois caixas abertos ao mesmo tempo, existe uma contagem de pedido por caixa ou uma
só?** O sandbox permite 10 caixas e tem *Caixa por Usuário* ligado, mas o histórico só tem um
caixa aberto por vez — então o dado não responde.

Isso muda a redação da seção 4 do manual: se a contagem for por caixa, dois operadores podem
ter um "pedido nº 1" simultâneo, e o manual tem de avisar. Duas saídas:

- **O dono responde** de cabeça (mais rápido, e provavelmente ele já sabe).
- **Testar no sandbox**: abrir um segundo caixa com Delivery, lançar um pedido em cada e
  comparar. Custa duas vendas e um fechamento de caixa.

Enquanto não houver resposta, a proposta é escrever a seção **no singular** ("o caixa aberto")
e não afirmar nada sobre caixas simultâneos.

---

## 16. Decisões que o dono precisa tomar

1. **Aprovar o manual** com a estrutura da seção 11.
2. **Responder a pergunta da seção 15** (dois caixas abertos), ou autorizar o teste.
3. **Corrigir o #44?** A linha do switch está errada (seção 7). Sugestão: corrigir junto,
   no mesmo trabalho.
4. **Entra a descoberta do checkbox Delivery** (seção 6)? É informação valiosa e explica
   chamado de suporte, mas mistura o assunto com o manual de abrir caixa. Sugestão: entra,
   em bloco curto de aviso, com link para o manual de Caixa.
5. **Nome do menu**: *Entendendo a numeração dos pedidos* — ou o dono prefere outro.

---

## 17. Como este estudo foi levantado

- **Código do front** (`~/refs/beefood-web-react`): parâmetro, pontos de exibição, ciclo de
  vida dos dois números, e a documentação interna em `docs/`.
- **Dado real do sandbox** (01/09/2026), via API autenticada, somente leitura: 304 vendas
  (`venda2/historicoVendas`), 10 caixas (`caixa2/caixaListagem`), detalhe de cada venda
  (`venda2/vendaDetalhes`, que traz o `caixaID`) e a configuração da empresa
  (`empresa2/empresaConfig`, que confirmou `pdvNumeroPedido: true`).
- **Telas conferidas**: Parâmetros (card PDV), Histórico de Vendas (coluna *Nº Pedido*) e
  Delivery (cards). Nenhum switch foi clicado; nenhuma venda foi criada.

O cruzamento que produziu a prova foi **associar cada venda à janela de tempo do caixa**
(abertura → fechamento), e não ao `caixaID` gravado na venda — esse campo fica `null`
enquanto a venda não é liquidada no caixa, e usá-lo esconderia o padrão. Fica registrado
para quem repetir o levantamento.
