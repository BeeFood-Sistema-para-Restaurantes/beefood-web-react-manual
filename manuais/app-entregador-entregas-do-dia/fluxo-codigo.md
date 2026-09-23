# O que o aplicativo faz de verdade — #112

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `app-entregador-entregas-do-dia.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

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

## 2. O que muda a lista sem o entregador mexer

Duas peças, uma em cada lado. No servidor, `src/models/gestaoEntrega/notificacao.js` é o **único**
lugar que decide se avisa, quem avisa e o que diz. No aplicativo,
`components/Navigation/EntregadorPushHost.js` monta dois ouvintes globais, ao lado do host de
localização.

| Evento | Título e corpo | Quando |
|---|---|---|
| `PEDIDO_VINCULADO` | **Novo pedido para você** · *Toque para ver a entrega* | o painel atribui um pedido avulso |
| `PEDIDO_DESVINCULADO` | **Um pedido saiu da sua lista** · *Toque para conferir suas entregas* | o painel tira o pedido dele |
| `ROTA_ASSOCIADA` | **Nova rota para você** · *Rota {código} com {N} paradas · toque para iniciar* | a rota ganha entregador |
| `ROTA_REMOVIDA` / `ROTA_CANCELADA` / `ROTA_ALTERADA` | *Rota removida* / *Rota cancelada* / *Sua rota mudou* | assunto do #113 |

**Nenhum texto leva endereço, nome de cliente nem número de pedido, de propósito:** a notificação
aparece na tela de bloqueio, sem desbloquear o aparelho. É o que sustenta a frase do manual — *o
aviso não diz qual pedido é* — e não é limitação do aviso, é decisão de privacidade.

Os textos estão marcados no código como **proposta**, não como texto aprovado. Se mudarem, mudam
num arquivo só, e as duas imagens deste manual ficam desatualizadas juntas.

Três comportamentos que explicam perguntas do FAQ:

- **Rota alterada tem freio de um aviso por minuto, por rota.** Arrastar paradas no painel dispara
  um evento a cada solta; sem o freio o telefone tremeria a cada arrasto. Os excedentes são
  **descartados**, não enfileirados — o aviso diz "confira", e conferir uma vez cobre as três
  mudanças.
- **Os dois ouvintes recarregam a lista com 800 ms de espera.** Sem isso, dois avisos ao mesmo
  tempo — dois pedidos, ou o par *removido de você* / *associado a ele* — disparam dois
  carregamentos, e o mais velho pode chegar por último.
- **Quando o toque é o que abre o app, o ouvinte pode não estar montado e o evento se perde.** O
  entregador cai no fluxo normal e vê a lista atualizada de qualquer forma, só não é levado pelo
  atalho. É a pergunta *chegou o aviso e a lista continua igual* — e a resposta do manual (tocar no
  aviso, não no ícone) é o caminho que funciona sempre.

O banner aparecer com o **aplicativo aberto** — que é o estado da imagem `11` — depende de
`setNotificationHandler` com `shouldShowBanner`; o padrão da biblioteca é engolir a notificação
nesse caso. O toque leva sempre para `Entregas`, nunca para a rota: o deep link de `Rota` é
declarado e não registrado no navegador.

### Sem rede, a lista não tem estado de erro

O inventário da tela tem lista cheia e **Nenhuma entrega agora**, e nada entre os dois: falha de
requisição deixa na tela o que o último carregamento trouxe. Foi medido no print de
`19-sem-internet/`, com o modo avião ligado — a pílula segue verde, os cartões seguem lá, o
**ATUALIZAR** roda e volta.

A pílula é presença declarada (`POST entrega2/gestao/presenca`), não estado de rede: ela só fica
com o ícone de nuvem quando **o próprio envio da presença** não foi confirmado. Lista que não
carrega e presença que não sobe são dois caminhos diferentes, e o manual precisa dizer isso porque
a tela não diz.

## 3. Os detalhes

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

## 4. O histórico

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

## 5. Onde o manual escolheu ser mais direto que a tela

| Tela | Manual | Por quê |
|---|---|---|
| os círculos numerados são só desenho | "os números dos círculos são do aplicativo, e valem a posição na sequência — não o número do pedido" | as duas numerações convivem no mesmo cartão, e a laranja é a que o restaurante cita no telefone |
| a observação de finalização aparece junto do recado do cliente, na mesma cor | o manual avisa que ela é **permanente** | é texto que o entregador escreve com pressa e que fica no registro da entrega |
| **TROCO** simplesmente não aparece quando não há | o manual diz que a coluna só existe em pedido de dinheiro, e mostra um rodapé de cada tipo | entregador acostumado com a coluna acha que a tela quebrou |
| sem rede a lista **repete** o que tinha, sem mensagem nenhuma | o manual responde em dois parágrafos, sem imagem | a tela sem rede e a tela com rede são a mesma tela; foto de uma não ensina a diferença da outra |

## 6. Procedência das imagens

Os oito prints da primeira rodada vêm do material do dono (emulador `Pixel_7_Pro`, Android 15).
Duas das dez primeiras imagens do manual são **recortes** de prints maiores — o cartão e o rodapé
—, não capturas novas.

As quatro da seção 2 vieram da segunda rodada, com duas diferenças de tratamento:

- **`14-antes-e-depois.png` é a única montagem do manual:** dois prints colados por
  `lado_a_lado()`, recortados na mesma faixa. Tela inteira duas vezes ficaria ilegível, e a metade
  de cima é idêntica nas duas.
- **A linha de *Previsão Entrega* foi trocada** pela do print da seção 1, por
  [`../gestao-entregas/scripts/relogio.py`](../gestao-entregas/scripts/relogio.py): os prints novos
  são de dois dias depois, e a data em letras vermelhas contradiz o resto do manual. O transplante
  é de tinta do próprio aplicativo — a Roboto do Android não existe na máquina que monta as
  imagens. Nada mais da tela muda.

Os destinatários que aparecem (*Ana Beatriz Moraes*, *Carlos Eduardo Prado*, *Rafael Monteiro
Dias*) foram conferidos na base do sandbox antes de versionar: são **clientes sintéticos**,
semeados por script, sem telefone nem e-mail. O laudo está em
[`../gestao-entregas/material-recebido/README.md`](../gestao-entregas/material-recebido/README.md).

### A armadilha de anotar esta tela

A lista de entregas desenha os **próprios números** nos círculos das paradas. Etiqueta verde
numerada em cima disso põe dois sistemas de numeração na mesma imagem, e o leitor não sabe qual é
qual. Por isso `01-lista.png` entra como **contexto**, sem seta, e quem explica o cartão é um
recorte de um cartão só.
