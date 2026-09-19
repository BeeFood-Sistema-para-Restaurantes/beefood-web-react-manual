# capturas-2 — a segunda rodada de prints do aplicativo

24 prints tirados em **19/09/2026, entre 02h e 04h**, na máquina do dono, em resposta ao pedido de
[`../../../pedidos/capturas-app.md`](../../../pedidos/capturas-app.md). Foram feitos por outra IA,
com o kit [`kit-teste-app-entregador.zip`](../../../pedidos/kit-teste-app-entregador.zip) — o
relatório dela está em [`RELATORIO.md`](RELATORIO.md) e vale ler antes de usar qualquer imagem
daqui.

| | |
|---|---|
| App | BeeFood Entregador `3.3.0` — build Android `1.0.1.2`, `versionCode 24`, rodando com o Metro |
| Aparelho | emulador `Pixel_7_Pro` (AVD), Android 15, `sdk_gphone64_x86_64`, locale pt-BR |
| Ambiente | empresa 38311 / filial 39202 / entregador 194115 (`BeeFood3 - Manual`) |
| Formato | PNG 1440x3120, tela inteira, sem recorte |

## As pastas

| Pasta | Prints | Vai para |
|---|--:|---|
| `16-notificacoes/` | 2 | #112, seção do aviso que chega |
| `17-troca-de-entregador/` | 2 | #112, *Uma entrega desapareceu sem eu fazer nada* |
| `18-ciclo-completo/` | 6 | **#117**, a metade do celular da janela combinada |
| `19-sem-internet/` | 2 | #112 e #115 |
| `20-permissao-e-presenca/` | 2 | #111, seção 5 e o FAQ da pílula |
| `21-listas-vazias/` | 2 | #111 e #112 |
| `22-erros-de-cobranca/` | 4 | #116, o FAQ inteiro |
| `23-rota-com-problema/` | 3 | #113, as três perguntas do FAQ |
| `24-plataforma-sem-confirmacao/` | 1 | #115, última pergunta |
| `_triagem/` | 3 | telas de trabalho que entraram no material (veja abaixo) |

## Três coisas para ler antes de usar

**`21-listas-vazias/prints/02-historico-vazio.png` não é o histórico vazio.** O nome vem do pedido;
a tela mostra o Histórico **com 22 entregas em três dias**. O caso `historico-vazio` desatribui os
pedidos do entregador, e o histórico dele continuou com o que já estava lá de dias anteriores. A
imagem é boa — só é outra coisa: o Histórico agrupado por dia. O *Nenhuma entrega no período*
continua pedido.

**`23-rota-com-problema/prints/02-falha-melhor-rota.png` mostra outra mensagem.** Com a rede
desligada, o MELHOR ROTA responde **Permissão necessária**, não *Ocorreu uma falha ao gerar a melhor
rota*. Não é erro de captura: é como o `try/catch` do app trata rede e GPS no mesmo `catch`. O #113
passou a responder a pergunta com as duas mensagens.

**O número do pedido não aparece em tela nenhuma do aplicativo.** O crachá laranja dos cartões e dos
detalhes traz só o `#`, sem número — o número de pedido é vocabulário do painel. Foi medido nestes
prints, e é o que decidiu como o #117 amarra as duas metades: endereço, valor, forma de pagamento,
letra da rota e hora da baixa.

## Os três prints da triagem

A IA entregou, além dos 24, uma pasta `_triagem/` com 145 telas de trabalho. Três delas entraram no
material porque contam algo que os 24 não contam:

| Arquivo | Por que ficou |
|---|---|
| `_triagem/prints/lista-antes.png` | a lista com **4** entregas, o *antes* que faltava no par da troca de entregador |
| `_triagem/prints/pos22.png` | o alerta *Pagamento registrado — Finalize a entrega* ao voltar para os detalhes |
| `_triagem/prints/pos22d.png` | o *Não foi possível dar baixa*, que é o laço em que o suporte cai |

As outras 142 ficaram fora do repositório: são variações da mesma tela, e material que não entra em
manual não precisa ser versionado.
