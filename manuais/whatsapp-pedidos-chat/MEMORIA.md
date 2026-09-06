# MEMORIA.md — #83 Pedidos pelo chat no WhatsApp

## Escopo
Primeiro manual da série WhatsApp: como **ligar o Pedido Chat** no BeeBot e como
o cliente fecha o pedido conversando. Produzido em 06/09/2026.

Não cobre: conectar o número (QR Code), notificações de status, respostas
automáticas por palavra-chave, campanhas, IA ChatGPT (#58) nem o resumo diário.

## Origem
Pedido do dono: *WhatsApp → pedidos pelo chat*. Sem WhatsApp conectado no
sandbox BeeFood3; o painel `bot.beefood.com.br` abre e o interruptor dá para
fotografar. O diálogo do cliente foi simulado na API
`POST https://chat.beetechapi.be/api/rest/tchatfluxo/validaFluxo` na filial
**3408** (empresa 3271) e virado em mockup de WhatsApp.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-beefood-whatsapp.png` | setas | `/whatsapp` desconectado + **Abrir Conversas WhatsApp** |
| `02-login-bot.png` | contexto | Login `bot.beefood.com.br` |
| `03-pedido-chat.png` | setas | Recorte da coluna: switch **Pedido Chat** ligado |
| `04-whatsapp-iniciar.png` | contexto (tira) | Celulares 1 e 2: começar + escolher produto |
| `05-whatsapp-finalizar.png` | contexto (tira) | Celulares 3 e 4: grupos/carrinho + resumo |

Puras individuais `w1`–`w4` e `02-dashboard-bot.png` ficam de fonte. A lista de
conversas do BeeBot teve nome/telefone ofuscados para **Cliente** (repositório
público).

## Decisões
- **Não** conectar o WhatsApp do sandbox (o dono avisou que não há número).
- Interruptor `beeBotBeeChatPedido` (`#beeBotBeeChatPedido`) grava sozinho.
  Toast: *Pedido via Chat ativado com sucesso.* Na primeira exploração o rótulo
  foi clicado e **desligou** o switch; foi religado na hora. Não repetir: o
  clique no **rótulo** também alterna.
- Fluxo da API (telefone `11959572150`, nome *Testes pedido*): `fazer pedido` →
  setor 1 (Burger) → produto 3 (Junior Burger R$ 20) → ponto *Ao ponto* → Coca
  350 ml → 1 unidade → finalizar → **Retirada** → observação 1 → **Dinheiro**
  → resumo R$ 20. No resumo, **2** (cancelar) devolveu o texto de
  “pedido enviado” (cadastro `chatAcaoNv1ID=6` / chatFluxoID 32910 usa a mesma
  frase do sucesso). **Não confirmar o pedido** (não gravar venda na 3271).
- Celulares: HTML + Playwright 390×844 DPR 2, no padrão da `MEMORIA-GERAL`
  (tira `montar_celulares`, 2+2 porque quatro numa tira aperta).
- Login do BeeBot aceita `contato@beefood.com.br` / `1q2w3e4r` (mesmo do
  BeeFood3). O host redireciona `bot.beefood.com.br` → `bot2.beefood.com.br`.
- Badge **Pedidos Chat** em `WhatsAppConexaoCard` só aparece com instância
  conectando/conectada. Com a loja desconectada, o caminho é o botão
  **Abrir Conversas WhatsApp**.

## SEO / FAQ (06/09, pedido do dono)
Texto de abertura e H2 passaram a falar **pedido pelo WhatsApp**, BeeBot e
cardápio digital — o que o restaurante pesquisa. FAQ com pergunta completa
(padrão do #33): ativar, diferença da IA, o que escrever, Delivery, grupos,
entrega/retirada, atendente, preço, WhatsApp conectado, desligar, vários
itens, loja fechada, PIX, resumo, caixa. Sem afirmar cupom no chat (o fluxo
`validaFluxo` não mostrou cupom). Loja fechada aponta para Respostas, sem
garantir que o Pedido Chat bloqueia sozinho.

## Status
Concluído — aguardando publicação do dono.
