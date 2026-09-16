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
2. **O custo** — o que acontece quando o problema acontece. É aqui que o leitor
   se reconhece. Custo em cena concreta ("alguém sai de novo no meio do pico"),
   não em número inventado.
3. **A virada** — o que muda, mostrado. Antes × depois é o slide mais
   compartilhado do carrossel.
4. **Onde ligar** — mockup de computador com o caminho de menu e o realce no
   campo.
5. **O atalho** — como fazer em vários itens de uma vez, quando existir.
6. **Até onde vai** — o efeito nas outras pontas (cozinha, entregador, cliente).
7. **O limite** — o erro comum. Slide que gera confiança porque não vende.
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
- [ ] A capa tem **uma** palavra em vermelho, e nenhum emoji junto dela.
- [ ] O slide 1 tem imagem, e a imagem mostra **um** destaque só.
- [ ] Cada slide tem **uma** ideia; o título do slide diz qual.
- [ ] Toda afirmação está no texto da novidade ou no manual — ou foi conferida
      na tela.
- [ ] Nenhum número aparece sem fonte.
- [ ] Todo slide com tela desenhada leva `.selo-ilustracao`.
- [ ] O CTA pede uma coisa só.
- [ ] Os pontos do rodapé marcam a posição certa do slide.
- [ ] Nenhum nome, telefone ou e-mail de cliente aparece em nenhum print.
