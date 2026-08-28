# MEMÓRIA — Manual de Campanhas SMS

> Memória detalhada deste manual (fluxo, uso, decisões e estado), para retomar a qualquer momento.
> Ver também a memória geral: `../../MEMORIA-GERAL.md`.

Status: 🔨 **Em execução** — Última atualização: 2026-08-28

---

## 1. Escopo do manual

Aprovado no checklist (#18): **criar campanha de SMS**, entender a **contagem de créditos por
segmento** (e como economizar sem acento/emoji), **comprar créditos por PIX** e usar a
**blacklist / opt-out**.

Autorização do dono nesta sessão: a empresa de testes **tem créditos sobrando** e um disparo
real pode ir para **15 99132-0694** (telefone do comercial da BeeFood). Não disparar para a
base de clientes.

Arquivo final: `campanhas-sms.md`. Mapa técnico: `fluxo-codigo.md`.

---

## 2. Conteúdo da pasta

```
manuais/campanhas-sms/
├─ MEMORIA.md
├─ campanhas-sms.md
├─ fluxo-codigo.md
├─ texto-documentation.ia.md
├─ annotate.py
├─ imagens-puras/
└─ imagens-tratadas/
```

---

## 3. Onde a funcionalidade fica

**Food Marketing → Campanhas SMS**, rota `/food-marketing/campanhas-sms`. Três abas:
**Campanhas**, **Saldo & Extrato**, **Blacklist / Opt-out**. Existe no desktop e no mobile;
o manual é de desktop.

Permissão: chave JSON `campanhaSMS` (distinta das Campanhas WhatsApp).

---

## 4. O que já se sabe pelo código (antes das capturas)

- Editor em 3 passos (Mensagem → Destinatários → Resumo), **sem auto-save**. Só grava ao
  avançar do passo 1. Dá para fotografar avisos e sair por FECHAR (ESC).
- Switch **Enviar sem acento e emoji** nasce **ligado**. GSM-7 = 160 chars / 1 crédito;
  UCS-2 (acento/emoji) = 70 chars / 1 crédito. Cada segmento extra = 1 crédito a mais por
  destinatário. O custo usa o **pior caso** da lista (nome com acento pode jogar tudo para UCS-2).
- Destinatários: segmentação ativa, telefone avulso ou Excel. Blacklist é removida sozinha.
- Compra: PIX (Asaas), mínimo R$ 5, faixas 0,16 / 0,14 / 0,12, máximo R$ 10.000 por pedido.
  **Não gerar PIX** nas capturas — o pedido fica pendente de verdade.
- Opt-out: resposta `SAIR` / `PARAR` / `STOP` / `CANCELAR` / `DESCADASTRAR`. Erro permanente
  de entrega também entra. Conteúdo bloqueado **não** bloqueia o número. Crédito de falha
  permanente **não volta**.
- Landing vazia usa `{nome}` nos presets; o editor correto é `{{chave}}`.

---

## 5. Plano de captura

Ambiente: **BeeFood3 - Manual** (`contato@beefood.com.br`), tema claro, Playwright,
viewport 1440×900 / DPR 1.5.

1. Diagnosticar saldo, campanhas, variáveis, pacotes e blacklist pela API.
2. Capturar as três abas e o modal de compra **sem** gerar PIX.
3. Abrir o editor, fotografar passo 1 (GSM, UCS-2, switch, variáveis, prévia) e sair sem salvar
   o que for só ensaio.
4. Criar uma campanha só com o telefone **15 99132-0694**, avançar, fotografar destinatários
   (os três modos) e o resumo.
5. Enviar de verdade (1 destinatário, 1 crédito se a mensagem couber em 1 segmento GSM).
6. Fotografar o detalhe/resultado e o débito no extrato.
7. Fotografar a blacklist (texto + modal de adicionar, sem gravar o comercial).

Dado pessoal de cliente: cobrir na imagem **pura**. O telefone do comercial foi autorizado
pelo dono para o teste; no manual ele entra como exemplo de telefone avulso.
