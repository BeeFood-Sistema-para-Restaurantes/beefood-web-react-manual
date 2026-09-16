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

**Pendente:** as telas do **Cardápio Digital no Tablet** e do **Totem** vistas
pelo cliente. O dono vai enviar as imagens; entram na seção 7 (*Como o cliente
vê*), que hoje é só texto — nenhuma imagem inexistente é referenciada, para não
quebrar o `validar-imagens.py`.

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

## Imagens (6, todas 2160×1350)

| Arquivo | Conteúdo |
|---------|----------|
| `01-setor-bandeiras.png` | Setor em português: onde ficam as três bandeiras |
| `02-setor-ingles.png` | Bandeira do inglês ativa, etiqueta *Inglês*, campo com borda destacada e *Sides* |
| `03-produto-ingles.png` | Produto: Nome e Descrição em inglês na mesma tela |
| `04-complemento-ingles.png` | Complemento *Molho verde* → *Green sauce* |
| `05-grupo-opcoes-ingles.png` | Grupo *Escolha um molho* → *Choose a sauce* |
| `06-totem-idiomas.png` | Aplicativos → Totem → Configuração → Idiomas → Habilitar tradução |

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

## Status

Concluído (parte do painel) — aguardando as imagens do tablet e do totem.
