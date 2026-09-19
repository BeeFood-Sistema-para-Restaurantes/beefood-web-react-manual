# Manuais do App do Entregador — Gestão de Entregas 2.0

Documentação de uso do **app do entregador** (BeeFood Entregador), tela por tela, com capturas
feitas no emulador Android contra a filial de teste **38311 / 39202**.

São **15 capítulos**, um por fluxo. Cada pasta traz o `manual.md` do fluxo, os prints em
`prints/` e **um arquivo de explicação por print**, nomeado como ele.

---

## Índice

| # | Capítulo | O que cobre |
|---|---|---|
| 01 | [Primeiros passos](01-primeiros-passos/manual.md) | permissões, login, senha visível, erro de credencial, lista vazia |
| 02 | [Disponibilidade](02-disponibilidade/manual.md) | online, pausa e offline — e o que o restaurante vê |
| 03 | [Lista de entregas](03-lista-de-entregas/manual.md) | o card do pedido, previsão, "Cobrar R$", atualizar |
| 04 | [Detalhes da entrega](04-detalhes-da-entrega/manual.md) | endereço fixo, complemento, observação, itens e a tarja de conferência |
| 05 | [Ver no mapa](05-ver-no-mapa/manual.md) | abrir uma entrega no Google Maps ou no Waze |
| 06 | [Rota do restaurante](06-rota-do-restaurante/manual.md) | grupo de rota, INICIAR ROTA, ABRIR NO MAPS, outras entregas |
| 07 | [Melhor rota](07-melhor-rota/manual.md) | várias entregas soltas na melhor ordem |
| 08 | [Código de barras](08-codigo-de-barras/manual.md) | ler a etiqueta do pedido no balcão — e por que isso despacha |
| 09 | [Pedido iFood](09-pedido-ifood/manual.md) | chip, localizador e a confirmação no site do iFood |
| 10 | [Pedido 99Food](10-pedido-99food/manual.md) | chip, código e a confirmação no site do 99Food |
| 11 | [Cobrança na porta](11-cobranca-na-porta/manual.md) | forma de pagamento, bandeira, troco, confirmação |
| 12 | [Divisão de conta](12-divisao-de-conta/manual.md) | dividir o valor e registrar uma forma por pessoa |
| 13 | [Finalizar sem cobrar](13-finalizar-sem-cobrar/manual.md) | baixa sem dinheiro, com conferência e observação |
| 14 | [Histórico](14-historico/manual.md) | o que você entregou, dia por dia |
| 15 | [Ajustes e sair](15-ajustes-e-sair/manual.md) | menu, permissões do aparelho, encerrar a sessão |

**Apêndices**

| Documento | O que traz |
|---|---|
| [`apendices/01-notificacoes.md`](apendices/01-notificacoes.md) | como o app avisa de entrega nova e o que acontece ao tocar |
| [`apendices/02-o-que-o-app-nao-faz.md`](apendices/02-o-que-o-app-nao-faz.md) | o que não existe na tela, para não procurar |

**Bastidores**

| Documento | O que traz |
|---|---|
| [`estudo/`](estudo/) | o estudo que definiu o plano: o que o app faz hoje, a evolução por commits e os cenários |
| [`smoketests/`](smoketests/README.md) | como recriar cada cenário e refazer as capturas |

---

## Como ler

Comece pelo `manual.md` do capítulo: ele conta o fluxo inteiro, com as capturas na ordem em que
as telas aparecem. Cada captura tem um link para o arquivo que a explica em detalhe — o que é
cada elemento, o que fazer e o que costuma dar errado ali.

Todo capítulo termina com **Como este capítulo foi produzido**, dizendo o que foi executado de
verdade e o que foi ilustrado. Nenhuma captura é mockup, com uma única exceção declarada no
próprio capítulo (a etiqueta dentro da faixa da câmera, no capítulo 08).

## O pedido-padrão dos exemplos

Todo pedido do manual é **1x Combo One Burger**, com **One Burger + Batata frita + Coca Cola
350ml** dentro. É sempre o mesmo, de propósito: você reconhece o pedido de um capítulo para
outro e repara no que muda — a forma de pagamento, a situação, o complemento do endereço.

Os IDs e preços saíram de pedidos reais desta loja, e é por isso que **só a Coca Cola tem
destaque de conferência**: a tarja preta aparece no manual exatamente onde ela aparece na vida
real.

## O que foi executado de verdade

| Operação | Onde | Efeito real |
|---|---|---|
| Login e permissões | cap. 01 | sessão de verdade, com o usuário 88711 |
| Despacho de rota | cap. 06 | três pedidos de *PRONTO/PREPARO* para *ENTREGA* |
| Leitura de código de barras | cap. 08 | pedido #1028 de *PREPARO* para *ENTREGA*, pela mesma rota que o leitor chama |
| Cobrança simples | cap. 11 | R$ 46,00 em dinheiro registrados no caixa; pedido *ENTREGUE* |
| Conta dividida | cap. 12 | duas linhas de pagamento (PIX + dinheiro) no mesmo pedido |
| Finalizar sem cobrar | cap. 13 | pedido *ENTREGUE*, com observação de entrega |
| Confirmação iFood / 99Food | cap. 09 e 10 | os sites das plataformas carregados no app; as etapas **não** concluídas (pedido de teste não existe lá) |

## Ambiente usado

| Item | Valor |
|---|---|
| Emulador | `Pixel_7_Pro` (`emulator-5554`), Android 15, locale pt-BR, GPS em Sorocaba |
| App | `com.beetechentregador`, build de desenvolvimento com Metro |
| API | `app.beetechapi.be` (login, 2.0) e `app3.beetechapi.be` (entregas, pagamento, histórico, 3.0) |
| Filial | empresa **38311**, filial **39202** |
| Sessão | `contato@beefood.com.br` — usuário 88711, entregador 194115 (`BeeFood3 - Manual`) |

Referência técnica do módulo: `beetech-server-node-3.0/docs/gestao-entrega-2.0/`, em especial
`16-app-entregador-na-rota.md`, `21-pagamento-na-rua.md`, `22-api-pagamento-app.md` e
`23-api-entregas-e-historico-app.md`.
