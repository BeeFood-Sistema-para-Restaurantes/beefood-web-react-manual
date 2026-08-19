# texto-documentation.ia.md — Fechar Caixa

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.
> O projeto do manual **já está anexo no contexto** — o prompt aponta os **arquivos exatos** a ler.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Caixa**, adicione um **item de menu por último** chamado **"Fechar Caixa"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/caixa-fechar/caixa-fechar.md`

2. **Imagens (use estas 12, nesta ordem):**
   - `beefood-web-react-manual/manuais/caixa-fechar/imagens-tratadas/01-listagem-caixa-aberto.png`
   - `beefood-web-react-manual/manuais/caixa-fechar/imagens-tratadas/02-ver-caixa-fechar.png`
   - `beefood-web-react-manual/manuais/caixa-fechar/imagens-tratadas/03-vendas-pendentes.png`
   - `beefood-web-react-manual/manuais/caixa-fechar/imagens-tratadas/04-pagamento-venda.png`
   - `beefood-web-react-manual/manuais/caixa-fechar/imagens-tratadas/05-venda-paga.png`
   - `beefood-web-react-manual/manuais/caixa-fechar/imagens-tratadas/06-aviso-fechar-mesmo-assim.png`
   - `beefood-web-react-manual/manuais/caixa-fechar/imagens-tratadas/07-conferencia-em-branco.png`
   - `beefood-web-react-manual/manuais/caixa-fechar/imagens-tratadas/08-calculadora-dinheiro.png`
   - `beefood-web-react-manual/manuais/caixa-fechar/imagens-tratadas/09-conferencia-com-quebra.png`
   - `beefood-web-react-manual/manuais/caixa-fechar/imagens-tratadas/10-confirmar-fechamento.png`
   - `beefood-web-react-manual/manuais/caixa-fechar/imagens-tratadas/11-imprimir-conferencia.png`
   - `beefood-web-react-manual/manuais/caixa-fechar/imagens-tratadas/12-listagem-fechado.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**

- Use o conteúdo do `caixa-fechar.md` exatamente como está (seções, textos e tabelas "Nº da seta → campo").
- Insira as 12 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Use **números normais** (`1`, `2`, `3`) nas referências às setas — **não** use números circulados (①②③).
- Idioma **português do Brasil**, tom didático (usuário final).
- Mantenha em destaque: o caminho é sempre **Ver Caixa → FECHAR CAIXA**; o recomendado é **quitar
  as vendas pendentes antes de fechar**; **Salvar Conferência mantém o caixa aberto** e
  **Fechar Caixa encerra**; no **Dinheiro** a comparação é com o **saldo** (a sangria já está descontada).
- O manual é de **desktop**. Não descreva a versão mobile.

---

## Estrutura da página (na ordem do `.md`)

1. Introdução (o que o manual ensina) e **Pré-requisitos**
2. **Etapa 1** — Abrir a tela de fechamento
3. **Etapa 2** — Resolver as vendas sem pagamento total (com o subitem "Como quitar uma venda por aqui" e "Se você optar por fechar com pendências")
4. **Etapa 3** — Conferir os valores (1ª conferência), com "Usando a calculadora" e "Atenção ao Dinheiro"
5. **Etapa 4** — Entender os totais e a quebra de caixa
6. **Etapa 5** — Salvar sem fechar, ou fechar o caixa
7. **Etapa 6** — Confirmar o resultado na listagem
8. **Dicas rápidas**

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-listagem-caixa-aberto.png` | com setas | 1 status **Em aberto** · 2 **Ver Caixa** (lupa azul) |
| 2 | `02-ver-caixa-fechar.png` | com setas | 1 botão **FECHAR CAIXA** · 2 **VALOR EM CAIXA** |
| 3 | `03-vendas-pendentes.png` | com setas | 1 botão verde (pagar a venda) · 2 coluna **Faltante** · 3 **FECHAR CAIXA MESMO ASSIM (F2)** |
| 4 | `04-pagamento-venda.png` | com setas | 1 **Pagamentos realizados** (Débito · Pago) · 2 **Pagamento completo** |
| 5 | `05-venda-paga.png` | com setas | 1 botão virou check (ver pagamentos) · 2 status **PAGA** |
| 6 | `06-aviso-fechar-mesmo-assim.png` | com setas | 1 **Por que confirmar os pagamentos antes?** · 2 **NÃO, REVISAR (ESC)** · 3 **FECHAR ASSIM MESMO (ENTER)** |
| 7 | `07-conferencia-em-branco.png` | com setas | 1 coluna **Entrada** · 2 campo **1ª Conferência** · 3 ícone da **calculadora** · 4 seta que abre o detalhe do **Dinheiro** |
| 8 | `08-calculadora-dinheiro.png` | com setas | 1 campo de valor · 2 **Valores Adicionados** · 3 **Total** · 4 **Incluir Conferência** |
| 9 | `09-conferencia-com-quebra.png` | com setas | 1 **Diferença** (-R$ 2,55) · 2 **Quebra de Caixa** (Falta) · 3 **Saldo Final Conferido** |
| 10 | `10-confirmar-fechamento.png` | com setas | 1 botão **Fechar caixa** na confirmação |
| 11 | `11-imprimir-conferencia.png` | com setas | 1 **Sim, imprimir** · 2 **Não** |
| 12 | `12-listagem-fechado.png` | com setas | 1 **Data/Hora Fechamento** · 2 **Conf. Saldo Final** · 3 **Quebra de Caixa** |

---

## Observações de conteúdo

- O exemplo do manual é real (conta de testes): dinheiro apurado **R$ 102,55**, contado
  **R$ 100,00**, resultando em **Quebra de Caixa R$ 2,55 (Falta)**; total apurado
  **R$ 1.911,98** contra **R$ 1.909,43** conferidos.
- A **segunda conferência** é mencionada apenas como dica no final. Ela terá manual próprio —
  não desenvolva o assunto aqui.
- **Não** publique nada do `fluxo-codigo.md` (rotas de API, nomes de campos, permissões internas).
