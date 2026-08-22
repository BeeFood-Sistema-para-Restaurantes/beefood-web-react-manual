# MEMÓRIA — Manual #47 Avisos do cardápio digital

> Memória detalhada deste manual: decisões, descobertas e estado do ambiente.

Última atualização: 2026-08-22 (manual produzido; aguardando publicação do dono)

---

## 1. Escopo

Um manual só, aba **Cardápio Digital → Avisos**. Recado operacional no cardápio do
cliente: feriado, horário novo, salão fechado. **Não** divulga produto e **não** tem
call to action — destaque e produto resolvem combo/lançamento.

Aprovado pelo dono depois do estudo: loja de exemplo = hamburgueria do sandbox
BeeFood3; artes em cartaz 1:1 com texto grande (a foto de fachada com papelzinho foi
recusada); três avisos (feriado, horário, só delivery).

---

## 2. Descobertas

### Não existe data de calendário

Os chips são `DOM…SÁB` (`domingo = 1`). Não há “7 de setembro”. O feriado do exemplo
é texto no cartaz; o lojista liga e depois pausa. Deixar só na segunda faz o aviso
voltar toda segunda.

### Título obrigatório no painel; descrição manda no modal

O backend aceita título vazio. O modal do painel **bloqueia** sem título e, se for
aviso recém-enviado, **CANCELAR descarta**. Sem descrição, o card no cardápio **não
abre detalhe**.

### Sem botão Salvar na aba

Cada ação persiste (`persistir` em `AvisosTab.tsx`). O plano interno antigo falava em
botão *SALVAR AVISOS* e teto de 5 avisos em 4:3 — **superado**. No ar: até **10**,
formato livre com ideal **1:1**, auto-save por ação.

### Quem decide se está no ar é o celular do cliente

Mesmo helper dos banners (`bannerAgenda`: dia `getDay()+1`, `hFim` exclusivo, sem
cruzar meia-noite). Cache do `validaDelivery` ~55 s — toast *até 1 minuto*.

### Horário inválido vira dia inteiro

O backend (`sanitizarJanela`) não descarta o aviso: se `hIni >= hFim` ou hora
inválida, grava `todoDia: true`. O lojista vê o aviso no ar e corrige.

### Aviso ≠ banner de cupom ≠ cashback

No cardápio do sandbox já existem a faixa verde de cupom e o card amarelo de
cashback. Os avisos entram **entre o filtro de categorias e os produtos**, em
carrossel (sem rotação automática).

### O subtítulo da aba ainda fala em “promoções”

Texto de produto. O manual corrige: promoção de item é Destaque.

---

## 3. Cenário no sandbox (BeeFood3)

Conta `contato@beefood.com.br`. Três avisos **deixados no ar** para o dono conferir:

| Aviso | Agenda gravada no fim | Canal |
|-------|------------------------|-------|
| Fechados no feriado | Todo dia · 24h | D + P |
| Novo horário | Seg–sáb · 24h (a captura do modal ainda mostra 18:00–23:00) | D + P |
| Hoje só delivery | Todo dia · 24h | só D |

O segundo aviso foi fotografado **com** a faixa 18:00–23:00 e depois voltou para dia
inteiro — senão, de manhã, o card some do cardápio público.

Cartazes em `/tmp/avisos-upload/` (não versionados como arte-fonte; a imagem pura do
painel e do cardápio já tem o cartaz).

Cardápio de prova: `https://menu.beefood.com.br/beefood3`.

---

## 4. Captura

Playwright, `LANG=pt_BR.UTF-8`, viewport 1440×900 DPR 1.5 (painel e desktop do
cardápio); mobile 390×844 DPR 2. Espera de 5 s após spinner. Widget flutuante
escondido por CSS. Banner *Dispensar* quando apareceu.

Onze imagens. Duas de contexto (modais do cardápio): o cartaz é o assunto, seta
taparia o texto.

---

## 5. Estado

Manual escrito, imagens anotadas, `validar-imagens.py` a rodar neste fechamento.
Aguardando publicação. Os três avisos **ficam** no sandbox até o dono pedir para
limpar.
