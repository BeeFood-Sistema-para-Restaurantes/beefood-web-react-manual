# MEMÓRIA — Gestão de Entregas (manual em preparação)

Pasta: `manuais/gestao-entregas/` · Manual: **ainda não escrito** · Numeração: **#104**
Aberta em 18/09/2026, na conta sandbox **BeeFood3 - Manual**
(`contato@beefood.com.br`, `empresaID 38311`, `filialID 39202`, usuário `88711`,
entregador `funcionarioID 194115`).

**Estado: estudo.** Nada foi capturado para manual, nada foi escrito para o usuário e **nada foi
alterado no sistema**. Duas rodadas até aqui: a primeira organizou o material que o dono enviou;
a segunda leu a documentação do backend e mediu o estado real do módulo.

    10|## Pedido do dono

> "quero começar um manual sobre gestão entregas 2.0 (vai se chamar gestao entregas). o gestão
> de entregas contempla: mapa no sistema para o operador gerenciar as entregas; aplicativo do
> entregador (android e ios); manuais do aplicativo entregador também."

E, na segunda rodada:

> "você vai criar todos os manuais e em cada manual será necessário criar um cenário manualmente.
> antes de mais nada, além do estudo atual que te passei do app entregador, quero que estude a
> nova funcionalidade lendo o backend `beetech-server-node-3.0\docs\gestao-entrega-2.0`. (…) leia
    20|> tudo, entenda, crie a memoria desse manual (nao é pe fazer o manual ainda, estamos estudando)"

## O escopo, em três partes

| Parte | O que é | Fonte de imagem |
|---|---|---|
| 1. Mapa no painel | `/gestao-entregas`: mapa ao vivo, painel de rotas, criar rota, despachar, trocar entregador, despacho automático | **capturável aqui**, em produção |
| 2. App do entregador | o que o motoboy vê no celular, do login à baixa da entrega | **material recebido** + capturas novas pedidas ao dono |
| 3. Juntar as peças | o mesmo pedido visto dos dois lados: o operador despacha, o entregador recebe | as duas fontes acima, casadas |

## Onde está o estudo

    30|| Arquivo | O que tem |
|---|---|
| [`estudo/01-como-o-sistema-funciona.md`](estudo/01-como-o-sistema-funciona.md) | a leitura completa de `docs/gestao-entrega-2.0` (~17.100 linhas): os quatro programas, os dois bancos, o ciclo da entrega, as dez operações de rota, as sete regras do despacho, o vocabulário de status, os quatro avisos de WhatsApp, e o que a doc promete e não existe |
| [`estudo/02-estado-medido.md`](estudo/02-estado-medido.md) | o que eu medi no sistema em 18/09, com evidência em `estudo/evidencias/` |
| [`material-recebido/README.md`](material-recebido/README.md) | procedência do manual do app que o dono enviou por WeTransfer: 15 capítulos, 63 prints, estudo e smoketests |
| [`pedidos/capturas-app.md`](pedidos/capturas-app.md) | o pedido de **12 prints em 5 pacotes** para o dono capturar no emulador |

## As dez coisas que o estudo mudou

Cada uma destas altera o manual, o cenário ou a promessa do texto. Resumo; o detalhe está nos
dois arquivos de estudo.

    40|1. **A documentação do backend está acessível**, ao contrário do que esta memória dizia. Ela mora
   em `~/refs/beetech-server-node-2.0/docs/gestao-entrega-2.0/` — o clone é do `2.0`, a pasta é do
   `3.0`. Não era problema de acesso, era confusão de nome de repositório.
2. **A tela tem duas portas de entrada**, e a principal não é a rota própria: é o botão
   **`Entregas`** na barra do **Delivery**, que abre a Gestão de Entregas **dentro de um modal**
   sobre o Delivery. O manual tem de começar por ali, porque é onde o operador está.
3. **Despachar não é um rótulo.** Ele grava `ENTREGA` no ERP, e isso passa pelo
   `SituacaoDeliveryUpdater`: **avisa marketplace, imprime e enfileira WhatsApp**. Três frases do
   manual dependem de acertar isso.
4. **O despacho automático não despacha, e não age com a tela fechada.** Ele agrupa e associa
    50|   entregador; o clique de despachar continua sendo do operador. E só age em filial onde alguém
   está com o painel aberto — é o `painel_heartbeat`, escrito pelo próprio `GET /painel`.
   **Conferido: o heartbeat foi gravado pela minha própria visita à tela.**
5. **"Melhor rota" no app desfaz a ordem do operador.** O app reordena por distância a partir da
   loja; a ordem que o painel montou some.
6. **As travas iniciais foram removidas de propósito.** Não dá para escrever "o sistema não
   permite": o dono preferiu dar liberdade ao operador e registrar tudo no log.
7. **O entregador `194115` está em uso de verdade** — 2.459 pings de GPS, o último **hoje**, app
   `3.3.0`, token de push ativo, 32 sessões de jornada. Isso derruba a restrição que eu havia
   registrado ("o pin no mapa exige app rodando e ninguém roda"): a janela combinada é viável.
    60|8. **O módulo tem um cliente piloto e nada mais.** O Aurora `entregas` só tem dados de duas
   filiais (a sandbox e uma real), e o `despacho_config` tem **1 linha na base inteira** — a da
   sandbox, desligada. O manual será a primeira descrição do recurso para qualquer pessoa.
9. **Consigo ler os dois bancos e a API do app daqui.** Aurora `entregas`, MSSQL `notafacilb` com
   o usuário de leitura, e `GET /entrega2/gestao/entregador/...` com Basic Auth devolvendo o mesmo
   payload do celular. Isso torna a conferência de cenário barata. ⚠️ **O usuário do Aurora também
   tem escrita** — registrado, não usado, e não usarei sem o dono pedir.
10. **Há três sujeiras na sandbox que estragariam captura em silêncio:** a *rota fantasma* do
    `194115` (`rotaIDAtual = 120`, e a rota 120 não existe — ele nunca receberá rota do despacho
    automático), duas rotas abertas de 13/09 invisíveis no painel mas vivas no banco, e **nenhum
    70|    caixa aberto** na filial, que é pré-requisito do capítulo de cobrança na rua.

## Achado para levar ao dono antes de escrever

**O aviso "Entregador próximo" (WhatsApp tipo 33) está ligado para a base toda e não dispara para
quase ninguém.** O campo de km na tela mostra `2`, mas esse `2` é o padrão do código:
`_WhatsappMsgTipoFilial.raioProximidadeMetros` está **NULL em 56.630 das 56.636 filiais**, e o
padrão global também está NULL. O próprio `010-raio-proximidade-na-notificacao.sql` diz que filial
com raio NULL **nunca recebe o aviso**, porque o cron pula. Só 6 filiais têm o valor, e chegaram lá
porque alguém abriu o modal e salvou. É problema de ambiente (o PASSO 3 do script não rodou), não
de manual — mas o manual não pode prometer um recurso que não funciona. Detalhe no
[`estudo/02-estado-medido.md`](estudo/02-estado-medido.md), §4.
    80|
## O que este repositório já tem sobre o assunto

| Onde | O que cobre | Relação com o manual novo |
|---|---|---|
| `manuais/app-entregadores/` (**#57**) | como **cadastrar** o entregador (funcionário + usuário), o código de barras no cupom e o uso no celular | **os prints do celular estão velhos**: versão anterior do app (cabeçalho branco, *FUNCIONÁRIO 1*, datas de 2024). O app de hoje é `3.3.0` — cabeçalho preto, pílula **ONLINE**, abas no rodapé |
| `.cursor/skills/manual-sistema/references/planos/PLANO-ENTREGADOR.md` | estudo do bloco do entregador (taxa, pagamento, relatórios) | já apontava a **Gestão de Entregas como o maior buraco do bloco**, com estimativa de 1 a 2 manuais próprios |
| `manuais/area-entrega-*` (**#35–#38**) | as quatro formas de área de entrega e a taxa | pré-requisito do cenário: sem área, o pedido não ganha coordenada e não vai para o mapa |
| `manuais/integracao-*` e `entrega-facil-ifood` (**#59–#63**) | entrega **terceirizada** | fronteira: aqui o assunto é o entregador **próprio** |

## Decisões do dono já registradas

    90|1. **Ainda não é para produzir o manual.** Recorte, numeração e plano ficam para quando ele
   retomar. As duas rodadas até agora foram organizar e estudar.
2. **O #57 será aposentado**, e não atualizado — o manual novo ocupa o lugar dele. Registrado na
   linha do #57 no `CHECKLIST-MANUAIS.md` e na `MEMORIA.md` daquele manual. **A remoção só
   acontece quando o manual novo estiver pronto**: aposentar antes deixaria o app sem manual.
3. **Capturas novas do app são possíveis** — o dono roda o emulador. O pedido está em
   [`pedidos/capturas-app.md`](pedidos/capturas-app.md): 12 prints em 5 pacotes, três deles numa
   janela combinada, porque quem dispara é o painel.
4. **Cada manual vai exigir montar um cenário à mão.** É o enunciado da segunda rodada, e é o que
   torna o §8 do `02-estado-medido.md` a parte mais importante do planejamento.
   100|
## Restrições que continuam valendo

1. **Não há como rodar o app do entregador aqui.** Sem emulador Android; iOS está fora de
   qualquer hipótese.
2. **Pin de entregador se movendo no mapa exige alguém online** no momento da captura — janela
   combinada com o dono.
3. **Cenário custa escrita em produção.** Criar pedido para despachar é venda real na sandbox, e
   cobrança na rua exige caixa aberto na filial, com lançamento em caixa real.
4. **Criar rota exige JWT.** O app não cria rota: ela nasce no painel ou no despacho automático.

   110|## Próximo passo

Duas perguntas para o dono, e nenhuma delas é de execução:

1. **O recorte.** O painel sozinho dá pano para 3 ou 4 manuais (ler o mapa; montar e despachar
   rota; despacho automático; os avisos de WhatsApp de entrega), e o app já tem 15 capítulos
   escritos no material recebido. Quantos manuais, e em que ordem?
2. **A autorização para montar cenário.** Semear pedido, criar rota e abrir caixa são escritas em
   produção na sandbox. O estudo que ele mesmo enviou já pedia essa decisão em seis itens; agora
   ela também vale para mim.

   120|Quando ele decidir, o fluxo da skill manda escrever o plano do bloco em `references/planos/`
antes de produzir, porque o bloco é grande.
