# texto-documentation.ia.md — Campanhas SMS

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.
> O projeto do manual **já está anexo no contexto** — o prompt aponta os **arquivos exatos** a ler.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Food Marketing**, adicione um **item de menu por último** chamado **"Campanhas SMS"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/campanhas-sms/campanhas-sms.md`

2. **Imagens (use estas 14, nesta ordem):**
   - `beefood-web-react-manual/manuais/campanhas-sms/imagens-tratadas/01-lista-campanhas.png`
   - `beefood-web-react-manual/manuais/campanhas-sms/imagens-tratadas/02-passo1-mensagem.png`
   - `beefood-web-react-manual/manuais/campanhas-sms/imagens-tratadas/03-aviso-ucs2.png`
   - `beefood-web-react-manual/manuais/campanhas-sms/imagens-tratadas/05-passo2-segmentacao.png`
   - `beefood-web-react-manual/manuais/campanhas-sms/imagens-tratadas/06-passo2-avulso.png`
   - `beefood-web-react-manual/manuais/campanhas-sms/imagens-tratadas/07-passo2-excel.png`
   - `beefood-web-react-manual/manuais/campanhas-sms/imagens-tratadas/09-aviso-link.png`
   - `beefood-web-react-manual/manuais/campanhas-sms/imagens-tratadas/09b-confirmar-envio.png`
   - `beefood-web-react-manual/manuais/campanhas-sms/imagens-tratadas/14-lista-apos-envio.png`
   - `beefood-web-react-manual/manuais/campanhas-sms/imagens-tratadas/15-detalhe-envio.png`
   - `beefood-web-react-manual/manuais/campanhas-sms/imagens-tratadas/16-extrato-apos-envio.png`
   - `beefood-web-react-manual/manuais/campanhas-sms/imagens-tratadas/10-comprar-creditos.png`
   - `beefood-web-react-manual/manuais/campanhas-sms/imagens-tratadas/12-blacklist.png`
   - `beefood-web-react-manual/manuais/campanhas-sms/imagens-tratadas/13-adicionar-blacklist.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**

- Use o conteúdo do `campanhas-sms.md` exatamente como está (seções, textos e tabelas).
- Insira as 14 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Use **números normais** (`1`, `2`, `3`) nas referências às setas — **não** use números circulados (①②③).
- Idioma **português do Brasil**, tom didático (usuário final).
- Mantenha em destaque, sem resumir:
  - que **cada segmento = 1 crédito por destinatário**;
  - a tabela **GSM-7 (160) × UCS-2 (70)** e o switch **Enviar sem acento e emoji**;
  - que o custo usa o **pior caso** da lista (um nome com acento pode jogar a campanha inteira para UCS-2);
  - que **não existe auto-save** — o rascunho só grava ao avançar do passo 1;
  - que `{{meu_link}}` ganha `?sms=` e é o que permite medir clique e conversão;
  - que SMS com link pede confirmação extra e pode ir para spam;
  - que o envio **não tem volta**;
  - que **opt-out** (`SAIR` / `PARAR` / `STOP` / `CANCELAR` / `DESCADASTRAR`) e erro permanente entram na blacklist, e que **conteúdo bloqueado não bloqueia o número**;
  - que crédito de falha permanente **não volta**;
  - as faixas de preço do PIX (R$ 0,16 / 0,14 / 0,12), mínimo R$ 5 e máximo R$ 10.000.
- O manual é principalmente de **desktop**. Pode citar que existe versão no celular, sem descrevê-la.
- Se o app permitir, cite a **Segmentação de Clientes** e as **Campanhas Inteligentes** como leitura complementar.

---

## Estrutura da página (na ordem do `.md`)

1. Introdução
2. **Onde encontrar**
3. **Como o crédito é cobrado**
4. **Passo 1 — A mensagem** (e o aviso de UCS-2)
5. **Passo 2 — Os destinatários** (segmentação, avulso, planilha)
6. **Passo 3 — Resumo e envio**
7. **Depois de enviar**
8. **Comprar créditos por PIX**
9. **Blacklist / opt-out**
10. **Dicas**

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-lista-campanhas.png` | com setas | 1 aba **Campanhas** · 2 **Saldo & Extrato** · 3 **Blacklist / Opt-out** · 4 **NOVA CAMPANHA** · 5 **Saldo SMS** · 6 **COMPRAR CRÉDITOS** |
| 2 | `02-passo1-mensagem.png` | com setas | 1 **Cardápio** · 2 botões de variável · 3 `{{primeiro_nome}}` · 4 `{{meu_link}}` · 5 prévia · destaque no aviso de link |
| 3 | `03-aviso-ucs2.png` | com setas | 1 contador **UCS-2** · 2 aviso de 70/67 chars · 3 switch desligado |
| 4 | `05-passo2-segmentacao.png` | com setas | 1 **Por segmentação** · 2 **Telefone avulso** · 3 **Planilha** · 4 seletor do público |
| 5 | `06-passo2-avulso.png` | com setas | 1 modo **Telefone avulso** · 2 campo do número · 3 **ADICIONAR** · 4 linha na lista |
| 6 | `07-passo2-excel.png` | com setas | 1 modo **Planilha** · 2 **SELECIONAR ARQUIVO** |
| 7 | `09-aviso-link.png` | com setas | 1 texto do risco · 2 **ENVIAR COM LINK (ENTER)** |
| 8 | `09b-confirmar-envio.png` | com setas | 1 destinatários / custo / saldo · 2 **ENVIAR (ENTER)** |
| 9 | `14-lista-apos-envio.png` | com setas | 1 selo **Enviada** · 2 saldo descontado · 3 ver detalhe |
| 10 | `15-detalhe-envio.png` | com setas | 1 cartões de resultado · 2 **EXPORTAR CSV** · 3 **ATUALIZAR** |
| 11 | `16-extrato-apos-envio.png` | com setas | 1 saldo depois · 2 débito da campanha |
| 12 | `10-comprar-creditos.png` | com setas | 1 total da compra · 2 slider · 3 pacotes sugeridos |
| 13 | `12-blacklist.png` | com setas | 1 texto de opt-out · 2 **ADICIONAR MANUAL** · 3 tabela |
| 14 | `13-adicionar-blacklist.png` | com setas | 1 campo telefone · 2 **SALVAR (F2)** |

---

## Observações de conteúdo

- Os números das imagens são reais da conta de testes **BeeFood3 - Manual**: saldo 95 → 92, campanha **#65**, 3 destinatários, 3 créditos. O manual não promete resultado comercial; usa os números só para mostrar onde cada informação aparece.
- Na lista de destinatários e no detalhe, **telefones de fixture** (não o comercial) foram cobertos de propósito. Mantenha as imagens como estão.
- O telefone **(15) 99132-0694** (comercial da BeeFood) foi autorizado pelo dono para o disparo de teste e aparece como exemplo de telefone avulso.
- **Não** publique nada do `fluxo-codigo.md` (rotas de API, chaves JSON, nomes de arquivo do front).
