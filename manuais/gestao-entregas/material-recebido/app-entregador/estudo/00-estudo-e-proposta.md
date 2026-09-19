# Estudo e proposta — Manuais do App do Entregador

Status: **aguardando aprovação.** Nada foi criado, semeado, cancelado ou alterado em banco. As
únicas ações executadas até aqui foram **leituras**: código dos dois repositórios, histórico de
245 commits, documentação da Gestão de Entregas 2.0, dois GET na API de produção e uma captura
de tela do emulador para provar que o pipeline de screenshot funciona.

Escopo, como você corrigiu: o manual é do **app do entregador**, não da tela de Gestão de
Entregas 2.0. A tela entra só no capítulo de rota, e só para mostrar o outro lado do que o
entregador vê no celular.

---

## 1. Os sete achados que definem o plano

Cada um destes mudou alguma parte da proposta. Estão aqui antes do plano porque é deles que o
plano sai.

### 1.1 Não existe ambiente de desenvolvimento — os scripts escrevem em produção

`src/config/execSQLProc.js`, `execSQLQuery.js`, `execSQLCaixaQuery.js` e
`initMySqlServerGestaoEntrega.js` têm host, usuário e senha **fixos no código**, apontando para
os RDS de produção (`beetech-amazon-standard/notafacilb`, `beefood-entregas/entregas`,
`beefood-caixa`). O `MODE_ENV` muda o `bd_prod` de algumas rotinas de cache, **não** muda de
banco.

Isso tem um lado bom e um lado sério, e os dois são estruturais:

- **Bom:** o app no emulador aponta para `app.beetechapi.be` (2.0, login) e
  `app3.beetechapi.be` (3.0, entregas/pagamento/histórico), que leem exatamente o mesmo banco em
  que o seeder escreve. Então **não precisamos de ngrok, nem de servidor local, nem de alterar o
  app** para o cenário aparecer na tela do celular. Um `node scripts/...` na máquina e um
  pull-to-refresh no emulador bastam.
- **Sério:** todo cenário que eu criar é uma escrita em produção. A única proteção existente é a
  lista branca literal `38311 / 39202` dentro do `seed-gestao-entregas.js` e do
  `limpar-teste-01.js`. É a mesma proteção que os testes da Gestão 2.0 já usam, e é por isso que
  a §6 pede sua confirmação explícita antes do primeiro `node`.

### 1.2 O login que você passou é o `BeeFood3 - Manual`, e a filial está zerada agora

Medido, não suposto — `POST tusuario/validaBeeEntregador` com `contato@beefood.com.br` / `1q2w3e4r`:

| Campo | Valor |
|---|---|
| `usuarioID` | **88711** |
| `empresaID` | 38311 |
| `filialID` | 39202 (e uma segunda filial, **50502** — "BeeFood 3 - Subdominio") |
| `funcionarioID` | **194115** |
| `funcionarioNome` | **BeeFood3 - Manual** |
| `bloquearMultiSessaoUsuario` | false |

O `usuarioID` 88711 não estava no seu enunciado e é obrigatório em quase toda URL do app —
registro aqui porque é o campo que eu teria que adivinhar.

E `GET /api/entrega2/gestao/entregador/38311/39202/88711/194115` devolveu **`pedidos: 0`,
`rotas: 0`**. A filial está limpa; o ponto de partida é zero, e a limpeza inicial que você pediu
é, neste momento, uma conferência e não uma faxina.

**Consequência a conhecer:** o `BeeFood3 - Manual` é, segundo o
`beetech-server-node-3.0/docs/gestao-entrega-2.0/testes/01-fluxo-completo.md` §10.1,
o **único entregador da filial com telefone cadastrado** — e o número é o da própria loja de
teste. Associar uma rota a ele **enfileira WhatsApp "nova entrega"** (tipo 30) para esse número.
Não é defeito, é o fluxo real; mas se sair mensagem no WhatsApp da loja durante a produção do
manual de rota, a causa é esta.

### 1.3 A captura de tela funciona — e o caminho óbvio no PowerShell não

`adb exec-out screencap -p > arquivo.png` produz **arquivo vazio/corrompido** no PowerShell: o
`>` trata o binário como texto. O que funciona é o caminho em dois passos:

```powershell
adb shell screencap -p /sdcard/cap.png
adb pull /sdcard/cap.png destino.png
```

Validado: 242.046 bytes, imagem legível. É esta captura, tirada do emulador `Pixel_7_Pro`
(`emulator-5554`, Android 15) com o app já instalado e rodando:

> A captura de validação (`evidencias/00-captura-de-validacao.png`) **não veio no pacote**
> enviado para o repositório de manuais. O print equivalente, já do manual pronto, é o
> [`01-primeiros-passos/prints/09-entregas-vazia.png`](../01-primeiros-passos/prints/09-entregas-vazia.png).

### 1.4 O emulador está em inglês — e isso apareceria dentro do manual

Veja o diálogo da imagem acima: *"Allow BeeFood Entregador to access this device's location?"*.
O app é em português, mas **os diálogos do sistema** (permissão de localização, câmera,
notificação, o seletor de app de mapa, o compartilhamento para o WhatsApp) saem no idioma do
Android. Um manual em português com metade dos prints em inglês é um manual pela metade,
justamente no capítulo de primeiros passos, que é todo feito de diálogos do sistema.

Proposta: trocar o locale do emulador para **pt-BR** antes da primeira captura. É reversível e
não toca no app.

### 1.5 O seeder não cria pedido de marketplace nem linha de pagamento

O `seed-gestao-entregas.js` cria pedido DELIVERY manual por procedure: cliente, endereço com
coordenada em Sorocaba, 1 a 3 itens, frete, `tipopagStr` rotativo (Dinheiro / Débito / Pix /
Crédito), `troco = null`, `Observacoes = [SEED-ENTREGAS] <timestamp>`, e `situacaoDelivery` em
`PREPARO` ou `PRONTO`. Ele **não** grava `correlationId`, `nnID` nem `keetaId`, e **não** cria
linha em `_PreVendaPagamento`.

Três capítulos do manual dependem justamente do que ele não cria:

| Capítulo | Depende de | O seeder entrega? |
|---|---|---|
| Confirmar pedido iFood | `ifoodLocalizer` no payload (botão **CONFIRMAR ENTREGA IFOOD**) | **não** |
| Confirmar pedido 99Food | `nnID` no payload (botão **CONFIRMAR ENTREGA 99FOOD**) | **não** |
| Pedido já pago / pago online | linha em `_PreVendaPagamento` (estado **Pedido já pago**) | **não** |

Sem linha de pagamento, `saldo ≈ valorTotal` e `cobrarDoCliente > 0` **em todos** os pedidos
semeados — ou seja, todo pedido aparece com **INICIAR COBRANÇA**, e o cenário "pedido pago
online, só finalizar" não nasce sozinho. O que falta é um script de cenário (§4.2), não uma
mudança no app.

### 1.6 Cobrança exige caixa aberto, e não há script que abra caixa

O `beetech-server-node-3.0/docs/gestao-entrega-2.0/21-pagamento-na-rua.md`
é explícito: sem caixa aberto na filial, o `POST /gestao/entregador/pagamento` é recusado com
*"Necessário abrir um caixa para continuar o pagamento."* — e a recusa vem **antes** de qualquer
escrita. Varri `scripts/`: **nenhum script abre ou confere caixa**. A rota que abre
(`POST /caixa2/abrir`) exige JWT, que o app do entregador não tem.

Então o manual de cobrança tem um pré-requisito de ambiente que ninguém automatizou ainda, e ele
mexe em dinheiro: o pagamento de teste **entra no caixa real** da filial, com o `funcionarioID`
194115 assinando. É a decisão 2 da §6.

### 1.7 Criar rota pede JWT; o resto do que o app faz é Basic

Inventariei o `entregaRouter2.js`. A divisão é limpa e ela decide como montar o cenário de rota:

| Operação | Auth | Quem chama hoje |
|---|---|---|
| `POST /gestao/rota` (criar), `PUT .../entregador`, `.../paradas`, `.../ordem`, `.../finalizar`, `.../excluir` | **JWT** | a tela de gestão |
| `PUT /gestao/rota/:id/despachar` | Basic | **o app** (INICIAR ROTA) |
| `PUT /gestao/rota/:id/paradas/:paradaID/entregar` | Basic | app / tela |
| `GET /gestao/entregador/...`, `POST /gestao/entregador/entregar`, `formasPagamento`, `pagamentos`, `pagamento*`, `historico*`, `dispositivo*`, `presenca` | Basic | **o app** |

Traduzindo: o app consegue **despachar, entregar e cobrar** sozinho, mas **não consegue criar a
rota** — ela nasce na tela ou no despacho automático. Para o capítulo de rota eu preciso criar a
rota por fora, e há três caminhos (§4.3).

---

## 2. O que o app faz hoje, e o que é novo

Inventário completo de telas, textos literais e APIs em
[`01-o-que-o-app-faz-hoje.md`](01-o-que-o-app-faz-hoje.md). Evolução do código em
[`02-evolucao-do-app-por-commits.md`](02-evolucao-do-app-por-commits.md).

O resumo que importa para decidir o índice: **o app mudou de escopo nos últimos 20 dias de
commit.** Até 30/08 ele era "lista de entregas + código de barras + confirmar iFood". Desde
então entraram, em três ondas:

1. **30/08 — Gestão 2.0 no app:** grupos de rota com `INICIAR ROTA`, presença de três estados na
   barra superior, bottom tabs, o padrão de folha que sobe de baixo, GPS em segundo plano.
2. **11 a 14/09 — pagamento na rua:** cobrança, divisão de conta até 10 pessoas, seletor de
   forma e bandeira, troco por pessoa, confirmação antes do POST, FINALIZAR SEM COBRAR.
3. **15 a 17/09 — acabamento operacional:** histórico e itens do pedido vindos da API 3.0,
   produtos carregados sob demanda, destaque de impressão com confirmação obrigatória, endereço
   fixo no topo dos detalhes, push que recarrega a lista.

Ou seja: **quase tudo o que o manual precisa ensinar é recente e nunca foi documentado para o
usuário final.** É isso que justifica um manual por fluxo em vez de um documento único.

Duas lacunas medidas no código, que o manual não pode fingir que não existem:

- **`ModalWhatsApp` existe, está completo e não está montado em nenhuma tela.** As cinco
  mensagens prontas ("Não encontrei o endereço", "Estou a caminho", "Cheguei no local", "Tentei
  entregar, sem resposta", "Atraso na entrega") não têm porta de entrada na UI atual.
- **Keeta aparece como etiqueta, sem botão de confirmação.** iFood e 99Food têm WebView;
  Keeta só mostra `#{keetaId}` no card.

Proposta: não documentar o que não tem porta de entrada, e registrar as duas lacunas num
apêndice de "o que não existe na tela" — evita que alguém procure por meia hora.

---

## 3. Índice proposto: 13 manuais

Um manual por fluxo, na ordem em que um entregador novo encontra as coisas. Cada manual é uma
pasta com `manual.md`, os prints, e **um `.md` por print** com a explicação daquela tela, como
você pediu.

```
docs/manual-gestao-entregas-2/
├── README.md                          índice geral e como usar
├── estudo/                            este estudo (você está aqui)
├── 01-primeiros-passos/               instalar, permissões, login, o que é cada aba
├── 02-disponibilidade/                presença: online, pausa, offline, e o que o restaurante vê
├── 03-lista-de-entregas/              o cartão do pedido, atraso, "Cobrar R$", atualizar, vazio
├── 04-detalhes-da-entrega/            endereço, complemento, observações, produtos, destaque
├── 05-ver-no-mapa/                    Google Maps e Waze a partir de uma entrega
├── 06-rota/                           grupo de rota, INICIAR ROTA, ABRIR NO MAPS, ordem das paradas
│                                      + o outro lado: como a rota é criada na Gestão 2.0
├── 07-melhor-rota/                    várias entregas soltas, MELHOR ROTA GOOGLE MAPS
├── 08-codigo-de-barras/               ler o código do pedido no balcão, sucesso, já lido, erro
├── 09-pedido-ifood/                   quando aparece CONFIRMAR ENTREGA IFOOD, localizador, WebView
├── 10-pedido-99food/                  CONFIRMAR ENTREGA 99FOOD, código, WebView
├── 11-cobranca/                       INICIAR COBRANÇA, forma, bandeira, troco, confirmar, sucesso
├── 12-divisao-de-conta/               dividir entre 2 a 10 pessoas, forma por pessoa, troco por pessoa
├── 13-finalizar-entrega/              FINALIZAR, observação, FINALIZAR SEM COBRAR, o que muda na loja
├── 14-historico/                      dia a dia, entrar num dia, ver o pedido entregue
├── 15-ajustes-e-sair/                 gaveta, permissões, sair e o que o logout faz
├── apendices/
│   ├── o-que-nao-existe-na-tela.md    WhatsApp sem porta de entrada, Keeta sem botão, etc.
│   ├── mensagens-de-erro.md           cada alerta do app, o que significa, o que fazer
│   └── push-e-notificacoes.md         o que chega, o que o toque faz
└── smoketests/                        scripts + roteiros reproduzíveis (§4)
```

São 15 pastas de conteúdo (chamei de "13 manuais" pelos fluxos principais; 01 e 15 são borda).
Se preferir menos arquivos, o corte natural é fundir 05 em 04, 07 em 06 e 12 em 11 — cai para
12 pastas sem perder assunto.

### Anatomia de cada manual

```
06-rota/
├── manual.md                 texto corrido do fluxo, costurando os prints na ordem
├── prints/
│   ├── 01-lista-com-rota.png
│   ├── 02-confirmacao-iniciar-rota.png
│   └── 03-maps-com-paradas.png
├── 01-lista-com-rota.md      o que esta tela mostra, cada elemento, quando aparece, o que fazer
├── 02-confirmacao-iniciar-rota.md
└── 03-maps-com-paradas.md
```

O `.md` por print é curto e sempre com a mesma estrutura: **o que é esta tela**, **cada elemento
numerado**, **o que acontece se eu tocar**, **quando esta tela não aparece**. O `manual.md` é a
narrativa; os `.md` de print são a referência.

---

## 4. Como o cenário é montado (a parte de engenharia)

O ciclo é este, e ele se repete uma vez por manual:

```
limpar  →  semear o cenário exato do capítulo  →  conferir pela API (GET)
        →  operar o app no emulador (adb)  →  capturar cada tela
        →  escrever o .md de cada print  →  escrever o manual.md  →  próximo capítulo
```

### 4.1 O que já existe e eu vou reusar

| Ferramenta | Onde | Papel no plano |
|---|---|---|
| `seed-gestao-entregas.js` | `node-3.0/scripts/` | cria de 1 a 15 pedidos DELIVERY na 38311/39202; `--qtd`, `--endereco-inicio`, `--dry-run` |
| `limpar-teste-01.js` | `node-3.0/scripts/` | devolve a config de despacho, derruba presença, **apaga todas as rotas da filial** e cancela os pedidos marcados `[SEED-ENTREGAS]` |
| `GET /gestao/entregador/...` | API 3.0 | conferência do cenário antes de tocar no celular — é o mesmo payload que o app vai ler |
| `adb` | emulador `emulator-5554` | operar o app e capturar |

O `limpar-teste-01.js` tem um limite a conhecer: ele cancela **só** pedidos com o marcador
`[SEED-ENTREGAS]` e que estejam em `AGUARDANDO/PREPARO/PRONTO/ENTREGA`. Pedido de outra origem,
ou já `ENTREGUE`, fica. Para o nosso caso isso basta, porque a filial está em zero e todos os
pedidos daqui para frente serão nossos.

### 4.2 O que preciso criar: um script de cenário

Proposta: **um** script novo, `scripts/cenario-entregador.js` no `node-3.0`, casca fina sobre o
`semearLote` que já existe, com uma flag por cenário do manual:

| Flag | Cenário que habilita | Manual |
|---|---|---|
| `--limpar` | chama a limpeza e confere que ficou em zero | todos |
| `--avulsos N` | N pedidos soltos, sem rota | 03, 04, 07 |
| `--rota N` | N pedidos + rota criada e associada ao 194115, **não despachada** | 06 |
| `--marketplace ifood` / `99food` | grava `correlationId`+`ifoodLocalizer` / `nnID`+`nnLocator` num pedido | 09, 10 |
| `--pago` | lança pagamento na venda para o app mostrar **Pedido já pago** | 11 |
| `--parcial` | paga metade: `saldo` menor que o total, com bloco **JÁ REGISTRADO** | 11 |
| `--troco N` | grava `tipopagStr = "Dinheiro \| troco para N"` para o app exibir a coluna **TROCO** | 11 |
| `--destaque` | marca `destaqueImpressao` num item e numa opção | 04 |

Duas coisas aqui não são "supor e escrever": o nome real da coluna de `ifoodLocalizer`/`nnLocator`
em `_PreVenda` e o formato exato que o app espera em `tipoPagStr` para render a coluna TROCO.
Antes de gravar qualquer um dos dois eu **leio o `INFORMATION_SCHEMA` e o payload da API**, e
ajusto — é o mesmo cuidado que o `21-pagamento-na-rua.md` §7 registra. Se a coluna não existir do
jeito que eu espero, o capítulo correspondente muda de método e eu te aviso antes.

### 4.3 A rota: três caminhos, e minha recomendação

Criar rota é JWT (§1.7). As opções:

| Caminho | Como | Custo | Risco |
|---|---|---|---|
| **A. Modelo direto** (recomendado) | o `cenario-entregador.js` chama `gestaoEntregaCriarRota` do próprio `node-3.0`, sem HTTP | nenhum — é a mesma função que a tela chama | nenhum novo |
| B. Painel web | abrir o `beefood-web-react`, criar a rota arrastando | exige subir o painel e o túnel | nenhum, e dá print do "outro lado" |
| C. Despacho automático | ligar o cron e esperar | exige `beefood3-server-entregas` + painel aberto para heartbeat | alto: depende de 4 peças de infra |

Recomendo **A** para montar todos os cenários, e **B uma única vez**, só para o manual 06 poder
mostrar como a rota nasce do lado do restaurante — que é exatamente a exceção que você abriu
("exceto na hora que vamos criar rotas fakes pra mostrar como fica aqui"). O C fica de fora: ele
testa o cron, não o app.

### 4.4 Operar o app pelo emulador

Eu mexo no app via `adb`, sem tocar no mouse:

```powershell
adb shell uiautomator dump /sdcard/ui.xml   # árvore da tela, com bounds de cada elemento
adb shell input tap X Y                      # toque
adb shell input text "..."                   # digitação
adb shell screencap -p /sdcard/cap.png       # captura
```

O `uiautomator dump` lê a árvore de acessibilidade — o app já usa `accessibilityLabel` em boa
parte dos controles (a pílula de presença, os botões pílula), então localizar elemento por texto
funciona. Onde não funcionar, caio nos `bounds` do nó. Proponho dois helpers pequenos em
`smoketests/`: um que captura já com nome sequencial e pasta certa, e um que imprime os
elementos clicáveis com as coordenadas — para eu não ficar adivinhando pixel.

**O ponto frágil declarado:** teclado e WebView. Campo de valor na cobrança e o site do iFood
dentro da WebView não expõem árvore de acessibilidade confiável. Nesses dois pontos a chance de
eu precisar de um ajuste manual seu é real, e eu aviso em vez de insistir.

### 4.5 Código de barras e QR: o problema de verdade do plano

O manual 08 precisa mostrar uma leitura acontecendo. O scanner usa `expo-camera` e, na leitura,
converte o EAN-13 em `preVendaID` (`parseInt(código.slice(0, -1))`) e chama
`POST tentrega/lerCodigoBarras`. No emulador, a câmera de trás é uma **cena virtual** — ela não
"vê" um código que eu coloque na tela do PC.

Três saídas, em ordem de fidelidade:

| # | Como | Resultado |
|---|---|---|
| 1 | Configurar o AVD para usar a **webcam do host** na câmera traseira e mostrar o código de barras do pedido na tela | leitura real, print real; depende de haver webcam disponível |
| 2 | Injetar o código na **cena virtual** do emulador (o poster do `emulator`), que aceita imagem PNG numa parede | leitura real, mais trabalhoso, não depende de webcam |
| 3 | Capturar a tela do scanner (faixa da câmera, mensagem "Aguardando Leitura") e disparar a leitura pela API, capturando em seguida a tela de sucesso | prints reais de todas as telas, mas a leitura não passou pela câmera |

Recomendo tentar **1**, cair para **2** e, se as duas falharem, documentar com **3** dizendo no
próprio manual que a leitura foi disparada por API. O que eu não quero é gastar meia hora de
tentativa e erro sem te contar — por isso a decisão 4 da §6.

### 4.6 Push

Para o manual de push ter print de notificação, o app precisa ter registrado token FCM no
emulador. O emulador é `sdk_gphone64` (tem Play Services), então tende a funcionar; mas o
registro depende de configuração de projeto do Expo que eu ainda não conferi. Trato como
**melhor esforço**: se o token registrar, capturo a notificação chegando e o efeito do toque
(volta para Entregas e recarrega a lista); se não, o apêndice descreve o comportamento sem print
e diz por quê.

---

## 5. Os scripts de smoketest

Você pediu scripts de smoketest na 38311/39202. Proposta de divisão por natureza, não por
capricho: o que fala com banco mora onde as credenciais e os models já estão; o que fala com o
emulador mora junto do manual.

| Onde | O quê |
|---|---|
| `beetech-server-node-3.0/scripts/cenario-entregador.js` | monta e limpa cenário (§4.2). Reusa `semearLote`, os models de rota e as conexões já configuradas |
| `beetech-server-node-3.0/scripts/abrir-caixa-teste.js` | abre caixa na filial se não houver aberto, e diz qual é o `caixaID`. **Só se a decisão 2 for "sim"** |
| `beetech-entregador/docs/manual-gestao-entregas-2/smoketests/` | roteiros `.md` por capítulo + helpers de `adb` (captura nomeada, dump de elementos clicáveis) |

Cada roteiro de smoketest é um `.md` com: pré-condição, comando de cenário, passos no app,
resultado esperado por passo, e o `GET` de conferência. Assim o manual não é só bonito: ele é
**reexecutável** por outra pessoa, que é o que transforma "print" em "teste".

Detalhe de estilo que vou seguir, por causa do `AGENTS.md`: identificadores e nomes de arquivo em
inglês onde o projeto já usa inglês, e **todo texto de conteúdo em português** — manual é UI
voltada ao usuário.

---

## 6. As seis decisões que eu preciso de você

Estas travam o início. As três primeiras são de risco; as três últimas são de método.

| # | Decisão | Minha recomendação |
|---|---|---|
| 1 | **Escrever na produção** da filial 38311/39202 (criar pedidos, rotas, dar baixa) | **Sim**, com a lista branca como única trava, exatamente como os testes da Gestão 2.0 já fazem |
| 2 | **Abrir caixa real** na filial para o manual de cobrança funcionar — o pagamento de teste entra no caixa e depois precisa ser fechado ou conciliado | **Sim**, e eu documento no manual quais lançamentos foram meus (valor, hora, `funcionarioID` 194115), para a conciliação ser trivial. Alternativa: eu paro na tela de confirmação e **não** envio o POST — os prints saem todos, menos o de sucesso |
| 3 | **Pedidos fake de iFood/99Food:** preencher `correlationId`/`nnID` faz a baixa daquele pedido **tentar notificar o marketplace de verdade** com um ID que não existe lá | Criar o pedido fake para obter os prints, e **finalizar esses dois pedidos por script com `notificarMarketplace: false`** em vez de pelo botão do app. O manual ganha os prints do WebView; o webhook não sai. O que se perde é o print do "finalizar" **desses dois** pedidos, que o manual 13 já mostra com pedido normal |
| 4 | **Código de barras no emulador:** webcam do host, cena virtual, ou leitura via API com prints reais das telas | Tentar na ordem 1 → 2 → 3 (§4.5), com teto de tempo: se 1 e 2 não funcionarem em 15 minutos, sigo com 3 e registro no manual |
| 5 | **Locale do emulador para pt-BR** antes de capturar | **Sim** — senão os diálogos do sistema entram em inglês no manual |
| 6 | **Tamanho do índice:** 15 pastas (§3) ou a versão enxuta de 12 | 15. Mapa e melhor rota são dúvidas de operação frequentes e ficam perdidas dentro de outro capítulo |

Uma sétima, só se você quiser: **limpar de verdade as vendas antigas da filial.** Hoje não
precisa — a lista do entregador está em zero. Se aparecer sujeira de execuções passadas durante
o trabalho, eu te mostro o que é antes de cancelar qualquer coisa que não tenha sido criada por
mim.

---

## 7. Ordem de execução e esforço

A ordem não é a do índice: ela vai do cenário mais simples de montar para o mais delicado, para
que um bloqueio no fim não impeça o começo.

| Onda | Manuais | Cenário necessário | Depende de decisão |
|---|---|---|---|
| 1 | 01, 02, 15 | nenhum (filial vazia) | 5 |
| 2 | 03, 04, 05, 07, 14 | avulsos, destaque, um entregue | 1 |
| 3 | 06 | rota associada + um print do painel | 1 |
| 4 | 13 | avulso + finalizar de verdade | 1 |
| 5 | 11, 12 | caixa aberto + pago/parcial/troco | 1, 2 |
| 6 | 09, 10 | pedido fake de marketplace | 1, 3 |
| 7 | 08 | leitura de código de barras | 4 |
| 8 | apêndices + README + smoketests | — | — |

Estimativa honesta: **8 a 10 ondas de trabalho**, sendo a onda 2 a mais longa (cinco manuais) e
a 7 a mais imprevisível. Eu reporto ao fim de cada onda, com os prints já no lugar, para você
corrigir o tom do texto antes de eu repetir o erro em dez capítulos.

---

## 8. O que eu não vou fazer sem perguntar

- Tocar em qualquer empresa/filial que não seja **38311 / 39202**.
- Cancelar ou alterar pedido que não tenha sido criado por mim.
- Enviar `POST` de pagamento antes da decisão 2.
- Dar baixa em pedido com ID de marketplace preenchido pelo botão do app antes da decisão 3.
- Alterar código do app. Se um print revelar bug, ele vira uma linha num apêndice de "achados",
  não um commit — a menos que você peça.
- Rodar `teste-01-fluxo-completo.js`: ele mexe em GPS, cron e despacho, e mede o sistema, não o
  app. Não é o que este trabalho precisa.
