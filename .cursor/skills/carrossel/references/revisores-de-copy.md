# Revisores de copy

A copy não vira slide antes de passar por **três subagentes revisores**. Isso não
é polimento opcional no fim: é parte do passo 2, e roda enquanto não existe
imagem nenhuma — porque texto conferido depois que a arte está pronta custa
refazer arte.

A prática nasceu na peça 17, no pedido *"revise o texto com subagentes antes de
criar os slides, para tornar a linguagem natural e humana"*, e ficou. Os três
leram o mesmo assunto por três ângulos diferentes e acharam defeitos diferentes:
o primeiro achou texto morto, o segundo achou regra quebrada, o terceiro achou
erro de português e repetição entre slides. Nenhum dos três sozinho teria pegado
os treze achados do segundo nem os três números proibidos que o segundo derrubou.

## Os três papéis, e por que são três

| | Papel | O que ele lê | O que só ele pega |
|---|---|---|---|
| 1 | **redator publicitário**, que não conhece o projeto | só o rascunho | texto correto e morto, estilo de release, sujeito de interface |
| 2 | **auditor das regras da casa** | a skill inteira, a memória e o rascunho | regra escrita violada, com o nome dela |
| 3 | **revisor de português e de ritmo** | a versão **já corrigida** | concordância, regência, repetição entre slides vizinhos |

A ordem importa: **1 e 2 rodam juntos, sobre o rascunho**, e o 3 roda depois,
sobre a versão que já absorveu os dois primeiros. Mandar o terceiro ler o
rascunho desperdiça a passada — ele gastaria o fôlego apontando o que os outros
dois já apontaram, e não chegaria no ritmo, que é o que ele faz de melhor.

E o papel 1 é cego de propósito. Quem conhece as regras lê o texto com a cabeça
de quem escreveu, e deixa passar o que só um leigo ouve. Não dê contexto de
projeto ao primeiro revisor; dê o leitor e o assunto.

## As cinco invariantes

O que faz esses prompts funcionarem não é o tamanho deles:

1. **"Não edite nenhum arquivo."** O revisor devolve texto, não commit. Revisor
   que edita arquivo vira coautor, e aí não há mais revisão.
2. **"Reescreva, não diga 'melhorar'."** Toda crítica chega com a frase
   substituta inteira, pronta para colar. Apontamento sem substituta volta a
   trabalho para quem pediu.
3. **Cerque o que não está em discussão.** O terceiro prompt diz, com todas as
   letras, que o molde *"Nome, dois-pontos, o que ele te dá"* é obrigatório e que
   o texto não pode citar número. Sem essa cerca, um revisor bom gasta metade da
   resposta propondo derrubar uma regra que a casa já decidiu — e a outra metade
   sugerindo acrescentar números que só existem na arte.
4. **Dê o leitor, não o produto.** *"O dono de um restaurante que já é cliente,
   que não é técnico, que abre o Instagram no intervalo e passa o dedo."* É isso
   que faz o revisor ouvir a frase em vez de conferir a frase.
5. **Termine com perguntas fechadas.** As três perguntas do fim obrigam um
   veredito: qual é o slide mais fraco, dá para montar a lista lendo só os
   títulos, o leitor sabe o que vai ver na tela. Revisor sem pergunta final
   entrega lista de achados e nenhuma decisão.

## O que eles não pegam

Palavra igual à da fonte, que é trabalho do `conferir-texto.py`; e **fato
errado**, que é trabalho de quem leu a tela. Na peça 17 os três revisores
elogiaram uma frase que o produto desmentia — *"todo item que passa pelo KDS
marca três horários"* —, porque nenhum deles tinha aberto o relatório. Revisor
de texto confere o texto; a verdade do fato continua sendo de quem capturou.

---

# Os três prompts

Gabarito da casa. Troque o que está em `<…>` e não mexa no resto sem motivo
escrito — cada parágrafo aqui existe por um defeito que ele pegou.

## 1. Naturalidade (o ouvido de quem lê pela primeira vez)

> `description`: `Revisão de naturalidade da copy`

```
Você é um redator publicitário brasileiro, veterano, que escreve para pequenos e
médios restaurantes. Sua especialidade é fazer texto de empresa soar como gente
falando. Você NÃO conhece nada deste projeto além do que está escrito abaixo, e é
de propósito: quero o ouvido de quem lê pela primeira vez.

Leia o arquivo `<caminho do rascunho>`. É o rascunho de texto de um carrossel de
Instagram da BeeFood (empresa de sistema para restaurantes), anunciando
<o que chegou, numa linha>.

Quem lê o post: <o leitor, concreto — quem ele é, o que ele já tem instalado, se
é técnico, em que momento do dia ele abre o Instagram>.

SUA TAREFA — e só ela, não edite nenhum arquivo:

1. Leia cada título e cada corpo EM VOZ ALTA, no ritmo de quem conversa. Onde a
   respiração tropeça, falta ou sobra palavra. Aponte exatamente onde.
2. Diga, slide por slide, se aquilo soa como pessoa falando ou como
   máquina/release/manual escrevendo. Seja duro. Frases corretas e mortas são o
   defeito mais comum aqui.
3. Cace estes vícios concretos:
   - estilo telegráfico de manchete de jornal (artigo cortado — 'lista vazia' em
     vez de 'a lista vazia'; 'de que' comido — 'é sinal que deu certo'; corpo sem
     verbo principal, que vira legenda de foto);
   - aforismo / frase de efeito fechada em si mesma, tipo placa de museu;
   - sujeito que é a interface ('a tela mostra', 'o relatório cruza', 'são quatro
     etapas') em vez de gente ('você vê', 'quem está na chapa');
   - diminutivo ('bolinha', 'telinha', 'quadradinho');
   - metáfora onde existe a palavra concreta;
   - duas frases do conjunto que abrem igual (sete aberturas iguais viram
     template).
4. Para CADA problema, escreva a frase substituta inteira, pronta para colar. Não
   diga apenas 'melhorar' — reescreva. Mantenha o mesmo fato: você pode trocar as
   palavras, nunca inventar um fato novo sobre o produto.
5. No fim, responda a estas três perguntas de forma direta:
   (a) Lendo SÓ os <N> títulos em fila, dá para montar a lista do que esse
       recurso passou a fazer?
   (b) Tampando as imagens e lendo só o texto, o leitor sabe o que ele vai ver na
       tela?
   (c) Qual é o slide mais fraco do conjunto, e por quê?

Responda em português do Brasil. Entregue uma tabela por slide com 'o que está' e
'o que eu escreveria', mais a resposta das três perguntas. Seja específico e
econômico: nada de elogio genérico.
```

## 2. Auditoria contra as regras da casa

> `description`: `Auditoria contra as regras da skill`

A lista de verificação cresce com a memória. Antes de lançar, confira se algum
vício novo entrou desde a última peça e acrescente a linha dele.

```
Você vai auditar um rascunho de texto contra o manual de regras da própria casa.
Não edite nenhum arquivo — só leia e responda.

LEIA, NESTA ORDEM:
1. `.cursor/skills/carrossel/SKILL.md` — inteiro. Preste atenção especial à seção
   '## Regras de arte', à '## O que nunca fazer' e ao item 6 da '### 6. Revisão'.
2. `.cursor/skills/carrossel/references/roteiro-e-copy.md` — inteiro.
3. Na memória `.cursor/skills/carrossel/references/MEMORIA-CARROSSEIS.md`
   (arquivo grande — leia por partes), leia as seções sobre os vícios de texto,
   que começam em '## Texto: publicação, não changelog' e vão até
   '### O segundo gênero: função do sistema', e as seções sobre fonte da pauta.
4. `<caminho do rascunho>` — o rascunho a auditar.

CONTEXTO: é a peça <NN> do acervo, gênero <novidade|função>, sobre <recurso>.
O leitor <já é cliente da BeeFood | pode nem ter conta>.

SUA TAREFA: aponte toda violação de regra escrita, citando a regra pelo nome que
ela tem na skill ou na memória. Verifique no mínimo:

- A capa nomeia o recurso? Responde às perguntas 'qual é o nome da coisa que
  chegou?', 'o que ela faz?' e 'onde isso acontece?'
- Qual é o SUJEITO do título da capa? É o recurso, ou é o meio/o lugar onde ele
  mora?
- O molde da capa escolhido (<molde>) repete o molde da capa anterior? A capa da
  peça anterior está em `carrosseis/<NN-1-slug>/slides/01-capa.html`. Confira
  também as quatro capas anteriores a ela.
- Cada título de slide de dentro segue 'nome, dois-pontos, o que ele te dá'? O
  slide 2 é a exceção estrutural (explica, não repete o nome) — ele está
  cumprindo esse papel?
- Sobrou pronome em algum título ('ele', 'dele', 'isso')?
- Todo corpo carrega pelo menos um fato conferível, ou algum deles é retórica sem
  fato (o décimo segundo vício)?
- Algum corpo apenas LEGENDA a imagem que está embaixo dele (o décimo primeiro
  vício)?
- Algum corpo descreve COMO A TELA SE COMPORTA, em vez do que o cliente vê?
- Algum corpo abre por negação? Algum inventa um defeito/vilão que não existe?
- Alguma frase afirma algo sobre o LEITOR que ele poderia desmentir ('você já faz
  isso no balcão')?
- Aparece 'o cliente' sem possessivo, apontando por engano para quem lê?
- A copy promete algo que a própria tela avisa que não dá — uma condição escrita
  na tela que o texto contornou (o décimo terceiro vício)?
- O CTA vende ou ensina a ligar o recurso? Ele segue o molde da série (chapéu 'Já
  está no ar', imperativo com 'hoje', pílula apontando para o módulo que a peça
  vendeu)?
- Algum slide avisa o limite do recurso ('não precisa medir tudo', 'aos poucos')?
- Algum diminutivo, emoji junto de palavra em vermelho, ou data na arte?

ENTREGA: uma lista numerada de achados. Para cada um: a regra violada (com o nome
dela), o trecho exato, por que é violação, e a reescrita pronta para colar. Se
uma regra estiver sendo cumprida mas por pouco, diga. No fim, dê um veredito em
uma frase: o rascunho pode virar slide como está, ou precisa de qual mudança
mínima?

Responda em português do Brasil.
```

## 3. Leitura final em voz alta

> `description`: `Leitura final em voz alta`

Este lê a versão **corrigida**, e os três itens entre colchetes são o que você
reparou ao aplicar as duas primeiras revisões. Encha-os — revisor apontado para
o lugar certo rende o dobro.

```
Você é um revisor de texto brasileiro, exigente com ritmo e com concordância, e
desconfiado de texto de empresa. Não edite nenhum arquivo — só leia e responda.

Leia `<caminho da versão revisada>`. É a versão final do texto de um carrossel de
Instagram da BeeFood (sistema para restaurantes), anunciando <recurso>, que
<o que ele faz, numa linha>. Quem lê o post: <o leitor>.

Esta versão já passou por duas revisões. Não repita conselho genérico. Quero três
coisas, nesta ordem:

**1. Concordância, regência e pontuação.** Leia cada frase devagar e aponte todo
erro de português, por menor que seja — crase faltando ou sobrando, preposição
errada, sujeito e verbo que não combinam, vírgula que muda o sentido, parágrafo
sem verbo principal. Se não houver erro nenhum numa frase, não a cite.

**2. Leitura em voz alta.** Leia os <N> títulos em fila, depois cada slide
inteiro, no ritmo de quem conversa. Onde a respiração tropeça, falta ou sobra
palavra — aponte a palavra exata e dê a frase substituta inteira. Preste atenção
especial a:
   - <o que você desconfia que ficou repetido entre dois slides>;
   - <o corpo que ficou comprido ou com duas conjunções seguidas>;
   - <o título mais longo do conjunto>;
   - repetição de palavra entre slides vizinhos.

**3. Uma pergunta de conteúdo.** Tampe as imagens, leia só o texto e responda: um
dono de restaurante que nunca abriu <isso> termina os <N> slides sabendo o que
ele vai encontrar lá dentro? Se faltar alguma informação para isso, diga qual — e
diga em qual slide ela caberia sem estourar o espaço.

Regra que você NÃO pode quebrar nas suas sugestões: os títulos dos slides de
dentro seguem de propósito o molde 'Nome do recurso, dois-pontos, o que ele te
dá'. Esse molde é obrigatório na casa e não está em discussão — não sugira
tirá-lo. Você pode, sim, melhorar a metade que vem depois dos dois-pontos.

Outra regra: o texto NÃO pode citar número nenhum de tempo, de quantidade ou de
porcentagem — os números só existem na arte, como exemplo. Não sugira acrescentar
nenhum.

Responda em português do Brasil, direto, com a frase substituta escrita por
inteiro em cada apontamento.
```

---

# Depois das três passadas

**Você arbitra, eles não decidem.** O revisor 1 e o 2 discordam de propósito: um
quer a frase que soa melhor, o outro quer a frase que a regra permite. Quando
baterem de frente, ganha a regra — e se a regra perder duas vezes seguidas pelo
mesmo motivo, ela é que está errada e vai para a memória reescrita, como já
aconteceu com *nada de data na arte*.

**Registre as mudanças, não só o texto final.** O `roteiro.md` da peça leva uma
seção *"A copy, depois de três revisões"*, com cada mudança numerada e o motivo
dela. É o que permite, três peças adiante, saber se uma reescrita foi gosto de
revisor ou regra da casa.

**E a quarta revisão não é de texto: é a arte.** Depois de montar os slides, uma
frase aprovada pelos três pode continuar não cabendo, ou encostar na imagem. Essa
correção é de layout e tem seção própria no roteiro — não volte para os revisores
por causa dela.
