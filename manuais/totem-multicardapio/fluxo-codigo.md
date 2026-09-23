# fluxo-codigo.md — #124 Mais de um cardápio no totem

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `totem-multicardapio.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Leitura do `beefood-web-react` e do bundle do totem em 22/09/2026, mais o
**pedido misto real** feito no aparelho no mesmo dia (venda 1168, pedido 73).

Cenário: empresa **38311**, totem na filial **39202** (`BeeFood3 - Manual`), e o
cardápio adicional na filial **50502** (`BeeFood3 - Manual Sushi`), criado pelo
dono logo antes da sessão. Totem `v1.170926.1226`.

## O painel: uma aba, uma chave, nenhum Salvar

`src/components/tef/totem-cardapios/TotemCardapiosTab.tsx` e
`src/hooks/useTotemCardapios.ts`.

| O que a tela faz | Onde |
|---|---|
| Lê os cardápios já ligados | `GET /api/totem2/configuracao/cardapios/{empresaID}/{filialID}/{usuarioID}` → `{ aaCardapios: [] }` |
| Grava **no clique** da chave | `POST /api/totem2/configuracao/cardapios` com `aaCardapios` inteiro + `log: { aaCardapios: anterior }`; sucesso mostra o toast *Cardápios salvos* |
| Reverte quando a API falha | `persist()` devolve `setAaCardapios(prev)` e mostra *Erro ao salvar cardápios* |

A lista é `filiais` (do `FiliaisContext`) **menos** a filial atual. Três estados
por linha, todos visíveis na captura 01:

- **principal** → `Badge` *Principal*, switch `checked` e `disabled`;
- **normal** → switch livre, `checked = aaCardapios.some(c => c.filialID === f.filialID)`;
- **sem cardápio** (`f.cardapioAdicional === false`) → `opacity-60`, logo em
  `grayscale`, `StatusBadge` *Cardápio Digital não habilitado* e switch travado.

Sem outra filial: *"Nenhum outro cardápio disponível."*

**Onde o cardápio adicional nasce** — `src/components/plano-novo/AdicionaisPorFilialManager.tsx`,
dentro do checkout do plano: *"Crie um novo cardápio ou habilite em um cardápio
existente"*, nos modos **Novo cardápio** (só o nome) e **Cardápio existente**
(escolhe filial não-matriz sem `cardapioAdicional`). Não se cria pela tela do
totem — daí o pré-requisito do manual falar de plano e suporte.

## O seletor de cardápios do painel

`src/components/CardapioSelector.tsx`, usado em `Cardapio.tsx` (aba Produtos),
`CardapioDigital.tsx`, `CardapioDigitalTablet.tsx`, `NFe`, `NFCe` e outras.

- `if (filiais.length <= 1) return null` — **o seletor só existe com dois
  cardápios**, e é por isso que a captura 07 não tinha como existir antes.
- Até **5** cardápios são chips de logotipo com bolinha de status
  (aberto/fechado) e tooltip com o `nomeFantasia`; acima de 5 vira combobox.
- `cardapioMode` deixa em `grayscale` e `cursor-not-allowed` a filial com
  `cardapioAdicional === false`, e o clique dispara o toast *Cardápio Digital não
  habilitado para esta filial*.
- A faixa **EDITANDO CARDÁPIO + nomeFantasia** de `CardapioDigital.tsx` também é
  condicionada a `filiais.length > 1`.

## O que decide o que entra em cada cardápio

| Cadastro | Campo | Arquivo |
|---|---|---|
| Setor | **Cardápios** (multi-seleção): *Todos os cardápios* / *N cardápios selecionados* / *Nenhum cardápio selecionado* | `src/components/ModalEditarSetor.tsx` |
| Produto | aba **Cardápios**: uma linha por cardápio com **Ativo** e, dentro dela, **Delivery** (+preço), **Presencial** (+preço), **Totem** (só chave) e **Promoção** (+preço) | `src/components/ModalEditarProduto.tsx` |

Duas consequências que viraram texto no manual: o mesmo produto pode ter **preço
diferente por cardápio**, e a chave **Totem** é **por cardápio** — dá para ter o
produto no totem de um e fora do outro. Linha desligada mostra *Produto inativo
para este cardápio* com o botão **Ativar**.

Os tooltips do cartão de produto na listagem confirmam isso em produção: `Ativo`,
`Delivery ativo`, `Presencial ativo`, `Totem ativo`, `Controla Estoque`.

## O aparelho

`GET /api/totem2/filial/{empresa}/{filial}/0` passa a devolver, no mesmo objeto
de configuração:

```json
"aaCardapios": [{"filialID": 50502, "nomeFantasia": "BeeFood3 - Manual Sushi",
                 "logotipoS3Link": ".../055285823.png", "corPrimaria": null}]
```

O bundle (`assets/index-BJK72UaC.js`) monta a lista em `UT()`: o principal
(`filialID` da URL, nome = `razaoSocial`) mais um item por `aaCardapios`,
descartando entrada sem `filialID` e a que repete o principal. Para **cada**
cardápio ele baixa, em sequência:

```
GET /totem2/setores/{empresa}/{filialID}/0
GET /totem2/produtos/{empresa}/{filialID}/0
```

Medido no sandbox: principal **7 setores / 67 produtos**, Sushi **12 / 98**.

| Comportamento | Regra no bundle |
|---|---|
| A tela de escolha só aparece com 2+ cardápios | no toque em *FAÇA SEU PEDIDO*: `if (menus.length > 1) abre o seletor; else vai para /menu` |
| **Ver todos os cardápios** | `products` = concatenação (67 + 98 = 165); `sectors` = união **deduplicada por `produtoSetorID`** |
| Setor repetido some da soma | 7 + 12 = 19, a tela mostra **17**: `213754 Sobremesas` e `213756 Bebidas` são o mesmo registro nos dois cardápios |
| Ordem da coluna | a do `concat`, com o cardápio adicional primeiro |
| Selo **INDISPONÍVEL** | `!menu.hasLoaded && !!menu.error` — o aparelho tentou baixar e falhou; cartão fica `cursor: not-allowed` |

**Nome na tela do cliente.** O painel lista a linha pelo `nomeFantasia` do
`FiliaisContext` (na captura 01, *Sushi*); o aparelho usa o `nomeFantasia` que
vem em `aaCardapios` da API do totem (*BeeFood3 - Manual Sushi*). Os dois podem
divergir — virou nota na seção 4 e linha nos problemas comuns.

### A regra da foto do setor — e a correção do #121

No trilho de setores: `const p = setores.some(s => !!s.s3Link)`.

- `p === false` → coluna de **texto**;
- `p === true` → coluna de **miniatura**, com `src = setor.s3Link || logotipoDaLoja`
  (o logotipo é `companyImages AALOGO`, com fallback em `config.logotipoS3Link`).

Logo, **setor sem foto no meio de setores com foto cai no logotipo da loja**, não
em espaço vazio. O #121 dizia *"fica com um espaço vazio no lugar da miniatura"*
e foi corrigido nesta sessão. A prova está na captura 03: os setores próprios do
Sushi não têm foto e saem todos com o mesmo logotipo.

### Textos do aparelho (i18n pt-BR)

| Chave | Texto |
|---|---|
| `escolhaCardapio` | Escolha um cardápio |
| `verTodosCardapios` | Ver todos os cardápios |
| `produtosDeNCardapios` | Produtos de {{count}} cardápios em uma só tela |
| `cardapioAtual` / `trocar` | Cardápio atual / Trocar |
| `cardapioPrincipal` / `selecionado` | Cardápio principal / Selecionado |
| `todosCardapios` / `mais` | Todos os cardápios / Mais |
| `indisponivel` | Indisponível |
| `nenhumSetor` / `valideCardapioAtivo` | Nenhum setor encontrado / Valide se o cardápio presencial está ativo. |

Tudo traduzido para **en** e **es**: o multicardápio respeita as bandeiras do
#100.

## O pedido é um só

`POST totem2/pedido/processar` (função `JC` do bundle):

```
filialID       = centralizarPedidoMatriz ? filialIDMatriz : filialID da URL
filialIDOrigem = centralizarPedidoMatriz ? filialID da URL : 0
produtos[]     = { produtoID, qtd, valorTotal, custo, taxa, custoComposicao,
                   obs, descricao, composicoes }
```

**Não existe `filialID` por item.** Item de cardápio adicional entra na mesma
venda, na loja do totem. No sandbox `centralizarPedidoMatriz = false` e
`filialIDMatriz = 39202`. Os `produtoID` não se repetem entre os dois cardápios
(67 e 98 IDs, 0 em comum), então não há ambiguidade no payload.

## O pedido misto real (22/09/2026)

Montado com a técnica do ensaio: o roteiro rodou inteiro até a tela de pagamento
sem confirmar, e só depois repetiu com `VALENDO=1`.

| Dado | Valor |
|------|-------|
| Venda / Pedido | **1168 / 73** |
| Tipo / Origem | Consumo Local / **AutoAtendimento** |
| Item do cardápio adicional | Temaki de Atum, 1x **R$ 35,00** |
| Item do cardápio principal | One Burger, 1x **R$ 28,00** |
| Forma | Dinheiro, **Não pago** |
| Desconto | 1% da forma *Dinheiro* |
| Valor total | R$ 63,00 → **R$ 62,37** |
| Mesa | 14 |
| Loja da venda | **BeeFood3 - Manual** (a do totem), não a do sushi |

O desconto da forma incidiu no total **misto** — é a evidência de que o pedido é
tratado como um só, e não como duas vendas somadas na tela.

## Fora de escopo

- **Captura da aba Cardápios do produto.** A listagem de `/cardapio` com dois
  cardápios tem produto de nome repetido nos dois e o modal não abriu por clique
  automatizado; a seção 7 do manual descreve os campos sem foto. Fica como
  material do futuro manual do **Cardápio Adicional**.
- **Cardápio adicional fechado** (fora do horário) no seletor do aparelho: não
  testado. O manual só descreve o que o próprio aparelho escreve na tela.
- **Contratação do Cardápio Adicional** pelo checkout do plano: o manual manda
  para o plano/suporte e não fotografa a compra.
