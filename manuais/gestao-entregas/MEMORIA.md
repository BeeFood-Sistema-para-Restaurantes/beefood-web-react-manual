# MEMÓRIA — Gestão de Entregas (manual em preparação)

Pasta: `manuais/gestao-entregas/` · Manual: **ainda não escrito** · Numeração: **a definir**
Aberta em 18/09/2026, na conta sandbox **BeeFood3 - Manual**
(`contato@beefood.com.br`, `empresaID 38311`, `filialID 39202`).

**Estado: organização da casa.** Nada foi capturado, nada foi escrito e nada foi alterado no
sistema. Esta rodada só recebeu e organizou o material pronto que o dono enviou.

## Pedido do dono

> "quero começar um manual sobre gestão entregas 2.0 (vai se chamar gestao entregas). o gestão
> de entregas contempla: mapa no sistema para o operador gerenciar as entregas; aplicativo do
> entregador (android e ios); manuais do aplicativo entregador também. mas antes quero organizar
> uma pasta de conteudo pré criado de inspiração, fizemos um manual completo do app entregador
> pra que agora consigamos fazer todo o manual completo e juntar as peças. o manual atual do app
> entregador é apenas um print passo a passo de todas as funções."

## O escopo, em três partes

| Parte | O que é | Fonte de imagem |
|---|---|---|
| 1. Mapa no painel | `/gestao-entregas`: mapa ao vivo, painel de rotas, criar rota, despachar, trocar entregador, despacho automático | **capturável aqui**, em produção |
| 2. App do entregador | o que o motoboy vê no celular, do login à baixa da entrega | **só o material recebido** — sem emulador neste ambiente |
| 3. Juntar as peças | o mesmo pedido visto dos dois lados: o operador despacha, o entregador recebe | as duas fontes acima, casadas |

## O material recebido

Chegou por WeTransfer em 18/09/2026 e está em
[`material-recebido/`](material-recebido/README.md): **manual completo do app do entregador**,
15 capítulos, 63 prints de aparelho real, mais o estudo e os smoketests que o produziram.
Procedência, achados e as três correções de link estão no README de lá.

O material é **muito mais fundo** do que o pedido sugere ("apenas um print passo a passo"): tem
um arquivo de explicação por print, um capítulo por fluxo e um estudo que mediu o backend. Ele
resolve a parte 2 inteira e não toca nas partes 1 e 3.

## O que este repositório já tem sobre o assunto

| Onde | O que cobre | Relação com o manual novo |
|---|---|---|
| `manuais/app-entregadores/` (**#57**) | como **cadastrar** o entregador (funcionário + usuário), o código de barras no cupom e o uso no celular | **os prints do celular estão velhos**: são de uma versão anterior do app (cabeçalho branco, *FUNCIONÁRIO 1*, datas de 2024). O app de hoje é outro — cabeçalho preto, pílula **ONLINE**, abas no rodapé |
| `.cursor/skills/manual-sistema/references/planos/PLANO-ENTREGADOR.md` | estudo do bloco do entregador (taxa, pagamento, relatórios) | já apontava a **Gestão de Entregas como o maior buraco do bloco**, com estimativa de 1 a 2 manuais próprios, e listou o despacho do entregador próprio no Delivery e o lápis do *Valor do entregador* como lacunas vizinhas |
| `manuais/area-entrega-*` (**#35–#38**) | as quatro formas de área de entrega e a taxa | pré-requisito do cenário: sem área, o pedido não ganha coordenada |
| `manuais/integracao-*` e `entrega-facil-ifood` (**#59–#63**) | entrega **terceirizada** | fronteira: aqui o assunto é o entregador **próprio** |

## O que eu conferi no sistema (somente leitura)

**A tela do painel existe e está capturável.** `/gestao-entregas` abriu na conta sandbox com o
mapa (Leaflet) centrado na loja em Sorocaba, os quatro chips de situação
(*em preparação / prontos / em rota / entregues*), o painel **Rotas de entrega** à direita e o
rodapé de entregadores. Estado atual: **zero pedidos em andamento**, **5 entregadores offline**,
**despacho automático desligado**.

No código (`beefood-web-react`, commit `495326c`), o módulo é grande: `src/pages/GestaoEntregas.tsx`
mais **24 arquivos** em `src/components/gestao-entregas/` (~4.800 linhas), incluindo
`MapaEntregas`, `PainelLateral`, `ModalCriarRota`, `ModalDespachar`, `ModalTrocarEntregador` e
`ModalDespachoAutomatico`. O hook do painel é `useGestaoEntregasPainel.ts`.

## Restrições que já dão para escrever

1. **Não há como rodar o app do entregador aqui.** Sem emulador Android, e iOS está fora de
   qualquer hipótese. Print novo do app depende da máquina do dono.
2. **Mapa com entregador ao vivo depende do app rodando.** Os 5 entregadores estão offline; a
   posição no mapa só aparece com alguém online de verdade. Sem isso, a parte 1 mostra rota e
   despacho, mas não o pin do entregador se movendo.
3. **A referência técnica do módulo está em outro repositório** (`beetech-server-node-3.0`,
   `docs/gestao-entrega-2.0/`), que não temos e não conseguimos clonar — o `BITBUCKET_TOKEN` do
   ambiente não autentica mais. Se o fluxo do servidor for necessário, o caminho é o dono
   enviar a pasta, como fez com este material.
4. **Cenário custa escrita em produção.** Criar pedido para despachar é venda real na sandbox, e
   cobrança na rua exige caixa aberto na filial.

## Decisões pendentes com o dono

1. **Quantos manuais?** A parte 1 (painel) e a parte 2 (app) têm tamanhos muito diferentes;
   o `PLANO-ENTREGADOR.md` já estimava 1 a 2 só para o painel.
2. **Numeração.** O último usado é o **#103**; a fila continuaria em **#104**.
3. **O que fazer com o #57.** Ele tem cadastro (que continua válido) e prints velhos do app
   (que o material novo substitui): atualizar, apontar para o manual novo, ou aposentar.
4. **Como o material do app entra no manual.** Reaproveitar os prints como `imagens-puras` e
   anotar no padrão da casa, ou publicar os 15 capítulos como estão, à parte.

## Próximo passo

Escrever o plano do bloco em `references/planos/` (o fluxo da skill manda plano antes de
produção quando o bloco é grande), com o recorte dos manuais, o cenário necessário e o que
depende da máquina do dono.
