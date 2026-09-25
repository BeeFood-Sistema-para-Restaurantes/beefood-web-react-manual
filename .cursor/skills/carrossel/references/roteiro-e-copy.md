# Roteiro e texto do carrossel

Quem lê é dono ou gerente de restaurante, no celular, entre dois pedidos. Ele não
procurou esse conteúdo: ele tropeçou nele. Isso define tudo abaixo.

## O gênero muda o leitor

Duas coisas viram carrossel aqui, e a diferença entre elas não é o assunto, é
**com quem se fala**:

- **novidade** — um fato datado, publicado em `beefood.app/novidades`. Quem lê
  **já é cliente**: ele pode ligar o recurso hoje, e é por isso que o CTA é um
  caminho de menu.
- **função do sistema** — uma capacidade que já existe, quase sempre puxada de
  uma página de `beefood.com.br` (um segmento, um módulo, um tema). Quem lê
  **pode não ter conta**: está escolhendo sistema, comparando com o que usa
  hoje. Caminho de menu não serve de pedido para quem não tem painel.

O que muda na prática:

| | Novidade | Função |
|---|---|---|
| pílula da capa | `Novidade` | o tema (`Dark Kitchen`, `PDV`, `Fiscal`) |
| palavra proibida | — | "novidade", "agora", "acabou de sair" — o recurso pode ter anos |
| fato ancorado em | release + manual | manual quando existe; **senão, a tela** |
| CTA | `Cardápio Digital → Formas de Recebimento` | a página do site, ou criar conta |
| slide do limite | o erro de quem usa | o mesmo, e ele vale ouro aqui: quem está escolhendo sistema desconfia de peça sem limite |

O que **não** muda: a capa nomeia, o slide 2 explica, o slide 3 mostra, toda
afirmação é do produto e nenhuma frase sobrevive igual à da fonte.

### Página de vendas é pauta, não fato

A página do site é matéria-prima pior que o release, porque ela **já é copy** —
escrita para busca e conversão, com a manchete-conceito pronta ("Tudo que sua
Dark Kitchen precisa para vender mais"). Dela saem duas coisas: os **eixos** (o
que a operação precisa) e o **público**.

Separe o que a página tem de dois tipos:

| **Afirmação funcional** — serve | **Claim institucional** — não serve |
|---|---|
| "cada marca tem seu próprio cardápio, canais e relatórios" | "+100 mil negócios impactados" |
| "os pedidos dos marketplaces chegam numa tela só" | "sistema com melhor avaliação no Google" |
| "o estoque pode ser compartilhado entre as marcas" | "melhor suporte do Brasil" |

A coluna da esquerda é a empresa descrevendo o próprio produto: dá para afirmar,
e o `roteiro.md` anota que a fonte é a página. A da direita o leitor não tem como
verificar, e o teste *quem poderia desmentir isto?* derruba as três. Peça que
precisa de número de instituição para convencer é peça que não achou o que
mostrar na tela.

**Antes disso: confira se a página é mesmo a página.** Parte do site é uma
**casca** — o endereço público devolve menu, rodapé e um
`<div class="super-loader">Carregando…</div>`, e o conteúdo é montado por um
app externo cujo endereço está no próprio HTML. Foi o que aconteceu com o
totem: `curl`, navegador e REST do WordPress concordaram que a página estava
vazia, e a peça inteira foi escrita sem a seção de fidelidade, sem a
demonstração do aparelho e sem o FAQ que existiam lá.

O `pauta.py` já percebe a casca e segue o endereço, avisando na saída com
`O endereço público é uma casca; o conteúdo veio de …`. A pergunta que evita o
erro não é *"a página tem conteúdo?"*, é **"esta página se serve sozinha?"**.

**E página vazia de verdade não cancela a peça.** O gênero se define por **quem
lê**, não por a fonte ter texto: quem está escolhendo sistema continua
existindo. O que não pode faltar é o fato, e ele está na tela.

E **afirmar não é provar**: a prova visual continua vindo do manual, da tela
capturada ou da tela desenhada — nunca da arte da própria página, que é ilustração
de marketing.

### Quando não existe manual, o fato é a tela

Boa parte das funções mais vendidas não tem manual (multicardápio e KDS não
têm). A ordem de ancoragem passa a ser:

> **manual > tela do sistema, capturada ou reconstruída > código de referência.**

"Reconstruída" é o caso novo: quando o sandbox não tem o cenário (uma segunda
marca, um pedido de marketplace), a tela se **desenha em HTML/CSS** a partir do
que o produto realmente mostra — as capturas dos manuais, as imagens da página e
o layout real do painel. Desenho não é licença para inventar comportamento: o
que ele desenha é o que o sistema faz, e o `roteiro.md` diz, tela por tela, o que
é captura e o que é desenho.

Três regras do desenho, para ele não virar mentira bonita:

- **rótulo é o do sistema.** As colunas se chamam `Aguardando`, `Preparo`,
  `Pronto/Entrega`, `Entregue`, `Cancelado` porque é assim na tela — inventar
  nome de coluna é inventar produto;
- **número é exemplo, e é um jogo só na peça inteira.** Nem o do release, nem o
  da arte do site (`R$ 298.921,66` é ilustração de marketing, e na nossa arte
  viraria promessa de resultado);
- **a arte da página não entra recortada.** Ela é referência de layout, como o
  print do manual: leia, e desenhe a sua. Ver *o manual é referência, não acervo
  de imagem*, que vale igual para o site.

### "Fale de X dentro de Y": o fato está na lista de canais de X

Pedido comum, e o primeiro foi *"precisamos falar de cupom e cashback"* numa
peça sobre o **totem**. Os dois não são recursos do totem: são do
**Fidelidade (CRM)**, com manual próprio. Procurar o fato no assunto errado
(um manual do totem, que não existe) leva direto a escrever de cabeça.

O que autoriza a peça é o **canal**: o manual de `cupom-desconto` traz os
*Canais de Visibilidade* (e o totem está lá), o de `cashback-configurar` traz
as *Modalidades* (idem). A tela confirma o resto — como o recurso aparece
naquele aparelho.

E isso muda o que o slide diz. O título vira *"O seu cupom vale no totem
também"*, não "crie um cupom": o recurso é do outro módulo, e o que a peça
acrescenta é **onde ele também funciona**. Quem já usa reconhece a própria
ferramenta; quem não usa descobre que ela existe.

### O acervo é parte da pauta

A pauta tem duas metades. A primeira é a fonte — o release ou a página. A
segunda é **o que a casa já publicou**, e ela foi descoberta tarde: o pedido
que a criou foi *"precisamos criar uma memória de que, ao criar um carrossel,
estudamos todos os que já foram criados para encontrar implementações casadas
com as outras que já foram feitas"*.

O levantamento é barato e vem antes de escrever:

```bash
cat carrosseis/README.md                 # índice, com gênero e fonte de cada peça
ls carrosseis/*/slides/                  # que assuntos já viraram slide
ls carrosseis/*/imagens-puras/           # que provas já estão capturadas
ls carrosseis/*/*.json                   # dados de exemplo já montados
```

Depois abra o `roteiro.md` das peças do mesmo gênero e das que tocam o mesmo
módulo. Duas perguntas, e as duas mudam a peça nova:

1. **Quais provas já existem sobre este assunto?** No plural: liste todas antes
   de escolher, e escolha a que sustenta a manchete inteira.
2. **O que a peça vizinha já prometeu, e como esta se diferencia dela?**
3. **Que erro ela já cometeu neste assunto?** O `roteiro.md` de cada peça
   registra o que deu errado. Repetir um erro documentado é o desperdício mais
   caro do acervo.

#### Por que isso vale muito mais no gênero `função`

Uma **novidade** é um recorte no tempo. Ela tem um fato próprio, com data, e
reaproveitar prova de outra peça quase sempre significa falar de outra coisa —
o leitor veio ver o que mudou, e o que mudou é só aquilo. Ali o acervo serve
para **não repetir**, e pouco mais.

Uma **função** é um canal da mesma plataforma. Totem, tablet, QR Code e
aplicativo do garçom leem o mesmo cadastro, o mesmo cardápio, o mesmo programa
de fidelidade — então a prova de um módulo compartilhado é **verdadeira em
todos eles**, e recapturar produz o mesmo arquivo com outro nome. Aí o reuso
deixa de ser atalho e vira o que mantém as peças coerentes: quem acompanha o
perfil vê a mesma tela de cadastro na peça do totem e na do tablet, e entende
sozinho que é um sistema só. Capturar de novo, com outro produto e outro
recorte, ensinaria o contrário.

#### Levantar todas as candidatas antes de escolher uma

O acervo quase nunca tem **uma** prova do assunto. Tem duas ou três, capturadas
em peças diferentes, e a primeira que aparece na busca é a que tende a ser
usada — o que é sorte, não escolha. Liste todas antes de pegar qualquer uma, e
escolha por um critério só:

> **Qual delas prova a manchete inteira?**

No slide de idiomas do tablet havia duas candidatas, e elas provam coisas
diferentes:

| Candidata | O que prova | Serve à manchete "inglês e espanhol"? |
|---|---|---|
| print do cadastro do produto | **quem escreve** o texto, num idioma | metade |
| par do mesmo item nos dois idiomas | **que são dois**, com foto e preço intactos | inteira |

A primeira versão pegou o cadastro sem comparar, e o slide ficou prometendo dois
idiomas enquanto mostrava um. O carrossel da tradução **já tinha passado por
isso** e registrado no roteiro: *"a capa promete espanhol e o carrossel só
mostrava inglês; e a prova cabe numa imagem"*. Ler o roteiro da peça vizinha
teria poupado a rodada.

O que a candidata perdedora provava não some do slide — desce para o chapéu e
para o corpo, onde cabe sem imagem.

#### A pergunta que autoriza o reuso

> **Esta prova é do módulo, ou é do canal?**

Prova de **módulo** viaja: a tela do cadastro de produto, o modal de
configuração, o cartão de cupom. Prova de **canal** não viaja, mesmo quando é a
melhor candidata — os dois recortes do cartão em inglês e espanhol são do
**totem**, em cartão de grade, e o slide vizinho da peça do tablet mostra a
lista do tablet: lado a lado, a arte diria que são dois aparelhos.

**Quando a melhor prova é do canal errado, redesenhe em vez de trocar de
prova.** O par foi refeito com o componente de tela do tablet, a foto real da
biblioteca e o texto do arquivo de tradução da peça de origem — mesmo item,
mesma foto, mesmo preço, mudando a linha do nome e o botão. O que se reusa aí
já não é o arquivo: é a **ideia da prova**, que é o que a tornava boa.

#### Reusar é adaptar, e adaptar começa na ideia — não na frase

> **A prova viaja. O slide, não.** O slide reaproveitado é escrito do zero para
> responder a pergunta que **esta** peça deixou aberta, e não a que a peça de
> origem respondia.

É a parte que escapa, e escapou duas vezes seguidas no mesmo slide.

**Primeiro escapou a frase.** A imagem foi reusada com o texto junto, e saíram
duas peças dizendo *"toque na bandeira e escreva o nome do jeito que o turista
entende"* com as mesmas palavras.

**Depois escapou a ideia, que é pior** — porque parece resolvido. As palavras
foram todas trocadas e o **ângulo** continuou sendo o de lá: chapéu *"Sem
segundo cardápio"*, manchete *"O mesmo produto, com um campo a mais"*. Aquilo
responde o medo de quem ainda **não tem** o recurso e teme trabalho dobrado. O
leitor da peça do tablet está avaliando um **aparelho**, acabou de ver o cliente
trocando de idioma sozinho, e a pergunta que sobra é outra: *o meu cardápio vai
mesmo estar em inglês, e quem escreve isso?* A manchete virou **"Seu cardápio em
inglês e espanhol"**, e o corpo passou a entregar controle em vez de economia de
esforço.

Três perguntas antes de escrever o slide reusado, e a primeira é a que pega o
erro:

1. **Qual pergunta esta peça deixou aberta neste ponto do arco?** Escreva a
   pergunta, não o título. Se a resposta for a mesma da peça de origem, ou o
   slide está no lugar errado, ou ele não era necessário.
2. **O que muda no leitor?** Lá ele pode não ter o recurso; aqui pode estar
   escolhendo entre dois produtos da linha. Leitor diferente compra por motivo
   diferente.
3. **O remate ainda serve?** *"Os três idiomas acompanham"* é argumento de
   **esforço**; numa peça de canal, o que fecha é *"o mesmo texto serve o
   tablet, o totem e o QR Code"*, que ainda prepara o CTA.

#### O limite, esse viaja sempre

Se a peça de origem descobriu que a página promete tradução automática e o
manual diz que quem escreve é a loja, esse limite vale na peça nova também.
Prova reaproveitada sem a ressalva vira promessa nova.

E o limite costuma ser vendável do lado certo: em vez de *evitar* a frase da
página, o slide do tablet passou a dizer que o texto é **seu**, e não um chute
de tradutor. Mesma verdade, virada para a frente.

#### O conferidor mede a frase, você julga a ideia

Como a frase repetida passou batida, o `conferir-texto.py` passou a comparar a
peça com os outros carrosséis e avisar. É `AVISO` e não erro — o CTA repete de
propósito. Mas ele só pega palavra igual: **ângulo herdado ele não vê**, e é por
isso que as três perguntas acima existem.

#### Onde o slide reusado entra

Pela **função que ele cumpre no arco**, não pela ordem em que o cliente encontra
aquilo na tela. No tablet, o slide do cadastro entrou logo depois do slide de
idiomas: um mostra o que o cliente lê, o outro mostra onde aquele texto foi
escrito, e o par faz a virada do lado do cliente para o lado do dono, que o
slide do painel completa.

## A novidade é matéria-prima, não roteiro

O texto publicado em `beefood.app/novidades` é registro de release: descreve o
**campo**, a **tela** e o **efeito**, na ordem em que o produto foi construído.
Carrossel não é isso. Recortar aquele parágrafo em oito pedaços e centralizar
cada pedaço num slide produz um changelog paginado, que ninguém arrasta.

O carrossel é uma **publicação nova, escrita a partir do fato**. Método:

1. **Extraia o fato, inteiro.** Em três linhas, sem adjetivo: o que mudou, onde
   fica, o que passa a acontecer, e qual o limite. Isso vem da novidade e do
   manual. Inteiro é a palavra que faz trabalho aqui — ver *o fato inteiro, e o
   exemplo não é o fato*.
2. **Ache o ângulo dentro do fato.** Qual custo ou situação do restaurante esse
   fato **resolve**? A bebida que fica na geladeira. A comanda que ninguém sabe
   se saiu. O custo que entra duas vezes no DRE. O ângulo se escreve no
   vocabulário do salão, e não no do sistema — mas ele sai do que o recurso faz,
   nunca de um hábito que a gente supõe que o leitor tem. Ver *tudo o que o
   slide afirma é do produto*.
3. **Escreva da cena para a tela**, nunca o contrário. O nome do campo aparece
   quando o leitor já quer saber onde fica: slide 4, não slide 1.
4. **Nenhuma frase sobrevive igual.** Se uma frase do carrossel também está no
   texto da novidade, ela não foi escrita — foi copiada. Reescreva.

O `roteiro.md` registra as três etapas numa tabela **fato → ângulo → o que o
slide diz**. Isso é o que permite a outra pessoa auditar a reescrita: ela vê que
nada foi inventado, e vê que nada foi copiado.

### Exemplo

| Fato (da novidade) | Ângulo | O que o slide diz |
|--------------------|--------|-------------------|
| Campo novo "Destaque na impressão" no cadastro de produto e complemento | todo mundo tem uma gambiarra caseira para não esquecer a bebida | "Toda loja tem uma gambiarra para não esquecer a bebida" |
| A linha sai com fundo escuro e letra clara | o cupom trata todas as linhas igual, e por isso a bebida some no combo | "Um esquecido custa duas viagens" |
| Usar com critério; marcar tudo anula o efeito | destaque funciona por contraste | "Se tudo é destaque, nada é" |

## Tudo o que o slide afirma é do produto

A frase que derrubou o carrossel de *desconto por forma de pagamento* foi o
slide 2: **"Você já faz isso no balcão. No caixa você propõe na hora: no Pix eu
tiro 5%."** Está em português claro, fala com o leitor, elogia antes de cobrar e
cumpre todas as regras de tom deste documento. E é invenção: nem a novidade nem
o manual dizem que o dono negocia forma de pagamento no balcão. Eu escrevi um
cenário e o afirmei como fato, no slide em que o leitor decide se arrasta.

A checagem já tinha a linha certa — *toda afirmação está na novidade ou no
manual* — e ela passou, porque eu li "afirmação" como afirmação **sobre o
sistema**. Não é. A regra vale para tudo, e o que mais escapa é a afirmação
sobre **o leitor**.

> Teste de uma pergunta: **quem poderia desmentir esta frase?**
>
> Se o leitor pode responder "não, eu não faço isso", a frase é invenção — e sai
> caro, porque ela vem justamente no slide em que ele decide continuar. Frase
> sobre o produto ninguém desmente: está na tela.

A fronteira é o sujeito da frase, e ela é fina:

| Sobrevive | Não sobrevive |
|---|---|
| "Seu cardápio é o seu melhor **vendedor**" — descreve o cardápio: foto, descrição, combo e adicional estão na tela | "Você já faz isso no balcão" — descreve **ele**, e nada na tela sustenta |
| "O mesmo pedido fecha em dois totais" — está no cardápio, conferido | "Você negocia na boca do caixa" — pode ser verdade em uma loja e ofensa em outra |
| "A taxa do crédito sai do subtotal" — é a conta que o sistema faz | "Isso te incomoda desde que você abriu a loja" — biografia |

Por isso o *elogie antes de cobrar* tem um limite que faltava: **elogie uma coisa
do produto que ele já usa**, não um hábito que a gente imaginou. E o molde do
"reconhecimento do que ele já fez" ("Você já fez a parte mais difícil") só serve
quando o que ele fez está no sistema — cadastrou o produto, subiu a foto, ligou
o cardápio. Fora disso é ficção com a cara de empatia.

Isto **não** proíbe falar do salão. O ângulo continua sendo o custo reconhecível,
e ele se escreve com as palavras do dono. O que muda é que a frase nomeia o
custo sem afirmar o que ele faz com ele: "a taxa do crédito sai da sua margem em
todo pedido" é o custo, é verdade e é do produto; "você já tentou resolver isso
na boca do caixa" é a história que eu inventei em volta.

## O fato inteiro, e o exemplo não é o fato

A capa do mesmo carrossel saiu **"Dê 5% de desconto no Pix"**. A novidade se
chama *Desconto **ou acréscimo** por forma de pagamento*, e o "ou" é a notícia:
o ajuste vai nos dois sentidos, em porcentagem **ou** em reais. A capa entregou
um quarto do recurso e, pior, entregou a frase que estava no release como
**exemplo** — "Exemplos: 5% de desconto no Pix, R$ 3,00 de desconto no dinheiro
ou 2% de acréscimo no crédito".

Duas regras saem disso.

**Exemplo da novidade não é fato da novidade.** A lista de exemplos existe para
mostrar a **amplitude**; promover um deles a manchete transforma a amplitude num
caso único. Quem lê "5% no Pix" entende "deu para dar desconto no Pix", e o que
entrou no sistema foi bem maior. Exemplo serve para a imagem e para o corpo do
slide, nunca para a capa.

**Concisão corta palavra, não corta eixo.** Três regras deste documento empurram
a capa para o osso — ela é a frase mais curta, tem uma palavra em vermelho, cada
palavra que sai é ganho — e nenhuma delas dizia onde parar. Agora diz: antes de
cortar, escreva o fato em uma linha **com todos os eixos**, e depois corte só
palavra.

Eixo é o que tem um "ou" (ou um "e") no título da novidade e muda **quem** se
interessa pelo post:

- *desconto ou acréscimo* — quem quer repassar a taxa do crédito não tem
  interesse nenhum num post sobre desconto;
- *em % ou em R$* — R$ 3,00 fixos são a régua de quem tem ticket baixo;
- *no cardápio, no totem, no caixa e no chat* — quem não tem delivery para de
  ler na primeira linha se a capa disser "cardápio digital".

E o corte não é só de texto: **a imagem da capa também carrega os eixos.** Um
total com desconto mostra um sentido; a lista de formas com um selo de desconto
numa e um de acréscimo na outra mostra o par inteiro, na mesma imagem e sem
palavra a mais.

| Amputado | Inteiro, e do mesmo tamanho |
|---|---|
| "Dê 5% de desconto no Pix" | "Acréscimo e desconto por **forma** de pagamento" |
| capa com o total abatido no Pix | capa com a lista de formas, desconto numa e acréscimo na outra |

## Nomear o recurso é o começo de vender

A correção acima foi feita uma vez pelo caminho errado, e a capa saiu **"Cada
forma de pagamento com o seu preço"**. Tem os três eixos, não copia o release,
não inventa nada sobre o leitor — e não diz o nome de coisa nenhuma. O dono leu
e devolveu: *"isso foge da funcionalidade"*.

É o que acontece quando *concisão corta palavra, não corta eixo* encontra a
regra que esta skill tinha então — *a capa não anuncia a funcionalidade, ela
nomeia um incômodo*: para caber todo mundo sem dizer o nome de ninguém, a frase
sobe um degrau de abstração e vira conceito. Conceito é bonito, é verdadeiro, e
o leitor não sabe o que o sistema passou a fazer. Aquela regra **caiu** — hoje
a capa de novidade anuncia, e o começo desta seção diz como —, mas o caminho
que ela abria continua tentador, e é por isso que o caso fica registrado.

> **Fugir do changelog nunca foi esconder o nome do recurso.** Changelog é
> recortar o texto do release nos oito slides. Dizer na capa o que o recurso faz
> é o contrário disso: é a notícia.

| Conceito (a peça devolvida) | Nome (a peça que foi) |
|---|---|
| "Cada forma de pagamento com o seu preço" | "Acréscimo e desconto por **forma** de pagamento" |
| "O pedido tinha um preço só" | "O ajuste fica no cadastro da **forma**" |
| "Comece pela forma que mais entra" | "Ligue o primeiro **ajuste** hoje" |

Os três pecados são o mesmo: metáfora ("preço", "o que mais entra") no lugar da
palavra que o recurso usa ("desconto", "acréscimo", "ajuste"). Quando existir
uma palavra concreta para a coisa, ela ganha da imagem poética — **sempre**.

### O nome vai inteiro, e o canal faz parte do nome

"As **Campanhas Inteligentes** já estão trabalhando" tem nome próprio no título
e passa nas duas perguntas do teste da capa. Voltou assim mesmo: *"faltou
clareza, são campanhas inteligentes no whatsapp"*.

O que faltava é **onde**. "Campanhas Inteligentes" não diz o meio — podia ser
e-mail, push, SMS, cartaz na porta —, e o meio é o que explica por que a
mensagem chega e por que ela é lida. O release chama a coisa de "Campanhas
Inteligentes no WhatsApp"; o "no WhatsApp" é eixo, e concisão corta palavra,
nunca eixo. Deixar o canal para o subtítulo não resolve: subtítulo se lê depois,
e quem passa o dedo leu só a primeira linha.

> Leia só o título e pergunte: **onde isso acontece?** Recurso que roda num
> canal só e não nomeia o canal deixa a pergunta em pé.

### E a regra do nome vale para os slides de dentro, não só para a capa

Esta seção existia inteira e endereçada só à capa. O efeito apareceu na décima
peça, num retorno de seis linhas em que o dono leu slide por slide:

| O que o slide dizia | O que ele devolveu |
|---|---|
| 3 · "No pico, a rota já chega montada" | *"Roteirização automática de pedidos — por que não usamos isso?"* |
| 7 · "Quanto da entrega é cozinha, e quanto é rua" | *"Relatórios… deveria ser esse o título vendedor"* |
| 8 · "Escolha como pagar, e o relatório fecha a conta" | *"também igual 7"* |

As três frases recusadas são boas frases. Nenhuma copia a fonte, todas dizem
uma verdade do produto e todas têm ângulo. O que falta nas três é a **mesma
coisa que faltava na capa de "Cada forma de pagamento com o seu preço"**: o
nome. Eu tinha escrito a regra e aplicado a um slide só — a capa —, e nos
outros oito continuei livre para ser esperto.

**A capa nomeia o módulo; cada slide de dentro nomeia o recurso que ele mostra.**
São nomes diferentes, e o de dentro é o que o leitor vai procurar no menu na
segunda-feira. "A rota já chega montada" não se procura; "Roteirização
automática" se procura. E é ele, não o ângulo, que o leitor repete quando conta
para o sócio o que viu no Instagram.

O molde que resolveu, e que serve como padrão: **nome, dois-pontos, o que ele te
dá.**

| Recusado | Publicado |
|---|---|
| "No pico, a rota já chega montada" | "**Roteirização automática**: a rota já chega montada" |
| "Quanto da entrega é cozinha, e quanto é rua" | "**Relatório de Operação**: quanto é cozinha, quanto é rua" |
| "Escolha como pagar, e o relatório fecha a conta" | "**Relatório do Entregador**: quanto pagar a cada um" |

O ângulo não foi jogado fora em nenhuma das três: ele virou a segunda metade do
título, que é onde ele sempre devia estar. Dois-pontos custa duas letras e paga
o nome inteiro.

> **O chapéu não conta como nome.** Ele é o rótulo pequeno em versalete, lido
> depois do título quando é lido, e a checagem de três leituras desta skill
> passa *só pelos títulos* justamente porque é assim que o feed se lê. Nome que
> está só no chapéu é nome que não foi dito.

A exceção é **uma**, e ela é estrutural: o **slide 2 explica** o recurso que a
capa acabou de nomear, e repetir o nome duas telas depois soa como gagueira.
Ali o título é a explicação — "O mapa mostra onde. A lista mostra quem leva."
Do slide 3 em diante, cada um mostra uma coisa diferente, e cada coisa tem nome
próprio.

O teste que fecha a regra: **leia os títulos em fila, sem as imagens.** Sai uma
lista do que o módulo passou a fazer, ou sai uma sequência de frases bonitas
sobre entrega?

| Só ângulos (a peça devolvida) | Com nome (a peça que foi) |
|---|---|
| No pico, a rota já chega montada | Roteirização automática |
| Online, em pausa ou offline — quem marca é ele | Situação do entregador, declarada por ele |
| A rota que você montou abre no celular dele | BeeFood Entregador |
| Dois telefonemas a menos em cada entrega | Avisos no WhatsApp |
| Quanto da entrega é cozinha, e quanto é rua | Relatório de Operação de Entrega |
| Escolha como pagar, e o relatório fecha a conta | Relatório do Entregador |

A coluna da direita é o que o leitor vai procurar no menu, e é o que ele repete
quando conta para o sócio o que viu. A da esquerda não se procura.

E um efeito colateral bom: com o nome no título, o chapéu para de ser
obrigado a carregá-lo — e para de virar nome de janela ("Despacho automático")
ou de item de menu ("Operação de entrega"), que a checagem já proibia e que
passou nove peças porque não havia para onde mover o nome.

### Pronome no título é sempre erro

Do mesmo retorno, outras duas linhas:

| O que o slide dizia | O que ele devolveu |
|---|---|
| 4 · "Online, em pausa ou offline — quem marca é ele" | *"quem marca é ele, ele quem?"* |
| 5 · "A rota que você montou abre no celular dele" | *"abre no celular dele quem? que frase estranha"* |

Nos dois casos o antecedente existia — "o entregador" estava no chapéu do slide
4 e no do 5, e estava na legenda, e estava no slide anterior. E não serve de
nada, porque **o título é a única parte do carrossel que se lê fora de ordem**.
Ele aparece sozinho na miniatura do feed, sozinho na folha de contato, sozinho
quando alguém passa o dedo rápido e para no meio. Um slide não é um parágrafo de
um texto corrido: é uma unidade que precisa fechar em si.

Daí a regra, sem exceção que valha o risco:

- **no título, nenhum `ele`, `dele`, `dela`, `isso`, `aquilo`, `o dele`.** Se a
  frase precisa da pessoa, a pessoa é nomeada ali: "quem marca é **o
  entregador**", "chega ao **celular do entregador**";
- **no corpo, o pronome exige o substantivo antes dele, no mesmo slide.** "Ele
  escolhe a situação no aplicativo" funciona embaixo de um título que diz *o
  entregador*; a mesma frase embaixo de um título que diz *a rota* troca de
  sujeito sem avisar;
- **`você` é o leitor, e só ele.** Essa parte a skill já tinha, e continua: o
  dono do restaurante é `você`, quem compra dele é nomeado pela ação.

> Leia cada título em voz alta, sozinho, sem o chapéu e sem o slide anterior.
> Se sobra uma pergunta de *quem?* ou de *o quê?*, o título está incompleto —
> não ambíguo, incompleto.

### Frase de manchete de jornal não é frase de carrossel

A terceira linha do retorno foi a mais dura, e é sobre gramática:

> *"a copy ficou estranha: título 'dois cadastros e o entregador já entra no
> mapa' e 'lista vazia com a pílula verde é sinal que deu certo'. Como estamos
> chegando num texto tão tosco assim?"*

O defeito tem nome em jornalismo: **estilo telegráfico**. Manchete de primeira
página corta artigo, corta verbo de ligação e empilha substantivo, porque ela
paga por centímetro de coluna. Carrossel não paga por centímetro, e a voz dele é
a de uma empresa conversando com um cliente — a mesma que a seção *fale como
gente fala* descreve. Cortar artigo naquela voz não soa econômico, soa mal
escrito.

| Telegráfico | Como gente fala |
|---|---|
| "Lista vazia com a pílula verde é sinal que deu certo" | "A lista vazia do primeiro acesso quer dizer que deu certo" |
| "Dois cadastros, e o entregador já entra no mapa" | "O entregador entra no mapa com dois cadastros que já existem" |
| "Na ordem que a loja definiu, com o número do pedido e a previsão" | "Ela chega na ordem que a loja definiu, com o número do pedido e a previsão" |
| "Quatro etapas medidas uma por uma, o tempo de loja separado do de rua" | "A entrega vem quebrada em quatro etapas, com o tempo de loja separado do de rua" |

Três coisas concretas, e as três aparecem na tabela:

- **artigo não se corta para ganhar linha.** "Lista vazia" pede "a lista vazia".
  Se com o artigo a frase estoura o bloco, o problema é o tamanho da frase, e o
  conserto é cortar conteúdo — nunca gramática;
- **`que` de ligação não se come.** "é sinal **que** deu certo" quer "é sinal
  **de que** deu certo", e a saída melhor é trocar o substantivo por verbo:
  "quer dizer que deu certo";
- **frase sem verbo principal não é frase.** Corpo que começa em "Na ordem
  que…", "Pela taxa cobrada…", "Quatro etapas medidas…" é uma legenda de foto
  colada no lugar de um parágrafo. Ele lê como anotação, e anotação é o que
  produz a sensação de "texto tosco".

> **O teste é a voz alta, e é o único que pega isto.** Erro de concordância e
> frase sem verbo passam batidos na leitura silenciosa, porque quem escreveu
> sabe o que quis dizer. Leia o slide inteiro em voz alta, no ritmo de quem
> conversa. Onde a respiração tropeça, falta palavra.

## O alvo de cada slide: a utilidade

Leia isto antes de escrever a primeira palavra. Tudo o que vem depois neste
documento é consequência daqui.

A pergunta na cabeça de quem lê é uma só:

> **"Isso serve pra quê na minha loja?"**

Não é "onde eu clico" — isso é o manual. E não é "como é a cena do meu cliente
comendo" — isso é comercial de agência. O slide entrega **uma ideia de uso e o
que ele ganha com ela**.

A frase-régua, para calibrar o ouvido:

> "Destaque o combo do dia no meio do cardápio."

Ela entrega uma coisa que vale a pena fazer, e o dono já se vê fazendo. Ela não
tem: nome de campo, passo a passo, cena em close, adjetivo de venda.

### As duas valas

O texto cai sempre para um dos dois lados da estrada, e a segunda vala é a mais
difícil de ver, porque parece boa escrita.

| Vala | Como soa | O que já escrevemos assim |
|---|---|---|
| **Manual** — ensina a mexer | nome de campo, ordem de tela, enumeração de opção | chapéu "Agendamento"; "Você marca em que dias a mídia aparece, de que horas a que horas, e se ela vale no delivery, no salão ou nos dois" |
| **Cinema** — narra a cena em close | dedo, boca, chapa, queijo derretendo; o cliente como personagem de filme | "Aí quem abriu o link só para ver o preço fica olhando a carne na chapa"; "Seu cliente rola o dedo e acha o combo" |

A vala do cinema aparece justamente quando a gente tenta fugir da do manual.
Fugir de uma não é cair na outra: as duas soam artificiais, uma por ser técnica
demais e a outra por ser teatral demais.

### Entregue a ideia, não a permissão

"Você pode pôr um banner no meio do cardápio" avisa que o recurso existe e pede
licença. "Destaque o combo do dia no meio do cardápio" entrega a ideia pronta. É
a mesma informação, e só a segunda faz o dono pensar no cardápio dele.

Por isso **o verbo vem na frente e mira nele**: destaque, mostre, programe, suba,
apague, comece.

E isto **não é molde**. "Você pode ___ para ___" foi uma tentativa intermediária
e virou cacoete em cinco dos sete slides, uniforme do mesmo jeito que o gabarito
que ela vinha substituir. Sete imperativos em fila seriam template igual.

A regra que sobra é sobre o conjunto, e não sobre a frase: **nenhuma abertura se
repete.** Se dois blocos começam do mesmo jeito, é cacoete, mesmo que a abertura
seja boa. Varie entre o imperativo, o ganho dito direto ("Combo de quarta aparece
só na quarta") e o reconhecimento do que ele já fez ("Você já fez a parte mais
difícil").

"Você" não está proibido, e não é cota a cumprir: a linha que faz o dono se
reconhecer tem "você" e fica. O que não serve é a moldura da permissão e a
abertura repetida.

### Clareza vem antes de tudo

Ordem de prioridade quando duas versões competem. Ela decide sozinha quase toda
dúvida de escrita.

1. **Antes da piada.** "Combo de quarta aparece só na quarta" venceu "Na quinta
   você nem lembra": a segunda é mais engraçada e não diz o que o recurso faz.
   Piada entra quando ela **também** é clara — "Recado não é produto de R$ 0,00"
   diz, na mesma frase, a gambiarra de hoje e o que mudou.
2. **Antes de qualquer cota de sujeito.** Se a frase mais clara tem o recurso
   como sujeito, ela fica. O problema nunca foi a gramática: foi a frase não
   dizer para que serve.
3. **Antes da originalidade.** Frase simples e direta vence frase interessante.

### O registro muda com a voz

Um carrossel sobre mídia tem **duas vozes**, e o que serve para uma soa errado na
outra:

| | Quem fala | Com quem | Registro |
|---|---|---|---|
| **slides** | a BeeFood | o dono do restaurante | claro, amigável e correto: "Suba o seu primeiro vídeo hoje" |
| **artes de mídia** | o dono da loja, no cartaz dele | alguém com fome | cartaz de rua, imperativo curto: "Pede a grande. Confia." |

O imperativo truncado é a marca do cartaz e o erro do slide: "Pede a grande"
funciona na arte da hamburgueria, e "Sobe o primeiro vídeo" soa estranho vindo da
BeeFood, porque ali quem fala é uma empresa conversando com um cliente dela.

### Palavra do dono, palavra do sistema

Não é lista para consultar, é a pergunta: **essa palavra está na boca de quem
fala?** O dono diz foto, vídeo, banner, cartaz, aviso, combo, preço, cardápio.
Ele não diz mídia, destaques, agendamento, carrossel da capa. Quando o termo do
sistema for inevitável, porque é onde ele vai clicar depois, escreva com a
palavra dele e deixe o nome do campo para o slide do caminho de menu.

O caso mais caro disso foi uma arte: "a partir de R$ 44,90" não foi escolha de
redação, é a **string da interface** do cardápio, que aparece doze vezes na
página. Sem declarar quem fala, quem fala é o sistema — ele é o que está na tela
enquanto a gente escreve.

### "O cliente" é quem lê — o comprador dele precisa de outro nome

"Quem marca a hora de falar é **o cliente**" quer dizer que o disparo é o
comportamento de quem compra, e não a agenda do dono. O que ela diz é outra
coisa, e o retorno foi imediato: *"mas quem tá lendo já é o cliente"*.

Nas peças em que o recurso fala com o consumidor final — campanha, cardápio,
tradução, totem —, a palavra **cliente tem dois donos**: quem lê é cliente da
BeeFood, e quem larga a sacola é cliente dele. Solta, com artigo definido, ela
cai no leitor.

Duas saídas, e a segunda é melhor:

| Ambíguo | Com dono | Nomeado pela ação |
|---|---|---|
| "o cliente escolhe a hora" | "seu cliente escolhe a hora" | "quem largou a sacola" |
| "avisa o cliente que sumiu" | "avisa o seu cliente que sumiu" | "quem não pede há trinta dias" |

A ação ganha porque paga duas dívidas com a mesma palavra: sai a ambiguidade e
entra prova — "quem recebeu o cardápio e não pediu" é, palavra por palavra, o
nome do cartão na tela. E ela tem limite: nomear pela ação é dizer o que a
pessoa **fez no sistema**, não narrar a pessoa. "Quem está com o dedo no
carrinho" é a vala do cinema outra vez.

> Procure "o cliente", "os clientes" e "do cliente" antes de renderizar. Em cada
> aparição, responda: **cliente de quem?** Se a resposta é "do leitor", falta o
> possessivo ou falta a ação.

## A regra do primeiro segundo

### Em peça de novidade, a capa ANUNCIA — e anunciar tem duas obrigações

Anunciar não é uma fórmula, é um resultado: quem leu só o slide 1 sai sabendo
**o nome da coisa que chegou** e **o que ela faz**. A primeira obrigação é do
título, a segunda é do subtítulo. A **forma** de dizer varia peça a peça, e tem
de variar — os moldes estão logo abaixo, e a regra de não repetir a forma
continua valendo.

O que não varia é o nome. Ele importa depois do post: é a palavra que o leitor
vai procurar no menu, digitar no suporte e ouvir do vendedor. A capa é onde ele
aprende essa palavra, e é o nome próprio mesmo — "Painel para Entregadores",
"Destaque na impressão" —, não uma paráfrase bonita da capacidade.

**O subtítulo tem obrigação, e a obrigação é explicar.** Não é onde a frase
"respira" nem onde o tom se recupera: é a linha em que o leitor descobre o que
a coisa anunciada faz. Uma frase, concreta, sem metáfora.

#### O erro do meio, que é o que esta skill vinha produzindo

Há três degraus, e o vício mora no segundo — o mais difícil de ver, porque ele
tem cara de texto bem escrito:

| Degrau | Exemplo | Por que falha |
|---|---|---|
| changelog | "Nova etapa Pronto no Delivery" | nomeia a tela: só entende quem já usa |
| **enigma** | "O entregador chega e vê sozinho se o pedido já saiu" | descreve a cena e **não diz o nome de nada** |
| anúncio | "Chegou o Painel para Entregadores" | diz o que chegou; o subtítulo diz o que faz |

O enigma engana porque é a frase mais gostosa das três. Ela é concreta, tem
cena, tem promessa, passa no teste de "não soa como changelog" — e o leitor
termina o carrossel sem saber o nome do que foi anunciado.

**Cena do release é matéria-prima do slide 2, não da capa.** Quase todo release
abre com uma: o entregador que interrompe a cozinha, a bebida esquecida na
sacola. Ela é boa e vai ser usada — na introdução, onde há espaço para
contá-la. Na capa, ela ocupa o lugar do nome.

#### O nome atravessa os seis moldes; nenhum deles dispensa

Os moldes estão em *o quarto vício* e *o sétimo vício* da
[`MEMORIA-CARROSSEIS.md`](MEMORIA-CARROSSEIS.md), com o placar de uso. O que
faltava era isto: **a escolha do molde é livre, a presença do nome não é.**

| Molde | Como ele nomeia |
|---|---|
| nome do recurso como ganho | o título **é** o nome ("Acréscimo e desconto por forma de pagamento") |
| anúncio de chegada | o verbo de chegada mais o nome ("Chegou o Painel para Entregadores") |
| afirmação do fato | o nome entra na frase, ou vai para o chapéu |
| ordem direta | idem — e só quando o recurso tem um objeto só |
| antes × agora | idem |
| pergunta | o título não comporta o nome: ele vai para a pílula ou para o chapéu |

**Quando o título não comporta o nome, a pílula leva** — e é aqui que os dois
gêneros se separam, o que explica por que o vício só acontece em novidade:

- em **peça de função**, a pílula é o tema, e o tema é o nome: `Totem de
  Autoatendimento`, `Cardápio Digital no Tablet`, `Dark Kitchen`. O leitor já
  tem o nome antes de ler o título, e o título fica livre para vender o uso;
- em **novidade**, a pílula está ocupada pela palavra `Novidade`, que anuncia o
  gênero e não nomeia coisa nenhuma. **Não há para onde empurrar o nome:** ou
  ele está no título, ou a capa não tem nome.

Por isso a exigência pesa mais na novidade, e por isso ela falhou lá — três das
quatro primeiras novidades saíram sem o nome em lugar nenhum, enquanto as três
peças de função saíram todas nomeadas, sem ninguém ter combinado isso.

**Condição de uso do anúncio de chegada:** ele pede um recurso **batizado**, com
nome próprio que vira item de menu. "Chegou o Painel para Entregadores"
funciona; "Chegou o acréscimo por forma de pagamento" soa torto, porque ali não
chegou um objeto, mudou uma capacidade — e para esse caso o molde certo é o
nome do recurso como ganho.

#### O teste da capa, agora com duas perguntas

Tape o resto do carrossel e leia só o slide 1:

1. **Qual é o nome da coisa que chegou?** Se você não consegue repetir o nome,
   a capa não anuncia nada.
2. **O que ela faz?** Se a resposta depende de arrastar, o subtítulo não
   cumpriu a parte dele.

Uma resposta só não basta — foram capas que respondiam a segunda e não a
primeira que motivaram esta seção. E leia em voz alta: se soa como changelog
("Novo campo X na tela Y"), reescreva; se soa como enigma, também.

#### E tem uma terceira pergunta, que só a folha de contato responde

As duas acima se fazem no texto. Esta se faz com a peça inteira renderizada:

> **Se você só pudesse publicar um slide, qual seria?**

Se não for o 1, a capa está entregando o segundo melhor. É o que aconteceu nas
Campanhas Inteligentes: *"slide 3 é o mais legal, deveria ser o 1"* — e era, os
seis cartões com nome, gatilho e estado são a única imagem que dá o tamanho do
recurso de uma vez.

A causa é de ordem de trabalho, não de gosto: **a capa se escreve no roteiro,
antes de existir uma captura para comparar.** Ela é a melhor ideia que se tinha
no começo, e a melhor prova aparece depois.

Promover não é trocar dois arquivos de lugar. A capa tem obrigações que o slide
do meio não tem — nome do recurso, subtítulo que explica, pílula, nenhum bloco
de corpo —, então o que sobe é **a prova**: a imagem forte vai para a capa e o
texto dela se reescreve em volta. O slide que ficou sem prova quase nunca tem
assunto próprio para continuar, e sai. Peça de seis slides com o mais forte na
frente vale mais que sete com o mais forte no meio; é para isso que o intervalo
vai de 6 a 8.

#### A quarta e a quinta: quem é o sujeito, e de onde veio o nome

As três perguntas acima aprovaram uma capa que voltou mesmo assim. A do
acompanhamento em tempo real dizia:

> A mesma mensagem, agora com **rastreio da entrega**
> No WhatsApp, quem pediu abre o mapa ao vivo

Ela tem nome, o subtítulo explica, o molde (antes × agora) não se repetia havia
dez peças e a prova da capa era a melhor da peça. O retorno foi seco: *"a hero
do slide 1 ainda não estamos conseguindo vender de forma correta"*. São dois
defeitos, e nenhuma das três perguntas alcança nenhum dos dois.

**Quarta pergunta: qual é o sujeito do título?** Ali é *a mensagem* — o
WhatsApp. E o WhatsApp é **por onde o recurso chega**, não o recurso. A
diferença parece fina no papel e é enorme no feed, porque título se lê da
esquerda para a direita e a leitura do feed muitas vezes para no meio: quem lê
"A mesma mensagem" foi informado de que **nada mudou**, e a novidade estava
depois da vírgula. O molde antes × agora tem essa armadilha embutida, porque o
"antes" ocupa a primeira metade da linha e o "antes" é sempre a coisa velha.

Não confunda com a regra do canal. O canal **faz parte do nome** e não sai por
concisão — "Campanhas Inteligentes no WhatsApp" está certo. O que ele não pode
ser é o sujeito: ali o canal é adjunto de um nome, aqui ele era o herói da
frase. Em posição de adjunto ("pelo WhatsApp", no subtítulo) ele cumpre a
terceira obrigação sem roubar a primeira.

**Quinta pergunta: de onde veio o nome?** "Rastreio da entrega pelo cliente" é
o título do release, e título de release é escrito do lado de quem construiu,
para descrever **o que foi construído**. O nome pelo qual o recurso se vende é
outro: *acompanhamento em tempo real*. Os dois são verdade, e é exatamente por
isso que a troca é invisível — ela não é erro de fato, então não cai no
`conferir-texto.py`, não cai na checagem "isto está no manual?" e não cai na
leitura em voz alta. O release é a fonte do que é **verdade**; não é a fonte do
que é **nome**.

Quando os dois divergem, a capa fica com o nome de venda e o
`copy-instagram.txt` registra o outro, em nota de produção, para quem for
responder comentário — porque o cliente que leu o release vai procurar pelo
nome dele.

A segunda versão ficou assim, e o destaque mudou de lugar junto:

> Acompanhamento **em tempo real**, pelo seu cliente
> O mapa da entrega chega pelo WhatsApp.

O vermelho caiu em "em tempo real" e não no nome inteiro. Nas peças anteriores
a palavra destacada era a que o leitor ia **procurar no menu** depois; aqui não
há menu para procurar, porque o recurso é automático e não tem tela de
configuração. Sem essa função, o destaque volta a fazer o que faz num cartaz:
marca o que é notícia.

### E a capa leva uma imagem, dentro de um aparelho

Capa só de texto perde para capa com imagem, e a imagem certa é o resultado da
novidade (o papel impresso, a tela nova), não um ícone decorativo.

**E ela entra num mockup, não solta.** Print com borda arredondada é um arquivo
colado no slide; o aparelho desenhado em volta diz **onde aquilo vive** — no
celular do cliente, no tablet da mesa, na TV da retirada. Numa capa isso vale
mais que legibilidade: o leitor não vai ler os cartões, vai reconhecer a cena.
Os aparelhos e as regras de cada um estão em [`mockups.md`](mockups.md); se o
que a novidade pede não existe lá, desenhe e **suba para a skill**.

O resto do carrossel é o contrário: o slide que precisa ser lido usa `.recorte`,
sem aparelho — ver *aparelho ou recorte: quem decide é o que precisa ser lido*.

**E a capa entra nessa conta quando a imagem dela é prova de leitura.** O
aparelho ganha da legibilidade porque, em geral, a capa quer reconhecimento: a
tela dentro do notebook diz "isso é no computador" e ninguém precisa ler os
cartões. Quando a prova promovida para a capa é o texto que está nela — o nome
de cada campanha, o rótulo de cada gatilho —, a premissa se inverte, e o
aparelho passa a ser exatamente o que come a largura de que esses nomes
precisam. Aí a capa fica com o recorte, como o slide interno.

**É a frase mais curta do carrossel.** "Cansou de bebida esquecida na sacola?"
tem seis palavras e está correta; "Cansou de esquecer a bebida?" tem cinco, diz o
mesmo e sobra slide para a imagem. A capa é a única frase que todo mundo lê —
cada palavra que sai dela é ganho, e é o único lugar onde cortar até o osso
melhora o texto.

**Uma palavra em vermelho, e só uma.** O `.destaque` na palavra que carrega o
assunto ("a **bebida**") dá o ponto de entrada do olho. Duas palavras vermelhas
na mesma frase não destacam nada, e emoji junto do vermelho é grifo em cima de
grifo — escolha um.

A exceção é o **nome do recurso**, que vai inteiro mesmo tendo três palavras:
"Chegou o **Painel para Entregadores**". Grifar meio nome é pior que grifar
três palavras, e num anúncio o ponto de entrada do olho **é** o nome.

**O subtítulo explica, e é explicando que a frase respira.** O título corta até
o osso; o subtítulo diz o que o recurso faz, e nisso recupera o tom. Pode
ocupar duas linhas: "Sem canetinha na lata, sem grito na cozinha. O cupom marca
sozinho." A versão de uma linha só ("Agora o cupom já sai com ela marcada")
tinha sido encurtada para abrir espaço para a imagem — e a imagem,
centralizada, coube junto com as duas linhas. Aperte a imagem antes de apertar
o subtítulo. O que ele não pode é virar só tom: subtítulo que não explica deixa
a capa com metade do anúncio.

**A imagem da capa mostra UM destaque.** A primeira versão desta capa usava o
cupom inteiro, com duas linhas em fundo preto — e aí a imagem dizia o contrário
do slide do limite ("não saia marcando tudo"). Quando a captura que existe não dá
para recortar até sobrar um destaque só, gere uma captura nova em que só ele
aparece; desenhar o cupom é o último recurso.

**E ela fica centralizada e grande.** Imagem sozinha na faixa, encostada numa
borda, deixa metade do slide vazia e sai menor do que podia. Inclinar em 3D só se
paga quando tem conteúdo do outro lado.

## Estrutura que funciona (6 a 8 slides)

1. **Capa** — o anúncio: o nome do recurso no título (ou no chapéu, se o molde
   escolhido não o comportar), o subtítulo dizendo o que ele faz, e a imagem
   dentro de um aparelho — ou no recorte, quando a prova da capa é para ser
   lida. Ela leva a prova mais forte da peça, o que às vezes só se descobre na
   folha de contato.
2. **A introdução** — explique o recurso que a capa nomeou: o que se marca,
   sobre o que a conta incide, onde o cliente vê. Duas ou três frases, e acabou.
   Aqui, sim, cabe a cena do release que a capa não podia carregar. Não é o
   slide da história ("você já faz isso no balcão"), e explicar **não é ensinar
   a mexer**: nome de campo, ordem de tela e passo a passo continuam no
   manual — ver *explicar o recurso não é ensinar a mexer*.
3. **A virada** — o que muda, mostrado. Antes × depois é o slide mais
   compartilhado do carrossel.
4. **Onde ligar** — mockup de computador com o caminho de menu e o realce no
   campo.
5. **O atalho** — como fazer em vários itens de uma vez, quando existir.
6. **Até onde vai** — o efeito nas outras pontas (cozinha, entregador, cliente).
7. **O limite de uso** — o erro comum de quem usa ("não saia marcando tudo").
   Gera confiança porque não vende. Não é a mesma coisa que avisar o que o
   sistema não faz: isso derruba a peça — ver *nunca avise o limite do recurso*.
8. **CTA** — um pedido só.

Não é camisa de força. Melhoria pequena cabe em quatro slides, e forçar oito
produz slide vazio — que é pior do que carrossel curto.

### O CTA promete o que ainda não foi mostrado, com a frase mais comum possível

O último slide falha de um jeito específico e fácil de não ver: ele convida
para o que o carrossel **acabou de mostrar**. *"Conheça o totem por dentro"*,
depois de oito slides de telas do totem, é a mesma coisa de novo — agora sem
imagem.

O conserto é achar o que há de **a mais** no destino, e prometer isso. A página
do totem tem a plataforma inteira ao lado — PDV, KDS, fiscal, estoque,
fidelidade — e o CTA virou *"Conheça todas as funcionalidades"*. O plural é o
que faz o trabalho: é mais do que o carrossel entregou.

**Mas não descreva o mecanismo do destino.** Essa é a armadilha da rodada
seguinte, e ela é convincente: a mesma página roda uma demonstração do pedido,
com pausa e setas, então *"passe pelo pedido inteiro, tela por tela"* parecia
ótimo — fato verificado, verbo preciso. Ficou pior. **Do feed, ninguém sabe que
existe uma demonstração do outro lado**, e a frase virou instrução para uma
coisa que o leitor não viu.

| o que existe só lá | serve para |
|---|---|
| a demonstração, a calculadora, o comparador | **escolher o destino** e conferir que vale a viagem |
| descrever isso no texto do CTA | nada: o leitor não tem contexto |

> O CTA é o único slide em que **ser convencional é vantagem**. O leitor
> precisa saber o que fazer com a frase sem explicação, e frase convencional é
> justamente a que ele já sabe ler. Gaste a criatividade na capa.

### E o CTA de novidade não ensina a ligar o recurso

O CTA da décima peça saiu **"O entregador entra no mapa com dois cadastros que
você já tem"**, com o caminho apontando para o cadastro do aplicativo. Voltou em
uma linha: *"refaça a copy inteira do último slide, não é sobre isso, venda a
novidade"*.

O defeito não é de frase, é de **assunto**: o slide era sobre trabalho. Criar o
funcionário, criar o usuário, instalar o aplicativo — tudo verdade, tudo o que o
leitor vai ter de fazer, e nada disso é motivo para ele querer fazer. Depois de
oito slides de argumento, fechar com a burocracia de ligar o módulo é entregar a
fatura antes da venda. É primo do *slide do problema que cobra* e do *alívio
antes do CTA*: os três põem o custo na frente do ganho, no pior lugar possível.

A saída não precisou ser inventada, porque a série já tinha molde, e ele se lê
de fora, na fila das peças:

| Peça | Chapéu | Título |
|---|---|---|
| #3 | Já está no ar | Suba o seu primeiro vídeo **hoje** |
| #4 | Já está no ar | Ligue o primeiro **ajuste** hoje |
| #8 | Já está no ar | Abra o painel e **deixe ligado** hoje |
| #9 | Já está no ar | Abra hoje e leia o que elas já **estão dizendo** |
| #10 (era) | Como começar | O entregador entra no mapa com dois cadastros |

**Chapéu "Já está no ar", título no imperativo com "hoje", subtítulo com o
primeiro passo mais a linha de fechamento da série, pílula de caminho.** Quatro
peças seguidas, e a quinta abandonou os quatro de uma vez — sinal de que o molde
estava no acervo e não no documento. Agora está nos dois. O CTA é o slide em que
*ser convencional é vantagem*, e convenção só funciona se alguém a escrever.

Duas regras finas que a mesma rodada fixou:

- **o caminho aponta para o módulo que a peça vendeu**, não para um acessório.
  Estava em `Aplicativos → Entrega → BeeFood Entregador`, que é assunto de um
  slide do meio; virou `Delivery → Entregas`;
- **a linha de disponibilidade é fato publicado, e é condicional.** "Quem tem o
  módulo Entrega já tem a Gestão de Entregas" sai da novidade da peça irmã, que
  diz o mesmo com as palavras do produto. "Todo mundo já tem" seria promessa
  nossa, e módulo em liberação não a sustenta.

E a imagem cai junto com a copy, sempre: a do CTA velho era o aplicativo
**vazio**, com "Nenhuma entrega agora", porque a frase precisava dela ("lista
vazia é sinal de que deu certo"). Tela em que não acontece nada é a pior arte
possível para fechar uma venda — e ela só passou na revisão de imagem porque o
texto a justificava. Trocado o texto, a imagem vira órfã na hora.

#### E a arte do CTA pode ser a da capa, de propósito

A substituta que eu tinha escolhido era um recorte da lista de rotas: prova o
título, mostra a rota pronta para sair. O dono resolveu por outro caminho —
*"coloque a foto do mapa e o pc na última com essa frase"* —, e a peça ficou
com **a mesma arte da capa, no mesmo lugar e no mesmo tamanho**.

É melhor, e o motivo é de forma: a peça **abre e fecha na mesma cena**. A capa
apresenta a tela e faz o leitor parar de rolar; o último slide devolve a mesma
imagem inteira, com um imperativo em cima, para alguém que agora sabe ler cada
coisa dali. Fechar num recorte é terminar olhando para um detalhe, logo depois
de oito slides de detalhe.

A regra geral desta skill continua sendo **não repetir prova dentro da mesma
peça** — repetição ali quase sempre é falta de arte. A exceção é uma, e é
estreita:

| Vale | Não vale |
|---|---|
| a arte da **capa**, repetida no **CTA** | a prova de um slide do meio, repetida em qualquer lugar |
| porque o assunto do CTA é literalmente *abra isto*, e o que ele manda abrir é o que a capa mostrou | porque aí é só falta de imagem nova |

### Frase de venda se procura no site antes de inventar

A página de vendas já foi escrita para vender aquilo, por quem decide como a
empresa fala. Antes de inventar manchete, subtítulo ou fecho, **leia a
página** e veja se ela já tem a frase.

O subtítulo da capa do totem precisava dizer por que cupom e cashback estão ali.
Saíram duas invenções — *"E o programa de fidelidade entra no pedido"*
(descreve onde o recurso mora) e *"E cada venda já sai puxando a próxima"*
(metáfora forçada) — antes de alguém abrir a página e achar, no cartão de
fidelidade: *"Aumente a recorrência com cashback e cupons."* Virou **"Mais
recorrência, com cashback e cupom."**

A régua de cópia não muda: a linha do site é **ponto de partida**, não texto
pronto. Reescreva com as nossas palavras e passe o `conferir-texto.py`.

## Ritmo de imagem

Pelo menos metade dos slides tem imagem, e a capa nunca fica de fora. Três
slides de texto seguidos é sinal de que dois deveriam virar um.

## Fale como gente fala

O vício que aparece sozinho na segunda rodada de escrita é o **aforismo**: título
curto, impessoal, em terceira pessoa, fechado em si mesmo. Cada frase fica
correta, elegante — e nenhuma é como alguém fala. O carrossel passa a soar como
placa de museu.

| Travado | Como alguém falaria |
|---------|---------------------|
| "Toda loja tem uma gambiarra para não esquecer a bebida" | "Cansou de esquecer a bebida?" |
| "Um esquecido custa duas viagens" | "Você sabe como essa história termina" |
| "A linha que importa para de se esconder" | "Olha o que muda no cupom" |
| "É um interruptor no cadastro do item" | "É só um interruptor" |
| "Marque a geladeira inteira de uma vez" | "Tem muita bebida? Marque tudo de uma vez" |
| "O entregador confirma antes de ir embora" | "Seu entregador também vê" |
| "Se tudo é destaque, nada é" | "Não saia marcando tudo" |
| "Todo recurso novo vira manual no mesmo dia" | "Acompanhe tudo que entra no sistema" |

O que tira do aforismo:

- **Dirija a frase a ele.** "Seu entregador também vê" tem dono; "o entregador
  confirma" é relatório. Mas dirigir não é abrir com "você pode" — ver *entregue
  a ideia, não a permissão*.
- **Não narre um "ele".** É o vício irmão, e é o que mais faz o texto parecer
  saído de máquina: "Ele queria pedir. Só não sabia o quê." descreve um
  personagem que não é quem lê. Corrigir isso narrando o cliente em close é cair
  na vala do cinema — ver *as duas valas*.
- **Pergunte.** Pergunta abre conversa e a pessoa responde de cabeça; declaração
  fecha o assunto antes de começar.
- **Mas não pergunte na capa de todo carrossel.** "Cansou de esquecer a
  bebida?", "Seu cardápio já fala inglês?", "Seu cardápio digital já tem
  vídeo?": três capas seguidas na mesma fórmula, e quem segue o perfil vê
  fórmula, não gancho. Antes de fechar a capa, leia as capas anteriores em
  sequência. Se a forma repetir, troque: afirmação do fato novo ("Sua capa
  agora é um **carrossel**") entrega a notícia na primeira linha, que é o que a
  pergunta só insinua.
- **Convide com o verbo.** "Olha o que muda", "Acompanhe", "Marque" — não
  "veja-se o que muda".
- **Não corte até virar telegrama.** "Um esquecido custa duas viagens" economiza
  três palavras e gasta toda a naturalidade. Palavra de ligação ("e", "então",
  "aí", "só") é o que faz a frase soar falada.
- **Leia em voz alta.** Se você não diria aquilo para um cliente no balcão,
  reescreva. É o teste que pega tudo o que está acima.

Aforismo tem lugar, mas **um por carrossel, no máximo** — e o carrossel funciona
bem sem nenhum.

## O carrossel vende. A voz é a de beefood.com.br

É post de uma empresa que vende sistema para restaurante, e quem lê está
decidindo se aquilo resolve algo na loja dele. Texto correto e morno não faz
esse trabalho. O site da marca é a régua, e cabe em quatro linhas:

| O site faz assim | Exemplo de lá |
|---|---|
| manchete é **ganho**, não recurso | "Aumente suas vendas com Cardápio Digital no Tablet" |
| fala com o dono | "Seu cliente pede direto pelo celular", "Dê mais autonomia ao seu cliente" |
| apoio curto e concreto embaixo | "Menos necessidade de garçons extras" |
| convida com verbo | "Comece", "Acompanhe", "Controle" |

No carrossel isso vira uma regra de fechamento: **cada slide termina no que muda
para o negócio** — fila que anda, mesa que fecha mais alta, equipe que atende
mais gente. Slide que só descreve funcionamento é documentação.

Duas cautelas:

- **não empreste número nem promessa do site.** "Até 40% de ticket médio" é de
  outro recurso, e a página do tablet fala em tradução "automática" — o recurso
  do carrossel depende de o dono escrever o texto. Promessa errada volta como
  comentário.
- **vender não é adjetivar.** "Revolucionário", "poderoso" e "incrível"
  continuam fora. O que vende é a cena concreta e a consequência.

### Explicar o recurso não é ensinar a mexer

O slide 2 explica, e a vala do manual fica logo ao lado. A fronteira é o tipo de
frase:

| Explicação (slide 2) | Manual (não entra) |
|---|---|
| "Em cada forma de pagamento você marca desconto, acréscimo ou nenhum dos dois" | "Abra **Cadastros → Formas de Recebimento**, clique na forma e role até **Ajuste no pagamento**" |
| "A conta incide sobre o total em produtos" | "O campo **Valor (R$)** aceita até duas casas decimais" |
| "O cliente vê o valor ao escolher como paga" | "O selo aparece à direita do nome, em verde ou vermelho" |

A esquerda diz **o que o recurso faz**; a direita diz **onde clicar** e como a
tela se comporta. O caminho de menu existe uma vez no carrossel, no CTA, quando
o leitor já quer saber onde fica.

E explicação não é enredo. "Você já faz isso no balcão", "no caixa você propõe
na hora" é história, e história no slide 2 gasta o lugar de quem ainda não
entendeu o recurso que a capa acabou de anunciar.

### O corpo: o que a pessoa vê, e só então o que isso resolve

A tabela acima separa explicação de **instrução** — o que o recurso faz contra
onde clicar. Falta o vizinho dela, que passou por onze peças: a **descrição**.
Ela não ensina caminho nenhum, não tem nome de campo, não fala em clicar, e
mesmo assim é manual. O retorno que a nomeou: *"tem slide que estamos
explicando o funcionamento da tela; não é um manual de usuário, e sim falar da
novidade"*.

**E a primeira correção caiu na vala do outro lado**, o que rendeu um segundo
retorno na rodada seguinte: *"o texto dos slides está sem sentido nenhum,
simplesmente frases estranhas, tentando vender uma ideia que deveria ser
simples — explicar a novidade"*. Por isso esta seção tem três colunas e não
duas. Com duas, o conserto vira "apague a descrição", e o que sobra é retórica.

| Manual — sujeito é a interface | Retórica — não sobrou fato | Certo — gente + fato + consequência |
|---|---|---|
| "A tela escreve o primeiro nome do entregador e a distância até a porta, e se refaz sozinha a cada poucos segundos" | "A ligação mais cara da noite é a de 'quanto tempo falta'. Ela perde o motivo quando quem pediu vê o entregador andando" | "Quem pediu lê o primeiro nome do entregador e quantos metros faltam até a porta, em linha reta, e vê a moto se mexer sem tocar em nada. É mais do que qualquer um do seu balcão conseguiria responder no telefone" |
| "São quatro etapas, e a frase embaixo muda junto com elas" | "Quem espera acompanha o pedido andar da cozinha até a porta. E a demora ganha explicação antes de virar reclamação" | "Quem pediu vê as quatro etapas se completarem, de **enviado** até **saiu para entrega**. E quando há outra parada antes da dele, ele lê em que lugar da viagem está" |
| "No computador o mapa ocupa a tela e as informações passam para a coluna da esquerda" | "Uma página só: nada de segunda versão para manter" | "É o mesmo endereço no celular e no computador — não há versão à parte para você divulgar" |
| "O sistema anexa o endereço do acompanhamento ao aviso de saída" | "Não há campo novo para preencher, tela nova para aprender nem mensagem a mais na conta" | "Na mensagem que avisa a saída, o sistema acrescenta o bloco **Acompanhe a entrega** e um endereço que vale só para aquele pedido" |

#### A distinção que separa as duas valas

Como a tela **se comporta** — com que frequência atualiza, onde ficam as
colunas, que a frase muda junto com a barra, quantos componentes existem — é
manual, e sai.

**O que o cliente lê ali é a novidade.** O primeiro nome do entregador, os
metros em linha reta, as quatro etapas, a frase que diz em que lugar da fila
ele está: isso não é descrição de tela, é o produto. Tirar isso não conserta o
defeito, esvazia o slide.

A diferença é fácil de ver em pares do mesmo fato:

| Comportamento (sai) | Conteúdo (fica) |
|---|---|
| "a tela se refaz sozinha a cada poucos segundos" | "ele vê a moto se mexer sem tocar em nada" |
| "a frase embaixo da barra muda junto com a etapa" | "ele lê em que lugar da viagem está" |
| "no computador vira duas colunas com o mapa à direita" | "é o mesmo endereço no celular e no computador" |

#### Por que a retórica é a vala mais perigosa das duas

O manual escreve sempre **fato + e daí**: "Carlos está indo até você / A 640 m
de você, em linha reta" e, páginas antes, "o cliente que vê a moto se mexendo
não pergunta". Ao corrigir a descrição, a mão promove o "e daí" a primeira
frase e apaga o fato que ele complementava. A frase resultante é verdadeira,
está no manual e **soa melhor** que a original — e por isso passa.

Mas benefício sem o fato a que se prende não tem onde se apoiar. Três sintomas,
todos da peça #11:

- **cabe em qualquer slide.** "A demora ganha explicação antes de virar
  reclamação" serviria igualmente ao slide 3, ao 4 e ao 6. Fato é o que amarra
  o parágrafo àquele slide;
- **vira tese de colunista.** "Mapa de entrega é o que os aplicativos gigantes
  ensinaram o país a esperar" — o manual diz que é o que **ele**, o cliente
  daquela loja, já conhece. "O país" é inflação de quem está escrevendo para
  impressionar;
- **inventa um vilão.** "Não um horário chutado que volta como reclamação",
  "nada de segunda versão para manter": o produto nunca prometeu horário e
  ninguém cogitou manter duas páginas. No manual essas frases têm seção e
  contexto; soltas no slide, plantam a suspeita de um problema que o leitor não
  tinha.

#### Em peça de novidade, explicar bem É vender

A raiz do erro é de gênero. Quem lê uma novidade **já é cliente e já paga**:
ele não precisa ser convencido de que rastreio é bom, precisa saber o que
chegou e o que aparece na tela do cliente dele. O registro persuasivo pertence
à peça de **função**, cujo leitor ainda não comprou nada.

Regra prática: o esforço de venda é proporcional à distância do leitor. Em
novidade essa distância é zero, e o texto que argumenta demais está gastando
espaço que devia estar informando.

#### As duas obrigações, e como conferir

1. **Todo corpo carrega pelo menos um fato conferível no manual.** Tampe a
   imagem, leia só a copy da peça inteira e responda: *o que o cliente vê na
   tela?* Se a resposta não sai, a peça não explicou a novidade — e esse era
   exatamente o estado da #11 depois da primeira correção.
2. **A consequência vem depois do fato, na mesma frase ou na seguinte, nunca
   abrindo o parágrafo.** Ela é o fecho. "É mais do que qualquer um do seu
   balcão conseguiria responder no telefone" vale como última linha e não vale
   como primeira.

E uma restrição de forma que caiu junto: **no máximo uma construção negativa
por corpo, e nunca na abertura**. Corpo que começa em "Não há campo novo, tela
nova nem mensagem a mais" obriga o leitor a montar sozinho o fato positivo, e
ainda sugere que poderia haver trabalho.

### O slide do problema elogia antes de cobrar

Vale para a peça que **abre pelo incômodo** — e, quando a capa nomeia o recurso,
o slide 2 é a introdução, não o problema. O erro que esta seção evita continua
sendo o mesmo: transformar o slide 2 em fatura.

Duas versões do carrossel de
tradução falharam ali: a primeira narrava o turista em terceira pessoa, e a
segunda perguntou **"Quanto seu salão perde por não falar inglês?"**, com três
linhas do que dá errado no salão e o custo no pé. Sujeito certo, tom de venda —
e ainda assim devolvido, porque aquilo é leitura de fatura. Ninguém salva um post
para ler a própria conta.

O que funcionou é a mesma informação de trás para frente:

1. **elogie o que ele já tem, com verdade.** "Seu cardápio é o seu melhor
   **vendedor**" — e é: foto, descrição, combo e adicional na tela são trabalho
   de vendedor. **O elogio é a uma coisa do produto**, nunca a um hábito
   suposto: "você já faz isso no balcão" tem o mesmo tom e é invenção (ver *tudo
   o que o slide afirma é do produto*).
2. **traga o furo depois, junto com a solução.** "Ele só vende para quem lê
   português (…) em inglês e em espanhol, esse vendedor volta a trabalhar."
3. **o custo fica, em cena e sem porcentagem:** "o pedido sai o mais simples
   possível, sem combo e sem sobremesa".

### Nunca avise o limite do recurso

"Não precisa traduzir tudo hoje." "Aos poucos." "Com calma." Parece gentileza, e
é o oposto: **aliviar um trabalho é admitir que existe um trabalho.** Um slide
desses no penúltimo lugar do carrossel foi lido como "o sistema não traduz
sozinho e é inútil" — a objeção plantada justo antes do CTA.

Quem precisa do limite abre o manual. A honestidade no carrossel se faz
mostrando a tela certa (o cadastro onde o texto em inglês é escrito) e
registrando no `roteiro.md` o que é captura e o que é desenho, não com aviso na
arte.

**Não confunda com o slide do limite de uso** ("não saia marcando tudo: marcar
dez linhas é não marcar nenhuma"). Aquele ensina a usar melhor e gera confiança;
este avisa o que o produto não faz e tira a venda.

E quando um slide desses cai, o lugar dele não fica vazio: **procure o que a peça
prometeu e não mostrou.** A capa prometia "inglês e espanhol" e o espanhol não
aparecia em slide nenhum — o slide do alívio virou o slide do espanhol, com dois
recortes da mesma tela provando o que antes era frase.

## Escrita

- Frase curta. Ponto final em vez de vírgula.
- Verbo no imperativo na instrução: "filtre o setor", "grave com SALVAR E SAIR".
- Termo da tela em **negrito**, exatamente como aparece no sistema. Se o sistema
  escreve "Editar em Lote", não escreva "edição em lote".
- Caminho de menu na classe `.caminho`: `Cardápio → Produtos`. Um por slide; duas
  pílulas de caminho na mesma frase viram um bloco colorido difícil de ler.
- Número sempre `1.`, `2.`, `3.`.
- Nada de "revolucionário", "incrível", "poderoso". O ganho concreto convence
  mais: "a equipe vê de longe o que conferir".
- **Número só se ele existir.** "Reduz 30% dos erros" não está na novidade nem no
  manual: é invenção, e invenção em post de produto volta como reclamação.
- **Sem diminutivo.** "Bandeirinha", "bolinha", "telinha" — soa infantil e faz o
  recurso parecer pequeno. Exceção só para nome próprio de produto.

## Microdetalhe de interface não entra

O carrossel da tradução gastou dois slides explicando um enfeite de tela: que a
bandeira ganha um sinal verde quando o idioma já tem texto, e que um grupo de
opções traduzido vale em todos os produtos que o usam. Correto, e inútil no
feed — é material de manual, e roubou o lugar do que o dono quer saber.

O teste é uma pergunta: **o que muda para ele se eu tirar essa frase?** Se a
resposta é "nada, ele só sabe menos um detalhe da tela", corte e ponha a
consequência no lugar.

| Microdetalhe | O que entrou no lugar |
|---|---|
| "A bolinha verde marca a bandeira que já recebeu tradução" | "Mudou o preço, acabou o estoque? Você mexe num lugar só, e os três idiomas acompanham" |
| "Traduza um grupo de opções e ele vale em todo produto que usa aquele grupo" | (cortado — e o slide inteiro caiu depois, por ser sobre o trabalho do lojista) |

Enfeite de tela, nome de campo e regra fina de comportamento entram quando
**são** o assunto do slide, nunca como explicação de brinde.

## Se a tela prova, o slide é a tela

O slide que substituiu o do alívio tem uma linha de texto e duas imagens: o mesmo
item do cardápio, recortado do mesmo ponto da tela, um em inglês e um em
espanhol. Mesma foto, mesmo preço, e o nome saindo de `FRENCH FRIES` para
`PAPAS FRITAS`. Nenhum parágrafo sobre "três idiomas" convence como esse par.

Pergunta de roteiro: **esse slide explica algo que a tela já mostra?** Se sim,
ele é um recorte com rótulo — e o texto vira uma linha. Para o recorte sair
comparável, a caixa é medida no DOM e usada igual nos dois idiomas
(`screenshot(clip=…)`), e a captura é em escala 2, porque na arte ela aparece
ampliada.

## Emoji

Pouco e onde couber — é o que dá cara de conversa sem virar post de promoção.

- **Até um por slide, e não em todos os slides.** Metade dos slides sem nenhum é
  o que faz os outros funcionarem.
- **Prefira os que a própria novidade usa** (🖨️ 🛵) e, depois, os do assunto
  (🥤 para bebida, 💰 para dinheiro).
- **Emoji que aponta tem função.** O 👇 no fim do título, encostado com `&nbsp;`,
  manda o olho para o mockup logo abaixo. Sem o `&nbsp;` ele cai sozinho na
  linha seguinte e parece acidente.
- **Nada de emoji em slide de limite, erro ou cuidado.** Ali ele sai
  sarcástico — o slide que avisa "não saia marcando tudo" fica sério.
- **Nada de emoji na frase que já tem palavra em vermelho.** Grifo em cima de
  grifo; na capa, o vermelho ganha.
- O ambiente tem a Noto Color Emoji instalada, então o emoji sai colorido no PNG
  sem configuração nenhuma.

## Legenda de publicação

Vai no fim do `roteiro.md`, pronta para copiar:

- Primeira linha repetindo o gancho — é o que aparece cortado no feed.
- Dois ou três parágrafos curtos: o que é, onde liga, qual o limite.
- Fechamento apontando o manual dentro do sistema, quando existir.
- Cinco a seis hashtags, sem empilhar trinta.

## Checagem antes de renderizar

- [ ] **A capa diz o nome do recurso?** Quem lê só ela sabe o que entrou no
      sistema — e o nome é o que o recurso faz, não o nome do campo.
- [ ] **Cada slide de dentro diz o nome do recurso que ele mostra?** Leia só os
      títulos, em fila: dá para montar a lista do que o módulo passou a fazer?
      Se um título só tem o ângulo ("a rota já chega montada"), falta o nome —
      ele entra antes dos dois-pontos, e o ângulo fica depois. Nome no chapéu
      não conta: chapéu se lê depois do título, quando é lido.
- [ ] **Nenhum título tem pronome.** Procure `ele`, `dele`, `dela`, `isso`,
      `aquilo` nos títulos: o título é a única parte da peça que se lê fora de
      ordem, então antecedente no chapéu, na legenda ou no slide anterior não
      resolve. No corpo, o substantivo vem antes do pronome, no mesmo slide.
- [ ] **O CTA de novidade segue o molde da série?** Chapéu "Já está no ar",
      título no imperativo com "hoje", subtítulo com o primeiro passo mais a
      linha de fechamento, pílula apontando para o **módulo que a peça vendeu**.
      E ele vende, em vez de ensinar a ligar o recurso: cadastro, instalação e
      permissão são trabalho, e trabalho no último slide é a fatura antes da
      venda.
- [ ] **Leia cada slide em voz alta.** Onde a respiração tropeça falta palavra:
      artigo cortado ("lista vazia" por "a lista vazia"), `de que` comido ("é
      sinal que deu certo") e corpo sem verbo principal ("Na ordem que a loja
      definiu, com o número do pedido"). Estilo telegráfico é de manchete de
      jornal, que paga por centímetro; aqui ele lê como texto mal escrito.
- [ ] **O gênero está certo do começo ao fim?** Em peça de função: nenhuma
      pílula `Novidade`, nenhum "agora", CTA que serve para quem ainda não tem
      painel, e nenhum número institucional na arte.
- [ ] **O acervo foi lido antes de a peça ser escrita?** Em peça de `função`:
      que prova de módulo compartilhado já existe capturada, e que gancho a peça
      vizinha já usou. Reuso é do **módulo**, nunca do canal.
- [ ] **Slide reaproveitado foi adaptado, e não copiado?** A prova é a de lá; a
      **ideia** é desta peça. Escreva a pergunta que este ponto do arco deixou
      aberta: se ela for a mesma que a peça de origem respondia, o ângulo veio
      junto por engano — trocar as palavras não conserta isso.
- [ ] **A arte prova a manchete inteira?** Se o título diz duas coisas (dois
      idiomas, dois canais, antes e depois) e a imagem mostra uma, ou a imagem
      está errada ou o título está grande demais. Havendo mais de uma prova no
      acervo, a escolhida é a que fecha o título — e, se ela for do canal
      errado, redesenhe em vez de trocar de prova.
- [ ] **A manchete vende o uso principal, e não o recurso mais vistoso?** Se o
      restaurante comprar por causa desta capa, é isso que ele vai usar todo
      dia? E, quando o produto tem irmãos na linha (totem, tablet, QR Code,
      app do garçom), a capa diz o que ele faz **de diferente** — não repete o
      gancho da peça vizinha num ponto em que este canal é mais fraco.
- [ ] **O slide 2 explica o recurso?** Não conta história, não cobra, e não
      ensina onde clicar.
- [ ] **Qual é o sujeito do título da capa?** Se for o canal, o aparelho ou a
      mensagem, a capa está anunciando o **meio** e não o recurso. O canal faz
      parte do nome, mas entra como adjunto ("pelo WhatsApp") — nunca como
      herói da frase. Cuidado redobrado no molde antes × agora, em que a
      primeira metade da linha é ocupada pela coisa velha.
- [ ] **O nome da capa é o nome que vende, ou o título do release?** Release é
      escrito do lado de quem construiu. Os dois nomes são verdade, então
      nenhuma conferência de fato pega a troca: "rastreio da entrega pelo
      cliente" virou "acompanhamento em tempo real". O do release fica anotado
      no `copy-instagram.txt`, para responder comentário.
- [ ] **Qual é o sujeito de cada oração do corpo?** Interface ("a tela
      escreve", "são quatro etapas", "o mapa ocupa a tela", "o sistema anexa")
      é manual de usuário. Tem de ser gente ("quem pediu", "quem espera"), com
      o fato como objeto dela.
- [ ] **Tampando a imagem, a copy diz o que o cliente vê na tela?** Se não diz,
      o slide virou tese: "a ligação mais cara da noite", "a demora ganha
      explicação", "nada de segunda versão para manter". Todo corpo carrega ao
      menos um fato conferível no manual, e a consequência vem **depois** dele,
      como fecho — nunca abrindo o parágrafo.
- [ ] **O corpo caberia em outro slide da mesma peça?** Se caberia, está sem
      fato dentro. É o teste mais rápido dos três.
- [ ] **Alguma frase inventa um defeito para dizer que ele não acontece?**
      "Horário chutado", "segunda versão para manter": no manual isso tem seção
      e contexto; no slide, planta a suspeita de um problema que não existe.
- [ ] **Algum corpo abre por negação?** Uma construção negativa por corpo, no
      máximo, e nunca na primeira frase. O fato positivo vem antes.
- [ ] **Alguma frase trocou a palavra concreta por metáfora?** "Preço" no lugar
      de desconto e acréscimo, "o que mais entra" no lugar da forma de
      pagamento. A palavra do recurso ganha da imagem poética.
- [ ] Existe a tabela **fato → ângulo → slide** no `roteiro.md`.
- [ ] Existe, no `roteiro.md`, a **ideia de uso** de cada slide — e cada slide
      entrega a dele.
- [ ] **Quem poderia desmentir cada frase?** Nenhuma afirma o que o leitor faz,
      tem ou sente — só o que o produto faz.
- [ ] A capa diz o fato **inteiro**: nenhum eixo da novidade (o "ou", o "e" do
      título) ficou fora, e nenhum **exemplo** do release virou manchete.
- [ ] A imagem da capa mostra os eixos, e não um lado só.
- [ ] **Um exemplo numérico, o mesmo em todos os slides.** Dois jogos de número
      para o mesmo recurso lêem como duas versões do produto.
- [ ] Nenhuma frase do carrossel aparece igual no texto da novidade.
- [ ] Nenhum slide entrega **permissão** ("você pode") em vez de ideia.
- [ ] Nenhum slide narra a cena do cliente em **close** (dedo, boca, chapa).
- [ ] Nenhum chapéu é nome de **campo, aba ou menu**.
- [ ] Três leituras de fora, em sequência: só os títulos, só as primeiras
      palavras de cada parágrafo, só os textos das artes. Se alguma das três soa
      como a mesma frase repetida, a peça volta.
- [ ] No máximo um emoji por slide, e não em todos.
- [ ] Nenhuma palavra no diminutivo, e nenhuma frase explicando enfeite de tela.
- [ ] Nenhum slide narra um "ele" que não é o leitor nem o cliente dele.
- [ ] Nenhum slide alivia um trabalho ("não precisa fazer tudo hoje", "aos
      poucos") nem avisa o que o sistema não faz.
- [ ] O slide do problema elogia o leitor antes de mostrar o furo.
- [ ] Nenhum slide explica com cinco linhas o que dois recortes da tela provam.
- [ ] Cada slide fecha no que muda para o negócio, não na descrição do recurso.
- [ ] A capa tem **uma** palavra em vermelho, e nenhum emoji junto dela.
- [ ] Nenhum título com palavra em vermelho leva emoji — em slide nenhum.
- [ ] A capa não repete a forma da capa do carrossel anterior (duas perguntas
      seguidas já é fórmula).
- [ ] O slide 1 tem imagem, e a imagem mostra **um** destaque só.
- [ ] Cada slide tem **uma** ideia; o título do slide diz qual.
- [ ] Toda afirmação está no texto da novidade ou no manual — ou foi conferida
      na tela.
- [ ] Nenhum número aparece sem fonte.
- [ ] O `roteiro.md` diz quais telas são captura e quais são desenho (na arte
      não vai carimbo de ilustração).
- [ ] O CTA pede uma coisa só, promete o que o carrossel **ainda não mostrou**
      e faz isso com a frase mais comum possível — sem descrever o mecanismo da
      página de destino.
- [ ] Toda frase de venda foi procurada **na página** antes de ser inventada, e
      reescrita com as nossas palavras depois de achada.
- [ ] Os pontos do rodapé marcam a posição certa do slide.
- [ ] Nenhum nome, telefone ou e-mail de cliente aparece em nenhum print.
- [ ] Nenhum print mostra data de publicação — nem o print de página nossa, que
      traz a data da novidade no alto do cartão.
