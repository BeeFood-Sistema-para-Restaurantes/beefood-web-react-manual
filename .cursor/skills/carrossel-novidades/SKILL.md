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
diz** (é o que permite auditar que nada foi inventado e nada foi copiado), a
tabela de slides (arquivo, tipo, ideia única, imagem) e a legenda de publicação.
Método completo em [`references/roteiro-e-copy.md`](references/roteiro-e-copy.md).

Roteiro aprovado primeiro; captura depois. Print tirado antes do roteiro quase
sempre é print que não entra.

### 3. Capturas

Primeiro decida **onde a tela mora** — é isso que define se existe captura:

| Tela | O que fazer |
|------|-------------|
| painel web (`beefood.app`) | `capturar.py --rota /cardapio` |
| cardápio digital público | `capturar.py --url <link> --publico --dispositivo celular` |
| app Android (Garçom, Entregador, Tablet) | não roda no Cloud Agent: **peça o print ao dono** (zip em URL pública, seção 6 da `MEMORIA-GERAL.md`) e, enquanto ele não vem, ilustre com selo (passo 4) |
| coisa que não é tela (cupom, impressora, balança) | print do manual, se existir; senão desenho em CSS |

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
| `ilustracao-app.html` | tela que não dá para capturar, desenhada e com selo |
| `antes-depois.html` | comparação; traz um cupom térmico desenhado em CSS |
| `cta.html` | último slide, um pedido só |

As classes disponíveis estão comentadas em
[`assets/slides/base.css`](assets/slides/base.css). Cores, fontes e tom de voz
ficam em [`assets/marca.json`](assets/marca.json) — mudar a marca é mudar esse
arquivo, não os slides.

O logo não é `<img>`: use `<span class="logo"></span>` e o renderizador injeta o
arquivo da skill.

#### Mockup em sangria

Aparelho inteiro dentro da margem sai com ~420 px numa arte de 1080, e a tela
dentro dele não se lê no feed. O padrão é **sangria**: o mockup ocupa pouco mais
de meia largura, começa por volta de 27% da altura e sai pela borda — ganha
escala, e o corte passa a sensação de que a tela continua.

- **Celular** (`.sangria .sangria--celular`) sangra pela **base**.
- **Computador** (`.navegador .sangria .sangria--janela`) sangra pela
  **direita**, porque é deitado; é assim que ele passa de 1000 px de largura.
- **O texto mora todo acima do mockup.** A coluna que sobra ao lado tem 288 px,
  estreita demais para corpo de 38 px. Orçamento: com o celular em `top: 530px`
  cabem chapéu + título de 2 linhas + 2 linhas de corpo; com a janela em
  `top: 700px`, chapéu + título de 2 linhas + 4 linhas de corpo.
- **`.realce`** é o anel vermelho sobre o mockup. Posicione em porcentagem do
  `.navegador__tela` e **meça a posição no arquivo** — estimar na miniatura
  circula a linha errada, já aconteceu duas vezes.

#### Quando a tela não existe: ilustrar

Ordem de preferência: **captura real > print pedido ao dono > ilustração**.

Só ilustre (`.tela-app`, modelo `ilustracao-app.html`) com as três condições:
o comportamento desenhado está escrito na novidade ou no manual; o desenho usa o
vocabulário do carrossel e **não** imita a interface real pixel a pixel; e o
slide leva `.selo-ilustracao`. Registre no `roteiro.md` o print que você pediu ao
dono, para trocar depois.

Cupom desenhado em `.cupom` não precisa de selo: bobina térmica em monoespaçada é
claramente desenho, e é a única forma de mostrar o "antes", que não existe como
captura.

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
direito do slide leva a data ou o "3 de 7", nunca informação); no story (9:16)
são faixas largas no topo e na base. A saída de `--guias` e de `--formato`
diferente do padrão ganha sufixo no nome, para não sobrescrever a arte final.

### 6. Revisão

```bash
python .cursor/skills/carrossel-novidades/scripts/conferir-texto.py <slug>
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
   pontos do rodapé.
4. Toda afirmação do slide está no manual ou na novidade? Se não está em nenhum
   dos dois, ou você confere no sistema, ou corta. Toda tela desenhada tem selo?
5. Registre o que aprendeu em
   [`references/MEMORIA-CARROSSEIS.md`](references/MEMORIA-CARROSSEIS.md).
6. Commit e push, como manda a regra de commit por ação da `MEMORIA-GERAL.md`.

## Estrutura da pasta de saída

```
carrosseis/<slug>/
├── roteiro.md            # fato→ângulo→slide, decisões e legenda de publicação
├── capturar-telas.py     # só quando a captura exige clique
├── imagens-puras/        # prints como saíram do navegador, nunca editados
├── slides/               # NN-nome.html (fragmentos de body)
├── png/                  # a arte final, 1080x1350
└── folha-de-contato.png  # todos os slides numa imagem
```

## Regras de arte

- **Uma ideia por slide.** Duas frases longas no mesmo slide são dois slides.
- **Máximo 10 slides**, e quem lê no feed costuma parar no quinto: ponha o ganho
  logo no começo, não no fim.
- **O gancho fala do salão, não do sistema.** "Cansou de bebida esquecida na
  sacola?" prende; "Novo campo Destaque na impressão" não.
- **Escreva como gente fala.** O vício que aparece sozinho é o aforismo — título
  curto, impessoal, fechado em si mesmo ("Todo recurso novo vira manual no mesmo
  dia"). Chame a pessoa de **você**, pergunte, e não corte a frase até virar
  telegrama. Teste: leia os títulos em voz alta, seguidos. A tabela
  travado × falado está em `references/roteiro-e-copy.md`.
- **Emoji: pouco e onde couber.** Até um por slide, e não em todos. Prefira os
  que a novidade usa (🖨️ 🛵) e os do assunto (🥤). Emoji que aponta (👇) vai
  encostado com `&nbsp;`, senão cai sozinho na linha. Slide de limite não leva.
- **A capa tem imagem**, e a imagem é o resultado da novidade (o papel impresso,
  a tela nova) — nunca um ícone decorativo. Capa só de texto perde no feed.
- **A imagem da capa mostra um destaque só.** Cupom com três linhas marcadas
  contradiz o slide que pede critério. Recorte até sobrar a linha do assunto.
- **Metade dos slides, no mínimo, tem imagem.** Três slides de texto seguidos é
  sinal de que dois deveriam virar um.
- **Mockup em sangria**, não aparelho inteiro no meio do slide.
- **Número só se ele existir** na novidade ou no manual. "Reduz 30% dos erros"
  é invenção, e invenção em post de produto volta como reclamação.
- **Números normais** (`1.`, `2.`, `3.`) — nunca ①②③. Mesma regra dos manuais.
- **Sem seta e sem número dentro da imagem.** Anotação assada no arquivo é
  linguagem de manual. Para dirigir o olhar no carrossel: recorte mais fechado e,
  se ainda faltar, o `.realce` — que é CSS no slide, não pixel no print.

## O que nunca fazer

- **Passar desenho por captura.** Ilustrar é permitido e às vezes é o único jeito
  (app Android não sobe no Cloud Agent), mas só com as três condições do passo 4
  — e a terceira é o `.selo-ilustracao` no slide. Sem selo, o leitor entende que
  aquela é a tela real do produto.
- **Ilustrar comportamento que ninguém conferiu.** O desenho pode mostrar o que
  está escrito na novidade ou no manual, e nada além disso.
- **Recortar a novidade em slides.** O carrossel se escreve a partir do fato; o
  texto do release não vai para a arte.
- **Publicar dado pessoal.** Este repositório é público; nome, telefone e e-mail
  de cliente saem na imagem **pura**, não só na arte.
- **Editar `manuais/`, `MEMORIA-GERAL.md` ou `CHECKLIST-MANUAIS.md`.**
- **Prometer comportamento não conferido.** Se a novidade é vaga, diga menos.
