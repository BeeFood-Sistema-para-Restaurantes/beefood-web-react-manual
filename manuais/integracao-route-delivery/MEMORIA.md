# MEMORIA.md — #129 Route Delivery (integração pela API Aberta)

## O pedido

O dono mandou o artigo público do parceiro —
`routedelivery-loja.vercel.app/ajuda/integrar-beefood.html` — e pediu: *"novo aplicativo de
entrega Route Delivery (igual Entregas Expressas, no sentido que eles que fizeram a integração e
não nós). Vamos criar um manual nosso copiando o dele + na hora de pedir a credencial ensinamos
a fazer por Aplicativos → API Aberta → Criar credencial, seguindo o fluxo mais amigável para o
cliente."*

Duas instruções, e a segunda é a que dá forma ao manual:

1. **Mesmo molde do #127.** Parceiro que fez a integração do lado dele, artigo público dele,
   trazido para o padrão da casa.
2. **O caminho da credencial muda de propósito.** No #127, criar credencial era o Passo 4,
   opcional; aqui é a Parte 1 inteira. O artigo manda criar no portal `docs.beefood.app`,
   marcando permissões e trocando o ambiente de *Sandbox* para *Produção*. Pelo painel são três
   cliques, as permissões já vêm ligadas e **a escolha de ambiente não existe** — que é
   justamente onde o artigo avisa, em caixa própria, que o lojista erra.

## A diferença de papéis em relação ao #127

No Entregas Expressas o lojista faz as três partes. Aqui **a parte do meio não é dele**: a
equipe Route Delivery é que vincula a loja no painel administrativo. Isso mudou a escrita em
três lugares:

- a abertura ganhou um parágrafo **"Quem faz cada parte"**, antes de qualquer passo;
- a Parte 2 abre dizendo, com todas as letras, que as telas são do parceiro e servem *"para você
  reconhecer o que foi feito, saber o que perguntar e combinar as escolhas"* — não para executar;
- o prompt de publicação pede que a apresentação deixe claro **onde o leitor está e quem clica**,
  porque "duas empresas" não basta quando numa delas ele não é o operador.

O par credencial → secret do webhook também virou **duas entregas de valor** ao parceiro, e o
manual fecha o ciclo: sem mandar o secret de volta, a linha da loja fica em *Falta o secret do
webhook* e a integração só funciona pela busca a cada 5 segundos.

## O que o estudo do código mudou no texto

O detalhe está no `fluxo-codigo.md`. O que importou para a escrita:

- **Criar credencial é mesmo o caminho mais amigável, e o código mostra por quê.**
  `SCOPES_PADRAO_NOVA` liga todos os recursos não marcados como *em breve*, em leitura e
  escrita, e `criar()` manda `active: true`. Os três scopes que o Route Delivery pede
  (`store:read`, `orders:read`, `orders:write`) já vêm satisfeitos — o leitor confere, não
  configura.
- **São dois diálogos, e o segundo é o que o manual precisava.** *Nova credencial adicional* →
  `CRIAR (F2)` → *Credencial criada*, com `clientId` e `clientSecret` e botão de copiar em cada
  um. É a tela que o artigo do parceiro não tem, e é ela que fecha o Passo 5.
- **O segredo não se perde**, e o rodapé do próprio diálogo diz isso: o ícone de olho revela o
  `clientSecret` depois. O artigo avisa o contrário — e está certo, para o portal.
- **A autenticação Basic é o oposto do #127.** Lá o aviso central era que os campos
  `clientId (usuário)` / `clientSecret (senha)` recebiam o usuário e a senha do parceiro. Aqui
  eles ficam **em branco**: o Route Delivery se identifica pelo *Secret do webhook*. Foi o
  trecho com maior risco de copiar errado do manual vizinho, e por isso o `fluxo-codigo.md`
  tem uma tabela de diferenças entre os dois.
- **Três eventos, não cinco.** `order_created`, `order_updated` e `order_delivery_updated`. Os
  dois de pagamento ficam desligados, e o back-end aceita qualquer subconjunto.
- **Os dois portões continuam de pé** (`API_ABERTA_ALLOWED_EMPRESAS` com quatro empresas, e
  empresa sandbox que nem vê o painel). Viraram pré-requisito e linhas da tabela de problemas.
- **`RECICLAR` fica a um clique do `CRIAR CREDENCIAL`**, logo acima dele na mesma tela. Ganhou
  seta própria na imagem 03 com o rótulo de **não clique** — num manual que manda clicar ali
  perto, apontar o botão vizinho é parte do serviço.

## As imagens: duas pontas, duas origens

Catorze tratadas, de treze puras. Oito são nossas e seis são do parceiro.

| Tratada | Origem |
|---|---|
| 01 a 05, 12 a 14 | capturadas em `beefood.app` pelo `capturar-painel.py` |
| 06 a 11 | extraídas do artigo público pelo `importar.py` |

- **As imagens do artigo estão embutidas em base64, não são arquivos.** O HTML traz cada print
  como `data:image/png;base64,…`. O `importar.py` decodifica a partir de um mapa de legenda →
  arquivo, e não baixa nada além do próprio HTML. Consequência boa: o manual não depende de o
  CDN do parceiro continuar no ar.
- **As duas "Ilustrações" do artigo foram ignoradas de propósito.** O que o artigo mostra como
  tela do *BeeFood Developers* são maquetes em HTML, sem `<img>` — campos desenhados com valores
  de exemplo. Copiar maquete de tela nossa seria o pior dos dois mundos: parece print e não é.
  Essas duas foram substituídas pelas nossas capturas reais do painel (imagens 02 a 05, 12 a 14).
- **Nada a cobrir, ao contrário do #127.** Os prints do Route Delivery só têm valores de exemplo
  (*Sua Loja*, `a1b2c3d4-0000-…-exemplo00001`). Não houve borrão em pura nenhuma.
- **`02` e `03` saem da mesma pura**, como no #127: o painel tem 1950 px com as oito permissões
  abertas, e numa imagem só o texto fica ilegível na página publicada.
- **Quatro geometrias no `annotate.py`, e cada uma tem motivo.** `painel()` e `dialogo()` vêm do
  #127. As novas são para as capturas do parceiro: `lado()` para print alto (faixa nos dois
  lados, como o painel) e `faixa()` para tira larga e rasa, em que os alvos ficam em duas linhas
  e seta horizontal atravessaria a linha inteira — por isso a etiqueta vai em cima e embaixo, e
  a seta fica vertical.
- **Quatro setas mudaram na revisão:**
  - `03` — a do `RECICLAR` vinha da direita e cruzava ~770 px de cartão vazio; passou a sair da
    faixa esquerda. O recorte também cresceu até 1880 px, para o título *Todas as credenciais*,
    que o texto cita, ficar visível.
  - `08` — a tira tem 160 px de altura útil; com faixa em cima **e** embaixo a seta virava um
    toco. Passou a chamar `annotate()` direto, com faixa só embaixo (170 px).
  - `12` — o recorte mostrava meio cartão de um webhook alheio. Termina em 512 px, logo antes do
    primeiro item da lista.
  - `14` — a ponta da seta cobria a palavra *Ativo*. O selo foi medido na pura com grade
    ampliada (pílula de x 2035 a 2100, texto de 2047 a 2088, centro em y 828) e a seta passou a
    parar em 2102, na borda direita do selo. É a regra do #126 aplicada de novo.
- **O `conferir-setas.py` ganhou um caso que o #127 não tinha.** Lá a referência a uma imagem
  anterior era sempre *"a seta N da imagem acima"*. Aqui o leitor vai e volta entre as duas
  pontas, e o texto aponta para *"a seta 1 do Passo 5"*, *"a seta 3 do Passo 10"*. O script
  passou a mapear cada imagem ao seu `### Passo N` e confere as seis citações cruzadas contra a
  imagem do passo citado.

## O cenário: o que foi mexido no sandbox, e como voltou

A conta é a **BeeFood3 - Manual** (`contato@beefood.com.br`), empresa **38311**, num BeeFood de
**produção**. Aqui houve uma decisão diferente da do #127:

- **A credencial foi criada de verdade, e apagada na mesma execução.** No #127 o diálogo entrou
  pela técnica do ensaio (abre, fotografa, cancela), porque criar era passo opcional. Aqui a
  tela *Credencial criada* **é** o Passo 5, e ela não existe sem criar. Então o
  `capturar-painel.py` cria, fotografa, e depois acha a linha pelo `clientId` que o diálogo
  mostrou e clica em **EXCLUIR**. A última coisa que ele imprime é a conferência:
  `credencial da foto ainda existe? 0`.
- **Logo, o `clientSecret` visível na imagem 05 é de uma credencial que não existe mais**
  (`clientId 254d9595-f0a8-460e-a47c-f4abce089fee`). Fica versionado como qualquer valor de
  sandbox.
- **O webhook também foi criado e apagado na mesma execução**, com URL de exemplo
  (`https://routedelivery.vercel.app/api/beefood/webhook/sua-loja-exemplo`). Nenhum pedido foi
  feito na janela em que ele existiu.
- **O sandbox já tinha dois webhooks alheios**, de um teste de outra pessoa
  (`…trycloudflare.com/hook`, os dois *Desativados*). Por isso o script **não** pode conferir
  *"a lista voltou a Nenhum webhook cadastrado"* como o do #127 faz: ele confere que **a minha
  URL** saiu. E é por isso que a imagem 12 precisou de recorte curto e que o fundo da imagem 13
  mostra dois cartões desfocados que não são deste manual.

Estado em que o sandbox ficou: igual ao de antes. Uma credencial principal e duas adicionais, e
os mesmos dois webhooks alheios desativados.

## Os arquivos desta pasta

| Arquivo | Para que serve |
|---|---|
| `integracao-route-delivery.md` | o manual |
| `fluxo-codigo.md` | o que a tela faz de verdade, lido no código (uso interno) |
| `texto-documentation.ia.md` | o prompt de publicação |
| `capturar-painel.py` | as sete capturas do BeeFood (e o desfazer da credencial e do webhook) |
| `importar.py` | as seis capturas do artigo do parceiro, decodificadas do base64 do HTML |
| `annotate.py` | setas e etiquetas das catorze imagens |
| `conferir-setas.py` | confere se o texto e as setas falam a mesma coisa |

Para refazer tudo, nesta ordem: `importar.py` → `capturar-painel.py` → `annotate.py` →
`conferir-setas.py`.

## O que ficou para depois

- **A tela Operação do parceiro não tem print no artigo.** A Parte 4 é a única sem imagem, e por
  isso é curta e textual. Se o parceiro publicar um print dela, vale uma imagem 15.
- **O ciclo completo não foi observado de ponta a ponta.** Nenhum pedido foi criado para ver a
  saída do entregador virar *despachado* e a finalização virar *entregue*: isso exigiria conta
  ativa no Route Delivery e entregador de verdade. O manual atribui essas afirmações ao
  parceiro.
- **A aba Avançado continua de fora**, pelo mesmo motivo do #127: *Aplicativos conectados* é o
  caminho OAuth, que nenhum destes dois parceiros usa hoje. Ela merece manual próprio, porque
  vale para qualquer parceiro.
- **Os dois webhooks alheios no sandbox** atrapalham qualquer captura futura da aba Webhooks.
  Apagá-los é ação destrutiva em conta compartilhada, então ficaram. Quem for fotografar essa
  aba de novo precisa recortar antes da lista, como a imagem 12 faz.
