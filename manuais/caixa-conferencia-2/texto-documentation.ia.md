# texto-documentation.ia.md — Segunda conferência (dupla checagem)

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.
> O projeto do manual **já está anexo no contexto** — o prompt aponta os **arquivos exatos** a ler.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Caixa**, adicione um **item de menu por último** chamado **"Segunda Conferência"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/caixa-conferencia-2/caixa-conferencia-2.md`

2. **Imagens (use estas 9, nesta ordem):**
   - `beefood-web-react-manual/manuais/caixa-conferencia-2/imagens-tratadas/01-listagem-caixa-fechado.png`
   - `beefood-web-react-manual/manuais/caixa-conferencia-2/imagens-tratadas/02-primeira-conferencia-leitura.png`
   - `beefood-web-react-manual/manuais/caixa-conferencia-2/imagens-tratadas/03-segunda-conferencia-em-branco.png`
   - `beefood-web-react-manual/manuais/caixa-conferencia-2/imagens-tratadas/04-calculadora-recontagem.png`
   - `beefood-web-react-manual/manuais/caixa-conferencia-2/imagens-tratadas/05-segunda-conferencia-conferida.png`
   - `beefood-web-react-manual/manuais/caixa-conferencia-2/imagens-tratadas/06-observacoes-conferido.png`
   - `beefood-web-react-manual/manuais/caixa-conferencia-2/imagens-tratadas/07-confirmar-conferencia.png`
   - `beefood-web-react-manual/manuais/caixa-conferencia-2/imagens-tratadas/08-listagem-conferido.png`
   - `beefood-web-react-manual/manuais/caixa-conferencia-2/imagens-tratadas/09-conferencia-travada.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**

- Use o conteúdo do `caixa-conferencia-2.md` exatamente como está (seções, textos e tabelas "Nº da seta → campo").
- Comece pela seção **"Por que a segunda conferência importa"** — ela é a razão de ser do manual e não deve ser resumida.
- Insira as 9 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Use **números normais** (`1`, `2`, `3`) nas referências às setas — **não** use números circulados (①②③).
- Idioma **português do Brasil**, tom didático (usuário final).
- Mantenha em destaque: a conferência é feita **uma única vez** e depois **trava**; quem confere
  **não deve ser** quem contou; a **1ª conferência nunca é apagada** (fica na coluna ao lado e em
  **Quebra 1ª Conf.**); o botão **Conferir** só libera com a declaração marcada.
- Este manual é a **continuação do "Fechar Caixa"**. Se o app permitir, cite esse manual como leitura anterior.
- O manual é de **desktop**. Não descreva a versão mobile.

---

## Estrutura da página (na ordem do `.md`)

1. Introdução (o que o manual ensina)
2. **Por que a segunda conferência importa**
3. **Pré-requisitos**
4. **Etapa 1** — Abrir a conferência do caixa fechado
5. **Etapa 2** — Iniciar a segunda conferência
6. **Etapa 3** — Recontar e digitar os valores
7. **Etapa 4** — Comparar e ver a quebra resolvida
8. **Etapa 5** — Registrar a observação e confirmar
9. **Etapa 6** — O que muda depois de conferir
10. **Dicas rápidas**

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-listagem-caixa-fechado.png` | com setas | 1 **Quebra de Caixa** (R$ 2,55) · 2 **Ver Conferência** (botão verde) |
| 2 | `02-primeira-conferencia-leitura.png` | com setas | 1 **Adicionar 2ª Conferência** · 2 campos travados da 1ª conferência · 3 **Quebra de Caixa** (Falta) |
| 3 | `03-segunda-conferencia-em-branco.png` | com setas | 1 coluna **2ª Conferência** (onde digitar) · 2 coluna **1ª Conferência** (consulta) · 3 **Observações da Conferência** |
| 4 | `04-calculadora-recontagem.png` | com setas | 1 campo de valor · 2 **Valores Adicionados** (R$ 100,00 + R$ 2,55) · 3 **Total** (R$ 102,55) · 4 **Incluir Conferência** |
| 5 | `05-segunda-conferencia-conferida.png` | com setas | 1 valor recontado com check verde · 2 **1ª Conferência** (R$ 100,00) · 3 **Quebra de Caixa: Correto** · 4 **Quebra 1ª Conf.** (R$ 2,55 Falta) |
| 6 | `06-observacoes-conferido.png` | com setas | 1 **Observações da Conferência** preenchida · 2 declaração marcada · 3 **Conferir** habilitado |
| 7 | `07-confirmar-conferencia.png` | com setas | 1 botão **Conferir** na confirmação |
| 8 | `08-listagem-conferido.png` | com setas | 1 **cadeado** (segunda conferência concluída) · 2 **Conf. Saldo Final** atualizado · 3 **Quebra de Caixa** zerada |
| 9 | `09-conferencia-travada.png` | com setas | 1 campos travados · 2 as duas contagens registradas · 3 **Conferir** desabilitado |

---

## Observações de conteúdo

- O exemplo é real (conta de testes) e continua o do manual "Fechar Caixa": a 1ª conferência
  apontou **R$ 2,55 (Falta)** no dinheiro e a recontagem encontrou o valor completo
  (**R$ 102,55**), zerando a quebra. O total do caixa é **R$ 1.911,98**.
- A observação usada no exemplo é *"Recontagem feita pela gerência: localizados R$ 2,55 em
  moedas que não haviam sido contados. Valores conferem."* — pode ser mantida como modelo.
- **Não** publique nada do `fluxo-codigo.md` (rotas de API, inversão dos campos no envio,
  permissões internas).
