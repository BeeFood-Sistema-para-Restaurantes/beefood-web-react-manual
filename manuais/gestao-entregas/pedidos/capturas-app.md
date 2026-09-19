# Capturas do app que faltam — 26 prints, em 10 pastas

Para o dono, em resposta a *"aguardo a pasta com todas imagens necessárias + scripts completos, te
entrego e vc finaliza"*.

Escrito em 18/09/2026, **depois** de os seis manuais do app estarem escritos. É a diferença que
importa: a rodada anterior deste arquivo pedia 12 prints por dedução, lendo os 15 capítulos que
você mandou. Esta pede o que os manuais **publicados** descrevem por texto e não mostram — cada
linha da tabela aponta a pergunta ou a seção que ganharia a foto.

> Substitui a lista de 12 prints em 5 pacotes da primeira rodada. Os 12 continuam válidos: onze
> deles estão aqui, com nome de arquivo novo, e o que sobrou (*iPhone*) virou a pasta 25.

## O que muda de verdade, e o que só melhora

| | Prints | Efeito |
|---|--:|---|
| **Bloqueia manual** | 6 | sem eles o **#117** não existe — é o manual que mostra o mesmo pedido nas duas telas |
| **Melhora manual publicado** | 18 | o texto já descreve a cena; a foto poupa o leitor de imaginar |
| **Fecha uma promessa** | 2 | o material promete Android **e iOS**, e tudo que temos é emulador Android |

Ou seja: **seis são obrigatórios**, vinte são bons de ter. Se der tempo para uma coisa só, faça a
pasta 18 — ela é a janela combinada, e é a única que precisa de mim ao mesmo tempo que de você.

## O script que monta cada cena

Nenhuma destas telas aparece clicando à toa. Pedido de marketplace já pago, pedido com saldo zero,
histórico com mais de um dia, rota chegando ao vivo — cada uma é um estado de banco. Por isso vem
com script:

```
manuais/gestao-entregas/scripts/smoke-app.js
```

Ele monta, **confere pela API do próprio app** e desmonta. A conferência é a parte que interessa:
ela responde se a tela está pronta para fotografar, em vez de você descobrir depois que a foto saiu
com quatro pedidos quando devia ter um.

```powershell
node smoke-app.js casos                     # a lista, com a foto de cada caso
node smoke-app.js preparar --caso pago       # monta e confere
node smoke-app.js conferir                   # confere de novo, quantas vezes quiser
node smoke-app.js limpar                     # tira tudo da tela do app
```

Ele lê host e senha do clone do backend, como o `cenario.js` ao lado — nada de credencial no
arquivo. Se o clone não estiver no lugar padrão, passe `--backend C:\caminho\beetech-server-node`.

A coluna **caso** das tabelas abaixo é o `--caso` que você roda antes de fotografar. Onde está
escrito *(eu)*, quem roda sou eu, do painel: a cena depende de uma ação do operador.

---

## 18. O ciclo completo — os 6 que bloqueiam o #117

Esta é a pasta que importa. O #117 mostra **o mesmo pedido** nas duas telas, com **o mesmo
número**, e não dá para montar por partes: ou as duas metades são fotografadas na mesma janela, ou
o manual mente. O roteiro das sete fases está em [`janela-117.md`](janela-117.md); aqui ficam só os
arquivos que eu preciso receber.

| Arquivo | A cena | Fase | Caso |
|---|---|--:|---|
| `18-ciclo-completo/prints/01-rota-recebida.png` | a lista com o grupo **ROTA** recém-chegado, mostrando *0 de 3* e os três números | 2 | (eu) |
| `18-ciclo-completo/prints/02-em-rota.png` | o cabeçalho da rota depois do despacho: etiqueta **em rota** e o botão **ABRIR NO MAPS** | 3 | (eu) |
| `18-ciclo-completo/prints/03-primeira-parada.png` | os detalhes da primeira parada, com endereço e **Cobrar R$** | 3 | (eu) |
| `18-ciclo-completo/prints/04-cobranca-concluida.png` | a tela de sucesso depois de registrar o pagamento da primeira | 5 | você |
| `18-ciclo-completo/prints/05-lista-sem-a-rota.png` | a lista depois da terceira entrega, sem o grupo da rota | 6 | você |
| `18-ciclo-completo/prints/06-historico-do-dia.png` | o **Histórico** do dia com as três entregas | 7 | você |

**Anote os três números do pedido.** Eles têm de aparecer nas fotos dos dois lados — é o que faz o
manual ser verdade em vez de montagem. A fase 1 do script imprime os números na tela.

---

## 16. Notificação chegando (2)

O apêndice de notificações é um dos textos mais úteis do material que você mandou, e é o único
**sem nenhuma imagem**. Quem lê *"o aviso aparece mesmo com o app aberto"* merece ver o aviso.

| Arquivo | A cena | Onde entra | Caso |
|---|---|---|---|
| `16-notificacoes/prints/01-aviso-chegando.png` | o aviso do BeeFood Entregador **na tela**, com a lista por baixo | apêndice `01-notificacoes.md` | `notificacao` (eu) |
| `16-notificacoes/prints/02-lista-depois-do-toque.png` | logo depois de tocar: aba **Entregas** em foco, já com a entrega nova | idem | idem |

O app precisa estar **online** e com a permissão de notificações **Ativa** (capítulo 15). O disparo
sai do servidor no instante em que eu atribuo o pedido — então é uma janela de segundos, e vale
deixar o celular na mão antes de eu rodar.

> Se o token FCM não registrar no emulador (o seu `estudo/` já marcou isso como "melhor esforço"),
> tente no aparelho físico. Se não sair em nenhum dos dois, me diga: o apêndice fica sem imagem, e
> o manual explica por texto — foi o que fizemos com o tablet no #103.

## 17. Entrega tirada do entregador (2)

É a pergunta que todo motoboy faz — *"sumiu uma entrega da minha lista"* — e a foto que fecha o
assunto **Trocar entregador** do painel.

| Arquivo | A cena | Onde entra | Caso |
|---|---|---|---|
| `17-troca-de-entregador/prints/01-aviso-de-remocao.png` | o aviso chegando, dizendo que a entrega saiu | #112, *Uma entrega desapareceu sem eu fazer nada* | `troca` (eu) |
| `17-troca-de-entregador/prints/02-lista-sem-o-pedido.png` | a lista depois, **sem** aquele pedido | idem | idem |

Fotografe a lista **com** o pedido antes de eu rodar, se puder: o par antes/depois é o que prova a
história, e o "antes" você tira sozinho.

---

## 19. Sem internet (2)

O apêndice `02-o-que-o-app-nao-faz.md` afirma que **não existe modo offline**. É a afirmação mais
consultada pelo suporte e a única sem foto.

| Arquivo | A cena | Onde entra | Como chegar |
|---|---|---|---|
| `19-sem-internet/prints/01-lista-sem-carregar.png` | a lista sem carregar, app sem conexão | #112 | `--caso lista`, depois `adb shell svc wifi disable` e abrir **Entregas** |
| `19-sem-internet/prints/02-plataforma-nao-carrega.png` | a tela de confirmação do iFood/99Food branca ou carregando | #115, *A tela da plataforma não carrega* | `--caso marketplace`, wifi desligado, e tocar no botão de confirmar |

## 20. Permissão e presença (2)

O capítulo 01 mostra as permissões sendo **concedidas**. Falta o outro lado, que é exatamente o
caso em que o entregador liga para o restaurante.

| Arquivo | A cena | Onde entra | Como chegar |
|---|---|---|---|
| `20-permissao-e-presenca/prints/01-localizacao-recusada.png` | a tela de **Permissões** com a localização em *Inativa* | #111, seção 5 | `adb shell pm clear com.beetechentregador`, entrar e escolher **Não permitir** |
| `20-permissao-e-presenca/prints/02-pilula-sem-nuvem.png` | a pílula de disponibilidade com o ícone de **nuvem cortada** | #111, *A pílula não fica ONLINE* | tocar na pílula com o wifi desligado |

## 21. As duas listas vazias (2)

| Arquivo | A cena | Onde entra | Caso |
|---|---|---|---|
| `21-listas-vazias/prints/01-entregas-vazia.png` | a aba **Entregas** sem nenhuma entrega | #111, #112 | `historico-vazio` |
| `21-listas-vazias/prints/02-historico-vazio.png` | o **Histórico** com *Nenhuma entrega no período* | #112, *O histórico está vazio* | idem |

Um comando produz as duas: o caso desatribui tudo o que estiver na sua lista e a conferência só
passa com as duas telas limpas.

## 22. Erros de cobrança (4)

O FAQ do #116 tem quatro respostas que o suporte usa toda semana e nenhuma tem foto. Juntas, elas
transformariam o FAQ numa seção ilustrada.

| Arquivo | A cena | Onde entra | Como chegar |
|---|---|---|---|
| `22-erros-de-cobranca/prints/01-soma-precisa-fechar.png` | o aviso vermelho da divisão, quando as partes não somam o total | #116, seção 3 | `--caso lista`, dividir em 2 e mudar um valor à mão |
| `22-erros-de-cobranca/prints/02-nao-foi-possivel-cobrar.png` | a mensagem de erro do servidor ao confirmar | #116, *Erro ao confirmar* | `--caso lista`, desligar o wifi **entre** escolher a forma e confirmar |
| `22-erros-de-cobranca/prints/03-pedido-ja-pago.png` | a folha **Pedido já pago** | #116, pergunta do mesmo nome | `--caso pago`, abrir os detalhes e tentar cobrar |
| `22-erros-de-cobranca/prints/04-falta-finalizar.png` | o aviso de que o pagamento entrou e a baixa não | #116, *Registrou o pagamento e a entrega continuou na lista* | o mais difícil: cortar a rede **depois** de o pagamento sair e antes de a baixa voltar |

> O último é o único que talvez não saia. Se não sair em duas tentativas, pule: o texto já explica
> o que fazer, e foto de corrida entre dois pedidos HTTP é sorte, não roteiro.

## 23. Rota com problema (3)

| Arquivo | A cena | Onde entra | Caso |
|---|---|---|---|
| `23-rota-com-problema/prints/01-despacho-nao-confirmado.png` | a mensagem **Despacho não confirmado** depois do INICIAR ROTA | #113, pergunta do mesmo nome | `rota-viva`, com o wifi caindo no toque |
| `23-rota-com-problema/prints/02-falha-melhor-rota.png` | **Ocorreu uma falha ao gerar a melhor rota** | #113, pergunta sobre a falha do cálculo | `lista` com wifi desligado, e tocar em **MELHOR ROTA** |
| `23-rota-com-problema/prints/03-duas-rotas.png` | duas rotas na mesma lista, **A** e **B** | #113, *Tenho duas rotas na tela* | (eu) — monto duas rotas para você no painel |

## 24. Plataforma sem confirmação (1)

| Arquivo | A cena | Onde entra | Caso |
|---|---|---|---|
| `24-plataforma-sem-confirmacao/prints/01-selo-keeta.png` | um pedido de plataforma **sem** botão de confirmação — só o selo | #115, última pergunta | `keeta` |

É a foto que prova a última frase do #115: nem toda plataforma tem confirmação no app. O caso monta
um pedido Keeta e a conferência garante que nenhum iFood ou 99Food sobrou na tela, para o selo
aparecer sozinho.

## 25. iPhone (2)

| Arquivo | A cena |
|---|---|
| `25-ios/prints/01-lista-entregas.png` | a lista de entregas no iPhone |
| `25-ios/prints/02-detalhes-entrega.png` | os detalhes de uma entrega no iPhone |

Não preciso do app inteiro em iOS: preciso do suficiente para o manual dizer, com honestidade, se a
tela é a mesma. Se for igual, o manual diz isso em uma linha e segue com as imagens do Android. Se
houver diferença de layout — barra do iOS, botão de voltar, altura do rodapé — as duas entram nos
manuais. **Sem iPhone à mão, pule e me diga**: o manual passa a falar só de Android, sem prometer o
que não conferimos.

---

## Como me entregar

Mesmo caminho que funcionou: **WeTransfer**, um zip só, com as pastas exatamente como estão nas
tabelas. Assim os prints entram no material sem renomear nada, continuando a numeração dos 15
capítulos que você já mandou.

```
capturas-2/
├── 16-notificacoes/prints/            01-aviso-chegando.png  02-lista-depois-do-toque.png
├── 17-troca-de-entregador/prints/     01-aviso-de-remocao.png  02-lista-sem-o-pedido.png
├── 18-ciclo-completo/prints/          01-rota-recebida.png  02-em-rota.png  03-primeira-parada.png
│                                      04-cobranca-concluida.png  05-lista-sem-a-rota.png
│                                      06-historico-do-dia.png
├── 19-sem-internet/prints/            01-lista-sem-carregar.png  02-plataforma-nao-carrega.png
├── 20-permissao-e-presenca/prints/    01-localizacao-recusada.png  02-pilula-sem-nuvem.png
├── 21-listas-vazias/prints/           01-entregas-vazia.png  02-historico-vazio.png
├── 22-erros-de-cobranca/prints/       01-soma-precisa-fechar.png  02-nao-foi-possivel-cobrar.png
│                                      03-pedido-ja-pago.png  04-falta-finalizar.png
├── 23-rota-com-problema/prints/       01-despacho-nao-confirmado.png  02-falha-melhor-rota.png
│                                      03-duas-rotas.png
├── 24-plataforma-sem-confirmacao/prints/  01-selo-keeta.png
└── 25-ios/prints/                     01-lista-entregas.png  02-detalhes-entrega.png
```

Duas coisas escritas que ajudam mais do que parecem:

1. **A versão do app** e a data. O manual precisa dizer de que build são as telas — as imagens do
   #57 envelheceram sem ninguém notar, e é o erro que não quero repetir.
2. **Uma linha por print** dizendo o que aconteceu antes, quando algo saiu diferente do pedido. Foi
   o que fez o material atual ser confiável: cada capítulo declara o que foi executado de verdade.

E o print, como sempre: **tela parada**, sem *spinner*, sem teclado aberto por acidente, e sem
notificação de outro app na barra de cima — exceto na pasta 16, onde a notificação **é** o assunto.

## Se nada disso chegar

Os seis manuais do app estão publicáveis hoje, e o `MEMORIA.md` de cada um já registra qual foto
falta e onde ela entraria. O único que não existe sem foto é o **#117** — e ele está escrito como
esqueleto, com o texto pronto e o lugar de cada imagem marcado, esperando a janela.
