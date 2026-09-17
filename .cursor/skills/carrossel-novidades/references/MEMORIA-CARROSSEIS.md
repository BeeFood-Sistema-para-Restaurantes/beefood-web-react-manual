# Memória dos carrosséis

Memória própria desta skill. Aprendizado de **captura genérica** do BeeFood
continua na `MEMORIA-GERAL.md`, escrita por quem trabalha nos manuais — aqui só
entra o que é de carrossel.

Última atualização: 2026-09-17 (15ª rodada: capas e destaques em vídeo — dois
mockups de computador, um **estúdio de mídia** para a novidade em que o recurso
é o conteúdo que o lojista sobe, o primeiro **slide em vídeo** e a lição de que
a arte não pode desmentir a frase do slide).

14ª rodada: o que o carrossel da tradução produziu de geral **subiu para a
skill** — aparelhos fotografados num catálogo, fotos de produto numa biblioteca
e os dois scripts de captura do totem.

13ª rodada: dois slides refeitos por motivo de **argumento**, não de arte — peça
de venda não avisa o limite do recurso, e o slide do problema elogia o leitor
antes de mostrar o furo.

12ª rodada: o carimbo "ILUSTRAÇÃO" saiu da arte para sempre; a foto de fundo do
totem de exemplo passou a ser nossa; e a régua de texto virou **texto que vende,
na voz da marca e falando com você**.

## Índice

| Carrossel | Novidade | Pasta | Formato | Estado |
|-----------|----------|-------|---------|--------|
| Destaque na impressão | [15/09/2026](https://beefood.app/novidades/destaque-impressao) | `carrosseis/destaque-impressao/` | 4:5, 8 slides | ✅ entregue — `entrega/destaque-impressao.zip` (8 PNG + copy) |
| Cardápio presencial em inglês e espanhol | [16/09/2026](https://beefood.app/novidades/traducao-cardapio-presencial) | `carrosseis/traducao-cardapio-presencial/` | 4:5, 7 slides | ✅ entregue — `entrega/traducao-cardapio-presencial.zip` (7 PNG + copy) |
| Capas, destaques e avisos com imagem e vídeo | [13/08/2026](https://beefood.app/novidades/cardapio-digital-avisos-banners-capas-midia) | `carrosseis/cardapio-capas-destaques/` | 4:5, 7 slides | ✅ entregue — `entrega/cardapio-capas-destaques.zip` (7 PNG + capa em vídeo + copy) |

**Pasta com nome mais curto que o slug.** O slug desta novidade tem cinco
palavras e vira nome de pasta ruim. Nesse caso a pasta leva o nome curto e o
`conferir-texto.py` recebe `--novidade <slug-publicado>` para achar a fonte no
feed.

**Quantos slides:** os que a novidade tem de assunto, entre 6 e 8. O primeiro
carrossel saiu com 8 e o segundo com 7, e os dois fecham — o de tradução tem uma
ideia grande e três apoios, e o oitavo slide só existiria para chegar a oito.
Nada no `base.css`, no `renderizar.py` nem no `empacotar.py` depende do número;
o `.contador` diz "3 de 7" porque o slide escreve isso, não porque a skill conte.

## Texto: publicação, não changelog

O erro da 1ª versão do *Destaque na impressão* foi tratar o texto da novidade
como roteiro. Os slides diziam "A bebida não fica mais para trás", "Onde ligar",
"No papel" — exatamente os tópicos do release, na ordem do release. Sai um
changelog paginado: correto, e ninguém arrasta.

O que corrigiu foi separar as três etapas, e registrá-las no `roteiro.md` numa
tabela **fato → ângulo → o que o slide diz**:

- **fato** sai da novidade e do manual, em três linhas sem adjetivo;
- **ângulo** é a cena do restaurante que o fato toca (a gambiarra caseira para
  não esquecer a bebida);
- **texto** é escrito da cena para a tela, e nenhuma frase pode sobreviver igual
  à da novidade.

Método detalhado em [`roteiro-e-copy.md`](roteiro-e-copy.md).

### O segundo vício: aforismo

Reescrever a partir do fato resolveu o conteúdo e criou um problema de registro.
Os títulos da 2ª versão eram todos **máxima**: curtos, impessoais, em terceira
pessoa, fechados em si mesmos. "Um esquecido custa duas viagens." "A linha que
importa para de se esconder." "Todo recurso novo vira manual no mesmo dia."
Frase por frase, tudo correto; lidas em sequência, oito placas de museu.

Ninguém fala assim. O que tirou do aforismo foi chamar a pessoa de **você**,
**perguntar** em vez de declarar, e parar de cortar palavra até virar telegrama —
é a palavra de ligação ("e", "então", "aí", "só") que faz a frase soar falada.
O teste que pega tudo: ler os oito títulos em voz alta, seguidos. A tabela
travado × falado está em [`roteiro-e-copy.md`](roteiro-e-copy.md), com o
antes-e-depois dos oito slides deste carrossel.

Máxima tem lugar, mas **uma por carrossel** — e o carrossel vive bem sem nenhuma.

### O terceiro vício: narrar em terceira pessoa, com "cara de IA"

Tirar o aforismo deixou o texto falado, e mesmo assim o dono devolveu o carrossel
da tradução com o diagnóstico mais duro de todos: *"a linguagem está estranha
demais, robótica, com cara de IA"*, *"parece que estamos falando na terceira
pessoa"*, *"a copy não me agrada, precisamos vender"*. As duas frases que ele
citou:

- "Ele queria pedir. Só não sabia o quê."
- "Ele toca na bandeira e o cardápio inteiro muda."

Elas não têm erro de português e não são aforismo. O problema é **quem fala e
com quem**. As duas narram um terceiro — um turista que não é quem lê — como
legenda de fotografia. Quem está do outro lado é o dono do restaurante, e ele
não abre o Instagram para acompanhar a jornada de um personagem: ele quer saber
o que ganha. Texto que descreve cena em vez de falar com alguém é exatamente o
que sai de um modelo que não sabe para quem escreve.

O conserto tem três movimentos, nesta ordem:

1. **Troque o sujeito.** O sujeito da frase é **você** (o dono) ou **seu
   cliente** — nunca um "ele" solto. "Ele toca na bandeira e o cardápio inteiro
   muda" vira "Seu cliente toca na bandeira e pede sozinho": mesmo fato, e agora
   com dono.
2. **Termine na consequência para o negócio.** Cada slide fecha no que muda para
   ele: fila que anda, mesa que fecha mais alta, equipe que atende mais mesa.
   Descrição de funcionamento sem consequência é documentação.
3. **Venda.** É peça de Instagram de uma empresa que vende sistema, não verbete.
   Constatação bonita não vende; frase que nomeia um ganho, sim. E cuidado com a
   tentação seguinte, que foi o erro da rodada 13: pergunta de cobrança
   (*"Quanto seu salão perde por não falar inglês?"*) vende menos que elogio
   seguido de virada — a seção logo abaixo conta por quê.

| Terceira pessoa, morno | Falando com você, vendendo |
|---|---|
| "Ele queria pedir. Só não sabia o quê." | "Seu cardápio é o seu melhor **vendedor**" (ver "o slide do problema elogia antes de cobrar") |
| "Abre o tradutor no celular e vai lendo item por item." | "Seu cliente abre o tradutor no celular e vai lendo item por item." |
| "Ele toca na bandeira e o cardápio inteiro muda." | "Seu cliente toca na bandeira e pede **sozinho**." |
| "No tablet é a mesma coisa." | "Na mesa, o tablet fala a língua do seu cliente." |
| "A versão em inglês mora no mesmo produto." | "Você escreve uma vez, e **pronto**." |
| "Então as bandeiras já estão aí." | "Seu cardápio pode falar inglês **hoje**." |

### A voz da marca está em beefood.com.br, e é de venda

O site é a régua, e dá para ler em cinco minutos. O padrão de lá, que o carrossel
copia:

- **manchete é ganho, não recurso**: "Aumente suas vendas com Cardápio Digital no
  Tablet", "Mais pedidos, menos filas no seu restaurante", "Mais agilidade e mais
  lucro no salão";
- **fala com o dono o tempo todo**: "Seu cliente pede direto pelo celular", "Dê
  mais autonomia ao seu cliente", "Atenda bem todos os públicos";
- **linha de apoio concreta embaixo da manchete**, sem adjetivo de folheto:
  "Menos necessidade de garçons extras", "Fechamento de contas simples e rápido";
- **verbo no imperativo** convidando: "Comece", "Controle", "Acompanhe";
- **emoji pontual** em título de bloco (🛵 📍 🍽️ 🌎), nunca em fileira.

Duas cautelas que o site cria e o carrossel tem de respeitar:

- a página do tablet diz que o cardápio "é traduzido automaticamente". O produto
  que o carrossel mostra **não** traduz sozinho: quem escreve é o dono. Copiar a
  promessa do site aqui viraria reclamação no comentário.
- "aumento de até 40% do ticket médio" é número do site, para outro recurso. Não
  vale emprestar número de vizinho: no carrossel, o ganho aparece em cena
  concreta ("o pedido sai o mais simples possível, sem combo e sem sobremesa").

### Aviso de limite não entra em peça de venda

O slide 6 do carrossel da tradução dizia "Não precisa traduzir tudo **hoje**" e
listava por onde começar: setores, mais vendidos, o resto quando der. A intenção
era boa — tirar o peso de quem imagina uma tarde inteira de digitação. O que
chegou do outro lado foi: *"dá a entender que o sistema não traduz sozinho e que
é inútil; ele também não traduz sozinho, mas não precisa tocar nisso"*.

O diagnóstico é preciso, e a parte que ensina é a segunda metade. **Aliviar um
trabalho é admitir que existe um trabalho.** Num manual isso é serviço; num
carrossel é uma objeção que o leitor ainda não tinha formulado, plantada no slide
anterior ao CTA — o pior lugar possível.

O que ficou:

- **peça de venda não anuncia o limite do recurso.** Quem precisa do limite abre
  o manual, que está a um clique de distância e é escrito para isso.
- **cuidado com a família de frases que parece gentileza:** "não precisa fazer
  tudo", "aos poucos", "com calma", "sem pressa", "comece pequeno". Todas
  carregam o trabalho junto com o alívio.
- **honestidade não é aviso.** O carrossel continua sem dizer "o sistema
  traduz": ele mostra o cadastro onde a versão em inglês mora, com a mão do
  lojista implícita na tela. O leitor entende sem que ninguém precise soletrar —
  e o `roteiro.md` registra o que é captura e o que é desenho.
- **se o slide ficar sem assunto, procure o que a peça prometeu e não mostrou.**
  Foi o caso: a capa prometia "inglês e espanhol" e o espanhol não aparecia em
  slide nenhum. O slide do alívio virou o slide do espanhol, com prova na
  imagem.

### O slide do problema elogia antes de cobrar

O slide 2 do mesmo carrossel teve três versões, e as duas primeiras erraram por
motivos diferentes: a primeira narrava o turista em terceira pessoa, a segunda
perguntava *"Quanto seu salão **perde** por não falar inglês?"* e listava o que
dá errado no salão. A segunda tem sujeito certo, tom de venda e fecha no custo —
e o dono devolveu de novo.

O que estava errado é o lugar da cobrança. **Slide 2 é onde o leitor decide se
arrasta ou não**, e ali ele recebeu uma fatura: três linhas do que ele faz
errado e um preço no pé. Ninguém salva um post para ler a própria conta.

A terceira versão vira o argumento do avesso, e é o padrão que fica:

1. **elogie o que ele já tem, e com verdade.** "Seu cardápio é o seu melhor
   vendedor" — e é: foto, descrição, combo e adicional na tela são trabalho de
   vendedor.
2. **mostre o furo depois, e no mesmo movimento que a solução.** "Ele só vende
   para quem lê português (…) em inglês e em espanhol, esse vendedor volta a
   trabalhar." O custo continua ("o pedido sai o mais simples possível, sem combo
   e sem sobremesa"), só que agora é consequência de uma premissa que o leitor
   aceitou.
3. **nunca em porcentagem.** Sem número que o BeeFood não publicou.

| Slide de problema que afasta | Slide de problema que prende |
|---|---|
| "Quanto seu salão **perde** por não falar inglês?" | "Seu cardápio é o seu melhor **vendedor**" |
| lista do que dá errado no salão dele | lista do que o cardápio dele já faz bem |
| custo no fim, sozinho | furo e solução na mesma frase |

### Emoji

Passou de "só o que a novidade usa" para **pouco e onde couber**: até um por
slide, em cerca de metade dos slides. O ambiente tem Noto Color Emoji, então sai
colorido no PNG sem configuração.

Dois detalhes que custaram uma rodada:

- **Emoji que aponta precisa de `&nbsp;`.** O 👇 no fim do título caiu sozinho na
  linha seguinte e parecia acidente. Encostado com `&nbsp;`, e com o título em
  uma linha, ele manda o olho para o mockup logo abaixo.
- **Slide de limite não leva emoji.** No slide "não saia marcando tudo" qualquer
  carinha soa sarcástica.
- **Capa com palavra em vermelho não leva emoji.** São dois grifos na mesma
  frase, e o segundo tira força do primeiro. A capa do *Destaque na impressão*
  perdeu o 🥤 quando "bebida" ficou vermelha — e a frase melhorou.
- **A regra vale em todo slide, não só na capa, e sobra o rótulo de bloco.** Em
  *Capas e destaques* os sete títulos têm palavra vermelha: o 👇 do slide da
  vitrine e o 🎬 do CTA eram grifo em cima de grifo, e saíram. O único emoji do
  carrossel foi para o rótulo do cartão ("🎬 O QUE ENTRA DE NOVO"), que não
  disputa com vermelho nenhum. Carrossel com zero emoji também passa; o que não
  passa é emoji colado no grifo.

### Microdetalhe de interface não é conteúdo

A terceira rodada do carrossel da tradução voltou com um recado curto: *"bolinha
verde é exatamente o tipo de explicação desnecessária, isso não agrega em nada"*.
Dois slides gastavam metade do texto ensinando um enfeite da tela — que a
bandeira ganha um sinal verde quando o idioma já tem texto, que o grupo de opções
traduzido atende todos os produtos que o usam. Nada ali é falso. Tudo ali é
**material de manual**, e no feed rouba o lugar do que o dono quer saber.

O teste é uma pergunta: **o que muda para ele se eu tirar essa frase?** Se a
resposta é "nada, ele só sabe menos um detalhe da tela", corta. No lugar entra a
consequência, que é o que ele compra:

| Microdetalhe | O que entrou no lugar |
|---|---|
| "A bolinha verde marca a bandeira que já recebeu tradução" | "Mudou o preço, acabou o estoque? Você mexe num lugar só, e os três idiomas acompanham" |
| "Traduza um grupo de opções e ele vale em todo produto que usa aquele grupo" | (saiu, e o slide inteiro saiu na rodada seguinte — era sobre o trabalho do lojista) |

Mesma régua para caminho de menu, nome de campo e regra de comportamento fina:
entram quando **são** o assunto do slide, nunca como explicação de brinde.

### Quando a prova cabe na imagem, a frase não precisa existir

O slide que substituiu o do alívio tem uma linha de texto e duas imagens: o
**mesmo** item do cardápio, recortado do **mesmo** ponto da tela do totem, um em
inglês e um em espanhol. Mesma foto, mesmo `R$ 11,00`, e o nome saindo de
`FRENCH FRIES` para `PAPAS FRITAS`. Nenhuma frase sobre "três idiomas" convence
como esse par de recortes, e o leitor gasta dois segundos em vez de ler cinco
linhas.

Vale como pergunta de roteiro: **esse slide está explicando algo que a tela já
mostra?** Se sim, o slide é um recorte com rótulo, e o texto vira uma linha só.

Três coisas que a execução ensinou:

- **o recorte tem de ser medido, não fixo.** O `capturar-totem.py` lê a caixa do
  cartão no DOM antes de fotografar (`medir_primeiro_cartao`). É o que garante
  que os dois idiomas caiam no mesmo pixel — e é o que faz o par ler como um
  item só, em vez de duas fotos parecidas.
- **capture em escala 2 o que vai aparecer ampliado.** O cartão tem 248 px no
  aparelho e aparece com 372 na arte; em escala 1 a letra fica pastosa.
- **fileira de grade não tem altura igual em todo idioma.** Em português aquele
  cartão sai 20 px mais alto, porque a altura da fileira é ditada pelo nome mais
  longo do setor (`MOZZA STICKS - PALITOS DE MUSSARELA`, em duas linhas). Com
  três recortes lado a lado, ou os rótulos desalinham ou aparece um degrau
  embaixo; com dois, cada um fica 1,5x maior e o nome dá para ler no feed. Duas
  provas bastam — a terceira língua já está em outro slide.

### Nada de diminutivo

"Bandeirinha", "bolinha", "telinha", "combinho". O diminutivo aparece sozinho
quando a gente tenta soar simpático, e faz o contrário: soa infantil e faz o
recurso parecer pequeno. O cliente lê "bandeira", "sinal", "tela".

A exceção é nome próprio: o produto `PISCININHA` do cardápio de exemplo se chama
assim, e nome de produto não se corrige.

### Cópia literal

O `conferir-texto.py` mecaniza a parte objetiva: acusa sequência de **6 palavras**
igual ao título ou ao texto da novidade. A janela é 6 porque nenhum rótulo do
sistema chega a seis palavras — com janela 4 o script acusa "na ficha da cozinha"
e "logo abaixo de descrição", que **têm** de repetir. Rodando na 1ª versão ele
pega a capa (`a bebida não fica mais para trás`, que era o próprio título da
novidade) e o slide *vale lembrar* (`a equipe volta a não saber o que conferir`);
na 2ª versão passa limpo.

No carrossel de tradução ele pegou duas frases que eu não tinha notado que eram
cópia: "então dá para ver num relance o que falta" (a bolinha verde) e "atende
todos os produtos que o usam" (o grupo de opções). **São as frases boas do
release** — e é por serem boas que a mão as repete. O script não cansa.

Duas coisas que ele precisou aprender na mesma rodada, e que valem como limite
do método:

- **nome de produto não é prosa de release.** "no Totem de Autoatendimento e no
  Cardápio Digital no Tablet" tem nove palavras e estourava a janela sozinho, só
  porque a novidade também precisa dizer em quais aplicativos a coisa funciona.
  A lista `NOMES_DE_PRODUTO` no `conferir-texto.py` troca cada nome por um token
  antes de comparar. Ela é **só para nome que o dono do produto escolheu** —
  cada linha nova ali é uma frase que o conferidor libera para sempre.
- **cabeçalho da copy é nota de produção.** As linhas antes do primeiro `====`
  do `copy-instagram.txt` dizem qual novidade é, com o título dela, e não vão
  para o Instagram. Conferir aquilo só ensinava a escrever cabeçalho ruim.

## Fonte da pauta

`beefood.app/novidades` é um SPA, mas publica **RSS** em
`/novidades/feed.xml`, com o corpo inteiro de cada item em texto puro (101 itens
em 15/09/2026). A página também traz um JSON-LD `CollectionPage` com a lista e as
URLs individuais (`/novidades/<slug>`). Ou seja: **não raspe o HTML e não dirija
navegador para ler a pauta** — o `pauta.py` resolve com `urllib` em menos de um
segundo.

Nas categorias do RSS, a **primeira** é o tipo (`Novidade` / `Melhoria`) e as
demais são as áreas. Os aplicativos (BeeFood App, Cardápio Digital) aparecem na
página, mas **não** no feed.

## Render

- O slide é **fragmento de body**; o `renderizar.py` embrulha. Contrato copiado
  do `open-carrusel` (`wrapSlideHtml`), que é o jeito de garantir que a revisão e
  o PNG saem iguais. O app dele não foi portado: é Next.js 16 + React 19 com o
  **Claude CLI** como subprocesso, dependência que não existe no Cloud Agent e
  que este repositório não precisa — aqui já havia Playwright e Pillow.
- **Fonte de disco, não do Google Fonts.** As `@font-face` apontam para os
  `.ttf` em `assets/fontes/`. Com CDN o screenshot sai com a fonte de fallback
  quando a rede demora, e o layout muda sem aviso.
- **`<base href>` apontando para a pasta do slide.** O HTML embrulhado é gravado
  em pasta temporária; sem o `<base>` toda imagem relativa quebra. Com ele,
  `../imagens-puras/x.png` e `../../../manuais/.../y.png` funcionam iguais.
- `Path.as_uri()` **estoura em caminho relativo** — resolva o caminho de entrada
  antes (`Path.resolve()`).
- O logo entra por `--logo` e `--logo-escuro` no `:root`, não por `<img>`: assim
  nenhum carrossel precisa de uma cópia dos arquivos. O nome do arquivo diz
  **para que fundo ele serve** (`-fundo-claro`, `-fundo-escuro`), não que cor ele
  tem: "logo escuro" é ambíguo e foi o que levou a inventar um negativo.

## Logo: duas artes oficiais, uma por tipo de fundo

A marca tem **duas versões prontas**, e a escolha é pelo fundo do slide:

| Arquivo | Onde | O que muda |
|---------|------|------------|
| `logo-beefood-fundo-claro.png` | slide claro (`.slide`, `.slide--suave`) | "BEE" em **preto** |
| `logo-beefood-fundo-escuro.png` | slide escuro (`.slide--capa`) | "BEE" em **branco**, e o selo ganha contorno branco |

O resto é igual nas duas: asa **branca**, cabeça **preta**, tarja amarela, "food"
vermelho. O selo não é o negativo dele mesmo — é o mesmo desenho com um contorno
branco acrescentado para descolar do fundo preto.

Isso custou duas tentativas erradas, e as duas estão anotadas porque são
tentadoras:

1. **`filter: brightness(0) invert(1)`** no logo do slide escuro. Resolve a
   visibilidade e **mata a identidade**: achata todos os tons em branco, e vão
   embora o amarelo da abelha e o vermelho do "food", que é o que faz o logo
   parecer o logo.
2. **Negativo gerado pixel a pixel** (preto→branco, branco→transparente). Mantém
   a cor, mas inverte a asa e a cabeça junto: a asa some no fundo e a cabeça
   acende. Fica um selo parecido, e errado.

A regra que fecha o assunto: **arte de marca não se calcula, se pede.** Quando
falta uma versão do logo, peça o arquivo ao dono em vez de derivar — foi o que
aconteceu, e o arquivo existia desde o começo. O `marca.json` aponta os dois, o
`renderizar.py` injeta os dois (`--logo` e `--logo-escuro`) e o `base.css` troca
sozinho no `.slide--capa`.

## Legibilidade (o erro que mais se repete)

Print de painel reduzido para a largura do slide fica ilegível no feed. A conta:
um recorte de **N px de largura lógica** exibido na largura útil de 904 px mostra
o texto da tela a `904 / N × 12` px.

| Recorte | Texto na arte de 1080 px | Serve? |
|---------|--------------------------|--------|
| modal inteiro (~1030 px) | ~10 px | não |
| meia tela (~600 px) | ~18 px | limite |
| faixa de um campo (~440 px) | ~25 px | sim |

No carrossel *Destaque na impressão* a primeira tentativa usou a faixa
*Descrição → interruptor* inteira (1030 px) e não dava para ler. O que resolveu
foi fechar no **interruptor com o rótulo e a linha de apoio** — e escolher a
borda direita em área vazia, porque corte no meio de uma palavra parece defeito.

A tabela vale para mockup **dentro da margem**, onde a largura útil é 904 px. Em
sangria a largura de exibição vai a 1120 px, o que empurra o teto de ~440 px para
~620 px lógicos — a conta refeita está em *Mockup de computador*, abaixo.

## Nada de data na arte

A capa saía com a data da novidade no canto superior direito, que parecia
inofensiva — é o canto que o contador do Instagram cobre, e era informação
dispensável. **Datava o post.** Carrossel aprovado não é publicado no dia: ele
entra na fila de conteúdo e sai dias ou semanas depois, e aí a arte anuncia uma
novidade que parece velha. Pior, ela envelhece no arquivo: o mesmo carrossel não
pode ser republicado nem reaproveitado.

O topo direito agora leva só **"N de 8"**, na capa também. A classe deixou de se
chamar `.data` e virou `.contador` — nome de classe é regra, e enquanto ela se
chamava `.data` alguém ia pôr uma data ali de novo.

Onde a data **pode** ficar:

- **dentro de um print de verdade.** O cupom da capa sai com "15/09/2026 21:01"
  porque é a data do pedido impresso, e essa é do papel, não do post. Cupom sem
  data pareceria adulterado.
- **no `roteiro.md` e no cabeçalho do `copy-instagram.txt`**, como referência de
  qual novidade é. É nota de produção, não sai na arte.

E onde ela se esconde: **print da própria página de novidades**. O CTA de capas
e destaques leva o celular na `beefood.app/novidades`, e o cartão da publicação
começa com as etiquetas e o "13/08/2026". A data é legítima na página e mata o
post do mesmo jeito. A correção é de rolagem, não de retoque: o
`capturar-telas.py` encosta o **título** no cabeçalho fixo em vez do cartão
inteiro, e etiquetas e data ficam atrás dele. Antes de fechar um CTA com print
de página nossa, leia o que aparece na primeira linha do print.

## Zona segura — o que o Instagram realmente cobre

A primeira versão do `--guias` pintava 120 px no topo e 180 px na base do 4:5.
**Está errado para o feed:** ali o Instagram não sobrepõe barra nenhuma à arte —
o cabeçalho do perfil e os botões de curtir ficam fora da imagem. O que ele
desenha por cima é o **contador do carrossel**, no canto superior direito.

Consequência de projeto: o canto superior direito do slide leva só coisa
dispensável — o `.contador`, e nada além dele. As faixas de topo e base valem para o
**story (9:16)**, e o `--guias` agora pinta a zona certa de cada formato.

## Onde a imagem fica na faixa

Regra que organiza todas as outras de arte, e que só ficou clara na 5ª rodada:

> **Imagem sozinha na faixa vai centralizada e no maior tamanho que couber, e
> reta. Encostar numa borda e inclinar só se paga quando o outro lado tem
> conteúdo.**

Era o que estava errado na capa: o cupom encostado na direita e girado em 3D
deixava a metade esquerda do slide vazia **e** saía menor do que podia, porque a
inclinação come altura. Centralizado e reto, o mesmo recorte cresceu e a capa
recuperou o subtítulo de duas linhas que tinha sido cortado para dar espaço.

Como isso se traduz nas classes:

| Situação | Classe | Posição |
|----------|--------|---------|
| imagem ocupa a faixa toda, sem sangrar | `.figura` | no fluxo, `align-self: center`, a maior largura que a base aceita |
| mockup sozinho na faixa, sangrando | `.sangria` com recuo **igual** dos dois lados | centralizado, sangrando só pela base |
| mockup dividindo a faixa com texto | `.sangria` encostada + `.cena3d`/`.g3d` | de um lado, e aí o 3D tem função |

Sangrar não é o mesmo que ficar torto: o celular do CTA sangrava pela base *e*
estava encostado na direita sem nada do outro lado. Centralizar o recuo e subir
de 586 para 660 px de largura fez o texto da página caber legível, e o rodapé
saiu porque o aparelho passou a cobrir a base inteira.

E o caminho inverso vale: para manter o 3D no slide do entregador, o corpo do
texto **desceu para uma coluna de 412 px ao lado do celular**. Foi o que deu
licença para o aparelho sair do centro.

## Mockup em sangria — o padrão

Aparelho inteiro dentro da margem sai com ~420 px de largura numa arte de 1080,
e a tela dentro dele fica pequena demais para o feed. A correção é **sangria**:
o mockup começa por volta de 27% da altura, ocupa pouco mais de meia largura e
sai pela borda. Além de ganhar escala, o corte na borda passa a sensação de que
a tela continua. Medidas do esboço do dono, já em `.sangria` no `base.css`:
topo 371 px, largura 586 px, recuo 118 px na direita.

Consequência de layout: **o texto mora todo acima do mockup**. A coluna que
sobra ao lado (288 px) é estreita demais para 38 px de corpo. Orçamento medido:

| Mockup | `top` | O que cabe acima |
|--------|-------|------------------|
| celular (`.sangria--celular`) | 530 px | chapéu + título de 2 linhas (`titulo--pequeno`) + 2 linhas de corpo |
| janela (`.sangria--janela`) | 700 px | chapéu + título de 2 linhas + 4 linhas de corpo |

### A imagem da capa

A capa do *Destaque na impressão* foi refeita três vezes. O que cada rodada
ensinou, na ordem em que doeu:

**A imagem da capa mostra UM destaque.** A 1ª versão usava o cupom inteiro do
manual #99, que sai com duas linhas em fundo preto (a Coca Cola e o "Sem
Maionese Verde"). A capa ficava bonita e dizia o contrário do slide do limite —
"não saia marcando tudo" logo depois de uma foto com tudo marcado.

**Recortar para sobrar um destaque só nem sempre é possível.** As duas faixas do
cupom do manual são **coladas**: uma acaba em y 390 e a outra começa ali. Não há
branco entre elas, então todo corte cai em cima de tinta e parece erro de render.
Gastei uma rodada tentando `aspect-ratio` em 390, 400, 472 e 590 — nenhum fecha.

**Quando a matéria-prima não dá, gere matéria-prima nova — não desenho.** O jeito
certo foi montar no sandbox um pedido em que só a bebida tem destaque (combo sem
o complemento marcado) e imprimir o cupom dele. Continua sendo impressão de
verdade, e a linha preta é uma só. Ver `registrar_pedido()` em
`carrosseis/destaque-impressao/capturar-telas.py` e `salvar_cupom()` na skill.

Duas consequências que valem para qualquer captura de cupom:

- **Imprima estreito.** A página de impressão centraliza uma bobina de largura
  fixa; num viewport largo sobra margem branca dos dois lados e o recorte da arte
  teria que mexer no eixo X também, o que `.recorte--topo` não faz. Em 340 px o
  papel é a imagem inteira e o slide só declara onde cortar em cima.
- **Separe registrar de imprimir.** Registrar cria venda no sandbox; reimprimir
  não cria nada. Duas etapas no script, e a arte pode ser refeita à vontade.

**Onde cortar se acha pela tinta.** Mapeie as faixas de tinta do PNG e corte numa
faixa branca larga o bastante para o dente da serrilha:

```python
from PIL import Image
g = Image.open('01-cupom-bebida.png').convert('L')
w, h = g.size
for y in range(h):
    tinta = any(g.getpixel((x, y)) < 120 for x in range(w))
    ...            # faixas: 454-519 preta, 532-535 traço, 557-587 "Subtotal"
```

No `01-cupom-bebida.png` (680×2200) os intervalos brancos entre linhas têm ~20 px.
`680 / 554` é a última janela que cabe: pega tudo até o traço duplo que fecha o
bloco de itens e para antes do "Subtotal". Cortei em 590 primeiro, e o "Subtotal"
entrou e foi mordido pelos dentes.

**Corte reto em papel parece defeito; dente parece papel destacado.** É o que
`.rasgado` faz (máscara na base do `.recorte`). Duas regras de uso:

- vai no **mesmo elemento** do `.g3d`, porque a máscara recorta box-shadow e
  pseudo-elemento junto — em elementos separados o dente aparece dentro de um
  retângulo;
- a máscara **come a sombra**. Em fundo escuro isso não custa nada (sombra escura
  em fundo escuro não aparece); em slide claro, custa, e aí é melhor corte reto.

**O papel é objeto na bancada, não elemento sangrado** — e, estando sozinho na
faixa, vai **centralizado**: `.figura` com 728 px de largura (o máximo que cabe
entre o subtítulo e o "Arraste"), inteiro dentro do slide, canto de 5 px (bobina térmica não tem canto arredondado, e os 24 px que o
`.recorte` traz de fábrica faziam o papel parecer cartão). A versão encostada na
direita e girada em 3D deixava a metade esquerda vazia e saía menor. A regra da
sangria continua valendo para mockup de aparelho — não para recorte de papel.

**Imagem em pé na capa custa uma linha de subtítulo.** A capa do *Destaque na
impressão* tem título de 2 linhas **e** subtítulo de 2 linhas porque a imagem é
um cupom deitado (680×554). Na capa da tradução a imagem é um totem, em pé: só o
aparelho come 830 px de altura, e com duas linhas de subtítulo ele começava
dentro do texto. Ficou com uma linha, e o resto do recado foi para a legenda.
Orçamento da capa com aparelho em pé: pílula + título de 2 linhas + **1** linha
de subtítulo, e o mockup começando por volta de 520 px.

**Na capa, tela cheia ganha de tela icônica.** A tela de espera do totem é a
imagem-símbolo do recurso (botão vermelho grande e as três bandeiras embaixo), e
foi a primeira capa. No render apareceu o problema: o miolo dela é um gradiente
(no aparelho de verdade roda vídeo), e isso virou um vão morto de ~300 px no meio
da capa. Trocada pelo **cardápio em inglês**, que enche a tela e ainda prova a
frase da capa. A tela icônica foi para o slide 3, onde a coluna de texto ao lado
equilibra o vão.

**Aparelho escuro em slide escuro desaparece.** O totem foi desenhado preto e na
capa preta virou uma silhueta sem contorno: a tela lia, o aparelho não. Na hora
isso foi tratado como problema de contraste e resolvido com uma variante clara —
depois a foto do catálogo mostrou que o totem **é branco**, e o `.totem` passou a
ser branco por padrão. Fica a regra geral, que vale mesmo quando a cor certa
resolve sozinha: **mockup tem de contrastar com o fundo do slide**; se o produto
só existe na cor do fundo, o jeito é trocar o fundo (`.slide--suave`), não
inventar um modelo que não existe. E o tablet, que **é** preto, ganhou o fio de
alumínio da carcaça real em volta da moldura — detalhe verdadeiro que também
resolve o contraste.

**Duas capas quando os dois aparelhos importam.** A novidade da tradução vale
para totem **e** tablet, e não dá para ter os dois grandes na mesma capa. Em vez
de escolher no lugar de quem publica, saíram duas: `01-capa.html` com os dois
(informa mais, cada tela menor) e `capa-alternativa/slides/01-capa-so-totem.html`
com um só (tela legível no feed). A alternativa mora em **pasta separada** — o
`renderizar.py` transforma em PNG todo `.html` de `slides/`, e duas capas na
mesma pasta viram um carrossel de oito imagens com dois slides "1 de 7". O
`empacotar.py` leva só o carrossel; a capa alternativa vai no recado.

**Capa honesta vende mais que capa perfeita.** Na capa da tradução, o setor
`MOLHOS ADICIONAIS` aparece em português ao lado do `DRINKS` traduzido, e isso
dilui um pouco o "fala inglês". Ficou: é o comportamento real do produto, é o que
o slide 6 promete, e é o detalhe que faz um dono desconfiado acreditar no resto.
Capa que promete mais do que o produto entrega volta como reclamação.

**A faixa preta cai no terço de baixo, e está tudo bem.** Antes dela há 454 px de
cabeçalho de cupom (PDV, empresa, número, data), ou seja ~40% da tira. Dá para
subir a faixa cortando o topo por `object-position`, mas aí o topo também vira
corte e precisa de serrilha; não compensa. O olho vai na faixa de qualquer jeito:
é o único preto sobre a única forma branca do slide.

- **Rodapé só onde sobra chão.** A janela cobre a base inteira; pontos desenhados
  por cima dela parecem sujeira, e o slide fica melhor sem rodapé (o "4 de 8" do
  topo basta). Com o celular, os pontos caem à esquerda do aparelho (x < 376) e
  podem ficar.
- **Sem notch.** A ilha desenhada em cima da captura tapa o cabeçalho da própria
  tela que o slide quer mostrar. A moldura arredondada já comunica "celular".
- Moldura de celular em CSS (`aspect-ratio: 390/844`) resolve o que nos manuais
  exigia o `montar_celulares` do `annotate.py`: o print entra como `<img>`,
  reduzido pelo navegador, sem passo de montagem em Pillow.
- Captura de celular: `--dispositivo celular` (390×844, `device_scale_factor=3`).
  O 3× existe porque o print entra reduzido na moldura e o 2× já mostrava serra
  no texto pequeno.

## Mockup 3D — só quando divide a faixa

Oito slides com o mesmo mockup reto viram catálogo. `.cena3d` + `.g3d` põem o
mockup em perspectiva: o pai dá o ponto de fuga e o filho gira. Sem o
`perspective` no pai, `rotateY` sai como achatamento, não como profundidade.

**São duas condições, e as duas têm de valer.**

1. **O aparelho é celular ou janela de computador.** Só. Totem e tablet vão
   sempre retos. O que o 3D valoriza é a espessura da peça girando; um totem é
   um armário em pé e não tem espessura para mostrar — girado, ele lê como
   armário tombando. O slide 3 do carrossel da tradução saiu assim na primeira
   versão e o dono devolveu na hora. Tablet no suporte tem o mesmo problema, com
   o agravante de o suporte sair torto.
2. **O mockup está dividindo a faixa com alguma coisa.** Imagem sozinha fica
   centralizada, grande e reta. Inclinar uma imagem que tem o slide todo para si
   troca tamanho por efeito, e tamanho é o que faz a imagem funcionar no feed.

Três coisas que fazem o 3D ler como 3D:

1. **Luz.** Face girada sem gradiente fica chapada. O `.g3d::after` joga um
   clarão do lado da quina que está na frente e escurece a que recua.
2. **Sombra deslocada**, e caindo para o lado oposto à luz. Sombra centrada
   continua parecendo adesivo.
3. **Giro pequeno.** 14° em Y, 5° em X e 2° em Z. Acima disso a borda de fora
   cresce e invade a margem, e o texto da tela começa a distorcer.

**Sempre virado para dentro.** A quina que afunda é a **de dentro**, a que aponta
para o texto: o aparelho parece entrar no slide. Girado ao contrário, a face abre
para o texto, a quina de dentro vem para frente e o aparelho parece estar caindo
para fora da arte — é o que estava no primeiro render do slide 6.

O ganho é medível, não é só gosto: no slide 6, com a coluna de texto acabando em
x 500, o vão mais estreito entre texto e aparelho passou de 51 para 71 px, e na
altura do primeiro parágrafo, de 72 para 134 px. A quina que recua abre espaço
exatamente onde o texto está.

Por isso o nome da classe é **pelo lado do slide em que o mockup está**, não pelo
eixo do `rotateY`: `.g3d--na-direita` e `.g3d--na-esquerda`. Nomear pela borda que
recua (`--direita`/`--esquerda`, como estava) obriga a refazer a conta a cada
slide, e a conta saiu errada na primeira vez. Cada variante leva a luz e a sombra
espelhadas junto — luz do lado da quina da frente, sombra caindo para o outro.

**Onde não usar:** no slide em que o leitor precisa ler rótulo de interface. A
face que recua come contraste justo onde está a informação. Neste carrossel o
slide 4 (achar o interruptor) ficou reto e o slide 6 (ilustração do app, texto
grande, com coluna de texto ao lado) ficou em 3D — um 3D a cada dois ou três
mockups é o suficiente para dar ritmo.

**O brilho do 3D cobre a caixa toda, não só a tela.** (Vale para celular, que é
onde o 3D é permitido; o caso abaixo é do totem porque foi ali que apareceu.) O
`.g3d::after` usa `inset: 0`, então ele pinta tudo que está dentro da caixa do
elemento girado. No primeiro render do totem em 3D saíram **duas abas brancas**
embaixo, dos lados da coluna: a coluna ocupa 30% da largura, o resto da linha é transparente, e o
brilho pintou o vão. A correção mudou a estrutura do mockup, não o gradiente: no
`.totem` e no `.tablet` a caixa é **só o corpo da tela**, e coluna, haste e pé são
`position: absolute` pendurados embaixo (`top: 100%`). Absolutos, giram junto com
o pai e ficam fora do retângulo que recebe o brilho.

Regra para o próximo mockup: **a caixa do elemento que leva `.g3d` tem de ser a
tela, e nada além dela.**

**Efeito colateral útil:** aparelho que termina dentro do slide mostra a base da
tela, e aí a barra de ação da ilustração tem de ir para lá (`flex: 1` no
`.tela-app__corpo` e `margin-top: auto` no `.tela-app__aviso`). Sem isso a tela
fica com um vazio de 300 px embaixo e parece render pela metade. Em mockup que
sangra pela base é o contrário: o aviso fica no fluxo, senão sai do slide.

## Mockup de computador

Tela de painel é tela de computador, e o mockup dela é a `.navegador`. Sendo
deitada, ela **sangra pela direita** em vez de pela base — e é isso que permite
passar de 1000 px de largura. Com `.sangria--janela` (1120 px), um recorte de
605 px lógicos sai a **1,85×**: o rótulo de 15 px da interface vira 27 px na
arte, que é a faixa legível da tabela acima. Recorte de painel inteiro
(1440 px lógicos) na mesma janela sai a 0,8× e não se lê.

Ou seja: a janela grande **não dispensa o recorte**, ela muda o limite. Antes o
teto era ~440 px lógicos (faixa de um campo); com sangria, vai a ~620 px (meia
tela), que é o que deixa a tela parecer tela em vez de tira.

### Notebook e monitor: a janela mostra a página, o aparelho mostra a cena

A 15ª rodada acrescentou `.notebook` e `.monitor`. A escolha entre os três não é
de gosto:

- **`.navegador`** mostra a **página**. É o mockup de "olhe este campo" — aceita
  `.realce` e vive de recorte.
- **`.notebook`** mostra a **cena**: alguém sentado, olhando aquilo. Numa capa
  isso vale mais que 100 px a mais de tela. A capa deste carrossel é o caso: o
  assunto era o cardápio virar vitrine, e vitrine se olha de longe.
- **`.monitor`** é o lugar de trabalho do dono, em 16/9.

O desenho de cada um, com as armadilhas de CSS, está em
[`mockups.md`](mockups.md). Duas valem repetir porque já custaram render em
outros aparelhos e voltaram aqui: peça de baixo (base, pescoço) **absoluta,
pendurada fora da caixa** — senão o brilho do `.g3d::after` pinta o vão das
quinas —, e `clip-path` **recorta os filhos**, então o afunilamento do pescoço
não pode ficar no invólucro do pé.

E uma nova: o `overflow: hidden` do `.slide` **come a base do notebook** quando
ele encosta no limite de baixo. A correção é subir o mockup alguns pixels, não
encolher.

### Realce, e por que medir

`.realce` é o anel vermelho que diz "olhe aqui", posicionado em porcentagem
dentro do `.navegador__tela`. Duas tentativas circularam a linha errada porque a
porcentagem foi estimada olhando a miniatura. O que resolveu foi medir no
arquivo — o interruptor verde era a única região saturada da imagem:

```python
from PIL import Image
im = Image.open('imagens-puras/03-modal-janela.png').convert('RGB')
W, H = im.size; px = im.load()
p = [(x, y) for y in range(H) for x in range(W)
     if (lambda r, g, b: g > 120 and g - r > 50 and g - b > 50)(*px[x, y])]
print(min(x for x, _ in p)/W, min(y for _, y in p)/H)   # → 0.134, 0.696
```

Cuidado que custou uma rodada: a altura do recorte **não** é a fração que você
pediu no `--recorte` × 1350 — o viewport de captura é 1440×900, não 1440×1350.
Leia a medida do arquivo com Pillow antes de calcular porcentagem.

## Totem e tablet — mockup de equipamento

Celular e navegador não cobrem tudo: a novidade da tradução acontece no **Totem
de Autoatendimento** e no **Cardápio Digital no Tablet**. Os dois mockups vivem
no `base.css` (`.totem`, `.tablet`).

> Esta seção é a **história**: o que se tentou, o que o dono devolveu e por que
> cada peça existe. O **estado atual** — largura de uso, telas disponíveis,
> fotos prontas — está em [`mockups.md`](mockups.md), com a folha do catálogo.
> Para usar, leia o `mockups.md`; para mexer no aparelho, leia os dois.

### Antes de desenhar, procure a referência — inclusive no `main`

Esta seção começou errada e foi refeita. A primeira versão do totem e do tablet
foi desenhada **de memória**, com "o que um totem parece": carcaça preta, tela
escura, lista vertical de itens; e um tablet claro com grade de cartões. O dono
devolveu como *"fora do layout"* e *"foge totalmente do padrão"*, e o problema
não era CSS — era não ter procurado como o produto é de verdade.

Existem duas fontes, e as duas são baratas:

- **os prints de produção, dentro deste repositório.** O manual da mesma
  novidade já os versionava em
  `manuais/traducao-cardapio-presencial/imagens-puras/`. Eles não apareciam no
  checkout porque o manual entrou **depois** do build do ambiente — o Cloud
  Agent parte de um snapshot. Um `git fetch origin main` e um
  `git ls-tree -r --name-only origin/main -- manuais/<slug>` resolvem. **Faça
  isso sempre**: manual publicado é a referência mais forte que existe, e a mais
  fácil de deixar passar.
- **as páginas de produto do site**, para o corpo do aparelho:
  `beefood.com.br/totem-de-autoatendimento` e `/cardapio-digital-tablet`.
  Capture com `capturar.py --publico` e recorte a foto do aparelho.

O que a referência corrigiu, e que nenhuma intuição acertaria:

| | desenhado de memória | como é |
|---|---|---|
| totem, carcaça | preta, canto de 28 px | **branca**, canto quase reto |
| totem, tela | escura, lista vertical | banner no topo, coluna de setores em **miniatura de foto**, grade de produtos com foto e barra vermelha da sacola no pé. O tema é do estabelecimento: o print do manual é claro, o totem de exemplo é escuro |
| tablet, tela | clara, grade de dois cartões | **escura**, cartões deitados com foto à esquerda, preço em **amarelo**, botão `Order` |
| tablet, suporte | pedestal fino com pé chato | **chapa de alumínio** larga que sai de trás e dobra até a mesa |
| bandeiras | redondas nos dois | redondas no totem, **retangulares** no tablet |

### O que faz cada aparelho ler como o que é

| Aparelho | O que dá a leitura | O que errei primeiro |
|---|---|---|
| totem | carcaça **branca**, tela 9/16 com moldura preta fina, **painel** embaixo com leitor de aproximação, boca de impressora e **pinpad**, e coluna + base pretas mais estreitas que a carcaça | sem o painel, é um celular gigante numa coluna; o painel é o que diz "autoatendimento" |
| tablet | moldura **proporcional e igual nos quatro lados** (`padding: 4.4%`), canto **bem arredondado** (38 px), fio de alumínio em volta, dois botões na lateral direita, ponto de câmera na moldura da esquerda e a **chapa larga** atrás | moldura em px, canto de 20 px e pedestal com pé: sai um iMac |

O tablet custou cinco rodadas, e o que resolveu foi medir em vez de opinar:

- **moldura em px não escala, e 2,2% ainda era fina.** O mockup nasceu com
  `padding: 11px`, que é 1,5% de uma largura de 720 e 1,2% de uma de 880: quanto
  maior o slide usa o aparelho, mais a moldura desaparece e mais ele vira
  monitor. Em `%` o `padding` mede a própria largura do elemento e a moldura
  acompanha — mas o primeiro valor em `%` foi chutado. Medido na foto do
  catálogo, o aparelho de 960 px tem ~45 px de preto de cada lado, ou seja
  **4,4%**, o dobro do que estava. Moldura grossa é o que separa tablet de
  monitor mais do que qualquer outro detalhe.
- **o canto é o sinal mais forte.** 20 px de raio em 880 de largura é canto de
  monitor; 38 px já é tablet. Em px e não em `%`, que daria elipse.
- **4/3 pareceu "mais tablet" e não é.** Testei, encolhe a tela e inventa um
  aparelho que o cliente não tem — o aplicativo roda em tablet Android, 16/10,
  que é também a proporção do print de produção (1280×800).
- **o suporte não é um trapézio, e também não é coluna com base.** Duas
  tentativas com `clip-path` de trapézio invertido saíram lendo "chapéu chinês"
  embaixo do aparelho. Depois vieram três tentativas de rolo estreito com aba
  oval na mesa, imitando a perspectiva da foto — e as três leram como **pedestal
  de monitor**, porque em desenho frontal "coluna + base" é monitor, ponto. O
  que funcionou foi **uma chapa só**, larga e rasa, abrindo 5% para cada lado de
  cima para baixo (`clip-path`), com o vinco da dobra a 76% e a aba de baixo mais
  clara.
- **e a chapa tem de ser grande.** Ela entrou com 46% da largura do aparelho por
  `100 / 24`, e ainda lia como pé de monitor: pequena demais para ser suporte.
  Medindo a foto do catálogo, a chapa ocupa **66% da largura** do aparelho e 23%
  da altura dele — e ali a foto está em perspectiva, que alarga. Frontal,
  **58% por `100 / 25`** é o que ficou parecido. Regra que serve para qualquer
  peça acessória: se ela lê como acessório de outro objeto, quase sempre está
  pequena, não malfeita.

  A lição geral: a foto do catálogo está em perspectiva e o mockup é frontal.
  **Copie a peça, não a pose.** Reproduzir o que a perspectiva revela (o lado do
  rolo, a aba fugindo para a direita) num desenho frontal devolve outro objeto.

Medidas que cabem no slide, com o texto acima:

| Mockup | Largura | Altura até a base da carcaça | Onde |
|---|---|---|---|
| totem sozinho (capa) | 400 px | 782 px (tela 626 + painel 141 + topo 16) | `top: 532px`, centralizado, coluna sangrando pela base |
| totem ao lado de texto | 420 px | 821 px | `top: 452px`, `right: 40px` |
| totem com outro aparelho (capa) | 384 px | 751 px | `top: 366px`, `right: 48px` |
| tablet inteiro | 880 px | 579 px + 128 px de chapa | `.figura`, centralizado |
| tablet com outro aparelho (capa) | 660 px | 434 px + 96 px de chapa | `top: 872px`, `left: 54px`, sangrando pela base |

**Aparelho em pé na capa pode sair pela base**, e é melhor que caber inteiro: a
borda de baixo do slide lê como chão. O que **não** pode sair é o painel do
pinpad, que é o que identifica o totem — corte a coluna, nunca o painel.

**Bandeira do seletor é emoji recortado em círculo** (`.bandeira`), não SVG novo
no repositório: o ambiente tem Noto Color Emoji, 🇧🇷 sai igual em toda máquina e
o `scale(1.5)` dentro do círculo é o que faz a tinta cobrir os cantos (a bandeira
emoji é ondulada e mais larga que alta). `.bandeira--anel` marca o idioma em uso,
como o sistema faz. No **tablet** elas são retangulares (`.bandeira--retangular`)
e empilhadas — dois aparelhos, dois desenhos. O sinal verde de "esse idioma já
tem texto" não entrou no desenho: ele só existe no cadastro, de onde existe
captura real, e nem lá o carrossel explica o que ele é (veja *Microdetalhe de
interface não é conteúdo*).

### A coluna de setores, e por que 24%

A coluna da esquerda da tela do totem nasceu com 21% e, no totem pequeno da
capa, `COMBOS (BURGER + PORÇÃO + BEBIDA)` quebrava em **seis linhas**: a coluna
virava uma pilha de fragmentos de uma palavra, e lia como layout estourado. Não
era `word-break` — era só coluna estreita com nome longo.

24% é a medida do print (230 px de 1024) e derruba o pior caso para quatro
linhas. Mais largo que isso só rouba da grade de produtos, que é onde estão as
fotos e os nomes em inglês.

Duas coisas relacionadas, para não perder tempo de novo:

- **letra minúscula no render não é quebra de palavra.** Em 8 px, `MOLHOS` com
  `letter-spacing` sai com vãos que parecem `MOL HOS` quando você dá zoom no
  PNG. Antes de mexer no CSS, meça: `Range.getClientRects()` no elemento diz
  quantas linhas o texto ocupa de verdade.
- **grade de 2 colunas na tela do totem, sempre.** Em 3 (como no print) o nome
  do produto quebra em três linhas dentro do cartão e sobra um vão branco
  embaixo. O setor Drinks tem três produtos, então a segunda linha fica com um
  cartão só — e isso é o que uma tela de duas colunas mostra mesmo.

### O corte da rolagem não pode cair em cima de número

A tela desenhada do totem é **cortada** pelo que cabe (`.tela-totem__rolagem`),
com a barra da sacola fixa no pé — é assim que a tela se comporta e evita vão
branco no meio. Mas *onde* o corte cai é escolha sua, e cortar no meio dos
dígitos de `R$ 8,90` lê como falha de render, não como tela rolada.

O parâmetro que move o corte é o `font-size` da `.tela-totem`, porque tudo lá
dentro é `em`. Vale varrer alguns valores e escolher o que deixa o último cartão
**inteiro** (ou cortado dentro da foto): 19 px no totem de 420 px do slide 3, com
quatro cartões em duas linhas. No tablet a conta é a mesma com outro alvo — o
preço do último item tem de caber (16 px em 880 px de largura, três itens). Dá
para medir sem olhar, comparando `rolagem.bottom` com `card.bottom`,
`img.bottom` e `preco.bottom`.

### Pílula escura em fundo escuro

Aprendido com o antigo carimbo de ilustração, e vale para qualquer peça de
interface da arte: pílula `rgba(30,30,30,.72)` em cima do `--escuro` da capa
**não existe** — sobra o texto branco solto no vão, que lê como legenda perdida.
**Toda pílula escura precisa da versão clara** antes de ser usada na capa.

### Três armadilhas de CSS que custaram render

- **dois blocos com o mesmo seletor, e o segundo ganha calado.** O redesenho do
  tablet entrou como um bloco `.tablet` novo, e o bloco antigo continuou no
  arquivo mais abaixo. Cascata resolve empate pela ordem: o `background`
  chapado e a ausência do fio de alumínio do bloco velho venceram o desenho
  novo, e o render saiu sem metade do trabalho. Ao redesenhar, **apague o bloco
  antigo**; e depois confirme com `grep -n '^\.classe {'` que ele existe uma
  vez só.

- **`.moldura img` pega as imagens de dentro da tela desenhada.** `.totem__tela
  img { height: 100% }` foi escrito para o print que ocupa a tela inteira, mas
  alcançava também as fotos dos cartões desenhados dentro dela — e o `height`
  anula o `aspect-ratio` delas. As fotos esticavam e o texto do cartão sumia.
  Regra de moldura é sempre **filho direto**: `.totem__tela > img`.
- **`flex: none` numa `<img>` dentro de flex column lê a altura do arquivo.**
  Com `flex-basis: auto`, o navegador usa a altura intrínseca da imagem e ignora
  o `aspect-ratio`. Cartão de grade é melhor em **bloco**: em flex column, a
  foto é a peça que cede quando a grade estica a linha, e duas fotos lado a lado
  saem com alturas diferentes.

## Ilustração de tela (imagem "fake")

App Android (Garçom, Entregador, Tablet) não sobe no Cloud Agent, e o slide que
mostra o efeito na rua era justamente o que faltava. A saída é desenhar a tela em
HTML/CSS (`.tela-app`, `.tela-totem` e `.tela-tablet` no `base.css`, modelos
`ilustracao-app.html`, `mockup-totem.html` e `mockup-tablet.html`), com ordem de
preferência clara: **captura real > print de produção que já está no repositório
> print pedido ao dono > ilustração**. O segundo degrau é novo e é o mais
esquecido: o manual da mesma novidade costuma ter o print, e ele pode estar só
no `main` (veja *Antes de desenhar, procure a referência*).

**Quando o print existe mas não encaixa, desenhe em cima dele.** O print do
totem é paisagem e a tela do aparelho é retrato; e print de tela cheia reduzido
para caber num slide fica com letra de 4 px no feed. Nos dois casos, colar o
arquivo inteiro na moldura é pior que desenhar. O meio-termo que funcionou:

- o CSS copia o **layout, a paleta e a hierarquia** do print, com a tipografia
  ampliada e uma coluna a menos na grade quando o nome não sobrevive à redução;
- as **fotos são as reais**. Melhor caso: baixe do `s3Link` da API do próprio
  aplicativo (veja *O totem é web*). Sem API, recorte do print com um script na
  pasta do carrossel, coordenadas **medidas no arquivo** com Pillow e comentadas
  no script. Foto de comida inventada é o que mais denuncia tela desenhada;
- pedaços que já vêm prontos entram inteiros. O banner do topo do totem é um
  recorte só, e traz o `CANCEL ORDER` e a pílula de bandeiras de produção
  dentro — é o pixel mais convincente do carrossel e não custou nada desenhar.

Duas condições, as duas obrigatórias:

1. o comportamento desenhado está escrito na novidade ou no manual;
2. o desenho usa o vocabulário do carrossel (cartão arredondado, Mulish, cor da
   marca) e **não** imita a interface real pixel a pixel.

### O carimbo "ILUSTRAÇÃO" saiu da arte, e não volta

Existiu por três rodadas uma pílula `.selo-ilustracao` no canto do slide com
tela desenhada. A intenção era honestidade. O efeito no feed é outro: numa peça
de venda, "ILUSTRAÇÃO" é a única palavra que ninguém esperava ler, o olho vai
nela antes de ir no título, e o que ela comunica é "o que você está vendo não é
o produto" — justamente no slide que devia convencer. Nenhuma marca carimba a
própria vitrine.

O carimbo saiu do `base.css`, dos modelos e dos dois carrosséis já entregues.
**A honestidade não saiu — ficou mais cara:**

- a tela desenhada copia layout, paleta e hierarquia do print de produção, e usa
  as **fotos reais** que a API serve;
- o desenho só mostra comportamento escrito na novidade ou no manual;
- o `roteiro.md` diz, slide por slide, o que é captura e o que é desenho. É lá
  que a auditoria mora, não em cima da arte.

**Texto de interface em outro idioma só entra se vier da tela.** `SEARCH`,
`MY CART`, `MY BILL`, `CANCEL ORDER`, `Order`, `Your bag is empty`: isso é o
aplicativo falando, e inventar uma tradução dessas é inventar comportamento do
produto. Todas as que estão nos slides saíram de print ou de captura.

**Nome e descrição de produto são outra coisa: são texto do restaurante.** Quem
escreve a versão em inglês de `BATATA FRITA COM CHEDDAR E BACON` é o dono da
loja, não o sistema — então escrever `CHEDDAR & BACON FRIES` para o exemplo não
inventa nada sobre o produto, desde que o carrossel não insinue tradução
automática. A primeira versão deste carrossel errou pelo excesso de zelo: ficou
com o cardápio meio em português para não "inventar tradução", e a arte ficou
pobre justamente no slide que vendia o recurso. A tradução do exemplo mora em
`traducoes.json`, na pasta do carrossel, e é a **mesma** em toda a peça — tela,
print do cadastro e legenda.

Dois preenchimentos que salvam tela desenhada sem inventar nada:

- **preço.** Ele não muda de idioma (o manual diz), então entra em todo cartão e
  enche o vazio com um detalhe verdadeiro.
- **foto real recortada do print.** É o que enche tela sem afirmar nada e o que
  mais separa desenho convincente de wireframe. Retângulo com gradiente no lugar
  da foto (`.tela-tablet__capa`, que existia aqui) entrega o desenho na hora.
- **lista cortada pela barra fixa do pé.** No aparelho a lista rola; no desenho,
  um contêiner com `overflow: hidden` e a barra depois dele reproduz isso e
  resolve o vão de 200 px que sobrava embaixo do último cartão.

Cupom desenhado em CSS (`.cupom`) não precisa de selo: bobina térmica em
monoespaçada é claramente desenho, e é a única forma de mostrar o "antes" — que
não existe como captura.

## Onde a tela mora

| Tela | Como capturar |
|------|---------------|
| painel web (`beefood.app`) | `capturar.py --rota /cardapio` |
| cardápio digital público | `capturar.py --url <link> --publico --dispositivo celular` |
| **totem de autoatendimento** | é **web**: `totem.beefood.app/?empresaID=&filialID=&token=`. Roda aqui, e é captura de verdade. Veja *O totem é web* |
| app Android (Garçom, Entregador, Tablet) | não roda aqui. Nesta ordem: procure o print de produção no manual da mesma novidade (`git fetch origin main` antes de concluir que não existe); senão peça ao dono (zip em URL pública, seção 6 da `MEMORIA-GERAL.md`); senão ilustre com selo |
| coisa que não é tela (cupom, impressora) | print do manual, se existir; senão desenho em CSS |

### O totem é web, e a tela do cliente pode ser captura

Este é o erro mais caro desta memória, e ficou aqui escrito por duas rodadas: eu
tratei o totem como app Android e desenhei a tela dele em CSS. O Totem de
Autoatendimento é uma **página web**, com URL de sessão:

```
https://totem.beefood.app/?empresaID=<id>&filialID=<id>&token=<uuid>
```

Ela abre no Playwright como qualquer outra. Antes de desenhar tela de aplicativo,
**pergunte ao dono se aquele aplicativo tem URL** — o de tablet não tem, o de
totem tem, e a diferença é um carrossel inteiro de credibilidade.

**Quando o recurso não está ligado na loja de exemplo, ligue na resposta da
API.** O totem de exemplo não tinha tradução cadastrada (`aaTraducao: null`,
`traducao: null` em todos os produtos), e pedir cadastro na loja de um cliente
não é opção. O `capturar-totem.py` intercepta as rotas do totem e devolve o
mesmo JSON com o que falta:

| Rota | O que a interceptação faz |
|---|---|
| `/api/totem2/filial/**` | liga `aaTraducao: true`, que é o que faz o seletor de bandeiras aparecer |
| `/api/totem2/setores/**` | escreve o campo `traducao` de cada setor |
| `/api/totem2/produtos/**` | escreve o `traducao` do produto e também dos `gruposList` e das `opc`, senão o detalhe do produto abre metade em português |
| `/api/totem2/imagens/**` | troca a arte de fundo da loja (`AASLIDE`, `AACAPA`) pela nossa; o logotipo (`AALOGO`) continua o dela |

O que sai disso **não é montagem**: é o aplicativo de produção renderizando, com
a fonte, o layout, as fotos e as animações dele. O que veio de fora é só o texto
que o restaurante escreveria. Três cuidados:

- **não finalize pedido.** Navegar e fotografar não gera venda; concluir gera. O
  dono avisou, e o script para no cardápio e no detalhe do produto.
- **capture na resolução em que o mockup vai usar.** O aplicativo desenha botão e
  bandeiras em px fixo: na captura de 1080×1920 reduzida para 384 px de mockup, a
  pílula de bandeiras vira um risco. A mesma tela capturada em 720×1280 tem os
  mesmos elementos proporcionalmente maiores e sobrevive à redução. Captura
  grande não é sempre melhor.
- **clique setor por índice, não por texto.** O nome muda com o idioma. Filtre os
  botões pela caixa (`r.left < 5 && r.width < 300 && r.height > 100`) e guarde o
  índice; e reclique o setor depois de cada troca de idioma, porque a troca
  volta a rolagem para o topo.
- **recorte de pedaço de tela sai do `screenshot(clip=…)`, com a caixa medida no
  DOM.** É como nasce o par `FRENCH FRIES` / `PAPAS FRITAS` do slide de espanhol:
  mesma caixa nos dois idiomas, então o leitor compara o mesmo cartão em vez de
  duas fotos parecidas. Detalhes em *quando a prova cabe na imagem*.

As **fotos dos produtos** vêm do `s3Link` da própria API (`pagina.request.get`),
em WEBP — converta com Pillow antes de usar no slide. Foto real na tela desenhada
é o detalhe que mais separa desenho convincente de wireframe.

### A promoção da loja de exemplo não pode virar o assunto da arte

O totem de exemplo é de um cliente de verdade, e a arte de espera dele era um
cartaz de **"Pudim R$ 16,90"**. Nos primeiros renders isso passou batido, e o
dono pegou na hora: a capa era sobre cardápio em inglês e a única coisa que se
lia na tela era o preço de um pudim. Arte de campanha de uma loja específica
**rouba o assunto** e ainda amarra o post àquela promoção.

A saída é tratar o fundo como material de arte nosso: o `preparar-fundo.py` tira
um quadro de um vídeo de comida (o dono mandou o link), recorta em 9/16 para a
tela de espera e numa faixa larga para o banner do cardápio, e a mesma
interceptação que injeta a tradução injeta as duas imagens. Duas medidas do
ofício:

- **o véu escuro não é estética, é contraste.** O aplicativo desenha o botão
  vermelho e a pílula de bandeiras por cima da foto, e vermelho sobre batata
  dourada some. A faixa do meio da imagem (onde o botão cai) é a que mais
  escurece; o topo e a base ficam quase limpos, e a comida continua apetitosa.
- **recorte de vídeo em pé para faixa larga precisa de foco alto.** Centralizado,
  o corte sai no meio da massa de comida e vira mancha laranja; em 34% da altura
  entra a ponta das batatas com a fumaça atrás, e a faixa lê como foto.

**E a armadilha que custou uma captura inteira:** o totem é PWA, e as imagens
passam pelo *service worker* dele. `page.route` não enxerga esse pedido — a
interceptação "funciona", o JSON sai trocado e a imagem chega quebrada, preta na
tela. O contexto tem de nascer com `service_workers="block"` e as rotas têm de
ser do **contexto**, não da página. Vale para qualquer aplicativo BeeFood que
instale worker.

### Print do produto certo: às vezes é mais rápido cadastrar

O slide do cadastro mostrava a Coca Cola, o único produto do sandbox com
tradução — e o resto do carrossel mostrava hambúrguer e porção. O dono pediu
*"outros produtos que fazem mais sentido do que uma coca cola"*, e a saída não
foi mudar o print: foi **cadastrar a tradução no produto certo** (a mesma que
está no `traducoes.json`) e fotografar aquele. Sandbox é para isso, e escrever
nele é mais barato que reescrever o carrossel em volta do print que existe.

Ganho de graça: o slide do totem mostra `CHEDDAR & BACON FRIES` na tela do
cliente e o slide do cadastro mostra o campo onde aquele texto foi escrito. O
mesmo produto nos dois lados é o que faz o carrossel fechar.

### Quando o recurso é a mídia que o lojista sobe

Capas e destaques em vídeo é um caso novo: **não existe captura do recurso**. O
cardápio modelo está vazio, e o cardápio de produção tem a campanha de um
cliente — que, como já se aprendeu com o pudim do totem, vira o assunto da arte.

A saída foi montar um **estúdio**: as artes são nossas (`assets/midia/artes/`,
renderizadas pelo `fazer-midia.py`), os vídeos são MP4 gerados no FFmpeg, e o
`capturar-cardapio.py` entrega tudo isso ao cardápio público na resposta do
`validaDelivery`. Quem renderiza continua sendo o aplicativo de produção: o
carrossel inteiro é captura, e o que veio de fora é só o conteúdo que o lojista
subiria. O passo a passo está em [`mockups.md`](mockups.md).

Duas lições que mudam o jeito de desenhar a arte:

- **a arte é da loja, não da BeeFood.** O `arte.css` tem a paleta da
  hamburgueria do cardápio modelo. Banner no vermelho da marca dentro do
  cardápio de um cliente lê como anúncio nosso na casa dele.
- **meça o vão antes de desenhar.** O cardápio corta com `object-fit: cover`:
  ~4,1/1 no computador e ~2,6/1 no celular. A primeira rodada saiu em 16/9 e o
  aplicativo comeu o selo e o preço. Em 1920×580 (3,3/1), com 14% de margem
  segura, o texto sobrevive aos dois cortes — e o texto fica na faixa de cima,
  porque embaixo o aplicativo desenha o logotipo da loja.

### Slide em vídeo: quando a novidade é movimento, a capa parada custa caro

O carrossel do Instagram aceita vídeo no lugar de uma imagem, e este foi o
primeiro post em que isso valeu a pena: a novidade **é** a capa que se mexe, e
um PNG do notebook pedia que o leitor acreditasse na palavra "vídeo".

O `filmar-slide.py` não inventa um segundo slide: ele mede no DOM a caixa da
tela do mockup, fotografa o cardápio quadro a quadro e costura o filme por cima
do PNG que já foi aprovado. Arte e vídeo saem do mesmo arquivo, então revisar um
é revisar o outro.

Duas coisas que só aparecem quando se tenta:

- **gravação de tela não serve.** Chromium headless grava com taxa irregular, e
  o zoom lento do banner sai aos trancos. Quadro a quadro, com o `currentTime`
  avançado na mão, cada quadro é determinístico.
- **desligue os temporizadores da página antes de filmar.** Cada quadro custa
  quase um segundo de relógio real: 6 s de filme levam mais de um minuto, e
  nesse tempo o carrossel do cardápio troca de mídia sozinho várias vezes. No
  filme isso sai como banner piscando. Derrubar os `setTimeout` e `setInterval`
  pendentes congela o carrossel e não atrapalha o vídeo, que não depende deles.
- **filme a 25 quadros por segundo, mesmo doendo no relógio.** A primeira versão
  saiu a 12: o H.264 fecha em 25 fps de qualquer modo, e o FFmpeg completa
  repetindo quadro — metade do filme é quadro parado, o zoom anda aos pares e
  quem assiste descreve "trepidação" ou "salto", não avanço de lente. A 25 a
  captura leva 2,5 min e os 150 quadros andam todos. Para conferir sem depender
  de olho: `crop` na caixa da tela e diferença média entre quadros vizinhos
  (em 12 fps, um a cada dois dá zero), ou empilhe uma linha de cada quadro num
  slit-scan — movimento contínuo vira diagonal lisa, quadro repetido vira
  degrau.

### A arte não pode desmentir a frase do slide

O slide 6 dizia "combo de quarta aparece só na quarta" e mostrava, logo abaixo,
o recorte do painel do manual com **os sete dias acesos**. Nenhuma revisão de
texto pega isso: a frase está certa, o print é de verdade, e mesmo assim a arte
diz o contrário do título.

Print de manual é print de manual: ele foi tirado para mostrar a tela, não para
sustentar o seu argumento. Quando o slide afirma um estado da interface,
**fotografe aquele estado**. No sandbox isso custou um script curto que abre o
modal, apaga seis dias, fotografa a linha e **fecha descartando** — o sandbox
fica como o manual deixou.

Vale como pergunta de revisão: *a imagem deste slide prova o título, ou só
ilustra o assunto dele?*

## A prateleira: o que nasce no carrossel e sobe para a skill

O tablet custou cinco rodadas e o totem três. Nada disso era CSS difícil — era
**referência que não tínhamos juntado ainda**. O risco, depois de entregue, é o
carrossel seguinte começar do zero outra vez: as fotos de produto ficaram dentro
de `carrosseis/traducao-cardapio-presencial/imagens-puras/`, o capturador do
totem era um script daquela pasta, e o aparelho pronto só aparecia para quem
abrisse os slides de lá.

Então a regra virou: **o que serve para o próximo carrossel não mora dentro de
um carrossel.** Depois de entregar, o material geral sobe para a skill.

| Subiu | Para onde | Por que |
|---|---|---|
| 12 fotos de produto, tela de espera do totem (pt e en), banner do cardápio | `assets/fotos/` | conteúdo de cardápio serve a qualquer peça; capturar de novo custa dois minutos de Playwright e uma rodada de conferência |
| as duas artes de fundo do totem | `assets/fundos/` | entram na captura, não no slide |
| `capturar-totem.py`, `preparar-fundo.py` | `scripts/` | viraram genéricos por argumento (`--saida`, `--conteudo`, `--video`) |
| o cardápio de exemplo dentro da tela desenhada | `assets/slides/mockup-{totem,tablet}.html` | o modelo agora abre pronto: troca-se o texto do slide, não o aparelho |
| as artes de banner e cartaz, com os MP4 | `assets/midia/` | o próximo carrossel de cardápio digital já nasce com mídia de exemplo pronta |
| `fazer-midia.py`, `capturar-cardapio.py` | `scripts/` | um faz a arte e o vídeo; o outro entrega tudo ao cardápio público e fotografa |
| `filmar-slide.py` | `scripts/` | põe o filme dentro da tela do mockup, a partir do mesmo slide e do mesmo PNG |

Ficou no carrossel o que é **prova dele**: modal do painel, cupom daquele pedido,
tela do cadastro, recorte de cartão nos dois idiomas, e o `midias.json` que diz
qual arte entra em qual lugar.

### O prefixo `skill:`

Biblioteca compartilhada não combina com caminho relativo. O slide fica em
`carrosseis/<slug>/slides/`, e apontar para `../../../.cursor/skills/...` é
frágil e ilegível; copiar a foto para dentro de cada carrossel devolve o problema
que a biblioteca resolve. Então o `renderizar.py` passou a trocar `skill:` pelo
caminho de `assets/` da skill:

```html
<img src="skill:fotos/foto-batata.png" alt="">
```

São duas linhas de código e um efeito grande: os **modelos** de `assets/slides/`
passaram a renderizar de qualquer pasta, porque as imagens deles não dependem
mais de estar dentro de um carrossel com os arquivos de nome certo.

A prova de que a mudança não mexeu na arte: mover as 15 imagens, reescrever os
`src` e renderizar de novo deu PNG **byte a byte igual** ao entregue. Refatoração
de arte sem essa conferência é aposta.

### O catálogo de aparelhos, e por que ele é imagem e não texto

O `base.css` sabe desenhar cinco aparelhos, cada um com largura certa e com duas
ou três telas possíveis. Isso estava escrito — e escolher aparelho lendo texto
custa uma rodada de render para descobrir que não era aquele.

O `catalogo.py` fotografa cada peça em `assets/catalogo/` e monta uma folha com
todas, e cada aparelho aparece em dois estados:

- **só a carcaça**, com a tela listrada: é o que mostra se o desenho lê como
  aparelho. O tablet leu como monitor de mesa em três rodadas, e é neste estado
  que isso aparece na hora.
- **com tela**, que é captura de verdade quando ela se lê reduzida
  (`totem-com-captura`) e tela desenhada quando não (`totem-com-cardapio`,
  `tablet-com-cardapio`).

Rodar o script depois de mexer no `base.css` é obrigatório: a folha é o teste de
regressão da arte. E ele revelou peça esquecida — a `.tela-totem--espera` existia
no CSS e nenhum slide usava, então ninguém sabia que ela estava disponível.

## Reaproveitamento do manual

O slide pode apontar direto para o print do manual
(`../../../manuais/<manual>/imagens-puras/<arquivo>.png`). Foi assim com o
cupom do #99: é o mesmo cupom, e duplicar o arquivo criaria duas verdades.
Prints **puros**, nunca os tratados — os tratados têm setas numeradas, que são
linguagem de manual.

## Entrega: imagem, legenda e zip

PNG renderizado não é entrega. Quem publica precisa das **imagens uma por uma**,
da **legenda pronta para colar** e de **um arquivo só para baixar** — e isso
virou parte do fluxo (passo 7 da `SKILL.md`), não um favor no fim.

O `copy-instagram.txt` leva quatro blocos, e os dois últimos são os que a gente
esquecia:

1. cabeçalho com a novidade, o formato e **a ordem de publicação** (o nome do
   arquivo já ordena, mas escrever evita o carrossel postado fora de ordem);
2. a legenda, hashtags no fim;
3. um primeiro comentário com pergunta — opcional, é o que puxa resposta;
4. **texto alternativo por imagem**. Slide é imagem: sem isso o post inteiro é
   invisível para leitor de tela, e a informação já existe no `alt` dos slides.

Duas decisões que a primeira entrega ensinou:

- **A legenda não é a soma dos slides.** Ela é o mesmo assunto em prosa corrida,
  para quem leu a capa e desceu sem arrastar. O gancho da capa pode repetir (é o
  que amarra o post), o texto do release não — por isso o `conferir-texto.py`
  passou a medir o `copy-instagram.txt` junto com os slides, na mesma janela de
  seis palavras.
- **A legenda saiu do `roteiro.md`.** Enquanto morava lá, era rascunho perdido no
  meio das decisões de arte; quem publica abria o roteiro inteiro para achar o
  texto. Roteiro é auditoria, copy é entrega.

O `empacotar.py` monta `entrega/<slug>.zip` com os PNG e o `.txt` **soltos na
raiz do zip**, sem pasta intermediária: quem recebe arrasta o conteúdo direto
para o celular. A folha de contato fica fora de propósito — é ferramenta de
revisão, e no meio das oito imagens alguém posta a nona por engano. E cada membro
entra com data fixa, senão o zip muda de bytes a cada rodada só pela hora e o
diff do commit fica ilegível.

## Cuidados

- O `validar-imagens.py` da raiz varre **só** `manuais/`. Ele não enxerga
  `carrosseis/`, e não deve: carrossel não tem `imagens-tratadas/` nem
  `texto-documentation.ia.md`.
- `/tmp/beefood-estado.json` guarda a sessão do Playwright. Se alguma permissão
  do grupo de acesso mudou, apague o arquivo: o `config_cache` do front congela
  no estado antigo.
