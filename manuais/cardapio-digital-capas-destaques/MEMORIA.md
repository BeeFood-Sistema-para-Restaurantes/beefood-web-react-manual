# MEMÓRIA — Manual #48 Capas e Destaques

> Memória detalhada deste manual: decisões, descobertas e estado do ambiente.

Última atualização: 2026-08-22 (manual produzido; aguardando publicação do dono)

---

## 1. Escopo

Um manual só, caminho **Cardápio Digital → Configurações → Capas e Destaques**.
Dois grupos (`capas` e `lojas`), imagem **e vídeo**, agenda por dia/hora/canal,
prova no cardápio público em desktop e mobile.

Não cobre: aviso (#47), capa fixa `fotoCapa` além da menção de que ela é só
imagem e entra como primeiro slide, horário/pausa (#32/#33).

---

## 2. Descobertas

### Sem auto-save

O modal é sujo (`dirty`) e só o **SALVAR (F2)** chama o POST. Fechar com
alteração abre “Descartar alterações”. Clique fora é bloqueado. Contraste com
avisos e horário, que gravam sozinhos.

### Capa fixa ≠ destaques da capa

`fotoCapa` (preview clicável no topo da aba) aceita só `image/png|jpeg|webp`.
Os **destaques da capa** é que aceitam vídeo e entram no carrossel **depois**
da capa fixa (`PreviewCarrossel` com `fundoComoSlide`).

### HEVC é armadilha

O validador lê os primeiros 256 KB e bloqueia `hvc1|hev1`. Se passar, o
Android mostra tela preta **sem evento de erro**. AVI/MKV também bloqueados.

### Recorte 16:9 no navegador

Vídeo vertical abre `ModalRecortarVideoBanner` (WebCodecs, sem áudio, máx 60 s,
saída 1280×720). Imagem vertical é recusada — não tem recorte.

### Agenda no relógio do cliente

Mesmo helper dos avisos (`bannerAgenda`): domingo=1, `hFim` exclusivo, sem
cruzar meia-noite. Backend (`sanitizarJanela`) com hora inválida vira **dia
inteiro**, não descarta. O painel recusa F2 se início = fim.

### Cache de até 1 minuto

`validaDelivery` + changelog. Toast/histórico pedem essa espera.

### Áudio some de propósito

O recorte descarta o som. O cardápio toca `<video muted>`.

---

## 3. Cenário no sandbox (BeeFood3)

Conta `contato@beefood.com.br`. Quatro mídias **deixadas no ar**:

| Grupo | Tipo | Arte | Agenda |
|-------|------|------|--------|
| capas | imagem | COMBO DO DIA (hambúrguer) | Todo dia · 24h · D+P |
| capas | vídeo | SAIU DO FOGÃO (chapa, Ken Burns 5 s) | Todo dia · 24h · D+P |
| lojas | imagem | BATATA + REFRI | Todo dia · 24h · D+P |
| lojas | vídeo | MILKSHAKE | Todo dia · 24h · D+P |

Artes geradas e convertidas em `/tmp/capas-midias/` (não versionadas). Vídeos
MP4 H.264 1280×720, ~390 KB, sem áudio.

Havia 1 vídeo + 2 imagens pausadas de teste antigo; foram **substituídas**.

Capa fixa (`fotoCapa`) do sandbox **não foi trocada** (hambúrguer + batata +
refri já existente). Avisos do #47 **não foram mexidos**.

Cardápio de prova: `https://menu.beefood.com.br/beefood3`.

---

## 4. Captura

Playwright, `LANG=pt_BR.UTF-8`, viewport 1440×900 DPR 1.5 (painel e desktop);
mobile 390×844 DPR 2. Espera de 5 s após spinner. Widget flutuante escondido.
Banner *Dispensar* quando apareceu.

A prévia do celular (`aside` inteiro) saiu com 5615 px de altura; o `07` é
recorte da captura 01 (aparelho + texto da prévia).

Onze imagens. Duas de contexto (vitrine no desktop e no mobile): o banner é o
assunto, seta taparia a arte. As 09 e 11 mostram o slide *BATATA + REFRI*;
as 08 e 10 mostram o *MILKSHAKE* — os dois tipos no cardápio público.

O cupom verde do cardápio público (*Você tem 2 cupons!*) não fechou pelo
seletor — ficou nas capturas 10 e 12. Não é desta tela.

---

## 5. Estado

Manual escrito, imagens anotadas, `validar-imagens.py` a rodar neste
fechamento. As quatro mídias **ficam** no sandbox até o dono pedir para limpar.
