# Avisos de WhatsApp da entrega

A entrega dispara **quatro** mensagens de WhatsApp. Três vão para o entregador e uma vai para
o cliente:

| Aviso | Quem recebe | Quando sai |
|-------|-------------|------------|
| **Nova entrega** | entregador | você põe o pedido na rota dele, ou vincula o entregador no pedido |
| **Entrega cancelada** | entregador | aquele pedido deixou de ser dele — saiu da rota, trocou de entregador ou a rota foi excluída |
| **Relatório diário** | entregador | de manhã, com as entregas do dia anterior |
| **Entregador próximo** | cliente | o entregador chegou a X km do endereço do cliente |

Todas nascem **ligadas** e com texto pronto. O que este manual mostra é onde elas ficam, o que
cada uma exige para sair de verdade e **um passo que precisa ser feito uma vez** para o aviso
do cliente funcionar.

> As imagens têm **setas numeradas** (1, 2, 3…). Cada número indica o campo correspondente na
> tela.

## Para que serve

- Avisar o entregador da entrega nova sem telefonar para ele.
- Avisar o cliente de que o entregador está chegando, com o nome de quem vai bater na porta.
- Dar ao entregador, de manhã, o resumo do que ele fez ontem e quanto foi de taxa.

## Antes de começar

- O WhatsApp da loja precisa estar **conectado** (WhatsApp → Conexão). Sem número conectado a
  tela grava o texto e nada é enviado.
- O entregador precisa de **Celular** no cadastro de funcionário. Sem telefone, as três
  mensagens dele são descartadas em silêncio.
- Para o aviso do cliente, o entregador precisa estar com o **aplicativo aberto**: o aviso
  depende da posição de GPS dele.

---

## 1. Onde ficam os quatro avisos

Abra **WhatsApp → Notificações**. A tela é uma lista de avisos separada em grupos.

![A lista de notificações automáticas](imagens-tratadas/01-lista-notificacoes.png)

| Nº | Onde | O que é |
|----|------|---------|
| 1. | Grupo **Delivery** | As mensagens que o **cliente** recebe. O contador `8/8` diz quantas estão ligadas. |
| 2. | **Interruptor** | Liga e desliga aquele aviso. Verde é ligado. |
| 3. | **Lápis** | Abre o texto para editar. |

Os avisos da entrega estão **em dois lugares diferentes**, e isso confunde na primeira vez:

![O grupo Entregador e o aviso do cliente](imagens-tratadas/02-grupo-entregador.png)

| Nº | Aviso | Quem recebe |
|----|-------|-------------|
| 1. | Grupo **Entregador** | O contador `3/3`: são três avisos, todos ligados. |
| 2. | **Nova entrega** | O entregador |
| 3. | **Entrega cancelada** | O entregador |
| 4. | **Relatório diário** | O entregador |
| 5. | **Entregador próximo** | O **cliente** — por isso ele está no grupo Delivery, e não no grupo Entregador |

> **A regra do agrupamento é o destinatário, não o assunto.** *Entregador próximo* fala do
> entregador, mas quem lê é o cliente; então ele mora com as mensagens de cliente. Procurar os
> quatro avisos no mesmo grupo é o erro que todo mundo comete aqui.

---

## 2. Nova entrega: o que o entregador recebe

Clique no lápis de **Nova entrega**.

![O texto de fábrica da Nova entrega](imagens-tratadas/03-modal-nova-entrega.png)

| Nº | Onde | O que fazer |
|----|------|-------------|
| 1. | **Mensagem principal** | O texto que vai ao entregador. Os trechos entre `**` são marcadores: o sistema troca cada um pelo dado do pedido. |
| 2. | **Restaurar padrão** | Devolve o texto de fábrica. É a saída quando a edição apagou um marcador. |
| 3. | **Variáveis disponíveis** | A paleta: clicar insere o marcador no texto. |

O texto de fábrica é este, e cada marcador vira um dado do pedido:

| Marcador | Vira |
|----------|------|
| `**MEU_NOME_FANTASIA**` | o nome do restaurante |
| `**VENDA_NUMERO**` | o número do pedido |
| `**CLIENTE_NOME**` | o nome do cliente |
| `**VENDA_ENTREGA**` | o endereço da entrega |
| `**VENDA_PAGAMENTO**` | a forma de pagamento |
| `**VENDA_TOTAIS**` | o bloco com total e taxa |

> **O nome do restaurante no começo não é enfeite.** O entregador roda para mais de um
> restaurante e recebe a mensagem de um número que não tem salvo. *"Nova entrega"* sem dizer
> de onde obriga ele a abrir o aplicativo para descobrir.

**Uma mensagem por pedido, não uma por rota.** Uma rota de três paradas manda três mensagens.
É de propósito: o entregador precisa de um endereço e um pagamento por vez.

---

## 3. Relatório diário: as entregas de ontem

O texto do **Relatório diário** usa quatro marcadores que **não estão na paleta** — eles só
existem nesta mensagem.

![Os marcadores do relatório diário](imagens-tratadas/04-modal-relatorio-diario.png)

| Nº | Marcador | Vira |
|----|----------|------|
| 1. | `**DETALHE_ENTREGAS**` | a lista das entregas, uma por linha, com pedido, taxa e endereço |
| 2. | `**LINHA_TAXAS**` | a linha do total de taxas — que **desaparece** quando não houve taxa nenhuma |

Os outros dois são `**DATA_REFERENCIA**` (o dia de ontem) e `**QTD_ENTREGAS**` (quantas
entregas ele fechou).

> **Se você apagar um destes marcadores, a paleta não o devolve.** Ela tem só as variáveis de
> cliente e de venda. Para recuperar, use **Restaurar padrão** — é mais rápido que digitar o
> marcador na mão e arriscar errar o nome.

A lista existe porque total sem detalhe é número que o entregador não tem como conferir. Ela é
cortada em cerca de 35 entregas, e quando isso acontece a mensagem avisa que o total é do dia
inteiro, não só das linhas que apareceram.

---

## 4. Entregador próximo: o aviso do cliente, e o campo de km

Este é o único aviso da tela com um campo a mais. Clique no lápis de **Entregador próximo**.

![O campo de distância do aviso de proximidade](imagens-tratadas/05-modal-entregador-proximo.png)

| Nº | Onde | O que fazer |
|----|------|-------------|
| 1. | **Avisar quando o entregador estiver a até … km do cliente** | A distância que dispara o aviso. Padrão **2 km**. |
| 2. | **Mensagem principal** | Usa `**ENTREGADOR_NOME**` (o primeiro nome de quem está levando) e `**VENDA_ENTREGA**`. |
| 3. | **Variações da mensagem** | Esta mensagem vem com **três variações** de fábrica. O sistema sorteia uma a cada envio. |
| 4. | **SALVAR (F2)** | Grava o texto **e a distância**. |

### Salve esta mensagem uma vez, mesmo sem mudar nada

É o passo mais importante deste manual, e ele não é óbvio: **o campo mostra 2 km antes de o
valor existir**. A tela preenche o campo com o padrão para você não ver uma caixinha vazia,
mas enquanto ninguém salvar, a distância não está gravada — e o aviso não sai para ninguém.

Abrir o aviso e clicar em **SALVAR (F2)**, sem trocar nada, grava os 2 km e resolve.
Conferimos os dois lados no nosso restaurante de teste: antes de salvar a distância estava em
branco no banco; depois do clique, gravada em 2 km.

| Quando | O que está gravado |
|--------|--------------------|
| Antes de salvar a primeira vez | nada — e o aviso é pulado |
| Depois de salvar | a distância que está no campo |

> **Vale para praticamente todos os restaurantes.** Na base inteira, quase nenhum tem essa
> distância gravada — o aviso está ligado, o texto está pronto e a tela mostra 2 km, mas ele
> ainda não saiu nenhuma vez. Um clique em SALVAR por loja resolve.

### O que o campo aceita

| Valor | O que acontece |
|-------|----------------|
| `0,1` a `50` | aceito (é km, com vírgula) |
| `0` ou vazio | recusado |
| `2000` | recusado — o campo é **km**, não metros |

![O aviso quando a distância não é válida](imagens-tratadas/07-km-recusado.png)

| Nº | Onde | O que diz |
|----|------|-----------|
| 1. | **Campo de km** | `2000` foi digitado — quem pensou em metros erra aqui. |
| 2. | **Aviso** | *Informe a distância em km, entre 0,1 e 50.* Nada é gravado, nem o texto. |

O teto de 50 km existe justamente para pegar esse erro: `2000` km avisaria todo cliente no
instante do despacho.

> **Mudança de distância leva até 30 minutos para valer.** O servidor que calcula a
> proximidade guarda esse número em memória e o recarrega de meia em meia hora. Já o
> liga/desliga do aviso vale na hora. Se você mudou de 2 para 1 km e nada mudou no primeiro
> pedido, é esse tempo.

**Para desligar o aviso, use o interruptor da lista** — não tente zerar o km.

---

## 5. Sem Celular no cadastro, o entregador não recebe nada

As três mensagens do entregador vão para o telefone do **cadastro de funcionário**, em
Cadastros → Funcionários → aba *Dados*.

![Os campos de telefone do funcionário](imagens-tratadas/10a-celular-do-entregador.png)

| Nº | Campo | O que o sistema faz |
|----|-------|---------------------|
| 1. | **Telefone** | Usado como reserva, se não houver Celular. |
| 2. | **Celular** | O primeiro escolhido — é o campo com mais chance de ser WhatsApp. |

Três coisas que decorrem disso:

- **Sem nenhum dos dois, nada é enviado** — e não aparece erro em tela nenhuma. Se um
  entregador diz que não recebe as mensagens, é o primeiro lugar a olhar.
- **Funcionário demitido ou inativo não recebe.** A data de demissão e o interruptor
  *Funcionário Ativo* valem também para o WhatsApp.
- **Telefone novo vale na hora.** Salvar o cadastro basta; não há espera.

---

## 6. O que chega no celular

O sandbox deste manual não tem número conectado, então as conversas abaixo são **simulação** —
mas o texto não foi escrito à mão: é o texto de fábrica das próprias mensagens, com os
marcadores já substituídos, exatamente como o sistema monta.

### No celular do entregador

![As três mensagens do entregador](imagens-tratadas/08a-conversa-entregador.png)

Na ordem: a entrega nova que entrou na rota dele, o pedido que saiu da mão dele (troca de
entregador) e o resumo do dia anterior, que chega de manhã.

### No celular do cliente

![As duas mensagens do cliente](imagens-tratadas/09a-conversa-cliente.png)

A primeira é o **Pedido saiu para entrega**, que já existia antes deste módulo e dispara no
despacho da rota. A segunda é o **Entregador próximo**.

> **As duas podem chegar quase juntas.** Em pedido perto do restaurante, o entregador já sai
> dentro dos 2 km do cliente — então o "saiu para entrega" e o "está chegando" caem no celular
> com um minuto de diferença. Quem resolve isso é você, baixando a distância: 800 m num bairro
> pequeno, 3 km numa cidade espalhada.

### Colocar o nome do entregador no "saiu para entrega"

O texto de fábrica do **Pedido saiu para entrega** não diz quem está levando. Para incluir,
acrescente `**ENTREGADOR_NOME**` ao texto daquele aviso — o sistema substitui, mesmo que a
paleta de variáveis não ofereça esse marcador.

Duas regras ao escrever essa frase:

- **Não deixe o marcador dentro de um trecho em negrito** e não comece a linha com ele.
- Escreva a frase de modo que ela continue fazendo sentido **sem** o nome: em pedido entregue
  por integradora não há entregador, e o marcador simplesmente desaparece.

---

## Perguntas frequentes

**O entregador não recebe nada.**
Na ordem: o WhatsApp da loja está conectado? O **Celular** dele está preenchido no cadastro? O
interruptor daquele aviso está verde? Ele está ativo e sem data de demissão?

**O cliente não recebe o "entregador está chegando".**
Abra o aviso **Entregador próximo** e clique em SALVAR uma vez (seção 4). Depois: o entregador
estava com o aplicativo aberto? A posição do GPS dele chegou nos últimos minutos? O endereço
do cliente tem coordenada?

**O entregador tem o aplicativo. Ele recebe em dobro?**
Recebe o aviso do aplicativo e o WhatsApp, sim. É de propósito: o WhatsApp é o único canal que
alcança quem não instalou o aplicativo.

**Troquei o entregador de um pedido. Os dois são avisados?**
Sim: quem perdeu recebe *Entrega cancelada* e quem ganhou recebe *Nova entrega*.

**"Entrega cancelada" é o cancelamento do pedido?**
Não. Aqui significa *"este pedido não é mais seu"*. O cancelamento do pedido tem aviso próprio,
e vai para o cliente.

**O relatório diário é o mesmo boletim que eu recebo de manhã?**
Não. O seu é o **Resumo Diário** (faturamento da loja). Este vai para o entregador, com as
entregas dele.

**Mexi no texto e ficou ruim. Como voltar?**
**Restaurar padrão**, dentro do aviso.

---

## Onde continuar

| Manual | O que cobre |
|--------|-------------|
| [Despachar a rota e acompanhar no mapa](../gestao-entregas-despachar/gestao-entregas-despachar.md) | O clique que dispara *Nova entrega* e *saiu para entrega* |
| [Liberar o entregador](../gestao-entregas-liberar-entregador/gestao-entregas-liberar-entregador.md) | O cadastro onde o Celular é preenchido |
| [Notificações de cada etapa do pedido](../whatsapp-notificacoes/whatsapp-notificacoes.md) | Os oito avisos do pedido, do recebido ao entregue |
| [Conectar o WhatsApp](../whatsapp-conectar/whatsapp-conectar.md) | O QR Code, sem o qual nada é enviado |
| [Entregador (Taxa / KM)](../entregador-quanto-recebe/entregador-quanto-recebe.md) | De onde vem o valor de taxa que aparece no relatório diário |

*Última atualização: setembro/2026 — BeeFood · Gestão de Entregas 2.0*
