# Plano — manuais de Parâmetros (Configuração)

**Status:** estudo — aguardando aprovação do recorte  
**Rota:** `/parametros` — menu **Configuração → Parâmetros**  
**Permissão:** `parametros`  
**API:** `GET` / `POST` `/api/empresa2/empresaConfig`  
**Data:** 21/08/2026

Este arquivo é o mapa da tela **Parâmetros**. Não produz manual até o dono aprovar o recorte.

---

## 1. O que é esta tela

Uma página com **6 cards**. Cada switch (no desktop) **salva sozinho** ~500 ms depois do clique — não há botão Salvar. No celular o mesmo conjunto de campos existe em `MobileParametrosPage` **com** botão Salvar.

Não confundir com:

- **Configuração fiscal** (`/configuracao-fiscal`) — NFC-e, SAT, etc.
- **Parâmetros RFV** (`ModalRFVParametros`) — outra tela, outro assunto.
- **Área de Entrega** — já tem manuais #34–#38.

Código de referência (somente leitura):

- `~/refs/beefood-web-react/src/pages/Parametros.tsx`
- `~/refs/beefood-web-react/src/hooks/useEmpresaParametros.ts`
- `~/refs/beefood-web-react/src/components/mobile/parametros/MobileParametrosPage.tsx`
- `~/refs/beefood-web-react/src/utils/configCache.ts`

Vídeos oficiais já embutidos na rota (não repetir no manual; no máximo linkar):

- Código do Operador — `G5PH7VOlunw`
- Senha Gerente — `CeXewqyMX6w`

---

## 2. Inventário dos 6 cards

### 2.1 Solicitar Senha Gerente

| Campo na tela | Flag | Onde o código usa |
|---|---|---|
| Cancelar Operação Caixa | `geCai` | `CaixaVerModal` |
| Cancelar Pagamento | `gePag` | fluxo de pagamentos |
| Cancelar Venda | `geVen` | PDV / vendas |
| Cancelar Produto Lançado | `gePro` | item já lançado no PDV |
| Editar Estoque | `geEst` | `useAlterarEstoque` / modal de estoque |
| Aplicar Desconto | `geDesc` | `useDescontoGuard` |
| Desconto máximo (%) | `geDescMax` | só aparece se `geDesc` estiver ligado; `0` = sem limite |
| Testar Validação | — | abre `ModalValidarSenhaGerente` |

**Pegadinha:** se o usuário logado já é gerente, o modal **não abre** (atalho no código). Para provar o Testar, precisa de um usuário **não gerente** ou demonstrar o efeito no PDV/caixa/estoque.

### 2.2 Taxa de Serviço e Mesas (inclui App Garçom)

Sub-bloco **Aplicativo do Garçom** — o que o app pergunta ao abrir uma venda:

| Campo | Flag |
|---|---|
| Menu de Comanda | `appGarcomComanda` |
| Menu de Mesa | `appGarcomMesa` |
| Menu de Nome Avulso | `appGarcomNomeAvulso` |
| Menu de Cliente | `appGarcomCliente` |

**Não temos o app.** Nestes quatro campos o manual mostra **só a tela de configuração** e descreve o efeito em texto. Sem print do celular do garçom.

Sub-bloco **Parâmetros gerais Mesas/Comandas** (changelog: valem no **web e no app**):

| Campo | Flag | Observação |
|---|---|---|
| Taxa de Serviço Padrão | `taxaServicoPadrao` | liga o campo de % |
| Valor da Taxa (%) | `taxaServicoValor` | default 10 se vazio |
| Cliente obrigatório | `mesaClienteObrigatorio` | web + app |
| Comanda obrigatória | `appGarcomComandaObrigatoria` | web + app |
| Mesa obrigatória | `appGarcomMesaObrigatoria` | web + app |

Estes cinco **dá para provar no BeeFood web** (Mesas / PDV de mesa), sem o app.

### 2.3 Geral

| Campo | Flag | Observação |
|---|---|---|
| Motivo de cancelamento | `motivoCancelamento` | exige motivo ao cancelar |
| Código do Operador | `operadorPDV` | seleção de operador no PDV |
| Testar | — | `ModalValidarOperador` |

**Campo fantasma:** `operadorPDVObrigar` existe no tipo TypeScript, na API e no state do mobile — **não tem switch no desktop**. Não inventar na tela. Se o dono quiser, vira nota de “existe na API, sem UI”.

### 2.4 Delivery

| Campo | Flag | Efeito |
|---|---|---|
| Pagamento automático ao entregar | `deliveryPagamentoAuto` | ao marcar o pedido como entregue, registra o pagamento se já houver intenção de pagamento |

Prova no módulo Delivery, se houver pedido em condições de entregar.

### 2.5 Caixa — **já documentado**

| Campo | Flag | Verdade (não a descrição da tela) |
|---|---|---|
| Um caixa por usuário | `caixaPorUsuario` | **não** impede dois usuários no mesmo caixa. Quem faz “cada um vê o seu” é **Usuário Fixo** no cadastro de caixas. Este parâmetro atua no **Histórico de Vendas**. |

Manual existente: **#13** `caixa-restricoes.md`.

**Não reescrever.** No plano de produção, só um parágrafo “já coberto pelo #13” com link.

### 2.6 PDV

| Campo | Flag | Efeito |
|---|---|---|
| Exibir número do pedido | `pdvNumeroPedido` | mostra o número no PDV |
| Imprimir venda automaticamente | `pvdImprimirVendaSempre` | cupom ao finalizar (typo histórico no nome da flag) |
| Impressão de Fichas | `impressaoFicha` | liga o bloco Individual / Lista |
| Individual | `impressaoFichaIndividual` | XOR com Lista (`usePDVImpressaoFichas.ts`) |
| Lista | `impressaoFichaLista` | XOR com Individual |
| Ativar Balança | `balancaAtivada` | liga o bloco técnico |
| Tipo de leitura | `balancaTipoLeitura` | `0` Peso / `1` Valor |
| Dígitos do código / início / fim | `balancaDigitosCodigo`, `Inicio`, `Fim` | parser em `src/utils/balancaParser.ts` |
| Dígitos do preço / início / fim | idem preço | só faz sentido no tipo Valor |

Ajuda oficial da balança (não duplicar o artigo): `https://ajuda.beefood.com.br/baseconhecimento/balanca/`

Ao ligar **Impressão de Fichas**, se nenhum modo estiver on, o código força **Individual**.

---

## 3. Recorte proposto — 5 manuais novos

Um manual por assunto que o usuário **consegue ver ou provar** no sandbox. Caixa não entra. App Garçom não vira manual sozinho.

| # provável | Pasta | Card | O que fotografar | O que **não** fotografar |
|---|---|---|---|---|
| — | `senha-gerente` | Senha Gerente | os 6 switches, % de desconto, Testar (se der), e **um** efeito real (ex.: desconto no PDV ou editar estoque) | vídeo do YouTube embutido |
| — | `mesas-taxa-app-garcom` | Taxa e Mesas | card inteiro + prova da taxa / cliente obrigatório **nas Mesas web** | tela do aplicativo do garçom |
| — | `parametros-geral` | Geral | switches + Testar operador + cancelar com motivo no PDV | — |
| — | `delivery-pagamento-auto` | Delivery | switch + pedido entregue com pagamento registrado | — |
| — | `pdv-parametros` | PDV | número do pedido, imprimir auto, fichas (Individual/Lista), balança **só o bloco de config** | app de balança / impressora física se não tivermos |

Numeração oficial só depois que o dono aprovar (próximos livres a partir do **#39**, se #34–#38 já estiverem no `main`).

### 3.1 Por que não 6 ou 7

- **Balança sozinha:** faz sentido se o dono quiser um artigo técnico. Hoje já existe na base de conhecimento. Sugestão: um capítulo dentro de `pdv-parametros`, com link para a ajuda, **sem** fingir que pesamos produto.
- **Fichas sozinhas:** só muda impressão. Sem impressora no sandbox, vira só config — cabe no mesmo `pdv-parametros`.
- **App Garçom sozinho:** seriam 4 switches sem prova. Melhor um capítulo “o que estes menus controlam” **dentro** de `mesas-taxa-app-garcom`, só com o print da configuração.

### 3.2 Alternativa (se o dono preferir mais granulado)

1. Senha gerente  
2. App Garçom (**só config**)  
3. Taxa e obrigatoriedades de mesa/comanda (com prova web)  
4. Geral  
5. Delivery  
6. PDV operação (número + imprimir)  
7. PDV fichas  
8. PDV balança  

Mais arquivos, mesmo conteúdo. Só vale se cada um for usado em treinamento separado.

---

## 4. Regras de produção (quando aprovado)

1. **Um assunto = uma pasta** em `manuais/`, no padrão do `CHECKLIST-MANUAIS.md` (`.md`, `MEMORIA.md`, `fluxo-codigo.md`, `texto-documentation.ia.md`, `annotate.py`, imagens).
2. **App Garçom:** texto + print da configuração. Frase padrão: *“Este parâmetro vale no aplicativo do garçom, que não faz parte deste manual.”*
3. **Não mentir a descrição da tela.** `caixaPorUsuario` já ensinou isso no #13.
4. **Auto-save:** o texto deve dizer que no computador a alteração grava sozinha. Não pedir “clique em Salvar” no desktop.
5. **Restaurar o sandbox** no fim de cada manual (switches no estado em que o dono deixou, ou o default da empresa Manual).
6. **Usuário gerente:** para senha gerente e Testar, pode ser preciso um usuário sem perfil gerente. Se não existir, o manual mostra o switch + o efeito bloqueado/liberado, e declara a limitação.
7. **Balança e impressão:** sem hardware, não inventar cupom. Configuração + (se o PDV mostrar) o número do pedido na tela.
8. Playwright / tema / toasts: mesmas regras dos manuais de Área de Entrega (1440×900, tema claro, esconder `div.fixed.bottom-6`).
9. Prefixo de commit: `docs(#NN): ...` depois de numerar. Enquanto for só o plano: `docs: plano de manuais de Parametros`.

---

## 5. Ordem sugerida (depois da aprovação)

1. `senha-gerente` — mais switches, maior risco de texto errado  
2. `parametros-geral` — curto, prova no PDV  
3. `pdv-parametros` — o card mais denso  
4. `mesas-taxa-app-garcom` — precisa do módulo Mesas web  
5. `delivery-pagamento-auto` — depende de ter pedido entregável  

Caixa: só conferir se o #13 ainda aponta para esta tela. Se a descrição do card mudou, atualizar o #13 num commit à parte — não misturar.

---

## 6. Dependências e riscos

| Risco | O que fazer |
|---|---|
| Usuário da sandbox é gerente | Testar Senha Gerente não mostra modal; usar outro usuário ou só o efeito no PDV |
| Sem app do garçom | Config only — combinado com o dono |
| Sem balança / impressora | Config only + link da ajuda |
| `operadorPDVObrigar` sem UI | Não fotografar; nota no `fluxo-codigo.md` |
| Auto-save vs mobile | Manuais são do **painel web** (desktop), não do app mobile de parâmetros |
| Pedido delivery para provar pagamento auto | Pode faltar pedido no estado certo; nesse caso o manual fica config + texto do efeito |

---

## 7. O que este estudo **não** cobre

- Cada campo de **empresa** fora desta tela (logo, horários, NF, etc.)
- Parâmetros do **cardápio digital** (já no `PLANO-CARDAPIO.md`)
- Parâmetros **RFV**
- Traduzir o artigo da balança da base de conhecimento

---

## 8. Checklist de aprovação (dono)

Marque o recorte:

- [ ] **A — 5 manuais** (recomendado): senha gerente; mesas/taxa/app-garçom; geral; delivery; PDV (fichas + balança no mesmo)
- [ ] **B — 8 manuais** (granulado): lista da seção 3.2
- [ ] **C — outro recorte** (escreva na resposta)

Confirmações:

- [ ] App Garçom = **só tela de configuração**
- [ ] Caixa / `caixaPorUsuario` = **não repetir**; fica o #13
- [ ] Balança = capítulo no PDV, sem hardware
- [ ] Posso numerar a partir do próximo livre (#39 se #34–#38 já estiverem no `main`)
