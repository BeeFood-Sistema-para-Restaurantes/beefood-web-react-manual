# O que o aplicativo faz de verdade — #112

Fonte: `manuais/gestao-entregas/material-recebido/app-entregador/estudo/01-o-que-o-app-faz-hoje.md`
(leitura do código do aplicativo) e `manuais/gestao-entregas/estudo/01-como-o-sistema-funciona.md`
(backend). **Nada aqui vai para o manual do usuário.**

## 1. A lista

`src/views/entregas/index.js`.

| Item | Como é |
|---|---|
| Endpoint | `GET entrega2/gestao/entregador/{empresaID}/{filialID}/{usuarioID}/{funcionarioID}` no 3.0, com **fallback** para o 2.0 se falhar |
| Recarrega | ao ganhar foco, no arrastar para baixo, no **ATUALIZAR** e quando o entregador toca na notificação |
| Vazia | **Nenhuma entrega agora** + *Quando o restaurante te enviar um pedido, ele aparece aqui.* |

A tela é **N grupos de rota + uma lista solta**, e qualquer um dos dois pode estar vazio. A faixa
**OUTRAS ENTREGAS ({N})** só aparece quando existem as duas coisas ao mesmo tempo — motivo pelo
qual ela **não** está neste manual: ela é assunto do #113, onde a rota aparece.

### A ordem

Os avulsos vêm ordenados por **distância da loja**, crescente; pedido sem coordenada vai para o
fim. Dentro de uma rota, a ordem é a `ordem` que o operador montou, e o número do círculo passa a
ser a parada — não a distância. O manual diz isso porque as duas telas são idênticas e a regra
muda no meio.

### O cartão — `ItemEntrega.js`

Número da parada (a `ordem` da rota, ou a posição na lista quando avulso), etiqueta
**#{numeroPedido}**, etiquetas de marketplace, **Previsão Entrega** com a hora (em vermelho se
atrasado), endereço completo e, quando há saldo, **Cobrar R$ {valor}** em verde.

**Não há botão de ação na lista.** Cobrar e finalizar vivem só nos detalhes, e isso é decisão de
produto: a lista é rolada com o polegar enquanto a moto está parada no farol.

## 2. Os detalhes

`src/components/Rota/Detalhes.js`. Abre como tela cheia sobre a lista, header **DETALHES DA
ENTREGA**.

**O bloco do endereço não rola.** Endereço, complemento em pílula vermelha, **Observações** em
laranja e **VER NO MAPA** ficam fixos no topo enquanto o corpo desce. É o que sustenta a frase do
manual sobre o endereço continuar visível.

**Os produtos são carregados sob demanda**, por
`GET entrega2/gestao/entregador/historico/produto/{empresaID}/{usuarioID}/{preVendaID}`, com
esqueleto de carregamento. É por isso que a pergunta *"os itens não aparecem"* virou FAQ: sem
internet, o cartão do pedido fica vazio e o resto da tela funciona.

### O destaque de impressão

O item sai em preto quando a loja marcou o produto (ou a opção) como destaque de impressão — o
mesmo parâmetro do manual [Destaque na impressão](../destaque-impressao/destaque-impressao.md).
A marcação é **linha a linha** quando só parte está marcada, e **cartão inteiro** quando produto e
todas as opções estão.

E ela não é só visual: com destaque presente, tocar em **INICIAR COBRANÇA** ou **FINALIZAR SEM
COBRAR** abre primeiro a folha **CONFIRMA E ENTREGA DESSES PRODUTOS CORRETAMENTE?**. O manual
trata isso como conferência, não como aviso, porque é o que ela é na prática.

### O rodapé

**FORMA DE PAGAMENTO** com o `tipoPagStr` (ou **não informado**), e as colunas **TOTAL**,
**TROCO** — só quando o texto do pedido traz "troco para" — e **COBRAR** em verde quando há saldo.

| Situação | Botões |
|---|---|
| Há saldo a cobrar | **INICIAR COBRANÇA** e, abaixo, **FINALIZAR SEM COBRAR** (cinza) |
| Não há saldo | **FINALIZAR** |
| O pagamento já foi registrado nesta sessão | só **FINALIZAR** |

## 3. O histórico

`src/views/historico/index.js`.

| Item | Como é |
|---|---|
| Endpoint | `GET entrega2/gestao/entregador/historico/{empresaID}/{usuarioID}/{funcionarioID}/{data}/{data}` |
| Período | o aplicativo manda **a data de hoje nos dois campos**; o período mostrado vem da resposta |
| Agrupamento | por dia (`ItemGrpHistorico.js`), com dia da semana, data e **{n} entrega(s)** |
| Vazio | **Nenhuma entrega no período** + *As entregas que você concluir aparecem aqui.* |

**Não existe filtro de data na tela.** O manual diz isso em vez de sugerir que o entregador
procure o filtro — ele procuraria.

No modo histórico, a tela de detalhes muda: **VALOR TOTAL DO PEDIDO** em lugar das três colunas, a
linha do tempo **REALIZADO / COLETADO / ENTREGUE** e **nenhum botão de ação**.

Duas coisas invisíveis que valem registro:

- a **linha de quilometragem existe na tela com opacidade zero** — está no código, escondida de
  propósito. Não entra no manual;
- o `!` vermelho de atraso compara a hora da baixa com a previsão. Não há como o entregador
  contestar pela tela.

## 4. Onde o manual escolheu ser mais direto que a tela

| Tela | Manual | Por quê |
|---|---|---|
| os círculos numerados são só desenho | "os números dos círculos são do aplicativo, e valem a posição na sequência — não o número do pedido" | as duas numerações convivem no mesmo cartão, e a laranja é a que o restaurante cita no telefone |
| a observação de finalização aparece junto do recado do cliente, na mesma cor | o manual avisa que ela é **permanente** | é texto que o entregador escreve com pressa e que fica no registro da entrega |
| **TROCO** simplesmente não aparece quando não há | o manual mostra as duas telas lado a lado | entregador acostumado com a coluna acha que a tela quebrou |

## 5. Procedência das imagens

Os oito prints vêm do material do dono (emulador `Pixel_7_Pro`, Android 15). Duas das dez imagens
do manual são **recortes** de prints maiores — o cartão e o rodapé —, não capturas novas.

Os destinatários que aparecem (*Ana Beatriz Moraes*, *Carlos Eduardo Prado*, *Rafael Monteiro
Dias*) foram conferidos na base do sandbox antes de versionar: são **clientes sintéticos**,
semeados por script, sem telefone nem e-mail. O laudo está em
[`../gestao-entregas/material-recebido/README.md`](../gestao-entregas/material-recebido/README.md).

### A armadilha de anotar esta tela

A lista de entregas desenha os **próprios números** nos círculos das paradas. Etiqueta verde
numerada em cima disso põe dois sistemas de numeração na mesma imagem, e o leitor não sabe qual é
qual. Por isso `01-lista.png` entra como **contexto**, sem seta, e quem explica o cartão é um
recorte de um cartão só.
