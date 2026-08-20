# Manual — Campanhas Inteligentes

As **campanhas inteligentes** são mensagens de WhatsApp que o BeeFood envia **sozinho**, quando
o cliente faz algo que merece uma resposta: abandonou o carrinho, ficou com cashback parado,
sumiu por meses, fez aniversário.

Você não aperta nenhum botão de enviar. Você configura uma vez e a campanha trabalha todos os
dias.

Este manual explica:

1. As **seis campanhas** que já vêm criadas na sua conta — e por que **quatro já estão ligadas**
2. Como **ler o card** de cada campanha
3. Os campos dos **três passos** de configuração
4. Como funcionam as **variáveis** e a **variação automática** das mensagens
5. Como **ligar, pausar** e **ler o resultado**

> As imagens têm **setas com números** (1, 2, 3...). No texto, cada número indica exatamente o
> campo ou botão correspondente na tela.

---

## Onde encontrar

No menu lateral, em **Food Marketing**, abra **Campanhas WhatsApp**. A página tem três abas no
topo: **Indicadores**, **Campanhas** e **Campanhas Inteligentes**. É na terceira que você
trabalha.

Vale entender a diferença logo de início, porque as duas primeiras abas parecem fazer o mesmo:

| | Campanhas | Campanhas Inteligentes |
|---|---|---|
| Quem decide o momento | Você, ao publicar | O sistema, quando o gatilho acontece |
| Quando envia | Na hora | Sempre que um cliente entra na regra |
| Público | Uma lista que você monta | Recalculado sozinho |
| Trabalho | Repetido a cada campanha | Configura uma vez |

---

## Antes de tudo: quatro campanhas já estão enviando

Esta é a informação mais importante do manual. A sua conta **já veio** com seis campanhas
prontas, e **quatro delas nascem ligadas**:

![As seis campanhas inteligentes](imagens-tratadas/01-lista-campanhas.png)

1. A aba **Campanhas Inteligentes**, dentro de Campanhas WhatsApp
2. O selo de estado — **Ativo** quer dizer que essa campanha está enviando mensagens
3. A chave liga/desliga de cada campanha
4. **Pausado** — está configurada, mas não envia
5. **Rascunho** — nunca foi ligada

As quatro que já vêm ligadas são **Carrinho abandonado**, **Recebeu o cardápio e não pediu**,
**Recuperador de vendas** e **Cashback parado**. As duas que vêm desligadas são **Aniversário**
e **Boas-vindas / 2ª compra**.

> **Reserve alguns minutos para revisar as quatro que já estão ativas.** Elas falam com os seus
> clientes usando o seu número de WhatsApp. Vale conferir se o texto combina com o jeito da sua
> loja e se o horário faz sentido para o seu funcionamento.

Todas as seis trazem o selo **BeeFood**, que significa campanha padrão da casa: você pode
editar tudo, mas não pode excluir. Se quiser voltar atrás, use **Restaurar padrão**.

---

## Como ler o card de uma campanha

![Anatomia do card de uma campanha](imagens-tratadas/02-card-anatomia.png)

1. **Estado**: Ativo, Pausado ou Rascunho
2. Selo **BeeFood**: campanha padrão, não pode ser excluída
3. **Chave liga/desliga**: sempre pede confirmação antes de valer
4. **Selo do gatilho**: o que faz a mensagem sair (veja a seguir)
5. **Receita gerada**: quanto de venda saiu de quem clicou no link desta campanha
6. **Resultado** e **Histórico**: os números e a lista de mensagens enviadas

Os três números embaixo da receita são **Conversão** (quantos dos que receberam acabaram
pedindo), **Envios** e **Pedidos**.

O selo do gatilho tem três variações, e ele é a chave para entender cada campanha:

| Selo | Significa |
|---|---|
| **Gatilho: Público de clientes** | Roda sobre um grupo de clientes (uma segmentação) |
| **Gatilho: Cardápio digital** | Reage a algo que o cliente fez no seu site de pedidos |
| **Gatilho: WhatsApp / BeeBot** | Reage à conversa do cliente com o BeeBot |

Quando uma campanha está em rascunho, o card mostra um botão diferente:

![Card de campanha em rascunho](imagens-tratadas/03-card-rascunho.png)

1. O selo **Rascunho**
2. **Revisar e ativar** abre a campanha para você conferir antes de ligar

---

## As seis campanhas padrão

Cada uma tem um gatilho próprio, um texto próprio e uma configuração de fábrica pensada para o
tipo de conversa que ela faz. Todas **param sozinhas** quando o cliente faz o pedido.

### Carrinho abandonado

O cliente montou a sacola no seu cardápio digital e não finalizou. Cerca de 15 minutos depois,
a campanha manda uma mensagem lembrando.

É a campanha mais rápida das seis, e a que costuma dar mais retorno, porque fala com alguém que
estava com fome agora. De fábrica ela vai até as 23h e aceita até 7 envios por dia.

### Recebeu o cardápio e não pediu

O cliente chamou no WhatsApp, o BeeBot mandou o link do cardápio, e o pedido não veio. Uns 15
minutos depois, a campanha puxa a conversa de volta.

Não depende do cardápio digital nem do Pixel: usa a própria conversa do BeeBot.

### Recuperador de vendas

Fala com quem já comprou e sumiu — o público **Clientes sumidos**, que junta quem não pede há
mais de 30 dias.

Por ser uma reconquista, ela é a mais contida de todas: manda no máximo 2 mensagens por dia e
só volta a falar com o mesmo cliente depois de 120 dias.

### Cashback parado

Fala com quem tem saldo de cashback esperando. Bom para o cliente, que não perde o dinheiro, e
bom para a loja, que traz o pedido de volta.

Como o texto usa o saldo, quem não tem cashback nunca recebe essa mensagem.

### Aniversário

Manda parabéns no dia do cliente, com uma oferta. Roda uma vez por dia sobre o público
**Aniversariantes do dia**, que o sistema monta sozinho.

Vem **desligada** de fábrica.

### Boas-vindas / 2ª compra

Fala com quem fez o primeiro pedido nos últimos 30 dias e convida para a segunda compra. Para
de falar quando a segunda compra acontece.

Vem **desligada** de fábrica. Manda uma única vez para cada cliente.

### A configuração de fábrica de cada uma

| Campanha | Gatilho | Horário | Só quem já falou (janela) | Espera para repetir | Envios por dia | Variações |
|---|---|---|---|---|---|---|
| Carrinho abandonado | Cardápio digital | 10h–23h | 90 dias | 7 dias | 7 | 9 |
| Recebeu o cardápio e não pediu | WhatsApp / BeeBot | 10h–22h | 1 dia | 7 dias | 50 | 9 |
| Recuperador de vendas | Público de clientes | 10h–21h | 120 dias | 120 dias | 2 | 5 |
| Cashback parado | Público de clientes | 10h–21h | 15 dias | 7 dias | 5 | 4 |
| Aniversário | Público de clientes | 10h–21h | 365 dias | 1 dia | 50 | 4 |
| Boas-vindas / 2ª compra | Público de clientes | 10h–21h | 30 dias | 365 dias | 5 | 5 |

Todas vêm com os **sete dias da semana** liberados e com a proteção **Anti Banimento** ligada.

Você pode ver a descrição de cada campanha a qualquer momento em **Novo campanha inteligente**
→ **Usar um modelo pronto**:

![Os seis modelos prontos com a descrição de cada um](imagens-tratadas/22-modelos-prontos.png)

---

## Passo 1 — Identificação e público

Clique em qualquer card para abrir a campanha. Ela abre num painel lateral, dividido em três
passos. O primeiro define **onde a campanha roda e com quem ela fala**.

![Passo 1 de uma campanha por público de clientes](imagens-tratadas/04-passo1-publico-segmentacao.png)

1. **Cardápio** — por qual número de WhatsApp a mensagem sai. Com uma loja só, deixe em
   **Todos os cardápios**
2. **Segmentação** — o grupo de clientes que recebe. Nas campanhas padrão isso já vem
   preenchido com um público da BeeFood

O quadro de cima, **Como esta automação funciona**, explica em uma frase quem entra na campanha
e quando ela para. O campo **Origem do público**, à direita, é o que determina o gatilho, com
três opções:

| Origem do público | O que dispara a mensagem |
|---|---|
| **Segmentação de clientes** | O cliente pertencer a um grupo (sumidos, aniversariantes, com cashback...) |
| **Carrinho abandonado** | O cliente deixar itens na sacola do cardápio digital |
| **Recebeu cardápio e não pediu** | O BeeBot mandar o cardápio e o pedido não vir |

Quando o gatilho é um **evento** — carrinho abandonado ou cardápio sem pedido — aparecem dois
campos de tempo no lugar da segmentação:

![Passo 1 de uma campanha por evento](imagens-tratadas/13-passo1-gatilho-evento.png)

1. **Esperar antes de enviar (min)** — quanto tempo o sistema aguarda antes de mandar. De
   fábrica são 15 minutos; a loja da imagem ajustou para 5. Curto demais incomoda, longo demais
   esfria
2. A **frase-resumo** que a tela monta com os dois campos, para você conferir o que configurou

O campo da direita, **Considerar eventos das últimas (h)**, é a idade máxima do evento que
ainda vale a pena perseguir. Um carrinho abandonado há mais horas que isso é considerado frio e
não recebe mensagem. Na campanha do BeeBot esse campo fica desabilitado, porque ali o controle
é por pendência do dia.

---

## Passo 2 — A mensagem e suas variações

![Passo 2 com as variações da mensagem](imagens-tratadas/05-passo2-variacoes.png)

Cada cliente recebe **uma única mensagem** desta campanha. As **variações** existem para que o
sistema alterne entre textos diferentes e as suas mensagens não pareçam disparo em massa — o
que reduz o risco de bloqueio.

As campanhas padrão já vêm com 4 a 9 variações escritas. Você pode editar, apagar e adicionar
com o botão **+ Variação**.

![Uma variação com variação automática](imagens-tratadas/17-variacao-com-spintax.png)

1. Trechos entre chaves com barra, como `{quase pronto|quase completo}`, são **variação
   automática**: o sistema sorteia uma das opções em cada envio
2. A **Prévia** mostra como a mensagem fica com as variáveis preenchidas

No alto da variação ficam a tag obrigatória **{{meu_link}}** e o botão **Inserir variável**.
Cada variação também aceita um anexo de até 10MB — imagem, vídeo ou documento.

> A Prévia troca as variáveis por exemplos, mas **não sorteia** a variação automática: ela
> continua mostrando `{quase pronto|quase completo}`. O sorteio acontece no envio de verdade.

### O link do cardápio é obrigatório

Toda variação precisa conter `{{meu_link}}`. Não é capricho: é por esse link que o sistema
descobre quem clicou e quem comprou por causa da mensagem. Sem ele, a campanha envia mas não
consegue mostrar resultado nenhum.

Se você apagar a tag, a tela avisa na hora:

![Aviso de mensagem sem o link do cardápio](imagens-tratadas/07-aviso-sem-link.png)

No lugar da tag você também pode colar o endereço do seu cardápio digital, desde que seja um
link do BeeFood. Endereço próprio da loja não serve — nesse caso, use `{{meu_link}}`.

---

## As variáveis das mensagens

Variável é um trecho que o sistema troca pelo dado de cada cliente no momento do envio. Escreva
`{{primeiro_nome}}` e o cliente lê "Maria".

Clique dentro do texto e depois em **Inserir variável** para abrir o catálogo:

![Catálogo de variáveis disponíveis](imagens-tratadas/14-modal-variaveis.png)

São 20 variáveis, organizadas em três grupos:

| Grupo | Para que serve |
|---|---|
| **Básicas** | Link do cardápio, nome do cliente e saldo de cashback |
| **Produto & Promoção** | Produto preferido, mais vendido, promoções e preços |
| **Foto** | As mesmas de produto, mas enviando a mensagem com a foto |

As quatro básicas são as que você mais vai usar:

| Variável | O que aparece para o cliente |
|---|---|
| `{{meu_link}}` | O endereço do seu cardápio digital — **obrigatória** |
| `{{primeiro_nome}}` | Só o primeiro nome, com a inicial maiúscula |
| `{{nome}}` | O nome completo, como está no cadastro |
| `{{saldo_cashback}}` | Quanto o cliente tem de cashback, já em reais |

`{{saldo_cashback}}` tem um detalhe importante: se a mensagem usa essa variável, ela **só é
enviada a quem tem saldo**. Quem está com zero não recebe.

### Algumas variáveis não funcionam em toda campanha

Nove das vinte usam o **histórico de compras** do cliente: produto preferido, último produto
comprado, dias desde a última compra, categoria preferida e as promoções ligadas ao gosto dele.

Elas funcionam nas campanhas por **público de clientes**, onde o sistema sabe exatamente com
quem está falando. Nas campanhas de **carrinho abandonado** e de **cardápio sem pedido** não
existe cliente identificado, então essas variáveis aparecem com um **cadeado** e não podem ser
inseridas:

![Variáveis bloqueadas por dependerem do histórico](imagens-tratadas/15-variaveis-bloqueadas.png)

Repare que **Mais vendido do restaurante** continua disponível: ela não depende do cliente, vale
para qualquer um. Nesses gatilhos, use as variáveis gerais — mais vendido, maior promoção, nome
do restaurante e preços.

### As variáveis com foto

As quatro do grupo **Foto** mudam o formato do envio: em vez de texto puro, a mensagem sai como
**imagem com legenda**, usando a foto do produto. Se o produto escolhido não tiver foto
cadastrada, a mensagem vai só como texto, sem erro.

### Variação automática: escrevendo um texto que muda sozinho

Além das variações separadas, você pode fazer o texto variar dentro de uma mesma frase. Escreva
as opções entre chaves, separadas por barra:

![Ajuda da variação automática](imagens-tratadas/16-spintax.png)

Escrevendo `{Oi|Olá|E aí}, {{primeiro_nome}}!`, cada cliente recebe uma versão diferente: "Oi,
Maria!", "Olá, Maria!" ou "E aí, Maria!". É o que impede o WhatsApp de ver centenas de
mensagens idênticas saindo do seu número.

Duas regras para não errar:

- **Chave simples** com barra é sorteio: `{opção1|opção2}`
- **Chave dupla** é variável: `{{primeiro_nome}}`

Nunca coloque barra dentro de uma variável.

---

## Passo 3 — Agenda e anti-spam

Este é o passo que protege o seu número.

![Passo 3 com agenda e proteções](imagens-tratadas/08-passo3-agenda.png)

1. **Dias da semana** em que a campanha pode enviar
2. **Horário de início** e **Horário de fim**
3. A proteção **Anti Banimento**
4. **Intervalo mín. entre mensagens (dias)**

Antes dos campos, leia o quadro verde: **as mensagens só são enviadas quando o cardápio digital
estiver aberto para pedidos**. Os dias e horários daqui servem apenas para **restringir ainda
mais** essa janela — por exemplo, evitar os minutos perto do fechamento. Eles nunca fazem a
campanha enviar fora do horário de funcionamento.

### Anti Banimento: a proteção que você não deve desligar

![Proteção Anti Banimento ligada](imagens-tratadas/09-anti-banimento-ligado.png)

Com a chave **Só enviar para quem já me mandou mensagem** ligada, a campanha só fala com quem
já conversou com você antes. É a diferença entre responder um cliente e abordar um
desconhecido — e o WhatsApp trata as duas coisas de formas muito diferentes.

O campo embaixo, **Considerar mensagens recebidas nos últimos (dias)**, define até quando aquela
conversa antiga ainda conta. Nas campanhas padrão esse número acompanha o tipo de conversa: 1
dia no caso do BeeBot, 120 dias na recuperação de clientes sumidos.

Se você desligar a proteção, a tela muda de cor e avisa:

![Proteção desligada, com aviso](imagens-tratadas/10-anti-banimento-desligado.png)

E ao salvar, aparece um alerta que vale ler com atenção:

![Alerta de risco de perder o número](imagens-tratadas/11-alerta-risco-banimento.png)

O risco descrito ali é real: banimento definitivo do número, perda das conversas e dos grupos,
e marcação como spam. **A recomendação é manter a proteção ligada.** Se ainda quiser
prosseguir, o botão da direita assume o risco; o da esquerda volta e mantém a proteção.

### Ritmo: quantas mensagens por dia

![Intervalo mínimo e ritmo de envio](imagens-tratadas/12-intervalo-e-ritmo.png)

**Intervalo mín. entre mensagens (dias)** é o tempo que a campanha espera antes de tentar de
novo. Cada cliente recebe uma única mensagem por campanha; esse número controla o ritmo geral.

**Ritmo: envios por dia** limita quantas mensagens saem por dia. Zero significa sem limite, mas
número baixo é mais seguro: um volume repentino de mensagens é justamente o que chama a atenção
do WhatsApp. Repare que a BeeFood usa apenas 2 por dia no Recuperador de vendas.

Quando terminar de ajustar, use **SALVAR (F2)**. Enquanto você não salva, nada é alterado — dá
para abrir, olhar e sair sem medo.

---

## Ligar e pausar

A chave no card liga e desliga a campanha, sempre com uma confirmação antes:

![Confirmação para ligar uma campanha](imagens-tratadas/20-dialogo-ativar.png)

Ligar **não dispara mensagem na hora**. A campanha passa a observar e envia quando um cliente
entrar nas regras, respeitando o horário, o anti-spam e o limite por dia.

Pausar interrompe os envios na hora e não apaga nada: o texto, a configuração e o histórico
continuam lá para quando você ligar de novo.

No menu de três pontos de cada card existe ainda **Restaurar padrão**, que devolve o nome, os
textos e as configurações originais da BeeFood, mantendo o estado e o cardápio. Use quando
mexer demais e quiser recomeçar — ou para trazer melhorias que a BeeFood tenha feito nos textos
padrão depois que a sua conta foi criada.

---

## Ler o resultado

O botão **Resultado** mostra os números da campanha:

![Resultado de uma campanha](imagens-tratadas/18-resultado.png)

**Jornadas dos clientes** conta em que ponto cada cliente está: **CONVERTIDO** é quem recebeu e
comprou. **Envios** separa o que saiu (**ENVIADO**), o que falhou e o que foi ignorado pelas
regras. E o **ROI da automação** mostra o caminho de quem clicou no link: acessos, sacola,
checkout, pedidos e receita.

O botão **Histórico** mostra a lista de mensagens, uma por uma:

![Histórico de envios](imagens-tratadas/19-historico.png)

1. **Exportar CSV** baixa a lista para planilha
2. A coluna **Mensagem** mostra o texto exatamente como o cliente recebeu
3. **Converteu?** diz se aquela mensagem virou pedido

A coluna **Mensagem** é o melhor lugar para conferir se o seu texto está bom, porque ali as
variáveis já estão preenchidas e a variação automática já foi sorteada. No exemplo da imagem, o
texto cadastrado era `{Olá|Oi}, {{primeiro_nome}}! ... {Conclua|Finalize} agora ...` e o cliente
recebeu "Olá Bruno! 🛒 O seu pedido está quase pronto. Conclua agora...", seguido do link do
cardápio — e o pedido veio.

---

## Dicas para não perder o número

1. **Mantenha o Anti Banimento ligado.** É a proteção mais importante das seis campanhas.
2. **Use várias variações e variação automática.** Mensagem idêntica repetida é o padrão que o
   WhatsApp procura.
3. **Ritmo baixo.** Vale mais mandar 20 mensagens por dia durante uma semana do que 140 num dia.
4. **Respeite o horário de gente.** As campanhas padrão começam às 10h por um motivo.
5. **Revise o texto antes de ligar.** Leia em voz alta: se não parece coisa que você escreveria
   para um cliente, reescreva.
6. **Confira o Histórico depois dos primeiros dias.** É lá que você vê a mensagem real e
   descobre se algum trecho ficou estranho.
