# O que o aplicativo faz de verdade — #113

Fonte: `manuais/gestao-entregas/material-recebido/app-entregador/estudo/01-o-que-o-app-faz-hoje.md`
e `manuais/gestao-entregas/estudo/01-como-o-sistema-funciona.md`. **Nada aqui vai para o manual do
usuário.**

## 1. Os três caminhos não são variações do mesmo botão

| Caminho | Escopo | O que dispara | Formato do endereço |
|---|---|---|---|
| **VER NO MAPA** | uma entrega | nada | **texto** (rua, número, bairro, cidade, CEP) |
| **INICIAR ROTA** | as paradas de uma rota | **despacho**: situação, painel, cliente | **coordenada** |
| **MELHOR ROTA GOOGLE MAPS** | só os pedidos **avulsos** | nada | coordenada, reordenada por distância |

As três diferenças da tabela são o motivo de o manual abrir com ela. Quem trata os três como
"abrir o mapa" acaba tocando no **INICIAR ROTA** para ver o caminho — e avisa o cliente de uma
saída que não aconteceu.

## 2. Texto contra coordenada

O **VER NO MAPA** de uma entrega monta a URL com o **endereço escrito**, e quem geocodifica é o
Google Maps ou o Waze. A consequência é real e foi observada na captura: bairro com nome parecido
com o de um estabelecimento faz o mapa propor rota para o estabelecimento.

A exceção é o pedido de marketplace: aí o endereço chega abreviado da plataforma e o aplicativo
manda a **coordenada**. Nas rotas (as duas), as paradas também vão por coordenada — daí o Maps
mostrar às vezes um endereço diferente do cartão, que é o que ele reconhece naquele ponto.

O manual diz "confie no cartão" em vez de explicar geocodificação. É a única instrução que
funciona na porta do prédio.

## 3. O grupo de rota — `CabecalhoRota.js`

| Elemento | De onde vem |
|---|---|
| a letra no círculo amarelo | o código da rota |
| **{n} de {N} entregues** | da **rota**, não dos cartões visíveis |
| a marca **em rota** | a rota já foi despachada |
| o botão | **INICIAR ROTA** (verde) enquanto não despachada; **ABRIR NO MAPS** (azul) depois |

O contador vir da rota é o que explica o "de 3" com dois cartões na tela — cartão entregue sai da
lista, o total não muda. Virou pergunta do FAQ porque parece bug.

A faixa **OUTRAS ENTREGAS ({N})** só é montada quando existem **rota e avulsos ao mesmo tempo**.
Sem rota, não há cabeçalho nenhum: é a mesma tela do #112.

## 4. O que o INICIAR ROTA dispara

É o **mesmo despacho** do botão do painel, chamado do celular. Na captura do material, o log do
aplicativo registrou `3 de 3 paradas viraram destino` e a URL com as três coordenadas na ordem da
rota; no banco, os três pedidos saíram de *PRONTO/PREPARO* para *ENTREGA*.

Ou seja: situação do pedido muda, o painel mostra na hora, o cliente recebe o aviso de WhatsApp
(quando ligado) e o marketplace é informado. Pelo aplicativo **não há desfazer** — igual à leitura
de código de barras do #114.

Quando o servidor não confirma, o aplicativo **abre o mapa de todo jeito** e mostra *Despacho não
confirmado*. É decisão de produto (não travar o motoboy na porta da loja), e é por isso que o
manual manda avisar a loja: o aplicativo não sabe se registrou.

O **ABRIR NO MAPS** é inofensivo: só remonta a URL. Pode ser tocado à vontade.

## 5. A melhor rota

Botão flutuante **MELHOR ROTA GOOGLE MAPS ({N})**, que só aparece com **mais de um** pedido
avulso. Abre a janela **ABRIR ROTA** com o ícone do Google Maps e **FECHAR**.

Quem calcula a ordem é o **servidor**, por distância da loja — daí a mensagem *Ocorreu uma falha
ao gerar a melhor rota* quando não há rede. E daí também o aviso mais importante da seção: ele
**reordena por distância e desfaz a sequência que o operador montou**, então cobre só os avulsos.

Não há Waze aqui porque URL com múltiplas paradas é recurso do Google Maps.

## 6. Onde o manual escolheu ser mais direto que a tela

| Tela | Manual | Por quê |
|---|---|---|
| **INICIAR ROTA** é um botão verde como qualquer outro | bloco de aviso, com as duas coisas que ele faz, antes da imagem do mapa | verde sugere "seguro"; este é o botão irreversível do aplicativo |
| o botão da melhor rota e o da rota convivem na mesma tela | o manual diz explicitamente que um **ignora** o outro | quem usa o de baixo desfaz o trabalho que o operador fez arrastando paradas |
| o Maps mostra o endereço que ele reconhece | "o endereço que vale é o do cartão" | é a instrução acionável; explicar geocodificação não é |

## 7. Procedência das imagens

Os oito prints vêm do material do dono (emulador `Pixel_7_Pro`, Android 15). **Quatro são telas do
Google Maps**, não do aplicativo — entram porque a pergunta do entregador é o que ele vê depois de
tocar, e a anotação se limita ao bloco de origem/destino e ao tempo.

A rota do material foi criada pelo caminho oficial do painel (`gestaoEntregaCriarRota`) pelo
gerador de cenário, com três dos quatro pedidos na rota A e o quarto solto — exatamente o caso de
"rota + outras entregas" na mesma tela. O **INICIAR ROTA** foi tocado de verdade.

Duas imagens são **recortes** de prints maiores: o cabeçalho da rota antes e depois do despacho.
A lista inteira entra como contexto, sem seta, pelo motivo registrado no #112 — ela numera as
próprias paradas.
