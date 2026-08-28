# MEMÓRIA — Manual de Campanhas SMS

> Memória detalhada deste manual (fluxo, uso, decisões e estado), para retomar a qualquer momento.
> Ver também a memória geral: `../../MEMORIA-GERAL.md`.

Status: ✅ **Concluído** — Última atualização: 2026-08-28

---

## 1. Escopo do manual

Aprovado no checklist (#18): **criar campanha de SMS**, entender a **contagem de créditos por
segmento** (e como economizar sem acento/emoji), **comprar créditos por PIX** e usar a
**blacklist / opt-out**.

Autorização do dono nesta sessão: a empresa de testes **tem créditos sobrando** e um disparo
real podia ir para **15 99132-0694** (telefone do comercial da BeeFood).

Arquivo final: `campanhas-sms.md`. Mapa técnico: `fluxo-codigo.md`.

---

## 2. Conteúdo da pasta

```
manuais/campanhas-sms/
├─ MEMORIA.md
├─ campanhas-sms.md              (manual final — 14 imagens)
├─ fluxo-codigo.md
├─ texto-documentation.ia.md
├─ annotate.py
├─ imagens-puras/                (também 04, 08, 08b, 11 — backup, sem seta)
└─ imagens-tratadas/             (14 usadas no manual)
```

Puras não referenciadas: `04-sem-acento.png` (quase igual à 02), `08-passo3-resumo.png` e
`08b-passo3-preview.png` (rascunho temporário com nome feio), `11-saldo-extrato.png` (a 16
já mostra o extrato depois do débito).

---

## 3. Onde a funcionalidade fica

**Food Marketing → Campanhas SMS**, rota `/food-marketing/campanhas-sms`. Três abas:
**Campanhas**, **Saldo & Extrato**, **Blacklist / Opt-out**. Existe no desktop e no mobile;
o manual é de desktop.

Permissão: chave JSON `campanhaSMS` (distinta das Campanhas WhatsApp).

API de produção (não é DataSnap): `https://app3.beetechapi.be/api/sms2/...`.
Empresa **38311**, usuário **88711**.

---

## 4. O que foi capturado, e como

Ambiente: **BeeFood3 - Manual** (`contato@beefood.com.br`), tema claro, Playwright,
viewport 1440×900 / DPR 1.5 → 2160×1350.

Scripts em `/tmp/cap-sms/` (não versionados). Diagnóstico pela API antes de escrever:

| Dado | Valor em 28/08/2026 |
|---|---|
| Saldo inicial | **95** créditos (os 100 de agosto já tinham 5 débitos de *Confirmação de telefone*) |
| Campanha | rascunho **#65** "Campanha SMS", mensagem `12123`, 0 dest na listagem — mas o passo 2 já tinha **Maria Santos** e **João Silva** (fixtures) |
| Variáveis | `primeiro_nome`, `nome`, `saldo_cashback`, `meu_link` |
| Pacotes | 1.000 / 5.000 / 10.000 / 20.000 · faixas 0,16 / 0,14 / 0,12 · mín R$ 5 / 32 cred. |
| Blacklist | 2 números manuais |
| PIX pendente | nenhum |

O editor **não tem auto-save**: só grava ao avançar do passo 1. Dá para fotografar UCS-2 e
sair. **Não geramos PIX** — o pedido ficaria pendente de verdade.

### Disparo real

Reaproveitamos o rascunho **#65**. Mensagem:

`Oi {{primeiro_nome}}! Teste de campanha SMS do Beefood. Peca pelo cardapio: {{meu_link}}`

Switch de acento **ligado**. Destinatários no envio: os dois fixtures **mais** o comercial
**(15) 99132-0694**. Custo **3 créditos**. Saldo **95 → 92**. Status dos três: **Aceito** /
Message Sent. Entregues ainda 0 no momento da captura (a operadora confirma depois).

O rascunho já tinha os dois fixtures — só vimos no passo 2. Não era a base de clientes da
loja; eram números de teste. Mesmo assim, o comercial autorizado **recebeu**.

Um rascunho extra (*Rascunho captura resumo*, id 205) foi criado só para tentar o passo 3
inteiro e **descartado** em seguida.

---

## 5. Decisões de conteúdo

1. O manual **abre pelo crédito** (GSM 160 × UCS-2 70). É a dúvida que queima dinheiro.
2. Os três caminhos de destinatário (segmentação / avulso / Excel) ficam no mesmo passo,
   com uma imagem cada.
3. PIX sem gerar pedido: o modal no mínimo (32 créditos / R$ 5,12) basta para ensinar
   faixa e slider.
4. Telefones de fixture e da blacklist **borrados na pura**. O comercial autorizado
   permanece visível como exemplo de avulso.
5. Landing vazia (`SmsEmptyLanding`) não foi fotografada: a conta já tinha campanha. Os
   presets da landing usam `{nome}` (errado); o editor correto é `{{chave}}`. O manual
   ensina só o formato certo.

---

## 6. Achados que valem para qualquer conta

**1. O custo é o pior caso da lista.** `piorCasoCreditos` substitui nome, cashback e link
e pega o máximo de segmentos. Um nome com acento + switch desligado joga **todo mundo**
para UCS-2.

**2. `{{meu_link}}` nasce sem `https://` e ganha `?sms={id}`.** Na prévia do #65:
`menu.beefood.com.br/beefood3?sms=65`. Domínio externo não mede clique.

**3. Extrato usa a chave `movimentos`, não `extrato`.** E mistura campanha com
*Confirmação de telefone* de cupom (1 crédito cada).

**4. Campanha enviada ou em envio não exclui.** Só rascunho / abortada / erro.

**5. Conteúdo bloqueado ≠ blacklist.** A própria aba explica: o problema é da mensagem.

**6. A API de produção não é `/datasnap/rest/`.** O host é `app3.beetechapi.be/api/sms2`.

---

## 7. Estado deixado no sistema

| Item | Estado |
|---|---|
| Campanha #65 *Teste manual SMS* | **Enviada**, 3 dest, 3 créditos, 28/08/2026 16:45 |
| Saldo | **92** créditos |
| Blacklist | inalterada (2 manuais) |
| PIX | nenhum pedido novo |
| Rascunho 205 | descartado |

---

## 8. Possíveis próximos incrementos

- Manual de **receitas** juntando segmentação + SMS (ideia já no checklist).
- Versão **mobile** das Campanhas SMS (`MobileSmsPage`).
- Aba **Indicadores** das Campanhas WhatsApp (ainda sem manual).
