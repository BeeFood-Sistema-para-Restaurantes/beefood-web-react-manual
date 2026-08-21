# MEMÓRIA — Manual #33 Fechar a loja fora do horário

> Memória detalhada deste manual: decisões, descobertas e estado do ambiente.

Última atualização: 2026-08-21 (manual concluído, aguardando publicação do dono)

---

## 1. Escopo

Par do **#32**. Enquanto o #32 responde *"que horas eu abro?"*, este responde *"preciso fechar
agora"* — que é operação, não configuração.

Cinco partes: pausa temporária (atalho do topo) → pausa programada (aba) → switches de canal →
agendamento com a loja fechada → mensagem de WhatsApp.

A peça central é a **tabela comparativa dos três mecanismos**, que não existe em lugar nenhum do
produto:

| Mecanismo | Duração | Serve para |
|-----------|---------|------------|
| Pausa temporária | 15 min a "por hoje" | fila cheia, cozinha atrasada |
| Pausa programada | período com data | feriado, férias, manutenção |
| Switch do canal | até alguém religar | suspender um canal por tempo indeterminado |

---

## 2. Descobertas

### Pausa temporária e pausa programada são a mesma API

Duas telas, um endpoint (`POST .../cardapioDigital/pausa`). A diferença:

- **atalho do topo** — rápido, mas fecha **os dois canais** (grava `delivery` e `presencial` como
  `true`) e usa o motivo fixo *"Pausa temporária"*;
- **aba** — permite escolher data, hora, canais e motivo, e guarda histórico.

O manual explica isso na FAQ, porque a dúvida "qual das duas eu uso?" é imediata.

### O badge do topo é a única confirmação visual

Com a pausa criada, o badge do popover mudou para **Fora do horário de atendimento** nos dois
canais. É a forma mais rápida de conferir se a pausa pegou — e virou a seta 3 da imagem 01.

O status vem do backend (`horarioAtendimentoAgora` no cabeçalho) e o contexto do front faz
polling de **60 s**. É isso que justifica o aviso *"pode levar até 1 minuto para refletir"*, que
o próprio sistema mostra ao criar a pausa.

### Switch desligado não avisa nada

Não há alerta no painel lembrando que um canal está desligado — só o badge no popover. É a forma
mais fácil de perder venda sem perceber, e o manual recomenda preferir pausa quando o
fechamento é temporário (a pausa reabre sozinha).

### O agendamento é só para delivery

O aviso fixo na aba diz: *"O agendamento de pedidos é válido somente para o Cardápio de Delivery
(Entrega / Retirada)"*. Não existe agendamento para o presencial. Vale destacar, porque a
pergunta aparece.

---

## 3. Estado do ambiente

Não precisou limpar base.

**O que foi alterado:**

| Ação | Detalhe |
|------|---------|
| Pausa criada | preset de **30 MINUTOS** (20/08/2026 21:58 → 22:28), sem motivo preenchido |
| Pausa desativada | switch **Ativo** desligado depois das capturas, para não deixar a loja fechada |

A pausa antiga de 16/07/2026 já existia e continua desligada — ela aparece na imagem 03 e serve
para mostrar que pausas ficam guardadas.

**Nenhum switch de canal foi mexido.** Os três do delivery (Entrega, Retirada, Consumo no Local)
e o QR Code Presencial seguem ligados, como estavam.

### Detalhe de automação

O campo **Motivo** não foi preenchido: o modal não é um `div[role="dialog"]` e três tentativas de
seletor falharam (por classe, por xpath a partir do rótulo e por `.last` do tipo texto). O
resultado foi uma pausa com motivo `-`, o que não prejudica as capturas — o campo aparece vazio
na imagem 04, que é justamente onde ele é explicado.

Também apareceu um comportamento estranho do ambiente: o traceback do Playwright passou a citar
seletores de versões anteriores do script, como se houvesse cache. Criar um **arquivo novo** com
outro nome resolveu. Vale lembrar disso se um erro parecer não corresponder ao código.

---

## 4. Marcação das imagens

10 imagens, **28 setas** em 9 delas. Uma de contexto (`passthrough`): a pausa desativada, onde o
ponto é o switch cinza no meio da lista.

Duas telas são popovers ancorados no topo (o menu de cardápios e o submenu de pausa), então os
badges ficam à direita deles, sobre a área do preview do cardápio — que não é o assunto.

Conferência automática (`annotate.py` × `.md`): **10 imagens, 0 divergência**.

---

## 5. O que ficou de fora

| Item | Por quê |
|------|---------|
| Captura da mensagem de loja fechada no WhatsApp | O BeeBot do sandbox está desconectado; o manual explica o caminho em texto (**WhatsApp → Respostas**, variável `**MEU_HORARIO**`) |
| Campos de prazo do Agendamento | Seis campos com faixas próprias; merece manual próprio |
| Pausa em múltiplos cardápios | O sandbox tem uma filial, então o checkbox **Aplicar para todos os cardápios** não aparece; explicado na FAQ |
| Efeito visto pelo cliente | O cardápio do cliente (`menu.beefood.com.br`) é outro sistema, fora do repositório de referência |

---

## 6. Próximo natural

**Agendamento** — a aba tem os três switches (já cobertos em visão geral aqui) mais seis campos
numéricos de prazo, com faixas específicas mapeadas em `fluxo-codigo.md`. É o complemento
natural deste par de manuais.
