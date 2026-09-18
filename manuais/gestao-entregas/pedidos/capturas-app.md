# Pedido de capturas do app — o que falta para o manual da Gestão de Entregas

Para o dono, em resposta a *"você pode pedir outras fotos do app, para isso deve criar um `.md`
específico com o que precisa (inclusive tecnicamente com scripts smoketest dos pedidos)"*.

Escrito em 18/09/2026, depois de ler os 15 capítulos e os `smoketests/` do
[material recebido](../material-recebido/README.md). **Os comandos aqui são os do seu próprio
roteiro** (`material-recebido/app-entregador/smoketests/README.md`) — não inventei nada novo.

## Resumo: 12 prints, em 5 pacotes

| Pacote | Prints | Por que falta | Precisa de mim ao mesmo tempo? |
|---|--:|---|---|
| 1. Notificação chegando | 2 | o apêndice `01-notificacoes.md` explica tudo e **não tem nenhuma imagem** | **sim** |
| 2. Entrega tirada do entregador | 2 | comportamento documentado, sem print — e é o par da troca de entregador no painel | **sim** |
| 3. Rota atribuída ao vivo | 2 | o manual precisa do **mesmo pedido** visto no painel e no app, com o mesmo número | **sim** |
| 4. Quando dá errado | 4 | sem internet e permissão recusada são os dois casos de suporte, e nenhum tem print | não |
| 5. iPhone | 2 | o manual promete Android **e iOS**, e tudo que temos é emulador Android | não |

Os pacotes 1 a 3 acontecem na **mesma janela combinada** (seção "A janela combinada"), porque
quem dispara é o painel — eu, daqui. Os pacotes 4 e 5 você faz quando quiser, sozinho.

---

## Pacote 1 — Notificação chegando (2 prints)

O apêndice de notificações é um dos textos mais úteis do material e é o único capítulo **sem
imagem**. Quem lê "o aviso aparece mesmo com o app aberto" merece ver o aviso.

| Arquivo | A cena |
|---|---|
| `16-notificacoes/prints/01-aviso-chegando.png` | o aviso do BeeFood Entregador **na tela**, com o app aberto na lista por baixo — é o caso que o texto destaca |
| `16-notificacoes/prints/02-lista-depois-do-toque.png` | logo depois de tocar no aviso: aba **Entregas** em foco e a lista já com a entrega nova |

**Como acontece:** eu atribuo um pedido a você pelo painel. Você não precisa rodar script — o
disparo vem do meu lado. Só preciso que o app esteja **online** e com a permissão de
notificações **Ativa** (capítulo 15).

> Se o token FCM não registrar no emulador — o `estudo/` já marcou isso como "melhor esforço" —
> tente no aparelho físico. Se não sair em nenhum dos dois, me diga: o apêndice fica sem imagem
> e o manual explica por texto, como fizemos com o tablet e o totem no #103.

## Pacote 2 — Entrega tirada do entregador (2 prints)

O apêndice diz que a notificação também chega **quando a entrega é tirada de você**, numa troca
de entregador. É a cena que fecha o assunto *ModalTrocarEntregador* do painel — e a pergunta que
todo entregador faz ("sumiu uma entrega da minha lista").

| Arquivo | A cena |
|---|---|
| `17-troca-de-entregador/prints/01-aviso-de-remocao.png` | o aviso chegando, dizendo que a entrega saiu |
| `17-troca-de-entregador/prints/02-lista-sem-o-pedido.png` | a lista depois, **sem** aquele pedido — de preferência mostrando o número que sobrou, para casar com o painel |

**Como acontece:** eu troco o entregador do pedido no painel, com você online. Nada de script.

## Pacote 3 — Rota atribuída ao vivo (2 prints)

Este é o coração da terceira parte do manual: **o mesmo pedido, dos dois lados**. O capítulo 06
já mostra uma rota, mas com pedidos do seu gerador — números que eu não tenho como reproduzir no
painel daqui. Preciso de uma rota criada por mim, fotografada por você.

| Arquivo | A cena |
|---|---|
| `18-rota-ao-vivo/prints/01-rota-recebida.png` | a lista com o grupo **ROTA** recém-chegado, mostrando os números dos pedidos e o *0 de N entregas* |
| `18-rota-ao-vivo/prints/02-primeira-parada.png` | os detalhes da primeira parada, com o endereço e o valor a cobrar |

**Como acontece:** eu crio os pedidos na sandbox pelo cardápio digital, monto a rota no painel e
despacho para o entregador **194115** (`BeeFood3 - Manual`). Você fotografa o que chega.

> **Importante:** nesta janela, **não rode** o `cenario-app-entregador.js`. Se os pedidos do
> gerador estiverem na lista junto com os meus, as duas fotos deixam de casar com o painel.
> Se já houver cenário de pé, limpe antes:
>
> ```powershell
> node scripts\cenario-app-entregador.js --empresa 38311 --filial 39202 --limpar
> ```

## Pacote 4 — Quando dá errado (4 prints)

O apêndice `02-o-que-o-app-nao-faz.md` afirma que **não há modo offline**, e o capítulo 01
mostra as permissões sendo **concedidas**. Falta o outro lado das duas coisas: é o que aparece na
tela quando o entregador liga para o restaurante reclamando.

| Arquivo | A cena | Como reproduzir |
|---|---|---|
| `19-falhas/prints/01-sem-internet-lista.png` | a lista sem carregar, com o app sem conexão | `adb shell svc wifi disable` (ou modo avião) e abrir a aba **Entregas** |
| `19-falhas/prints/02-sem-internet-cobranca.png` | a tentativa de registrar cobrança sem conexão — a mensagem que o app dá | mesma coisa, com um pedido do perfil `unico` já aberto nos detalhes |
| `19-falhas/prints/03-localizacao-recusada.png` | o que o app mostra quando a permissão de localização é **recusada** | `adb shell pm clear com.beetechentregador`, logar e escolher **Não permitir** |
| `19-falhas/prints/04-historico-vazio.png` | o histórico de quem ainda não entregou nada no dia | `--limpar` e abrir a aba **Histórico** |

Cenário sugerido para os dois primeiros:

```powershell
node scripts\cenario-app-entregador.js --empresa 38311 --filial 39202 --perfil unico
```

## Pacote 5 — iPhone (2 prints)

O pedido original fala de **Android e iOS**, e todo o material é emulador Android. Não preciso do
app inteiro em iOS: preciso o suficiente para o manual dizer, com honestidade, se a tela é a
mesma.

| Arquivo | A cena |
|---|---|
| `20-ios/prints/01-lista-entregas.png` | a lista de entregas no iPhone |
| `20-ios/prints/02-detalhes-entrega.png` | os detalhes de uma entrega no iPhone |

Se as telas forem iguais às do Android, o manual diz isso em uma linha e segue com as imagens
do Android. Se houver diferença de layout — barra do iOS, botão de voltar, altura do rodapé — as
duas imagens entram no manual. **Se não houver iPhone com o app à mão, pule este pacote** e me
diga: o manual passa a falar só de Android, sem prometer o que não conferimos.

---

## A janela combinada (pacotes 1, 2 e 3)

Uns 30 minutos, e o roteiro é este:

1. Você sobe o emulador, entra como `contato@beefood.com.br`, deixa o app **online** e me avisa.
   Se puder, fixe o GPS na loja: `adb emu geo fix -47.4657927 -23.5061438`.
2. Eu crio 3 pedidos na sandbox e **atribuo um** a você → você fotografa o **pacote 1**.
3. Eu monto a rota com os outros dois e **despacho** → você fotografa o **pacote 3**.
4. Eu **troco o entregador** de um deles → você fotografa o **pacote 2**.
5. Enquanto isso eu fotografo o painel do meu lado: o mapa com o seu pin **online**, o contador
   de entregadores disponíveis, o painel de rotas e o *ModalTrocarEntregador* com o selo
   **Online** — que hoje eu não consigo capturar, porque os 5 entregadores da filial estão
   offline e o mapa só tem o pin da loja.
6. No fim, você finaliza ou eu desfaço: combinamos na hora, para não deixar entrega aberta.

**Por que precisa ser junto:** o pin do entregador no mapa só existe com o app enviando posição,
e as duas metades do manual só valem se o número do pedido for o mesmo nas duas fotos.

## Como me entregar

Mesmo caminho que funcionou: **WeTransfer**, um zip só, com as pastas como estão nas tabelas
acima (`16-notificacoes/prints/…`, `17-troca-de-entregador/prints/…`, e assim por diante). Assim
os pacotes entram no material sem renomear nada, continuando a numeração dos 15 capítulos.

Duas coisas escritas que ajudam mais do que parecem:

1. **A versão do app** (a build que você usou) e a data — o manual precisa dizer de que app são
   as telas, porque as imagens do #57 envelheceram sem ninguém notar.
2. **Uma linha por print** dizendo o que aconteceu antes, se algo saiu diferente do pedido. Foi
   o que fez o material atual ser confiável: cada capítulo declara o que foi executado de verdade.

E o print, como sempre: **tela parada**, sem spinner, sem teclado aberto por acidente, e sem
notificação de outro app na barra de cima.
