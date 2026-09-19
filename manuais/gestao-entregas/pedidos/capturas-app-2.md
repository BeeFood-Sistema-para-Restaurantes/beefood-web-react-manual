# Capturas do app, segunda lista — 6 prints e 3 arquivos de fonte

Para a IA que opera o emulador na máquina do dono, depois de fechar o bloco da Gestão de Entregas 2.0
com as 24 capturas da rodada anterior ([`capturas-app.md`](capturas-app.md), respondida em
19/09/2026).

> **Nada aqui bloqueia manual nenhum.** Os dezesseis manuais do bloco estão publicáveis hoje, e o
> `## O que falta` de cada um diz *nada*. Esta lista é de **qualidade**: seis telas que hoje o texto
> descreve por escrito, e uma delas substitui a **única imagem composta** de todo o bloco.
>
> Se não vierem, nada se perde. Se vierem, o #114 deixa de ter imagem montada e o #112 ganha as duas
> telas que hoje são só frase.

## O que este pedido pressupõe que você tem

Escrito depois de o dono deixar claro o que existe do seu lado, porque a primeira versão desta lista
pedia duas coisas que não existem: **etiqueta impressa em papel** e **APK da Play Store**. Nenhuma das
duas aparece aqui.

| Você tem | E é com isso que cada cena é montada |
|---|---|
| o **emulador Android** e o app rodando nele | todas as seis fotos |
| **acesso ao banco**, pelo `smoke-app.js` | as cenas que não se alcançam clicando |
| **printscreen** | o `capturar.ps1` que veio no kit |
| o **repositório do aplicativo** (`beetech-entregador`) | a pasta 29, e a foto 28, que sai de um build seu |

**Nada aqui pede aparelho físico, papel, impressora ou loja de aplicativos.** Se algum passo parecer
pedir, ele está mal escrito — anote no relatório e siga.

## O que muda de verdade

| | Prints | Efeito |
|---|--:|---|
| **Troca imagem composta por imagem real** | 1 | o #114 é o único manual do bloco com uma imagem **sobreposta**: o emulador não tem câmera, e a etiqueta dentro da faixa foi montada por script |
| **Mostra as faixas de resultado da leitura** | 3 | o #114 descreve seis mensagens da faixa de status e não mostra nenhuma |
| **Fecha duas frases sem tela** | 2 | o histórico realmente vazio (o print da rodada passada veio com 22 entregas) e o aplicativo abrindo **sem rede** |
| **Confirma o que o manual afirma** | 3 arquivos | os fontes das três telas desta rodada, para eu conferir o texto contra o código em vez de contra o estudo de outra pessoa |

Se der tempo para uma coisa só, é a foto **26/01** — ela é a que tira uma imagem montada de um manual
publicado, e é a de menor risco das quatro da pasta 26. O motivo está logo abaixo.

## Antes de tudo: duas travas que valem para as seis

**1. Ler a etiqueta DESPACHA o pedido de verdade.** Não é conferência. A leitura chama a mesma rota
que o botão de despachar do painel (`POST tentrega/lerCodigoBarras` → `SituacaoDeliveryUpdater` com
`'ENTREGA'`), e isso avisa o cliente por WhatsApp e registra a saída no marketplace.

Então: **só bipe etiqueta de pedido semeado pelo script**, nunca de pedido que apareceu na fila por
outro caminho. Os pedidos do `preparar --caso lista` são de clientes sintéticos, **sem telefone e sem
e-mail** (conferido na base antes de versionar o material da primeira rodada), e não são de
plataforma. Neles a leitura não dispara WhatsApp para ninguém nem avisa marketplace nenhum.

**2. O histórico do aplicativo não é o lote da execução.** Ele lê **tudo** o que o entregador já
entregou. É o que fez a foto do histórico vazio voltar errada na rodada passada. O comando para isso
é novo e está explicado na pasta 27.

## Os scripts, e o que mudou neles

```
manuais/gestao-entregas/scripts/smoke-app.js
```

Mesmos comandos da rodada anterior, mais dois:

```powershell
node smoke-app.js casos                     # a lista, com a foto de cada caso
node smoke-app.js preparar --caso lista      # monta e confere
node smoke-app.js conferir                   # confere de novo, quantas vezes quiser
node smoke-app.js limpar                     # tira tudo da tela do app

node smoke-app.js historico-zerar            # NOVO: tira TUDO do Histórico, e guarda o desfazer
node smoke-app.js historico-voltar           # NOVO: devolve exatamente o que o zerar tirou
```

Os dois novos foram exercitados de ponta a ponta antes de virar pedido: zeraram as 8 entregas
concluídas do entregador de teste, a trava recusou um segundo `zerar` sobre um desfazer pendente, e o
`voltar` devolveu as 8 com as datas originais intactas. O desfazer mora em
`.smoke-app-historico.json`, ao lado do script, e é apagado só quando a conta fecha.

---

## 26. A leitura de código de barras de verdade (4)

| Arquivo | A cena | Precisa de |
|---|---|---|
| `26-codigo-de-barras/prints/01-codigo-na-faixa.png` | a etiqueta EAN-13 **dentro da faixa da câmera** | a câmera **ver** o código |
| `26-codigo-de-barras/prints/02-lido-com-sucesso.png` | a faixa **Pedido lido com sucesso!** | a câmera **decodificar** |
| `26-codigo-de-barras/prints/03-faixa-vermelha.png` | **Erro na leitura, tente novamente** | decodificar, e o envio falhar |
| `26-codigo-de-barras/prints/04-pedido-ja-lido.png` | **Pedido já lido.** | decodificar duas vezes |

**A primeira é diferente das outras três, e é a que importa mais.** Ela não depende de a leitura dar
certo: basta a câmera estar **apontada para o código**, com ele entre as duas linhas vermelhas. A
faixa de status pode continuar em *Aguardando Leitura* — a foto que o manual precisa é a do
enquadramento, e é exatamente essa que hoje está montada por script. Se você conseguir só ela, o
pedido já valeu.

As outras três só existem **depois de uma decodificação**. Sem ela a faixa nunca sai de *Aguardando
Leitura*, e não há como forçar pela tela: o modal não tem campo para digitar código.

### Por que a 01 vale tanto

O #114 descreve seis mensagens de status numa tabela e não mostra nenhuma. E a imagem que ele mostra
da leitura — `06-codigo-na-faixa.png` — é a única imagem **composta** do bloco inteiro: o emulador vê
uma sala virtual, e a etiqueta foi sobreposta ali pelo `compor-leitura.ps1`, que veio no seu próprio
material da primeira rodada. Está declarado no `fluxo-codigo.md` do manual, o que é honesto, mas
imagem real é melhor que imagem declarada.

### Como pôr um código na frente da câmera do emulador

O emulador usa a câmera **virtualscene**: uma sala 3D com pôsteres na parede. Ela aceita **trocar um
pôster por um PNG seu**, e é esse o caminho.

1. `node smoke-app.js preparar --caso lista` — quatro pedidos abertos, clientes sintéticos.
2. `node smoke-app.js estado` e anote o `preVendaID` de um pedido em **PREPARO** ou **PRONTO**.
   Pedido já em `ENTREGA` responderia *Pedido já lido* na primeira tentativa.
3. Gere a etiqueta desse pedido com o gerador que já veio no kit:
   `3-referencia/material-original/smoketests/codigo-de-barras/gerar-ean13.js`. Ele monta o EAN-13 a
   partir do `preVendaID` — **os 12 primeiros dígitos são o identificador do pedido** e o 13º é o
   verificador. Rodei aqui para conferir: `node gerar-ean13.js 59588083` sai com o código
   `0000595880834`, num PNG de 840x340. O comentário do próprio script diz que o módulo é largo
   **porque a imagem vai ser lida pela câmera do emulador** — quem o escreveu já tinha este caminho
   em mente, e é a razão de eu insistir nele.
4. No emulador, **Extended controls** (os três pontos da barra lateral) → **Camera** → a lista de
   imagens da cena virtual → adicione o PNG da etiqueta. Ele passa a ser um pôster na parede.
5. Abra o leitor no app (aba **Código barras**) e **ande até o pôster** dentro da cena: com a prévia
   da câmera ativa, as teclas `W A S D` movem e o mouse com `Alt` pressionado gira a visão. Encoste no
   pôster até o código ocupar a faixa entre as linhas vermelhas.
6. `01-codigo-na-faixa.png` é esta tela. Tire a foto **aqui**, antes de tentar as outras três — se a
   decodificação não vier, você já tem a que mais vale.

> **Não conferi este caminho daqui**, porque não existe emulador nesta máquina; conferi só a geração
> do código. Se a etiqueta não aparecer na faixa depois de duas tentativas honestas, **pare**: anote
> no relatório o que aconteceu e siga para a pasta 27. Não invente outro jeito de pôr a imagem na
> tela, e principalmente **não componha a foto** — a composta o manual já tem, e declarada.

### As três que dependem da decodificação

| Foto | Como produzir |
|---|---|
| `02-lido-com-sucesso` | a leitura acima, com rede ligada. A faixa fica **verde** e o pedido vai para *ENTREGA* |
| `04-pedido-ja-lido` | **sem sair da tela do leitor**, aproxime a mesma etiqueta de novo. O app bloqueia a releitura na mesma sessão e a faixa diz *Pedido já lido.* — nada é enviado |
| `03-faixa-vermelha` | abra o leitor **com rede**, depois desligue (`adb shell svc wifi disable` e `svc data disable`) e só então aproxime a etiqueta de **outro** pedido. A leitura acontece no celular e o envio falha: é o *Erro na leitura, tente novamente* |

A ordem importa: faça `02` e `04` primeiro, com rede, e `03` no fim — é a que precisa da rede
desligada, e ela deixa o pedido **sem** despachar, que é o que o manual afirma.

> **Se a faixa vermelha não sair na primeira tentativa, siga.** O aplicativo tem 20 s de timeout
> nesta chamada, e em rede caindo devagar ele pode demorar a desistir. Desligar wifi **e** dados
> antes de aproximar resolve na maioria das vezes.

---

## 27. O histórico realmente vazio (1)

| Arquivo | A cena | Onde entra |
|---|---|---|
| `27-historico-vazio/prints/01-historico-vazio.png` | **Nenhuma entrega no período** + *As entregas que você concluir aparecem aqui.* | #112, a pergunta *O histórico está vazio*; e o #111 |

**Esta é a única das seis que depende só de emulador e banco.** Se alguma tiver que sair, que seja
outra.

Ela foi pedida na rodada passada e voltou como outra coisa: a tela veio com **22 entregas em três
dias**. Não foi erro de quem fotografou — foi erro do pedido. O caso `historico-vazio` desatribui os
pedidos **do lote da execução**, e o Histórico do aplicativo lê tudo o que aquele entregador já
entregou, de qualquer dia. Sobrou o que estava lá de antes.

O aplicativo **não tem filtro de data** nessa tela (ele manda a data de hoje nos dois campos do
período e o servidor devolve mais do que isso), então não há como chegar a *Nenhuma entrega no
período* pela tela. A única forma é o entregador não ter entrega concluída nenhuma — e é para isso que
os dois comandos novos existem.

```powershell
node smoke-app.js limpar               # a aba Entregas vazia
node smoke-app.js historico-zerar      # o Histórico vazio, com o desfazer guardado
#   --> abra a aba Histórico e tire a foto
node smoke-app.js historico-voltar     # devolve tudo, com as datas originais
```

**O `historico-voltar` é obrigatório, e logo depois da foto.** Enquanto o histórico está zerado, as
entregas não contam no relatório Operação de Entrega — e é o relatório que o #118 documenta com dados
dessa mesma filial.

Ele é reversível por construção: o `zerar` grava quem era o entregador de cada entrega **antes** de
escrever no banco, e o `voltar` só apaga o desfazer depois de conferir que a conta fechou. Se não
fechar, ele avisa e **mantém** o arquivo.

---

## 28. O aplicativo abrindo sem rede (1)

| Arquivo | A cena | Onde entra |
|---|---|---|
| `28-abrir-sem-rede/prints/01-app-sem-rede-do-zero.png` | o aplicativo **aberto do zero** sem rede — a tela que ele mostra antes de ter qualquer lista em cache | #112, *A lista não carrega* |

O que o #112 mostra hoje é outra coisa, e está correto: com o aplicativo **já aberto** e a rede
desligada, a lista fica congelada no que estava em cache e o *puxar para atualizar* não muda nada.
Sem mensagem de erro. É o que o entregador vê na maioria das vezes, e é o que o manual descreve.

Falta o outro caminho: **abrir o aplicativo do zero**, sem rede. Você anotou no relatório da rodada
passada por que não saiu, e a explicação está certa: no build de desenvolvimento o aplicativo carrega
o bundle JavaScript do Metro, então sem rede ele morre antes de qualquer tela.

**A saída não é a Play Store — é um build de release seu.** Build de release **embute** o bundle no
APK (`index.android.bundle` dentro dos assets) e não procura o Metro, porque o
`getUseDeveloperSupport()` dele é falso. Aberto sem rede, ele chega até a tela.

### Como montar a cena

1. No repositório do app, veja se já existe release pronto em
   `android/app/build/outputs/apk/release/`. Se existir, pule para o passo 3.
2. `cd android` e `.\gradlew assembleRelease`. No template do React Native o `buildType release` usa
   o **keystore de debug** por padrão, então normalmente isso funciona sem nenhuma chave sua. **Se o
   projeto tiver uma assinatura própria que você não tem, pare aqui** e anote no relatório — não
   procure a chave, não gere uma nova. O manual continua correto sem esta foto.
3. Instale: `adb install -r android\app\build\outputs\apk\release\app-release.apk`. Ele conversa com o
   mesmo servidor, então o entregador de teste entra igual.
4. Entre **com rede**, para o login e a lista existirem.
5. Force a parada e limpe o **cache** — **não** os dados, para não perder o login (`adb shell pm
   clear` derrubaria a sessão e o token de push).
6. Desligue wifi e dados, e abra o aplicativo.
7. Fotografe o que aparecer. **Qualquer tela serve como resposta**, inclusive "nada de especial, a
   lista abre vazia": se não houver mensagem, escreva isso no relatório e o manual passa a dizer que
   não há. O que não serve é a suposição.

> Se o release subir e o app **não** abrir por outro motivo (assinatura conflitando com o debug já
> instalado, por exemplo — `adb uninstall com.beetechentregador` antes resolve), tente uma vez e siga.

---

## 29. Três arquivos de fonte, para eu conferir o texto (0 fotos)

Não é foto, é leitura. Copie estes três arquivos do repositório do app para a pasta, como estão:

| Arquivo no app | Para conferir o quê |
|---|---|
| `src/components/Barras/BarcodeScannerModal.js` | as **seis mensagens** da faixa de status do #114, a cor de cada uma e a trava de releitura |
| `src/views/historico/index.js` | que o Histórico **não tem filtro de data** na tela, e o texto exato do vazio (#112) |
| `src/views/entregas/index.js` | o que a lista faz **sem rede**: cache, *puxar para atualizar* e ausência de mensagem de erro (#112) |

**Por que pedir fonte, e não só a foto.** Hoje eu afirmo essas três coisas com base no
`estudo/01-o-que-o-app-faz-hoje.md` que veio no seu material da primeira rodada — que é bom, e foi
escrito lendo o código, mas é leitura de segunda mão. Já custou uma correção: o manual listava **cinco**
mensagens de faixa e o estudo mostra **seis**, e a que faltava (*Erro: {mensagem}*, o servidor
recusando) é justamente a que muda o que o entregador deve fazer. Quero conferir o resto eu mesmo.

**O que acontece com esses arquivos depois.** Eu leio, tiro o que interessa para o `fluxo-codigo.md`
de cada manual, e **não versiono nenhum deles** — este repositório de manuais é público, e fonte de
aplicativo não entra nele. Mesma regra que já vale para senha e host do backend: o achado fica, o
arquivo não.

Se algum dos três tiver outro nome ou outro caminho, manda o que existe e escreve no relatório qual
foi. Se você preferir não mandar fonte, diga no relatório — as fotos continuam valendo por si.

---

## Como me entregar

Mesmo caminho das duas vezes: **WeTransfer**, um zip só, com as pastas exatamente como estão nas
tabelas. Sem renomear e sem recortar — o recorte é feito aqui, pelo `annotate.py` de cada manual.

```
capturas-3/
├── 26-codigo-de-barras/prints/    01-codigo-na-faixa.png  02-lido-com-sucesso.png
│                                  03-faixa-vermelha.png   04-pedido-ja-lido.png
├── 27-historico-vazio/prints/     01-historico-vazio.png
├── 28-abrir-sem-rede/prints/      01-app-sem-rede-do-zero.png
├── 29-fontes/                     BarcodeScannerModal.js  historico-index.js  entregas-index.js
└── RELATORIO.md
```

A pasta se chama `capturas-3` porque é a **terceira leva de material** — `capturas-2` foi a rodada
de 19/09. Os números 26 a 29 continuam a numeração dos capítulos, que é o que identifica cada cena de
verdade.

### O relatório, de novo, é a parte que faz o material valer

Três coisas, e a terceira é a que mais rendeu na rodada passada:

1. **A versão do app** e a data da captura. Se a pasta 28 sair de um build de release seu, diga a
   versão dele também — ela pode não ser a mesma do build de desenvolvimento.
2. **O aparelho**: qual AVD, qual Android. E, na pasta 26, **se a cena virtual funcionou ou não** —
   isso vale tanto quanto a foto, porque decide se o manual continua com a imagem composta ou não.
3. **Uma linha por print que saiu diferente do pedido**, dizendo o que aconteceu antes — e uma linha
   por print que **não saiu**, dizendo por quê.

Na rodada passada foi o item 3 que virou achado: o *Permissão necessária* no lugar da falha da melhor
rota mudou uma resposta do #113, e o "histórico vazio" com 22 entregas gerou os dois comandos novos do
script. **Print que sai diferente do pedido é informação, não defeito** — mas só se vier com a linha
que explica o que foi feito antes dele.
