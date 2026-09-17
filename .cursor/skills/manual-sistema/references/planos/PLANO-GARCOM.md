# Plano — manuais de garçom (comissão e taxa de serviço)

> Aprovado pelo dono em **06/09/2026**. Estudo em leitura no mesmo dia; produção
> na sequência, sem parar.
>
> Conta sandbox: **BeeFood3 - Manual** (`contato@beefood.com.br`).
> Próximos números: **#83, #84, #85**.

---

## 1. Recorte aprovado

Três manuais, um por pergunta. Taxa de serviço e comissão **não são o mesmo
dinheiro**.

| Nº | Manual | Pasta | Pergunta |
|----|--------|-------|----------|
| **#83** | Comissão do garçom: cadastrar e lançar | `manuais/comissao-garcom-cadastrar/` | Como o garçom passa a ganhar comissão em cada produto que lança? |
| **#84** | Relatório de comissão | `manuais/relatorio-comissao-garcom/` | Como fecho a comissão da equipe no fim do dia ou do mês? |
| **#85** | Relatório de taxa de serviço | `manuais/relatorio-taxa-servico/` | Como vejo a gorjeta (10%) por garçom — e como isso é diferente da comissão? |

Ordem: **#83 → #84 → #85**.

---

## 2. Decisões do dono (06/09/2026)

1. **Três manuais.** Os relatórios mostram **só dados que nós lançamos**. Filtro
   de data **hoje + amanhã** (06 e 07/09/2026), para isolar o cenário.
2. **Pode criar à vontade** (funcionário, usuário, vendas). **Não criar
   produto** — a base já tem cardápio de hamburgueria.
3. **Resumo presencial do caixa** entra nos dois relatórios, cada um no seu
   contexto (comissão no #84, taxa no #85).
4. Switch **Sem taxa de serviço** do produto entra **rápido** no #85.
5. Comissão **só existe** quando o item é lançado:
   - pelo **aplicativo do garçom**, ou
   - pelo **sistema com o usuário vinculado** ao funcionário garçom, ou
   - com o **código do operador** ligado (várias pessoas no mesmo computador).
   O código do operador **já tem manual** — só linkar, não ensinar:
   https://ajuda.beefood.com.br/parametros-codigo-operador
6. **Não existe** comissão no cadastro do produto. O % mora no **garçom**.

---

## 3. O que já existe e não se repete

| Manual | Uso aqui |
|--------|----------|
| **#40** App Garçom (parâmetros) | Só link. Sem print de celular. |
| **#41** Taxa e obrigatoriedades | A taxa 10% já está ligada. O #85 lê o resultado, não configura. |
| **#42** Código do operador | Link. Não ensinar. |
| **#76** Criar usuário | O campo **Funcionário** já foi ensinado. O #83 só usa. |
| **#75** Grupos de acesso | Os dois switches de Desempenho Presencial já estão no catálogo. |
| **#57** Entregador | Função diferente (diária / KM). |

Cadastro completo de funcionários (endereço, demissão) continua no backlog.

---

## 4. Cenário de prova (sandbox)

Dois garçons, percentuais diferentes, produtos que já existem:

| Garçom | Comissão | Produto lançado | Conta |
|--------|----------|-----------------|-------|
| **Ana Garçom** | 10% | Chicken Deluxe R$ 14,50 + Anéis de Cebola Empanada R$ 19,20 (sem taxa) | comissão R$ 3,37 |
| **Bruno Garçom** | 5% | Batata frita com cheddar e bacon R$ 19,90 | comissão R$ 0,99 |

Usuários vinculados (`ana.garcom` e `bruno.garcom`), grupo que já existe
(Administrador2 ou equivalente). Login **como o garçom** para lançar — é assim
que a comissão nasce no web, sem o app.

Vendas **presenciais** (Mesas → Novo Pedido), **recebidas em dinheiro**, com
taxa de serviço padrão do #41. Uma das vendas inclui um produto marcado
**Sem taxa de serviço** (prova rápida do #85).

Filtro dos relatórios: **Hoje** no fuso da loja (no sandbox o lançamento caiu em
05/09/2026 21:45 SP). Comissão total **R$ 4,36**. Taxa total **R$ 3,44**.

---

## 5. Manual por manual

### #83 — Comissão do garçom: cadastrar e lançar

Cadastros → Funcionários → Função Garçom → Comissão (%). Vincular o usuário.
Lançar o item logado como o garçom. Prova: a **linha do produto** no relatório
(uma imagem só; o resto do relatório é o #84).

Abrir dizendo os três jeitos de identificar o garçom (app / usuário ativo /
código do operador) e apontar o manual do operador.

### #84 — Relatório de comissão

Desempenho → Presencial → **Pedidos (Mobile e Comissão)**, data hoje+amanhã.
KPIs, Comissão por Garçom, grade item a item, filtro RECEBIDO, Excel.
Caixa → Resumo Presencial → **Comissão Garçom**.

### #85 — Relatório de taxa de serviço

Abre com **taxa ≠ comissão**. Desempenho → Presencial → **Taxa Serviço**.
KPIs, Taxa por Garçom, grade por venda, tipo % vs R$.
Produto **Sem taxa de serviço** (rápido).
Caixa → Resumo Presencial → **Taxa de Serviço** (só Gerente).

---

## 6. Fora de escopo

- Operar o aplicativo do garçom no celular.
- Cadastro completo de funcionários.
- Operação do mapa do salão (abrir/fechar mesa).
- Ensinar o código do operador (#42).

---

## 7. Produção (06/09/2026)

Concluído. Três pastas, 17 imagens no `.md`. Provas e armadilhas no
`CHECKLIST-MANUAIS.md` (histórico 06/09) e em cada `MEMORIA.md`.
