# O que a tela faz de verdade — #114 Código de barras

Lido em `beetech-server-node-2.0/docs/gestao-entrega-2.0/19-codigo-de-barras-no-3.md` e no
material do app (`material-recebido/app-entregador/08-codigo-de-barras/`). A parte do painel
(ligar a etiqueta) foi capturada na sandbox pelo `/tmp/ge/cap-barras.py`, no #104.

## Ler é despachar — e é o mesmo código do painel

O app chama `POST tentrega/lerCodigoBarras`. O servidor roda a
`procProcessa_Entregador_LerCodigoBarras` e chama o **mesmo** `SituacaoDeliveryUpdater` com
`'ENTREGA'` que o botão de despachar do painel usa. Daí vem tudo o que o manual lista como
consequência: aviso ao marketplace, impressão e WhatsApp ao cliente.

É por isso que o aviso de "não é conferência, é despacho" abre o manual em vez de fechar: o nome
"leitor de código de barras" sugere bipar para ver o que é, e aqui bipar **muda o pedido**.

## O que o código carrega

EAN-13, 13 dígitos. O app faz `data.slice(0, -1)` e trata o resultado como `preVendaID` — ou
seja, **os 12 primeiros dígitos são o identificador interno do pedido** e o 13º é o dígito
verificador do próprio EAN-13. Nenhum outro formato é aceito, e o manual diz isso porque loja com
etiqueta própria (QR, Code128) tenta e não entende por que nada acontece.

O modal também **evita reler o mesmo pedido na mesma sessão** — é de onde vem a mensagem *Pedido
já lido*, que não é erro.

## O gate comercial devolve 200, e isso vira uma pergunta do FAQ

`empresaLiberadaAppEntregador(empresaID)`: libera quem tem o plano do entregador, quem tem
`entregaAtiva` ou quem está numa lista de 32 empresas de exceção. Quando barra, **responde 200**,
não 403 — decisão registrada no doc 19: *"o app não distingue os códigos nesse ponto, e um erro
faria a tela dizer 'erro na leitura' para quem apenas não tem o recurso contratado"*.

Consequência para quem opera: em loja sem o recurso, a leitura **parece** funcionar e o pedido não
muda. Não há sintoma em tela. Por isso o FAQ tem a pergunta "bipo, diz sucesso, mas o pedido não
mudou no painel" — sem ela, o lojista procuraria defeito na impressora.

## O log do lojista

A leitura grava no log com `coluna = 'Situação Delivery'` e o texto **`App Entregador: ENTREGA`**,
com `registro = 'Venda {numeroPreVenda}'`. É o que permite, depois, saber que aquele despacho veio
do celular. O `usuarioID` vai **nulo** de propósito, para o evento não ter duas formas dependendo
da versão do app.

O manual menciona isso em uma linha ("fica registrado como *App Entregador*") sem citar coluna nem
nome de tabela.

## Dependência de um servidor só

O app aponta para o `apiN3` **sem fallback** para o 2.0 (decisão do dono). Se o `app3` cair, não
há como despachar pela etiqueta — o caminho é o painel. Isso está no FAQ como "faixa vermelha", sem
citar servidor.

O timeout de escrita do app é de 20 s nesta chamada, maior que o das outras: é escrita com efeito
externo (marketplace), e não convém desistir em 8 s.

## Onde a etiqueta é ligada

`Configuração → Impressão → Layout → Cupom Pedido → aba Texto Padrão`, caixinha **Código de
Barras App Entrega**. Duas coisas medidas na sandbox durante o #104:

- A caixinha vive no **fim** de um formulário longo, dentro do card *Texto padrão Delivery* — sem
  rolar até ela, a janela sai cortada no print e o leitor do manual não a encontra na tela.
- Ela fica ao lado de **QR Code Cardápio Digital**, que é outra coisa (o QR do cardápio para o
  cliente). As duas caixinhas vizinhas com nomes parecidos são a razão de o manual gastar uma
  linha da tabela dizendo o que a segunda não é.

## Por que duas imagens do painel vêm do #104

`01-impressao-layout.png` e `02-cupom-texto-padrao.png` são as mesmas capturas do #104 — a tela é
a mesma e recapturar produziria imagem idêntica com outro nome. O `annotate.py` traz o arquivo com
`copiar_pura()` e desenha a anotação **própria** deste manual: no #104 a seta principal é a
caixinha no meio do fluxo de liberação; aqui ela é o assunto da página.

## O que não foi exercitado

**Nenhuma leitura real de etiqueta.** O emulador não tem câmera física, e a única imagem composta
do material é a etiqueta dentro da faixa da câmera (declarado no capítulo 08 do material). O
despacho correspondente **foi** feito de verdade pelo dono, chamando a mesma rota do leitor para o
pedido #1028, e conferido no banco: o pedido saiu de *PREPARO* para *ENTREGA*.
