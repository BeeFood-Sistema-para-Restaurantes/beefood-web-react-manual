# Prompt para publicar o manual — Horário de atendimento (#32)

> Cole o texto abaixo na IA de documentação do app, junto com as 20 imagens da pasta
> `imagens-tratadas/`, na ordem da tabela do fim.

---

## Instrução

Publique um manual de usuário final chamado **"Horário de atendimento"**, na seção
**Cardápio Digital**. Use o conteúdo de `manuais/horario-atendimento/horario-atendimento.md` como
fonte, **sem reescrever o texto** — ele já está no padrão dos outros manuais publicados.

Este manual é **par** do **"Fechar a loja fora do horário"** (#33): um trata da grade semanal, o
outro de fechar fora dela. Os dois se referenciam, então publique os dois juntos ou este
primeiro.

### Estrutura a preservar

1. As duas coisas para saber antes (duas grades separadas; não existe botão de salvar)
2. Onde fica (as duas visões e o Assistente)
3. Parte 1 — Começar do zero (reset), com o alerta de que o reset é global
4. Parte 2 — Montar a semana com o Assistente (3 passos)
5. Parte 3 — Conferir o resultado
6. Parte 4 — Ajustar um dia na mão
7. Parte 5 — Fechar um dia
8. Parte 6 — Quem fecha depois da meia-noite
9. Parte 7 — O que o sistema recusa
10. Parte 8 — Não esqueça a grade Presencial
11. Resumo do caminho
12. Perguntas frequentes
13. Manuais relacionados

### Pontos que NÃO podem se perder

- **Delivery e Presencial são grades separadas.** Configurar uma não configura a outra — é o erro
  mais comum da tela.
- **Não existe botão de salvar**: a tela grava sozinha e avisa *Salvo automaticamente*.
- ⚠️ **O Resetar horários apaga as duas grades**, não só a da sub-aba onde você está. Confirmado
  na prática: reset no Delivery deixou o Presencial todo fechado. O Assistente, por contraste,
  substitui só a grade atual.
- **Virada de meia-noite**: digitar 18:00 → 02:00 faz o sistema **dividir o turno**
  automaticamente (até 23:59 no dia e 00:00 → 02:00 no dia seguinte), com o aviso
  *"Turno dividido: …"*. Consequência a destacar: o dia seguinte ganha um turno de madrugada,
  mesmo que estivesse fechado.
- **Não existe copiar um dia para outro.** O botão clonar duplica turno **no mesmo dia**; para
  repetir em vários dias, só o Assistente.
- **Tempo de entrega e de retirada ficam nesta tela**, por dia da semana — e **não existem** na
  sub-aba Presencial.
- **Duas recusas**: início igual ao fim (*"Nenhum horário válido para salvar…"*) e sobreposição no
  mesmo dia (*"Horários não podem se sobrepor no mesmo dia."*). Para abrir o dia inteiro, usar
  00:00 às 23:59 — nunca 00:00 às 00:00.
- **A grade é por cardápio/filial.**

### Os quatro modelos prontos do Assistente (não alterar)

| Modelo | Horário |
|--------|---------|
| Restaurante (Almoço + Jantar) | 11:00–15:00 e 18:00–23:00 |
| Lanchonete / Pizzaria (só noite) | 18:00–23:59 |
| Padaria / Café (manhã) | 06:00–14:00 |
| Comercial | 09:00–18:00 |

---

## Imagens, na ordem

Todas em `manuais/horario-atendimento/imagens-tratadas/`.

| # | Arquivo | Tipo | Legenda / o que mostra |
|---|---------|------|------------------------|
| 1 | `01-timeline-antes.png` | setas | A tela na visão Timeline · 1 sub-abas Delivery/Presencial · 2 Timeline/Lista · 3 Assistente |
| 2 | `02-lista-antes.png` | contexto | A mesma grade desorganizada na visão Lista |
| 3 | `03-presencial-antes.png` | contexto | A grade Presencial, independente da de Delivery |
| 4 | `04-menu-resetar.png` | setas | Menu de três pontos · 1 Resetar horários |
| 5 | `05-reset-confirmacao.png` | setas | Aviso do reset · 1 OK! (ENTER) |
| 6 | `06-apos-reset.png` | setas | Grade zerada · 1 todos os dias fechados |
| 7 | `07-assistente-aviso.png` | setas | Aviso de que o Assistente substitui tudo · 1 OK! (ENTER) |
| 8 | `08-assistente-passo1.png` | setas | Passo 1 · 1 dias da semana · 2 atalhos · 3 Avançar |
| 9 | `09-assistente-passo2.png` | setas | Passo 2 · 1 modelos prontos · 2 abertura/fechamento · 3 segundo turno · 4 tempos de entrega e retirada |
| 10 | `10-assistente-passo3.png` | setas | Passo 3 · 1 a semana · 2 os tempos · 3 Aplicar |
| 11 | `11-timeline-depois.png` | setas | Resultado · 1 bloco do almoço · 2 bloco do jantar · 3 Domingo Fechada |
| 12 | `12-lista-dois-turnos.png` | setas | Lista · 1 primeiro turno · 2 segundo turno · 3 remover o segundo · 4 tempos por dia |
| 13 | `13-resumo-desempenho.png` | setas | 1 resumo de horas da semana |
| 14 | `14-popover-bloco.png` | setas | Popover do bloco · 1 Início e Fim · 2 Entrega e Retirada · 3 Aplicar |
| 15 | `16-dia-fechado.png` | setas | 1 switch desligado = Fechado · 2 o turno 00:00–02:00 no domingo |
| 16 | `15-meia-noite-toast.png` | setas | **A prova do split** · 1 aviso "Turno dividido" · 2 o campo virou 23:59 |
| 17 | `17-validacao-igual.png` | setas | 1 mensagem de erro · 2 campo com início igual ao fim |
| 18 | `18-presencial-fechado.png` | contexto | Presencial fechado depois do reset |
| 19 | `19-presencial-passo2.png` | setas | Assistente no Presencial · 1 o título confirma o canal · 2 aqui não há tempo de entrega |
| 20 | `20-presencial-configurado.png` | setas | 1 grade Presencial montada |

> As imagens 15 e 16 aparecem fora da ordem numérica do arquivo: a `16-dia-fechado.png` entra
> antes da `15-meia-noite-toast.png` porque ela também mostra o resultado do split no domingo, e
> o texto a usa na Parte 5. Publique na ordem da tabela.

---

## Observações para quem publica

- Manual **somente desktop** (existe versão mobile da tela, sem a Timeline).
- Nenhum dado de cliente nas capturas.
- As capturas foram feitas com o navegador em português para os campos de hora saírem em **24h**.
  Se alguém recapturar, precisa do mesmo cuidado — o padrão sai em AM/PM.
- Se numa versão futura o **reset** passar a respeitar a sub-aba, o alerta da Parte 1 precisa de
  ajuste.
