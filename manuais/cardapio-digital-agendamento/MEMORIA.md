# MEMORIA.md — #70 Agendamento do cardápio digital

## Escopo
Aba **Cardápio Digital → Agendamento**: três switches + sete campos
de prazo, cada um mapeado na tela **AGENDAR PEDIDO** do cardápio
público (faixa de dias + Hora Aproximada).

Não cobre: grade semanal (#32), pausa (#33), filtro de agendados no
Delivery, switch de agendamento no cadastro do produto.

## Origem
Pedido do dono (30/08/2026): manual detalhado parâmetros × tela do
cardápio onde o cliente escolhe data/hora. Estudo e execução no
mesmo turno. O #33 já tinha os três switches em visão geral e
avisava que os prazos “merecem um manual próprio”.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-aba-switches.png` | setas | Aba + aviso + 3 switches |
| `02-par-chaves.png` | recorte | Painel (3 switches) → Hoje / Agendar |
| `03-par-dias.png` | recorte | Painel (2 e 7) → TER 01 / QUA 02… |
| `04-par-horarios.png` | recorte | Dois 60 separados: 01:00+60→02:00 e 23:59−60→22:00 |
| `05-cardapio-digital.png` | setas | Tira dos três celulares |
| `04-cel-hoje-agendar.png` | pura | Fonte do recorte / tira |
| `05-cel-calendario.png` | pura | Fonte do recorte / tira |
| `06-cel-horarios.png` | pura | Fonte do recorte / tira |
| `02-tempo.png` | pura | Fonte dos recortes de tempo |

Pedido do dono (mesmo dia): lado a lado parâmetro → tela, com
recortes. A Parte 2 passou a ser três pares `montar_par` (painel à
esquerda, cardápio à direita, seta verde). A tira ficou na Parte 3.

Pedido seguinte: a `04-par-horarios.png` misturava iniciar 60,
finalizar 60 e intervalo 60 num par só — é onde mais se confundem.
Virou compositor didático (`montar_horarios_didatico`): dois cards
com a conta, linha do tempo, exemplo de almoço 11:00–15:00 e nota
separando o intervalo. A última faixa **não** é `23:59−60=22:59`;
o limite é 22:59 e a última que cabe no passo de 1 h é 22:00–22:30.

`02-tempo-dias.png` e `03-tempo-intervalo.png` são extras de captura
(não entram no `.md`).

## Decisões
- Exemplo didático gravado via POST (auto-save + `fill` em sequência
  perdeu os números no primeiro teste): min **2**, máx **7**,
  iniciar/finalizar **60**, agora **90**, intervalo **60**, qtd **5**.
  Switches: ON / ON / OFF.
- **Só aceita** ficou OFF para não quebrar o checkout imediato dos
  #19/#20/#64.
- Grade do sandbox **não** é mais a do #32 (11–15 / 18–23, domingo
  fechado). Em 30/08/2026 a Delivery está **~01:00–23:59** todos os
  dias (segunda ainda tem um bloco extra 18:00–22:00). O manual
  ensina a **conta** (abertura + iniciar / fechamento − finalizar) e
  usa essa grade no exemplo.
- Calendário com min=2 / máx=7 (hoje 30/08): **TER 01 … SEG 07**.
  Máximo = quantidade de bolinhas a partir do primeiro dia, não
  “hoje + N”.
- Slots terça: **02:00–02:30** até **22:00–22:30**, início de hora
  em hora. `agendaInterM=60` é o espaço entre **inícios**; a faixa
  visível dura **30 min**. Primeiro = 01:00+60; último cabe antes
  de 23:59−60.
- `agendaAgoraM` só vale no dia de hoje. Com min=2 o calendário não
  mostra HOJE; o efeito (16:35 + 90 → primeiro slot 18:05, intervalo
  30) foi visto antes, com min=0 e defaults. Ficou no texto, sem
  celular extra.
- Qtd máx: sem encher 5 pedidos; só texto.
- Tira de 3 aparelhos (modalidade / dias / horários). Viewport
  390×844 dsf 2. Não clicar Retirada na home. Combo R$ 39. Telefone
  (15) 99999-8888. **Não finalizar.** Cashback: CANCELAR se aparecer.
- Cache do cardápio: até **5 minutos**.

## Estado deixado no sandbox
- Agendamento **ON**, loja fechada **ON**, Só aceita **OFF**
- Dias 2 / 7; 60 / 60 / 90 / 60 min; 5 pedidos
- Grade de horário **não** foi alterada
- Cashback R$ 5 do Teste Manual intacto
- Tabelas #68/#69 e descontos #64 intactos

## Status
Concluído — aguardando publicação.
