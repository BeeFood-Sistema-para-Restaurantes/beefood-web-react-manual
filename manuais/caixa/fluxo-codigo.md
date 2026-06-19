# Caixa — Mapeamento técnico (a partir do código)

> Fonte: exploração do código em `C:\projetos\beefood-web-react\src`.
> Serve de base para escrever o manual do usuário final. Labels = textos exatos da UI.

---

## 1. Página e rota

| Item | Valor |
|------|-------|
| URL | `/caixa` |
| Menu lateral | **Caixa** (ícone Wallet) |
| Página principal | `src/pages/Caixa.tsx` (desktop `CaixaDesktop` / mobile `MobileCaixaPage`) |
| Hook de dados | `src/hooks/useCaixaData.ts`, `useCaixaListagem.ts` |

### Tela inicial (labels)
- Abas: **Listagem de Caixa**, **Cancelamentos** (só gerente c/ permissão).
- Botão: **Abrir Caixa** (verde). Filtro: **Selecione usuário** / **Todos os usuários**. Botão **Atualizar**.
- Colunas: status, **Ações**, **Caixa**, **Data/Hora Abertura**, **Data/Hora Fechamento**,
  **Usuário Abertura**, **Usuário Fechamento**, **Saldo Final**, **Conf. Saldo Final**, **Quebra de Caixa**, **Operações**.
- Tooltips de ação: **Ver Caixa**, **Reabrir Caixa**, **Ver Conferência**.
- Status: `ABERTO`, `FECHADO`, **Em aberto**.

---

## 2. Abrir um caixa

- Componente: `src/components/CaixaAbrirModal.tsx`.
- Ação: botão **Abrir Caixa** → modal **Abrir Caixa** → `POST /datasnap/rest/caixa2/abrir`.

| Campo (label UI) | Obrigatório | Detalhes |
|------------------|-------------|----------|
| **Saldo Inicial em Dinheiro \*** | SIM | Placeholder `R$ 0,00`. Botão **Sem saldo** preenche 0. |
| **Caixa \*** | SIM | Select; placeholder **Selecione um caixa**; opções `Caixa {n} - {titulo}`. |
| **Tipos de Venda** | Não | Switches **Presencial** (sub: Mesas/Comandas) e **Delivery** (sub: Entrega). Ligados por padrão. |
| **Observação (opcional)** | Não | Placeholder `Anotações sobre a abertura...`. |

- Validações/avisos: "Defina um **saldo inicial** e selecione o **caixa** para continuar."
  Pendências: **Selecione um caixa**, **Informe um saldo inicial**.
- Botão principal: **ABRIR CAIXA** (enviando: **Abrindo...**).
- Sucesso (toast): **Caixa aberto com sucesso**.
- Payload: `{ saldoDinheiroInicial, obs, delivery, presencial, satID }`.

---

## 3. Pagamento que cai no caixa

- O frontend NÃO grava direto; pagamento de venda → backend cria a operação no caixa aberto.
- Endpoint: `POST /datasnap/rest/venda2/pagamentoPago` (envia `caixaID: null`).
- Origem: PDV, Mesas/Comandas, Delivery (modal de pagamentos).
- Formas de pagamento (fechamento): Dinheiro, Cartão de Débito, Cartão de Crédito,
  Vale Alimentação, Vale Refeição, Crédito Loja, Outros, Carteira Digital, PIX Beetech, Fiado.
- Na listagem de operações do caixa: colunas **Data/Hora**, **Descrição**, **Valor**, **Tipo Pagamento**;
  subtexto **Venda #{numero}**; tooltip **Ver detalhes da venda**.

### Operações manuais (não são venda)
| Operação | Botão UI | API (`operacaoManual`) | Efeito |
|----------|----------|------------------------|--------|
| Sangria | **SANGRIA** | `operacao: "SANGRIA"` | Saída em dinheiro |
| Acréscimo (=suprimento) | **ACRÉSCIMO** | `operacao: "ACRESCIMO"` | Entrada em dinheiro |

> Na UI NÃO existe a palavra "Suprimento". Usar **ACRÉSCIMO**.

---

## 4. Consultar valor / saldo / movimentações

- Acesso: `/caixa` → **Ver Caixa** (lupa azul) → `src/components/CaixaVerModal.tsx`.
- Título: `Caixa #{n} - {titulo}` + badge `ABERTO`/`FECHADO` + **Delivery**/**Presencial**.

### Painel esquerdo — Operações
- Botões (caixa aberto): **SANGRIA**, **ACRÉSCIMO**, **TRANSFERIR** (c/ permissão), busca **Buscar...**.
- Tabela: Data/Hora | Descrição | Valor | Tipo Pagamento. Verde = entrada, vermelho = saída.

### Painel direito — Resumo e saldo
- Botão: **FECHAR CAIXA** (aberto) / **VER CONFERÊNCIA** (fechado).
- Seletor: **Resumo**, **Resumo Frete**, **Resumo Presencial**. Botão **Imprimir Resumo**.
- Seção **Resumo Dinheiro** (labels da API):
  - **SALDO INICIAL**, **ENTRADA MANUAL**, **SANGRIAS**, **VENDAS EM DINHEIRO**, **VALOR EM CAIXA**, **TOTAL**.
- Seção **Observações** (texto da abertura).

### Fechamento / conferência
- `src/components/CaixaFecharModal.tsx` — "Conferência de Valores - 1ª/2ª Conferência".
- Colunas: Forma de Pagamento | Entrada | Saída | Saldo | Conferência | Diferença.
- Totais: Total Entrada/Saída, Entrada Conferida, **Quebra de Caixa**, **Saldo Final**, **Saldo Final Conferido**.

---

## 5. Observações para o manual

1. Usar **ACRÉSCIMO** (não "Suprimento").
2. Pagamento entra automaticamente ao finalizar a venda; não há tela "lançar venda no caixa".
3. Caixa aberto é pré-requisito (erros: **Caixa já aberto**, **Caixa não encontrado ou não está aberto**).
4. Permissões controlam colunas financeiras e abas.
