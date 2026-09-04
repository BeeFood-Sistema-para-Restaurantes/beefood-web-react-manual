# texto-documentation.ia.md — Cadastrar forma de recebimento

## PROMPT (copiar e colar)

Em **Cadastros**, crie um novo item de menu por último chamado **Cadastrar forma de recebimento**.

Leia APENAS os arquivos abaixo (não varra o resto do projeto):

1. Conteúdo (use na íntegra):
    10|   `beefood-web-react-manual/manuais/formas-recebimento/formas-recebimento.md`
2. Imagens (nesta ordem), em `beefood-web-react-manual/manuais/formas-recebimento/imagens-tratadas/`:
   `01-menu-cadastros.png`, `02-listagem.png`, `03-nova-forma.png`, `04-ajuste-pagamento.png`,
   `05-aba-taxas.png`, `06-aba-tef.png`, `07-forma-criada.png`, `08-pagamento-presencial.png`,
   `09-cardapio-digital-formas.png`, `10-cardapio-adicionar.png`, `11-financeiro-formas.png`

NÃO leia outros arquivos (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

- Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. É um manual **de cadastro e de canais**: o leitor quer que a forma apareça no
    20|  lugar certo. Mantenha o passo a passo e as tabelas "Nº → o que fazer" logo depois de cada imagem.
- **Manter a tabela das três telas parecidas** (Cadastros × Cardápio Digital × Financeiro) na
  abertura: é ela que evita o erro mais comum.
- **Manter a tabela "onde você quer receber → switch que precisa estar ligado"**, com a frase de que
  **não existe switch de PDV** (PDV, mesa e comanda são o canal Presencial).
- Manter a tabela dos **dez tipos** com a coluna "tem aba de taxas?".
- Manter a seção final **Exemplo prático** na ordem em que está (vale novo com taxa e prazo).
- Não publicar nada do `fluxo-codigo.md`.

## Estrutura da página (na ordem do `.md`)
    30|
1. Antes de começar: três telas parecidas
2. Onde fica
3. A tela: é aqui que se liga o canal
4. Cadastrar uma forma (tipos / desconto ou acréscimo)
5. Aba Taxas e Bandeiras
6. Aba TEF (Stone/PayGo)
7. Conferindo o resultado
8. Para o cliente ver na sacola: a outra tela (+ E a terceira tela?)
9. Exemplo prático: aceitar um vale novo
    40|10. Resumo
11. Perguntas frequentes
12. Manuais relacionados

## Anexo — legendas das imagens (na ordem em que aparecem no texto)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|-------|----------------------------------|------|---------|
| 1 | `01-menu-cadastros.png` | com setas | Menu lateral: **Cadastros → Formas Recebimento** |
| 2 | `02-listagem.png` | com setas | A listagem com os switches **Ativo**, **Delivery** e **Presencial** |
    50|| 3 | `03-nova-forma.png` | com setas | O cadastro, aba **Configuração** |
| 4 | `04-ajuste-pagamento.png` | com setas | As cinco opções de **Ajuste no pagamento** |
| 5 | `05-aba-taxas.png` | com setas | Aba **Taxas e Bandeiras**: taxa, desconto fixo e dias para recebimento |
| 6 | `06-aba-tef.png` | com setas | Aba **TEF (Stone/PayGo)** |
| 7 | `07-forma-criada.png` | com setas | A forma nova na listagem, com os dois canais ligados |
| 8 | `08-pagamento-presencial.png` | com setas | A forma aparecendo na hora de receber uma mesa |
| 9 | `09-cardapio-digital-formas.png` | com setas | **Cardápio Digital → Formas Recebimento**: a lista que o cliente vê |
| 10 | `10-cardapio-adicionar.png` | com setas | O modal do cardápio digital, com **Vincular à Forma de Pagamento** |
| 11 | `11-financeiro-formas.png` | contexto | **Financeiro → Formas Pagamento**, a terceira tela |

    60|## Observações de conteúdo

- A imagem **`02-listagem.png`** é a mais importante: publique grande o bastante para o leitor
  distinguir os switches **Delivery** e **Presencial** de cada linha.
- Na imagem **`08`** há uma região borrada de propósito (documento do cliente). Não substituir nem
  tentar "limpar".
- Não afirmar que a forma criada em Cadastros aparece sozinha na sacola do cliente — ela precisa
  do cadastro no **Cardápio Digital**.
- Não publicar nomes de campo da API, rotas, IDs de forma de pagamento nem nomes de arquivo do
  código.
