# Fluxo de código — Horário de atendimento

> Mapeamento técnico do que o manual **#32 Horário de atendimento** documenta.
> Fonte: `beefood-web-react`, somente leitura. Levantado em 21/08/2026, versão
> **v3.200826.2051** em produção.
> O que fecha a loja fora da grade está em `manuais/loja-fechar-pausa/fluxo-codigo.md`.

---

## 1. Onde fica

| Item | Valor |
|------|-------|
| Página | `src/pages/CardapioDigital.tsx` |
| Rota | `/cardapio-digital?tab=horarioAtendimento` |
| Sub-aba | `&subTab=delivery` ou `&subTab=presencial` |
| Componente | `src/components/cardapio-digital/HorarioAtendimentoTab.tsx` |
| Mobile | `src/components/mobile/cardapio-digital/MobileHorarioAtendimentoTab.tsx` |
| Hook da API | `src/hooks/useCardapioDigitalHorarioAtendimento.ts` |
| Validação | `src/utils/horarioAtendimentoSort.ts` |
| Timeline | `src/components/cardapio-digital/horario-timeline/TimelineSemanal.tsx` |
| Popover do bloco | `.../horario-timeline/BlocoHorarioPopover.tsx` |
| Assistente | `.../horario-timeline/WizardHorarioModal.tsx` |

A aba **Horário Atendimento** é a 6ª das 11 abas do Cardápio Digital. A visão escolhida
(Timeline ou Lista) fica no `localStorage`, chave `horario-atendimento-view`.

---

## 2. Duas grades no mesmo endpoint

O `GET` devolve **todos** os registros da filial, e o front separa pelas flags:

| Sub-aba | Filtro |
|---------|--------|
| **Delivery** | `delivery: true`, `presencial: false` |
| **Presencial** | `presencial: true`, `delivery: false` |

Confirmado no sandbox: cada dia tem **dois registros**, um de cada tipo. Campos observados:

```json
{
  "deliveryAtendimentoID": 542956,
  "filialID": 39202,
  "diaSemana": 1,
  "horaInicio": "1970-01-01T04:00:00.000Z",
  "horaFim": "1970-01-01T21:15:00.000Z",
  "horaInicio2": null,
  "horaFim2": null,
  "tempoEntregaMinutos": 45,
  "tempoRetiradaMinutos": 20,
  "presencial": false,
  "delivery": true,
  "ativo": true,
  "lugaresMaximo": null,
  "clone": null,
  "diaSemanaExtenso": "Domingo"
}
```

Notas:

- `diaSemana`: **1 = Domingo** … **7 = Sábado**. A tela exibe começando na segunda.
- As horas vêm como ISO em **1970-01-01** e são lidas com `getUTCHours()` / `getUTCMinutes()` —
  não há seletor de fuso na interface.
- `tempoEntregaMinutos` / `tempoRetiradaMinutos` só existem no registro de delivery.
- `lugaresMaximo` só faz sentido no presencial (não é editável nesta tela).
- `clone: true` marca turnos extras criados pelo botão de clonar.

---

## 3. Turnos

| Recurso | Como funciona |
|---------|---------------|
| Dois turnos por dia | Mesmo registro, campos `horaInicio`/`horaFim` e `horaInicio2`/`horaFim2` |
| Terceiro turno ou mais | Botão **clonar** cria **novo registro** no mesmo dia, com `clone: true` |
| Copiar de um dia para outro | **Não existe.** O clone é sempre no mesmo dia; para replicar, usa-se o Assistente |
| Fechar o dia | `ativo: false`. Os horários **não** são apagados |

Atalhos de configuração rápida (topo da visão Lista):

| Botão | Grupo | Cada opção |
|-------|-------|------------|
| Pode selecionar apenas uma opção | mín 1 / máx 1 | mín 1 / máx 1 |
| Pode selecionar várias opções sem repetir | mín 1 / máx 10 | mín 1 / máx 1 |
| Poderá selecionar várias opções e repetir | mín 1 / máx 10 | mín 1 / máx 10 |

---

## 4. Auto-save

Não há botão de salvar. `useAutoSave` grava ~300 ms depois da última alteração e mostra o toast
**Salvo automaticamente** (id `cardapio-autosave`). Isso vale para a Lista, a Timeline e o
popover do bloco.

---

## 5. O Assistente (WizardHorarioModal)

Três passos, com um `AlertDialog` antes:

**Aviso** — *"Reconfigurar horários / O assistente irá substituir os horários atuais. Deseja
continuar?"*, botões **Não (ESC)** e **OK! (ENTER)**. Só aparece quando já existe horário.

**Passo 1** — *"Em quais dias você abre?"*: botões Seg a Dom, atalhos **Todos**, **Dias úteis**,
**Fim de semana**. Default: Seg a Sáb (`DEFAULT_DIAS_SELECIONADOS`). Sem nenhum dia, avisa
*"Selecione ao menos um dia."*

**Passo 2** — *"Como você opera?"*, com quatro presets:

| Preset | Horário |
|--------|---------|
| Restaurante (Almoço + Jantar) | 11:00–15:00 e 18:00–23:00 |
| Lanchonete / Pizzaria (só noite) | 18:00–23:59 |
| Padaria / Café (manhã) | 06:00–14:00 |
| Comercial | 09:00–18:00 |

Campos: **Abertura**, **Fechamento**, checkbox *Tenho um segundo turno (ex.: almoço + jantar)*,
**Abertura 2**, **Fechamento 2** e — **só na sub-aba Delivery** — **Tempo de entrega (min)** e
**Tempo de retirada (min)**. Bloqueia o avanço se `horaInicio >= horaFim`.

**Passo 3** — *"Revise sua configuração"*, com a semana e o botão **Aplicar**.

O wizard abre sozinho na primeira carga quando nenhum dia tem par válido na sub-aba atual. O
texto do cabeçalho muda conforme a sub-aba: *"Configure os horários de **Delivery**"* ou
*"...de **Presencial**"*.

---

## 6. Virada de meia-noite

Ao salvar um par em que `inicio > fim`, o front detecta `crossesMidnight` e **divide o turno**:

- o registro do dia vai até **23:59**;
- um registro novo é criado no **dia seguinte**, de **00:00** até o fim original.

Toast (info, 5 s): *"Turno dividido: 18:00→23:59 (Segunda-Feira) e 00:00→02:00 (Terça-Feira)"*.

Comprovado no sandbox com o sábado: o campo virou 23:59 e o domingo ganhou 00:00–02:00.

Detalhe da Timeline: ela só desenha pares com `inicio < fim` (`isPairValid`), então um turno que
cruza a meia-noite **não aparece como bloco único** — aparece como os dois pedaços, um em cada
dia. A sanitização da API aceita `isPairValid` **ou** `crossesMidnight`.

---

## 7. Validações

| Mensagem | Quando |
|----------|--------|
| `{Dia}: horário inicial e final não podem ser iguais ou vazios` | par 1 inválido em dia ativo (id `horario-atendimento-invalido`) |
| `Nenhum horário válido para salvar. Corrija os horários com início e fim iguais ou vazios.` | nada passou na sanitização |
| `Horários não podem se sobrepor no mesmo dia.` | sobreposição na timeline (id `horario-overlap`) |
| `Turno dividido: …` | split da meia-noite |
| `Salvo automaticamente` | sucesso |
| `Nenhum registro base encontrado para esse dia.` | adicionar bloco sem registro |
| `Novo período criado. Ajuste o horário no bloco clonado.` | clone |
| `Organizando horários...` | overlay durante reordenação |

Diálogos: **Confirmar exclusão** (*"Deseja realmente excluir este horário de {dia}? Esta ação
não pode ser desfeita."*) e **Resetar Horários** (*"Deseja resetar todos os horários de
atendimento? Esta ação não pode ser desfeita."*).

Limites numéricos: tempo de entrega e de retirada de **0 a 999** minutos.

---

## 8. Reset é global, não por sub-aba

**Achado importante deste manual.** O endpoint é
`POST /api/empresaDelivery2/cardapioDigital/atendimento/horarioReset`, sem parâmetro de canal.

Comprovado no sandbox: o reset rodado na sub-aba **Delivery** deixou a grade **Presencial**
inteira fechada. Ou seja, quem reseta para arrumar um canal derruba o outro.

O Assistente, por contraste, **substitui apenas a grade da sub-aba atual**.

---

## 9. Endpoints

| Operação | Método | Path |
|----------|--------|------|
| Listar | GET | `/api/empresaDelivery2/cardapioDigital/atendimento/{empresaID}/{filialID}/{usuarioID}` |
| Salvar | POST | `/api/empresaDelivery2/cardapioDigital/atendimento` (body com `atendimentos[]`) |
| Excluir clone | DELETE | `/api/empresaDelivery2/cardapioDigital/atendimento` |
| Clonar | POST | `/api/empresaDelivery2/cardapioDigital/atendimento/clonar` |
| Resetar | POST | `/api/empresaDelivery2/cardapioDigital/atendimento/horarioReset` |

O horário é **por `filialID`**: cada cardápio tem a sua grade, trocada pelo seletor do topo.

---

## 10. Onde o horário aparece fora desta tela

| Lugar | Como usa |
|-------|----------|
| Menu de cardápios (topo) | Badge com `horarioAtendimentoAgora` — texto pronto do backend |
| `CardapiosStatusContext` | Polling de 60 s em `GET .../cardapioDigital/status/...` |
| Delivery (tela de pedidos) | Bolinha verde/vermelha por filial |
| WhatsApp → Respostas | Variável `**MEU_HORARIO**` na mensagem de loja fechada |
| Automações de WhatsApp | *"As mensagens só são enviadas quando o cardápio digital estiver aberto para pedidos"* |

**Horários que não são da loja** e confundem quem procura: agenda de **Avisos**, agenda de
**banners e destaques** (`bannerAgenda.ts`), janelas de **campanha** e o horário do **suporte
BeeFood** (`suporteHorarios.ts`).

---

## 11. Nota sobre o ambiente de captura

Esta tela usa `input type="time"`. O Chromium renderiza o campo em **AM/PM** quando o navegador
está em inglês, e as capturas precisam do formato 24h que o usuário brasileiro vê.

O que resolve é a variável de ambiente **`LANG=pt_BR.UTF-8`** no processo do Chromium. Testado
em 21/08/2026: nem o `locale` do contexto do Playwright nem o argumento `--lang` mudam o formato
do campo — só o `env`. O campo passou de 189 px (12h) para 137 px (24h).
