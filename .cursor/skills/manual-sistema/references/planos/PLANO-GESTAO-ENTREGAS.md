# Plano — bloco Gestão de Entregas 2.0

> Pedido do dono em **18/09/2026**, depois de mandar o material do app e de eu ler o backend:
> *"funcionalidade está em desenvolvimento, ngm ta usando ainda / o entregador online sou eu, vou
> sair / whatsapp, ainda não está em produção, podemos assumir o funcionamento tranquilamente e
> criar mensagens fakes no manual respectivo / os testes vc terá que simular o entregador + criar
> as entregas, fazer tudo funcionar no modo fake. agora me passe a lista de manuais que iremos
> fazer."*

Status: ✅ **entregue em 19/09/2026 — 16 manuais, #104 a #119.** A lista de catorze foi aprovada e
executada; os **dois relatórios** que o dono pediu no meio da rodada (#118 Operação de Entrega e
#119 Entregador Taxa/KM) entraram por cima dela. O #104 de hoje no checklist (uma linha só para "o
módulo inteiro") foi substituído por esta divisão.

**O que o plano previu errado, e vale ler antes de planejar o próximo bloco:**

| O plano dizia | Como foi |
|---|---|
| **12 capturas** do app faltando | foram **26** pedidas, porque a lista real só apareceu depois de os seis manuais existirem. Chegaram 24; as 2 de iPhone foram canceladas pelo dono, que decidiu que o manual não usa imagem de iOS |
| o **#117** exige uma janela coordenada, o dono no emulador e eu no painel ao mesmo tempo | a janela foi dispensável. O celular fotografou primeiro e o painel foi **reencenado depois**, restaurando no banco o estado de cada fase, porque o que amarra as duas metades é endereço, valor e hora — não número de pedido |
| seis manuais **dependem** de foto do emulador | dependiam do miolo, não do todo: os seis ficaram publicáveis antes das fotos, e cada `MEMORIA.md` registrava qual imagem faltava e em que pergunta ela entraria |

Depois da entrega ainda houve uma **segunda lista de capturas**, que o dono recusou na leitura
porque pedia imagem de tela vazia. O critério que saiu dela é a **regra 0** das boas práticas de
imagem da [`MEMORIA-GERAL.md`](../MEMORIA-GERAL.md): imagem entra se o leitor sair dela fazendo algo
diferente.

---

## 1. Resumo em cinco linhas

A Gestão de Entregas 2.0 é grande demais para um manual e pequena demais para virar quarenta: o
recorte que funciona é **por pergunta que o lojista faz**, e são catorze. Cinco são do operador
diante do mapa, seis são do motoboy com o celular na mão, uma prepara o terreno (cadastro e
liberação), uma é a tela de avisos de WhatsApp e a última mostra o mesmo pedido pelos dois lados ao
mesmo tempo. Sete eu fecho sozinho, porque **provei hoje que consigo criar o cenário inteiro daqui**
— pedido, entregador, GPS e despacho. Seis dependem de fotos do emulador que já pedi em
`manuais/gestao-entregas/pedidos/capturas-app.md`. E o #57, o manual antigo do app, é aposentado
pelo #104, que herda a parte dele que continua valendo.

---

## 2. O que mudou com a autorização do dono

Antes desta mensagem, o bloco estava travado em duas perguntas: *posso escrever no sandbox?* e *o
que faço com o WhatsApp, que não está em produção?* As duas foram respondidas, e uma terceira coisa
mudou de figura.

| Antes | Agora |
|---|---|
| Não sabia se podia criar pedido de teste | **Pode.** Ninguém usa o módulo ainda |
| O entregador online era um mistério no painel | Era o dono. Ele saiu, e **eu simulo** |
| WhatsApp sem prova possível | **Assumir o funcionamento** e montar mensagem fake no manual |
| Cenário talvez dependesse do dono | **Cenário é meu**: pedido, entregador e movimento |

A terceira é a que mais muda o plano. Eu conferi o caminho de escrita antes de escrever este
documento, porque prometer cenário sem saber se consigo montá-lo seria prometer no vazio:

| Peça do cenário | Como monto | Conferido em 18/09 |
|---|---|---|
| Pedido de delivery com endereço e coordenada | `scripts/seed-gestao-entregas.js` do backend, com lista branca na 38311/39202 | ✅ 4 pedidos criados (vendas 1036–1039), todos no painel |
| Entregador online / em pausa / offline | `POST /api/entrega2/gestao/presenca` com Basic Auth | ✅ `{"resultado":true,"alterado":true}` |
| Entregador **andando** no mapa | `INSERT` em `entregas.posicao` + `UPDATE` em `entregador_status`, igual à Lambda | ✅ `posicaoIdadeMinutos` caiu para 0 |
| Ler o painel sem abrir o navegador | `GET /api/entrega2/gestao/painel/...` com o JWT do painel | ✅ 200, 5 entregadores e 2 rotas |
| Criar/despachar rota | pela tela, que é o que o manual mostra de todo jeito | — |

> **A Lambda de rastreamento eu não consigo chamar**: ela exige `x-api-key` que mora num `.env`
> gitignored. Escrever direto no Aurora chega ao mesmo resultado — é literalmente o que a Lambda
> faz — e não depende de segredo que eu não tenho.

---

## 3. A lista

### Bloco 1 — Preparar o terreno (1 manual)

| Nº | Manual | O que entra | Cenário |
|---|---|---|---|
| **104** | **Liberar o entregador: cadastro, acesso ao app e código de barras** | Funcionário com a função *Entregador*, usuário de acesso com os *Aplicativos* ligados, o que o app exige para o login funcionar, e o código de barras no cupom | Cadastrar um entregador novo na hora, do zero |

Este manual **herda a Parte 1 do #57** (que continua correta — são telas do painel, não do app) com
prints novos, e é o que permite **aposentar o #57**: a Parte 2 dele mostra um app que não existe mais.
Enquanto o #104 não estiver pronto, o #57 fica no ar para não abrir buraco.

### Bloco 2 — O painel do operador (5 manuais)

| Nº | Manual | O que entra | Cenário |
|---|---|---|---|
| **105** | **Ler o mapa e o painel de entregas** | As duas portas de entrada (`/gestao-entregas` e o botão *Entregas* no Delivery), o que cada pino significa, os quatro chips de situação, os grupos do painel lateral, o rodapé de entregadores, a busca e o tema | 4 a 6 pedidos em situações diferentes + 1 entregador online perto da loja |
| **106** | **Montar a rota: agrupar, ordenar e escolher o entregador** | Selecionar pedidos, criar rota, escolher o entregador, arrastar paradas, *otimizar ordem*, adicionar e remover pedido, mover pedido entre rotas, marcar como pronto | 4 pedidos prontos, 2 perto e 2 longe, para a ordem importar |
| **107** | **Despachar a rota e acompanhar no mapa** | O que o despacho **dispara de verdade** (situação no Delivery, impressão, marketplace, WhatsApp), o aviso do modal, trocar de entregador no meio, excluir rota | Rota montada + entregador que eu faço andar da loja até a primeira parada |
| **108** | **Fechar a entrega no painel** | Baixa por parada, finalizar a rota inteira, o grupo *Entregues*, a rota concluída que fica colapsada e some depois, e como o pedido aparece no Delivery depois | Rota despachada com 3 paradas, baixando uma por vez |
| **109** | **Despacho automático: as sete regras** | As sete regras do modal, ligar e desligar, a etiqueta *Automático* na rota, e as duas coisas que ele **não** faz: não despacha o pedido e só roda com a tela aberta | Despacho ligado + pedidos agrupáveis + entregador dentro do raio |

O **107** é o manual mais delicado do bloco, e por um motivo que o dono precisa saber antes de
aprovar: despachar não é um botão de organização interna, é o gatilho que **avisa o cliente, o
marketplace e a impressora**. Um manual que trate isso como "clique em despachar" ensina o operador
a disparar coisa irreversível sem perceber.

O **109** tem a mesma armadilha ao contrário: o despacho automático **agrupa e escolhe entregador,
mas não despacha** — de propósito, para não disparar aviso sozinho. Quem ler esperando entrega
automática de ponta a ponta vai achar que está quebrado.

### Bloco 3 — Os avisos (1 manual)

| Nº | Manual | O que entra | Cenário |
|---|---|---|---|
| **110** | **Avisos de WhatsApp da entrega** | Os quatro avisos (entrega nova, entrega cancelada e relatório do dia para o entregador; *entregador está chegando* para o cliente), onde configurar, o campo de distância em km, e as variáveis de cada mensagem | A tela de notificações automáticas + **mensagens fake**, como o dono autorizou |

Aqui vale registrar uma coisa que **medi e que não é opinião**: o campo
`raioProximidadeMetros` está **nulo em praticamente todas as filiais**, e o padrão global também.
A tela mostra "2 km" e parece configurada, mas o cron pula quem está nulo — então hoje o aviso de
*entregador está chegando* não sairia para ninguém. O manual precisa mandar **salvar a tela uma vez**
para gravar o valor, e isso vira uma seção, não uma nota de pé de página.

### Bloco 4 — O app do entregador (6 manuais)

Os quinze capítulos do material que o dono mandou viram seis manuais. Quinze manuais de três fotos
cada seriam quinze páginas que ninguém acha; seis são seis perguntas que o motoboy faz de verdade.

| Nº | Manual | Capítulos do material | Fotos que já tenho |
|---|---|---|---|
| **111** | **App do entregador: instalar, entrar e ficar disponível** | 01 primeiros passos, 02 disponibilidade, 15 ajustes e sair | 15 |
| **112** | **App do entregador: as entregas do dia e o histórico** | 03 lista de entregas, 04 detalhes da entrega, 14 histórico | 8 |
| **113** | **App do entregador: chegar no endereço** | 05 ver no mapa, 06 rota do restaurante, 07 melhor rota | 8 |
| **114** | **App do entregador: confirmar a entrega pelo código de barras** | 08 código de barras | 3 |
| **115** | **App do entregador: pedido de iFood e de 99Food** | 09 pedido iFood, 10 pedido 99Food | 8 |
| **116** | **App do entregador: receber na porta** | 11 cobrança na porta, 12 divisão de conta, 13 finalizar sem cobrar | 20 |

São **63 fotos** já em mãos, o que cobre o miolo dos seis. O que falta são **12 capturas** que já
estão pedidas em `manuais/gestao-entregas/pedidos/capturas-app.md` — as telas que só existem com o
painel agindo ao mesmo tempo (rota chegando no app, troca de entregador, entrega cancelada).

> **Eu não consigo tirar foto do app daqui.** O Cloud Agent não roda emulador Android. Estes seis
> manuais avançam até o limite do material recebido e param onde faltar foto — não há como contornar
> isso do meu lado.

### Bloco 5 — Juntar as peças (1 manual)

| Nº | Manual | O que entra | Cenário |
|---|---|---|---|
| **117** | **Uma entrega do começo ao fim: painel e app lado a lado** | O mesmo pedido nas duas telas: operador monta a rota → motoboy recebe → operador despacha → motoboy anda → cliente é avisado → motoboy dá baixa → o painel muda | O mais caro de todos: os dois lados ao vivo, no mesmo pedido |

É o manual que o dono descreveu como *"juntar as peças"*, e o único que **não dá para fazer por
partes**: ou as duas telas são capturadas no mesmo pedido e no mesmo minuto, ou o manual mente. Ele
é o último da fila por isso, e depende das capturas coordenadas do pedido de fotos.

---

## 4. O que eu fecho sozinho, e o que depende do dono

| Manuais | Dependência |
|---|---|
| #104 a #110 | **Nenhuma.** Cenário, cadastro e prints são meus |
| #111 a #116 | Fotos do emulador (12 capturas já pedidas) |
| #117 | Janela coordenada: o dono no emulador, eu no painel |

Sete manuais podem começar hoje. É o que sugiro: rodar o bloco do painel inteiro enquanto as fotos
do app não chegam, e deixar o #117 por último, quando os dois lados já estiverem documentados
separadamente.

---

## 5. O que fica de fora, e por quê

Três coisas apareceram no estudo do backend e **não viram manual agora**, porque manual de
funcionalidade que não existe é manual que nasce errado:

| Assunto | Por que fica fora |
|---|---|
| **Notificação push no app** | Fase 8, ainda não construída. Exige build novo do app |
| **Pagamento na rua pelo app** | A API existe no servidor, mas o app precisa de tela — os capítulos 11 a 13 do material cobrem a cobrança que **já** existe |
| **Analytics e KPIs de entrega** | Fase 7, ainda um mapa de ideias. Só 35% dos pedidos têm entregador atribuído, então relatório hoje mediria o vazio |

Sobrou também um item que **não é manual, é recado**: a rota fantasma. O entregador 194115 está com
`rotaIDAtual = 120`, e a rota 120 não existe. A documentação diz que isso foi corrigido, mas o
sandbox mostra o contrário, e o efeito prático é um entregador que fica ocupado para sempre sem ter
entrega nenhuma. Vou limpar antes de montar cenário, mas **se isso acontece em loja real, o lojista
não tem como resolver pela tela** — e isso é bug, não assunto de manual.

---

## 6. Ordem sugerida

1. **#104** — sem entregador cadastrado nada funciona, e ele destrava a aposentadoria do #57
2. **#105** — a tela em repouso, base de vocabulário para os quatro seguintes
3. **#106**, **#107**, **#108** — o fluxo do operador na ordem em que ele acontece
4. **#109** e **#110** — as duas telas de configuração
5. **#111** a **#116** — o app, à medida que as fotos chegarem
6. **#117** — por último, com os dois lados já documentados

---

## 7. Base deste plano

| Fonte | O que rendeu |
|---|---|
| `beetech-server-node-3.0/docs/gestao-entrega-2.0/` (21 docs, 13 prompts, 14 SQL) | Como o módulo funciona de verdade — em `manuais/gestao-entregas/estudo/01-como-o-sistema-funciona.md` |
| Sandbox medido em 18/09 (Aurora, MSSQL, API e tela) | O que está no ar e o que não está — em `estudo/02-estado-medido.md` |
| Material do app mandado pelo dono (15 capítulos, 63 fotos) | O miolo do bloco 4 — em `material-recebido/` |
| Manual #57 | A Parte 1 que o #104 herda, e a Parte 2 que é aposentada |
