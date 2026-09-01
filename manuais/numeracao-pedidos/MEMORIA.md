# MEMÓRIA — Entendendo a numeração dos pedidos (#74)

Manual **conceitual**: explica os dois números da venda, não ensina um cadastro.
Estudo que o originou: [`PLANO-NUMERACAO-PEDIDOS.md`](../../PLANO-NUMERACAO-PEDIDOS.md).

Estado: ✅ **Concluído** em 01/09/2026. 6 imagens, 13 setas + 1 moldura.

---

## 1. O que o manual afirma, e com que prova

| Afirmação | Prova |
|-----------|-------|
| Número da venda nunca reinicia | 304 vendas na faixa 627–930, zero buraco e zero repetição |
| Número do pedido reinicia a cada caixa | Virada **reproduzida ao vivo** (930/pedido 60 → 931/pedido 1) e caixa 927703 com pedido nº 1 **4 segundos** depois da abertura |
| Mesa nunca recebe | 0 de 15 vendas de mesa no histórico; e não existe `mesaNumeroPedido` no código |
| Mesa não consome número | Caixa 927703 usou 110 números na faixa 1..110 **sem buraco**, tendo 13 vendas sem número |
| PDV depende do switch | Parâmetro `pdvNumeroPedido`; hora exata em que foi ligado: 21/08 entre 16:21 e 16:33 |
| Formato `pedido (venda)` | 12 pontos no código + conferido em 4 telas |

Detalhe técnico em `fluxo-codigo.md`.

---

## 2. Como o cenário foi montado (01/09/2026)

O dono **fechou o caixa 967508** às 16:39:40 e o caixa **983507** abriu às 16:39:44. Isso deixou
a virada do contador disponível para fotografar, o que é a imagem central do manual.

Vendas criadas pela tela do PDV, produto **Suco de uva Del Valle** (R$ 8,90 — nome único no setor
Bebidas, então o clique não corre risco de cair no produto errado; a base tem nomes repetidos):

| Venda | Pedido | Situação | Observação |
|------:|-------:|----------|------------|
| 931 | **1** | Recebido (Dinheiro) | Primeiro pedido do caixa novo. Paga depois, via **Reabrir (F6)** |
| 932 | **2** | Recebido (Dinheiro) | Confirma que a contagem segue 1, 2, 3… |

As vendas 929 e 930 (delivery, pedido 59 e 60) já existiam e ficaram **Abertas** — são elas que
aparecem no card do Delivery e do lado de baixo da virada.

**Nenhuma venda de mesa foi criada.** Não era preciso: o histórico já tinha as vendas 854–858
entre os pedidos 5 e 6, que provam as duas coisas ao mesmo tempo (mesa não recebe e mesa não
consome). E o PDV **não** serve para criar venda de mesa: ele manda `tipo: 'PDV'` mesmo com a
mesa selecionada no topo — venda de mesa exige o fluxo **Novo Pedido (F1)** da tela de Mesas.

---

## 3. Armadilhas de captura (custaram tempo)

- **O clique na mesa livre não abre nada.** Na tela de Mesas, selecionar uma mesa livre não inicia
  venda; é o **Novo Pedido (F1)** que abre o fluxo.
- **O modal Reabrir Venda exige confirmar.** Clicar na linha da venda só a seleciona: sem
  **CONFIRMAR SELEÇÃO (F1 / ENTER)** o carrinho fica vazio e o botão **Receber** continua
  desabilitado.
- **A aba de setor do PDV é `div`, não `button`.** `button:has-text('Bebidas')` acha zero
  elementos; localizar pelo texto exato do `div` no topo resolve.
- **A paginação do Histórico não responde a `button:has-text('Próximo')`.** O caminho que
  funcionou foi trocar **Itens por página** para **100** (o seletor abre `[role="option"]`) e
  rolar até a linha desejada com `scrollIntoView({block:'center'})`.
- **O cabeçalho da tabela é fixo (sticky) e encobre a linha logo abaixo dele.** Na imagem 03 o
  recorte começa **abaixo** do cabeçalho por isso; quem mostra o cabeçalho da coluna é a
  imagem 02.

### O cupom: popup bloqueado, e como contornar

O botão de impressora do detalhe da venda (`lucide-printer` no cabeçalho do modal — o
`chef-hat` ao lado é a ficha de cozinha) tenta o BeeImpressão, falha e avisa
*"Servidor offline. Usando impressão do navegador."*

Esse fallback **não é** `window.open`: é `imprimirViaIframe`, que escreve o cupom num iframe
oculto de id **`beefood-print-frame`** (`src/lib/impressao-service.ts`). Duas consequências:

1. Sobrescrever `window.open` **não captura nada** (foi a primeira tentativa, e falhou).
2. Nenhuma aba nova abre, então não há o que fotografar na tela.

O que funcionou: instalar um `MutationObserver` + poll de 40 ms antes do clique, ler
`contentDocument.documentElement.outerHTML` do iframe assim que ele aparece, e renderizar esse
**mesmo HTML** numa página limpa com viewport de 400 px (bobina de 80 mm). O conteúdo é idêntico
ao que o navegador do usuário mostraria.

---

## 4. Imagens

| Arquivo | Setas | Onde entra no manual |
|---------|------:|----------------------|
| `01-parametros-pdv.png` | 2 | Ligando no PDV |
| `02-historico-virada.png` | 3 | **A virada do contador** (imagem central) |
| `03-historico-mesa.png` | 3 + moldura | Mesa não recebe e não gasta número |
| `04-delivery.png` | 2 | Como o sistema escreve os dois |
| `05-venda-detalhe.png` | 2 | Os dois números (abertura) |
| `06-cupom.png` | 1 | O cupom do cliente |

`annotate.py` recorta antes de anotar (a tela cheia do Histórico tem 16 colunas e o número fica
ilegível na página publicada) e usa **margem à esquerda** nas imagens 02 e 03, para a seta sair
dela e chegar ao número sem atravessar os botões da coluna **Ações**. Raio do badge tem mínimo
de 14 px, senão ele desaparece na imagem estreita do cupom.

### Dado pessoal coberto na imagem PURA

O repositório é público e a pura também é versionada. Foram borradas, **antes do primeiro
commit**:

- coluna **Cliente** do Histórico nas imagens 02 e 03 (a 03 tinha um nome completo real);
- **telefone e endereço** do cliente nos dois cards do Delivery (imagem 04).

A coluna **Mesa/Comanda** ficou legível de propósito: são nomes de mesa e comanda, não dado de
cliente, e o manual precisa deles.

---

## 5. Decisões do dono (01/09/2026)

| Assunto | Decisão |
|---------|---------|
| Corrigir o manual **#44** (ele descreve o switch errado) | **Não** — deixar como está |
| Incluir a descoberta do **checkbox Delivery** na abertura do caixa | **Não** — ficou registrada no `fluxo-codigo.md` |
| Nome do item de menu | **Entendendo a numeração dos pedidos** |
| Dois caixas abertos ao mesmo tempo | Sem resposta. Manual escrito **no singular** ("o caixa aberto"), sem afirmar nada sobre caixas simultâneos |

---

## 6. Estado do ambiente ao terminar

- Caixa **983507** aberto, com as duas vendas do manual pagas em Dinheiro. Nenhuma venda
  pendente deixada por este trabalho.
- Parâmetro **Número de Pedido no PDV**: **ligado** (`checked`), como já estava. Nenhum switch
  foi clicado — a tela de Parâmetros tem auto-save de 500 ms e clicar "só para ver" já altera.
- Vendas 929 e 930 seguem **Abertas** no Delivery: já estavam assim antes.
