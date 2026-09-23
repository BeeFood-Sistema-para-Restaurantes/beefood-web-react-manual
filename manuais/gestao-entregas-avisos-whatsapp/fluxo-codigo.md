# O que a tela faz de verdade — #110 Avisos de WhatsApp da entrega

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `gestao-entregas-avisos-whatsapp.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Lido em `beetech-server-node-2.0/docs/gestao-entrega-2.0/20-whatsapp-de-entrega.md` e no
`lovable/13-raio-proximidade.md`, no modelo `src/models/gestaoEntrega/whatsappEntregador.js`,
no controller `whatsapp2/notificacaoPOST.js` e no componente
`beefood-web-react/src/components/whatsapp/ModalEditarNotificacao.tsx`. **Medido no MSSQL** e
conferido na sandbox salvando o aviso de proximidade e lendo a coluna depois.

## Os quatro avisos são quatro tipos no catálogo de mensagens

| Tipo | `categoria` | Nome na tela | Destinatário | Quem monta o texto |
|---|---|---|---|---|
| 30 | `Entregador` | Nova entrega | entregador | `beefood-server-whatsapp-cron` |
| 31 | `Entregador` | Entrega cancelada | entregador | idem |
| 32 | `Entregador` | Relatório diário | entregador | `beefood-server-estoque-cron` |
| 33 | `Delivery` | Entregador próximo | **cliente** | `beefood-server-whatsapp-cron` |

A `categoria` é o que agrupa a tela — e é por isso que o *Entregador próximo* aparece no grupo
Delivery: a tela agrupa por destinatário, não por assunto. O manual explica isso porque é a
primeira coisa que o lojista não acha.

O quinto aviso que a entrega dispara não é novo: o tipo **4 — Pedido saiu para entrega** já
existia, e o despacho da rota o dispara pelo caminho normal (`situacaoDelivery = ENTREGA`). O
que a Fase 10 acrescentou nele foi o marcador `**ENTREGADOR_NOME**`, **opt-in**: o texto padrão
não foi alterado para não mexer na mensagem que a base inteira já recebe.

## A descoberta que virou a seção 4 do manual: o raio não está gravado

Medido em 18/09/2026, no MSSQL, com `SELECT ... FROM _WhatsappMsgTipoFilial WHERE
WhatsappMsgTipoID = 33`:

| | Medido |
|---|---|
| Filiais com o tipo 33 | 56.661 |
| Ativas | 56.603 |
| **Sem `raioProximidadeMetros`** | **56.654** |
| Padrão global (`_WhatsappMsgTipo.raioProximidadeMetros`) | **NULL** |

O `sql/010` previa exatamente o contrário — a conferência dele diz *"esperado: filiaisSemRaio =
0"* —, então o passo 2 (as colunas) rodou e o passo 3 (o back-fill) não. Efeito prático:

1. A tela **mostra 2 km** de todo jeito, porque o React cai no padrão
   (`raioProximidadeMetros ?? raioDefault ?? 2000`) para não exibir caixinha vazia.
2. O cron de proximidade **pula filial sem raio**: para ele, NULL é "não configurado", não "use
   o padrão".
3. Logo, hoje o aviso *entregador está chegando* não sai para praticamente ninguém — com a tela
   parecendo configurada.

**Conferido nos dois sentidos na sandbox**, e é o que o manual manda fazer:

```
antes de salvar:  [{"WhatsappMsgTipoID":33,"Ativo":true,"raioProximidadeMetros":null}]
depois de SALVAR: [{"WhatsappMsgTipoID":33,"Ativo":true,"raioProximidadeMetros":2000}]
```

Salvar resolve porque o modal **sempre** manda o campo quando o tipo é 33
(`dados.raioProximidadeMetros = Math.round(km * 1000)`), e o valor que está na tela é o padrão.
Em qualquer outro tipo o campo vai nulo, e o `UPDATE` usa
`COALESCE(@raio, raioProximidadeMetros)` — ou seja, salvar outra notificação **não** apaga a
distância. Essa proteção é o motivo de a tela poder mandar nulo sem risco.

## Validação do km, e por que o teto é 50

A tela recusa antes de mandar: `!Number.isFinite(km) || km <= 0 || km > 50`. O backend recusa
de novo (`raio > 0`, senão trata como "não mexa"). O teto de 50 km existe para pegar quem
digitou **metros** no campo de **km**: `2000` seria "avise quando estiver a 2.000 km", o que
avisaria todo cliente no instante do despacho.

A conversão é de borda: a tela mostra km com vírgula e grava metros (`km * 1000`).

## A distância leva 30 minutos para valer. O liga/desliga, não

Quem lê o raio é o `beefood3-server-entregas`, por um cache em memória recarregado a cada 30
minutos — o cron roda a cada minuto, e ler o MSSQL por rodada seriam 1.440 consultas diárias
para um número que muda uma vez por mês. Já o `Ativo` é lido pelo cron de **envio**, sem cache
no meio, então desligar vale na hora. A assimetria está no manual porque quem testa muda o
número e conclui que não funcionou.

## O telefone do entregador vem do cadastro de funcionário

`getFuncionarioContato(empresaID, funcionarioID)` lê o **cache de funcionários** da empresa, e
prefere `Celular` a `Telefone`. Três comportamentos herdados do cache, todos no manual:

| Situação | O que acontece |
|---|---|
| Sem Celular e sem Telefone | nada é enviado; o log registra `SEM_TELEFONE` com o `funcionarioID` |
| Demitido ou inativo | fora do cache, não recebe |
| Telefone recém-salvo | vale na hora — salvar funcionário invalida o cache |

Nenhum desses casos vira erro em tela. Por isso o manual transforma "sem Celular não recebe" em
seção, e não em nota de pé de página: é a única forma de o lojista descobrir.

## Uma mensagem por pedido, e a dedup que distingue o destinatário

Pedido do dono: rota criada manda **uma mensagem por pedido**, não uma por rota. A dedup do
banco é por `(preVendaID, tipo, funcionarioID)` — procedure própria
(`procProcessa_WhatsApp_MsgDelivery2`) para não tocar na que outros sete projetos compartilham.

Duas consequências que o manual usa:

- **Reordenar paradas não gera mensagem repetida** (idempotência vem de graça).
- **Troca de entregador avisa os dois:** o `funcionarioID` na chave é o que permite o segundo
  aviso do mesmo pedido no mesmo dia. Sem ele, quem ganhou a entrega ficava sem aviso.

## "Entrega cancelada" não é o cancelamento do pedido

Decisão do dono: o tipo 31 significa *"este pedido não é mais seu"* — parada removida,
transferida, rota excluída ou entregador trocado. O cancelamento do pedido no ERP tem tipo
próprio e vai para o cliente. O manual repete isso porque os dois nomes são quase iguais.

Lacuna conhecida, registrada no doc 20 e **não** contornada pelo manual: pedido transferido
para a rota de outro entregador, quando a rota de origem **não** fica vazia, não avisa o
entregador de origem.

## Vazão da fila: 5 mensagens por filial por minuto

A fila envia no máximo 5 mensagens por filial por ciclo (~1 min), e ela é compartilhada com as
mensagens de cliente. Uma rota de 5 pedidos gera 5 avisos ao entregador mais 5 "saiu para
entrega" ao cliente: 2 minutos para escoar. Para *Nova entrega* é irrelevante; é uma das razões
de o raio padrão ser 2 km e não 500 m — a 30 km/h, 2 km dão ~4 minutos de antecedência, que
absorvem a fila.

## Os marcadores do tipo 32 não estão na paleta

A paleta do modal é fixa, com três grupos (`MEU`, `CLIENTE`, `VENDA`). Ela **não** tem
`**ENTREGADOR_NOME**`, `**DATA_REFERENCIA**`, `**QTD_ENTREGAS**`, `**DETALHE_ENTREGAS**` nem
`**LINHA_TAXAS**` — todos funcionam, mas precisam ser digitados. É o que faz **Restaurar
padrão** virar a recomendação do manual para quem apagou um deles.

## O tipo 4 e o tipo 33 colidem em pedido perto

As duas mensagens nascem do mesmo instante: o despacho põe a primeira parada `EM_ROTA`, o que
dispara o tipo 4 e torna a parada elegível ao 33. Em pedido dentro dos 2 km, o cliente recebe as
duas com um minuto de diferença. Não é defeito a corrigir por código — decisão do dono: quem
escolhe é o restaurante, baixando o raio, porque o número certo depende da geografia.

## Por que as conversas do manual são mockup

O sandbox não tem número conectado, e o dono autorizou mensagem fake neste manual. Para a
imagem não mentir, o texto não foi escrito à mão: o `/tmp/ge/mock110.py` lê o `msgPadrao`
gravado no banco (tipos 4, 30, 31, 32 e 33), substitui os marcadores pelos dados do cenário
(rota 125, pedidos 1048 a 1050) e resolve o spintax `{a|b}` na primeira opção — que é o que a
camada de envio faz, só que sorteando.
