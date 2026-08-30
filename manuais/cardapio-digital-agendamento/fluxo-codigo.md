# fluxo-codigo.md — #70 Agendamento do cardápio digital (uso interno, NÃO publicar)

- Aba: `CardapioDigital.tsx` `tab=agendamento`.
- UI: `src/components/cardapio-digital/AgendamentoTab.tsx`.
- Mobile: `MobileAgendamentoTab.tsx`.
- Hooks: `useCardapioDigitalAgendamento` + lógica no próprio tab
  (`useCardapioDigitalAgendamentoLogic` no mobile).
- GET `/api/empresaDelivery2/cardapioDigital/agendamento/{empresa}/{filial}/{usuario}`.
- POST `/api/empresaDelivery2/cardapioDigital/agendamento`.
- Auto-save `useAutoSave` delay **800 ms**. Unmount **não faz flush**.
  Campo fora da faixa → `isFormValid` false → POST não dispara.
- Aviso fixo: só Delivery (Entrega / Retirada).
- Card **Configurações de Tempo** só com `agendamento === true`.
- Switches 2 e 3 `disabled` se o 1º está off.

| Tela | API | Default | Faixa |
|------|-----|---------|-------|
| Agendamento | `agendamento` | false | switch |
| Agendamento com o Cardápio Digital fechado | `agendamentoLojaFechada` | false | switch |
| Só aceita agendamento | `agendaSomente` | false | switch |
| Dias mínimo | `agendaDiasMin` | 0 | 0–30 |
| Dias máximo | `agendamentoDias` | 30 | 1–60 |
| Iniciar depois de aberto | `agendaMinAntes` | 2 | 0–720 |
| Finalizar antes de fechar | `agendaMinDps` | 36 | 0–720 |
| Tempo mínimo para iniciar agendamento agora | `agendaAgoraM` | 90 | 0–1440 |
| Intervalo entre agendamentos | `agendaInterM` | 30 | 1–240 |
| Quantidade máxima de pedidos por intervalo | `agendaQtd` | 5 | 1–999 |

`agendaMinAntes` no código é “minutos **depois** de abrir” (o nome da
API é contra-intuitivo). `agendaMinDps` é minutos **antes** de fechar.

Cardápio Vue (`menu.beefood.com.br`): fonte não está no repo de refs.
Mapeamento comprovado no sandbox:

- Depois da modalidade (Retirar / Entrega): botões **Hoje** e **Agendar**.
- **Agendar** abre overlay **AGENDAR PEDIDO**.
- Faixa horizontal **Dia** (HOJE / SEG 31 / TER 01…).
- Lista **Hora Aproximada** com faixas `HH:MM - HH:MM`. A duração
  visível da faixa no Vue foi **30 min**; `agendaInterM` é o passo
  entre os **inícios** (60 → 02:00, 03:00, 04:00…).
- Com min=2 e máx=7 (hoje 30/08): dias **TER 01 … SEG 07**. Máximo
  = quantidade de dias a partir do primeiro permitido.
- Rodapé: **AGENDAR PEDIDO** / **CANCELAR AGENDAMENTO**.
- `agendaSomente` some o **Hoje**.
- `agendaAgoraM` só entra quando o dia selecionado é hoje.
- Slots cruzam com a grade Delivery (`Horário Atendimento`).
- Cache do menu público: até **5 minutos**.

IDs sandbox (BeeFood3): empresa 38311, filial 39202, usuário 88711.
`empresaDeliveryID` 39764.

Preenchimento via Playwright `fill` em sequência **não é confiável**
aqui: o `useEffect` do GET e o debounce do auto-save se pisam. Gravar
pelo POST autenticado e recarregar a aba para confirmar.

Filtro de pedidos agendados no Delivery:
`src/utils/deliveryAgendamentoFilter.ts` — outra tela, fora deste
manual. Switch **Somente Agendamento** no produto:
`ModalEditarProduto.tsx` — também fora.
