# fluxo-codigo.md — Fechar Caixa (mapeamento técnico)

> Mapa do código que sustenta o manual `caixa-fechar.md`. Base: `beefood-web-react`
> (commit `d4b1ad0`, produção `v3.190826.0925`). **Não publicar** — material interno.

---

## 1. Componentes e hooks

| Arquivo | Papel |
|---------|-------|
| `src/pages/Caixa.tsx` | Listagem de caixas. Ações por linha: **Ver Caixa** (azul), **Reabrir Caixa** (laranja) e **Ver Conferência** (verde). Colunas `Conf. Saldo Final` e `Quebra de Caixa`. |
| `src/components/CaixaVerModal.tsx` | Detalhes do caixa. Mostra **FECHAR CAIXA** quando `situacao === "ABERTO"` e **VER CONFERÊNCIA** quando `FECHADO`. |
| `src/components/CaixaFecharModal.tsx` | A tela de conferência (802 linhas). É o **mesmo componente** para fechar e para ver a conferência — muda só a prop `readOnly`. |
| `src/hooks/useCaixaFecharDetalhes.ts` | Estado e regras da conferência: campos, cálculos, e as três chamadas de gravação. |
| `src/hooks/useCaixaFechar.ts` | Busca os dados do fechamento (`CaixaFecharData`). |
| `src/hooks/useCaixaValidarFechamento.ts` | Pré-validação de vendas sem pagamento total. |
| `src/components/caixa/CaixaVendasPendentesModal.tsx` | Tela das vendas pendentes, com pagamento embutido via `ModalPagamentos`. |
| `src/components/CalculadoraModal.tsx` | Somador de valores usado por linha da conferência. |
| `src/hooks/useCaixaImpressaoResumo.ts` | Gera o **Resumo Conferência de Caixa** (`gerarLinhasResumoConferencia`). |
| `src/components/mobile/caixa/MobileCaixaFecharPage.tsx` | Versão mobile do mesmo fluxo (**fora do escopo deste manual**). |

**Descoberta que definiu o escopo:** não existe modal separado de conferência. O
`CaixaFecharModal` é usado em três pontos, sempre o mesmo componente:

1. `CaixaVerModal` → `readOnly={caixaDetalhes?.situacao === "FECHADO"}`
2. `Caixa.tsx` (ação **Ver Conferência**) → `readOnly={true}`
3. O próprio fechamento (caixa aberto) → `readOnly={false}`

---

## 2. Rotas da API (DataSnap)

| Momento | Rota | Método |
|---------|------|--------|
| Pré-validação ao clicar em **FECHAR CAIXA** | `/datasnap/rest/caixa2/caixaValidarFechamento/{empresaID}/{filialID}/{usuarioID}/{caixaID}` | GET |
| Carregar os dados da conferência | `/datasnap/rest/caixa2/caixaFechar/{empresaID}/{filialID}/{usuarioID}/{caixaID}` | GET |
| Salvar / fechar / conferir | `/datasnap/rest/caixa2/caixaFecharSalvarFecharConferir` | POST |
| Atualizar uma venda após pagar | `/datasnap/rest/venda2/vendaDetalhes/{empresaID}/{usuarioID}/{preVendaID}/{esteira}` | GET |

O POST único distingue a ação pelo campo `tipo`:

| `tipo` | Ação | Efeito |
|--------|------|--------|
| `SALVAR` | Botão **Salvar Conferência** | Grava os valores e **mantém o caixa aberto**. |
| `FECHAR` | Botão **Fechar Caixa** | Grava e fecha. Em seguida o modal dispara a pergunta de impressão. |
| `CONFERIR` | Botão **Conferir** (2ª conferência) | Grava a dupla checagem e marca `conferido`. |

---

## 3. Regras de cálculo

Em `useCaixaFecharDetalhes.ts`:

- **Formas exibidas:** `visiblePaymentTypes` filtra `paymentTypes` mantendo só as que têm
  `entrada > 0`. Por isso a tabela muda de caixa para caixa.
- **Comparação do Dinheiro:** usa `data.saldoDinheiro` (entradas menos saídas), não
  `entradaDinheiro`. É o que faz a sangria já entrar descontada.
- **Diferença por linha:** `conferido - comparado`, zerada quando `|diff| < 0,01`.
- **Quebra de caixa:** `totalConferido - (totalEntrada - totalSaidaDinheiro)`.
  Positivo aparece como **(Sobra)**, negativo como **(Falta)**.
- **Campo vazio** é gravado como `null` (`convertValue`), não como zero.

### Detalhe da calculadora

`handleApplyCalculator` faz `total.toString().replace('.', ',')`. Um total de 100 entra no
campo como `"100"`, não `"100,00"` — o valor é o mesmo, mas aparece sem os centavos até
ser salvo. Isso está explicado no manual para não gerar dúvida.

### Troca de campos na 2ª conferência

Em `handleConferirCaixa` os valores são invertidos ao enviar: a **1ª** conferência vai nos
campos `conferencia*2` e a **2ª** nos campos `conferencia*` originais. Quem for produzir o
manual da segunda conferência precisa saber disso ao ler o banco ou a API.

---

## 4. Permissão

A flag `itemID136` (vem de `caixaListagem` / `caixaDetalhes`) controla:

- o botão **Reabrir Caixa** na listagem;
- o botão **Ver Conferência** na listagem;
- o botão **Adicionar 2ª Conferência** dentro da conferência.

Sem ela, o usuário fecha o caixa mas não revisita nem reabre.

---

## 5. Rótulos exatos de tela

| Onde | Texto |
|------|-------|
| Título da conferência | `Conferência de Valores - 1ª Conferência` |
| Totais | `Total Entrada`, `Total Saída`, `Entrada Conferida`, `Quebra de Caixa` |
| Saldos | `Saldo Final`, `Saldo Final Conferido` |
| Detalhe do Dinheiro | `Saldo de Abertura`, `Entrada Manual`, `Vendas` |
| Confirmação de fechamento | `Confirma fechamento do caixa?` / botões `Fechar caixa` e `Cancelar` |
| Impressão | `Deseja imprimir a conferência?` / botões `Sim, imprimir` e `Não` |
| Saída sem salvar | `Tem certeza que deseja sair?` / `Sair sem salvar` e `Continuar editando` |
| Vendas pendentes | `N vendas sem pagamento total` / `FECHAR CAIXA MESMO ASSIM (F2)` / `PROSSEGUIR FECHAMENTO` quando a lista está vazia |
| Aviso de pendências | `Fechar caixa com N vendas pendentes?` / `NÃO, REVISAR (ESC)` e `FECHAR ASSIM MESMO (ENTER)` |
| Calculadora | `Calculadora - <forma>` / `Valores Adicionados` / `Total:` / `Incluir Conferência` |
| Tooltip do cadeado (após 2ª conferência) | `Segunda conferência concluída` |

---

## 6. Atalhos de teclado

| Tecla | Onde | Efeito |
|-------|------|--------|
| `Enter` / `Tab` | Campo da conferência | Pula para a próxima forma de pagamento. |
| `Enter` | Calculadora | Adiciona o valor à lista. |
| `F1` | Calculadora | Aplica o total no campo (mesmo que **Incluir Conferência**). |
| `Esc` | Calculadora | Fecha sem aplicar. |
| `F2` | Vendas pendentes | Equivale a **FECHAR CAIXA MESMO ASSIM**. |
| `Enter` | Aviso de pendências | Equivale a **FECHAR ASSIM MESMO**. |
