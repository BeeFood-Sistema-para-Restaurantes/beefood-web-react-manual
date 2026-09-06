# MEMORIA.md — Comissão do garçom: cadastrar e lançar

Manual **#83**. Produzido em 06/09/2026 com os #84 e #85. Sandbox BeeFood3.

Última atualização: 06/09/2026.

## O que o manual afirma

| Afirmação | Prova |
|-----------|-------|
| O % mora no garçom, não no produto | Aba Função `#comissao`; mesmo produto, Ana 10% e Bruno 5% |
| Comissão só com identidade | Login `ana.garcom` / `bruno.garcom` com `funcionarioID`; relatório com % Mobile 0% e comissão preenchida |
| Código do operador não se ensina aqui | Link para https://ajuda.beefood.com.br/parametros-codigo-operador |
| Taxa ≠ comissão | Ana: comissão R$ 3,37 nos dois itens; taxa só R$ 1,45 (anel sem taxa) |

## Cenário

| Quem | Login | Comissão | Mesa | Itens |
|------|-------|----------|------|-------|
| Ana Garçom | `ana.garcom` / `manual123` | 10% | 16 | Chicken Deluxe R$ 14,50 + Anéis R$ 19,20 |
| Bruno Garçom | `bruno.garcom` / `manual123` | 5% | 17 | Batata frita com cheddar e bacon R$ 19,90 |

Usuários no grupo Administrador2, Aplicativos ligado. Código operador Ana 10, Bruno 11.
Anéis com **Sem taxa de serviço** (prova do #85).

Vendas **#939** (Ana) e **#940** (Bruno), recebidas em Dinheiro (a forma tem −1%).

## Armadilhas

- F2 no modal de **usuário** não salva — precisa clicar SALVAR.
- Cache `funcionarios_cache_v2` (30 min): depois de criar o garçom, limpar o cache antes
  de abrir o combo Funcionário em Usuários.
- `garcons_cache` nas Mesas: recarregar depois do cadastro.
- Clique em “Selecione uma mesa” sem `exact=True` acerta o empty state atrás do modal.
- Horário São Paulo vs UTC: o lançamento perto da meia-noite UTC cai no dia anterior
  no caixa (05/09 21:45 SP). Filtrar **Hoje** no fuso da loja.

## Imagens

8 no `.md` (01–07 e 09). `08-pedido-bruno.png` ficou nas puras como contexto: o combo
mostrou o ID `279483` em vez do nome (cache de garçons no login novo) — não publicar.
