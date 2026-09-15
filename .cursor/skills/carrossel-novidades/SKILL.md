---
name: carrossel-novidades
description: Produz carrossel de Instagram (prints reais, mockups e slides em PNG 1080x1350) sobre uma novidade publicada em beefood.app/novidades ou sobre um tema do sistema BeeFood. Use quando o pedido falar de carrossel, post, arte, slides, divulgação ou comunicação de novidade. Não use para escrever manual de usuário — manual tem fluxo próprio na MEMORIA-GERAL.md.
---

# Carrossel de novidades do BeeFood

Transforma uma novidade do sistema em carrossel publicável: prints reais do
produto, mockups de celular e navegador, e slides exportados no tamanho exato do
Instagram.

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

Crie `carrosseis/<slug>/roteiro.md` com a tabela de slides (arquivo, tipo, a
**ideia única** de cada um e qual imagem ele usa), as decisões que você tomou e a
legenda de publicação. Como escrever o gancho, o corpo e o CTA está em
[`references/roteiro-e-copy.md`](references/roteiro-e-copy.md).

Roteiro aprovado primeiro; captura depois. Print tirado antes do roteiro quase
sempre é print que não entra.

### 3. Capturas

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
largura do slide fica ilegível no feed. Regra de bolso: o recorte não passa de
**~540 px de largura lógica**, senão o texto da tela cai abaixo de 20 px na arte
de 1080 px. Prefira fechar a borda do recorte em área vazia — corte no meio de
uma palavra parece defeito.

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
| `capa.html` | slide 1, só o gancho |
| `texto.html` | o problema, o "o que muda", o "vale lembrar" |
| `print-navegador.html` | print do painel dentro de moldura de navegador |
| `mockup-celular.html` | um ou dois celulares lado a lado |
| `antes-depois.html` | comparação; traz um cupom térmico desenhado em CSS |
| `cta.html` | último slide, um pedido só |

As classes disponíveis estão comentadas em
[`assets/slides/base.css`](assets/slides/base.css). Cores, fontes e tom de voz
ficam em [`assets/marca.json`](assets/marca.json) — mudar a marca é mudar esse
arquivo, não os slides.

O logo não é `<img>`: use `<span class="logo"></span>` e o renderizador injeta o
arquivo da skill.

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

1. Abra a folha de contato: o conjunto tem ritmo, ou três slides de texto seguidos?
2. Abra em **tamanho real** os slides com print. Miniatura esconde texto ilegível.
3. Toda afirmação do slide está no manual ou na novidade? Se não está em nenhum
   dos dois, ou você confere no sistema, ou corta.
4. Registre o que aprendeu em
   [`references/MEMORIA-CARROSSEIS.md`](references/MEMORIA-CARROSSEIS.md).
5. Commit e push, como manda a regra de commit por ação da `MEMORIA-GERAL.md`.

## Estrutura da pasta de saída

```
carrosseis/<slug>/
├── roteiro.md            # slides, decisões e legenda de publicação
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
- **O gancho fala do salão, não do sistema.** "A bebida não fica mais para trás"
  prende; "Novo campo Destaque na impressão" não.
- **Números normais** (`1.`, `2.`, `3.`) — nunca ①②③. Mesma regra dos manuais.
- **Sem seta e sem número nos prints.** Anotação é linguagem de manual; em
  miniatura de carrossel ela só suja a imagem. Para dirigir o olhar, recorte.
- **Um emoji por slide, no máximo**, e só se a novidade já usa aquele emoji.

## O que nunca fazer

- **Inventar tela.** Sem captura real, o slide não existe. Mockup de app Android
  é o caso clássico: o emulador não sobe no Cloud Agent, então ou a captura vem
  de aparelho real, ou aquele slide fica fora do carrossel.
- **Publicar dado pessoal.** Este repositório é público; nome, telefone e e-mail
  de cliente saem na imagem **pura**, não só na arte.
- **Editar `manuais/`, `MEMORIA-GERAL.md` ou `CHECKLIST-MANUAIS.md`.**
- **Prometer comportamento não conferido.** Se a novidade é vaga, diga menos.
