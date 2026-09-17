# Roteiro e texto do carrossel

Quem lê é dono ou gerente de restaurante, no celular, entre dois pedidos. Ele não
procurou esse conteúdo: ele tropeçou nele. Isso define tudo abaixo.

## A novidade é matéria-prima, não roteiro

O texto publicado em `beefood.app/novidades` é registro de release: descreve o
**campo**, a **tela** e o **efeito**, na ordem em que o produto foi construído.
Carrossel não é isso. Recortar aquele parágrafo em oito pedaços e centralizar
cada pedaço num slide produz um changelog paginado, que ninguém arrasta.

O carrossel é uma **publicação nova, escrita a partir do fato**. Método:

1. **Extraia o fato.** Em três linhas, sem adjetivo: o que mudou, onde fica, o
   que passa a acontecer, e qual o limite. Isso vem da novidade e do manual.
2. **Ache o ângulo.** Qual cena reconhecível do restaurante esse fato toca? A
   bebida que fica na geladeira. A comanda que ninguém sabe se saiu. O custo que
   entra duas vezes no DRE. O ângulo é o que o leitor já viveu — não o recurso.
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

## A regra do primeiro segundo

O slide 1 não anuncia a funcionalidade — ele nomeia **um incômodo que a pessoa
já teve** — e leva **uma imagem**. Capa só de texto perde para capa com imagem, e
a imagem certa é o resultado da novidade (o papel impresso, a tela nova), não um
ícone decorativo.

| Em vez de | Escreva |
|-----------|---------|
| "Novo campo Destaque na impressão" | "Cansou de esquecer a bebida?" |
| "Nova etapa Pronto no Delivery" | "Quem está pronto já saiu, ou ainda não?" |
| "DRE: controle Considerar Custo Vendas" | "Seu custo pode estar entrando duas vezes no DRE" |

Teste rápido: leia só o slide 1 em voz alta. Se soa como changelog, reescreva.

**É a frase mais curta do carrossel.** "Cansou de bebida esquecida na sacola?"
tem seis palavras e está correta; "Cansou de esquecer a bebida?" tem cinco, diz o
mesmo e sobra slide para a imagem. A capa é a única frase que todo mundo lê —
cada palavra que sai dela é ganho, e é o único lugar onde cortar até o osso
melhora o texto.

**Uma palavra em vermelho, e só uma.** O `.destaque` na palavra que carrega o
assunto ("a **bebida**") dá o ponto de entrada do olho. Duas palavras vermelhas
na mesma frase não destacam nada, e emoji junto do vermelho é grifo em cima de
grifo — escolha um.

**O subtítulo é onde a frase respira.** O título corta até o osso; o subtítulo
recupera o tom, e pode ocupar duas linhas: "Sem canetinha na lata, sem grito na
cozinha. O cupom marca sozinho." A versão de uma linha só ("Agora o cupom já sai
com ela marcada") tinha sido encurtada para abrir espaço para a imagem — e a
imagem, centralizada, coube junto com as duas linhas. Aperte a imagem antes de
apertar o subtítulo.

**A imagem da capa mostra UM destaque.** A primeira versão desta capa usava o
cupom inteiro, com duas linhas em fundo preto — e aí a imagem dizia o contrário
do slide do limite ("não saia marcando tudo"). Quando a captura que existe não dá
para recortar até sobrar um destaque só, gere uma captura nova em que só ele
aparece; desenhar o cupom é o último recurso.

**E ela fica centralizada e grande.** Imagem sozinha na faixa, encostada numa
borda, deixa metade do slide vazia e sai menor do que podia. Inclinar em 3D só se
paga quando tem conteúdo do outro lado.

## Estrutura que funciona (6 a 8 slides)

1. **Capa** — o incômodo em no máximo oito palavras, com imagem.
2. **O reconhecimento** — é aqui que o leitor se vê. Elogie primeiro o que ele já
   tem funcionando e mostre o furo depois, na mesma frase que traz a solução; o
   custo aparece em cena concreta ("alguém sai de novo no meio do pico"), nunca
   em número inventado. Slide 2 que cobra afasta — ver *o slide do problema
   elogia antes de cobrar*.
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

- **Chame a pessoa de você.** "Seu entregador também vê" tem dono; "o entregador
  confirma" é relatório.
- **Não narre um "ele".** É o vício irmão, e é o que mais faz o texto parecer
  saído de máquina: "Ele queria pedir. Só não sabia o quê." descreve um
  personagem que não é quem lê. O sujeito é **você** (o dono) ou **seu
  cliente**. "Seu cliente toca na bandeira e pede sozinho" diz o mesmo e tem
  dono.
- **Pergunte.** Pergunta abre conversa e a pessoa responde de cabeça; declaração
  fecha o assunto antes de começar.
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

### O slide do problema elogia antes de cobrar

O slide 2 é onde o leitor decide se arrasta o carrossel. Duas versões do de
tradução falharam ali: a primeira narrava o turista em terceira pessoa, e a
segunda perguntou **"Quanto seu salão perde por não falar inglês?"**, com três
linhas do que dá errado no salão e o custo no pé. Sujeito certo, tom de venda —
e ainda assim devolvido, porque aquilo é leitura de fatura. Ninguém salva um post
para ler a própria conta.

O que funcionou é a mesma informação de trás para frente:

1. **elogie o que ele já tem, com verdade.** "Seu cardápio é o seu melhor
   **vendedor**" — e é: foto, descrição, combo e adicional na tela são trabalho
   de vendedor.
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

- [ ] Existe a tabela **fato → ângulo → slide** no `roteiro.md`.
- [ ] Nenhuma frase do carrossel aparece igual no texto da novidade.
- [ ] Você leu os oito títulos em voz alta seguidos. Soa conversa, ou desfile de
      aforismo?
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
- [ ] O slide 1 tem imagem, e a imagem mostra **um** destaque só.
- [ ] Cada slide tem **uma** ideia; o título do slide diz qual.
- [ ] Toda afirmação está no texto da novidade ou no manual — ou foi conferida
      na tela.
- [ ] Nenhum número aparece sem fonte.
- [ ] O `roteiro.md` diz quais telas são captura e quais são desenho (na arte
      não vai carimbo de ilustração).
- [ ] O CTA pede uma coisa só.
- [ ] Os pontos do rodapé marcam a posição certa do slide.
- [ ] Nenhum nome, telefone ou e-mail de cliente aparece em nenhum print.
- [ ] Nenhum print mostra data de publicação — nem o print de página nossa, que
      traz a data da novidade no alto do cartão.
