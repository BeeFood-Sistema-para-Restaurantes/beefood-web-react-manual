# Leia primeiro — o trabalho, em uma página

Para a IA que vai operar o emulador Android (ou um aparelho físico) e tirar os prints do **BeeFood
Entregador**. **Esta é a segunda rodada.** A primeira pediu 26 fotos e recebeu 24 — obrigado, o
material foi bom e dois dos prints "errados" viraram achado que mudou o manual.

Seu trabalho agora é **6 fotos de tela**, com nome de arquivo exato, devolvidas num zip. Nada além
disso. Você não escreve manual, não recorta imagem, não desenha seta, não monta colagem. As fotos
entram num material que já está escrito — o recorte, a seta verde numerada e o texto são feitos do
outro lado, por scripts que esperam a foto crua.

**Nenhuma das seis bloqueia manual nenhum.** Os dezesseis manuais do bloco estão publicáveis hoje.
Estas seis são de qualidade: quatro substituem a **única imagem composta** de todo o bloco, e duas
fecham frases que hoje não têm tela. Se uma não sair, o manual continua de pé.

**A regra que vale mais que todas as outras: foto que você não conseguiu tirar não se inventa.**
Nem editor de imagem, nem tela parecida de outro cenário, nem "essa serve". Um print errado é pior
que um print faltando, porque o faltando está anotado no relatório e o errado vira manual publicado
mentindo. Se uma cena não sair, escreva no `RELATORIO.md` o que aconteceu e siga.

## O que tem neste kit

| Pasta | O que é | Você faz o quê |
|---|---|---|
| `1-pedido/` | **o pedido em si**: as 6 fotos, nome por nome, com a cena e o manual que recebe cada uma | é a sua lista de tarefas — `capturas-app-2.md` é o arquivo central |
| `2-scripts/` | o `smoke-app.js`, que **monta cada cena no banco**, confere e desmonta | você roda, antes de cada foto |
| `3-referencia/` | os manuais já publicados **com as imagens**, o material original inteiro e os scripts de emulador | você consulta para saber que tela é qual e como as fotos atuais são enquadradas |
| `4-entrega/` | a árvore de pastas vazia, com os nomes exatos | você preenche, e é isso que volta zipado |

Comece por `1-pedido/capturas-app-2.md`, que é a lista. O `1-pedido/capturas-app.md` é o pedido da
rodada passada, e vai junto só como histórico — **não é tarefa**.

O material da sua rodada anterior está em
`3-referencia/material-original/capturas-2/`, com o seu próprio `RELATORIO.md`. Use-o como padrão de
enquadramento: os novos prints precisam sair iguais àqueles.

## O ambiente, e o que precisa estar de pé

Tudo isto roda na **máquina Windows do dono**, que é onde o emulador e o clone do backend já existem.

| O quê | Como |
|---|---|
| emulador | `emulator -avd Pixel_7_Pro -prop persist.sys.locale=pt-BR` — o locale **tem** que vir na subida; `adb root` derruba a instância |
| o app | precisa do Metro do projeto: `cd C:\projetos\beetech-entregador` e `yarn start` |
| GPS | `adb emu geo fix -47.4657927 -23.5061438` — é a loja, em Sorocaba. Sem isso o Google Maps calcula rota a partir do Vale do Silício |
| login | o dono tem a senha do entregador **194115** (`BeeFood3 - Manual`). Ela não está neste kit, e não deve estar |

**Se o app mostrar "Unable to load script"**, o emulador perdeu a rota de rede e não alcança o Metro
em `10.0.2.2:8081`. Reciclar o Wi-Fi virtual resolve: `adb shell svc wifi disable; adb shell svc wifi
enable`, e confira com `adb shell ip route` que existe rota default por `wlan0`.

**Duas fotos desta rodada podem pedir aparelho físico**, e é a diferença mais importante em relação à
rodada passada:

- a pasta **26** precisa de uma câmera que veja um código de barras. Há um caminho pelo emulador (a
  cena virtual aceita trocar o pôster da parede por um PNG seu), e o pedido explica. Se não der,
  aparelho físico com a etiqueta impressa é a via boa;
- a pasta **28** precisa do **APK de produção**, não do build de desenvolvimento: sem o Metro o build
  de desenvolvimento não carrega o bundle, e "abrir sem rede" derruba o app antes de qualquer tela —
  foi exatamente o que você anotou no relatório da rodada passada.

As ferramentas de emulador vêm no kit, em `4-entrega/capturas-3/_ferramentas/emulador/`, e é de
propósito que elas estão **lá dentro**: elas gravam dois níveis acima de si mesmas, então a partir
daquela pasta o arquivo cai exatamente onde o pedido quer.

```powershell
cd 4-entrega\capturas-3\_ferramentas\emulador

.\elementos.ps1 -Filtro COBRAR      # lista os controles da tela com o centro de cada um
.\capturar.ps1 -Capitulo 26-codigo-de-barras -Nome 01-codigo-na-faixa
```

O `capturar.ps1` existe porque `adb exec-out screencap -p > arquivo.png` **corrompe o PNG** no
PowerShell: o operador de redirecionamento trata binário como texto. Use o script, que faz
`screencap` no `/sdcard` seguido de `pull`, e ainda recusa arquivo com menos de 10 KB — a assinatura
de captura que falhou.

## O formato do print

Os mesmos cinco pontos da rodada passada. Não negocie neles.

1. **PNG, tela inteira, resolução nativa** — os prints do material são `1440 × 3120`. Nada de
   recorte, nada de redimensionar. O recorte é feito do outro lado, e recorte que chega pronto impede
   o enquadramento que o manual precisa. **Se a pasta 26 sair de aparelho físico, a resolução vai ser
   outra — está tudo bem, é só escrever qual no relatório.**
2. **Tela parada.** Sem *spinner*, sem animação no meio, sem transição. `capturar.ps1 -Espera 2`
   ajuda.
3. **Teclado fechado**, a menos que o assunto da foto seja digitar.
4. **Barra de cima limpa**: sem notificação de outro app. Nesta rodada não há exceção — nenhuma das
   seis fotos tem notificação como assunto.
5. **Nome de arquivo exatamente como está na tabela**, na pasta exatamente como está na árvore.

Sobre nome de cliente: os que aparecem no app (*Ana Beatriz Moraes*, *Rafael Monteiro Dias*) são
**clientes sintéticos**, criados por script, conferidos um por um na base antes de o material ir para
um repositório público. Não borre, não cubra, não edite.

## O script que monta as cenas

```powershell
node smoke-app.js casos                     # os cenários, e a foto que cada um destrava
node smoke-app.js preparar --caso lista     # monta e confere
node smoke-app.js conferir                  # confere de novo, quantas vezes quiser
node smoke-app.js limpar                    # tira tudo da tela do app

node smoke-app.js historico-zerar           # NOVO nesta rodada
node smoke-app.js historico-voltar          # NOVO nesta rodada
```

Ele lê host e senha do **clone do backend**, não de dentro de si mesmo. Se o clone não estiver no
caminho padrão, passe `--backend C:\projetos\beetech-server-node`. O clone precisa dos dois drivers
uma vez: `npm install --no-save mssql mysql2`.

A conferência é a parte que vale o script: ela lê a **API do próprio app**, não o banco. Já aconteceu
de o banco estar certo e a tela vir vazia, porque entre os dois moram o agrupamento de rota, o filtro
de situação e a ordenação por distância.

### Os dois comandos novos, e por que eles existem

Na rodada passada, a foto do histórico vazio voltou com **22 entregas em três dias**. Não foi erro
seu: o caso `historico-vazio` desatribui os pedidos **do lote da execução**, e o Histórico do
aplicativo lê tudo o que aquele entregador já entregou, de qualquer dia.

O `historico-zerar` tira **todas** as entregas concluídas do entregador e guarda quem era o
entregador de cada uma num arquivo local. O `historico-voltar` devolve. Foram exercitados de ponta a
ponta antes de virar pedido: zeraram 8 entregas, a trava recusou um segundo `zerar` sobre um desfazer
pendente, e o `voltar` devolveu as 8 com as datas originais.

**Rode o `historico-voltar` logo depois da foto.** Enquanto está zerado, o relatório Operação de
Entrega não conta essas entregas — e é um relatório que também está documentado.

### Três coisas sobre escrever no banco

Leia isto antes do primeiro `preparar`, porque não há desfazer (fora o do histórico).

**Não existe ambiente de desenvolvimento neste backend.** Host, usuário e senha são fixos no código e
apontam para o RDS de **produção**. O que protege é uma lista branca literal — empresa `38311`,
filial `39202` — e ela aborta antes de abrir conexão em qualquer outro alvo. Nunca tente destravar
isso. Semear pedido falso em loja real é pior que qualquer bug, porque o lojista sai entregando.

**Rode `--dry-run` primeiro, sempre.** Todo comando aceita, inclusive os dois novos. Ele imprime o
que faria, sem escrever nada.

**Ler a etiqueta de código de barras DESPACHA o pedido de verdade.** É a trava nova desta rodada, e a
mais importante: a leitura chama a mesma rota do botão de despachar do painel, o que avisa o cliente
por WhatsApp e registra a saída no marketplace. **Só bipe etiqueta de pedido semeado pelo
`preparar --caso lista`** — os clientes desses pedidos são sintéticos, sem telefone e sem e-mail, e
não são de plataforma. Nunca bipe etiqueta de pedido que apareceu na fila por outro caminho.

## Quando uma foto não sai

Escreva no `RELATORIO.md` e siga. Duas das seis são reconhecidamente difíceis, e o pedido já diz:

| Foto | Por que pode não sair |
|---|---|
| `26-codigo-de-barras/01-codigo-na-faixa.png` | precisa de câmera vendo um código de verdade. O caminho da cena virtual do emulador não foi conferido do outro lado; se falhar em duas tentativas, pule — a imagem composta que o manual tem hoje continua servindo, e está declarada como composta |
| `26-codigo-de-barras/03-faixa-vermelha.png` | o app tem 20 s de timeout nessa chamada. Desligue wifi **e** dados antes de aproximar a etiqueta |

E se, fotografando, você notar que **o app faz diferente do que o manual escreveu**, isso é ouro:
escreva no relatório, com o nome do manual e a frase que está errada. Foi assim que a rodada passada
consertou duas afirmações. Não edite os arquivos de `3-referencia/` — eles estão ali como consulta, e
a correção é feita no repositório, do outro lado.

## O que devolver

Um zip com a árvore de `4-entrega/capturas-3/` preenchida, mais um `RELATORIO.md` na raiz. A pasta
`_ferramentas/` pode ficar ou sair, tanto faz.

O relatório precisa de três coisas, e a terceira é a que faz o material ser confiável:

1. **A versão do app** e a data da captura. Se a pasta 26 sair de APK de produção ou de aparelho
   físico, diga a versão de cada um.
2. **O aparelho**: emulador (qual AVD, qual Android) ou aparelho físico, qual. Nesta rodada pode ser
   mais de um, e o manual precisa saber qual foto veio de qual.
3. **Uma linha por print que saiu diferente do pedido**, dizendo o que aconteceu antes. E uma linha
   por print que **não saiu**, dizendo por quê. Print que saiu exatamente como pedido não precisa de
   linha nenhuma.

Do outro lado, cada foto vira recorte, seta numerada e texto. Quem faz isso conta com uma coisa só:
que a foto seja **o que ela diz que é**.
