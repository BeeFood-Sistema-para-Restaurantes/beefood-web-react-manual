# Carrossel 14 — API Aberta

- **Gênero:** novidade
- **Fonte:** [API Aberta liberada 🔌](https://beefood.app/novidades/api-aberta-liberada),
  13/10/2026 — e a **documentação**, em [`docs.beefood.app`](https://docs.beefood.app)
- **Manual:** não existe. O passo a passo do recurso é o próprio portal de
  desenvolvedores, que o release indica pelo nome
- **Medição:** `consultar-api.py` → `chamadas.json`. Toda chamada desta peça é
  real, contra a loja sandbox *BeeFood3 - Manual* (empresa 38311), pelo mesmo
  caminho que o parceiro percorre: credencial → `POST /v1/oauth/token` →
  `Authorization: Bearer`

## Em peça de integração, o release é a manchete e a documentação é a fonte

O release tem nove linhas e lista o que dá para integrar. Ele não diz como a
coisa funciona, e numa peça sobre API é exatamente isso que o leitor precisa
ver. A regra que a #13 deixou escrita na memória vale aqui pela primeira vez
com as duas fontes à mão, e o que veio de cada uma:

| Do release | Da documentação |
|---|---|
| que a API Aberta foi liberada, e para **toda loja com plano ativo** | que são **61 rotas de negócio** em cinco grupos, 29 delas de escrita |
| as áreas: Pedidos, Catálogo, Clientes, Loja, Cupons, Avaliações | que o **Catálogo** sozinho tem 33, e 24 escrevem |
| que existem webhooks de pedido, entrega e pagamento | que são **cinco eventos**, com nome, e que o webhook é "a alternativa recomendada ao polling" |
| que a ativação é em *Aplicativos → API Aberta* | que o token sai de `POST /v1/oauth/token` e vale 1 hora |
| que há exemplos e ambiente de testes | que o exemplo vem pronto em **treze linguagens** e que o sandbox é outro endereço (`api-sandbox.beefood.app`) |

## Fato → ângulo → o que o slide diz

| Fato | Ângulo | O que o slide diz |
|---|---|---|
| A API Aberta está disponível para toda loja com plano ativo; o sistema ou o parceiro da loja se integra direto ao BeeFood | o dono não programa, mas ele tem um outro sistema — e o que ele decide é **liberar** | capa: "**API Aberta**: o seu sistema lê e escreve no BeeFood" |
| A integração troca clientId e clientSecret por um token e chama as rotas de `/v1`; a resposta volta sempre no mesmo formato | o leitor nunca viu uma resposta de API, e é ela que mostra que o dado é o dele | 2: "O seu sistema pergunta. O BeeFood responde." |
| São 61 rotas de negócio; o Catálogo tem 33 e 24 delas alteram dado | "integrar" costuma ser entendido como exportar relatório; aqui o outro sistema **mexe** no cardápio | 3: "Catálogo: 24 das 33 rotas escrevem no cardápio" |
| Cinco eventos avisam a aplicação do parceiro: pedido criado, pedido alterado, entrega atualizada, pagamento criado, pagamento alterado | o contrário da integração que só funciona quando alguém aperta "atualizar" | 4: "Os webhooks avisam o seu sistema sem ninguém perguntar" |
| A permissão é por recurso e por ação — **Consultar** e **Alterar** —, e quem altera também consulta | entregar uma chave para terceiro assusta; o que desarma é que a chave só abre o que foi marcado | 5: "Você liga Consultar e Alterar em cada recurso" |
| A documentação é pública, traz o exemplo pronto em treze linguagens e tem ambiente de testes com endereço próprio | ninguém quer que o parceiro aprenda a integração em cima dos pedidos de sexta à noite | 6: "A documentação já traz o exemplo pronto" |
| A ativação é em *Aplicativos → API Aberta*: gerar a credencial e marcar as permissões | — | 7: "Libere o acesso do seu **sistema** hoje" |

## A capa: molde *nome do recurso como ganho*

Placar dos moldes antes desta peça — afirmação do fato 5, anúncio de chegada 3,
pergunta 2, nome + canal 1, nome + dois-pontos 1, nome + para quem 1; ordem
direta e antes × agora em 0.

A #13 abriu com **anúncio de chegada**, e a capa não repete a forma da anterior.
Os dois moldes zerados foram escritos e caíram:

- **ordem direta** saiu bem — *"Ligue o seu sistema ao BeeFood pela API
  Aberta"* — e brigou com o CTA. O molde de CTA da série é imperativo com
  "hoje", e duas ordens na mesma peça, uma na primeira tela e outra na última,
  é a mesma abertura duas vezes;
- **antes × agora** não tem "antes". O único par documentado é *polling × webhook*,
  que é vocabulário de quem integra, não do leitor — e inventar o "antes" do
  leitor é o erro que a #4 pagou.

Sobrou o molde que a memória já marcava como preferencial para este caso:
**a novidade cria uma capacidade que não existia no sistema, então a notícia é o
nome dela.** Fica *nome + dois-pontos* (placar 1 → 2), com o nome como sujeito —
não o canal, não o meio.

> **API Aberta**: o seu sistema lê e escreve no BeeFood
> Pedidos, cardápio e clientes — e um aviso automático a cada pedido novo.

O "lê e escreve" é o eixo que mais muda quem se interessa, e é o que a #13 quase
perdeu: metade da API altera dado. O vermelho pega o nome inteiro, porque é ele
que o leitor vai procurar em *Aplicativos*.

## Slide a slide

| # | Arquivo | Título | Imagem |
|---|---|---|---|
| 1 | `01-capa.html` | **API Aberta**: o seu sistema lê e escreve no BeeFood | o fluxo entradas → BeeFood → saídas, **desenhado** |
| 2 | `02-como-funciona.html` | O seu sistema pergunta. O BeeFood responde. | cartão de requisição e resposta, **desenhado** com a chamada real do `chamadas.json` |
| 3 | `03-catalogo.html` | **Catálogo**: 24 das 33 rotas escrevem no cardápio | a grade dos seis recursos liberados, **desenhada** |
| 4 | `04-webhooks.html` | Os **webhooks** avisam o seu sistema sem ninguém perguntar | o aviso saindo do pedido para o endereço do parceiro, **desenhado** |
| 5 | `05-permissoes.html` | Você liga **Consultar** e **Alterar** em cada recurso | `rec-permissoes.png` — **captura** da folha *Aplicativos → API Aberta* |
| 6 | `06-documentacao.html` | A **documentação** já traz o exemplo pronto | `rec-exemplo.png` — **captura** de `docs.beefood.app` |
| 7 | `07-cta.html` | Libere o acesso do seu **sistema** hoje | o mesmo fluxo da capa |

Lidos em fila, os sete títulos montam o recurso: ele lê e escreve, o seu sistema
pergunta e o BeeFood responde, o cardápio é a maior parte, os avisos chegam
sozinhos, a permissão é sua, a documentação está pronta, e dá para liberar hoje.
O slide 2 é a exceção da regra do nome — ele explica o que a capa acabou de
nomear.

## O que é captura e o que é desenho

Esta é a peça com mais desenho do acervo, e o motivo não é preguiça de capturar:
**o resultado da API Aberta acontece dentro do sistema do outro.** Não há tela
nossa que mostre um ERP recebendo pedido, e o pedido de quem encomendou a peça
foi justamente esse — *"aqui precisamos criar as imagens, ilustrar"*.

| Imagem | Origem |
|---|---|
| `.fluxo-api` (slides 1 e 7) | **desenho**, na composição da ilustração do alto de `docs.beefood.app` — referência de layout, como print de manual: nada foi recortado de lá |
| `.requisicao` (slide 2) | **desenho**, com a chamada e a resposta medidas pelo `consultar-api.py` |
| `.areas` (slide 3) | **desenho**, a mesma grade de tiques que a #13 trouxe da folha do MCP |
| `.aviso` (slide 4) | **desenho**, com os cinco `eventType` que a documentação publica |
| `rec-permissoes.png` (slide 5) | **captura** do painel, recortada no DOM |
| `rec-exemplo.png` (slide 6) | **captura** do portal de documentação |

O desenho não inventa comportamento: rótulo, nome de evento, nome de rota e
número saem da documentação ou da chamada real.

### O recorte do slide 5 começa abaixo da credencial

A folha abre com *Credencial principal*, e ali estão o Client ID e o campo do
Client Secret. **O repositório é público**, e credencial de loja em produção não
é credencial de sandbox descartável: o quadro começa na linha *Permissões* e
fecha em *Avaliações*. O que fica de fora não é só o segredo — é também o par
*Entregadores* e *Estoque*, que a tela mostra apagados, com a etiqueta **Em
breve**. Promessa não é assunto de peça de lançamento, e a #13 já tinha
descartado as mesmas duas linhas pelo mesmo motivo.

## O que ficou de fora

- **o campo da credencial, o botão de copiar e o CRIAR CREDENCIAL.** É a folha
  de configuração do recurso, e configuração não é imagem de carrossel — nem
  capturada, nem desenhada. O caminho vai escrito na pílula do CTA, que é onde
  ele serve;
- **as duas formas de autenticar.** A documentação separa *Integração direta*
  (client credentials, o lojista entrega a credencial) de *Conectar com BeeFood*
  (authorization code com PKCE, o lojista autoriza num botão do site da
  integradora). É a diferença mais interessante do recurso para quem integra, e
  é invisível para quem lê: nas duas o crachá é o mesmo e abre as mesmas portas.
  Fica na legenda;
- **o *Publicar aplicativo*.** A documentação tem uma página inteira para quem
  quer levar a própria ferramenta para dentro de *Aplicativos*. É outro leitor —
  o parceiro, não a loja — e, num carrossel só, atender os dois é não atender
  nenhum. Vale peça própria, no gênero função;
- **o formato de erro e a paginação** (`{"message", "status"}`, `page`, `limit`,
  `sort`). São as convenções que fazem a API ser previsível e não têm nada para
  mostrar: o leitor compra o que a integração passa a fazer;
- **os `Relatórios`** (5 rotas: resumo de pedidos, agrupado, vendas por setor,
  por produto, por opção). A #13 já é inteira sobre perguntar número ao sistema,
  e repetir o assunto aqui seria a peça irmã dizendo a mesma coisa com outra
  porta de entrada;
- **a data do pedido** na resposta do slide 2. O item real traz
  `createdAt`, `deliveryType` e `paidAmount` além dos cinco campos que o cartão
  mostra. Arte com data nasce velha, e o título do slide fala de status e valor —
  o cartão fecha onde a afirmação fecha, e o `…` no fim diz que há mais campo.

## A peça irmã

A #13 (MCP) saiu do release do **mesmo dia**, e as duas são a mesma porta vista
de dois lados: lá uma pessoa pergunta em português e a IA executa a chamada;
aqui o sistema do parceiro executa a chamada sozinho, sem ninguém na frente.

O que a #13 deixou de herança, e que esta peça usa:

- a grade `.areas`, que nasceu lá como bloco de capa e aqui vira o miolo do
  slide 3;
- a contagem de rotas por grupo, medida pelo `listar_endpoints` do servidor de
  documentação — é a mesma medição, e por isso os dois carrosséis não se
  contradizem: o `listar_endpoints` conta as **61 rotas de negócio**, e a home do
  portal mostra 69 porque soma as 7 de autenticação mais o *health check*;
- a lição de que **prova de escrita se faz, não se desenha**. Aqui ela foi
  cumprida de outro jeito: a resposta do slide 2 é uma chamada real, e o número
  do slide 3 é a contagem do próprio servidor.

O que **não** se reaproveita é o ângulo. Lá o leitor pergunta; aqui ele libera.
