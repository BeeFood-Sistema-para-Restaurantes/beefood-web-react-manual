# Memória dos carrosséis

Memória própria desta skill. Aprendizado de **captura genérica** do BeeFood
continua na `MEMORIA-GERAL.md`, escrita por quem trabalha nos manuais — aqui só
entra o que é de carrossel.

Última atualização: 2026-09-15 (skill criada; primeiro carrossel: *Destaque na
impressão*).

## Índice

| Carrossel | Novidade | Pasta | Formato | Estado |
|-----------|----------|-------|---------|--------|
| Destaque na impressão | [15/09/2026](https://beefood.app/novidades/destaque-impressao) | `carrosseis/destaque-impressao/` | 4:5, 7 slides | ✅ renderizado |

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

## Mockup

- **Sem notch.** A ilha desenhada em cima da captura tapa o cabeçalho da própria
  tela que o slide quer mostrar. A moldura arredondada já comunica "celular".
- Moldura de celular em CSS (`aspect-ratio: 390/844`) resolve o que nos manuais
  exigia o `montar_celulares` do `annotate.py`: o print entra como `<img>`,
  reduzido pelo navegador, sem passo de montagem em Pillow.
- Captura de celular: `--dispositivo celular` (390×844, `device_scale_factor=3`).
  O 3× existe porque o print entra reduzido na moldura e o 2× já mostrava serra
  no texto pequeno.

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
