# Programa de Pontos

- **Gênero:** novidade
- **Fonte:** [Programa de Pontos ⭐](https://beefood.app/novidades/programa-de-pontos)
  — 07/10/2026, áreas Marketing, Cardápio Digital, Mesas/Comandas e PDV;
  aplicativos BeeFood App, Cardápio Digital, Cardápio Digital Tablet e Totem.
- **Manual:** [Programa de Pontos](https://ajuda.beefood.com.br/programa-pontos)
  — na pasta,
  [`manuais/programa-pontos/`](../../manuais/programa-pontos/programa-pontos.md),
  com o [estudo de código](../../manuais/programa-pontos/fluxo-codigo.md) que
  leu o painel e o bundle publicado do cardápio.
- **Nome de venda × nome do release:** desta vez os dois são o mesmo —
  **Programa de Pontos**. É como o release batiza, como o menu escreve
  (*Fidelidade (CRM) → Programa de pontos*) e como o restaurante compra. A
  pergunta do passo 6a da skill foi feita assim mesmo, porque uma coincidência
  não dispensa a conferência.
- **Formato:** 1080 × 1350 (4:5)
- **Slides:** 8

## O acervo, antes de escrever

Onze peças entregues. Duas tocam este assunto, e de jeitos diferentes:

| Peça | O que ela já vendeu | O que esta peça faz com isso |
|---|---|---|
| **#9, Campanhas Inteligentes no WhatsApp** | o **motor**: seis campanhas de fábrica, quatro ligadas, o gatilho, a variação de texto, o Anti Banimento e o Resultado | aqui o motor não é o assunto. O slide 6 afirma uma coisa só, que é nova: o Programa de Pontos **chega plugado nele**, com público e campanha próprios já criados |
| **#11, Acompanhamento em tempo real** | a tela de **quem compra** como captura, e não como desenho | método reusado inteiro: o cardápio público aceita interceptação de API, e quem desenha a tela é o aplicativo de produção |

Nenhuma imagem foi reaproveitada: não há, em `carrosseis/*/imagens-puras/`,
uma única tela de fidelidade — nem de cashback, nem de pontos. As nove capturas
desta peça nasceram aqui.

**O erro documentado que esta peça herdou pronto** é o da #9: os cartões das
Campanhas Inteligentes declaram `R$ 0,00 de receita gerada`, e receita não se
monta — monta-se o recorte. O quadro do slide 6 fecha logo abaixo da descrição
da campanha, antes da linha do dinheiro.

**A capa não repete a forma da anterior.** A #11 usou *nome + para quem*. Aqui
o molde é **anúncio de chegada**, usado uma vez em onze peças (a #8, o Painel
para Entregadores) — é um módulo inteiro nascendo, e a notícia é literalmente
que ele chegou. Placar depois desta peça: afirmação do fato 5, pergunta 2,
anúncio de chegada **2**, nome + canal 1, nome + dois-pontos 1, nome + para
quem 1; ordem direta e antes × agora continuam em 0.

*Antes × agora* chegou a ser escrito e caiu, e vale registrar por quê: o par
natural aqui seria *"antes o cashback devolvia dinheiro, agora os pontos criam
uma meta"*. São duas frases verdadeiras e o molde faz as duas trabalharem
contra a peça — a primeira metade do título fala de **outro produto que a
BeeFood vende e continua vendendo**, e a #11 já tinha ensinado que o "antes"
ocupa a metade da linha que todo mundo lê.

## O fato, o ângulo, e o que o slide diz

| Fato (release + manual) | Ângulo | O que vira slide |
|---|---|---|
| Chegou o **Programa de Pontos**: o cliente acumula a cada compra e troca por **desconto em reais** ou por **produto grátis** | Um módulo de fidelidade inteiro nascendo. A capa anuncia o nome e o subtítulo entrega os dois eixos da troca | Capa |
| A faixa **Acumule pontos a cada compra** aparece na home do cardápio só por o programa estar ativo — não depende de o cliente estar identificado | A novidade se anuncia sozinha para quem abre o cardápio, sem a loja avisar ninguém | 2 |
| Você define **quantos pontos cada R$ 1,00 dá** (aceita casa decimal) e **por quantos dias eles valem**, contados **de cada crédito** | A régua é da loja, e a mesma conta aparece pronta na tela do cliente | 2 (corpo) |
| **Bônus de boas-vindas** na primeira compra, e acúmulo também **sobre a taxa de entrega** | Dois acréscimos opcionais que não pedem tela nova | 2 (corpo) |
| A vitrine lista cada recompensa com o preço em pontos e o selo **Disponível** ou **Faltam N pts** | O que separa ponto de cashback é a **meta**: a linha que ainda não dá é a que deixa um motivo marcado | 3 |
| Dois tipos de recompensa: **desconto em reais** (vale em qualquer cardápio) e **produto do cardápio grátis** | Recompensa de produto custa o preço de um lanche e vale, para quem recebe, um pedido inteiro | 3 |
| O resgate acontece **dentro da sacola**, depois da modalidade escolhida: **RESGATAR** no desconto que o saldo alcança, **ADICIONAR** no produto grátis, **INSUFICIENTE** no que não alcança | Ele não sai do pedido para trocar, e é por isso que a troca acontece | 4 |
| Resgatado, o **Total do pedido** cai na hora (R$ 29,00 → R$ 19,00) e o ganho do pedido **continua o mesmo** (29 pontos), porque é calculado sobre os itens | A recompensa de hoje não corta o acúmulo de amanhã | 5 |
| **Um resgate por pedido**: escolhida uma, as outras param de responder; e o ponto só sai do saldo **quando o pedido é fechado** | Sacola abandonada não gasta ponto de ninguém | 5 (corpo) |
| A aba **Saldo por Cliente** abre com **Total de Pontos** em circulação, **Clientes com Pontos**, **Total de Clientes** e **Média por Cliente** | É o tamanho do que a loja já prometeu em recompensa, numa linha | 6 |
| O olho de cada linha abre o extrato, e **ADICIONAR** credita na hora, com um **Motivo** que o cliente lê inteiro no celular | Cortesia por atraso vira crédito imediato, com a explicação junto | 6 (corpo) |
| O público **Pontos parados** e a **campanha de WhatsApp** que fala com ele **já vêm criados pela BeeFood**, ativos, usando o saldo de cada pessoa | Marketing que normalmente é projeto chega como item de lista | 7 |
| O módulo está em **Fidelidade (CRM) → Programa de pontos** | CTA: a decisão que ninguém pode tomar pela loja é **o que o cliente vai ganhar** | 8 (CTA) |

Os slides acima são doze linhas de fato para oito lugares — a tabela de slides
abaixo diz onde cada uma caiu.

**Ficou de fora, de propósito:**

- **o totem.** O release promete, no totem, *"selo nos produtos, pontos que o
  pedido gera e resgate na finalização"*. O
  [estudo de código](../../manuais/programa-pontos/fluxo-codigo.md) procurou
  `pontos` no bundle publicado do totem e achou **zero ocorrência**, e a seção
  12 do manual concorda: *o totem ainda não tem tela de pontos*. O que é
  verdade é que a venda do totem **acumula**, se o canal estiver ligado. A arte
  não afirma nem uma coisa nem outra, e a legenda fica com o acúmulo;
- **o selo de presente na foto do produto.** O release diz que ele marca os
  produtos **que pontuam**; a seção 6 do manual lê o mesmo selo como marca dos
  produtos **que são recompensa**. As duas não podem valer ao mesmo tempo, e a
  captura decide: na loja de exemplo **todos** os combos têm o selo e só um
  produto é recompensa. O selo aparece na imagem do slide 2 e **nenhuma frase
  da peça o explica** — quando duas fontes da casa discordam, a peça afirma a
  terceira coisa, que é o que a tela mostra;
- **o processamento da madrugada.** *"Só pedido pago e finalizado gera ponto, e
  o crédito acontece toda madrugada"* é o fato mais importante do suporte e o
  pior possível num slide: é a única parte do recurso que **demora**, e escrita
  antes do CTA planta a objeção. Está na legenda, onde quem publica responde se
  a pergunta vier;
- **a exclusividade com o cashback e a migração nos dois sentidos.** O fato é
  bom — ninguém perde saldo —, mas a frase que o carrega começa por *"você não
  pode ter os dois"*, que é limite, e a tela que o prova é a janela de
  conversão, que é configuração. Foi para a legenda, escrito como capacidade:
  o saldo atravessa de um programa para o outro;
- **a lista dos seis canais de acúmulo, um a um** (cardápio digital delivery,
  presencial, PDV, mesas/comandas, delivery manual e totem) e o fato de cada um
  ligar e desligar: é lista de interruptor, e interruptor é tela de
  configuração. Virou uma oração no corpo do slide 2 e uma linha na legenda;
- **o defeito do código do produto na recompensa de produto** (seção 5 do
  manual): é aviso de suporte, e peça de venda não carrega aviso. Ele está no
  `cena.json` porque mudou a captura, não porque vira texto;
- **a aba Fila Processamento, o Histórico e a correção de que `Usou` sai em
  verde no extrato do cliente**: material de quem atende.

## Slide a slide

| # | Arquivo | Título | Imagem |
|---|---|---|---|
| 1 | `01-capa.html` | Chegou o Programa de **Pontos** | `04-sacola-com-pontos.png` num `.celular` sangrando pela base — **captura** |
| 2 | `02-cada-compra-acumula.html` | Quem compra **acumula** a cada pedido, na conta que você definir | `rec-home-faixa.png` — **captura**, recorte |
| 3 | `03-recompensas.html` | **Recompensas**: o que dá para trocar, e quanto ainda falta | `rec-vitrine.png` — **captura**, recorte |
| 4 | `04-resgate-na-sacola.html` | **Resgate na sacola**: a troca acontece dentro do pedido | `05-sacola-resgatada.png` num `.celular` — **captura** |
| 5 | `05-total-do-pedido.html` | **Total do pedido**: o desconto entra na hora, e o ganho não muda | `rec-total-antes.png` + `rec-total-depois.png` — **captura**, dois recortes |
| 6 | `06-saldo-por-cliente.html` | **Saldo por Cliente**: quanto a sua loja tem de ponto em circulação | `rec-totais-painel.png` + `rec-linhas-cliente.png` — **captura**, dois recortes |
| 7 | `07-pontos-parados.html` | **Pontos parados**: o público e a campanha já chegam prontos | `rec-campanha.png` + `rec-segmentacao.png` — **captura**, dois recortes |
| 8 | `08-cta.html` | Escolha **hoje** a primeira recompensa | `04-sacola-com-pontos.png`, a mesma arte da capa |

São **oito** slides, e o teto da skill é 8. A conta de por que nenhum par se
funde está em *oito slides, e nenhum é de brinde*, abaixo.

Lidos em fila, os oito títulos montam a lista do que o módulo passou a fazer —
acumular, mostrar o que dá para trocar, deixar trocar dentro do pedido, descontar
na hora, medir o saldo em circulação e chamar quem parou. Nenhum tem pronome, e
o slide 2 é a exceção estrutural da regra do nome: ele explica o recurso que a
capa acabou de nomear.

## Decisões de arte

### Dez imagens, dez capturas, nenhuma tela de configuração

É a primeira peça da série em que **todas** as imagens são captura de resultado,
e isso não é mérito de disciplina: é que este recurso tem um lado de cliente
inteiro, e o lado de cliente é só resultado.

O inverso também vale, e era a armadilha. O Programa de Pontos é, do lado do
painel, **seis cartões de campo**: o switch de ativar, a régua de pontos por
real, a validade, as seis modalidades, os dois cartões de bônus e os dois
formulários de recompensa. São as telas mais fáceis de capturar da peça inteira
— abrem com um clique e não precisam de cena montada —, e são exatamente o que
a skill proíbe. Nenhuma entrou. O que entrou foi o **efeito** de cada uma:

| A configuração | O efeito que virou imagem |
|---|---|
| switch *Ativar programa de Pontos* | a faixa amarela na home do cardápio (slide 2) |
| *Pontos ganhos a cada R$ 1,00* e *Validade* | a frase pronta na vitrine, com o número e os dias (slide 3) |
| os dois formulários de recompensa | as quatro linhas da vitrine, com preço em pontos e selo (slide 3) |
| o cadastro visto do lado de quem compra | os botões **RESGATAR**, **ADICIONAR** e **INSUFICIENTE** na sacola (slide 4) |

### A recompensa de produto foi devolvida pela resposta da API

Entre a captura do manual e a desta peça, alguém trocou o cadastro da
recompensa de produto na sandbox. A que o cliente via — *Chicken Deluxe grátis*
por 100 pontos, `produtoID` **2515303** — saiu, e entrou uma gravada com o id
interno do painel (faixa 26xxxxx), que o cardápio público **descarta em
silêncio**. É o defeito 1 do
[`fluxo-codigo.md`](../../manuais/programa-pontos/fluxo-codigo.md), e ele
aconteceu ao vivo.

Sem a recompensa de produto, a vitrine fica só com os três descontos — e a peça
perde metade do eixo que a capa promete (*desconto **ou** produto grátis*). A
saída é a sancionada pela skill desde o totem: a resposta de
`GET .../pontos/recompensas/{filial}` é trocada dentro do Chromium da captura,
com **exatamente** o cadastro que o manual fotografou de manhã, e quem desenha
a tela é o cardápio de produção.

```python
ctx.route("**/pontos/recompensas/**",
          lambda rota: rota.fulfill(status=200, content_type="application/json",
                                    body=json.dumps(RECOMPENSAS)))
```

O `cena.json` registra linha por linha o que foi devolvido e por quê, e `--cru`
mostra a vitrine como ela está hoje. Nada é gravado em servidor nenhum: a única
chamada alterada é um `GET`.

### O pedido foi montado e não foi fechado

O slide 4 e o slide 5 mostram um resgate acontecendo, e resgate é passo que
mexe em saldo. O roteiro da captura **para antes de fechar o pedido**, que é a
técnica do ensaio da casa: o ponto só sai do saldo quando a venda nasce, e aqui
a venda não nasce. Os 121 pontos do cliente de teste estão intactos, e é isso
que mantém *Faltam 59 pts* sendo a mesma conta em todos os slides.

O produto do pedido é o lanche **Chicken Deluxe**, e não o *Combo Chicken
Deluxe*: o combo tem dois grupos de opções obrigatórios, e com eles o botão
*Adicionar* não responde. É a mesma regra que o manual dá ao lojista na seção 5
— recompensa de produto se escolhe entre itens sem obrigatoriedade —, encontrada
do lado de dentro.

E uma armadilha que o manual não pegou porque capturou de manhã: **fora do
horário a loja exige agendamento** antes de liberar a etapa dos pontos. Marcar
dia e hora e tocar em *AGENDAR PEDIDO* não cria pedido nenhum — é escolha
guardada na sacola —, e sem essa etapa o *Continuar* não sai da modalidade.

### A fonte dos ícones chegou depois do print

Uma rodada inteira saiu sem o selo de desconto, sem o presente e sem a estrela:
a vitrine ficou com quatro linhas de texto e nenhum ícone. Não é defeito do
produto nem do recorte — são glifos de **webfont**, e a fonte chegou depois do
print.

A espera de cinco segundos da casa não pega isso, porque ela conta do fim do
spinner e o spinner já tinha sumido. A captura ganhou um `assentar()` que espera
`networkidle`, depois `document.fonts.ready`, e só então os quatro segundos. A
lição é geral e subiu para a memória da skill: **espere a fonte, não só a
tela** — a tela sem ícone continua certa, e a prova, não.

### Sete recortes medidos, e por que cada um fecha onde fecha

Todos os cortes são medidos no DOM pela própria captura
([`medidas.json`](medidas.json)), nunca estimados na miniatura.

- **`rec-home-faixa.png`** começa logo acima da faixa amarela — o alto da tela
  fica **fora de propósito**, porque ali mora *"Fechado, abrimos Quinta às
  01:00"* em vermelho. É estado da loja de exemplo, não do recurso, e numa peça
  de venda a primeira coisa legível não pode ser a palavra *fechado*. E fecha
  no pé do **primeiro** cartão de produto: descer até o segundo partia a foto
  dele ao meio, e borda de recorte em cima de produto lê como erro de render.
- **`rec-vitrine.png`** vai de *Recompensas* ao pé da quarta linha, com as
  quatro inteiras. A folga do pé teve de ser medida duas vezes: a primeira
  fechava na **linha de texto** da última recompensa e cortava a borda do
  cartão dela.
- **`rec-total-antes.png`** e **`rec-total-depois.png`** saem com a **mesma
  caixa**, medida na mesma tela, e levam o botão *Continuar* no meio de
  propósito: ele é idêntico nas duas fotos, e é ele que faz o olho ir direto no
  número que mudou (R$ 29,00 → R$ 19,00) e no que não mudou (*Ganhe 29
  pontos*).
- **`rec-campanha.png`** começa na pílula **Ativo** e fecha logo abaixo da
  descrição da campanha, **acima** da linha `R$ 0,00 de receita gerada`. O
  começo é a prova (a campanha chega cadastrada, com o selo `BeeFood` e a chave
  ligada); o fim é a lição da #9 (receita não se monta, e `R$ 0,00` numa peça
  de venda desmente a peça).
- **`rec-totais-painel.png`** usa o **menor ancestral que contém os quatro
  cartões** nos dois sentidos, horizontal e vertical. Medido pelo texto, o
  quadro começava depois do ícone do primeiro cartão e o cortava ao meio.
- **`rec-linhas-cliente.png`** leva **duas** linhas da lista, e não a lista
  inteira: as outras contas da sandbox aparecem como `-`, e fila de traço não
  prova nada. A faixa dos totais sozinha deixava meio slide vazio; com as duas
  linhas, a imagem conta a frase inteira — o número da loja em cima, a pessoa
  com nome e saldo embaixo, que é de onde se abre o extrato. O rótulo do cartão
  é *Saldo total* no DOM, e o maiúsculo da tela é `text-transform`: ancorar o
  xpath em `SALDO TOTAL` não acha nada e estoura em *timeout*.
- **`rec-segmentacao.png`** começa na linha dos pontos, e não no alto da
  tabela: acima dela a sandbox tem *Cashback parado* **duas vezes**, e linha
  repetida num print de venda lê como defeito da tela. À direita ele fecha na
  borda da célula do criador, com folga **zero** — a célula já traz o próprio
  respiro, e somar folga deixava entrar uma lasca da coluna seguinte. Foi o que
  trouxe o `folga_lado` para o `recortar()`, ao lado do `folga_pe`.

### Os telefones saem borrados na imagem pura

A aba *Saldo por Cliente* lista clientes com telefone. O borrão é aplicado
**antes** do print, na própria pura — ela também é versionada, e o repositório é
público. O filtro pega só o **nó mais interno** de cada cadeia que casa com o
padrão de telefone: borrar o ancestral apagaria a linha inteira, com saldo e
tudo.

Os dois nomes que ficam legíveis — *Teste Manual* e *Bruno Pontos* — são contas
de teste da sandbox, criadas pelos manuais.

### Dois celulares e seis recortes

A capa e o CTA levam o celular inteiro; o slide 4 também, e os outros levam
recorte. O critério é o da skill: aparelho quando a capa quer reconhecimento,
recorte quando o que precisa ser lido é o texto da tela.

O slide 4 é a exceção entre os de dentro, e ela se paga: o assunto dali é que a
troca acontece **dentro do pedido**, e é a moldura do celular com a palavra
*Sacola* no alto que prova a palavra *dentro*. Recortado, o cartão de
recompensas poderia estar em qualquer tela.

A imagem da capa é a **sacola**, e não a vitrine, por um motivo de miniatura: o
cartão vermelho do alto dela escreve **Programa de Pontos ⭐**, e na capa isso
põe o nome do recurso dentro da própria prova. O corte da sangria cai logo
abaixo da lista de recompensas, bem antes do rodapé do total — que é justamente
o que o slide 5 mostra de perto, então nenhuma imagem repete outra.

### Oito slides, e nenhum é de brinde

A peça começou em sete e cresceu para oito na escrita, o que a skill manda
justificar. A pergunta é *quais dois slides entregam a mesma ideia de uso?*, e
o par candidato era o 4 e o 5 — os dois mostram a sacola.

Eles não se fundem porque respondem a perguntas diferentes do mesmo leitor. O
slide 4 responde *onde meu cliente troca?* (dentro do pedido, sem sair dele). O
slide 5 responde *quanto isso me custa?* (o desconto sai do total daquele
pedido, e o acúmulo continua inteiro). O primeiro é de uso, o segundo é de
conta — e é a conta que o dono do restaurante faz antes de ligar qualquer
programa de fidelidade.

Fundidos, sobraria um slide com dois assuntos e três imagens, e o que sairia da
peça seria a conta — que é a parte que vende.

### A capa: anúncio de chegada, e o eixo inteiro no subtítulo

> Chegou o Programa de **Pontos**
> Cada compra vira desconto ou produto grátis.

O título é o nome e a notícia; o subtítulo é o que ele faz, com os **dois**
eixos da troca. Concisão corta palavra, nunca eixo: *"cada compra vira
desconto"* entregaria metade do recurso, e a recompensa de produto é justamente
a que custa pouco para a loja e vale muito para quem recebe.

O vermelho pega **Pontos**, uma palavra só, e é a que o leitor vai procurar no
menu depois — que é a função que o destaque cumpre quando o recurso tem tela
própria (na #11 não tinha, e o vermelho foi para a notícia).

Nenhum emoji ao lado do vermelho, nenhuma data na arte, e o topo direito leva só
o contador.

### O CTA pede uma decisão, não um cadastro

O molde da série está lá — chapéu *Já está no ar*, imperativo com **hoje**,
primeiro passo no subtítulo e a pílula apontando para o módulo. O que mudou foi
o verbo.

*"Ligue o Programa de Pontos hoje"* é trabalho, e trabalho no último slide é a
fatura antes da venda. O primeiro passo que este recurso realmente exige da
loja não é mexer num switch: é **decidir o que o cliente vai ganhar**.

> Escolha **hoje** a primeira recompensa
> Desconto em reais ou produto do cardápio: essa escolha é sua.

O subtítulo retoma os **dois tipos de recompensa do slide 3**, e não a frase do
slide 7 — que é o que ele dizia na primeira versão, e que o leitor tinha
acabado de ler duas telas antes. Repetição colada não reforça, cansa.
