# MEMÓRIA — Quanto o entregador recebe

Pasta: `manuais/entregador-quanto-recebe/` · Escrito em 18/09/2026 na sandbox
**BeeFood3 - Manual** (`empresaID 38311`, `filialID 39202`, entregador `194115`).

Não estava na lista de 14 manuais do bloco. Entrou por pedido do dono:

> *"relatorios: entregador taxa/km -> como configurar a taxa de entrega por entregador (tem a
> taxa que o cliente paga e taxa por entrega do entregador (valor entregador)"*

A frase dele já contém o recorte: **são dois valores**, e a confusão entre eles é o assunto. O
manual abre com a tabela dos dois, antes de qualquer tela.

## O recorte

O pedido era "o relatório". O manual ficou maior do que isso porque relatório sem configuração
é relatório vazio — e foi exatamente o que a sandbox mostrou: o relatório existia, e o valor do
entregador estava zerado em tudo.

Ficaram quatro partes: os **três lugares** onde o valor se configura (área de atendimento,
pedido, cadastro do funcionário) e o relatório que soma. A ordem é a do dinheiro, não a da tela:
onde o valor nasce → onde ele se ajusta → como se paga por KM → onde se fecha a conta.

## O que a captura descobriu

1. **O valor do entregador vive no pedido, não na configuração.** O relatório lê o pedido; a
   área de atendimento só preenche o pedido no momento em que o endereço é calculado. Isso
   explica por que pedido semeado nasce com *Não definido* e por que o lápis da tela do pedido
   existe. Virou o aviso central da seção 2.
2. **A coluna `KM (Ida)` mostra dinheiro.** 86,30 km × R$ 1,50 = `129,45` na coluna. A distância
   fica na coluna `KM` ao lado. É o tipo de detalhe que faz o lojista achar que o sistema
   calculou errado; virou destaque.
3. **A diária é linha própria e é contada por dia com entrega.** Apareceu como
   *BeeFood3 - Manual - Diária*, 1 × R$ 60,00, e soma por cima de qualquer modo.
4. **Os campos de diária e KM não têm máscara e travam em 999,99.** Digitei `6000` esperando
   R$ 60,00 e o campo gravou `999.99` — o relatório passou a mostrar um entregador recebendo mil
   reais de diária. Corrigi para 60,00 e 1,50 e recapturei tudo. Fica o alerta para quem
   recapturar: **conferir o valor lido de volta antes de fotografar**.
5. **Três pedidos com valor, dez sem — e isso ficou nas fotos de propósito.** É o que mostra,
   na mesma imagem, a diferença entre o que tem valor gravado e o que não tem. Forçar valor em
   todos os treze deixaria a tabela bonita e o ensinamento fraco.
6. **O modo de cálculo é lembrado por navegador.** Dois usuários da mesma loja podem abrir o
   relatório em modos diferentes e ver totais diferentes. Não virou parágrafo técnico no manual,
   virou conselho: escolha um modelo e fique nele.

## Capturas

Quatorze fotos em três grupos. As do relatório são **recortes** de faixas da tela, porque a tela
tem 2.160 px de largura e as setas empilhariam num canto:

| Faixa | Recorte |
|---|---|
| botões + modos de cálculo | `07a-cabecalho` |
| os cinco cartões | `07b-cartoes` |
| tabela (tabs + cabeçalho + duas linhas) | `07c-resumo`, `08-modo-area`, `09-modo-km`, `10-ida-e-volta` |

As quatro últimas usam o **mesmo recorte** de propósito: quem folheia vê a mesma tabela mudando
de coluna, que é o ponto.

Armadilhas de captura registradas:

- **A janela da faixa de bairro não é `[role=dialog]`** e o lápis não é o primeiro botão da
  linha. O clique certo é o botão cujo `innerHTML` tem `pencil`.
- **"R$ 3,50" na linha usa espaço não separável.** Procurar pelo texto literal não acha;
  a expressão precisa ser `/R\$\s*3,50/`.
- O rótulo do campo é **"Valor pago ao entregador"**, com `e` minúsculo. Com `E` maiúsculo o
  alvo não é encontrado.

## O cenário

Aproveitou o rastro dos manuais #106 a #109 (15 pedidos do dia, 13 entregues em duas rotas) e
acrescentou três gravações de valor do entregador, diária e KM no cadastro. O que ficou gravado
na sandbox depois deste manual:

| Onde | Valor |
|---|---|
| faixa de bairro (já existia) | frete R$ 6,50 · entregador R$ 3,50 |
| funcionário 194115 | diária R$ 60,00 · KM R$ 1,50 |
| pedidos 1048, 1049, 1050 | valor do entregador R$ 3,50 |

Nada disso foi revertido: é configuração plausível de loja, e serve de base para recapturar.

## Se for mexer neste manual

- As fotos do relatório são do período **Hoje**. Em outro dia os números mudam; as frases do
  manual que citam valor (R$ 10,50, R$ 129,45, R$ 318,90) precisam ser revistas junto.
- A parte 1 mostra a área **por bairro e CEP**, porque é o que a sandbox usa. Os campos são os
  mesmos em KM e em mapa; se recapturar em outra loja, o texto continua valendo.
- O cartão *Taxa Entregador Total* mostra o que está gravado nos pedidos, e não muda com o modo
  de cálculo. Quem recapturar vai achar que travou; não travou.
