# MEMÓRIA — #106 Montar a rota

Pasta: `manuais/gestao-entregas-montar-rota/` · Numeração: **#106** ·
Escrito em 18/09/2026 na sandbox **BeeFood3 - Manual** (`empresaID 38311`,
`filialID 39202`, entregador `194115` simulado por script).

Segundo manual do painel, depois do [#105](../gestao-entregas-mapa-painel/MEMORIA.md). Ele
presume o vocabulário do #105 e entrega o #107 (despachar) com a rota já montada.

## O recorte

O plano previa "selecionar, criar, ordenar, adicionar, remover, mover entre rotas, marcar
pronto" — sete verbos. Virou **seis seções**, porque *remover pedido* e *mover entre rotas*
são a mesma mecânica de *adicionar*, e cabem como frase em vez de seção própria.

A decisão de redação que organiza o manual: **rota nasce parada**. Isso permite separar
"montar" (este manual, sem consequência nenhuma para o cliente) de "despachar" (#107, que
dispara aviso, impressão e marketplace). Um manual só, com os dois assuntos, ensinaria a
apertar um gatilho irreversível no meio de uma explicação de organização.

## O que mudou o texto depois de ler o backend

1. **A letra da rota é reaproveitada** — é a menor letra livre entre as rotas **ativas**, e
   rota concluída devolve a letra. Na sandbox há três rotas do dia, todas `A`. O manual
   passou a avisar que a letra não serve para falar de entrega passada.
2. **As sete travas foram removidas de propósito.** Não dá para escrever "o sistema não
   permite" em lugar nenhum deste bloco. A dica final do manual virou justamente isso: quase
   nada é bloqueado, e o cuidado é do operador.
3. **Adicionar pedido joga no fim da fila** (`ordem = max + 1`), o que explica o *Otimizar
   ordem* reaparecendo logo depois.
4. **O menu de "Adicionar à rota" lista rotas concluídas.** A API aceita. O manual marca a
   opção errada com seta própria, em vez de fingir que ela não existe.
5. **Otimizar ordem é vizinho mais próximo em linha reta**, calculado no navegador — sem
   malha viária e sem trânsito. E o **app desfaz** com o botão *melhor rota*.

## Decisões de captura

- **Refiz o fluxo inteiro do zero**, apagando a rota da rodada anterior. A primeira rodada
  tinha as quatro primeiras telas certas, mas faltavam o grupo da rota aberto, o menu de três
  pontos e o *Adicionar à rota* — e capturá-los depois, numa rota diferente, deixaria o
  manual com números de pedido trocando de seção para seção.
- **Três armadilhas novas**, todas registradas na `MEMORIA-GERAL`:
  1. menu flutuante **não abre** com `element.click()` via `evaluate` (o componente escuta
     `pointerdown`) — tem de ser o clique do Playwright com `force=True`;
  2. menu flutuante sobre o mapa **não sai no print**, porque o Leaflet compõe por cima no
     headless. Em vez de esconder o mapa (metade da imagem branca), **subir o `z-index` do
     popper e baixar o das `.leaflet-pane`**. O mapa fica na foto;
  3. **parar o ponteiro** antes do print: depois de *Otimizar ordem* o botão desaparece e a
     primeira parada nasce embaixo do cursor, que troca o visto pelo "x" de remover.
- **Duas cópias da mesma pura** (`05a` e `05b`) para o grupo da rota. Cabeçalho e paradas
  ficam a 100 px um do outro; nove setas na mesma imagem viram um novelo. `recortar` com a
  caixa inteira serve de cópia.
- **Etiquetas sobre o mapa.** A lateral é densa e não tem vão: as etiquetas caem no mapa, à
  esquerda, e as setas entram na lateral pela borda dos cartões. Ficou legível com ~120 px
  de distância vertical entre etiquetas.
- **Dois alvos derivados**, não chutados: a bolinha da letra (sempre 62 px à esquerda do chip
  de situação) e a alça/visto de outras linhas (altura de linha fixa, 99 px, medida nas três
  paradas do print). Está comentado no `annotate.py`.

## O que ficou fora

| Assunto | Por quê |
|---|---|
| Arrastar parada **na prática** (captura do arraste) | print de meio-arraste não se lê; a alça marcada com seta resolve |
| Remover parada | o "x" da linha só aparece com o ponteiro em cima, e o caminho do lojista é *Excluir rota* ou arrastar |
| Mover pedido entre rotas | é *Adicionar à rota* mais uma vez; virou frase, não seção |
| Despachar | #107, de propósito |

## Links que este manual faz

| Para | Estado |
|---|---|
| `../gestao-entregas-mapa-painel/` | ✅ #105 |
| `../gestao-entregas-liberar-entregador/` | ✅ #104 |
| `../gestao-entregas-despachar/` | ✅ #107 |
| `../gestao-entregas-fechar-entrega/` | ✅ #108 |
| `../gestao-entregas-despacho-automatico/` | ✅ #109 |
