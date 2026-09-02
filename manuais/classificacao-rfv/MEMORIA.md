# MEMÓRIA — Manual de Classificação RFV

> Memória detalhada deste manual. Ver também: `../../MEMORIA-GERAL.md`.

Status: ✅ **Concluído** em 2026-09-02 — 7 imagens, `classificacao-rfv.md`,
`fluxo-codigo.md` e `texto-documentation.ia.md`.

---

## 1. Escopo

O dono pediu o manual depois do estudo. Correção dele no meio do caminho:

- Campanha inteligente **também** usa segmentação, e a segmentação **usa RFV**.
  Isso faltava no primeiro estudo (parecia que a inteligente lia RFV direto).
- Campanhas e Segmentação neste manual são **básicos**. Já existem o #14 e o #16.

Núcleo: o que é R/F/V, os 11 grupos, como editar os limites, prazo de 24h,
classificação não se atribui na mão. Um parágrafo + 1 print para segmentação e
outro para campanha inteligente, com ponte para os manuais prontos.

Cadastro de cliente, Excel e duplicados **ficam de fora** (continuam ideia no
backlog de Clientes).

---

## 2. A cadeia correta

```
Parâmetros RFV (Clientes → RFV)
  → recálculo diário grava grupo + notas no cliente
  → Segmentação (#14) filtra por classificação / R / F / V
  → Campanha inteligente (#16) com origem SEGMENTACAO avalia esse público
  → WhatsApp em massa (#15) e SMS (#18) também podem chegar no RFV
     (massa: direto ou via segmentação; SMS: via segmentação)
```

As quatro inteligentes de público (Recuperador, Cashback parado, Aniversário,
Boas-vindas) nascem com público **fixo** da BeeFood — sumidos / cashback /
aniversário / novos. **Não** são filtro de classificação RFV. O elo que o
usuário precisa entender: a inteligente lê a **segmentação**; se essa
segmentação filtrar RFV (ou se ele trocar o público por uma que filtre), a
campanha passa a falar com o grupo.

Carrinho abandonado e “Recebeu cardápio e não pediu” são por evento.

---

## 3. Decisões de produção

- 7 imagens, desktop 1440×900 DPR 1.5, tema claro, widget escondido, spinner + 5 s.
- Relatório Análise RFV só em texto (não inflar).
- Ajuda dos 11 grupos não coube inteira no modal (rola). A tabela do `.md` é a
  lista completa; a foto mostra o formato do card.
- Nome e telefone cobertos **na pura** (02 e 05) — repo público. Cliente da
  ficha: João Muraro, usado só como prova das notas (R4 F5 V2 = Fiéis).
- Nada foi salvo no sandbox: parâmetros só abertos; editor da inteligente saiu
  por ESC; “Nova segmentação” não gravou.

## 4. Achados que o texto precisa acertar

- **V = ticket médio** na modal de parâmetros. A ficha rotula o círculo de
  “Total gasto”, mas a nota do João (ticket 34,89 → 2; total 1.919 → seria 5)
  segue o ticket. O manual avisa.
- 11 grupos, dois nomes para o mesmo quadrado (Em potenciais / Potenciais fiéis).
- Sem botão recalcular. Sem janela de tempo da Frequência na UI (só quantidade
  de pedidos). A copy da modal fala em “período específico”, mas o campo não
  existe — o manual **não** repete essa frase.
- Chips somem quando o grupo está vazio. O padrão ao vivo do sandbox (2026-09-02)
  está no `fluxo-codigo.md`.

## 5. O que não fazer da próxima vez

- Não recontar o #14 nem o #16. Uma foto cada + o diagrama da cadeia.
- Não prometer o SQL do job de 24h (procedure fora do front).
- Não abrir a ficha do primeiro da lista sem chip: a primeira página é gente
  sem pedido e os círculos RFV vêm vazios.
