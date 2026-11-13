# MEMORIA.md — #133 Valor fiscal por produto

## O pedido do dono

> *"estude o novo campo venda fiscal e crie um manual explicativo com exemplos."*
> *"estude o novo campo venda fiscal e crie um manual explicativo com exemplos. tudo isso
> para nosso MCP consiga ajudar os clientes nessa duvida"* — 13/11/2026.

Dois recados dentro do mesmo pedido:

1. **"com exemplos"** — o que o lojista não sabe fazer não é clicar no campo, é **a conta**.
   Daí a seção *Mais exemplos*, com seis casos e os totais fechados, e a tabela antes/depois
   da nota.
2. **"para nosso MCP"** — a página vai ser lida por máquina para responder cliente. Por isso o
   FAQ é longo e cada pergunta repete os termos que o cliente digita, inclusive os errados:
   *venda fiscal* (nome do campo na API) ao lado de *valor fiscal* (nome na tela), *brinde não
   sai na nota*, *combo na nota fiscal*, *NFC-e*. A pergunta direta com a resposta direta
   embaixo vale mais que um parágrafo bonito.

## O nome do campo

O pedido fala de *"venda fiscal"*, a tela diz **Valor fiscal** e a API diz `vendaFiscal`. O
manual usa **Valor fiscal** no corpo — é o que o cliente vê — e cita *venda fiscal* no FAQ e
no rodapé de busca, para quem procurar pelo nome técnico também achar.

## O que entrou e o que ficou fora

**Entrou:** onde o campo mora (produto e complemento), como preencher e salvar, a conta do
combo fechando com o preço pago, o *Editar em Lote* nas três etapas, seis exemplos numéricos e
o par antes/depois de como a nota passa a detalhar os itens.

**Ficou fora, de propósito:**

- **A emissão da nota.** A sandbox está em **homologação** (`nfceProd: false`) e com 0
  emissões em 240 vendas. Emitir nota é passo irreversível e, pela regra da casa, pede
  confirmação do dono. A seção *Como isso aparece na nota* é **exemplo fictício** declarado,
  no mesmo formato do #5 (reforma tributária).
- **A fórmula do ajuste proporcional.** Ela está no servidor, que não está nesta máquina. O
  manual diz o efeito — *ajusta os itens configurados proporcionalmente* — e mostra os
  centavos como aproximação declarada.
- **Grupo de opções e brinde.** Como se monta um combo com grupo marcado *Brinde* é assunto do
  manual de fundamentos do cardápio. Regra 0: imagem só entra se o leitor sair dela fazendo
  algo diferente.

## O que o código entregou e a tela não diz

- **Vazio, R$ 0,00 e negativo são a mesma coisa.** `normalizarVendaFiscal` devolve `null` para
  os três, e o teste do projeto é explícito: *"positivo é mantido, mesmo maior que a venda"*.
  Não existe valor fiscal zero — logo, não há como esconder item da nota por este campo.
- **O campo aceita valor maior que o preço de venda.** O front não barra. Quem fecha a conta é
  o servidor, e o total da nota continua sendo o que o cliente pagou. É a origem do exemplo
  *"quando a soma passa do que o cliente pagou"*.
- **A permissão é a comum de editar cardápio**, não a de preço: `readOnly={!podeEditar}`, e
  `vendaFiscalCheck` ficou fora de `PRECO_FIELDS` no lote. Quem não pode ver preço pode
  preencher valor fiscal.
- **`empresaTemFiscalAtivo` olha qualquer filial**, não a filial aberta na tela. Primeira
  pergunta para quem diz *"não acho o campo"*.
- **No complemento, o bloco *Opções avançadas* existe só por causa deste campo**
  (`{(!isComplemento || mostrarValorFiscal) && …}`). Sem fiscal ativo, o complemento não tem
  nem o bloco.
- **As listagens não devolvem `vendaFiscal`** — só o detalhe do produto. Por isso o manual não
  promete coluna nem filtro: para conferir, abre-se o produto.

## O cenário

Nada precisou ser semeado: o exemplo é um combo **real** do cardápio do sandbox, com os dois
brindes que o recurso veio resolver.

| Item | ID | Papel |
|---|---|---|
| Combo Tasty Bacon (R$ 60,00) | 2698512 | item pago |
| Batata Frita Especial One | 2698513 (complemento) | opção sem acréscimo do grupo *Escolha 1 acompanhamento* |
| Sprite 350ml | 2698520 (complemento) | opção do grupo *Escolha sua Bebida Gelada*, marcado **Brinde** |

Como se descobre isso: o grupo vem com `agregaValor: false` e `statusTraduzido: "Brinde"` em
`GET /api/produto2/cardapio/grupoOpcao/{e}/{u}/{grupoID}`, e a lista de complementos diz, em
`grupos[].descricao`, a qual grupo cada um pertence. Atenção para a pegadinha: a chave
`produtos` da resposta do grupo é a lista dos produtos **que usam** o grupo, não as opções
dele.

## As capturas

Sete imagens, 16 setas, seis em 2160x1350 e a última recortada em 1091x344.

- **O `<details>` nasce fechado.** É por isso que existem duas imagens do cadastro: sem o
  clique em *Opções avançadas*, o campo não existe na tela. Foi a primeira decisão de imagem.
- **No complemento, o *Preço de Venda* e o *Valor fiscal* não cabem na mesma foto.** Com o
  bloco aberto, o campo fica no fim de um corpo de ~870 px dentro de uma janela de ~430 px de
  altura útil, e subir a viewport para 1040 px não resolveu (a janela cresce menos que o
  formulário). A prova de que o item é brinde na mesma foto passou a ser outra: os preços de
  *Delivery* e *Presencial* **vazios**, que aparecem logo acima do bloco.
- **O rótulo do `FieldGroup` do lote não tem `htmlFor`.** Clicar no texto *Valor fiscal* não
  marca nada; é preciso clicar na caixinha — e o campo só é desenhado depois de marcada.
  `label:has-text(...)` + `preceding::button[@role='checkbox'][1]` resolve.
- **A etapa 1 do lote abre com todos os produtos marcados.** *Marcar Todos* é alterna-tudo e
  serve para zerar a seleção; cada linha depois liga no clique do próprio nome.
- **A etapa 3 é uma janela quase vazia.** Em vez de descartar a imagem, `annotate.py` ganhou
  `recorte` — frações aplicadas antes das setas, com as coordenadas dos marcadores passando a
  ser frações do recorte.

## O estado do sandbox depois

Os cinco itens tocados voltaram para `vendaFiscal = None`, que é como estavam (o estado de
partida ficou guardado em `/tmp/valor-fiscal-antes.json`): os três do exemplo, escritos pelo
cadastro, e os dois do lote (`Combo One Burger`, `Combo One Cheddar`), escritos pelo
*PROCESSAR*. O `python3 capturar.py limpar` faz isso pela própria tela, e o
`python3 capturar.py estado` confirma.
