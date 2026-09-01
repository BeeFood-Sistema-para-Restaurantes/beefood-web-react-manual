# Plano — manuais dos relatórios (Desempenho)

> Fila aprovada pelo dono em **01/09/2026**: **um manual por relatório**, produzidos
> **unitariamente**, conversando um por vez antes de cada um.
>
> **Regra do dono (01/09/2026, revisão): não usar o histórico.** Para cada relatório o cenário é
> **construído por nós** e o relatório é lido com o filtro em **hoje** (no máximo hoje + amanhã).
> O motivo apareceu no primeiro manual: o histórico do sandbox tem dado *tecnicamente* presente
> mas *didaticamente* ruim — no Taxa de Serviço, 34 dos 38 pedidos estavam sem garçom, todos com
> a mesma taxa de 10%, e com valores quebrados que o leitor não confere de cabeça. Com o cenário
> construído e o filtro no dia, os números da tela são exatamente os que o manual explica.
>
> Isso muda a coluna **Dado** das tabelas abaixo: ela passa a indicar se **existe base para
> construir** o cenário, não se o histórico serve. E acrescenta um passo ao checklist de cada
> manual: **desenhar e criar o cenário antes de capturar**.
>
> Primeiro da fila, em proposta: **#94 Taxa de Serviço** —
> [`PLANO-RELATORIO-TAXA-SERVICO.md`](PLANO-RELATORIO-TAXA-SERVICO.md).
>
> Este documento é o **checklist da fila**. Ele não é o manual de nenhum relatório: serve
> para saber quantos são, o que cada um precisa cobrir, quais têm dado para fotografar hoje
> e em que ordem atacar.

Fonte: `beefood-reports-hub` (GitHub, clonado em `~/refs/beefood-reports-hub`, somente
leitura). Levantamento e diagnóstico feitos em **01/09/2026**.

---

## 1. O essencial em oito linhas

São **25 telas de relatório**, não as ~15 que o README do repositório descreve — aquele README
está **desatualizado** (fala de `vendas-origem`, `vendas-setor` e `vendas-produto`, que não
existem mais com esses nomes, e não menciona Recebimento, Descontos, Cancelamentos, Entregador,
Taxa Serviço, RFV nem Base de Clientes). Das 25, **22 são documentáveis hoje** e **3 estão
bloqueadas** (seção 5). Nenhuma é *simples*: são 10 de complexidade média e 15 alta. O sandbox
tem dado de verdade em quase tudo — só **Sugestões (presencial)** vem vazio. A captura foi
testada e funciona, mas só por um caminho (seção 6). E há **rótulos repetidos** na tela que
obrigam a batizar os manuais com nomes diferentes dos rótulos (seção 4).

---

## 2. Onde esses relatórios vivem

O menu **Desempenho** do painel não tem tela própria: ele monta um **iframe** apontando para
`relatorios.beefood.com.br`, passando autenticação por parâmetro na URL
(`beefood-web-react/src/pages/Desempenho.tsx:36-42`). Tudo que o cliente vê ali é renderizado
pelo `beefood-reports-hub`.

```
Painel (beefood-web-react)          App de relatórios (beefood-reports-hub)      API
menu Desempenho  ──iframe──►  relatorios.beefood.com.br/relatorios  ──►  report.beetechapi.be
                                                                          /api/relatorio2/*
```

Consequências para os manuais:

- O **caminho na tela** é sempre **Desempenho → \<grupo\> → \<relatório\>**.
- Os **filtros globais** (período, cardápio/filial, hora início/fim) ficam numa barra própria do
  app de relatórios, acima do conteúdo, e valem para todos. **Isso é conteúdo repetido em 22
  manuais** — proposta na seção 7.
- A **visibilidade de cada relatório depende do grupo de acesso** do usuário
  (Configuração → Usuários → Grupos de Acesso). O manual precisa dizer isso, senão o cliente
  que não vê o item acha que o manual está errado.
- O app tem **cache de 5 minutos** por empresa + período + filial. Ao capturar, número que não
  muda pode ser cache, não erro.

---

## 3. A fila — 22 manuais

Ordem de execução proposta: **Vendas → Produtos → Clientes → Delivery → Presencial**. O critério
é reaproveitamento: os cinco de Produtos compartilham uma única chamada de API e o mesmo modal de
filtros, e os de Clientes conectam com os manuais de CRM já publicados.

Legenda de dado no sandbox: 🟢 abundante · 🟡 magro (print sai ralo) · 🔴 vazio.

### Bloco 1 — Vendas (6)

| Nº | Manual | Rótulo na tela | Pasta | Complex. | Dado |
|----|--------|----------------|-------|----------|------|
| 75 | **Resumo geral** | Resumo (raiz) | `relatorio-resumo-geral/` | Alta | 🟢 369 |
| 76 | **Vendas por origem** | Vendas → Origem | `relatorio-vendas-origem/` | Média | 🟢 369 |
| 77 | **Resumo de vendas** | Vendas → Resumo | `relatorio-resumo-vendas/` | Alta | 🟢 430 |
| 78 | **Recebimento** | Vendas → Recebimento | `relatorio-recebimento/` | Alta | 🟢 88 |
| 79 | **Descontos** | Vendas → Descontos | `relatorio-descontos/` | Média | 🟢 429 |
| 80 | **Cancelamentos** | Vendas → Cancelamentos | `relatorio-cancelamentos/` | Média | 🟢 429 |

### Bloco 2 — Produtos (5)

| Nº | Manual | Rótulo na tela | Pasta | Complex. | Dado |
|----|--------|----------------|-------|----------|------|
| 81 | **Produtos vendidos** | Produtos → Produtos | `relatorio-produtos-vendidos/` | Média | 🟢 1.262 |
| 82 | **Vendas por setor** | Produtos → Setor | `relatorio-produtos-setor/` | Média | 🟢 1.262 |
| 83 | **Produtos sem opções** | Produtos → Produtos sem opções | `relatorio-produtos-sem-opcoes/` | Média | 🟢 1.262 |
| 84 | **Produtos com opções** | Produtos → Produtos com opções | `relatorio-produtos-com-opcoes/` | Alta | 🟢 1.262 |
| 85 | **Grupo de opções** | Produtos → Grupo de Opções | `relatorio-grupo-opcoes/` | Média | 🟢 1.262 |

### Bloco 3 — Clientes (3)

| Nº | Manual | Rótulo na tela | Pasta | Complex. | Dado |
|----|--------|----------------|-------|----------|------|
| 86 | **Base de clientes** | Clientes → Base de Clientes | `relatorio-base-clientes/` | Alta | 🟢 301 |
| 87 | **Análise RFV** | Clientes → Análise RFV | `relatorio-analise-rfv/` | Alta | 🟢 params ok |
| 88 | **Análise de recorrência** | Clientes → Análise Recorrência | `relatorio-analise-recorrencia/` | Alta | 🟢 365 |

### Bloco 4 — Delivery (5)

| Nº | Manual | Rótulo na tela | Pasta | Complex. | Dado |
|----|--------|----------------|-------|----------|------|
| 89 | **Entregador (taxa e KM)** | Delivery → Entregador (Taxa / KM) | `relatorio-entregador/` | Alta | 🟢 118 |
| 90 | **Mapa de calor das entregas** | Delivery → Mapa de Calor | `relatorio-mapa-calor/` | Alta | 🟢 116 |
| 91 | **Oportunidades de delivery** | Delivery → Oportunidades | `relatorio-oportunidades/` | Média | 🟢 39 |
| 92 | **Top bairros** | Delivery → Top Bairros | `relatorio-top-bairros/` | Alta | 🟢 116 |
| 93 | **Sugestões do cardápio (delivery)** | Delivery → Sugestões | `relatorio-sugestoes-delivery/` | Média | 🟡 4 |

### Bloco 5 — Presencial (3)

| Nº | Manual | Rótulo na tela | Pasta | Complex. | Dado |
|----|--------|----------------|-------|----------|------|
| 94 | **Taxa de serviço** | Presencial → Taxa Serviço | `relatorio-taxa-servico/` | Alta | 🟡 → cenário próprio |
| 95 | **Pedidos no mobile e comissão** | Presencial → Pedidos (Mobile e Comissão) | `relatorio-pedidos-mobile/` | Média | 🟢 74 |
| 96 | **Sugestões do cardápio (presencial)** | Presencial → Sugestões | `relatorio-sugestoes-presencial/` | Média | 🔴 0 |

---

## 4. Rótulos repetidos — os manuais não podem usar o nome da tela

Três colisões. Se cada manual se chamar como o item do menu, a documentação fica com nomes
duplicados e o leitor não acha o que procura.

| Rótulo na tela | Quantos | Nome proposto para o manual |
|----------------|---------|-----------------------------|
| **Resumo** | 2 (raiz e Vendas → Resumo) | **Resumo geral** (#75) e **Resumo de vendas** (#77) |
| **Sugestões** | 2 (Delivery e Presencial) | **Sugestões do cardápio (delivery)** (#93) e **(presencial)** (#96) |
| **Acesso Cardápio Digital** | 2 (Delivery e Presencial) | bloqueados — seção 5 |

E um caso de nome pouco informativo: **Produtos → Produtos** virou **Produtos vendidos** (#81),
e **Produtos → Setor** virou **Vendas por setor** (#82), que é o que o relatório mostra.

> **Cuidado de redação:** o **Resumo geral** e o **Resumo de vendas** são relatórios
> completamente diferentes — o primeiro é um painel analítico com gráficos, o segundo é um
> fechamento de vendas com totais e lista. Cada manual precisa começar dizendo qual é qual e
> apontar para o outro, ou o suporte vai receber a confusão.

---

## 5. Os 3 bloqueados — e por quê

| Relatório | Situação | Evidência |
|-----------|----------|-----------|
| **Itens Vendidos** | ❌ **Não existe em produção.** Fora de escopo até publicar | Endpoint `relatorioItensVendidos` devolve **404**, testado em dois períodos (1 e 2 meses). Também **não tem item no menu lateral** — só abre por URL |
| **Acesso Cardápio Digital (Delivery)** | ❌ **Oculto em produção por código** | Checagem `isProduction` em `src/lib/accessControl.ts:67-71` esconde o item. A API responde (94 registros), mas o cliente não vê a tela |
| **Acesso Cardápio Digital (Presencial)** | ❌ mesma coisa | idem |

Os dois "Acesso Cardápio Digital" são os relatórios de **funil do cardápio digital** (visitas
únicas → adicionado ao carrinho → pedidos finalizados), com dispositivos e origens de tráfego.
São bons relatórios e valem manual **no dia em que forem liberados** — vale avisar quando isso
acontecer.

> Existe um `docs/relatorio-itens-vendidos.md` no repositório documentando o Itens Vendidos com
> bastante detalhe. Ele **adianta um manual futuro**, mas hoje descreve tela que a API não serve.

---

## 6. Captura — o que foi testado (01/09/2026)

Testei os dois caminhos possíveis. **Só um funciona**, e o plano depende disso:

| Caminho | Resultado |
|---------|-----------|
| **A) Entrar em `beefood.app/desempenho` e trabalhar dentro do iframe** | ✅ **Funciona.** O iframe carrega `relatorios.beefood.com.br/relatorios?auth=...`, e o Playwright lê e clica dentro dele normalmente. Print sai com o painel e o relatório juntos, que é o que o cliente vê |
| **B) Montar a URL direta com o `bearer`** | ❌ **Falha.** Redireciona para `beefood.app`. O `?auth=` que o painel envia é um token **criptografado** (formato `U2FsdGVkX1...`), diferente do bearer da API — não dá para reconstruir do lado de fora |

Prova do caminho A: capturei o **Resumo geral** com dado real — *Valor Total* **R$ 5.967,43**
(+11,7% vs período anterior), *Ticket Médio* **R$ 44,87**, gráfico *Vendas por período* e o bloco
*Vendas por Origem* (Delivery R$ 2.283,27 em 48 vendas; Mesas R$ 1.823,47 em 6 vendas).

**Detalhes de captura a resolver no primeiro manual (#75):**

- **O widget flutuante do WhatsApp aparece dentro do iframe** (canto inferior esquerdo). O
  `add_style_tag` da página principal **não alcança** o iframe — precisa injetar o CSS no
  **frame**, não na página.
- Os relatórios são **altos**: quase todos passam de uma tela. Vai ser preciso decidir por
  relatório entre print da área visível, recorte por bloco, ou print de página inteira.
- **Cache de 5 minutos**: ao trocar período para capturar, esperar ou usar o botão ↻ dos
  relatórios que têm.
- Vários relatórios têm **abas internas** (Resumo/Vendas, Resumo/Dados, Agrupado/Sem opções) —
  cada aba é uma captura.

---

## 7. Decisão de estrutura que vale para os 22

Os **filtros globais** (período com 15 presets, seletor de cardápio/filial, hora início/fim) e o
aviso sobre **grupo de acesso** e **cache** são idênticos em todos os relatórios. Repetir isso 22
vezes engorda cada manual e envelhece mal.

**Proposta:** um manual **#0 do bloco** — *"Relatórios: os filtros e o que vale para todos"* —
que explica a barra de filtros, os presets de período, o seletor de cardápio, o horário, o
comparativo de período, o cache e a permissão. Os 22 manuais então abrem com uma linha
("os filtros são os mesmos de todos os relatórios — veja *Relatórios: os filtros*") e vão direto
ao que é próprio deles.

Isso adiciona **1 manual** e enxuga os outros 22. **Precisa da sua aprovação** — se preferir cada
manual autossuficiente, repito os filtros em todos, e cada um fica uns 30% maior.

---

## 8. O que cada manual precisa cobrir (roteiro padrão)

Para não reinventar a estrutura 22 vezes:

1. **Para que serve** — a pergunta de negócio que o relatório responde, em duas linhas.
2. **Onde fica** — Desempenho → grupo → relatório.
3. **Não confunda com** — o relatório vizinho parecido (crítico nos dois Resumo e nos Produtos).
4. **Os filtros próprios** — só os que este relatório tem além dos globais.
5. **Lendo o relatório** — cada bloco/coluna, com o nome literal do cabeçalho e o que significa.
6. **As contas** — quando houver métrica derivada (ticket médio, margem, % do total, faturado
   × realizado, comissão). É aqui que o cliente mais erra.
7. **Exportar e imprimir** — Excel, A4, cupom 80 mm, conforme o relatório.
8. **Perguntas frequentes** — incluindo "por que está vazio" e "por que o número não bate".

---

## 9. Armadilhas por relatório, já mapeadas

Levantadas na leitura do código; vão poupar tempo na produção de cada um.

| Relatório | Armadilha |
|-----------|-----------|
| **Resumo geral** (#75) | Comparativo dispara **depois** da chamada principal: o print cedo sai sem as variações |
| **Resumo de vendas** (#77) | Duas abas (**Resumo** / **Vendas**) e seis agrupamentos; imprime A4 **e** cupom |
| **Recebimento** (#78) | **Quatro eixos de data** (venda, vencimento, previsto, recebido) que mudam o resultado inteiro; e o conceito **faturado × realizado**, que é o mesmo do manual #65 |
| **Produtos** (#81–#85) | Os cinco submenus **compartilham uma chamada** de API e o mesmo modal de filtros; trocar filtro em um afeta os outros |
| **Produtos com opções** (#84) | Hierarquia **produto → grupo → opção** expansível, e tem **tutorial embutido** na tela |
| **Base de clientes** (#86) | **Não usa o filtro de período** — é um retrato do cadastro. Vai gerar dúvida |
| **Análise RFV** (#87) | Depende de **parâmetros configuráveis** por empresa (faixas R, F e V); os 11 segmentos têm nome próprio |
| **Entregador** (#89) | **Colunas dinâmicas** conforme a configuração de taxa (3 modos, ida/volta) e **cupom configurável** em modal próprio |
| **Mapa de calor** (#90) | Depende da **chave do Google Maps** e de endereço geolocalizado; entrega sem coordenada fica fora do mapa e vai para uma aba separada do Excel |
| **Top bairros** (#92) | Tem **insights automáticos** dos 3 primeiros e Excel de 2 abas |
| **Taxa de serviço** (#94) | Vários **agrupamentos** (garçom, mesa, comanda, pagamento) que trocam as colunas |
| **Sugestões presencial** (#96) | **Sem dado** no sandbox: precisa de cenário montado antes |

---

## 10. Checklist de execução (por manual)

Repetir para cada um dos 22, um por vez, com conversa antes de começar:

- [ ] Confirmar com o dono qual é o próximo
- [ ] Ler o componente e os hooks do relatório no `beefood-reports-hub`
- [ ] **Desenhar o cenário** (quais registros criar, com valores que o leitor confira de cabeça) e **aprovar com o dono**
- [ ] **Criar o cenário** no sandbox e conferir pela API que gravou como esperado
- [ ] Ler o relatório com o filtro em **hoje** e confirmar que só o cenário aparece
- [ ] Criar `manuais/relatorio-<slug>/` com as subpastas do padrão
- [ ] Capturar por **Desempenho → grupo → relatório**, escondendo o widget do WhatsApp **dentro do frame**
- [ ] Cobrir dado pessoal de cliente **na imagem pura** (vários relatórios listam nome, telefone e endereço)
- [ ] Tratar as imagens no `annotate.py` e conferir uma a uma em tamanho real
- [ ] Escrever o `.md` no roteiro da seção 8
- [ ] `fluxo-codigo.md`, `MEMORIA.md` e `texto-documentation.ia.md`
- [ ] `python validar-imagens.py <pasta>`
- [ ] Commit + push + PR, e registrar no `CHECKLIST-MANUAIS.md`

> **Atenção especial ao dado pessoal neste bloco.** Diferente dos manuais anteriores, aqui
> vários relatórios **listam clientes**: Oportunidades traz nome, endereço, bairro e **telefone**;
> Base de Clientes e RFV são o cadastro inteiro; Resumo de vendas, Descontos e Cancelamentos têm
> coluna Cliente. O repositório é público — borrão na **pura** antes do primeiro commit, sem
> exceção.

---

## 11. Perguntas abertas

1. **Entra o manual dos filtros comuns** (seção 7)? Muda o tamanho dos outros 22.
2. **Começamos pelo #75 (Resumo geral)?** É o relatório que todo cliente abre primeiro, e por
   isso o lugar natural de começar — mas é de complexidade alta (seis blocos analíticos). Se
   preferir firmar o padrão num relatório menor antes, o **#79 Descontos** ou o **#91
   Oportunidades** servem bem de piloto.
3. **Montar cenário para os 🟡 e 🔴** (#93, #94, #96) quando chegar a vez deles, ou publicar com o
   dado magro que existe?
4. **Avisar quando os dois "Acesso Cardápio Digital" saírem do bloqueio de produção?**
