# MEMÓRIA — Manual #32 Horário de atendimento

> Memória detalhada deste manual: decisões, descobertas e estado do ambiente.

Última atualização: 2026-08-21 (manual concluído, aguardando publicação do dono)

---

## 1. Escopo e por que virou dois manuais

O pedido do dono foi *"como configurar horário do cardápio digital/loja?"*. O estudo mostrou que
o assunto está espalhado em **sete lugares** do sistema, e que são **duas perguntas
operacionais diferentes**:

- *"Que horas eu abro?"* — configuração que se faz uma vez → **#32** (este manual)
- *"Preciso fechar agora"* — operação do dia a dia → **#33**

O dono aprovou a divisão em dois. O Agendamento ficou como visão geral no #33 e merece manual
próprio (tem seis campos numéricos com faixas próprias).

Oito partes: onde fica → resetar → Assistente → conferir → ajustar na mão → fechar um dia →
virada de meia-noite → o que o sistema recusa → grade Presencial.

---

## 2. Descobertas

### O reset é global, não por sub-aba

**A mais importante.** O endpoint `.../atendimento/horarioReset` não tem parâmetro de canal.
Rodamos o reset na sub-aba **Delivery** e a grade **Presencial** também ficou toda fechada.

Isso é uma armadilha séria: quem reseta para arrumar o delivery fecha o presencial sem perceber
(e o presencial não avisa nada). O manual alerta em destaque e explica a alternativa — o
**Assistente**, que substitui apenas a grade da sub-aba atual.

### As duas grades vêm no mesmo endpoint

O `GET` devolve todos os registros da filial; o front separa pelas flags `delivery` e
`presencial`. Cada dia tem **dois registros**, um de cada tipo. Era a dúvida que ficou do plano,
e foi resolvida lendo a resposta da API antes de escrever qualquer coisa.

### Virada de meia-noite é resolvida pelo sistema

Digitar 18:00 → 02:00 faz o front **dividir o turno**: o dia vai até 23:59 e nasce um registro
no dia seguinte, de 00:00 até o fim original. O toast explica: *"Turno dividido: 18:00→23:59
(Sábado) e 00:00→02:00 (Domingo)"*.

Comprovado no sandbox com o sábado. É a dúvida clássica de pizzaria, e o manual mostra o efeito
colateral: o domingo, que estava fechado, ganha um turno de madrugada.

### Não existe copiar um dia para outro

O botão **clonar** duplica turno **no mesmo dia** (para um terceiro turno), não entre dias. Para
repetir horário em vários dias, só o Assistente. Fonte garantida de frustração — está no manual.

### Não existe botão de salvar

Auto-save ~300 ms com toast *Salvo automaticamente*. Vale avisar no começo do manual, senão o
usuário procura "Salvar" e acha que não gravou.

### O tempo de entrega mora aqui

**Tempo de entrega** e **Tempo de retirada**, em minutos, ficam na tela de horário, **por dia da
semana**. Ninguém espera encontrar isso aqui. E no Presencial esses campos não existem — o que
serviu para uma comparação didática entre as duas sub-abas (imagens 09 e 19).

---

## 3. Aprendizado de captura: campo de hora em AM/PM

**Vale para qualquer manual com `input type="time"` ou `type="date"`.**

O Chromium renderiza o campo de hora em **AM/PM** quando o navegador está em inglês. As
primeiras capturas saíram com "02:30 AM", que não é o que o usuário brasileiro vê.

Testado em 21/08/2026, quatro combinações:

| Tentativa | Resultado |
|-----------|-----------|
| padrão | 12h (AM/PM) — campo de 189 px |
| `new_context(locale="pt-BR")` | 12h |
| `--lang=pt-BR` nos args | 12h |
| **`env={"LANG": "pt_BR.UTF-8", "LANGUAGE": "pt_BR"}`** | **24h** — campo de 137 px |

Ou seja: **é a variável de ambiente do processo do Chromium**, não o locale do contexto do
Playwright nem o argumento de linha de comando. O `base.py` das capturas foi atualizado para
passar o `env` sempre, com `timezone_id="America/Sao_Paulo"`.

A medida de largura do campo (189 px vs 137 px) é um jeito rápido de testar sem depender de OCR.

---

## 4. Estado do ambiente

Não precisou limpar base: horário é configuração, não cadastro.

**A grade estava desorganizada** (02:30 às 23:00, 00:15 às 23:00, 04:00 às 21:15, sem padrão),
com registros duplicados na quinta-feira. Isso virou material: as imagens 01, 02 e 03 são o
"antes" do manual.

**O que foi alterado:**

| Passo | Efeito |
|-------|--------|
| **Resetar horários** | apagou as duas grades (delivery e presencial) |
| Assistente no Delivery | preset Restaurante, Seg a Sáb, 11:00–15:00 e 18:00–23:00, entrega 45 min / retirada 20 min, Domingo fechado |
| Edição manual | sábado com fim 02:00 → dividido em 23:59 + domingo 00:00–02:00 |
| Assistente no Presencial | mesmo preset, sem tempos |

**Estado final:** grade limpa e realista nos dois canais, com o turno de madrugada no domingo
como exemplo vivo da virada de meia-noite. O reset também limpou as duplicidades da
quinta-feira, o que melhorou as capturas do "depois".

---

## 5. Marcação das imagens

20 imagens, **41 setas** em 17 delas. Três de contexto (`passthrough`): as duas do estado
desorganizado que abrem o manual e a grade Presencial zerada — nelas o ponto é o conjunto.

A tela não é um modal centralizado na maior parte do tempo, então os badges ficam na área vazia
ao lado do conteúdo (à direita da lista, abaixo da timeline) ou na faixa da sidebar. Nos modais
do Assistente, na margem escura em volta.

Conferência automática (`annotate.py` × `.md`): **20 imagens, 0 divergência**.

---

## 6. O que ficou de fora

| Item | Por quê |
|------|---------|
| Campos de prazo do Agendamento | Seis campos com faixas próprias; merece manual próprio |
| Horário por múltiplas filiais | O sandbox tem uma filial; o manual explica em texto |
| Mensagem de loja fechada no WhatsApp | Ficou no #33, em texto (o BeeBot do sandbox não está conectado) |
| Arrastar e redimensionar blocos na timeline | A tela oferece, mas é difícil de capturar em imagem estática |
