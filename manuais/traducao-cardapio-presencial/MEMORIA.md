# MEMORIA.md — #100 Tradução Cardápio Presencial

## Pedido do dono (16/09/2026)

> "faça um git pull em beefood-web-react e veja a ultima atualização de
> tradução para inglês dos Setores, Produtos, Descritivo dos produtos,
> complementos e descritivo dos complementos e grupo de opções. crie um manual
> **Tradução Cardápio Presencial**. ele se aplica ao Cardápio Digital Tablet e
> Totem Autoatendimento. as imagens do Cardapio Digital Tablet e Totem
> Autoatendimento eu vou te passar depois e você trata. objetivo agora é
> mostrar como traduzir o cardapio presencial."

## Escopo

Como **traduzir** o cardápio presencial no painel. Cinco cadastros com
bandeiras: setor, produto (nome + descrição), complemento (nome + descrição) e
grupo de opções, mais o interruptor **Habilitar tradução** do totem.

As telas vistas pelo cliente entraram em 16/09/2026, com fotos de produção
enviadas pelo dono: **totem** (tela inicial e menu) na seção 7 e **tablet** na
seção 8.

## Fonte

`beefood-web-react` atualizado em 16/09/2026 (`bdb7106`). A tradução entrou nos
commits `da3049d` (10/09) e `de63fe5` (13/09) — arquivo novo
`src/components/cardapio/BandeiraIdioma.tsx`. Detalhe técnico em
`fluxo-codigo.md`.

## Cenário do sandbox (BeeFood3)

- `qtdAA = 5` e `qtdTablet = 10` no `config_cache` → `temTraducaoContratada()`
  verdadeiro, então as bandeiras aparecem. **Sem totem/tablet contratado o
  campo não tem bandeira nenhuma** — é o primeiro item dos problemas comuns.
- `aaTraducao` do totem já estava **ligado** (o modal lê da API, o
  `config_cache` mostrava `null`). Nada foi alterado nessa tela.
- Exemplos escolhidos com **nome único** (a base tem 21 nomes repetidos; duas
  *Batata frita* e dois *One Burger*):

| Item | ID | Português | Inglês | Espanhol |
|------|----|-----------|--------|----------|
| Setor | 213752 | Acompanhamentos | Sides | Guarniciones |
| Produto | 2515373 | Anéis de Cebola Empanada / *Porção com 8 cebolas empanadas* | Breaded Onion Rings / *Portion with 8 breaded onion rings* | Aros de cebolla empanizados / *Porción con 8 aros de cebolla empanizados* |
| Complemento | 2515378 | Molho verde | Green sauce | Salsa verde |
| Grupo de opções | 257216 | Escolha um molho | Choose a sauce | Elige una salsa |

- **Limpeza:** o setor **Bebidas** (213756) tinha tradução de teste do
  desenvolvedor (`Drinksx` / `Drinkles`). Foi trocada por `Drinks` / `Bebidas`
  para as futuras fotos do totem não saírem com texto sujo.
- Gravado de verdade (não é ensaio) e conferido pela API nos endpoints de
  detalhe: o português ficou intacto nos quatro itens.

## Imagens (9)

As 6 primeiras são capturas do painel (2160×1350). As 7 a 9 são telas de
produção enviadas pelo dono, em resolução menor (1055×475, 1186×799, 1280×800):
foram anotadas no tamanho original, sem reescalar, com `r=15, w=3` para as setas
ficarem no mesmo peso visual das outras.

| Arquivo | Conteúdo |
|---------|----------|
| `01-setor-bandeiras.png` | Setor em português: onde ficam as três bandeiras |
| `02-setor-ingles.png` | Bandeira do inglês ativa, etiqueta *Inglês*, campo com borda destacada e *Sides* |
| `03-produto-ingles.png` | Produto: Nome e Descrição em inglês na mesma tela |
| `04-complemento-ingles.png` | Complemento *Molho verde* → *Green sauce* |
| `05-grupo-opcoes-ingles.png` | Grupo *Escolha um molho* → *Choose a sauce* |
| `06-totem-idiomas.png` | Aplicativos → Totem → Configuração → Idiomas → Habilitar tradução |
| `07-totem-iniciar-idioma.png` | Totem, tela de espera: bandeiras embaixo do **FAÇA SEU PEDIDO** (Brasil selecionado) |
| `08-totem-menu-idioma.png` | Totem em inglês: seletor no canto superior direito, `DRINKS` traduzido e `MOLHOS ADICIONAIS` sem tradução |
| `09-tablet-coca-traduzida.png` | Tablet em inglês: *Cola US* / *The drink cola*, a segunda Coca sem tradução e as bandeiras da coluna esquerda |

Padrão das setas: cada uma sai de um espaço vazio e mira a **borda** do
elemento (regra da MEMORIA-GERAL). Nas imagens do setor a bandeira fica na
beirada do modal, então o número foi para fora da janela; nas demais há espaço
branco à direita do rótulo.

## Decisões de texto

- Título em tom de busca: *"como traduzir o cardápio do tablet e do totem"*.
- O manual diz o que **não** é traduzido (preço, foto, Nome Público, sub-setor,
  cupom, ficha da cozinha, PDV) — evita a dúvida de suporte.
- Aviso sobre o **Melhorar com Inteligência Artificial**: ele reescreve a
  descrição **em português**, mesmo com a bandeira do inglês selecionada
  (`handleMelhorarDescricaoIA` grava `formData.descricao`).
- Sem afirmação sobre a tela do tablet além do que o cadastro alimenta: o
  aplicativo Android não está acessível no Cloud Agent e o painel não tem
  interruptor de idioma para o tablet.
- Não existe tradução em lote — dito no manual e transformado em roteiro
  (setores → grupos → produtos → complementos).

## Scripts

- `capturar.py` — Playwright. Etapas: `setor`, `produto`, `complemento`,
  `grupo`, `bebidas` (limpeza), `totem`. `DRY=1` fotografa sem gravar.
  A aba do cardápio **não tem campo de busca** e a lista é virtualizada: em
  Produtos é preciso clicar no setor antes de achar o item.
- `annotate.py` — setas/molduras em pixels.

## Telas do cliente (16/09/2026)

Confirmado na API antes de escrever (endpoints de detalhe, que são os únicos que
devolvem `traducao`):

| Item | ID | Português | Inglês |
|------|----|-----------|--------|
| Produto da foto do tablet | 2515399 | Coca Cola 350ml / *Coca Cola Lata 350ml* | Cola US / *The drink cola* |
| Coca sem tradução (logo abaixo, na mesma foto) | 2515308 | Coca Cola 350ml / *Coca Cola Lata 350ml* | `traducao: null` |
| Setor da foto | 213756 | Bebidas | Drinks |
| Setores sem tradução da foto do totem | 213755, 213750, 213751 | Molhos adicionais, Combos…, Burgers Avulsos… | `traducao: null` |

Ou seja: as duas fotos provam o fallback com dados reais — traduzido e não
traduzido lado a lado, na mesma tela.

Onde fica o seletor de idioma:

- **Totem** — embaixo do botão **FAÇA SEU PEDIDO** (antes de iniciar) e no
  **canto superior direito** do menu (durante o pedido).
- **Tablet** — coluna da esquerda, embaixo de *Avaliar*.

Dois detalhes anotados no manual:

- No tablet, o **título da faixa** continuou *Bebidas* (Nome Público do setor é
  `tituloWeb`, que estava `null`) enquanto a coluna de setores mostrou *Drinks*:
  o cabeçalho da lista não acompanha o idioma. Virou linha em *Problemas comuns*.
- Os textos do próprio aplicativo (*CANCEL ORDER*, *MY CART*, *MY BILL*,
  *Order*, *SEARCH*) já vêm traduzidos — não são cadastro do lojista.

## Status

Concluído — painel (imagens 1 a 6) e telas do cliente (7 a 9).
