# Memória dos carrosséis

Memória própria desta skill. Aprendizado de **captura genérica** do BeeFood
continua na `MEMORIA-GERAL.md`, escrita por quem trabalha nos manuais — aqui só
entra o que é de carrossel.

Última atualização: 2026-09-15 (2ª rodada: texto reescrito em vez de recortado,
capa com imagem, mockup em sangria, mockup de computador, ilustração com selo).

## Índice

| Carrossel | Novidade | Pasta | Formato | Estado |
|-----------|----------|-------|---------|--------|
| Destaque na impressão | [15/09/2026](https://beefood.app/novidades/destaque-impressao) | `carrosseis/destaque-impressao/` | 4:5, 8 slides | ✅ renderizado (2ª versão) |

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

O `conferir-texto.py` mecaniza a parte objetiva: acusa sequência de **6 palavras**
igual ao título ou ao texto da novidade. A janela é 6 porque nenhum rótulo do
sistema chega a seis palavras — com janela 4 o script acusa "na ficha da cozinha"
e "logo abaixo de descrição", que **têm** de repetir. Rodando na 1ª versão ele
pega a capa (`a bebida não fica mais para trás`, que era o próprio título da
novidade) e o slide *vale lembrar* (`a equipe volta a não saber o que conferir`);
na 2ª versão passa limpo.

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
- O logo entra por `--logo` no `:root`, não por `<img>`: assim nenhum carrossel
  precisa de uma cópia do arquivo.

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

## Zona segura — o que o Instagram realmente cobre

A primeira versão do `--guias` pintava 120 px no topo e 180 px na base do 4:5.
**Está errado para o feed:** ali o Instagram não sobrepõe barra nenhuma à arte —
o cabeçalho do perfil e os botões de curtir ficam fora da imagem. O que ele
desenha por cima é o **contador do carrossel**, no canto superior direito.

Consequência de projeto: o canto superior direito do slide leva só coisa
dispensável (a data, o "3 de 7"). As faixas largas de topo e base valem para o
**story (9:16)**, e o `--guias` agora pinta a zona certa de cada formato.

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

Na capa a conta muda: o `.inclinado` (rotação de −3°) avança o canto do papel
~15 px além da largura declarada, então a coluna de texto para em 400 px.

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

## Ilustração de tela (imagem "fake")

App Android (Garçom, Entregador, Tablet) não sobe no Cloud Agent, e o slide que
mostra o efeito na rua era justamente o que faltava. A saída é desenhar a tela em
HTML/CSS (`.tela-app` no `base.css`, modelo `ilustracao-app.html`), com ordem de
preferência clara: **captura real > print pedido ao dono > ilustração**.

Três condições, todas obrigatórias:

1. o comportamento desenhado está escrito na novidade ou no manual;
2. o desenho usa o vocabulário do carrossel (cartão arredondado, Mulish, cor da
   marca) e **não** imita a interface real pixel a pixel;
3. o slide leva `.selo-ilustracao` — ilustração que passa por captura engana quem
   lê, e este repositório é público.

O selo mora na coluna vazia à esquerda do celular em sangria (`left: 88px`).
Colocado sobre o texto, ele foi lido como botão.

Cupom desenhado em CSS (`.cupom`) não precisa de selo: bobina térmica em
monoespaçada é claramente desenho, e é a única forma de mostrar o "antes" — que
não existe como captura.

## Onde a tela mora

| Tela | Como capturar |
|------|---------------|
| painel web (`beefood.app`) | `capturar.py --rota /cardapio` |
| cardápio digital público | `capturar.py --url <link> --publico --dispositivo celular` |
| app Android (Garçom, Entregador, Tablet) | não roda aqui: peça o print ao dono (zip em URL pública, seção 6 da `MEMORIA-GERAL.md`) ou ilustre com selo |
| coisa que não é tela (cupom, impressora) | print do manual, se existir; senão desenho em CSS |

## Reaproveitamento do manual

O slide pode apontar direto para o print do manual
(`../../../manuais/<manual>/imagens-puras/<arquivo>.png`). Foi assim com o
cupom do #99: é o mesmo cupom, e duplicar o arquivo criaria duas verdades.
Prints **puros**, nunca os tratados — os tratados têm setas numeradas, que são
linguagem de manual.

## Cuidados

- O `validar-imagens.py` da raiz varre **só** `manuais/`. Ele não enxerga
  `carrosseis/`, e não deve: carrossel não tem `imagens-tratadas/` nem
  `texto-documentation.ia.md`.
- `/tmp/beefood-estado.json` guarda a sessão do Playwright. Se alguma permissão
  do grupo de acesso mudou, apague o arquivo: o `config_cache` do front congela
  no estado antigo.
