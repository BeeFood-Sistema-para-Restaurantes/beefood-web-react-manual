# Prompt para publicar o manual — Fechar a loja fora do horário (#33)

> Cole o texto abaixo na IA de documentação do app, junto com as 10 imagens da pasta
> `imagens-tratadas/`, na ordem da tabela do fim.

---

## Instrução

Publique um manual de usuário final chamado **"Fechar a loja fora do horário"**, na seção
**Cardápio Digital**. Use o conteúdo de `manuais/loja-fechar-pausa/loja-fechar-pausa.md` como
fonte, **sem reescrever o texto** — ele já está no padrão dos outros manuais publicados.

Este manual é **par** do **"Horário de atendimento"** (#32). Publique os dois juntos, ou o #32
primeiro: os dois se referenciam.

### Estrutura a preservar

1. Os três jeitos de fechar (a tabela comparativa — é a peça central do manual)
2. Parte 1 — Pausa temporária: o caminho mais rápido
3. Parte 2 — Pausa programada: feriado e período marcado
4. Parte 3 — Desligar um canal por tempo indeterminado
5. Parte 4 — Continuar vendendo com a loja fechada (Agendamento)
6. Parte 5 — Avisar o cliente pelo WhatsApp
7. Resumo: o que usar em cada situação
8. Perguntas frequentes
9. Manuais relacionados

### Pontos que NÃO podem se perder

- **A diferença entre os três mecanismos**: as pausas têm fim marcado e a loja reabre sozinha; o
  switch não tem fim e fica desligado até alguém religar.
- **A atualização leva até um minuto** para chegar ao cliente (o sistema faz polling de 60 s).
  O próprio produto avisa isso ao criar a pausa.
- **A pausa rápida do topo fecha os dois canais.** Para pausar só um, é preciso usar o modal da
  aba, que tem switch por canal.
- **Switch desligado não avisa nada** — não há alerta no painel. É a forma mais fácil de perder
  venda sem perceber; para algo temporário, preferir pausa.
- **Desligar o switch Ativo encerra a pausa antes da hora**, e ela fica guardada na lista para
  reutilizar (útil para feriados recorrentes).
- **O agendamento vale só para o Delivery (Entrega / Retirada)** — não existe para o presencial.
- **"Agendamento com o Cardápio Digital fechado"** é o switch que permite ao cliente pedir fora
  do horário; depende do switch **Agendamento** estar ligado.
- **Para fechar todo domingo, não é pausa** — é a grade semanal (manual #32).
- A variável **`**MEU_HORARIO**`** na mensagem de WhatsApp mostra sempre o horário atualizado.

### Tabela que deve aparecer inteira

| Situação | O que fazer |
|----------|-------------|
| Cozinha atolada, 20 minutos de atraso | Pausa temporária de 15 ou 30 min, no menu do topo |
| Acabou o ingrediente principal hoje | Pausar por hoje |
| Feriado na semana que vem | Pausa programada com data e hora |
| Férias de duas semanas | Pausa programada com o período todo |
| Sem entregador por tempo indefinido | Desligar o switch Entrega, mantendo a Retirada |
| Reforma no salão, delivery normal | Pausa programada só no Presencial |
| Quer receber pedido para amanhã mesmo fechado | Agendamento com o Cardápio Digital fechado |

---

## Imagens, na ordem

Todas em `manuais/loja-fechar-pausa/imagens-tratadas/`.

| # | Arquivo | Tipo | Legenda / o que mostra |
|---|---------|------|------------------------|
| 1 | `01-header-popover.png` | setas | Menu do cardápio no topo · 1 onde clicar · 2 Pausa Temporária · 3 status do canal · 4 switches de canal |
| 2 | `02-pausa-temporaria-menu.png` | setas | Submenu · 1 Pausas ativas · 2 pausar por 15/30/45 min · 3 Pausar por hoje |
| 3 | `03-pausa-aba.png` | setas | Aba Pausa Programada · 1 Adicionar · 2 switch Ativo · 3 período e motivo |
| 4 | `04-pausa-modal.png` | setas | Modal em branco · 1 presets de duração · 2 HOJE/AMANHÃ · 3 Início e Fim · 4 switches de canal · 5 Motivo |
| 5 | `05-pausa-preenchida.png` | setas | Preset aplicado · 1 30 MINUTOS · 2 início e fim automáticos · 3 CONFIRMAR PAUSA (F2) |
| 6 | `06-pausa-confirmacao.png` | setas | Confirmação · 1 duração, início e fim · 2 CONFIRMAR (ENTER) |
| 7 | `07-pausa-criada.png` | setas | Pausa valendo · 1 Ativo ligado · 2 canais afetados · 3 período |
| 8 | `08-pausa-desativada.png` | contexto | Pausa encerrada antes da hora, com o switch desligado |
| 9 | `09-configuracoes-switches.png` | setas | Configurações · 1 Delivery Ativo · 2 Entrega/Retirada/Consumo no Local |
| 10 | `10-agendamento.png` | setas | Aba Agendamento · 1 Agendamento · 2 **com o Cardápio Digital fechado** · 3 Só aceita agendamento |

---

## Observações para quem publica

- Manual **somente desktop**.
- Nenhum dado de cliente nas capturas.
- A **Parte 5 (WhatsApp) não tem captura**: o BeeBot do sandbox está desconectado. O texto
  descreve o caminho (**WhatsApp → Respostas**, linha *Mensagem de Loja Fechada*) e a variável
  `**MEU_HORARIO**`. Se houver captura disponível de outra conta, vale acrescentar.
- Na conta usada havia só um cardápio, então o checkbox **Aplicar para todos os cardápios** não
  aparece nas imagens — está explicado na FAQ.
