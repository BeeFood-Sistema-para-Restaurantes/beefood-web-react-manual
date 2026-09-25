# MEMÓRIA — #109 Despacho automático: as sete regras

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `gestao-entregas-despacho-automatico.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Pasta: `manuais/gestao-entregas-despacho-automatico/` · Numeração: **#109** ·
Escrito em 18/09/2026 na sandbox **BeeFood3 - Manual** (`empresaID 38311`, `filialID 39202`,
entregador `194115` simulado por script).

Quinto manual do painel e o primeiro de configuração: os quatro anteriores ensinam a fazer à
mão, este delega. Por isso ele cita os três anteriores e não o contrário.

## O recorte

O título fala de **sete regras** porque foi o que sobrou depois de tentar organizar o manual
por tela: a janela tem sete campos e dois avisos, e é isso. O que não é campo — as duas fases,
o freio de 2 horas, o heartbeat da tela aberta — virou seção própria, porque nenhuma delas é
visível no formulário e todas mudam o resultado.

A seção 5 (*o entregador entra depois*) nasceu de um problema de captura e virou a parte mais
útil do manual. Ver mais abaixo.

## O que a captura descobriu, e o que mudou por causa disso

1. **O automático não despacha.** Está escrito no primeiro parágrafo do manual porque é a
   expectativa errada mais provável: quem liga "despacho automático" espera entrega automática
   de ponta a ponta. Ele agrupa e escolhe entregador; o avião continua sendo um clique do
   operador. O motivo é bom e entra no manual: rota que saísse sozinha avisaria o cliente de
   que o pedido está em rota antes de alguém pegar as sacolas.
2. **A rota nasce sem dono.** Isso não estava previsto como seção. A primeira captura pegou a
   rota em *Montando*, *Sem entregador* em itálico, e eu tratei como estado transitório a ser
   descartado. É estado de projeto: duas fases separadas para o lojista poder intervir. Rendeu
   as fotos 03 e 04, que são o par mais didático do manual.
3. **A tolerância de GPS segurou a rota por dez minutos.** Três pedidos prontos, entregador
   disponível a 0 m da loja, raio de 500 m — e nada. O que barrava era a idade da última
   posição: acima de 5 minutos o entregador sai da lista de candidatos. Renovar a posição
   destravou a associação na rodada seguinte. Isso não está em documento nenhum do backend;
   apareceu porque o cenário rodou de verdade, e virou a tabela de quatro causas da seção 5.
4. **O limite de 2 horas é constante, não campo.** A janela explica o limite sem oferecer o
   campo, e isso é proposital. O manual repete a explicação e acrescenta o que o lojista
   precisa: ao ligar numa loja com pedidos acumulados, os antigos ficam de fora — e isso é
   proteção, não bug.
5. **Painel fechado, despacho parado.** O cron só trabalha em filial que deu sinal de tela
   aberta. É requisito, não recomendação, e por isso está em *Antes de começar* e em destaque
   na seção 1.

## Capturas

Cinco fotos, todas do painel:

| Foto | O que mostra | Detalhe da captura |
|---|---|---|
| `01a-janela-avisos.png` | topo da janela: explicação, interruptor e os dois avisos | recorte da metade de cima da janela |
| `01b-janela-regras.png` | as sete regras em duas colunas | recorte da metade de baixo da mesma captura |
| `02-janela-ligada.png` | interruptor ligado + confirmação + SALVAR | |
| `03-rota-automatica.png` | rota criada sozinha, *Sem entregador*, *Montando* | |
| `04-rota-associada.png` | a mesma rota com entregador, *Pronta para sair* | |

Dois detalhes técnicos que vão doer se esquecidos:

- **A janela não cabe em 1440×900.** O título e a explicação do topo ficam cortados. As fotos
  01a e 01b saíram de um contexto com viewport `1440×1200`, e depois recortadas.
- **A associação exige GPS fresco durante a espera.** O laço de captura que só esperava nunca
  via a associação. O que funcionou foi renovar a posição do entregador a cada volta do laço,
  porque é o que o celular de verdade faz sozinho.

## Cenário

Montado com `manuais/gestao-entregas/scripts/cenario.js`:

1. Regras afrouxadas (máximo 3, distância 6.000 m) e interruptor ligado pela tela.
2. `semear --qtd 3` — pedidos **novos**. Os que sobraram do #108 tinham mais de 4 h e o freio
   de 2 h os ignorava; isso custou duas tentativas até eu perceber.
3. `presenca` + `andar --para` a coordenada da loja.
4. `rota-prontos` para os três pedidos ficarem prontos (a regra era *Finalizados*).
5. Renovação de posição a cada tentativa, o que destravou.

No fim, as regras voltaram ao original (máximo 2, distância 3.000 m) e o interruptor voltou a
**desligado**: a sandbox ficou como estava.

## O que ficou de fora

- **Simular duas rodadas com filas diferentes** para mostrar o efeito de cada regra isolada.
  Renderia cinco fotos quase idênticas e um manual duas vezes maior; a explicação em texto
  cobre.
- **Mostrar rota com pedido sem coordenada.** O comportamento está no `fluxo-codigo.md`, mas
  criar pedido sem coordenada de propósito na sandbox suja o cenário dos outros manuais.
- **Medir o consumo do cron.** Não é assunto de lojista.

## Se for mexer neste manual

- O interruptor **nasce desligado** em qualquer loja: se o revisor abrir a janela e vir tudo
  desligado, está certo.
- Se a foto 03 e a 04 forem recapturadas, precisam ser da **mesma rota**, senão a letra muda e
  o par perde o sentido.
- Os números dos campos nas fotos 01b seguem a ordem visual da janela (coluna da esquerda de
  cima para baixo, depois a da direita), que é a mesma ordem da tabela do manual. Manter.
