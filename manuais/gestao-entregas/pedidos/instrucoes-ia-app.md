# Leia primeiro — o trabalho, em uma página

Para a IA que vai operar o emulador Android e tirar os prints do **BeeFood Entregador**.

Seu trabalho é **26 fotos de tela**, com nome de arquivo exato, devolvidas num zip. Nada além
disso. Você não escreve manual, não recorta imagem, não desenha seta, não monta colagem. As fotos
entram num material que já está escrito — o recorte, a seta verde numerada e o texto são feitos do
outro lado, por scripts que esperam a foto crua.

**A regra que vale mais que todas as outras: foto que você não conseguiu tirar não se inventa.**
Não há atalho aceitável — nem editor de imagem, nem tela parecida de outro cenário, nem "essa serve".
Um print errado é pior que um print faltando, porque o print faltando está anotado no relatório e o
errado vira manual publicado mentindo. Se uma cena não sair, escreva no `RELATORIO.md` o que
aconteceu e siga para a próxima. Duas ou três faltas são normais; uma foto forjada invalida o lote.

## O que tem neste kit

| Pasta | O que é | Você faz o quê |
|---|---|---|
| `1-pedido/` | **o pedido em si**: as 26 fotos, nome por nome, com a cena e o manual que recebe cada uma | é a sua lista de tarefas — `capturas-app.md` é o arquivo central |
| `2-scripts/` | o `smoke-app.js`, que **monta cada cena no banco**, confere e desmonta | você roda, antes de cada foto |
| `3-referencia/` | os manuais já publicados **com as imagens**, o material original inteiro e os scripts de emulador | você consulta para saber que tela é qual e como as fotos atuais são enquadradas |
| `4-entrega/` | a árvore de pastas vazia, com os nomes exatos | você preenche, e é isso que volta zipado |

Comece por `1-pedido/README.md`, que é curto, e depois `1-pedido/capturas-app.md`, que é a lista.

## O ambiente, e o que precisa estar de pé

Tudo isto roda na **máquina Windows do dono**, que é onde o emulador e o clone do backend já
existem. Os 63 prints do material atual saíram daí.

| O quê | Como |
|---|---|
| emulador | `emulator -avd Pixel_7_Pro -prop persist.sys.locale=pt-BR` — o locale **tem** que vir na subida; `adb root` derruba a instância |
| o app | precisa do Metro do projeto: `cd C:\projetos\beetech-entregador` e `yarn start` |
| GPS | `adb emu geo fix -47.4657927 -23.5061438` — é a loja, em Sorocaba. Sem isso o Google Maps calcula rota a partir do Vale do Silício |
| login | o dono tem a senha do entregador **194115** (`BeeFood3 - Manual`). Ela não está neste kit, e não deve estar |
| começar do zero | `adb shell pm clear com.beetechentregador` |

**Se o app mostrar "Unable to load script"**, o emulador perdeu a rota de rede e não alcança o Metro
em `10.0.2.2:8081`. Reciclar o Wi-Fi virtual resolve: `adb shell svc wifi disable; adb shell svc wifi
enable`, e confira com `adb shell ip route` que existe rota default por `wlan0`.

Duas ferramentas de emulador vêm no kit, em `4-entrega/capturas-2/_ferramentas/emulador/`, e é de
propósito que elas estão **lá dentro**: elas gravam dois níveis acima de si mesmas, então a partir
daquela pasta o arquivo cai exatamente onde o pedido quer.

```powershell
cd 4-entrega\capturas-2\_ferramentas\emulador

.\elementos.ps1 -Filtro COBRAR      # lista os controles da tela com o centro de cada um
.\capturar.ps1 -Capitulo 16-notificacoes -Nome 01-aviso-chegando
```

O `capturar.ps1` existe porque `adb exec-out screencap -p > arquivo.png` **corrompe o PNG** no
PowerShell: o operador de redirecionamento trata binário como texto. Use o script, que faz
`screencap` no `/sdcard` seguido de `pull`, e ainda recusa arquivo com menos de 10 KB — a assinatura
de captura que falhou.

Para tocar na tela: `.\elementos.ps1` diz o X e o Y de cada controle pelo nome, e
`adb shell input tap X Y` toca. É mais confiável que adivinhar pixel, porque o app usa
`accessibilityLabel` na maior parte dos controles.

## O formato do print

Não negocie nestes cinco pontos. Os prints atuais seguem todos eles, e as ferramentas do outro lado
contam com isso.

1. **PNG, tela inteira, resolução nativa** — os 61 prints do material são `1440 × 3120`. Nada de
   recorte, nada de redimensionar. O recorte é feito do outro lado, e recorte que chega pronto
   impede o enquadramento que o manual precisa. Os prints atuais estão em
   `3-referencia/material-original/<capítulo>/prints/`: abra dois ou três antes de começar, é o
   padrão que os seus precisam seguir.
2. **Tela parada.** Sem *spinner*, sem animação no meio, sem transição. Se houver carregamento na
   tela, espere e tire de novo — `capturar.ps1 -Espera 2` ajuda.
3. **Teclado fechado**, a menos que o assunto da foto seja digitar.
4. **Barra de cima limpa**: sem notificação de outro app. A única exceção é a pasta
   `16-notificacoes`, onde a notificação **é** o assunto.
5. **Nome de arquivo exatamente como está na tabela**, na pasta exatamente como está na árvore.
   Renomear depois custa mais que acertar na hora, e a numeração continua a dos 15 capítulos que já
   existem.

Sobre nome de cliente: os que aparecem no app (*Ana Beatriz Moraes*, *Rafael Monteiro Dias*) são
**clientes sintéticos**, criados por script, conferidos um por um na base antes de o material ir
para um repositório público. Não borre, não cubra, não edite.

## As duas metades do trabalho

**Vinte fotos são suas, sozinho.** Estão nas pastas 16, 17, 19, 20, 21, 22, 23, 24 e 25. Cada linha
da tabela em `capturas-app.md` diz o comando que monta a cena e o gesto que produz a tela. Faça na
ordem que quiser.

**Seis fotos dependem de duas pessoas ao mesmo tempo.** É a pasta `18-ciclo-completo`, e o roteiro
está em `1-pedido/janela-117.md`: sete fases, o operador roda cada uma do painel, você fotografa
entre uma e outra. **Não tente montar essa pasta sozinho.** O manual que a recebe mostra o *mesmo
pedido*, com o *mesmo número*, nas duas telas — seis fotos de seis pedidos diferentes não servem
para nada, e é o erro mais fácil de cometer aqui. Combine a hora com o dono.

Se der tempo para uma coisa só, é a pasta 18: as outras vinte melhoram manual que já está
publicável hoje, e essas seis destravam um manual que não existe sem elas.

## O script que monta as cenas

Nenhuma dessas telas aparece clicando à toa. Pedido de marketplace já pago, pedido com saldo zero,
histórico com mais de um dia, rota chegando ao vivo — cada uma é um estado de banco. Por isso o kit
vem com `2-scripts/smoke-app.js`.

```powershell
node smoke-app.js casos                     # os nove cenários, e a foto que cada um destrava
node smoke-app.js preparar --caso pago      # monta e confere
node smoke-app.js conferir                  # confere de novo, quantas vezes quiser
node smoke-app.js limpar                    # tira tudo da tela do app
```

Ele lê host e senha do **clone do backend**, não de dentro de si mesmo. Se o clone não estiver no
caminho padrão, passe `--backend C:\projetos\beetech-server-node`. O clone precisa dos dois drivers
uma vez: `npm install --no-save mssql mysql2`.

A conferência é a parte que vale o script: ela lê a **API do próprio app**, não o banco. Já
aconteceu de o banco estar certo e a tela vir vazia, porque entre os dois moram o agrupamento de
rota, o filtro de situação e a ordenação por distância. Quando o `conferir` passa, a tela está
pronta para a foto.

### Três coisas sobre escrever no banco

Leia isto antes do primeiro `preparar`, porque não há desfazer.

**Não existe ambiente de desenvolvimento neste backend.** Host, usuário e senha são fixos no código
e apontam para o RDS de **produção**. O que protege é uma lista branca literal — empresa `38311`,
filial `39202` — e ela aborta antes de abrir conexão em qualquer outro alvo. Nunca tente destravar
isso. Semear pedido falso em loja real é pior que qualquer bug, porque o lojista sai entregando.

**Rode `--dry-run` primeiro, sempre.** Todo comando aceita. Ele imprime o que faria, sem escrever
nada. Leia a saída, veja se o alvo é o esperado, e só então rode de verdade.

**`--permitir-passado` só no caso `historico-dias`.** É a única escrita que mexe em data de entrega,
e data de entrega é o que o relatório de operação soma por dia. Mover uma entrega para ontem tira
ela do total de hoje.

## Quando uma foto não sai

Escreva no `RELATORIO.md` e siga. Três das 26 são reconhecidamente difíceis, e o pedido já diz isso:

| Foto | Por que pode não sair |
|---|---|
| `22-erros-de-cobranca/04-falta-finalizar.png` | exige cortar a rede **entre** dois pedidos HTTP. É sorte, não roteiro. Duas tentativas e pule |
| `16-notificacoes/*` | o token FCM pode não registrar no emulador. Tente no aparelho físico; se não sair em nenhum, o apêndice fica sem imagem |
| ~~`25-ios/*`~~ | **cancelada em 19/09/2026.** Precisava de um iPhone, não havia, e o dono decidiu que o manual não usa imagem de iOS. Não tente, não fotografe, não crie a pasta |

E se, fotografando, você notar que **o app faz diferente do que o manual escreveu**, isso é ouro:
escreva no relatório, com o nome do manual e a frase que está errada. Não edite os arquivos de
`3-referencia/` — eles estão ali como consulta, e a correção é feita no repositório, do outro lado.

## O que devolver

Um zip com a árvore de `4-entrega/capturas-2/` preenchida, mais um `RELATORIO.md` na raiz. A pasta
`_ferramentas/` pode ficar ou sair, tanto faz.

O relatório precisa de três coisas, e a terceira é a que faz o material ser confiável:

1. **A versão do app** e a data da captura. O manual precisa dizer de que build são as telas — as
   imagens de um manual antigo envelheceram sem ninguém notar, e é o erro que não se repete.
2. **O aparelho**: emulador (qual AVD, qual Android) ou aparelho físico, qual.
3. **Uma linha por print que saiu diferente do pedido**, dizendo o que aconteceu antes. E uma linha
   por print que **não saiu**, dizendo por quê. Print que saiu exatamente como pedido não precisa de
   linha nenhuma.

Do outro lado, cada foto vira recorte, seta numerada e texto. Quem faz isso conta com uma coisa só:
que a foto seja **o que ela diz que é**.
