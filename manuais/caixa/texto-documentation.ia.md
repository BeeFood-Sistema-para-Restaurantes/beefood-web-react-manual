# texto-documentation.ia.md — Caixa (abrir, receber, consultar)

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.
> O projeto do manual **já está anexo no contexto** — o prompt aponta os **arquivos exatos** a ler.

> **Nota:** este foi o primeiro manual do repositório e a página dele foi publicada **antes** de o
> prompt existir — é a ela que os outros manuais se referem quando pedem "apresente as imagens
> igual ao menu Abrir Caixa". O arquivo ficou escrito para republicação e para a pasta seguir o
> mesmo padrão das outras 98.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Caixa**, adicione um **item de menu como primeiro** chamado **"Abrir Caixa"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/caixa/caixa.md`

2. **Imagens (use estas 5, nesta ordem):**
   - `beefood-web-react-manual/manuais/caixa/imagens-tratadas/03-modal-abrir-caixa-preenchido.png`
   - `beefood-web-react-manual/manuais/caixa/imagens-tratadas/05-pdv-formas-pagamento.png`
   - `beefood-web-react-manual/manuais/caixa/imagens-tratadas/06-pdv-dinheiro-valor.png`
   - `beefood-web-react-manual/manuais/caixa/imagens-tratadas/08-caixa-listagem-aberto.png`
   - `beefood-web-react-manual/manuais/caixa/imagens-tratadas/09-ver-caixa-check.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**

- Use o conteúdo do `caixa.md` exatamente como está (seções, textos e tabelas "Nº da seta → campo").
- Insira as 5 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- Use **números normais** (`1`, `2`, `3`) nas referências às setas — **não** use números circulados (①②③).
- Idioma **português do Brasil**, tom didático (usuário final).
- Mantenha em destaque: o valor entra no caixa **automaticamente** ao finalizar o pagamento de uma
  venda — **não existe** tela de "lançar dinheiro no caixa"; só a forma **Dinheiro** soma em
  **Vendas em Dinheiro**; e **Valor em Caixa = Saldo Inicial + Vendas em Dinheiro − Sangrias**.
- O manual é de **desktop**. Não descreva a versão mobile.

---

## Estrutura da página (na ordem do `.md`)

1. Introdução (o que o manual ensina) e **Pré-requisitos**
2. **Etapa 1** — Abrir o caixa
3. **Etapa 2** — Receber um pagamento (cai no caixa)
4. **Etapa 3** — Consultar o valor no caixa aberto
5. **Dicas rápidas**

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `03-modal-abrir-caixa-preenchido.png` | com setas | 1 **Saldo Inicial em Dinheiro** · 2 **Caixa** · 3 **Tipos de Venda** · 4 **ABRIR CAIXA** |
| 2 | `05-pdv-formas-pagamento.png` | com setas | 1 **Dinheiro** · 2 **Valor a receber** (Total e Falta) |
| 3 | `06-pdv-dinheiro-valor.png` | com setas | 1 **Valor do pagamento** · 2 **CONFIRMAR (ENTER/F1)** |
| 4 | `08-caixa-listagem-aberto.png` | com setas | 1 **Ver Caixa** (lupa azul) · 2 status **Em aberto** |
| 5 | `09-ver-caixa-check.png` | com setas | 1 **Operação da venda** · 2 **VENDAS EM DINHEIRO** · 3 **VALOR EM CAIXA** |

---

## Observações de conteúdo

- O exemplo do manual é real (conta de testes): caixa aberto com **R$ 50,00**, uma venda de
  **R$ 4,44** em dinheiro, e **Valor em Caixa** de **R$ 54,44**.
- **Sangria**, **acréscimo** e o **fechamento** aparecem só como dica no final. Fechar caixa tem
  manual próprio (**Fechar Caixa**) — não desenvolva o assunto aqui.
- As capturas deste manual estão em **tema escuro**, por serem as primeiras do repositório; o padrão
  passou a ser tema claro. Se as imagens forem refeitas, recapturar no claro e manter as mesmas
  cinco etapas.
- **Não** publique nada do `fluxo-codigo.md` (rotas de API, nomes de campos, permissões internas).
