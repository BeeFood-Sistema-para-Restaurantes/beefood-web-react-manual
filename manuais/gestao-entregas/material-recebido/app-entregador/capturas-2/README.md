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
| `19-sem-internet/` | 2 | #115; a do #112 foi publicada e **depois retirada** (veja abaixo) |
| `20-permissao-e-presenca/` | 2 | #111, seção 5 e o FAQ da pílula |
| `21-listas-vazias/` | 2 | #111 e #112 |
| `22-erros-de-cobranca/` | 4 | #116, o FAQ inteiro |
| `23-rota-com-problema/` | 3 | #113, as três perguntas do FAQ |
| `24-plataforma-sem-confirmacao/` | 1 | #115, última pergunta |
| `_triagem/` | 3 | telas de trabalho que entraram no material (veja abaixo) |

A pasta `25-ios/` do pedido **não existe aqui, e não vai existir**: não havia iPhone nem simulador iOS
na máquina, e o dono cancelou o item — *"não precisamos de imagem de iOS / Android diferentes no
manual"*. Nenhum dos seis manuais do aplicativo perdeu nada com isso: eles descrevem o texto da tela,
que é o mesmo nos dois sistemas, e nomeiam o Android só onde a tela **é** do Android (as janelas de
permissão do #111).

## Quatro coisas para ler antes de usar

**`21-listas-vazias/prints/02-historico-vazio.png` não é o histórico vazio.** O nome vem do pedido;
a tela mostra o Histórico **com 22 entregas em três dias**. O caso `historico-vazio` desatribui os
pedidos do entregador, e o histórico dele continuou com o que já estava lá de dias anteriores. A
imagem é boa — só é outra coisa: o Histórico agrupado por dia. E o *Nenhuma entrega no período*
**deixou de ser pedido**: manual não usa tela de ausência, porque ninguém o consulta para saber como
é a tela quando não há nada nela.

**`19-sem-internet/prints/01-lista-sem-carregar.png` virou imagem do #112 e saiu depois.** Ela é uma
lista de entregas normal: sem rede o aplicativo repete o que carregou por último, sem mensagem
nenhuma. Anotada, ficava uma foto de tela comum com três etiquetas explicando que era comum — o
leitor não tem o que comparar. O achado ficou no manual como dois parágrafos, com o teste que
funciona (abrir um detalhe e ver se os itens vêm vazios), e a imagem saiu. A outra da pasta, a
confirmação de plataforma que não carrega, **ficou**: ali há o que ver, a faixa do aplicativo cheia
sobre a página branca do site, e o que fazer, copiar o código.

**`23-rota-com-problema/prints/02-falha-melhor-rota.png` mostra outra mensagem.** Com a rede
desligada, o MELHOR ROTA responde **Permissão necessária**, não *Ocorreu uma falha ao gerar a melhor
rota*. Não é erro de captura: é como o `try/catch` do app trata rede e GPS no mesmo `catch`. O #113
passou a responder a pergunta com as duas mensagens.

**O número do pedido aparece em uma tela só: a de PAGAMENTO.** O crachá laranja dos cartões e dos
detalhes traz só o `#`, sem número, porque lê `numeroPedido` — numeração de marketplace, nula em
pedido do restaurante. O selo *PEDIDO #NNNN* da tela de pagamento lê `numeroPreVenda`, que sempre tem
valor: é o `#1082` de `22-erros-de-cobranca/prints/01-soma-precisa-fechar.png`, confirmado no banco
(filial 39202, `numeroPedido` nulo em todos os 34 pedidos das capturas). Isso é o que decidiu como o
#117 amarra as duas metades: como a cobrança é o último passo da parada, antes dela o entregador não
tem número para conferir, e a ponte é endereço, valor, forma de pagamento, letra da rota e hora da
baixa.

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
