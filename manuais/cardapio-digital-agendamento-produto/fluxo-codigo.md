# fluxo-codigo.md — #72 Produto só com agendamento (uso interno, NÃO publicar)

## Campo no cadastro do produto

- UI: `src/components/ModalEditarProduto.tsx` — bloco dentro do
  `<details>` **Opções avançadas**, só quando `!isComplemento`.
  Switch `id="somenteAgendamento"`, rótulo *Somente agendamento
  (Cardápio Digital Delivery Entrega / Retirada)* e descrição
  *Esse produto só pode ser pedido com agendamento; ao adicioná-lo, o
  pedido inteiro será agendado.*
- Estado: `useEditarProdutoLogic.ts` → `formData.somenteAgendamento`.
- **O campo da API é `importadoMatriz`** (nome legado, não tem relação
  com matriz/filial):
  - leitura: `somenteAgendamento: produtoData.importadoMatriz || false`
  - gravação: `importadoMatriz: isComplemento ? null : formData.somenteAgendamento`
- Grava só no **SALVAR E SAIR** (`useSalvarProduto`). Não tem auto-save.
- Mobile: `MobileEditarProdutoPage.tsx`.

## Editar em Lote

- Botão: `CardapioProdutosTab.tsx` (aba Produtos) e
  `CardapioComplementosTab.tsx` (aba Complementos) — visível com
  `canCardapioAcao('editarLote')`. Também em `ModalBuscaAvancada.tsx`.
- Modal: `src/components/cardapio/ModalEditarLote.tsx`, 3 etapas.
  - Etapa 1 (`Step1Selection`): recebe `filteredProdutos` da aba, ou
    seja **o filtro de setor da tela já entra no assistente**. Todos
    vêm marcados. Filtro interno: busca por nome + setor.
    `ConfirmationDialog` quando há selecionado fora do filtro.
  - Etapa 2 (`Step2Config`): `ToggleField` **Somente Agendamento**
    (`somenteAgendamentoCheck` + `somenteAgendamento`). O switch só
    aparece depois de marcar o checkbox; default do valor é **false**
    (`Não`) — marcar o campo e processar **desliga** a flag.
    `show()` respeita `allowedFields` e a permissão `editar`.
  - Etapa 3 (`Step3Processing`): progresso + linha por produto.
- Hook: `src/hooks/useEditarLote.ts`
  - POST `/api/produto2/cardapio/editarLote`, **lotes de 5**
    (`BATCH_SIZE`), payload é uma **lista**.
  - Campos enviados: `somenteAgendamentoCheck`, `somenteAgendamento`,
    `somenteAgendamentoAnterior: false`. Quando o check é falso manda
    `somenteAgendamento: false` (o backend ignora pelo check).
  - Ao terminar com algum sucesso chama `notificarCardapioAtualizado()`.
- O campo **aparece** no lote de complementos (o `ToggleField` não é
  filtrado por `isComplemento`), mas o cadastro do complemento não tem
  o switch e o `useSalvarProduto` manda `null` para complemento.

## Lista de produtos (painel)

- `VirtualizedProductGrid.tsx`: `produto.importadoMatriz` desenha
  `CalendarDays` `text-[#1565c0]` com o texto *Aceita somente
  agendamento no cardápio digital*. O Tooltip do grid é um **shim com
  `title` nativo** (comentário no topo do arquivo), então o texto
  **não** aparece em screenshot.
- Mobile: `MobileCardapioProdutos.tsx`, mesmo ícone.
- A listagem `/api/produto2/cardapio/produtos/{empresa}/{filial}/{usuario}`
  devolve `importadoMatriz` (`None` quando nunca foi mexido).

## Cardápio público (Vue, fonte fora do repo)

Comprovado no sandbox em 31/08/2026:

- Card do produto e detalhe: etiqueta vermelha **Encomenda** com ícone
  de calendário. Botão de ajuda `.attributes-row__help-btn` abre
  *Mais informações → Encomenda — Produto disponível apenas por
  agendamento*.
- Sacola → **Continuar** com o item de encomenda: abre a tela
  **AGENDAR PEDIDO** mesmo com **Hoje** marcado. Só depois de escolher
  dia/hora vai para as formas de pagamento. Produto normal vai direto
  ao pagamento.
- **Com `agendamento: false` na aba** (teste feito e revertido): a
  etiqueta **continua** aparecendo, o botão **Agendar** desaparece e o
  **Continuar** vai direto ao pagamento — o item de encomenda sai para
  agora. A marca sozinha não segura nada.
- Dias e faixas vêm do #70 (`agendaDiasMin`, `agendamentoDias`,
  `agendaInterM`…) cruzados com o Horário de Atendimento.
- Cache do cardápio público: até **5 minutos**.

IDs sandbox (BeeFood3): empresa 38311, filial 39202, usuário 88711.
Produtos do exemplo: Pudim - Brigadeiro `2515387`, Pudim - Leite
Condensado `2515385`, Pudim - Zero Açucar `2515386` (setor
Sobremesas). Brownie `2515384` ficou de fora, de propósito.

Só abrir a aba **Agendamento** já dispara um POST do auto-save com o
snapshot atual (mensagem *Configurações de agendamento salvas com
sucesso*) — não altera valor, mas aparece no log.
