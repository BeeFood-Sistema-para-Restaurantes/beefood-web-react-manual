# fluxo-codigo.md — Segunda conferência (mapeamento técnico)

> Mapa do código que sustenta o manual `caixa-conferencia-2.md`. Base: `beefood-web-react`
> (commit `d4b1ad0`, produção `v3.190826.0925`). **Não publicar** — material interno.
> O mapa geral da tela de conferência está em `../caixa-fechar/fluxo-codigo.md`; aqui ficam
> apenas as particularidades da 2ª conferência.

---

## 1. É o mesmo componente do fechamento

A segunda conferência não tem tela própria. Ela é o `CaixaFecharModal` com
`readOnly={true}`, depois que o usuário aciona `handleAddSecondConference` e o estado
`showSecondConference` passa a `true`.

Pontos de entrada (ambos com `readOnly={true}`):

| Onde | Como |
|------|------|
| `src/pages/Caixa.tsx` | Ação **Ver Conferência** (botão verde) na linha do caixa fechado |
| `src/components/CaixaVerModal.tsx` | Botão **VER CONFERÊNCIA** quando `situacao === "FECHADO"` |

## 2. Quando o botão "Adicionar 2ª Conferência" aparece

```tsx
readOnly && data?.situacao === 'FECHADO' && !showSecondConference && !data?.conferido
```

Ou seja: caixa fechado, aberto em modo leitura, sem segunda conferência em andamento e
**ainda não conferido**. Depois de `conferido === true` o botão deixa de existir — não há
terceira conferência.

Além disso, os três recursos (reabrir, ver conferência e adicionar a 2ª) dependem da flag de
permissão `itemID136`.

## 3. O que muda na tabela

Com `showSecondConference === true`:

- O título vira `Conferência de Valores - 2ª Conferência`.
- A coluna de input passa a se chamar **2ª Conferência** e escreve em `secondConferenceData`.
- Aparece uma coluna extra **1ª Conferência** (só leitura) ao final da linha.
- Nos totais surge **Quebra 1ª Conf.** (`quebraDeCaixaPrimeira`), ao lado da **Quebra de
  Caixa** da conferência atual.
- Surge a seção com o campo **Observações da Conferência** (`conferidoObs`) e o checkbox
  **Conferência realizada e valores conferidos** (`conferido`).
- O botão **Conferir** só habilita com o checkbox marcado:
  `disabled={isLoading || isSaving || !conferido || data?.conferido}`.

Os campos da 2ª conferência começam **vazios** (`emptySecondConferenceData`), de propósito —
a recontagem não é pré-preenchida com o valor anterior.

## 4. A troca de campos no envio (importante)

`handleConferirCaixa` faz `POST /datasnap/rest/caixa2/caixaFecharSalvarFecharConferir` com
`tipo: "CONFERIR"` e **inverte** os campos:

| O que | Vai para |
|-------|----------|
| Valores da **1ª** conferência (`conferenceData`) | campos `conferenciaDinheiro2`, `conferenciaCD2`, ... |
| Valores da **2ª** conferência (`secondConferenceData`) | campos `conferenciaDinheiro`, `conferenciaCC`, ... |

Mais `conferido` e `conferidoObs`. Ou seja: **depois de conferir, os campos "sem sufixo"
guardam a segunda conferência** e os campos `*2` guardam a primeira. É por isso que a
releitura (`data.conferido === true`) mostra a 2ª como coluna principal e a 1ª na coluna
lateral:

```ts
conferenceValue = data[type.conferenciaField]           // 2a conferencia
totalPrimeiraConferencia += data[type.conferenciaField2] // 1a conferencia
```

Quem for consultar banco ou API precisa saber dessa inversão para não ler os valores trocados.

## 5. Efeitos observados após confirmar (19/08/2026)

- `conferido` passa a `true` → cadeado na listagem, com tooltip **Segunda conferência
  concluída** (`Caixa.tsx`, `caixa.conferido === true`).
- A coluna **Conf. Saldo Final** da listagem passa a refletir a **segunda** conferência
  (mudou de R$ 1.909,43 para R$ 1.911,98).
- A coluna **Quebra de Caixa** da listagem passa a mostrar **R$ 0,00** com check verde.
- **A Data/Hora Fechamento foi regravada:** o registro mudou de `19/08/2026 10:18` (fechamento)
  para `19/08/2026 10:54` (momento da conferência). Vale saber ao comparar prints antigos ou
  relatórios — o horário exibido passa a ser o da conferência, não o do fechamento.
- A tela reaberta vem com `showSecondConference` já ativo, porque
  `hasSecond = data.situacao === 'FECHADO' && data.conferido === true`.

## 6. Rótulos exatos de tela

| Onde | Texto |
|------|-------|
| Título | `Conferência de Valores - 2ª Conferência` |
| Botão que inicia | `Adicionar 2ª Conferência` (tooltip: `Inicia uma segunda conferência para validar os valores do caixa fechado`) |
| Colunas | `2ª Conferência` (input) e `1ª Conferência` (leitura) |
| Totais | `Quebra de Caixa` e `Quebra 1ª Conf.`; quando zerada aparece `Correto` |
| Observação | `Observações da Conferência` / placeholder `Digite observações sobre a conferência (opcional)` |
| Declaração | `Conferência realizada e valores conferidos` |
| Confirmação | `Confirma a conferência do caixa?` / botões `Conferir` e `Cancelar` |
| Listagem | tooltip do cadeado: `Segunda conferência concluída` |
