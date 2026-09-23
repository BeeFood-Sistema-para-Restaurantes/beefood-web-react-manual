# MEMÓRIA — Gestão de Entregas (a pasta de trabalho do bloco)

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `gestao-entregas.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Pasta: `manuais/gestao-entregas/` · Bloco: **#104 a #119** · Aberta em 18/09/2026, na conta sandbox
**BeeFood3 - Manual** (`contato@beefood.com.br`, `empresaID 38311`, `filialID 39202`, usuário
`88711`, entregador `funcionarioID 194115`).

**Esta pasta não é um manual.** Ela guarda o estudo, o material que o dono enviou, os scripts de
cenário e o pedido de fotos. Os manuais moram em pastas próprias, listadas em *O que foi entregue*,
no fim deste arquivo.

**Estado: bloco fechado. 16 manuais prontos, nenhum esqueleto.** #104 a #119, incluindo o **#117**,
que era o único pendente porque precisa das duas telas no mesmo pedido. Ele fechou em 19/09, quando as
fotos do celular chegaram da máquina do dono — a metade do painel foi **reencenada** depois, com os
mesmos três pedidos. Em [`pedidos/`](pedidos/README.md) **não há lista aberta**: uma segunda lista de
capturas foi escrita, empacotada e recusada na leitura pelo dono, porque pedia imagem de tela vazia.
O que sobrou dela é o critério, e está em *O que falta*.

O histórico das primeiras rodadas fica abaixo, porque é ele que explica as decisões: a primeira
organizou o material que o dono enviou; a segunda leu a documentação do backend e mediu o estado real
do módulo. **Nessas duas, nada foi alterado no sistema** — a autorização de cenário veio depois.

## Pedido do dono

> "quero começar um manual sobre gestão entregas 2.0 (vai se chamar gestao entregas). o gestão
> de entregas contempla: mapa no sistema para o operador gerenciar as entregas; aplicativo do
> entregador (android e ios); manuais do aplicativo entregador também."

E, na segunda rodada:

> "você vai criar todos os manuais e em cada manual será necessário criar um cenário manualmente.
> antes de mais nada, além do estudo atual que te passei do app entregador, quero que estude a
> nova funcionalidade lendo o backend `beetech-server-node-3.0\docs\gestao-entrega-2.0`. (…) leia
> tudo, entenda, crie a memoria desse manual (nao é pe fazer o manual ainda, estamos estudando)"

## O escopo, em três partes

| Parte | O que é | Fonte de imagem |
|---|---|---|
| 1. Mapa no painel | `/gestao-entregas`: mapa ao vivo, painel de rotas, criar rota, despachar, trocar entregador, despacho automático | **capturável aqui**, em produção |
| 2. App do entregador | o que o motoboy vê no celular, do login à baixa da entrega | **material recebido** + capturas novas pedidas ao dono |
| 3. Juntar as peças | o mesmo pedido visto dos dois lados: o operador despacha, o entregador recebe | as duas fontes acima, casadas |

## Onde está o estudo

| Arquivo | O que tem |
|---|---|
| [`estudo/01-como-o-sistema-funciona.md`](estudo/01-como-o-sistema-funciona.md) | a leitura completa de `docs/gestao-entrega-2.0` (~17.100 linhas): os quatro programas, os dois bancos, o ciclo da entrega, as dez operações de rota, as sete regras do despacho, o vocabulário de status, os quatro avisos de WhatsApp, e o que a doc promete e não existe |
| [`estudo/02-estado-medido.md`](estudo/02-estado-medido.md) | o que eu medi no sistema em 18/09, com evidência em `estudo/evidencias/` |
| [`material-recebido/README.md`](material-recebido/README.md) | procedência do manual do app que o dono enviou por WeTransfer: 15 capítulos, 63 prints, estudo e smoketests |
| [`pedidos/`](pedidos/README.md) | o pedido de captura. Na primeira rodada eram **12 prints em 5 pacotes**, deduzidos do material; depois de os manuais existirem virou **26 prints em 10 pastas**, deduzidos do que o texto descreve e não mostra |

## As dez coisas que o estudo mudou

Cada uma destas altera o manual, o cenário ou a promessa do texto. Resumo; o detalhe está nos
dois arquivos de estudo.

1. **A documentação do backend está acessível**, ao contrário do que esta memória dizia. Ela mora
   em `~/refs/beetech-server-node-2.0/docs/gestao-entrega-2.0/` — o clone é do `2.0`, a pasta é do
   `3.0`. Não era problema de acesso, era confusão de nome de repositório.
2. **A tela tem duas portas de entrada**, e a principal não é a rota própria: é o botão
   **`Entregas`** na barra do **Delivery**, que abre a Gestão de Entregas **dentro de um modal**
   sobre o Delivery. O manual tem de começar por ali, porque é onde o operador está.
3. **Despachar não é um rótulo.** Ele grava `ENTREGA` no ERP, e isso passa pelo
   `SituacaoDeliveryUpdater`: **avisa marketplace, imprime e enfileira WhatsApp**. Três frases do
   manual dependem de acertar isso.
4. **O despacho automático não despacha, e não age com a tela fechada.** Ele agrupa e associa
   entregador; o clique de despachar continua sendo do operador. E só age em filial onde alguém
   está com o painel aberto — é o `painel_heartbeat`, escrito pelo próprio `GET /painel`.
   **Conferido: o heartbeat foi gravado pela minha própria visita à tela.**
5. **"Melhor rota" no app desfaz a ordem do operador.** O app reordena por distância a partir da
   loja; a ordem que o painel montou some.
6. **As travas iniciais foram removidas de propósito.** Não dá para escrever "o sistema não
   permite": o dono preferiu dar liberdade ao operador e registrar tudo no log.
7. **O entregador `194115` está em uso de verdade** — 2.459 pings de GPS, o último **hoje**, app
   `3.3.0`, token de push ativo, 32 sessões de jornada. Isso derruba a restrição que eu havia
   registrado ("o pin no mapa exige app rodando e ninguém roda"): a janela combinada é viável.
8. **O módulo tem um cliente piloto e nada mais.** O Aurora `entregas` só tem dados de duas
   filiais (a sandbox e uma real), e o `despacho_config` tem **1 linha na base inteira** — a da
   sandbox, desligada. O manual será a primeira descrição do recurso para qualquer pessoa.
9. **Consigo ler os dois bancos e a API do app daqui.** Aurora `entregas`, MSSQL `notafacilb` com
   o usuário de leitura, e `GET /entrega2/gestao/entregador/...` com Basic Auth devolvendo o mesmo
   payload do celular. Isso torna a conferência de cenário barata. ⚠️ **O usuário do Aurora também
   tem escrita** — registrado, não usado, e não usarei sem o dono pedir.
10. **Há três sujeiras na sandbox que estragariam captura em silêncio:** a *rota fantasma* do
    `194115` (`rotaIDAtual = 120`, e a rota 120 não existe — ele nunca receberá rota do despacho
    automático), duas rotas abertas de 13/09 invisíveis no painel mas vivas no banco, e **nenhum
    caixa aberto** na filial, que é pré-requisito do capítulo de cobrança na rua.

## Achado para levar ao dono antes de escrever

**O aviso "Entregador próximo" (WhatsApp tipo 33) está ligado para a base toda e não dispara para
quase ninguém.** O campo de km na tela mostra `2`, mas esse `2` é o padrão do código:
`_WhatsappMsgTipoFilial.raioProximidadeMetros` está **NULL em 56.633 das 56.639 filiais**, e o
padrão global também está NULL. O próprio `010-raio-proximidade-na-notificacao.sql` diz que filial
com raio NULL **nunca recebe o aviso**, porque o cron pula. Só 6 filiais têm o valor, e chegaram lá
porque alguém abriu o modal e salvou. É problema de ambiente (o PASSO 3 do script não rodou), não
de manual — mas o manual não pode prometer um recurso que não funciona. Detalhe no
[`estudo/02-estado-medido.md`](estudo/02-estado-medido.md), §4.

## O que este repositório já tem sobre o assunto

| Onde | O que cobre | Relação com o manual novo |
|---|---|---|
| `manuais/app-entregadores/` (**#57**) | como **cadastrar** o entregador (funcionário + usuário), o código de barras no cupom e o uso no celular | **os prints do celular estão velhos**: versão anterior do app (cabeçalho branco, *FUNCIONÁRIO 1*, datas de 2024). O app de hoje é `3.3.0` — cabeçalho preto, pílula **ONLINE**, abas no rodapé |
| `.cursor/skills/manual-sistema/references/planos/PLANO-ENTREGADOR.md` | estudo do bloco do entregador (taxa, pagamento, relatórios) | já apontava a **Gestão de Entregas como o maior buraco do bloco**, com estimativa de 1 a 2 manuais próprios |
| `manuais/area-entrega-*` (**#35–#38**) | as quatro formas de área de entrega e a taxa | pré-requisito do cenário: sem área, o pedido não ganha coordenada e não vai para o mapa |
| `manuais/integracao-*` e `entrega-facil-ifood` (**#59–#63**) | entrega **terceirizada** | fronteira: aqui o assunto é o entregador **próprio** |

## Decisões do dono já registradas

1. ~~**Ainda não é para produzir o manual.**~~ Valeu nas duas primeiras rodadas, que foram organizar
   e estudar. **Revogada** na terceira: *"faça o manual sem parar, todas"*.
2. **O #57 será aposentado**, e não atualizado — o manual novo ocupa o lugar dele. Registrado na
   linha do #57 no `CHECKLIST-MANUAIS.md` e na `MEMORIA.md` daquele manual. **A remoção só
   acontece quando o manual novo estiver pronto**: aposentar antes deixaria o app sem manual.
3. **Capturas novas do app são possíveis** — o dono roda o emulador. O pedido está em
   [`pedidos/capturas-app.md`](pedidos/capturas-app.md) — refeito na terceira rodada, com o roteiro
   da janela combinada em [`pedidos/janela-117.md`](pedidos/janela-117.md), porque quem dispara é o
   painel.
4. **Cada manual vai exigir montar um cenário à mão.** É o enunciado da segunda rodada, e é o que
   torna o §8 do `02-estado-medido.md` a parte mais importante do planejamento.
5. **Autorização de cenário: concedida** (18/09). *"os testes vc terá que simular o entregador +
   criar as entregas, fazer tudo funcionar no modo fake"*. O módulo está em desenvolvimento e
   **ninguém usa ainda**, então escrever na sandbox não atropela trabalho de lojista.
6. **O entregador que estava online era o dono**, e ele saiu. Daqui para frente **quem simula
   entregador sou eu** — presença, posição e movimento.
7. **WhatsApp: assumir o funcionamento.** *"ainda não está em produção, podemos assumir o
   funcionamento tranquilamente e criar mensagens fakes no manual respectivo"*. O manual de avisos
   monta a mensagem em vez de esperar a entrega real chegar no celular.
8. **A lista de manuais foi aprovada e cresceu**: os 14 propostos (#104 a #117) mais os dois
   relatórios que o dono pediu depois (#118 e #119). A proposta original está em
   [`references/planos/PLANO-GESTAO-ENTREGAS.md`](../../.cursor/skills/manual-sistema/references/planos/PLANO-GESTAO-ENTREGAS.md).

## Como montar cenário (conferido em 18/09)

As quatro peças foram testadas de verdade antes de entrar no plano — não são caminho teórico:

| Peça | Como | Resultado medido |
|---|---|---|
| Pedido com endereço e coordenada | `node scripts/seed-gestao-entregas.js --empresa 38311 --filial 39202 --qtd N` no clone do backend | 4 pedidos criados (vendas 1036–1039), todos no painel; as 7 conferências do próprio script passaram |
| Presença do entregador | `POST https://app3.beetechapi.be/api/entrega2/gestao/presenca`, Basic `beetech:1q2w3e4r` | `{"resultado":true,"online":true,"status":"DISPONIVEL","alterado":true}` |
| Entregador **andando** | `INSERT` em `entregas.posicao` + `UPDATE entregador_status` (lat, lng, `dataHoraUltimaPosicao`, `distanciaLojaMetros`) | `posicaoIdadeMinutos` foi de 169 para **0** |
| Ler o painel sem navegador | `GET /api/entrega2/gestao/painel/38311/39202/88711` com JWT | 200 — loja, 5 entregadores, 2 rotas |

O **JWT do painel** sai do `localStorage` depois do login com Playwright: chave
`beefood_auth_token`, ofuscada por XOR com `bf2024_secure_key_token`. O `usuarioID` tem que ser o
88711; Basic Auth devolve **401** na rota do painel, embora funcione na de presença.

O `seed-gestao-entregas.js` tem lista branca literal para a 38311/39202, só deixa passar quatro
procedures, só dá `UPDATE` em `_PreVenda` com ID criado na própria execução, e tem `--dry-run`.
Rodar fora da sandbox exigiria editar o arquivo. **Não invente atalho: use o script.**

> **`beetech_leitura` engana pelo nome.** O usuário do MSSQL que todo o backend usa é
> `db_datareader` **+ `db_datawriter` + `db_ddladmin`**, com `EXECUTE` no banco inteiro. É por isso
> que o seeder funciona daqui. Trate como escrita em produção, porque é.

> O clone do backend não vem com `node_modules`. Antes da primeira execução:
> `cd ~/refs/beetech-server-node-2.0 && npm install --no-save mssql mysql2`.

> A **Lambda de rastreamento não é chamável daqui**: exige `x-api-key` guardada num `.env`
> gitignored. Escrever direto no Aurora chega ao mesmo estado, porque é o que a Lambda faz.

> Script Python não pode se chamar `token.py`: ele sombreia o módulo `token` da biblioteca padrão e
> o Playwright morre com um erro de importação circular que não parece ter nada a ver.

## Restrições que continuam valendo

1. **Não há como rodar o app do entregador aqui.** Sem emulador Android; iOS está fora de
   qualquer hipótese. É a única restrição que a autorização do dono **não** derrubou, e é o que
   separa os sete manuais que eu fecho sozinho dos seis que dependem de foto dele.
2. **Cenário custa escrita em produção.** Criar pedido é venda real na sandbox. O dono autorizou,
   mas cobrança na rua ainda exige **caixa aberto** na filial — e o `02-estado-medido.md` mediu
   que não há caixa aberto hoje.
3. **Criar rota exige JWT.** O app não cria rota: ela nasce no painel ou no despacho automático.
4. **A rota fantasma está viva no sandbox.** O entregador 194115 tem `rotaIDAtual = 120`, e a rota
   120 não existe — o efeito é um entregador ocupado para sempre, sem entrega nenhuma. Limpar
   antes de montar cenário. **Em loja real o lojista não resolve isso pela tela**: é bug, não
   assunto de manual.

## O que foi entregue

Dezesseis linhas de checklist, em cinco frentes. A numeração passou de #117 porque o dono
acrescentou dois relatórios no meio da rodada.

| Nº | Manual | Pasta |
|---|---|---|
| 104 | Liberar o entregador | [`gestao-entregas-liberar-entregador`](../gestao-entregas-liberar-entregador/gestao-entregas-liberar-entregador.md) |
| 105 | Ler o mapa e o painel de entregas | [`gestao-entregas-mapa-painel`](../gestao-entregas-mapa-painel/gestao-entregas-mapa-painel.md) |
| 106 | Montar a rota | [`gestao-entregas-montar-rota`](../gestao-entregas-montar-rota/gestao-entregas-montar-rota.md) |
| 107 | Despachar a rota e acompanhar | [`gestao-entregas-despachar`](../gestao-entregas-despachar/gestao-entregas-despachar.md) |
| 108 | Fechar a entrega no painel | [`gestao-entregas-fechar-entrega`](../gestao-entregas-fechar-entrega/gestao-entregas-fechar-entrega.md) |
| 109 | Despacho automático | [`gestao-entregas-despacho-automatico`](../gestao-entregas-despacho-automatico/gestao-entregas-despacho-automatico.md) |
| 110 | Avisos de WhatsApp da entrega | [`gestao-entregas-avisos-whatsapp`](../gestao-entregas-avisos-whatsapp/gestao-entregas-avisos-whatsapp.md) |
| 111 | App: entrar e ficar disponível | [`app-entregador-entrar`](../app-entregador-entrar/app-entregador-entrar.md) |
| 112 | App: as entregas do dia e o histórico | [`app-entregador-entregas-do-dia`](../app-entregador-entregas-do-dia/app-entregador-entregas-do-dia.md) |
| 113 | App: chegar no endereço | [`app-entregador-rota`](../app-entregador-rota/app-entregador-rota.md) |
| 114 | Código de barras: ligar e ler | [`app-entregador-codigo-barras`](../app-entregador-codigo-barras/app-entregador-codigo-barras.md) |
| 115 | App: pedido de iFood e de 99Food | [`app-entregador-marketplace`](../app-entregador-marketplace/app-entregador-marketplace.md) |
| 116 | App: receber na porta | [`app-entregador-cobranca`](../app-entregador-cobranca/app-entregador-cobranca.md) |
| 117 | Uma entrega do começo ao fim | [`gestao-entregas-ciclo-completo`](../gestao-entregas-ciclo-completo/gestao-entregas-ciclo-completo.md) — ✅ 13 imagens |
| 118 | Relatório Operação de Entrega | [`relatorio-operacao-entrega`](../relatorio-operacao-entrega/relatorio-operacao-entrega.md) |
| 119 | Quanto o entregador recebe (Taxa / KM) | [`entregador-quanto-recebe`](../entregador-quanto-recebe/entregador-quanto-recebe.md) |

Os **#118** e **#119** não estavam no plano. Entraram porque o dono pediu no meio da rodada — o
primeiro filtrado na data de hoje contra o cenário que eu mesmo montei, e o segundo cobrindo as
**três fontes** do valor do entregador, que era a parte que ele destacou.

### O que sobrou nesta pasta

| Onde | O que é |
|---|---|
| [`estudo/`](estudo/) | as duas leituras da primeira rodada: como o módulo funciona e o que eu medi |
| [`material-recebido/`](material-recebido/README.md) | as duas rodadas que o dono enviou por WeTransfer: 15 capítulos e 63 prints, mais os [24 da segunda rodada](material-recebido/app-entregador/capturas-2/README.md) |
| [`pedidos/`](pedidos/README.md) | o pedido das 26 capturas (**respondido**), o roteiro da janela do #117, o kit que vai para quem fotografa e o registro do pedido que foi **recusado na leitura** |
| [`scripts/`](scripts/README.md) | `cenario.js` (o painel) e `smoke-app.js` (o app) |

## O que falta

**Nada, e nada está pedido.** Das 26 capturas pedidas, 24 chegaram em 19/09 e as 2 de iPhone foram
canceladas pelo dono — o manual não usa imagem de iOS. As 6 que bloqueavam o #117 saíram; as demais
viraram seção nova em quatro manuais do aplicativo, e o `## O que falta` de cada um dos seis diz hoje
**"nada"**.

### A segunda lista de capturas existiu e foi recusada na leitura

Fechado o bloco, escrevi uma lista nova de 6 prints, empacotei o kit e versionei o zip. O dono leu e
abortou antes de delegar:

> *"que tipo de manual estamos fazendo? pra que vamos ter uma sessão e uma imagem mostrando 'Nenhum
> pedido'? o manual deve ser util e não ter um monte de conteudo sem sentido."*

**Ele está certo, e o erro é de critério, não de execução.** As três coisas que a lista pedia tinham a
mesma falha: existiam porque o aplicativo tem aquele estado, não porque alguém precisa daquela
resposta.

| O que eu pedi | Por que não servia |
|---|---|
| o histórico **de verdade vazio** | ninguém abre manual para ver como é a tela quando não há nada nela |
| o app **abrindo sem rede** | não há o que fazer com a resposta: sem rede o entregador já sabe que está sem rede |
| as **faixas de resultado** da leitura, uma foto para cada | são seis mensagens curtas; a tabela do #114 é mais útil que quatro fotos quase iguais de uma faixa colorida |

O que saiu junto, e é o que dá o tamanho do erro: uma **imagem já publicada** (a lista sem rede do
#112, que era uma lista normal com três etiquetas explicando que era normal), **dois comandos de
script** (`historico-zerar` e `historico-voltar`, que apagavam o histórico inteiro do entregador só
para produzir a tela vazia) e a engenharia de pedido que eu tinha montado para viabilizar as fotos —
cena virtual do emulador, `assembleRelease`, separação por risco de decodificação. Tudo correto, tudo
a serviço de imagem que não devia ter sido pedida. **A pergunta certa vem antes de "consigo produzir
esta imagem?", e é "alguém precisa dela?"**

O critério que ficou está na
[memória geral](../../.cursor/skills/manual-sistema/references/MEMORIA-GERAL.md), na regra 0 das boas
práticas de imagem, e é uma pergunta: **o leitor sai daí fazendo algo diferente?** A seção *Quando a
cobrança não fecha* do #116 passa — quatro telas, quatro ações, dinheiro em jogo. A janela *Despacho
não confirmado* do #113 passa — manda ligar para a loja e avisa para não tocar de novo. Tela de
ausência não passa.

Uma coisa se salvou, e aponta para onde olhar primeiro na próxima vez. Relendo o estudo de fonte que
já estava no material da primeira rodada
(`material-recebido/app-entregador/estudo/01-o-que-o-app-faz-hoje.md`, seção 2.10), a faixa de status
do leitor tem **seis** mensagens, e o #114 listava cinco: faltava ***Erro: {mensagem}***, que é o
servidor recusando, caso diferente de *Erro na leitura, tente novamente*, que é o envio que não saiu.
A distinção decide o que o entregador faz, e o manual foi corrigido. **A correção real do dia saiu de
reler o que já estava no disco**, não de pedir foto nova.

**A única imagem composta do bloco fica, declarada.** O #114 sobrepôs a etiqueta dentro da faixa da
câmera porque o emulador não tem câmera, e isso está escrito no `fluxo-codigo.md` dele. Trocá-la por
uma real seria melhor; mandar alguém montar um pôster de cena virtual para isso não é proporcional ao
ganho, e a declaração é honesta.

O receio que justificava a janela combinada — *o manual mostra números de pedido diferentes de cada
lado* — não se concretizou, e por um motivo que só apareceu ao medir: **o número do pedido não
aparece na lista nem nos detalhes do aplicativo**. O crachá laranja de lá vem só com o `#`, porque lê
`numeroPedido`, nulo em pedido do restaurante. O número existe numa tela só, a de pagamento, que lê
`numeroPreVenda`. Foi o que permitiu reencenar o painel depois, em vez de fotografar os dois lados na
mesma hora: o que amarra as duas metades é endereço, valor, forma de pagamento, letra da rota e hora
da baixa — e esses o #117 fez concordarem.

Fora de foto, ficou registrado um recado que **não é manual**: a *rota fantasma*. O entregador
`194115` está com `rotaIDAtual` apontando para uma rota que não existe, o que o deixa ocupado para
sempre aos olhos do despacho automático. Em loja real o lojista não resolve isso pela tela — é bug. O
`limpar-fantasma` do `cenario.js` conserta na sandbox.
