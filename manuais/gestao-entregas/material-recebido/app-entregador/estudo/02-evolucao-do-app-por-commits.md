# Evolução do app, lida no histórico de commits

245 commits, de 24/08/2024 a 17/09/2026 (`git log --date=short`). O que interessa aqui não é a
cronologia por si: é **quais funcionalidades são novas o bastante para nunca terem sido
explicadas a ninguém** — e essas são justamente as que o manual precisa cobrir com mais cuidado.

A conclusão em uma linha: **mais da metade do que o app faz hoje entrou depois de 30/08/2026.**

---

## 1. As sete fases

### Fase 1 — Nascimento, ago–out/2024

Scanner de código de barras com `expo-camera`, navegação em gaveta e pilha, keystore, primeiros
builds de iOS e Android. Muito commit de configuração de build (`pre build`, `podfile`,
`downgrade RN`) — a fase em que o app ainda estava se estabilizando como projeto.

Marcos: `f5d569d add barcode scan with expo`, `9925282 Modal Entregas -> Detalhes: deixar full
screen`.

### Fase 2 — Operação de rua, nov–dez/2024

Aqui o app deixa de ser lista e passa a ajudar quem está na moto:

| Commit | O que entrou |
|---|---|
| `1522b84` | **melhor rota** pelo Google Maps |
| `4cab313` | **destaque da observação da venda e do complemento do endereço** — a pílula vermelha que os detalhes ainda usam |
| `6eea8ea` … `23a9252` | **confirmação de entrega do iFood por WebView**, com teclado numérico injetado e ajuste de botões |
| `da4239e` | notificação de código de barras no iOS |

O manual 09 (iFood) documenta um fluxo de **dezembro de 2024** — o mais antigo do conjunto, e o
único que já rodou muito em campo.

### Fase 3 — Marketplaces e manutenção, jul–nov/2025

`31459f8` troca o `expo-barcode-scanner` pelo `expo-camera` e sobe para Android 35.
`5839c5b`/`87bbb8e`/`296a7c5` trazem **99Food e as opções de produto**; `dbcd2c9` conserta o
troco positivo; `05fe7da` arruma a ordenação do histórico; `931ae8d` recupera compatibilidade com
aparelho antigo.

O 99Food (manual 10) nasce aqui, quase um ano depois do iFood, e reusa a mesma WebView.

### Fase 4 — Marketplaces novos e abas, mar–abr/2026

`f16b469 Keeta` (só etiqueta, sem confirmação), `d476129`/`b58b912` **mensagens de WhatsApp**,
`fe69126` histórico apontando para API nova, `67772a7 add bottom tab component` — a barra de
abas que o app usa hoje —, `17ee70c` delimita a área de leitura do código de barras por CSS, e
`b3a60f4` passa a considerar latitude e longitude do marketplace quando existem.

### Fase 5 — GPS de verdade, mai/2026

`cae7aed add background task`, `216f852`, `7df908c`: a captura e o envio de posição migram para
dentro da callback do `TaskManager`, e nasce a tela de permissões (`b567b2f`). É a mudança que
faz o rastreamento sobreviver ao app minimizado no iPhone.

### Fase 6 — Gestão de Entregas 2.0 no app, 30/08/2026

Um commit único e enorme (`3c54335 gestão entregas`, seguido de `05f78d0`) que traz:

- **grupos de rota** na lista, com cabeçalho, `X de N entregues` e **INICIAR ROTA**;
- **presença de três estados** (online, pausa, offline) na barra superior;
- o padrão de **folha que sobe de baixo** aplicado a disponibilidade, mapas e finalizar;
- **um botão de ação por linha, largura cheia**, com FINALIZAR acima de CANCELAR;
- remoção do deep linking herdado do app da cozinha.

### Fase 7 — Pagamento na rua, 11 a 17/09/2026

A fase mais densa do repositório: **33 commits em sete dias**, e é o assunto dos manuais 11, 12 e
13.

| Data | O que entrou |
|---|---|
| 11/09 | SVG das bandeiras, cache de formas de pagamento, tela de cobrança, `AcoesEntrega`, **FINALIZAR SEM COBRAR**, confirmar sair, botões pílula, animação da folha |
| 14/09 | **troco por pessoa**, folha **Troco para**, **ConfirmarCobranca** antes do POST, ajuste de teclado no iOS, safe area dos rodapés, guia de estilo (`STYLE.md`) |
| 15/09 | **histórico e itens do pedido pela API 3.0**, produtos sob demanda, **confirmação de produtos em destaque**, rodapés claros nas telas de resultado, espaçamento compacto |
| 17/09 | endereço fixo no topo dos detalhes com as observações da venda, push que **recarrega a lista de entregas** ao ser tocado |

---

## 2. O que isso significa para o manual

| Fluxo | Idade | Consequência para o manual |
|---|---|---|
| Código de barras | 2024, muito rodado | documentar o comportamento estável; risco baixo de surpresa |
| iFood | dez/2024 | idem, mas o site do parceiro pode ter mudado — conferir na captura |
| 99Food | set–nov/2025 | idem |
| Melhor rota | dez/2024 | atenção: passou a valer **só para os avulsos** em 30/08 |
| Presença | 30/08/2026 | novo; ninguém explicou a diferença entre pausa e offline ainda |
| Rota e INICIAR ROTA | 30/08/2026 | novo; e é o único fluxo que depende do que o restaurante fez antes |
| Cobrança e divisão de conta | 11–14/09/2026 | **o mais novo e o mais complexo**; nunca rodou em campo (a documentação do servidor registra que as escritas de pagamento nunca foram executadas) |
| Produtos em destaque | 15/09/2026 | novo; a confirmação obrigatória surpreende quem não sabe por que ela aparece |
| Push | 15–17/09/2026 | novo |

Duas implicações práticas:

1. **O manual de cobrança é o primeiro documento que vai exercitar o fluxo de pagamento de ponta
   a ponta.** A documentação do servidor diz, com todas as letras, que as três escritas de
   pagamento nunca foram executadas nem uma vez. Produzir esse manual é, na prática, o primeiro
   teste real do fluxo — e é por isso que ele está na onda 5 do plano, depois de os fluxos
   estáveis estarem documentados, e não na primeira.
2. **Se um print revelar bug, é esperado, não excepcional.** O acordo que proponho: o achado vira
   linha num apêndice, com o print, e o manual descreve o comportamento correto. Corrigir código
   é outra conversa, e só se você pedir.
