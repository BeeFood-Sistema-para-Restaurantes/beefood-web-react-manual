---
name: carrossel-novidades
description: Produz carrossel de Instagram (prints reais, mockups e slides em PNG 1080x1350) sobre uma novidade publicada em beefood.app/novidades ou sobre um tema do sistema BeeFood. Use quando o pedido falar de carrossel, post, arte, slides, divulgação ou comunicação de novidade. Não use para escrever manual de usuário — manual tem fluxo próprio na MEMORIA-GERAL.md.
---

# Carrossel de novidades do BeeFood

Transforma uma novidade do sistema em **publicação** para o Instagram: texto
escrito a partir do fato (não recortado do release), prints reais do produto em
mockup de celular e de computador, e slides exportados no tamanho exato do feed.

## Quando usar, e quando não

| Pedido | Onde ele é atendido |
|--------|---------------------|
| "faz um carrossel da novidade X", "post sobre o KDS", "arte para o Instagram" | **aqui** |
| "cria o manual de X", "documenta a tela Y", "atualiza o manual Z" | `MEMORIA-GERAL.md` + `manuais/` — **não é esta skill** |
| "carrossel do tema X" (sem novidade publicada) | aqui; a pauta vem do manual ou do tema, não do feed |

Esta skill **não altera** `MEMORIA-GERAL.md`, `CHECKLIST-MANUAIS.md` nem nada
dentro de `manuais/`. Ela lê esse material e escreve só em `carrosseis/` e na
própria pasta da skill. O manual continua com o foco dele: passo a passo com
setas numeradas para o usuário final.

## Conhecimento que vem do manual (leia antes de capturar)

Captura de tela do BeeFood já está resolvida pelos manuais. Não reinvente:
leia [`references/conhecimento-compartilhado.md`](references/conhecimento-compartilhado.md),
que mapeia exatamente quais seções da `MEMORIA-GERAL.md` abrir e por quê.
O resumo curto: **espere o spinner sumir e mais 5 segundos antes de cada print**,
use a conta sandbox, tema claro, e cubra dado pessoal na imagem pura.

Se a novidade tem manual, o manual é a fonte de verdade do comportamento — ele
foi conferido no sistema. O `pauta.py` aponta o manual correspondente sozinho.

## Fluxo

### 1. Pauta

```bash
python .cursor/skills/carrossel-novidades/scripts/pauta.py
python .cursor/skills/carrossel-novidades/scripts/pauta.py --slug <slug>
```

Lê o RSS de `beefood.app/novidades` (título, data, tipo, áreas, texto completo)
e indica o manual relacionado, com a contagem de capturas que já existem lá.

### 2. Roteiro — antes de qualquer imagem

**O texto da novidade é matéria-prima, não roteiro.** Ele é registro de release:
descreve o campo, a tela e o efeito na ordem em que o produto foi construído.
Recortar aquele parágrafo em oito pedaços e centralizar cada pedaço num slide
produz um changelog paginado, que ninguém arrasta. O carrossel é uma **publicação
nova, escrita a partir do fato**:

1. **fato** — o que mudou, onde fica, o que passa a acontecer, qual o limite;
   em três linhas, sem adjetivo, tirado da novidade e do manual;
2. **ângulo** — qual cena reconhecível do restaurante esse fato toca;
3. **texto** — escrito da cena para a tela. Nenhuma frase pode aparecer igual à
   da novidade; se apareceu, foi copiada.

Crie `carrosseis/<slug>/roteiro.md` com a tabela **fato → ângulo → o que o slide
diz** (é o que permite auditar que nada foi inventado e nada foi copiado) e a
tabela de slides (arquivo, tipo, ideia única, imagem). A legenda não fica aqui:
ela é peça de entrega e mora em `copy-instagram.txt` (passo 7).
Método completo em [`references/roteiro-e-copy.md`](references/roteiro-e-copy.md).

Roteiro aprovado primeiro; captura depois. Print tirado antes do roteiro quase
sempre é print que não entra.

### 3. Capturas

Primeiro decida **onde a tela mora** — é isso que define se existe captura:

| Tela | O que fazer |
|------|-------------|
| painel web (`beefood.app`) | `capturar.py --rota /cardapio` |
| cardápio digital público | `capturar.py --url <link> --publico --dispositivo celular` |
| cardápio digital com mídia nossa dentro | `capturar-cardapio.py --conteudo midias.json` (banner, vídeo e cartaz de aviso entregues na resposta da API) |
| Totem de Autoatendimento | é **web**, e já tem script pronto: `capturar-totem.py` (telas, tradução injetada, fotos de produto). **Não finalize pedido** |
| app Android (Garçom, Entregador, Tablet) | não roda no Cloud Agent: **peça o print ao dono** (zip em URL pública, seção 6 da `MEMORIA-GERAL.md`) e, enquanto ele não vem, desenhe a tela em CSS copiando o print de produção (passo 4) |
| cupom impresso | `ganchar_cupom` + `salvar_cupom`: o cupom nasce num iframe que vai para a impressora, então não dá para fotografar a tela |
| coisa que não é tela (impressora, balança) | print do manual, se existir; senão desenho em CSS |

**Print do manual que não serve, você refaz — não desenha.** O cupom do manual
*Destaque na impressão* sai com duas linhas em preto porque o manual precisava
mostrar que complemento também destaca; a capa do carrossel precisava de uma.
A saída foi montar no sandbox um pedido com só a bebida marcada e imprimir o
cupom dele (`registrar_pedido` no `capturar-telas.py` do carrossel). Continua
sendo impressão de verdade. Separe **registrar** de **imprimir**: registrar cria
venda no sandbox, reimprimir não cria nada, e a arte pode ser refeita à vontade.

**Sandbox sem o dado que o slide precisa: cadastre o dado.** O único produto com
tradução no sandbox era um refrigerante, e o carrossel mostrava hambúrguer e
porção — fotografar o produto errado sai mais caro que escrever a tradução no
produto certo (`gravar_traducao` no `capturar-telas.py` do carrossel da
tradução). Vale para o que o slide mostra; para **ligar recurso na loja de
exemplo de um cliente**, não: aí a saída é interceptar a resposta da API.

**Recurso desligado na loja de exemplo se liga na resposta da API.** O totem de
exemplo não tinha tradução cadastrada, então o `capturar-totem.py` intercepta
`/api/totem2/filial|setores|produtos`, devolve o mesmo JSON com `aaTraducao:
true` e com o campo `traducao` preenchido a partir de um `traducoes.json` da
pasta, e o **aplicativo de produção renderiza**. O que veio de fora é só o texto
que o restaurante escreveria. O script está pronto e é de uso geral; as
armadilhas (resolução, setor por índice, service worker, setor de combo) estão
em [`references/mockups.md`](references/mockups.md).

**Quando o recurso é a mídia que o lojista sobe, você faz a mídia.** Capa e
vitrine em vídeo não têm captura: o cardápio modelo está vazio e o de produção
tem a campanha de um cliente. O `fazer-midia.py` renderiza as artes de
`assets/midia/artes/` e gera os MP4 (6 s, H.264, mudos); o `capturar-cardapio.py`
entrega tudo ao cardápio público na resposta do `validaDelivery` e fotografa o
aplicativo de verdade renderizando. A arte usa a **paleta da loja**, não a da
BeeFood, e o formato é **1920×580** com 14% de margem segura — o cardápio corta
com `object-fit: cover` (~4,1/1 no computador, ~2,6/1 no celular). Detalhes em
[`references/mockups.md`](references/mockups.md).

**A campanha da loja de exemplo não pode virar o assunto da arte.** O totem de
exemplo anunciava "Pudim R$ 16,90" na tela de espera, e numa capa sobre cardápio
em inglês o olho lia o preço do pudim. A mesma interceptação troca a arte de
fundo por uma foto nossa, que o `preparar-fundo.py` tira de um vídeo de comida —
as duas prontas estão em `assets/fundos/`. O logotipo da loja continua o dela.

Tela que abre direto numa rota:

```bash
python .cursor/skills/carrossel-novidades/scripts/capturar.py <slug> \
    --rota /cardapio --nome 02-produtos
python .cursor/skills/carrossel-novidades/scripts/capturar.py <slug> \
    --url https://beefood.app/novidades --nome 01-pagina --publico
python .cursor/skills/carrossel-novidades/scripts/capturar.py <slug> \
    --rota /cardapio-digital --nome 04-menu --dispositivo celular
```

Tela que exige clique: escreva `carrosseis/<slug>/capturar-telas.py` importando
`sessao`, `esperar` e `limpar` do `capturar.py` — mesmo padrão dos manuais, que
têm um script por pasta. Veja
[`carrosseis/destaque-impressao/capturar-telas.py`](../../../carrosseis/destaque-impressao/capturar-telas.py).

**Recorte é obrigatório em tela de painel.** Um modal inteiro reduzido para a
largura do slide fica ilegível no feed. O teto depende de como o slide exibe o
recorte:

| Exibição | Recorte máximo (largura lógica) |
|----------|--------------------------------|
| `.navegador` / `.recorte` dentro da margem | ~440 px (faixa de um campo) |
| `.sangria--janela` (1120 px, sangrando pela direita) | ~620 px (meia tela) |

Prefira fechar a borda do recorte em área vazia — corte no meio de uma palavra
parece defeito. O viewport de captura é **1440×900 com DPR 2**, então a fração
que você passa em `--recorte` vira pixels sobre 900 de altura, não sobre 1350:
confira a medida do arquivo com Pillow antes de calcular porcentagem de realce.

Capturas já existentes em `manuais/` podem ser **referenciadas** de dentro do
slide (`../../../manuais/<manual>/imagens-puras/<arquivo>.png`). Não copie: o
print do manual é o mesmo print, e duplicar cria duas verdades.

**Mas print de manual não sustenta afirmação de slide.** Ele foi tirado para
mostrar a tela, não o seu argumento: o slide "combo de quarta aparece só na
quarta" saiu com o print do manual, que tem **os sete dias acesos**, e a arte
desmentia o título. Quando o slide afirma um estado da interface, fotografe
aquele estado — no sandbox, deixando a tela como estava (abra, ajuste, capture
e **feche descartando**).

**Antes de capturar, olhe a prateleira.** Fotos de produto, tela de espera do
totem e faixa do cardápio já estão em `assets/fotos/`, e os aparelhos já estão
desenhados — o índice é [`references/mockups.md`](references/mockups.md), com a
folha do catálogo em `assets/catalogo/catalogo.png`. No slide, imagem da
biblioteca vai com o prefixo `skill:`, que o renderizador resolve:

```html
<img src="skill:fotos/foto-batata.png" alt="">
```

O que é prova de um carrossel só continua em `imagens-puras/`, com caminho
relativo. Regra: **se o próximo carrossel pode querer, entra na biblioteca.**

### 4. Slides

Cada slide é um **fragmento de body** em `carrosseis/<slug>/slides/NN-nome.html`
— sem `<html>`, `<head>` ou `<!DOCTYPE>`, e sem `<script>`. O renderizador
embrulha o fragmento com a fonte Mulish, o `base.css` e a medida do formato, de
modo que o que você revisa é exatamente o que sai em PNG.

Comece copiando um modelo de `assets/slides/`:

| Modelo | Serve para |
|--------|-----------|
| `capa.html` | slide 1: gancho **mais uma imagem** |
| `texto.html` | o custo, o limite, o "vale lembrar" |
| `mockup-computador.html` | tela do painel em janela de navegador, com realce |
| `mockup-celular.html` | tela de celular (cardápio digital, app) |
| — (`.notebook`, `.monitor` no `base.css`) | página deitada vista como **cena**, não como página: capa e slide de resultado |
| `mockup-totem.html` | Totem de Autoatendimento: tela em pé sobre coluna, com cardápio de exemplo |
| `mockup-tablet.html` | Cardápio Digital no Tablet: tela deitada em suporte de mesa, com cardápio de exemplo |
| `ilustracao-app.html` | tela que não dá para capturar, desenhada em CSS |
| `antes-depois.html` | comparação; traz um cupom térmico desenhado em CSS |
| `cta.html` | último slide, um pedido só |

Os modelos de totem e de tablet saem **prontos**, com a tela e as fotos da
biblioteca: troque o texto e os itens, não o aparelho.

As classes disponíveis estão comentadas em
[`assets/slides/base.css`](assets/slides/base.css). Cores, fontes e tom de voz
ficam em [`assets/marca.json`](assets/marca.json) — mudar a marca é mudar esse
arquivo, não os slides.

O logo não é `<img>`: use `<span class="logo"></span>`. A marca tem **duas artes
oficiais** e o renderizador injeta as duas; o `base.css` escolhe pelo fundo do
slide:

| Arquivo | Onde | O que muda |
|---|---|---|
| `logo-beefood-fundo-claro.png` | `.slide`, `.slide--suave` | "BEE" em preto |
| `logo-beefood-fundo-escuro.png` | `.slide--capa` | "BEE" em branco, e contorno branco no selo |

Asa branca, cabeça preta, tarja amarela e "food" vermelho ficam iguais nas duas.
**Nunca derive uma da outra**: filtro achata a marca em branco e negativo pixel a
pixel inverte a asa e a cabeça. Falta uma versão? Peça o arquivo ao dono.

#### Onde a imagem fica na faixa

A regra que manda nas outras:

> **Imagem sozinha na faixa vai centralizada e no maior tamanho que couber, e
> reta. Encostar numa borda e inclinar só se paga quando o outro lado tem
> conteúdo.**

| Situação | Como |
|----------|------|
| imagem ocupa a faixa toda, sem sangrar | `.figura` — no fluxo, centralizada, na maior largura que a base aceita |
| mockup sozinho na faixa, sangrando | `.sangria` com recuo **igual** dos dois lados; sangra só pela base |
| mockup dividindo a faixa com texto | `.sangria` encostada + `.cena3d`/`.g3d`; é aqui que o 3D tem função |

Sangrar não é ficar torto: mockup encostado num lado com o outro lado vazio troca
tamanho por nada.

#### Mockup em sangria

Aparelho inteiro dentro da margem sai com ~420 px numa arte de 1080, e a tela
dentro dele não se lê no feed. O padrão é **sangria**: o mockup ocupa pouco mais
de meia largura, começa por volta de 27% da altura e sai pela borda — ganha
escala, e o corte passa a sensação de que a tela continua.

- **Celular** (`.sangria .sangria--celular`) sangra pela **base**.
- **Computador** (`.navegador .sangria .sangria--janela`) sangra pela
  **direita**, porque é deitado; é assim que ele passa de 1000 px de largura.
- **Notebook** (`.notebook`) e **monitor** (`.monitor`) são a outra saída para
  tela deitada: a janela mostra a **página**, e eles mostram a **cena** — alguém
  sentado, olhando aquilo. Numa capa isso vale mais que 100 px a mais de tela.
- **Totem** (`.totem`) e **tablet** (`.tablet`) já estão desenhados, com largura
  de uso e tela de exemplo — veja [`references/mockups.md`](references/mockups.md)
  e a folha `assets/catalogo/catalogo.png`. Mexer neles pede rodar o
  `catalogo.py` de novo: as três primeiras tentativas do tablet leram como
  monitor de mesa, e a folha é o que pega isso.
- **Nos dois, a caixa do elemento é só o corpo da tela** e coluna, painel e
  suporte são absolutos pendurados embaixo.
- **Regra de moldura é sempre filho direto** (`.totem__tela > img`). `.moldura
  img` alcança também as fotos de dentro de uma tela desenhada, e o `height:
  100%` de lá anula o `aspect-ratio` delas.
- **Seletor de idioma** é `.bandeira` (emoji de bandeira recortado em círculo)
  com `.bandeira--anel` no idioma em uso. No tablet ele é retangular
  (`.bandeira--retangular`) e empilhado.
- **O texto mora todo acima do mockup.** A coluna que sobra ao lado tem 288 px,
  estreita demais para corpo de 38 px. Orçamento: com o celular em `top: 530px`
  cabem chapéu + título de 2 linhas + 2 linhas de corpo; com a janela em
  `top: 700px`, chapéu + título de 2 linhas + 4 linhas de corpo.
- **`.realce`** é o anel vermelho sobre o mockup. Posicione em porcentagem do
  `.navegador__tela` e **meça a posição no arquivo** — estimar na miniatura
  circula a linha errada, já aconteceu duas vezes.

#### Mockup 3D, só quando divide a faixa

`.cena3d` no contêiner e `.g3d .g3d--na-direita` (ou `--na-esquerda`) no mockup
põem o aparelho em perspectiva. O modificador é o **lado do slide em que o mockup
está**, e o giro é sempre **para dentro**: a quina que aponta para o texto é a que
afunda, e o aparelho parece entrar no slide. Ao contrário, ele parece cair para
fora da arte.

- **Só em celular e em janela de computador.** Totem e tablet vão sempre retos:
  o 3D valoriza a espessura da peça girando, e armário em pé não tem espessura —
  girado, lê como armário tombando.
- **Só com conteúdo ao lado.** É a coluna de texto ao lado que dá licença para o
  mockup sair do centro e girar. Sozinho na faixa, ele vai centralizado, grande e
  reto — inclinar ali troca tamanho por efeito.
- **Um a cada dois ou três mockups.** Serve para dar ritmo; em todos, vira efeito.
- **Nunca no slide em que o leitor precisa ler rótulo da interface.** A face que
  recua come contraste justo onde está a informação. Slide de "onde ligar" fica
  reto; slide de ilustração ou de resultado aceita 3D.
- **Aparelho que termina dentro do slide mostra a base da tela.** Aí a barra de
  ação da ilustração vai para lá (`flex: 1` no `.tela-app__corpo` e
  `margin-top: auto` no `.tela-app__aviso`), senão sobra um vazio de 300 px e a
  tela parece render pela metade. Em mockup que sangra pela base é o contrário.
- **`.rasgado`** serrilha a base do recorte, para corte de papel não parecer erro
  de render. Vai no **mesmo elemento** do `.g3d` (a máscara recorta box-shadow e
  pseudo-elemento junto) e **come a sombra** — o que é irrelevante em fundo
  escuro e custa caro em slide claro.

#### Quando a tela não existe: ilustrar

Ordem de preferência: **captura real > print de produção que já está no
repositório > print pedido ao dono > ilustração**.

O segundo degrau é o mais esquecido: o **manual da mesma novidade** costuma ter
o print do aparelho, e ele pode estar só no `main` (o Cloud Agent parte de um
snapshot). Antes de concluir que não existe, rode `git fetch origin main` e
`git ls-tree -r --name-only origin/main -- manuais/<slug>`.

**Print que existe mas não encaixa não vira lixo.** Quando a proporção é outra
(print de totem em paisagem, tela do aparelho em retrato) ou quando a tela
cheia reduzida fica ilegível no feed, desenhe a tela em CSS copiando **layout,
paleta e hierarquia** do print, e traga dele as **fotos reais** com um script de
recorte na pasta do carrossel — coordenadas medidas no arquivo com Pillow, não
estimadas. Foto de comida inventada é o que mais denuncia tela desenhada.

Só ilustre (`.tela-app`, `.tela-totem`, `.tela-tablet`; modelos
`ilustracao-app.html`, `mockup-totem.html`, `mockup-tablet.html`, catálogo em
[`references/mockups.md`](references/mockups.md)) com as duas
condições: o comportamento desenhado está escrito na novidade ou no manual; e o
desenho usa o vocabulário do carrossel e **não** imita a interface real pixel a
pixel. Registre no `roteiro.md` o que é captura, o que é desenho e o print que
você pediu ao dono, para trocar depois.

**Nada de carimbo "ILUSTRAÇÃO" na arte.** Existiu, e saiu: numa peça de venda é
a única palavra que o leitor não esperava, rouba o olho no feed e avisa que o
que ele está vendo não é o produto. A honestidade fica onde não atrapalha a
peça — no desenho fiel (layout, paleta e **fotos reais** do aparelho) e no
`roteiro.md`.

**Texto de interface em outro idioma só entra se vier da tela.** `SEARCH`,
`MY CART`, `Order`, `Your bag is empty` é o aplicativo falando: tire de print ou
de captura, nunca do seu inglês. **Nome e descrição de produto são o contrário**:
quem escreve a versão em inglês do cardápio é o dono da loja, então traduzir
`BATATA FRITA COM CHEDDAR E BACON` para o exemplo não afirma nada sobre o
produto — desde que o carrossel não insinue tradução automática. Guarde essa
tradução num `traducoes.json` na pasta do carrossel e use **a mesma** na tela, no
print do cadastro e na legenda.

**Tela desenhada que é cortada tem de ser cortada num lugar limpo.** A
`.tela-totem__rolagem` corta o conteúdo que não cabe, com a barra da sacola fixa
no pé — sem isso sobra um vão branco de 200 px no meio da tela. O `font-size` da
tela é o que move o corte (tudo lá dentro é `em`): varra alguns valores e fique
com o que deixa o último cartão inteiro ou cortado **dentro da foto**. Corte em
cima de `R$ 8,90` lê como falha de render.

Pílula escura na capa escura desaparece: se a arte tiver alguma peça de
interface em `rgba(30,30,30,…)`, faça a versão clara antes de usá-la ali.

Cupom desenhado em `.cupom` é o caso mais tranquilo: bobina térmica em
monoespaçada é claramente desenho, e é a única forma de mostrar o "antes", que
não existe como captura.

### 5. Render

```bash
python .cursor/skills/carrossel-novidades/scripts/renderizar.py \
    carrosseis/<slug> --contato
```

Sai em `carrosseis/<slug>/png/`, mais a folha de contato para ver o conjunto de
uma vez. O script recusa PNG fora da medida e recusa mais de 10 slides.
`--formato 1:1` ou `9:16` quando o pedido não for o 4:5 padrão.
`--guias` pinta o que a interface do Instagram cobre naquele formato: no feed é
só o **contador do carrossel**, no canto superior direito (por isso o topo
direito do slide leva só o `.contador`, nunca informação); no story (9:16)
são faixas largas no topo e na base. A saída de `--guias` e de `--formato`
diferente do padrão ganha sufixo no nome, para não sobrescrever a arte final.

### 6. Revisão

```bash
python .cursor/skills/carrossel-novidades/scripts/conferir-texto.py <slug>
python ... <pasta> --novidade <slug-publicado>   # pasta com nome mais curto
```

Acusa qualquer sequência de seis palavras que apareça igual no texto (ou no
título) da novidade — nenhum rótulo do sistema chega a seis palavras, então o que
ele pega é cópia. Ele não julga o roteiro; para isso existe a tabela
fato → ângulo → slide.

1. Abra a folha de contato: o conjunto tem ritmo, ou três slides de texto seguidos?
   A capa tem imagem?
2. Abra em **tamanho real** os slides com print. Miniatura esconde texto ilegível
   e esconde realce fora de lugar — os dois erros mais comuns.
3. Confira que o mockup em sangria não cobriu nenhuma linha de texto nem os
   pontos do rodapé, que o mockup em 3D não caiu no slide que pede leitura de
   rótulo, e que nenhuma imagem sozinha na faixa ficou encostada numa borda —
   sozinha, ela vai centralizada e grande.
4. Toda afirmação do slide está no manual ou na novidade? Se não está em nenhum
   dos dois, ou você confere no sistema, ou corta. O `roteiro.md` diz quais
   telas são captura e quais são desenho? E a imagem de cada slide **prova o
   título**, ou só ilustra o assunto dele? (Print emprestado do manual costuma
   mostrar outro estado da tela — e aí a arte desmente a frase.)
5. Alguma frase explica enfeite de tela ("a bolinha verde marca…")? Algum
   diminutivo? Algum "ele" que não é o leitor nem o cliente dele? Os três saem
   — e o que fica no lugar é a consequência para o negócio.
6. Algum slide alivia um trabalho ("não precisa traduzir tudo hoje", "aos
   poucos")? Sai: é aviso de limite, e ele planta a objeção justo antes do CTA.
   E o slide do problema — normalmente o 2 — elogia o leitor antes de mostrar o
   furo, ou entrega uma fatura na cara dele?
7. Nos slides de fundo escuro, o logo do topo é a arte de fundo escuro — "BEE" em
   branco, contorno branco no selo, tarja amarela e "food" vermelho?
8. Nenhum slide tem data na arte? O topo direito é só `.contador`, a capa
   inclusive. (Data impressa dentro de um print de verdade pode ficar.)
9. Saiu peça nova de uso geral (aparelho, tela desenhada, foto, script)? Ela
   **sobe** para a skill: foto e tela em `assets/fotos/`, aparelho no
   `base.css` + `catalogo.py`, script em `scripts/`. Atualize
   [`references/mockups.md`](references/mockups.md) e rode o `catalogo.py`.
10. Registre o que aprendeu em
    [`references/MEMORIA-CARROSSEIS.md`](references/MEMORIA-CARROSSEIS.md).

### 7. Entrega

Arte renderizada não é entrega. Quem publica precisa de **três coisas**: as
imagens uma por uma, a legenda pronta para colar e um arquivo único para baixar.

Escreva `carrosseis/<slug>/copy-instagram.txt` com, nesta ordem:

1. **cabeçalho** — novidade, data, formato e a ordem de publicação;
2. **legenda** — o texto que vai no campo de legenda, com as hashtags no fim;
3. **primeiro comentário** — uma pergunta, opcional;
4. **texto alternativo** — um por imagem, para o campo de acessibilidade.

A legenda **não é a soma dos slides**: ela é o mesmo assunto em prosa corrida,
para quem leu a capa e desceu. Vale o gancho repetido da capa (é o que amarra o
post), mas nunca o texto do release — o `conferir-texto.py` mede a legenda na
mesma régua dos slides.

```bash
python .cursor/skills/carrossel-novidades/scripts/empacotar.py <slug>
```

Gera `carrosseis/<slug>/entrega/<slug>.zip` com os PNG e o `.txt`, em nomes
soltos na raiz do zip (quem recebe arrasta direto para o celular, e a ordem de
publicação é a ordem alfabética). A folha de contato fica fora de propósito: é
ferramenta de revisão, e no meio das imagens alguém posta uma imagem a mais por
engano.

Feche com commit e push, como manda a regra de commit por ação da
`MEMORIA-GERAL.md`.

## Estrutura da pasta de saída

```
carrosseis/<slug>/
├── roteiro.md            # fato→ângulo→slide e decisões de arte
├── copy-instagram.txt    # legenda, primeiro comentário e texto alternativo
├── capturar-telas.py     # só quando a captura exige clique
├── traducoes.json        # conteúdo injetado na captura, quando houver
├── imagens-puras/        # prints como saíram do navegador, nunca editados
├── slides/               # NN-nome.html (fragmentos de body)
├── png/                  # a arte final, 1080x1350
├── entrega/<slug>.zip    # png + copy, o arquivo que vai para quem publica
└── folha-de-contato.png  # todos os slides numa imagem
```

## O que a skill guarda de um carrossel para o outro

```
.cursor/skills/carrossel-novidades/
├── assets/slides/base.css   # os aparelhos e as telas desenhadas
├── assets/slides/*.html     # modelos de slide, prontos para copiar
├── assets/fotos/            # biblioteca: fotos de produto e telas reusáveis
├── assets/fundos/           # arte de fundo que entra no totem na captura
├── assets/midia/            # banner, cartaz de aviso e MP4 do cardápio digital
├── assets/catalogo/         # os aparelhos fotografados, e a folha com todos
├── scripts/capturar-totem.py, capturar-cardapio.py, fazer-midia.py,
│          preparar-fundo.py, catalogo.py
└── references/mockups.md    # o índice da prateleira: o que já existe e a medida
```

Carrossel novo começa por aí, e não por CSS novo. O que virou geral **sai** da
pasta do carrossel e vem para cá — foi o caso do capturador do totem, das fotos
de produto e do fundo de comida, que nasceram dentro do carrossel da tradução, e
do estúdio de mídia do cardápio digital, que nasceu no de capas e destaques.

## Regras de arte

- **Nenhuma data na arte.** O topo direito leva só o `.contador` ("1 de 7"), na
  capa também. Carrossel aprovado entra na fila de conteúdo e é publicado dias
  depois: data na arte faz a novidade parecer velha e impede reaproveitar o post.
  Data **dentro de print de verdade** fica (a do cupom é do pedido, não do post),
  e a data da novidade mora no `roteiro.md` e no cabeçalho da copy.
- **Uma ideia por slide.** Duas frases longas no mesmo slide são dois slides.
- **Tantos slides quantos a novidade tiver de assunto**, entre 6 e 8 (o teto
  técnico é 10). Oito não é meta: o carrossel da tradução fecha em 7 porque o
  oitavo slide só existiria para chegar a oito. Quem lê no feed costuma parar no
  quinto, então ponha o ganho no começo.
- **O gancho fala do salão, não do sistema.** "Cansou de bebida esquecida na
  sacola?" prende; "Novo campo Destaque na impressão" não.
- **Escreva como gente fala.** O vício que aparece sozinho é o aforismo — título
  curto, impessoal, fechado em si mesmo ("Todo recurso novo vira manual no mesmo
  dia"). Chame a pessoa de **você**, pergunte, e não corte a frase até virar
  telegrama. Teste: leia os títulos em voz alta, seguidos. A tabela
  travado × falado está em `references/roteiro-e-copy.md`.
- **O sujeito é você ou seu cliente, nunca um "ele" solto.** "Ele toca na
  bandeira e o cardápio muda" narra um personagem que não é quem lê, e é o que
  dá ao texto a cara de máquina. "Seu cliente toca na bandeira e pede sozinho"
  diz o mesmo fato e tem dono.
- **É peça de venda, na voz do site.** `beefood.com.br` é a régua: manchete é
  ganho ("Mais pedidos, menos filas no seu restaurante"), a linha de apoio é
  concreta ("Menos necessidade de garçons extras") e o slide fecha no que muda
  para o negócio — fila que anda, mesa que fecha mais alta, equipe que rende
  mais. Descrever funcionamento sem consequência é documentação, não post.
- **Nunca avise o limite do recurso.** "Não precisa traduzir tudo hoje", "aos
  poucos", "com calma": parece gentileza e entrega o contrário — aliviar um
  trabalho é admitir que existe um trabalho, e plantar essa objeção no slide
  antes do CTA é derrubar a peça no fim. Quem precisa do limite abre o manual.
  Honestidade se faz mostrando a tela certa (o cadastro onde o texto em inglês é
  escrito), não com aviso.
- **O slide do problema elogia antes de cobrar.** Slide 2 é onde o leitor decide
  se arrasta: "Quanto seu salão **perde** por não falar inglês?" entrega uma
  fatura, e ninguém salva post para ler a própria conta. Comece pelo que ele já
  tem funcionando ("Seu cardápio é o seu melhor **vendedor**") e traga o furo
  depois, na mesma frase que traz a solução.
- **Se a tela prova, o slide é a tela.** Antes de escrever cinco linhas
  explicando que o cardápio existe em outro idioma, veja se dois recortes da
  mesma tela não dizem isso sozinhos — mesmo item, mesma foto, mesmo preço, nome
  diferente. Recorte medido no DOM (mesma caixa nos dois idiomas) e capturado em
  escala 2; o texto vira uma linha.
- **Microdetalhe de interface não é conteúdo.** "A bolinha verde marca o idioma
  que já tem texto" é correto e não agrega nada a quem está no feed — é material
  de manual. Teste cada frase com "o que muda para ele se eu tirar isso?"; se a
  resposta é "ele sabe menos um detalhe da tela", corta e ponha a consequência
  no lugar. Enfeite de tela, nome de campo e regra fina de comportamento entram
  quando **são** o assunto do slide, nunca como explicação de brinde.
- **Nada de diminutivo.** "Bandeirinha", "bolinha", "telinha": aparece quando a
  gente tenta soar simpático e faz o recurso parecer pequeno. Escreva
  "bandeira", "sinal", "tela". Exceção só para nome próprio de produto.
- **Emoji: pouco e onde couber.** Até um por slide, e não em todos. Prefira os
  que a novidade usa (🖨️ 🛵) e os do assunto (🥤). Emoji que aponta (👇) vai
  encostado com `&nbsp;`, senão cai sozinho na linha. Slide de limite não leva.
- **A capa é a frase mais curta do carrossel**, com **uma** palavra no `.destaque`
  vermelho e nenhum emoji junto dela. Duas palavras vermelhas não destacam nada,
  e emoji ao lado do vermelho é grifo em cima de grifo.
- **A capa tem imagem**, e a imagem é o resultado da novidade (o papel impresso,
  a tela nova) — nunca um ícone decorativo. Capa só de texto perde no feed.
- **A imagem da capa mostra um destaque só.** Cupom com duas linhas marcadas
  contradiz o slide que pede critério. Se a captura que existe não dá para
  recortar até sobrar um destaque, gere uma captura nova em que só ele apareça.
- **Na capa, tela cheia ganha de tela icônica.** Tela cujo miolo é gradiente ou
  foto (a de espera do totem, por exemplo) deixa um vão morto no meio da capa.
  Prefira a tela que mostra o recurso funcionando e enche a área útil.
- **Imagem em pé na capa custa uma linha de subtítulo.** Aparelho em pé come
  ~830 px de altura: com título de 2 linhas cabe **1** linha de subtítulo, e o
  resto do recado vai para a legenda.
- **Metade dos slides, no mínimo, tem imagem.** Três slides de texto seguidos é
  sinal de que dois deveriam virar um.
- **Mockup em sangria**, não aparelho inteiro pequeno no meio do slide. E se ele
  está sozinho na faixa, a sangria vai centralizada, com recuo igual dos dois
  lados.
- **Número só se ele existir** na novidade ou no manual. "Reduz 30% dos erros"
  é invenção, e invenção em post de produto volta como reclamação.
- **Números normais** (`1.`, `2.`, `3.`) — nunca ①②③. Mesma regra dos manuais.
- **Sem seta e sem número dentro da imagem.** Anotação assada no arquivo é
  linguagem de manual. Para dirigir o olhar no carrossel: recorte mais fechado e,
  se ainda faltar, o `.realce` — que é CSS no slide, não pixel no print.

## O que nunca fazer

- **Carimbar "ILUSTRAÇÃO" na arte.** A pílula existiu e foi removida da skill: é
  a única palavra da peça que o leitor não esperava ler, e avisa que aquilo não
  é o produto justo no slide que devia vender.
- **Ilustrar comportamento que ninguém conferiu.** É o que o carimbo tentava
  compensar, e não compensava. O desenho mostra o que está escrito na novidade
  ou no manual, com layout, paleta e fotos reais do aparelho — e nada além
  disso. O `roteiro.md` registra o que é captura e o que é desenho.
- **Falar de um "ele" que não é quem lê.** Quem lê é o dono do restaurante: o
  sujeito da frase é **você** ou **seu cliente**. Narrar a cena em terceira
  pessoa é o que deixa o texto com cara de máquina.
- **Recortar a novidade em slides.** O carrossel se escreve a partir do fato; o
  texto do release não vai para a arte.
- **Publicar dado pessoal.** Este repositório é público; nome, telefone e e-mail
  de cliente saem na imagem **pura**, não só na arte.
- **Editar `manuais/`, `MEMORIA-GERAL.md` ou `CHECKLIST-MANUAIS.md`.**
- **Prometer comportamento não conferido.** Se a novidade é vaga, diga menos.
