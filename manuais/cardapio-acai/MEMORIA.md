# MEMÓRIA — Manual #30 Cardápio: açaí

> Memória detalhada deste manual: decisões, cenário montado, descobertas e estado do ambiente.

Última atualização: 2026-08-20 (manual concluído, aguardando publicação do dono)

---

## 1. Escopo

Quarto manual do bloco de cardápio. Dois assuntos novos:

1. **O padrão "N inclusos + extras pagos"** — a regra comercial da açaiteria, que o BeeFood não
   tem como campo e se resolve com **dois grupos**.
2. **Tamanhos** — um produto por tamanho, com os **mesmos grupos compartilhados** entre eles.

Sete partes: complementos → grupo Brinde com limite → grupo Normal dos extras → cobertura
compartilhada → um produto por tamanho → vínculo → PDV.

**Fora do escopo:** açaí por peso (usa balança, outro assunto), copo vs tigela, rodízio.

---

## 2. A descoberta central

**Não existe "os 3 primeiros grátis".** O grupo limita **quantidade**, nunca valor — procurado no
modal do grupo, no hook de detalhes e no cálculo do PDV. A tradução da regra é a dupla de grupos:

| Grupo | Formação | Máx | Efeito |
|-------|----------|-----|--------|
| Acompanhamentos inclusos | **Brinde** | 3 | até 3, nada soma |
| Acompanhamentos extras | **Normal** | 5 | cada um soma |

O que cria a sensação de "3 inclusos" é o **máximo do primeiro grupo**, que trava a quarta
seleção. Confirmado no PDV: com três marcados, o checkbox do quarto voltou
`unchecked (bloqueado)`.

**Detalhe que diferencia do Obrigatório:** o limite **não** emite mensagem — o controle
simplesmente não responde. O Obrigatório, sim, mostra toast (ver #28). Vale explicar isso ao
usuário, porque a ausência de aviso pode parecer defeito.

---

## 3. Cenário montado no sandbox

Base **limpa pelo dono** em 20/08/2026, confirmado pela API antes de começar.

| Item | Valor |
|------|-------|
| Setor | **Açaí** |
| Inclusos | Granola · Banana · Leite em pó · Paçoca — **R$ 0,00**, com foto |
| Extras | Morango R$ 3,00 · Creme de avelã R$ 6,00 · Leite condensado R$ 2,00 |
| Coberturas | Calda de chocolate R$ 2,00 · Calda de morango R$ 2,00 |
| Grupos | Acompanhamentos inclusos (Brinde, 0/3) · Acompanhamentos extras (Normal, 0/5) · Cobertura (Normal, 0/1) |
| Produtos | **Açaí 300 ml** R$ 18,00 · **Açaí 500 ml** R$ 22,00 · **Açaí 700 ml** R$ 26,00 — os três com os três grupos |

**Conta conferida no PDV:** R$ 22,00 → com 3 inclusos segue **R$ 22,00** → com Creme de avelã e
Morango vai a **R$ 31,00** → com a calda fecha em **R$ 33,00**.

**Estado em que o ambiente ficou:** cenário completo, com um Açaí 500 ml de R$ 33,00 no carrinho
do PDV (não finalizado).

### Fotos

10 imagens geradas: 9 complementos e 1 açaí, usada nos três tamanhos. Deliberadamente **a mesma
foto nos três produtos** — é o mesmo item em volumes diferentes, e o manual diz isso.

---

## 4. Erro de automação que vale registrar

O grupo **Cobertura** ficou com **uma só opção** na primeira rodada, embora o log tenha
registrado as duas como marcadas.

**Causa:** a função marcava os checkboxes por **índice**, calculado **antes** dos cliques. No
modal *Buscar e Cadastrar Opções* a lista se reorganiza ao marcar itens, então o segundo clique
caiu em outro elemento e desmarcou o primeiro. Nos grupos maiores o efeito não apareceu; no de
duas opções, sim.

**Correção:** marcar por **texto**, reconsultando a lista a cada clique — a função
`marcar_por_texto` de `p30d_fix_cobertura.py`. É o jeito certo para os próximos manuais.

**Como foi pego:** o modal do PDV mostrou o grupo Cobertura com uma única calda. Vale a regra
geral: **antes de capturar, conferir no PDV se todas as opções estão lá.** A tela de venda é o
melhor teste do cadastro.

---

## 5. Detalhes de layout que afetam capturas

**A faixa amarela de grupo compartilhado empurra o conteúdo do modal ~0,07 para baixo.** No
grupo Cobertura (vinculado aos três tamanhos), isso foi suficiente para os campos **Mínimo** e
**Máximo** saírem da área visível da captura. Por isso:

- a imagem 06 tem coordenadas próprias no `annotate.py`;
- as setas dela apontam para o aviso e para a formação, não para a Quantidade;
- o texto usa a regra que aparece no PDV (*Escolha 0 a 1*) para explicar o limite.

**Setas em tabela de três linhas:** apontar para a **primeira** linha vindo de baixo faz a seta
atravessar as outras duas — na imagem 08 ela cobria a palavra *Brinde*. Corrigido apontando para
a **última** linha. Vale para qualquer listagem com mais de duas linhas.

---

## 6. Marcação das imagens

15 imagens, **30 setas** em 14 delas. Uma de contexto (`passthrough`): o cardápio com os três
tamanhos.

Os dois grupos de acompanhamento aparecem **em par** (detalhes e opções, lado a lado no manual)
com as setas nas mesmas posições, para o leitor ver que a diferença está só na formação e no
preço.

Conferência automática (`annotate.py` × `.md`): **15 imagens, 0 divergência**.

---

## 7. O que o #31 herda daqui

| Item | Detalhe |
|------|---------|
| Limite de grupo | Trava o checkbox **sem mensagem**; contador fica `N/N` |
| Dois grupos para "N inclusos" | Padrão reutilizável (serve para porção com acompanhamento incluso) |
| Grupo compartilhado | Faixa amarela + aba **Produtos** com contador; a faixa desloca o layout |
| Tamanhos | Um produto por tamanho; mesma foto nos três |
| Marcar opção em modal | **Por texto, reconsultando a lista** — nunca por índice pré-calculado |
| Verificação | Abrir o produto no PDV antes de capturar, para conferir se todas as opções entraram |
| Setas em tabela | Apontar para a **última** linha, vindo de baixo |

**Antes do #31 (comida japonesa): avisar o dono para limpar a base e esperar a confirmação.**
