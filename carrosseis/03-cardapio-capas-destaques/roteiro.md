# Roteiro — Avisos, capas e destaques com imagem e vídeo no Cardápio Digital

- Novidade: https://beefood.app/novidades/cardapio-digital-avisos-banners-capas-midia
- Data da novidade: 13/08/2026
- Manuais relacionados no repositório:
  - `manuais/cardapio-digital-capas-destaques/` (capa, vitrine, vídeo, agenda)
  - `manuais/cardapio-digital-avisos/` (o cartaz de recado)
- Cardápio modelo: https://menu.beefood.com.br/oneburger/ (ONE STAND HAMBURGUERIA)
- Cardápio com o recurso configurado: https://menu.beefood.com.br/beefood3
- Formato: 4:5, 7 slides

## O fato, em três linhas

A capa e a vitrine do cardápio digital passaram a aceitar **imagem e vídeo**
(dois grupos de até 5 mídias, horizontal, MP4 H.264, tocando sozinho e sem som).
No topo isso muda de figura: a foto de capa era uma só e ficava parada, e agora
é o primeiro slide de um carrossel que roda sem o cliente tocar em nada. Também
apareceu a aba **Avisos**, com cartaz quadrado, título e descrição, para dar
recado sem cadastrar produto de R$ 0,00. Tudo com **agenda** por dia da semana,
faixa de horário e canal (Delivery, Presencial). Fora da agenda, a mídia não
aparece.

## Fato → ângulo → ideia de uso → o que o slide diz

A coluna da **ideia de uso** é a que decide o texto. A pergunta na cabeça de
quem lê é "isso serve pra quê na minha loja?", e cada slide responde uma. Sem
essa coluna, o slide escorrega para um dos dois lados: ensina a mexer no sistema
ou narra a cena do cliente em close.

| Fato (novidade e manual) | Ângulo | Ideia de uso | O que o slide diz |
|---|---|---|---|
| O topo aceitava **uma** foto parada; agora a foto fixa é o primeiro slide de um carrossel de até 5 mídias, imagem ou vídeo, que passam sozinhas | cardápio digital é lista de preço; o que vende na rua é a vitrine que se move | mostrar até cinco fotos e vídeos onde cabia uma foto | "Sua capa agora é um **carrossel**" |
| O dono já tem foto, descrição e combo montados; faltava movimento | ele fez a parte difícil e não sabe que o trabalho agora rende mais | mostrar os produtos dele em foto e vídeo | "Você já fez a parte mais **difícil**" |
| A capa fixa continua o primeiro slide; os destaques entram depois dela | ele tem medo de perder a capa que já escolheu | pôr um vídeo do produto depois da capa que ele já escolheu | "Seu cliente vê a **comida** antes do preço" |
| Destaques da sua loja: vitrine no meio da página, até 5 mídias | quem entra para pedir um lanche e sai com sobremesa | destacar combo do dia, sobremesa nova ou milk shake entre as categorias | "Um banner chamativo vende mais **combo**" |
| Aba Avisos: imagem quadrada, título e descrição, sem botão de pedir | a gambiarra de cadastrar produto de R$ 0,00 para dar recado | subir um cartaz de recado e apagar o produto que fazia esse papel | "Recado não é produto de **R$ 0,00**" |
| Agenda por dia, hora e canal; fora do período a mídia sai do ar | a promoção de quarta que fica no ar até domingo | programar a promoção para entrar e sair sozinha | "Combo de quarta aparece só na **quarta**" |
| Prévia ao vivo na aba Configurações; até 1 minuto para publicar | — | — | fora: é detalhe de tela de quem já está configurando |

## Slides

1. **Capa** — "Sua capa agora é um **carrossel**" com o notebook centralizado e
   grande, mostrando a capa em vídeo rodando no cardápio. Afirmação, e não
   pergunta: os três carrosséis anteriores abriram perguntando, e o quarto
   seguido faz da pergunta cacoete de marca, não gancho.
2. **O reconhecimento** — elogia o trabalho que já está feito (foto, descrição,
   combo) e traz o furo junto com a solução: faltava movimento.
3. **Antes × agora** — o topo do mesmo cardápio, no celular, sem mídia e com o
   vídeo. A capa fixa continua lá; o vídeo entra depois dela.
4. **O meio do cardápio** — o banner entre as categorias, e o ganho no título:
   pedido de lanche que vira pedido de combo com sobremesa.
5. **Avisos** — o cartaz de recado, aberto no celular do cliente, e o fim do
   produto de R$ 0,00.
6. **Agenda** — dia, horário e canal, com a linha real do painel.
7. **CTA** — um pedido só: subir a primeira mídia.

Nenhum dos sete blocos abre igual a outro, e nenhum abre com "você pode": a
abertura alterna entre o imperativo ("Destaque", "Suba", "Programe"), o ganho
dito direto ("Combo de quarta aparece só na quarta") e o reconhecimento ("Você
já fez a parte mais difícil"). Sete imperativos em fila seriam template do mesmo
jeito que sete "você pode".

## Capturas

Tudo em `imagens-puras/`. Nenhuma tela é desenhada neste carrossel: o cardápio
público é o próprio aplicativo, rodando com a nossa mídia injetada na resposta
da API (`--conteudo midias.json`). Nada foi gravado em loja de cliente.

```bash
# 1. a mídia de exemplo (banner 1920x580, cartaz 1080x1080, MP4 mudo)
python3 .cursor/skills/carrossel/scripts/fazer-midia.py

# 2. o cardápio modelo com a mídia dentro dele
python3 .cursor/skills/carrossel/scripts/capturar-cardapio.py \
  --saida carrosseis/03-cardapio-capas-destaques/imagens-puras \
  --conteudo carrosseis/03-cardapio-capas-destaques/midias.json

# 3. as duas telas que exigem clique: a agenda com um dia só e a página de
#    novidades parada no cartão desta publicação
python3 carrosseis/03-cardapio-capas-destaques/capturar-telas.py
```

| Arquivo | O que é |
|---|---|
| `pc-capa-video.png` | capa no slide de vídeo, computador (1440x900, escala 2) |
| `pc-capa-imagem.png` | capa no slide de imagem, computador |
| `pc-vitrine.png` | vitrine no slide de vídeo, computador |
| `pc-avisos.png` | fileira de avisos, computador |
| `cel-capa-video.png` | capa no vídeo, celular (390x844, escala 3) |
| `cel-capa-limpa.png` | o mesmo topo sem mídia nenhuma — o "antes" |
| `cel-vitrine.png` | vitrine no vídeo, celular |
| `cel-avisos.png` | fileira de avisos, celular |
| `cel-aviso-aberto.png` | aviso aberto, com título e descrição |
| `pc-capa-limpa.png` | capa parada no computador (reserva do "antes") |
| `novidades-celular.png` | página de novidades, parada no cartão desta novidade |
| `painel-dias.png` | dias da semana no painel, com só a quarta marcada |

O `painel-dias.png` começou como recorte do print do manual e teve de ser
refeito: lá os **sete** dias estão acesos, e o slide 6 diz que o combo de quarta
aparece só na quarta — a arte desmentia o título. O `capturar-telas.py` abre o
modal no sandbox, apaga seis dias, fotografa a linha e **fecha descartando**, de
modo que a agenda do sandbox continua como o manual deixou.

O `novidades-celular.png` para no **título** do cartão, e não no começo dele: o
cartão abre com as etiquetas e a data da publicação, e data que aparece na arte
data o post. Rolando 12 px além do cabeçalho fixo, etiquetas e data ficam atrás
dele e o print continua sendo print.

O recorte é só dos dias da semana: a linha inteira da agenda tem 1276 px e,
reduzida para os 904 px da margem do slide, a letra do painel some no feed.
Horário e canal estão no texto do slide.

## A mídia de exemplo

As artes são nossas, feitas no `fazer-midia.py`, com as fotos de produto e os
preços reais do cardápio modelo (TASTY BACON, R$ 41,90; SMASH 2.0, R$ 44,90 —
números lidos da API pública do cardápio). Ficam em `assets/midia/` da skill,
para o próximo carrossel de cardápio digital já nascer com elas.

**Quem fala na arte não é a BeeFood, é a loja.** Este carrossel tem duas vozes,
e confundi-las foi o erro da primeira rodada: nos slides fala a BeeFood com o
dono, em tom claro e correto; nas artes fala o dono da ONE Stand, no cartaz
dele, com alguém que está com fome. Por isso o selo dá ocasião ("Chegou", "Pede
junto", "Pra fechar") e não categoria de produto, e a linha é o que o atendente
diria no balcão ("Pede a grande. Confia.", "Pede junto com o lanche. Depois não
cabe.").

A versão anterior escrevia "a partir de R$ 44,90" e "Sai da fritadeira e vai
direto pra mesa" — a primeira é a **string da interface** do cardápio, que
aparece doze vezes na página do produto, e a segunda é legenda de catálogo.
Nenhuma loja imprime cartaz com o texto do próprio software.

No cartaz de aviso vale a mesma economia: o card do aviso já imprime título e
descrição **embaixo** da imagem, então a linha dentro da arte diz outra coisa. A
arte do feriado fala quando a loja volta ("Dia 8 a chapa volta a ligar"), e o
card, o que a loja faz no dia ("Dia 7 a cozinha descansa. Voltamos dia 8, no
horário de sempre").

| Arte | Onde entra | Tipo |
|---|---|---|
| `banner-capa-combo.jpg` | destaques da capa | imagem |
| `banner-capa-chapa.mp4` | destaques da capa | vídeo, 6 s, mudo |
| `banner-vitrine-shake.mp4` | destaques da loja | vídeo, 6 s, mudo |
| `banner-vitrine-batata.jpg` | destaques da loja | imagem |
| `aviso-feriado.png` | avisos | imagem quadrada |
| `aviso-horario.png` | avisos | imagem quadrada |
| `aviso-so-delivery.png` | avisos | imagem quadrada |

Por que o banner é 1920x580 e não 16:9: o cardápio mostra a mídia numa faixa,
com `object-fit: cover`. Medido no aplicativo, o vão é ~4,1/1 no computador e
~2,6/1 no celular. A primeira rodada foi em 16:9 e o cardápio comeu o selo e o
preço. Em 3,3/1 a perda fica em ~20% de cada lado e cabe na zona segura.

O zoom do vídeo de capa é **ancorado no topo** (`"ancora": "topo"` no
`fazer-midia.py`). Ancorado no centro, o cardápio corta a faixa em cima e
embaixo e, no último segundo do filme, o selo "SAIU DA CHAPA" aparecia pela
metade. Preso no topo, o texto só se afasta da borda.

Na largura, o teto é outro: o corte do celular (~2,6/1) come 10% de cada lado, a
margem segura da arte tem 14%, e em 1,22 o zoom leva o resto — rodando inteiro
num celular, o título perde a primeira letra depois de uns 4 s. A captura de
celular é feita no segundo 2,4, e é esse quadro que entra no slide 3. Arte feita
para rodar inteira no celular pede zoom de 1,08, ou texto a 22% da borda.

E a arte de capa joga o texto todo para a faixa de cima: embaixo, o próprio
cardápio desenha o logotipo da loja (à esquerda no computador, no meio no
celular) e o selo de avaliação fica no alto à direita.

## Um emoji no carrossel inteiro

Os sete títulos têm palavra em vermelho, e emoji junto do grifo é grifo em cima
de grifo. O 👇 do slide 4 e o 🎬 do slide 7 saíram; sobrou o 🎬 no rótulo do
cartão do slide 2, que não disputa com vermelho nenhum.

## A capa em vídeo ficou fora

A entrega são os **7 PNG**, e nada de MP4. A capa em vídeo foi filmada com o
`filmar-slide.py` e descartada: o zoom que dá vida ao banner é o mesmo que come
o texto dele. O cardápio já corta a faixa em cima e embaixo para caber no vão de
4,1/1, e a partir do quarto segundo o avanço da lente empurra "CHEGOU", "SMASH
2.0" e "R$ 44,90" contra a borda esquerda até faltar letra.

Dá para salvar baixando o zoom, e aí o filme quase não anda — foi exatamente
essa a reclamação da primeira versão. Arte de banner com texto encostado na
margem e zoom de capa não convivem no mesmo arquivo: ou a arte nasce com 22% de
folga, ou o slide é parado.

O script continua na skill, para a próxima novidade em que o movimento não
disputar espaço com a letra.

## Legenda da publicação

Está em `copy-instagram.txt`, junto com o primeiro comentário e os textos
alternativos.
