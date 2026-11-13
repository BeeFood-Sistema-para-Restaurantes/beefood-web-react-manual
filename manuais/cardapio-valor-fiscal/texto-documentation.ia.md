# texto-documentation.ia.md — #133 Valor fiscal por produto

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Cardápio**, adicione um manual por último chamado
**"Valor fiscal por produto: o que vai para a nota quando não é o preço de venda"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/cardapio-valor-fiscal/cardapio-valor-fiscal.md`

2. **Imagens (use estas 7, nesta ordem):**
   - `beefood-web-react-manual/manuais/cardapio-valor-fiscal/imagens-tratadas/01-cardapio-produtos.png`
   - `beefood-web-react-manual/manuais/cardapio-valor-fiscal/imagens-tratadas/02-produto-opcoes-avancadas.png`
   - `beefood-web-react-manual/manuais/cardapio-valor-fiscal/imagens-tratadas/03-produto-valor-fiscal.png`
   - `beefood-web-react-manual/manuais/cardapio-valor-fiscal/imagens-tratadas/04-complemento-valor-fiscal.png`
   - `beefood-web-react-manual/manuais/cardapio-valor-fiscal/imagens-tratadas/05-lote-selecao.png`
   - `beefood-web-react-manual/manuais/cardapio-valor-fiscal/imagens-tratadas/06-lote-valor-fiscal.png`
   - `beefood-web-react-manual/manuais/cardapio-valor-fiscal/imagens-tratadas/07-lote-resultado.png`

**NÃO leia outros arquivos** (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `capturar.py`,
`conferir-setas.py`, `imagens-puras/`).

- Faça a apresentação das imagens **igual** ao menu **"Abrir Caixa"**.
- A ordem das imagens é a mesma do nome do arquivo, de `01` a `07`.
- A imagem `07` é um **recorte** (faixa larga e baixa) da janela de resultado do lote: ela é
  menor que as outras de propósito e não deve ser esticada.
- pt-BR, didático; o leitor é o **lojista** que monta combo e promoção e precisa que a nota
  detalhe os itens.
- **As tabelas de exemplo são o coração da página.** São números, e número resumido não serve
  para nada: manter todas as linhas e todos os totais.
- Não publicar o rodapé de referências internas.
- Palavras que o leitor vai buscar e que devem sobreviver na página: *valor fiscal*,
  *venda fiscal*, *valor fiscal do produto*, *valor fiscal por produto*,
  *valor diferente do preço de venda na nota*, *brinde na nota fiscal*,
  *brinde não sai na nota*, *combo na nota fiscal*, *como declarar combo na nota*,
  *dividir o valor do combo na nota*, *promoção na nota fiscal*, *NFC-e*, *NF-e*,
  *cupom fiscal*, *Opções avançadas*, *Editar em Lote*, *complemento de cortesia*,
  *não aparece o campo valor fiscal*, *fiscal ativo*.

## Estrutura da página (na ordem do `.md`)

1. Título e abertura — para que serve (combo e promoção com preço fechado), o caso do
   **brinde que não aparecia na nota** e a frase de que o campo **não muda o preço de venda**.
2. Antes de começar — loja com **fiscal ativo**, permissão de editar cardápio, a conta pronta.
3. **O que o campo é — e o que ele não é** — a tabela que separa *Preço de Venda* de *Valor
   fiscal*, com a frase-chave: **o total da nota é sempre igual ao que o cliente pagou**.
4. **Passo 1** — *Cardápio → Produtos*, clicar no nome do produto.
5. **Passo 2** — o **Preço de Venda** no alto e o bloco **Opções avançadas**, que vem fechado.
6. **Passo 3** — preencher o **Valor fiscal**, o texto de apoio e **SALVAR E SAIR (F2)**. Mais
   o aviso de que **R$ 0,00 é o mesmo que vazio**.
7. **Passo 4** — o mesmo campo no **complemento** que sai de brinde (o combo só fecha com ele).
8. **Passo 5** — a tabela da conta do combo: R$ 42,00 + R$ 8,00 + R$ 10,00 = R$ 60,00.
9. **Vários produtos de uma vez** — *Editar em Lote* nas três etapas, incluindo o truque de
   marcar a caixinha com o campo **vazio** para **limpar** em massa.
10. **Mais exemplos** — combo com dois brindes, promoção "2 por R$ 50,00", soma que passa do
    total pago, produto comum, pedido com desconto e taxa de serviço.
11. **Como isso aparece na nota** — o par antes/depois, com o aviso de exemplo fictício.
12. Quando algo não funciona — tabela sintoma/verificação.
13. Perguntas frequentes.
14. Precisa de ajuda? e Onde continuar.

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Seção | Tipo | Legenda |
|---|---|---|---|---|
| 1 | `01-cardapio-produtos.png` | Passo 1 | com setas (1) | A aba **Produtos** do *Cardápio*, com o combo do exemplo; o clique no nome abre o cadastro |
| 2 | `02-produto-opcoes-avancadas.png` | Passo 2 | com setas (2) | O cadastro do produto, com o **Preço de Venda** e o bloco **Opções avançadas** ainda fechado |
| 3 | `03-produto-valor-fiscal.png` | Passo 3 | com setas (3) | O campo **Valor fiscal** preenchido com R$ 42,00, o texto de apoio e **SALVAR E SAIR** |
| 4 | `04-complemento-valor-fiscal.png` | Passo 4 | com setas (3) | O mesmo campo no complemento de cortesia, sem preço de venda e com **R$ 8,00** de valor fiscal |
| 5 | `05-lote-selecao.png` | Vários de uma vez | com setas (3) | A etapa 1 do **Editar em Lote**, com a busca, o contador de selecionados e **PRÓXIMO** |
| 6 | `06-lote-valor-fiscal.png` | Vários de uma vez | com setas (3) | A etapa 2 com a caixinha **Valor fiscal** marcada, o valor digitado e **PROCESSAR** |
| 7 | `07-lote-resultado.png` | Vários de uma vez | com setas (1) | Recorte da etapa 3: **2 sucesso**, com uma linha por produto atualizado |

## Observações de conteúdo

- **A frase que não pode faltar em lugar nenhum:** o total da nota continua **igual ao que o
  cliente pagou**. O campo reparte esse total entre os itens; ele não aumenta nem diminui a
  nota. Quase toda dúvida de lojista nasce de achar o contrário.
- **O brinde é o caso de uso, não um detalhe.** Antes, item de R$ 0,00 simplesmente não
  existia na nota. O valor fiscal do brinde sai **de dentro** do valor do item pago.
- **O campo do brinde fica no cadastro do complemento**, não no do combo. Essa confusão é a
  causa mais provável de "configurei e o brinde continua fora da nota".
- **Vazio e R$ 0,00 são a mesma coisa:** os dois querem dizer "emitir pelo preço de venda".
  Não existe valor fiscal zero, e não há como esconder um item da nota por esse campo.
- **Quando a soma passa do total pago**, o sistema ajusta os itens configurados
  **proporcionalmente**. Não prometer fórmula nem centavo exato: o que o lojista precisa saber
  é que a nota sai certa, mas os valores que ele planejou deixam de valer, e o jeito de ter o
  que planejou é **fechar a soma** no preço pago.
- **A taxa de serviço fica fora** dessa divisão.
- **O campo só aparece para loja com fiscal ativo** — e, no cadastro de complemento, sem
  fiscal ativo não aparece nem o bloco *Opções avançadas*. É a primeira coisa a verificar em
  "não acho o campo".
- **Permissão:** basta a de **editar cardápio**. Não é a permissão de preço. Não escrever que
  precisa de acesso fiscal.
- **Não existe coluna de valor fiscal na lista do cardápio.** Para conferir, abre-se o
  produto. Não prometer filtro nem relatório.
- A seção **Como isso aparece na nota** é **exemplo fictício** e precisa manter o aviso em
  negrito. Nenhuma nota foi emitida para escrever este manual.
- As capturas são do sandbox de manuais, com cardápio fictício (*Combo Tasty Bacon*, *Batata
  Frita Especial One*, *Sprite 350ml*). Não há dado de cliente em imagem nenhuma.
