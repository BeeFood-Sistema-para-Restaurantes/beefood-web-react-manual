# O que o aplicativo faz de verdade — #115

Fonte: `manuais/gestao-entregas/material-recebido/app-entregador/estudo/01-o-que-o-app-faz-hoje.md`,
`.../estudo/00-estudo-e-proposta.md` e o modelo `gestaoEntrega/erpPedido.js` do servidor. **Nada
aqui vai para o manual do usuário.**

## 1. O que liga o botão de confirmação

Não é "o pedido é de marketplace". É o **campo do identificador**, um por plataforma:

| Botão | Aparece quando o pedido tem |
|---|---|
| **CONFIRMAR ENTREGA IFOOD** | o localizador do iFood |
| **CONFIRMAR ENTREGA 99FOOD** | o identificador do 99Food |
| nenhum | Keeta, Uber, Rappi e as demais: **só o selo** |

Keeta é o caso interessante: o pedido mostra o selo na lista e nos detalhes, e **não tem** tela de
confirmação. Por isso o manual fecha com a pergunta *"o pedido é de outra plataforma e não tem
botão"* — não é falha, é que só duas plataformas exigem confirmação de entrega própria.

## 2. A tela de confirmação é um site, embutido

O botão abre uma janela de navegador **dentro do aplicativo**, no endereço da própria plataforma.
A faixa de cima — com o código espaçado e o botão de copiar — é a única parte que é do aplicativo;
todo o resto é página da plataforma, inclusive os quadradinhos e o botão de continuar.

Três consequências, todas no manual:

1. **Precisa de internet**, e sem ela a tela fica em branco.
2. **O aplicativo não preenche o site.** Ele copia o código para a área de transferência e o
   entregador cola. Não há automação nenhuma.
3. **O layout pode mudar sem aviso**, porque é a plataforma que publica. O manual descreve os
   passos pelo texto que a página mostra, não por posição na tela.

## 3. O código que o aplicativo mostra não é sempre o que o site pede

Foi observado na captura do 99Food e ficou registrado como aviso em caixa: a faixa do aplicativo
mostra o código que **veio no pedido** (6 dígitos, no caso capturado), e a página pede um
localizador de **8 dígitos**, que vem do recibo.

O iFood não tem esse problema na captura: o localizador que chega no pedido tem 8 dígitos e é
exatamente o que a página pede.

Esconder isso deixaria o entregador colando um código que o site recusa. O manual diz, na ordem:
o número que vale é o do recibo, e é a própria tela da plataforma que indica isso.

## 4. Confirmar na plataforma e finalizar no aplicativo são dois registros

O **FINALIZAR** é a baixa de sempre da entrega. O que ele faz, além de fechar no restaurante:
leva o pedido para *ENTREGUE*, e é essa troca de situação que dispara a sincronia com o
marketplace. O despacho (quando o pedido vai para *ENTREGA*) já havia avisado a plataforma que o
pedido saiu.

A confirmação no site é outra coisa: é a **prova de entrega** que a plataforma pede de quem
entrega com frota própria, feita com um código que só o cliente e a comanda têm.

Ou seja, não há redundância — e não há, tampouco, um que faça o outro. O manual põe isso em duas
linhas numeradas e repete nas perguntas frequentes, nos dois sentidos (confirmou e não finalizou;
finalizou e não confirmou).

## 5. Por que não há cobrança

O pedido de marketplace chega **pago**, com a forma de pagamento da plataforma (*PAGO ONLINE* no
iFood capturado, *PIX* no 99Food). O saldo a receber é zero, e o aplicativo reage a isso
escondendo a linha *Cobrar R$* do cartão e trocando as ações do rodapé: some o **INICIAR
COBRANÇA**, some o **FINALIZAR SEM COBRAR**, e sobra **FINALIZAR**.

É o mesmo comportamento de "o que não existe não aparece" registrado no #112 — aqui aplicado ao
bloco de ações inteiro.

## 6. A plataforma que só tem etiqueta

O aplicativo tem `WebView` de confirmação para **iFood** e **99Food**, e mais nada. Pedido de
**Keeta** entra no mesmo lugar dos outros — etiqueta no cartão e nos detalhes, com o identificador
da plataforma — e o rodapé **não ganha botão colorido**: o entregador vai direto ao `FINALIZAR`.

Não é lacuna a preencher no manual, é o estado de hoje, e está declarado no apêndice
*o que não existe na tela* do material. A imagem `11` é a prova: selo presente, rodapé com um botão
só.

**A etiqueta da Keeta é amarela, como a do 99Food.** Medido nos dois prints, lado a lado: o que
distingue é o logotipo dentro da etiqueta. O manual passou a dizer isso na seção 1, porque
descrever plataforma por cor levaria o entregador a procurar botão de confirmação que não existe.

## 7. Procedência das imagens

Os oito prints vêm do material do dono (emulador `Pixel_7_Pro`, Android 15), dos capítulos 09 e
10. Os pedidos **#1034** (iFood) e **#1035** (99Food) foram criados pelo gerador de cenário com
identificadores nos mesmos formatos que aparecem em produção, e já nasceram pagos.

Os botões de confirmação foram tocados de verdade, e os sites das duas plataformas carregaram no
emulador. **As confirmações não foram concluídas**: os pedidos não existem no iFood nem no
99Food, e seguir só produziria erro de plataforma. Por isso as capturas param no primeiro passo —
o que vem depois é tela da plataforma, não do aplicativo.

A baixa desses dois pedidos foi feita **por script**, e não pelo botão, justamente para não
disparar webhook de entrega com identificador que não existe do outro lado. Está registrado no
risco 3 do estudo do material.

As duas últimas imagens vieram da segunda rodada de capturas. A `10` é a mesma tela de confirmação
com o wifi desligado — o site não carregou, e é isso que ela mostra. A `11` é um pedido de Keeta
montado pelo cenário, e o recorte começa **abaixo da linha de *Realizado às***: essa linha traz
data e hora, e o print é de dois dias depois dos outros deste manual. Nenhuma das duas mostra data,
então nenhuma passou pelo
[`../gestao-entregas/scripts/relogio.py`](../gestao-entregas/scripts/relogio.py).

## 8. Onde o manual escolheu ser mais direto que a tela

| Tela | Manual | Por quê |
|---|---|---|
| o cartão simplesmente não tem linha de cobrança | o manual **aponta a ausência** em negrito | entregador acostumado a conferir o valor acha que a tela quebrou |
| os dois botões do rodapé parecem alternativas | o manual numera: **confirma, depois finaliza** | é a única ordem que fecha os dois lados |
| o X da tela de confirmação é um X comum | o manual garante que **não desfaz nada** | sem essa frase, ninguém fecha a tela por medo |
| a página do 99Food explica o localizador num parágrafo | o manual transforma em aviso destacado, com os dois formatos | é o erro que o suporte recebe |
