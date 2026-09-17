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
(dois grupos de até 5 mídias, horizontal, MP4 H.264, tocando sozinho e sem som),
e apareceu a aba **Avisos**, com cartaz quadrado, título e descrição, para dar
recado sem cadastrar produto de R$ 0,00. Tudo com **agenda** por dia da semana,
faixa de horário e canal (Delivery, Presencial). Fora da agenda, a mídia não
aparece.

## Fato → ângulo → o que o slide diz

| Fato (novidade e manual) | Ângulo | O que o slide diz |
|---|---|---|
| Capa e destaques aceitam vídeo, e a mídia roda sozinha no cardápio | cardápio digital é lista de preço; o que vende na rua é a vitrine que se move | "Seu cardápio digital já tem **vídeo**?" |
| O dono já tem foto, descrição e combo montados; faltava movimento | ele fez a parte difícil e não sabe que o trabalho agora rende mais | "Você já fez a parte mais difícil" |
| A capa fixa continua o primeiro slide; os destaques entram depois dela | ele tem medo de perder a capa que já escolheu | "Olha o que muda no topo do cardápio" (antes × agora) |
| Destaques da sua loja: vitrine no meio da página, até 5 mídias | quem entra para pedir um lanche e sai com sobremesa | "No meio do cardápio, a sua vitrine" |
| Aba Avisos: imagem quadrada, título e descrição, sem botão de pedir | a gambiarra de cadastrar produto de R$ 0,00 para dar recado | "Recado de feriado não é produto de R$ 0,00" |
| Agenda por dia, hora e canal; fora do período a mídia sai do ar | a promoção de quarta que fica no ar até domingo | "Combo de quarta aparece só na quarta" |
| Prévia ao vivo na aba Configurações; até 1 minuto para publicar | — | fora: é detalhe de tela de quem já está configurando |

## Slides

1. **Capa** — "Seu cardápio digital já tem **vídeo**?" com o notebook
   centralizado e grande, mostrando a capa em vídeo rodando no cardápio.
2. **O reconhecimento** — elogia o trabalho que já está feito (foto, descrição,
   combo) e traz o furo junto com a solução: faltava movimento.
3. **Antes × agora** — o topo do mesmo cardápio, no celular, sem mídia e com o
   vídeo. A capa fixa continua lá; o vídeo entra depois dela.
4. **A vitrine** — destaques da loja no meio da página, onde o cliente já está
   rolando. Imagem e vídeo na mesma fileira.
5. **Avisos** — o cartaz de recado, aberto no celular do cliente, e o fim do
   produto de R$ 0,00.
6. **Agenda** — dia, horário e canal, com a linha real do painel.
7. **CTA** — um pedido só: suba a primeira mídia.

## Capturas

Tudo em `imagens-puras/`. Nenhuma tela é desenhada neste carrossel: o cardápio
público é o próprio aplicativo, rodando com a nossa mídia injetada na resposta
da API (`--conteudo midias.json`). Nada foi gravado em loja de cliente.

```bash
# 1. a mídia de exemplo (banner 1920x580, cartaz 1080x1080, MP4 mudo)
python3 .cursor/skills/carrossel-novidades/scripts/fazer-midia.py

# 2. o cardápio modelo com a mídia dentro dele
python3 .cursor/skills/carrossel-novidades/scripts/capturar-cardapio.py \
  --saida carrosseis/cardapio-capas-destaques/imagens-puras \
  --conteudo carrosseis/cardapio-capas-destaques/midias.json

# 3. as duas telas que exigem clique: a agenda com um dia só e a página de
#    novidades parada no cartão desta publicação
python3 carrosseis/cardapio-capas-destaques/capturar-telas.py
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

O recorte é só dos dias da semana: a linha inteira da agenda tem 1276 px e,
reduzida para os 904 px da margem do slide, a letra do painel some no feed.
Horário e canal estão no texto do slide.

## A mídia de exemplo

As artes são nossas, feitas no `fazer-midia.py`, com as fotos de produto e os
preços reais do cardápio modelo (TASTY BACON a partir de R$ 41,90, SMASH 2.0 a
partir de R$ 44,90 — números lidos da API pública do cardápio). Ficam em
`assets/midia/` da skill, para o próximo carrossel de cardápio digital já nascer
com elas.

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

E a arte de capa joga o texto todo para a faixa de cima: embaixo, o próprio
cardápio desenha o logotipo da loja (à esquerda no computador, no meio no
celular) e o selo de avaliação fica no alto à direita.

## A capa em vídeo

O carrossel do Instagram aceita vídeo no lugar de uma imagem, e neste post a
novidade **é** movimento: capa parada gasta o melhor argumento da peça. O
`video/01-capa.mp4` é o mesmo slide 1, com o vídeo rodando dentro do notebook.

```bash
python3 .cursor/skills/carrossel-novidades/scripts/filmar-slide.py \
  carrosseis/cardapio-capas-destaques/slides/01-capa.html \
  --tomada pc-capa-video \
  --conteudo carrosseis/cardapio-capas-destaques/midias.json \
  --saida carrosseis/cardapio-capas-destaques/video/01-capa.mp4 \
  --segundos 6 --fps 12
```

O script mede no DOM a caixa da tela do notebook (78,696 · 922x576), fotografa
o cardápio quadro a quadro avançando o `currentTime` do vídeo na mão e costura
tudo por cima do PNG do slide. Os temporizadores da página são desligados antes
da filmagem: cada quadro custa quase um segundo de relógio real, e sem isso o
carrossel do cardápio troca de mídia sozinho no meio do filme.

O PNG parado continua entregue, para quem preferir publicar tudo em imagem.

## Legenda da publicação

Está em `copy-instagram.txt`, junto com o primeiro comentário e os textos
alternativos.
