# MEMORIA.md — #124 Mais de um cardápio no totem

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `totem-multicardapio.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

## Pedido do dono

22/09/2026, logo depois de fechado o bloco #121–#123:

> "o totem é multi cardapio. acabei de inserir um cardápio adicional na empresaID
> 38311 e agora na aba cardápios do totem é possível ativar este. então o totem
> mostra o cardápio pro cliente selecionar ou ambos. estude e crie um manual sobre
> multicardápios no totem."

Ou seja: o dono **montou o cenário** (o cardápio adicional na filial 50502) e
pediu o manual do recurso. O #121 já tinha a aba Cardápios, mas só em três
parágrafos de texto — sem o cenário não havia como fotografar nada.

## Escopo

A chave do painel e **cada tela nova do aparelho**: escolher o cardápio, ver os
dois juntos, ver um só, misturar na sacola e achar o pedido no painel. Fecha com
o seletor de cardápios que o painel ganha, porque é ele que responde "mexi no
preço e o totem não mudou".

Fica fora: contratar o Cardápio Adicional (é checkout de plano), e o cadastro de
setor/produto em detalhe — descrito em texto, apontando para o #121 e para o
manual do Cardápio.

## O que o estudo achou (o que virou seção)

1. **A tela de escolha só existe a partir do segundo cardápio.** No bundle:
   `if (menus.length > 1)`. Com um cardápio, o totem continua indo direto aos
   produtos — logo, quem liga a chave muda o primeiro toque do cliente.
2. **"Ver todos os cardápios" não é só concatenação.** Produtos somam (67 + 98 =
   165), mas os setores são **deduplicados por `produtoSetorID`**: 7 + 12 = 19
   setores viram **17** na tela, porque *Bebidas* e *Sobremesas* são o mesmo
   registro nos dois cardápios. Virou a dica da seção 3 e duas linhas de problemas
   comuns (setor "repetido" e setor que "sumiu").
3. **O pedido é um só, na loja do totem.** `POST totem2/pedido/processar` não tem
   `filialID` por item. Confirmado com venda real: item de sushi + item de burger
   na venda **1168**, loja *BeeFood3 - Manual*.
4. **Preço e chave de totem são por cardápio** (aba Cardápios do produto). É a
   resposta para "preciso cadastrar tudo de novo?" — não precisa.
5. **Correção do #121:** setor sem foto no meio de setores com foto **não** fica
   com espaço vazio; ele cai no **logotipo da loja**
   (`src = setor.s3Link || logotipoDaLoja`). O #121 foi corrigido na mesma sessão.

## O pedido misto real (22/09/2026)

Técnica do ensaio: `python3 capturar.py ensaio` percorreu tudo até a tela de
pagamento sem gravar, e só depois `VALENDO=1 python3 capturar.py pedido` fechou.

| Dado | Valor |
|------|-------|
| Venda / Pedido | 1168 / 73 |
| Itens | Temaki de Atum R$ 35,00 (cardápio adicional) + One Burger R$ 28,00 (principal) |
| Forma | Dinheiro, **Não pago** |
| Total | R$ 63,00 → **R$ 62,37** (1% da forma *Dinheiro*) |
| Mesa | 14 — é por ela que o `capturar.py detalhe` acha o card certo |
| Cliente | Teste Manual, (15) 99999-8888 |

A venda ficou **aberta** no sandbox, como as do #123. Nada foi recebido no caixa.

## Imagens (7)

| Arquivo | Conteúdo |
|---------|----------|
| `01-modal-cardapios-chave.png` | A aba Cardápios: principal travada, chave do adicional ligada |
| `02-totem-escolha-cardapio.png` | *Escolha um cardápio*: Ver todos, principal (SELECIONADO) e adicional |
| `03-totem-todos-cardapios.png` | Os dois cardápios juntos, com a emenda da coluna de setores visível |
| `04-totem-cardapio-adicional.png` | Só o cardápio adicional, para comparar a coluna com a imagem 03 |
| `05-totem-sacola-mista.png` | A sacola com um item de cada cardápio e o total |
| `06-painel-pedido-misto.png` | O pedido no Delivery: um card, dois itens, loja do totem |
| `07-painel-editando-cardapio.png` | O seletor de cardápios do painel e a faixa EDITANDO CARDÁPIO |

Decisões de recorte e anotação:

- A **03 precisou de rolagem** na coluna de setores. Sem rolar, o alto da tela era
  idêntico ao da 04 e a imagem não provava nada — a emenda (setores do sushi com
  logotipo, setores da hamburgueria com foto) é o conteúdo da foto.
- A **05 vai em duas faixas empilhadas** (`crops` + risco cinza no corte): os itens
  ficam no alto e o total no pé, com meia tela vazia no meio.
- Na **01**, o corte em `y=760` tira o vão até o rodapé do modal, e as três
  etiquetas cabem **dentro** do modal — foi o único caso do bloco do totem sem
  faixa branca à esquerda.
- Na **06**, a seta da origem *AutoAtendimento* **saiu**: o assunto é do #123 e ela
  só disputava espaço com a linha do tempo do pedido.

## Scripts

`capturar.py`: `painel`, `aparelho`, `ensaio`, `pedido` (com `VALENDO=1`),
`detalhe`.

Manhas do aparelho, as duas que custaram tempo:

- O **seletor de cardápio** é `motion.button` e **ignora `click()` por
  JavaScript** — precisa de `page.mouse.click` (o `tocar(..., real=True)` e o
  `escolher()` do script). O mesmo já valia para o teclado numérico no #123.
- O `escolher()` tem de ser **escopado no diálogo**
  (`[role=dialog][aria-labelledby="menu-picker-title"]`): procurar "sushi" no
  documento inteiro acha o cartão de um produto atrás da camada e o clique morre.
- Item do cardápio adicional para o pedido misto: **Temaki de Atum**, escolhido por
  não ter grupo de opções. Depois de adicionar, a **venda sugestiva** entra na
  frente e precisa de *CONTINUAR SEM ADICIONAR*.
- `capturar.py detalhe` acha o card pela **Mesa 14**; clicar no primeiro *Teste
  Manual* da coluna abria outro pedido do sandbox.

Tentativa abandonada: captura da **aba Cardápios do produto**. Em `/cardapio` com
dois cardápios, o mesmo nome de produto aparece duas vezes na listagem e o modal
não abriu por clique automatizado. A seção 7 descreve os campos em texto, lidos no
`ModalEditarProduto.tsx`, e a foto fica para um futuro manual do **Cardápio
Adicional**.

## Status

Concluído — 7 imagens, manual, fluxo de código e prompt de publicação. Inclui a
correção do #121 (foto do setor).
