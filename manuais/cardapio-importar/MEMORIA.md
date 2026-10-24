# MEMORIA.md — #130 Importar cardápio (os quatro caminhos)

## O pedido, em duas etapas

O dono pediu primeiro o **estudo**: *"vamos criar um manual de importação de cardápio, dando as
possibilidades que sistema traz hoje. estude e me traga como seria o manual. não faça ainda."*
A proposta foi um manual **único**, com os quatro caminhos e uma tabela de decisão no alto —
aprovada na mensagem seguinte, que trouxe também a autorização que faltava:

> *"limpei o cardápio da empresa de testes e o copiar do iFood também. tudo limpo. sendo assim,
    10|> pode copiar o iFood do One Stand Burger nosso cliente base […] pode simular todas as outras
> importações sem medo. não precisa excluir depois. sendo assim, comece pelo copiar do iFood, o
> cardápio vai ser criado 100%. depois complemente com outras importações pra testar (iFood o
> mais importante)."*

Isso mudou a natureza do trabalho. **Este é o primeiro manual da casa em que a captura cria dado
de verdade e o deixa lá.** Nos anteriores a regra era a técnica do ensaio ou criar-e-apagar
(#127, #129). Aqui o dono zerou o cenário de propósito e pediu o oposto: importar para valer, nos
quatro caminhos, e deixar o resultado no sandbox.

    20|## Por que um manual só, e não quatro

Os quatro caminhos não compartilham nada no código — rota, componente e convenção de resposta são
diferentes em cada um. A tentação era um manual por caminho. O que decidiu pelo manual único foi
o leitor: ele chega sabendo **o que tem** (loja no iFood, cardápio no papel, planilha, outra
empresa) e não sabendo **o nome da tela**. Quatro páginas o obrigariam a escolher antes de
entender, e a decisão é metade do valor da página.

Daí a estrutura: tabela de decisão antes de qualquer passo, e os caminhos na ordem em que fazem
sentido serem usados — o iFood primeiro, porque monta o cardápio inteiro, e os outros três como
    30|complemento. As capturas seguem essa mesma ordem, e as imagens 06 e 07 já mostram o cardápio
cheio porque foram tiradas depois da importação do iFood.

## O que o estudo do código mudou no texto

O detalhe está no `fluxo-codigo.md`. O que pesou na escrita:

- **Os estados do cartão do iFood são a espinha do Caminho 1.** `getStatusDisplay()` traduz seis
  situações em selo, e duas delas confundem: a mensagem que **gira** a cada dez segundos (catorze
  frases fixas, iguais para todos os cartões) e o `done` **sem** `importado`, que mostra
  *Finalizando importação…*. O manual diz que o andamento de verdade é o contador, e que o selo
    40|  que libera o leitor é o verde **Concluído**.
- **A validação da URL tem quatro mensagens de erro**, e elas entraram no texto como a tela as
  mostra. É o erro mais provável do leitor — link de item, de busca ou do aplicativo não tem o
  UUID no fim.
- **O campo da URL se preenche sozinho** a partir da área de transferência. Sem avisar, o leitor
  acha que o sistema adivinhou algo.
- **Dois interruptores de ambiente** (`DISABLE_IFOOD_IMPORT`, `IFOOD_IMPORT_MANUTENCAO`) podem
  tirar o item do menu ou trocar a tela por um aviso de manutenção. Por isso a tabela de
  problemas não diz só "confira a permissão".
- **No Excel, só o nome é obrigatório**, e o aviso do NCM/CEST como texto é da própria tela. O
    50|  template é gerado no navegador, então a tabela de colunas do manual é exatamente a lista do
  código.
- **Na clonagem, a própria empresa não serve de origem** — e o subtítulo da tela sugere o
  contrário. O manual explica a diferença em vez de repetir o subtítulo.

## A digitalização por imagem é outro aplicativo

`CopiarImagem.tsx` é só moldura: um `iframe` para
`https://foto-cardapio.beefood.com.br/?empresaID=…&filialID=…`. O código do produto **não está**
no `beefood-web-react`, mesma situação do cardápio público no #125. Tudo o que o manual afirma
sobre os três passos, o assistente e os cartões de resultado saiu da **observação da tela no ar**.
    60|
O painel controla três coisas, e as três estão no texto: a escolha do cardápio antes de carregar o
iframe, o botão **Editar** com o aviso *"Os dados da importação serão perdidos, tem certeza?"*, e
o overlay de carregamento.

## As imagens: dezoito, de quatro telas diferentes

| Tratadas | Caminho | Script |
|---|---|---|
| 01 a 05 | Copiar do iFood | `capturar-ifood.py` |
| 06 e 07 | o cardápio pronto | `capturar-cardapio-pronto.py` |
    70|| 08 a 12 | Copiar de Imagem | `capturar-digitalizar.py` |
| 13 a 15 | planilha Excel | `capturar-excel.py` |
| 16 a 18 | Clonar e importar | `capturar-clonagem.py` |

- **A fila e o processamento duram pouco e não voltam.** Os dois estados aparecem por alguns
  segundos e seguem para o próximo. O `capturar-ifood.py` fotografa a cada quatro segundos
  durante a importação inteira, grava os candidatos em `/tmp/cap-ifood/` nomeados pelo estado que
  a API devolveu, e imprime o andamento de cada rodada. Depois se escolhe, com calma, o melhor
  print de cada estado — 23 candidatos para três puras.
- **Nenhuma geometria especial no `annotate.py`, e isso é escolha.** As quatro telas são de
  largura cheia e têm área vazia dentro da própria captura, então a etiqueta cabe sem recorte e
    80|  sem faixa montada em volta. Faixa e recorte existem para painel lateral e tira de celular.
- **Duas imagens entram sem seta**, por `passthrough()`: a lista de produtos e a de grupos de
  opção. São a prova do resultado, são densas, e não há nada para o leitor clicar nelas.
- **O cardápio digitalizado é fictício, desenhado pelo próprio script.** O
  `capturar-digitalizar.py` monta um PNG de 1000x1300 — *CANTINHO DO CAFÉ*, duas categorias, seis
  itens com preço e descrição. Três motivos: não tem dado de ninguém, o resultado da extração é
  previsível (sabe-se de antemão o que a IA deveria achar) e o script não depende de arquivo
  solto numa pasta.
- **A planilha do Caminho 3 sai do template de verdade**, baixado pelo próprio botão da tela com
  `expect_download()` e preenchido com `openpyxl`. Se um dia o template mudar, o script acusa.
    90|- **A revisão mexeu em onze das dezoito imagens**, sempre por ponta cobrindo texto ou por
  colisão de etiqueta. As duas que valem registro:
  - `16` — a etiqueta 1 ficou **escondida embaixo da 3**: as duas caíram em x 0,190, e numa folha
    de contato isso não se vê. Ela foi para dentro da barra lateral, no vão abaixo do último item
    do menu, apontando para cima.
  - `09` — a etiqueta 2 foi para o vão do cabeçalho depois de pousar sobre o texto do passo
    *Enviar arquivo*. É o segundo caso de etiqueta movida **duas vezes** no mesmo manual: corrigir
    uma colisão cria outra, e só a leitura da tratada em tamanho real acusa.
- **Nada a cobrir.** A loja copiada do iFood é pública, o cardápio digitalizado é fictício e a
  planilha é de porções inventadas. Não há dado de cliente em imagem nenhuma.
   100|
## O cenário: o que ficou no sandbox

Conta **BeeFood3 - Manual** (`contato@beefood.com.br`), empresa **38311**, em **produção**. O dono
zerou o cardápio e o histórico de importações antes de autorizar; o `diagnostico.py` registrou o
ponto de partida (`qtdProdutos: 0`, nenhuma importação).

Depois das três importações reais, o sandbox tem:

| Origem | O que entrou |
|---|---|
   110|| iFood (One Stand Hamburgueria) | 8 setores, **84 produtos** (53 na lista, o resto cadastro de opção), 15 grupos de opção com 61 opções |
| digitalização | 2 setores (*Cafés*, *Doces da Casa*) e 6 produtos |
| planilha Excel | 1 setor (*Porções*, criado pela importação) e 5 produtos |
| **total** | **11 setores, 95 produtos** |

**O dono disse para não excluir.** Quem for fotografar essas telas de novo encontra o cardápio
cheio — e o estado vazio da imagem 01 **não se repete** sem limpar tudo outra vez. É o maior
custo deixado por este manual.

**A clonagem parou na confirmação, de propósito.** Confirmar copiaria os **1190 produtos** da
   120|outra empresa de teste (`beefood1`, empresa 107) por cima do cardápio em que as outras dezessete
imagens se apoiam. A autorização do dono era para "simular as importações", e a prévia do Passo
16 já mostra tudo o que o manual precisa: os números da origem, o aviso de duplicação e os dois
botões. O `capturar-clonagem.py` para no diálogo e imprime `>>> PARANDO AQUI`.

## Os dois achados que mudaram o conteúdo

1. **A própria empresa não pode ser a origem da clonagem.** A primeira execução travou esperando
   o botão *Copiar cadastro* que nunca apareceu. O diagnóstico veio da API, não da tela:
   `POST /api/cloneUtils2/origem/validar` com as credenciais do próprio sandbox responde
   `422 {"resultado": false, "mensagem": "A empresa de origem é a mesma da empresa atual."}`.
   130|   A origem passou a ser a `beefood1`, e a mensagem virou linha da tabela de problemas.
2. **Os produtos duplicados do iFood têm causa benigna.** 53 produtos na lista, 42 nomes
   distintos, 11 pares. Cruzando com
   `GET /datasnap/rest/produto2/cardapio/grupoOpcao/opcoes/{empresaID}/{usuarioID}/0`, em
   **todos** os 11 pares exatamente um dos dois cadastros é usado como **opção de grupo** e o
   outro não — é o item avulso e o item-dentro-do-combo. A evidência está em
   `/opt/cursor/artifacts/evidencia-duplicados-combo-130.log`. Sem essa conferência o manual
   teria de escolher entre ignorar o que o leitor vê na tela ou mandá-lo apagar o repetido, e
   apagar o cadastro errado deixa o combo sem opção.

   140|## Os arquivos desta pasta

| Arquivo | Para que serve |
|---|---|
| `cardapio-importar.md` | o manual |
| `fluxo-codigo.md` | o que cada caminho faz de verdade, lido no código (uso interno) |
| `texto-documentation.ia.md` | o prompt de publicação |
| `diagnostico.py` | varredura só de leitura: prova que o sandbox estava zerado antes da captura |
| `capturar-ifood.py` | o Caminho 1, em laço — o único script não idempotente |
| `capturar-cardapio-pronto.py` | as duas imagens de contexto do cardápio importado |
   150|| `capturar-digitalizar.py` | o Caminho 2, com o cardápio fictício que serve de insumo |
| `capturar-excel.py` | o Caminho 3, baixando o template de verdade |
| `capturar-clonagem.py` | o Caminho 4, parando no pedido de confirmação |
| `annotate.py` | as 50 setas das dezoito imagens |
| `conferir-setas.py` | confere se o texto e as setas falam a mesma coisa |

Para refazer tudo, nesta ordem: `diagnostico.py` → `capturar-ifood.py` →
`capturar-cardapio-pronto.py` → `capturar-digitalizar.py` → `capturar-excel.py` →
`capturar-clonagem.py` → `annotate.py` → `conferir-setas.py`. Só que **o Caminho 1 não refotografa
o estado vazio** sem alguém limpar o cardápio antes.
   160|
## O que ficou para depois

- **A escolha de cardápio quando a empresa tem várias filiais.** O `FilialSelectorModal` dos
  Caminhos 1 e 2 não aparece em captura nenhuma, porque o sandbox tem uma filial só. Está no
  texto, sem imagem: forjar uma segunda filial mudaria o cenário das outras dezessete fotos.
- **A clonagem executada até o fim.** Precisa de uma empresa de destino descartável, não desta,
  para não destruir o cardápio que as outras imagens mostram. Daria uma imagem 19 — o resultado
  com os cartões e o *Impostos dos produtos: copiados*.
- **O passo *Importando…* do Excel.** Cinco linhas importam instantaneamente, e o print saiu
  idêntico ao do *Resultado*. Ele foi descartado, e os contadores ao vivo estão descritos no
   170|  texto. Com planilha de centenas de linhas valeria a imagem.
- **As outras três abas do Clonar e importar** (*Área de entrega*, *Clientes*, *Zona de risco*).
  Cada uma merece manual próprio, e a Zona de risco em especial tem exclusão em massa — assunto
  que não cabe num manual de importação.
- **Complementos por planilha** tem a mesma tela do Caminho 3, sem a coluna *Setor*. Está
  descrito em uma frase, sem imagem própria.
