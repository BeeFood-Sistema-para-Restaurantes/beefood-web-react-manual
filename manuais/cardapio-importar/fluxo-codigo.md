# fluxo-codigo.md — #130 importar cardápio (uso interno, NÃO publicar)

O que cada caminho faz de verdade, lido no `beefood-web-react` em `78eeddd`. São **quatro**
caminhos independentes, escritos em épocas diferentes, e nada é compartilhado entre eles — nem
componente, nem rota, nem convenção de resposta. Daí o manual ter de ensinar quatro telas em vez
de uma com quatro abas.

Um deles, a digitalização por imagem, **não está neste repositório**: é um aplicativo separado
carregado em `iframe`. Tudo o que o manual afirma sobre ele saiu da observação do produto no ar,
como no #125.

## Onde mora cada caminho

| Caminho | Rota | Permissão | Arquivos |
|---|---|---|---|
| Copiar do iFood | `/copiar-ifood` | `copiarIFood` (submenu `cardapio`) | `src/pages/CopiarIFood.tsx`, `src/components/cardapio/CardapioCopiarIFoodTab.tsx`, `ModalImportarIFood.tsx`, `src/hooks/useCopiarIFood.ts` |
| Copiar de Imagem | `/copiar-imagem` | `copiarImagem` (submenu `cardapio`) | `src/pages/CopiarImagem.tsx` — só a moldura; o produto é `foto-cardapio.beefood.com.br` |
| Planilha Excel | modal em `/cardapio` | a do próprio Cardápio | `src/components/cardapio/ModalImportarProdutosExcel.tsx` |
| Clonar e importar | `/clonagem` | `empresa` (submenu `configuracao`) | `src/pages/Clonagem.tsx`, `src/components/clonagem/ClonarCardapioForm.tsx`, `src/hooks/useClonagem.ts` |

## Caminho 1 — Copiar do iFood

**A validação da URL é um regex, e as mensagens de erro são quatro.** Vale a pena citá-las no
manual exatamente como a tela as mostra, porque é o erro mais provável do leitor:

```ts
const IFOOD_URL_REGEX = /^https:\/\/www\.ifood\.com\.br\/delivery\/[\w-]+\/[\w-]+\/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
```

`normalizeIfoodUrl` tira espaço, query string, hash e barra final, e aceita link sem protocolo
ou sem `www` — por isso o manual pode dizer que colar o endereço da barra do navegador funciona
mesmo com `?utm_...` no fim. O que **não** passa é link de item, de busca ou do aplicativo, que
não tem o UUID no fim.

**O campo se preenche sozinho.** Ao abrir, o modal lê a área de transferência
(`navigator.clipboard.readText()`); se o conteúdo passa no regex, preenche e mostra *URL do iFood
detectada* por dez segundos. Isso virou frase do Passo 2, porque o leitor que copiou o link antes
de abrir a tela vai encontrar o campo cheio e precisa saber que é esperado.

**O Cardápio Destino só vem preenchido com uma filial:**
`setFilialID(filiais.length === 1 ? String(filiais[0].filialID) : '')`, e o `CONFIRMAR` fica
desabilitado sem filial escolhida.

**Os estados do cartão, que são a espinha do manual.** `getStatusDisplay()` traduz o status da
API em selo:

| status da API | selo |
|---|---|
| `queued` | *Na fila — posição N*, ou *Próximo na fila…* quando `queue_position === 1` |
| `processing_menu` | *Extraindo cardápio…* |
| `processing_products` / `awaiting_options` | uma das 14 frases rotativas (*Processando setores…*, *Processando fotos…*) |
| `done` com `importado === 1` | **Concluído** |
| `done` sem `importado` | *Finalizando importação…* |
| `error` | *Erro na importação*, com *Ver detalhes do erro*; ou *Cancelado*, quando a mensagem é `Cancelado pelo usuário` |

Três consequências para o texto:

- **A frase rotativa não é etapa.** Ela gira a cada 10 s num `setInterval` sobre uma lista fixa, e
  é a mesma para todos os cartões em processamento. O manual diz, com todas as letras, que o que
  mede andamento é `processed_items/total_items` e a barra.
- **`done` sozinho não basta.** O selo verde só aparece com `importado === 1`; por isso o Passo 5
  manda esperar o *Concluído* antes de ir conferir o cardápio, e a tabela de problemas tem a
  linha do *Finalizando importação…*.
- **O Cancelar existe nos quatro estados ativos** (`queued`, `processing_menu`,
  `processing_products`, `awaiting_options`) e passa por `ConfirmationDialog`. Depois do
  Concluído ele desaparece — não há desfazer, e isso está na FAQ.

**A tela se atualiza sozinha:** polling de **12 s** enquanto `hasActiveImportation`, 30 s fora
disso. O comentário do código ainda diz "5s when active", e o valor é 12000 — o manual não cita
número, só diz que não precisa recarregar.

**Confete em dois momentos:** ao criar a importação e ao detectar a conclusão
(`fireConfetti()`, 2,5 s), mais um anel verde de 3 s no cartão (`recentlyCompleted`). É enfeite,
e no manual entrou como uma frase só, para o leitor não achar que clicou em algo errado.

**O convite da loja nova** é o `useIfoodOnboard`: com `qtdProdutos < 10` a empresa vê o onboard;
com `>= 10` ele nunca mais aparece (`beefood_ifood_has_products` no `localStorage`). Virou a nota
do Passo 1. O mesmo hook obedece aos dois interruptores de ambiente.

**Dois interruptores de ambiente**, hoje os dois `false` em `src/lib/environment.ts`:

- `DISABLE_IFOOD_IMPORT` — **tira o item do menu** e a rota do `App.tsx`;
- `IFOOD_IMPORT_MANUTENCAO` — mantém o menu e troca a tela por `CopiarIFoodManutencao`.

Por isso a tabela de problemas não diz apenas "confira a permissão": o item pode sumir, ou a tela
pode avisar manutenção, sem que o leitor tenha feito nada.

## Caminho 2 — Copiar de Imagem

`CopiarImagem.tsx` é moldura, e isso é o fato mais importante aqui:

```tsx
const iframeUrl = `https://foto-cardapio.beefood.com.br/?empresaID=${userData.empresaID}&filialID=${selectedFilial.filialID}`;
```

O que o painel controla:

- **escolha do cardápio** antes de carregar o `iframe` (`FilialSelectorModal`), pulada quando a
  empresa tem uma filial só;
- o **cabeçalho** com o nome do cardápio e o botão **Editar**, que passa por um
  `ConfirmationDialog` — *"Trocar cardápio — Os dados da importação serão perdidos, tem certeza?"*
  Virou a última nota do Caminho 2;
- um `setTimeout` de 8 s que libera o overlay *Carregando importação…* caso o `onLoad` do iframe
  não dispare.

Todo o resto — os três passos, a leitura por IA, o Assistente do Cardápio, os botões
Copiar/baixar/Excel, o diálogo *Confirmar envio*, os cinco cartões do resultado — é do aplicativo
de dentro, e foi documentado **por observação**: formatos e limite (PNG, JPG, WEBP, PDF, 10 MB
cada, múltiplos arquivos), o placeholder do campo de instruções, o texto do diálogo e os rótulos
dos cartões saíram da tela, não de código deste repositório.

Medições da captura, que sustentam o que o manual promete: a extração de um cardápio de 6 itens
e 2 categorias terminou em **10 a 15 s**; o assistente respondeu em **cerca de 5 s**; e a
correção de preço feita no assistente (*R$ 6,50 → R$ 7,50*) **chegou ao cadastro** — o produto
`Café Expresso` está com `venda: 7.5` na API depois do cadastro. É isso que autoriza a frase "o
que você corrige aqui é o que entra".

## Caminho 3 — Planilha Excel

Mesmo componente para produto e para complemento (`isComplemento`), em quatro passos:
*Selecione o arquivo* → *Mapeamento de colunas* → *Importando…* → *Resultado*.

**O template é gerado no navegador**, não baixado do servidor:

```ts
const headers = isComplemento
  ? ['Descrição', 'Código', 'Preço Venda', ... 'NCM', 'CEST']
  : ['Setor', 'Descrição', 'Código', ... 'NCM', 'CEST'];
```

Daí a tabela de colunas do manual sair igual à do arquivo: ela é a lista acima, e o de
complementos é o mesmo sem `Setor`.

**O mapeamento automático tem dois estágios:** `FIELD_ALIASES` (nome exato normalizado) e, se
falhar, `PARTIAL_KEYWORDS` (palavra contida). Um campo do sistema só aceita uma coluna
(`disabled={usedFields.includes(...)}`), e `— Ignorar —` descarta. `IMPORTAR` fica desabilitado
com `mappedFieldsCount === 0`.

**Só `descricao` é obrigatória.** `isRowValid()` olha apenas a coluna mapeada em `descricao`, e o
aviso amarelo diz o mesmo. `venda` e `custo` passam por `parseFloat` com troca de vírgula por
ponto; `ncm` e `cest` perdem tudo o que não é dígito — é aí que nasce o conselho de formatar a
coluna como texto, porque o zero à esquerda se perde **no Excel**, antes de chegar aqui.

**Envio em blocos de 50** para `POST /api/produto2/cardapio/importar`, com a resposta item a item
(`resultado` / `msg`) alimentando a grade. O `CANCELAR` do passo 3 liga `abortRef`, que só
impede os blocos **seguintes**: o que já foi gravado fica, e o resto vira *Cancelado*. Essa é a
nota final do Caminho 3.

**Nada confere duplicata.** O payload não leva id, e o back-end cadastra: importar duas vezes
cria duas vezes. Vale para os quatro caminhos, e é o aviso que abre o manual.

**Um setor novo é criado pela importação.** Verificado: antes da planilha o sandbox tinha 10
setores; depois das cinco linhas com `Setor = Porções`, 11, com `produtoSetorID: 228309`
chamado *Porções*. É o que autoriza a resposta "o setor da planilha precisa existir antes? Não".

## Caminho 4 — Clonar e importar

Duas chamadas, em `useClonagem.ts`:

- `POST /api/cloneUtils2/origem/validar` com `{ empresaID, usuarioID, usuario, senha }` →
  devolve `origem.resumo` (setores, produtos, grupos, insumos), `destinoPopulado` e
  `destinoJaPopulado`. É a prévia do Passo 16.
- `POST /api/cloneUtils2/cardapio/clonar` com `{ origem: { usuario, senha }, incluirImpostos,
  forcar }`.

O que o formulário garante, e que virou texto:

- **a credencial é da empresa de origem, e não é salva** — o próprio subtítulo diz *"As
  credenciais não ficam salvas"*, e `executar()` faz `setCred(null)` no sucesso;
- **o aviso de duplicação é da tela**, com os números do destino, quando `destinoJaPopulado`;
- **dois diálogos em sequência:** `Copiar cadastro` / `COPIAR` sempre; e, se a API responder
  **409 com `permiteForcar`**, o segundo — *Copiar mesmo assim?* / `COPIAR MESMO ASSIM`;
- **saída bloqueada durante a cópia:** `beforeunload` enquanto `clonando`, e as abas desabilitadas
  pelo `onOcupadoChange`. Virou o "não feche a página" do Passo 17;
- **impostos são opt-in** (`incluirImpostos`, desmarcado), e o resultado imprime *Impostos dos
  produtos: copiados / não copiados*.

**A própria empresa não serve de origem** — verificado contra a API, não deduzido:
`origem/validar` com as credenciais do próprio sandbox responde
`422 {"resultado": false, "mensagem": "A empresa de origem é a mesma da empresa atual."}`. O
subtítulo da página (*"ou entre cardápios desta empresa"*) se refere às **outras abas**: é
`clonarAreaEntrega` que aceita `filialIDOrigem`/`filialIDDestino` com `origem: null`, ou seja,
cópia entre cardápios da mesma empresa. O manual diz isso em vez de repetir o subtítulo.

## O fenômeno dos produtos duplicados, e por que ele entrou no manual

A importação do iFood criou **84 produtos**, dos quais **53** aparecem na lista de produtos, com
**42 nomes distintos** e **11 pares repetidos**. Cruzando a lista com
`GET /datasnap/rest/produto2/cardapio/grupoOpcao/opcoes/{empresaID}/{usuarioID}/0`, em **todos os
11 pares** exatamente um dos dois cadastros está sendo usado como **opção de grupo** e o outro
não; em 7 deles um dos dois carrega `combo: True`. Os dois também diferem no `s3Link` (um ainda
aponta para `static-images.ifood.com.br`, o outro já para o bucket da casa).

Ou seja: não é defeito da importação, é o item avulso e o item-dentro-do-combo. A evidência está
em `/opt/cursor/artifacts/evidencia-duplicados-combo-130.log`. Sem essa conferência, o manual
teria de escolher entre ignorar o que o leitor vai ver na tela ou mandá-lo apagar o repetido — e
apagar o cadastro errado deixa o combo sem opção.

## O que ficou de fora do manual, de propósito

- **As quatro abas da tela de clonagem.** Só a do cardápio é assunto aqui; *Área de entrega*,
  *Clientes* e *Zona de risco* aparecem como "onde continuar". A Zona de risco em especial tem
  exclusão em massa, e manual de importação não é lugar para ela.
- **O `Preview` das cinco primeiras linhas** do passo 2 do Excel. Ele fica abaixo da tabela de
  mapeamento, fora da captura, e está descrito em uma frase — fotografá-lo pediria rolar o modal
  e repetir a imagem.
- **A escolha de cardápio** nos caminhos 1 e 2 quando a empresa tem várias filiais. O sandbox tem
  uma só, então o modal `FilialSelectorModal` não aparece em captura nenhuma; está no texto, sem
  imagem, porque forjar duas filiais mudaria o cenário das outras dezessete fotos.
- **Produtos criados como opção** (os 84 − 53). Eles existem no cadastro e não têm tela própria na
  lista de produtos; o manual os explica na seção *Depois de importar*, sem foto.
