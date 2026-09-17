# Carrossel — Cardápio presencial em inglês e espanhol

- **Novidade:** [Cardápio presencial em inglês e espanhol](https://beefood.app/novidades/traducao-cardapio-presencial) — Novidade, Cardápio + Aplicativos
- **Manual:** [Tradução do cardápio presencial: inglês e espanhol](https://ajuda.beefood.com.br/cardapio-presencial-ingles-espanhol)
- **Formato:** 4:5 (1080×1350), **7 slides**
- **Pasta:** `carrosseis/traducao-cardapio-presencial/`

Sete slides, não oito: a novidade tem uma ideia grande (o cliente lê o cardápio
na língua dele) e três apoios (totem, tablet, e o fato de não existir um segundo
cardápio para manter). Esticar para oito pediria um slide de "onde ativar", que é
exatamente o que este carrossel não é.

## O que este carrossel **não** faz

O manual ensina a configurar; o carrossel divulga. Então ficam **fora**:

- caminho de menu para ligar a tradução no totem (`Aplicativos → Totem →
  Configuração → Idiomas`);
- o aviso de que o sistema não traduz sozinho;
- a lista de campos traduzíveis e a de campos que não mudam;
- a tabela de problemas comuns.

Nada disso é mentira — é material de manual. Quem quer o passo a passo clica no
link; quem está no feed quer saber **o que muda no salão**.

Um cuidado que isso obriga: o carrossel **nunca insinua tradução automática**.
Ele não diz "você traduz sozinho" e também não diz "o sistema traduz". Mostra o
cadastro onde a versão em inglês mora (slide 5) e trata o trabalho como coisa
tranquila e parcial (slide 6). Promessa de tradução automática voltaria como
reclamação.

## Fato → ângulo → o que o slide diz

| Fato (novidade/manual) | Ângulo | O que o slide diz | Slide |
|---|---|---|---|
| O cliente troca o idioma tocando numa bandeira, no Totem e no Cardápio Digital no Tablet; os idiomas são português, inglês e espanhol | o turista que entrou e não pediu é venda que já estava dentro da loja | "Seu cardápio já fala inglês?" | 1 |
| O turista encontra o cardápio todo em português e desiste de pedir | ninguém vai embora por causa do preço nessa cena; vai embora porque não entendeu | o que ele faz hoje: tradutor no celular, mímica, ou a porta | 2 |
| A tradução vale para setor, nome, descrição e grupos de opções; o cliente troca de idioma no meio do pedido sem perder o que montou | não é meia tradução: o cardápio muda inteiro, até o fim do pedido | "Ele toca na bandeira e o cardápio inteiro muda" | 3 |
| No tablet as bandeiras ficam na coluna da esquerda, sem configuração; os textos do app (SEARCH, MY CART, MY BILL) já vêm traduzidos | na mesa, quem resolve é o cliente — sem chamar ninguém | "No tablet é a mesma coisa" | 4 |
| Três bandeiras na linha do Nome; um único SALVAR E SAIR guarda português e as duas traduções | o medo é manter dois cardápios; não é isso que acontece | "A versão em inglês mora no mesmo produto" | 5 |
| Item sem tradução continua em português, nada fica em branco; a ordem sugerida começa pelos setores | o que travaria a adoção é achar que precisa traduzir tudo antes de ligar | "Não precisa traduzir tudo hoje" | 6 |
| As bandeiras aparecem para lojas com Totem de Autoatendimento ou Cardápio Digital no Tablet | quem já tem o equipamento não precisa comprar nada | "Tem totem ou tablet? Então as bandeiras já estão aí" | 7 |

## Slides

| # | Arquivo | Tipo | Ideia única | Imagem |
|---|---------|------|-------------|--------|
| 1 | `01-capa.html` | capa com imagem | o cardápio passou a falar a língua do cliente | totem com a tela de espera em inglês (captura real) e o tablet com o cardápio traduzido |
| 1 | `capa-alternativa/slides/01-capa-so-totem.html` | capa com imagem | idem, versão alternativa | só o totem, centralizado e grande, com a captura da tela de espera |
| 2 | `02-cena.html` | texto | o turista não vai embora por preço | — |
| 3 | `03-totem.html` | mockup reto + texto ao lado | o cardápio muda inteiro, não pela metade | cardápio do totem em inglês, com as porções e as fotos reais |
| 4 | `04-tablet.html` | mockup centralizado | na mesa as bandeiras já estão na lateral | tablet com três hambúrgueres descritos em inglês |
| 5 | `05-mesmo-cadastro.html` | print real em janela | a tradução mora no mesmo produto | captura da linha do Nome com a bandeira dos Estados Unidos escolhida e `CHEDDAR & BACON FRIES` no campo |
| 6 | `06-aos-poucos.html` | texto com lista | dá para traduzir aos poucos | — |
| 7 | `07-cta.html` | CTA com mockup | quem tem o equipamento já tem o recurso | página de novidades no celular, captura real |

Cinco dos sete slides têm imagem, e a capa é um deles.

## Decisões de roteiro

**A capa responde à própria pergunta.** "Seu cardápio já fala inglês?" só funciona
porque a imagem mostra um totem com o cardápio em inglês — a pergunta é retórica
e a resposta está na arte, não no texto. Sem a imagem, o dono lê "não" e passa. A
palavra em vermelho é **inglês**, uma só; o espanhol entra no subtítulo, que é
onde cabe a segunda informação.

**Qual tela vai na capa: a de espera, e a decisão inverteu.** A primeira versão
pôs o cardápio na capa porque a tela de espera *desenhada* tinha um gradiente no
miolo, e aquilo abria um vão morto de 300 px na imagem. Quando o totem passou a
ser captura de verdade, a tela de espera virou a melhor candidata: ela é quase
toda foto e botão, então sobrevive à redução para 384 px de mockup — e o botão
diz `START YOUR ORDER`, que responde a pergunta da capa em inglês, com as três
bandeiras logo abaixo. O cardápio foi para o slide 3, onde o mockup é maior e a
tela pode ser desenhada com a letra ampliada.

Regra que ficou: **tela cheia de texto fino vai no slide grande; tela de imagem e
botão vai na capa.** Não é sobre qual tela é mais bonita, é sobre qual aguenta
ser reduzida.

**O subtítulo da capa tem uma linha.** Vale registrar porque contraria a rodada
anterior, em que duas linhas ficaram melhores: lá a imagem era um cupom deitado,
aqui é um aparelho **em pé**, que come 830 px de altura. Com duas linhas de
subtítulo o totem começava dentro do texto. Imagem em pé na capa custa uma linha
de subtítulo.

**A composição da capa com dois aparelhos é um grupo, não duas ilhas.** A
primeira versão tinha o totem num canto e o tablet no outro, com um vão no meio
da base — e o dono devolveu como falta de harmonia. O que arrumou: o totem atrás
e à direita (`top: 366px`, `right: 48px`), o tablet à frente e à esquerda
(`top: 872px`, `left: 54px`, `z-index: 2`) encostando na coluna dele, e os dois
saindo pela borda de baixo, que lê como piso e mesa. O título perdeu largura
(`max-width: 570px`) para parar onde o totem começa.

**Um aparelho sobrepondo o outro é o que faz um grupo.** Enquanto as silhuetas
não se tocavam, qualquer ajuste de posição só mudava o tamanho do vão.

**O slide 2 não fala de sistema.** É a cena do salão inteira — tradutor no
celular, mímica, a porta. É o slide que faz o dono reconhecer o problema antes de
ouvir a solução, e o que segura a atenção até o terceiro. A caixa de fecho existe
para nomear o custo: não foi o preço, foi o cardápio.

**A primeira versão do totem e do tablet foi desenhada de memória, e saiu
errada.** Totem escuro com lista vertical, tablet claro com grade de cartões —
o dono devolveu como "fora do layout" e "foge totalmente do padrão", e tinha
razão nos dois. O que faltou foi procurar a referência antes de desenhar.

Ela existia em dois lugares:

- **os prints de produção**, que o próprio manual versiona em
  `manuais/traducao-cardapio-presencial/imagens-puras/` — tela de espera do
  totem (`07`), cardápio do totem em inglês (`08`) e cardápio do tablet em
  inglês (`09`). Não estavam no checkout local porque o manual entrou depois do
  build do ambiente; um `git fetch origin main` resolveu.
- **as fotos do catálogo**, em `beefood.com.br/totem-de-autoatendimento` e
  `beefood.com.br/cardapio-digital-tablet`, que mostram os aparelhos.

O que os prints corrigiram, e que nenhuma memória substitui:

| | desenhado de memória | como é |
|---|---|---|
| totem, carcaça | preta, canto de 28 px | **branca**, canto quase reto, painel com leitor, impressora e pinpad |
| totem, tela | escura, lista vertical de itens | banner no topo, coluna de setores em miniatura de foto e grade de produtos com foto (o tema é do estabelecimento: o print do manual é claro, o totem de exemplo é escuro) |
| tablet, tela | clara, grade de dois cartões | **escura**, cartões deitados, preço em amarelo, botão `Order` |
| tablet, suporte | pedestal fino com pé chato | **chapa de alumínio** larga que dobra até a mesa |
| bandeiras | redondas nos dois | redondas no totem, **retangulares** no tablet |

**E o totem não precisava ser desenhado: ele é web.** Descoberta da rodada
seguinte, e é a que mais mudou o carrossel. O Totem de Autoatendimento abre em
`totem.beefood.app/?empresaID=&filialID=&token=`, então roda no Playwright como
qualquer página — as telas de totem dos slides 1 e 3 são **captura de verdade**
do totem de exemplo, com fonte, layout e fotos de produção. Duas rodadas foram
gastas desenhando uma tela que dava para fotografar, e a pergunta que não foi
feita é simples: *esse aplicativo tem URL?*

**A loja de exemplo não tinha tradução, então a tradução entrou pela API.** O
`capturar-totem.py` intercepta as rotas do totem e devolve o mesmo JSON com
`aaTraducao: true` e com o campo `traducao` preenchido a partir do
[`traducoes.json`](traducoes.json) — setor, produto, e também os `gruposList` e
as `opc`, senão o detalhe do produto abre metade em português. O aplicativo
renderiza o resto. Pedir cadastro na loja de um cliente não era opção, e
finalizar pedido lá também não: o script só navega e fotografa.

A tradução é minha, e isso é honesto: quem escreve a versão em inglês do cardápio
é o dono da loja, não o sistema. O que **não** pode ser inventado é texto de
interface (`SEARCH`, `MY CART`, `Order`, `Your bag is empty`) — esse veio da
própria tela. E `PISCININHA`, `SMASH 2.0`, `ONE BURGER` ficaram como estão: nome
próprio de produto não se traduz, e é o que um restaurante faz de verdade.

**A tela do slide 3 continua desenhada, e continua com selo.** O cardápio do
totem tem cartão pequeno e preço miúdo: a captura reduzida para 420 px de mockup
fica com letra de 5 px no feed. Então o CSS copia o layout e a paleta da captura,
com a letra ampliada e a grade em duas colunas em vez de três, e usa as **fotos
reais** — baixadas do `s3Link` da própria API — mais o banner do topo, que é um
recorte da captura e vem com o `CANCEL ORDER` e a pílula de bandeiras dentro.

Três medidas foram para o `base.css` depois da conferência no PNG:

- **coluna de setores em 22-24%.** Em 21% o nome longo quebrava em seis linhas no
  totem pequeno, e a coluna lia como layout estourado.
- **moldura do tablet em 4,4%** e suporte em chapa única. A moldura fina e o
  pedestal com base faziam o tablet ler como monitor — e havia dois blocos
  `.tablet` no CSS, com o antigo ganhando por ordem de cascata.
- **chapa do suporte em 58% da largura.** Com 46% ela continuava lendo como pé de
  monitor, de pequena; na foto do catálogo a chapa ocupa dois terços da largura
  do aparelho.

O `font-size` das telas desenhadas não é gosto: 19 px no totem é o maior valor em
que os quatro cartões cabem inteiros antes da barra da sacola, e 16 px no tablet
é o maior em que os três itens mantêm o preço visível. Corte em cima de número lê
como falha de render.

**O print do cadastro é o slide mais importante dos apoios.** O slide 5 responde
ao medo que mata a adoção — "vou ter que manter dois cardápios" — e a resposta só
convence vendo: é a linha do Nome com a bandeira dos Estados Unidos escolhida e
`CHEDDAR & BACON FRIES` dentro do mesmo campo.

O produto mudou nesta rodada, e por um motivo que vale registrar: o sandbox só
tinha tradução na Coca Cola, e o dono pediu exemplos que fizessem mais sentido
que refrigerante. Em vez de fotografar o produto errado, **cadastrei a tradução
no produto certo** (`gravar_traducao` no `capturar-telas.py`) — a mesma que está
no `traducoes.json`. Assim o slide 3 mostra `CHEDDAR & BACON FRIES` na tela do
cliente e o slide 5 mostra o campo onde aquele texto foi escrito. Sandbox é para
isso.

**O que saiu da copy: microdetalhe e diminutivo.** Os slides 5 e 6 explicavam a
bolinha verde e a herança do grupo de opções — o dono devolveu como *"exatamente
o tipo de explicação desnecessária, isso não agrega em nada"*, e tinha razão: é
material de manual. No lugar entrou a consequência ("mudou o preço, acabou o
estoque? você mexe num lugar só") e o alívio ("o resto, quando der"). Os
diminutivos saíram junto: "bandeirinha" virou "bandeira". As duas regras estão
na `MEMORIA-CARROSSEIS.md` e na `SKILL.md`.

**Nenhum slide em 3D.** O slide 3 chegou a sair girado — ele é o único em que o
aparelho divide a faixa com uma coluna de texto, que era a condição para girar.
Mas o aparelho ali é um **totem**, e totem girado lê como armário tombando: o
que o 3D valoriza é a espessura da peça, e um armário em pé não tem espessura
para mostrar. A regra ficou mais estreita e está na `MEMORIA-CARROSSEIS.md`: 3D
só em **celular e em janela de computador**. Totem e tablet vão retos.

**Duas capas, e a escolha é de quem publica.** `01-capa.html` traz o totem e o
tablet juntos: a capa já diz "nos dois aparelhos" sem gastar linha de texto, e o
preço é cada tela ficar menor. `capa-alternativa/slides/01-capa-so-totem.html`
traz o totem sozinho, centralizado e grande: o `START YOUR ORDER` e as três
bandeiras ficam bem legíveis no feed. A alternativa mora em pasta
separada porque o `renderizar.py` transforma em PNG todo `.html` de `slides/`, e
duas capas na mesma pasta virariam um carrossel de oito imagens com dois
slides "1 de 7".

**A data no print do CTA fica.** O celular do slide 7 mostra a página de
novidades, e nela aparece "16/09/2026" — data que o site publica, dentro de um
print de verdade. É o caso que a memória abre ("Nada de data na arte"): a arte
não tem data, e essa é da página fotografada. Mesmo print do CTA do carrossel
anterior.

**Emoji em dois dos sete.** 🇺🇸 no slide 4 e 🌎 no 7, e a capa sem nenhum — ela já
tem a palavra em vermelho. Os dois são o assunto do post, então informam em vez
de enfeitar; nos slides de texto puro (2, 5 e 6) não entra nenhum, porque ali o
emoji só apareceria para animar parágrafo. As bandeiras **dentro** dos mockups
não são emoji soltos: são o emoji recortado em círculo (`.bandeira`), do jeito
que o sistema desenha o seletor.

**Duas frases voltaram do `conferir-texto.py`.** A bolinha verde ("então dá para
ver num relance o que falta") e o grupo de opções ("atende todos os produtos que
o usam") tinham saído iguais à novidade, palavra por palavra, sem que eu
percebesse — são as frases boas do release, e é justamente por serem boas que a
mão as copia. As duas acabaram cortadas por outro motivo na rodada seguinte:
eram explicação de microdetalhe.

## Capturas

```bash
python carrosseis/traducao-cardapio-presencial/capturar-telas.py
```

O script faz duas coisas, na ordem: **grava** a tradução de inglês e de espanhol
no produto do sandbox (`Batata frita com cheddar e bacon`, do setor
Acompanhamentos) e depois **fotografa** a linha do Nome com o inglês escolhido.
A tradução é a mesma do `traducoes.json`.

Sai em `imagens-puras/`:

- `05-cadastro-ingles.png` — a linha do Nome com as três bandeiras, a etiqueta
  `Inglês` e `CHEDDAR & BACON FRIES` no campo. É o recorte do slide 5.
- `07-novidades-celular.png` — a página de novidades no celular, para o CTA.

O sandbox **tem** o recurso: a empresa de teste tem Cardápio Digital no Tablet,
então as bandeiras aparecem no cadastro. Se um dia desaparecerem, é contrato, não
bug (o manual diz que sem Totem nem Tablet não há bandeira).

### As telas do cliente: o totem é web

```bash
python carrosseis/traducao-cardapio-presencial/capturar-totem.py
```

Abre o totem de exemplo (`totem.beefood.app`, ONE Stand, empresaID 350 /
filialID 380), liga a tradução na resposta da API, injeta o `traducoes.json` e
captura. **Nenhum pedido é finalizado.** Sai em `imagens-puras/`:

- `totem-espera-en-720.png` — a tela de espera em inglês, com `START YOUR ORDER`
  e as três bandeiras. É a tela das duas capas. Em 720×1280 e não em 1080p de
  propósito: o aplicativo desenha botão e bandeira em px fixo, e na captura
  grande reduzida para o mockup a pílula de bandeiras virava um risco;
- `totem-espera-idioma.png`, `totem-menu-pt|en|es.png`, `totem-produto-en.png` —
  as telas em resolução cheia, para conferência do que o aplicativo faz com cada
  idioma;
- `totem-banner-en.png` — o banner do topo, que entra na tela desenhada do
  slide 3;
- `foto-*.png` — as fotos dos produtos, baixadas do `s3Link` da API e convertidas
  de WEBP para PNG.

Os prints `manual-07|08|09` continuam na pasta: foram a referência do redesenho
do totem e do tablet, e o `09` ainda é a referência da tela do tablet, que não
tem URL para capturar. O `preparar-telas.py`, que recortava foto de bebida
daqueles prints, saiu do repositório junto com os recortes dele: as fotos passaram
a vir da API, e script sem uso é armadilha para a próxima rodada.

## Render e entrega

```bash
python .cursor/skills/carrossel-novidades/scripts/renderizar.py \
    carrosseis/traducao-cardapio-presencial --contato
python .cursor/skills/carrossel-novidades/scripts/renderizar.py \
    carrosseis/traducao-cardapio-presencial/capa-alternativa
python .cursor/skills/carrossel-novidades/scripts/conferir-texto.py traducao-cardapio-presencial
python .cursor/skills/carrossel-novidades/scripts/empacotar.py traducao-cardapio-presencial
```

A legenda, o primeiro comentário e o texto alternativo de cada imagem estão em
[`copy-instagram.txt`](copy-instagram.txt). O que vai para quem publica é
`entrega/traducao-cardapio-presencial.zip`.
