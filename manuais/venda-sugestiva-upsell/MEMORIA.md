# MEMÓRIA — #103 Venda Sugestiva (UpSell)

Pasta: `manuais/venda-sugestiva-upsell/` · Manual: `venda-sugestiva-upsell.md` · 13 imagens
Produzido em 17/09/2026, em **produção**, na conta sandbox
**BeeFood3 - Manual** (`contato@beefood.com.br`, `empresaID 38311`).

## Pedido do dono

> "faça git pull em beefood-web-react → veja a nova funcionalidade de venda sugestiva
> (upsell), precisamos criar um manual completo + mostrar como fica no cardapio digital.
> o upsell pode ser configurado por 3 lugares: em /cardapio nos 3 pontinhos, nos 3
> pontinhos de um produto, na modal de produto. a venda sugestiva funciona em: cardapio
> digital (delivery e presencial), cardapio digital tablet, totem autoatendimento. o
> relatorio pode ser visto junto com as sugestoes atuais: desempenho →
> delivery/presencial → sugestões. as sugestoes automaticas não é possível configurar
> (não precisa falar isso no manual, esquece)."

O `git pull` no `beefood-web-react` trouxe a funcionalidade inteira (commit `029145e`),
inclusive os planos do Lovable em `.lovable/plan/venda-sugestiva-upsell-*`.

**Decisão de escopo:** as **sugestões automáticas** (a lista que o cardápio monta dentro
do carrinho a partir do histórico de vendas, sem configuração no painel) ficaram
**fora** do manual, por pedido explícito. Elas existem no mesmo bundle
(`recalculateSuggestions`, campo `sugestoes` do item) e caem no **mesmo relatório** —
por isso o texto fala do relatório como "sugestões", sem prometer que o número é só de
upsell.

## Por que o recurso pode não aparecer

`src/utils/vendaSugestivaAcesso.ts` libera por empresa:
`VENDA_SUGESTIVA_EMPRESAS = [107, 38311]`. Sem isso somem os três caminhos (item do menu
de ações, item do menu do produto e a aba do cadastro). O sandbox dos manuais é
**exatamente** uma das empresas liberadas — deu para capturar tudo em produção. O manual
abre avisando que o recurso está em liberação, sem citar `empresaID`.

## O que virou texto do manual

- **Três caminhos, uma configuração.** Janela geral (`ModalVendaSugestivaGeral`), janela
  de escolha (`ModalVendaSugestiva`) e aba do cadastro (`ProdutoVendaSugestivaTab`)
  gravam no mesmo endpoint. A aba **salva sozinha** (etiqueta *Salvo automaticamente*);
  as duas janelas exigem **SALVAR (F2)** e o **CANCELAR (ESC)** descarta sem avisar.
- **Limite de 6** (`MAX_UPSELL`), com a mensagem *"Limite de 6 atingido. Remova um para
  escolher outro."* e as caixinhas dos outros desabilitadas — imagem 06.
- **A ordem do array é a ordem que o cliente vê.** Nada é reordenado por nome. Virou
  aviso na seção 2.1 e item da FAQ.
- **A configuração é por cardápio (filial).** `filialID = filialAtual?.filialID ||
  userData.filialID`. Virou pré-requisito 4 e linha de *Problemas comuns*.
- **Salvar com zero selecionados limpa** a configuração (não existe DELETE) — é a
  resposta de "como eu desligo".
- **Não existe permissão nova**: acompanha quem já edita produto.
- **Não existe a aba em complemento** (`hideForComplemento`), e produto ainda sem
  `produtoID` mostra *"Salve o produto antes de configurar a venda sugestiva."*

## O que o cliente vê (e o achado mais útil)

`openUpsell` no bundle Nuxt de `menu.beefood.com.br` roda depois de o item entrar no
carrinho e **filtra a lista**: descarta o próprio produto, o que **já está na sacola**, o
inativo e o `disabled`, corta em 6 e só abre a janela se sobrar alguém.

Isso apareceu na prática: o **Combo One Burger** foi configurado com **quatro** produtos
(Anéis de Cebola Empanada, Milk Shake de Morango, Brownie, Pudim - Leite Condensado) e o
cliente vê **três** — o **Brownie** está oculto naquele cardápio pela tabela
*Ocultar Brownie (manual)* do #68. Não foi bug: foi o filtro funcionando.

A pedido do dono (17/09/2026), esse caso é **explicado com nome e sobrenome** no manual,
em três lugares: a seção 5 virou *"Produto inativo ou oculto não aparece na sugestão"*
(com a lista dos cinco motivos de descarte e o cruzamento das duas imagens — quatro chips
na linha *Sugere:* da imagem 02, três cards na imagem 07); a seção 6 ganhou o item
*"São três cards, e não quatro"*; e há uma pergunta própria na FAQ. O texto também diz
que a configuração **não se perde**: quando o produto volta ao cardápio, volta a ser
oferecido.

Outro detalhe provado nas capturas: **o preço é o do canal**. O mesmo anel de cebola sai
por **R$ 17,60** no delivery e **R$ 19,20** no presencial; o milk-shake aparece com
*R$ 18,90* riscado, selo *-20%* (Preço Programado do #69) e o cashback do item.

Fluxo da janela: título **Que tal levar junto?**, linha *"Você adicionou &lt;produto&gt;."*,
os cards e o rodapé **CONTINUAR SEM ADICIONAR**. Tocar num card **não adiciona**: abre o
produto normal, e quem confirma é o **Adicionar**.

## Relatório — o que foi medido

`Desempenho → Delivery → Sugestões` e `Desempenho → Presencial → Sugestões` são o mesmo
componente (`DigitalMenuSuggestions.tsx` do `beefood-reports-hub`), chamando
`relatorioSugestao/{empresaID}/{inicio}/{fim}/{tipo}` com `tipo` 1 (delivery) e 2
(presencial).

**O relatório é processado uma vez por dia e leva até 24 horas** — informação do dono, em
17/09/2026, depois da primeira entrega do manual. É a explicação certa para o que a
medição do dia mostrou:

| Venda | Situação | Aparece no relatório? |
|-------|----------|-----------------------|
| 809 (13/08) | `FECHADO`, arquivada | **sim** — é o R$ 44,00 / 4 sugestões da imagem 09 |
| 1013 (17/09, feita para este manual, com o upsell aceito) | `RECEBIDO`, `valorPago 51,94` | **não** — ainda não processada |

> **Erro que ficou registrado de propósito.** A primeira versão deste manual explicava a
> ausência da 1013 pela **esteira** (a venda ainda estar no caixa aberto) e mandava o
> lojista conferir "depois do fechamento do caixa". Era dedução minha a partir da
> diferença entre as duas vendas, não regra do produto — a regra é o **processamento
> diário**. Antes de explicar atraso de relatório por estado de venda, pergunte: quase
> todo relatório do BeeFood tem janela de processamento.

Consequência das capturas, que fica valendo: a imagem 09 mostra números de uma venda
antiga e a **10 (presencial) sai zerada** — `tipo=2` não tem **nenhuma** linha em 2026
inteiro (conferido pela API). O manual usa a 10 como exemplo do relatório vazio e avisa,
nas duas seções, na FAQ e em *Problemas comuns*, que os números do dia levam até 24 h.

> Para quem retomar: passadas 24 h, a venda **1013** deve aparecer no relatório de
> delivery com o **Milk Shake de Morango** — o item aceito na janela da imagem 07. Vale
> recapturar a imagem 09 então. Nada de fechar caixa: era conclusão errada.

O `sugestao: true` que marca a linha é gravado item a item no `pedidoPOST.js` do backend;
foi confirmado no payload do pedido 1013.

## Capturas

Três scripts, uma etapa por imagem:

- `capturar.py` — painel (imagens 01–06). Etapas: `acoes`, `geral`, `escolha`, `vazia`,
  `toast`, `menu_produto`, `aba`, `limite`.
- `capturar-cardapio.py` — cardápio público em 390×844 DPR 2 (as puras das tiras 07 e
  08), delivery e `?tipo=p` para o presencial.
- `capturar-relatorio.py` — relatório dentro do iframe (`09`, `10`), com
  `PERIODO="Últimos 60 dias"`.

Armadilhas anotadas (as duas primeiras são novas e valem para outros manuais):

- **O ⋮ do card do produto não tem rótulo próprio e a grade é virtualizada.** Todos os
  cards têm o mesmo botão. O que funcionou foi `abrir_menu_do_produto()`: achar o título
  do produto, pegar todos os botões com `svg.lucide-ellipsis-vertical` e escolher o que
  está **à direita e na mesma linha** (menor diferença de `y`, tolerância de 40 px).
- **Rolar o relatório não funciona com `window.scrollTo`**: o conteúdo está num iframe
  com rolagem própria. O jeito é `page.mouse.move()` sobre o iframe + `page.mouse.wheel`
  em passos pequenos, e depois **afastar o ponteiro** (`mouse.move(80, 700)`) para não
  ficar tooltip do gráfico no print.
- Combo já vem com a **única opção do primeiro grupo obrigatório pré-selecionada**:
  clicar nela *desmarca* e o **Adicionar** recusa. Só clicar em grupo cujo cabeçalho
  ainda mostra **OBRIGATÓRIO**.
- A janela de sugestão é `fullscreen` no celular — o print pega ela inteira.
- **Cache do cardápio público demorou mais que o 1 minuto de sempre** (uns 10 minutos
  entre salvar o upsell e a janela abrir para o cliente). Se a sugestão não aparecer,
  esperar antes de suspeitar da configuração.

Sobras em `imagens-puras/` que **não** entram no manual: `08-presencial-produto-sugerido.png`
(a tira do presencial ficou com 2 aparelhos), `10-relatorio-presencial-listas.png`
(rankings vazios) e a série `90-pedido-*` (prova do pedido real 1013).

## Ambiente: o que foi alterado

- **Venda sugestiva configurada em 2 produtos** do sandbox (conferido pela API em
  17/09/2026): **Combo One Burger** (`2515341`) com 4 itens — Anéis de Cebola Empanada,
  Milk Shake de Morango, Brownie, Pudim - Leite Condensado — e **Combo Chicken Deluxe**
  (`2515351`) com 6 itens (os três pudins, os dois milk-shakes e o Brownie), que ficou
  no `6/6` da imagem 06. Fica como cenário do manual; para zerar, abrir cada um e
  salvar sem nenhum marcado.
- **Um pedido real de delivery (venda 1013)** feito pelo cardápio público com a sugestão
  aceita, aceito no painel e recebido em dinheiro. Serve de prova do `sugestao: true`.
- Nenhum produto, preço, setor ou parâmetro foi alterado.
