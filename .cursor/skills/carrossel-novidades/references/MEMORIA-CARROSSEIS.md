# Memória dos carrosséis

Memória própria desta skill. Aprendizado de **captura genérica** do BeeFood
continua na `MEMORIA-GERAL.md`, escrita por quem trabalha nos manuais — aqui só
entra o que é de carrossel.

Última atualização: 2026-09-16 (9ª rodada: segundo carrossel, com mockup de
totem e de tablet desenhados do zero — e sete slides, porque a novidade tinha
sete slides de assunto).

## Índice

| Carrossel | Novidade | Pasta | Formato | Estado |
|-----------|----------|-------|---------|--------|
| Destaque na impressão | [15/09/2026](https://beefood.app/novidades/destaque-impressao) | `carrosseis/destaque-impressao/` | 4:5, 8 slides | ✅ entregue — `entrega/destaque-impressao.zip` (8 PNG + copy) |
| Cardápio presencial em inglês e espanhol | [16/09/2026](https://beefood.app/novidades/traducao-cardapio-presencial) | `carrosseis/traducao-cardapio-presencial/` | 4:5, 7 slides | ✅ entregue — `entrega/traducao-cardapio-presencial.zip` (7 PNG + copy) |

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
| totem, tela | escura, lista vertical | **clara**, coluna de setores em caixa alta, banner no topo, grade de produtos com foto, barra vermelha da sacola no pé |
| tablet, tela | clara, grade de dois cartões | **escura**, cartões deitados com foto à esquerda, preço em **amarelo**, botão `Order` |
| tablet, suporte | pedestal fino com pé chato | **chapa de alumínio curva** que sai de trás e dobra até a mesa |
| bandeiras | redondas nos dois | redondas no totem, **retangulares** no tablet |

### O que faz cada aparelho ler como o que é

| Aparelho | O que dá a leitura | O que errei primeiro |
|---|---|---|
| totem | carcaça **branca**, tela 9/16 com moldura preta fina, **painel** embaixo com leitor de aproximação, boca de impressora e **pinpad**, e coluna + base pretas mais estreitas que a carcaça | sem o painel, é um celular gigante numa coluna; o painel é o que diz "autoatendimento" |
| tablet | moldura **proporcional e igual nos quatro lados** (`padding: 2.2%`), canto **bem arredondado** (38 px), fio de alumínio em volta, dois botões na lateral direita, ponto de câmera na moldura da esquerda e a **chapa curva** atrás | moldura em px, canto de 20 px e pedestal com pé: sai um iMac |

O tablet custou quatro rodadas, e o que resolveu foi medir em vez de opinar:

- **moldura em px não escala.** O mockup nasceu com `padding: 11px`, que é 1,5%
  de uma largura de 720 e 1,2% de uma de 880: quanto maior o slide usa o
  aparelho, mais a moldura desaparece e mais ele vira monitor. Em `%` o `padding`
  mede a própria largura do elemento e a moldura acompanha.
- **o canto é o sinal mais forte.** 20 px de raio em 880 de largura é canto de
  monitor; 38 px já é tablet. Em px e não em `%`, que daria elipse.
- **4/3 pareceu "mais tablet" e não é.** Testei, encolhe a tela e inventa um
  aparelho que o cliente não tem — o aplicativo roda em tablet Android, 16/10,
  que é também a proporção do print de produção (1280×800).
- **o suporte não é um trapézio.** Duas tentativas com `clip-path` de trapézio
  saíram lendo "chapéu chinês" embaixo do aparelho. A peça real é uma chapa
  curva: vista de frente é quase um retângulo de cantos arredondados, com o
  volume vindo do gradiente (claro no meio, escuro nas beiradas) e a dobra do
  pé vindo de um `border-radius` assimétrico.

Medidas que cabem no slide, com o texto acima:

| Mockup | Largura | Altura até a base da carcaça | Onde |
|---|---|---|---|
| totem sozinho (capa) | 410 px | 802 px (tela 641 + painel 144 + topo 17) | `top: 522px`, centralizado, coluna sangrando pela base |
| totem ao lado de texto | 396 px | 775 px | `top: 462px`, `right: 46px` |
| totem pequeno, com outro aparelho | 322 px | 629 px | `top: 450px`, `right: 34px` |
| tablet inteiro | 880 px | 565 px + 81 px de suporte | `.figura`, centralizado |
| tablet ao lado de outro aparelho | 640 px | 410 px + 59 px de suporte | `top: 828px`, `left: 28px` |

**Aparelho em pé na capa pode sair pela base**, e é melhor que caber inteiro: a
borda de baixo do slide lê como chão. O que **não** pode sair é o painel do
pinpad, que é o que identifica o totem — corte a coluna, nunca o painel.

**Bandeira do seletor é emoji recortado em círculo** (`.bandeira`), não SVG novo
no repositório: o ambiente tem Noto Color Emoji, 🇧🇷 sai igual em toda máquina e
o `scale(1.5)` dentro do círculo é o que faz a tinta cobrir os cantos (a bandeira
emoji é ondulada e mais larga que alta). `.bandeira--anel` marca o idioma em uso,
como o sistema faz. No **tablet** elas são retangulares (`.bandeira--retangular`)
e empilhadas — dois aparelhos, dois desenhos. A **bolinha verde** de "esse idioma
já tem texto" não entrou no desenho de propósito: ela só existe no cadastro, e do
cadastro existe captura real.

### Duas armadilhas de CSS que custaram render

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
- as **fotos são as reais**, recortadas do print por um script na pasta do
  carrossel (`preparar-telas.py`), com as coordenadas **medidas no arquivo** com
  Pillow e comentadas no script. Foto de comida inventada é o que mais denuncia
  tela desenhada;
- pedaços que já vêm prontos entram inteiros. O banner do topo do totem é um
  recorte só, e traz o `CANCEL ORDER` e a pílula de bandeiras de produção
  dentro — é o pixel mais convincente do carrossel e não custou nada desenhar.

O selo continua: a tela é desenhada.

Três condições, todas obrigatórias:

1. o comportamento desenhado está escrito na novidade ou no manual;
2. o desenho usa o vocabulário do carrossel (cartão arredondado, Mulish, cor da
   marca) e **não** imita a interface real pixel a pixel;
3. o slide leva `.selo-ilustracao` — ilustração que passa por captura engana quem
   lê, e este repositório é público.

O selo mora na coluna vazia à esquerda do celular em sangria (`left: 88px`).
Colocado sobre o texto, ele foi lido como botão.

**Texto de tela em outro idioma só entra se estiver documentado.** É a condição 1
levada a sério no caso mais escorregadio. No carrossel da tradução, as telas
desenhadas de totem e tablet usam só o inglês que o manual escreve: `DRINKS`
(Bebidas traduzido), `Sides`, `Cola US`, `The drink cola`, `CANCEL ORDER`,
`SEARCH`, `MY CART`, `MY BILL`. Faltou um segundo produto em inglês para encher a
grade, e a tentação foi traduzir eu mesmo "Anéis de Cebola Empanada" — traduzir
no desenho é **inventar comportamento do produto** e some a diferença entre o que
o sistema entrega e o que eu achei bonito. A saída foi mostrar menos itens e
deixar os nomes em português onde não havia tradução documentada, que por sorte é
o comportamento real.

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
| app Android (Garçom, Entregador, Tablet, Totem) | não roda aqui. Nesta ordem: procure o print de produção no manual da mesma novidade (`git fetch origin main` antes de concluir que não existe); senão peça ao dono (zip em URL pública, seção 6 da `MEMORIA-GERAL.md`); senão ilustre com selo |
| coisa que não é tela (cupom, impressora) | print do manual, se existir; senão desenho em CSS |

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
