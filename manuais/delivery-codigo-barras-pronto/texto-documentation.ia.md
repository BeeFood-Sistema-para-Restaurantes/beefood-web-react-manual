# texto-documentation.ia.md — #132 Código de barras no cupom para marcar o pedido como Pronto

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Delivery**, adicione um manual por último chamado
**"Código de barras no cupom para marcar o pedido como Pronto"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/delivery-codigo-barras-pronto/delivery-codigo-barras-pronto.md`

2. **Imagens (use estas 5, nesta ordem):**
   - `beefood-web-react-manual/manuais/delivery-codigo-barras-pronto/imagens-tratadas/01-aba-layout-cupom-pedido.png`
   - `beefood-web-react-manual/manuais/delivery-codigo-barras-pronto/imagens-tratadas/02-caixinha-codigo-barras-pronto.png`
   - `beefood-web-react-manual/manuais/delivery-codigo-barras-pronto/imagens-tratadas/03-cupom-com-codigo-barras.png`
   - `beefood-web-react-manual/manuais/delivery-codigo-barras-pronto/imagens-tratadas/04-fila-antes-da-leitura.png`
   - `beefood-web-react-manual/manuais/delivery-codigo-barras-pronto/imagens-tratadas/05-pedido-em-pronto.png`

**NÃO leia outros arquivos** (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `capturar.py`,
`conferir-setas.py`, `imagens-puras/`).

- Faça a apresentação das imagens **igual** ao menu **"Abrir Caixa"**.
- A ordem das imagens é a mesma do nome do arquivo, de `01` a `05`.
- A imagem `03` é a foto de um **cupom**: estreita e alta. Ela precisa aparecer inteira, sem
  corte no pé, porque o código de barras fica justamente lá.
- pt-BR, didático; o leitor é o **lojista** ou quem está na cozinha, com o cupom na mão e um
  leitor de código de barras ligado no computador.
- **Manual curto, de propósito:** uma caixinha para marcar e uma leitura para fazer.
- Não publicar o rodapé de referências internas.
- Palavras que o leitor vai buscar e que devem sobreviver na página: *código de barras no
  cupom*, *bipar o pedido*, *marcar pedido como pronto*, *pedido pronto*,
  *código de barras envia pedido para PRONTO*, *leitor de código de barras*,
  *leitor de código de barras no delivery*, *cupom com código de barras*,
  *imprimir código de barras no cupom*, *EAN-13 no cupom*, *layout Cupom Pedido*,
  *Texto Padrão*, *Configuração Impressão Layout*, *pedido não encontrado no Delivery*,
  *pedido já está em Pronto*, *Código de Barras App Entrega*.

## Estrutura da página (na ordem do `.md`)

1. Título e abertura — o que a caixinha faz, para quem serve (cozinha com as mãos ocupadas) e
   a frase que diz que vale para **qualquer pedido do Delivery**, inclusive retirada.
2. Antes de começar — acesso ao grupo *Configuração*, um leitor comum de teclado, a tela
   Delivery aberta e o cupom impresso.
3. **Passo 1** — abrir *Configuração → Impressão*, aba **Layout**, linha **Cupom Pedido**.
4. **Passo 2** — aba **Texto Padrão**, marcar a caixinha e **SALVAR E FECHAR**. Mais o aviso de
   que ela **não** é a *Código de Barras App Entrega* logo acima.
5. **Passo 3** — o cupom sai com o código no pé, mostrado num pedido de **retirada**, e o aviso
   de que o código **não tem número embaixo das barras**.
6. **Passo 4** — a tela Delivery aberta, o pedido em *Aguardando* ou *Preparo*, e o aviso de
   clicar numa área vazia antes de bipar.
7. **Passo 5** — bipar: o aviso *Pedido #N marcado como Pronto* e o cartão na coluna *Pronto*.
8. **As duas caixinhas de código de barras** — a tabela que separa esta da *App Entrega*.
9. Quando algo não funciona — tabela sintoma/verificação.
10. Perguntas frequentes.
11. Precisa de ajuda? e Onde continuar.

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Seção | Tipo | Legenda |
|---|---|---|---|---|
| 1 | `01-aba-layout-cupom-pedido.png` | Passo 1 | com setas (2) | A aba **Layout** de *Configuração → Impressão*, com a linha **Cupom Pedido** e o lápis que abre a edição |
| 2 | `02-caixinha-codigo-barras-pronto.png` | Passo 2 | com setas (3) | A aba **Texto Padrão** com **Código de barras envia pedido para PRONTO** marcada e o botão **SALVAR E FECHAR** |
| 3 | `03-cupom-com-codigo-barras.png` | Passo 3 | com setas (2) | O cupom de um pedido de **retirada**, com o código de barras impresso no pé |
| 4 | `04-fila-antes-da-leitura.png` | Passo 4 | com setas (1) | A fila do **Delivery** com o pedido na coluna **PREPARO**, antes da leitura |
| 5 | `05-pedido-em-pronto.png` | Passo 5 | com setas (2) | O aviso **Pedido #33 marcado como Pronto** e o cartão já na coluna **PRONTO** |

## Observações de conteúdo

- **O que o leitor não adivinha é que existem duas caixinhas parecidas, uma embaixo da outra.**
  A de cima (*Código de Barras App Entrega*) é do app do entregador e só imprime em pedido de
  entrega com endereço; a nova imprime em **qualquer** pedido do Delivery e é bipada no
  computador. A tabela que separa as duas é a seção mais importante depois dos passos e não
  deve ser resumida em uma frase.
- **Ligar as duas não imprime dois códigos.** O cupom imprime um código só, que serve para os
  dois usos. Essa frase evita que o lojista desligue uma por medo.
- **O leitor da tela Delivery já vem ligado** e não tem configuração nenhuma. A única
  configuração do recurso é a caixinha do cupom. Não inventar passo de "ativar o leitor".
- **Foco e janela aberta** são a causa de quase toda leitura que "não faz nada": o painel
  ignora a leitura quando o cursor está num campo de texto ou quando existe uma janela na
  frente. Manter o aviso do Passo 4 e as duas linhas correspondentes da tabela de problemas.
- **Só adianta pedido em *Aguardando* ou *Em preparo*.** Pedido que já passou disso recebe
  *Pedido #N já está em …* e não se move — é proteção, não defeito.
- **Digitar o número à mão não funciona**, porque o painel reconhece a rajada rápida de dígitos
  do leitor. Quem não tem leitor arrasta o cartão ou usa o botão *PEDIDO PRONTO*. Não sugerir
  digitação como alternativa.
- **O código guarda o número interno do pedido**, num EAN-13, e não tem dígitos impressos
  embaixo das barras. Não dizer que o número do código é o *Pedido #N* do cupom.
- **Impressora térmica:** o código de barras no cupom que sai da impressora depende do
  **BeeImpressão** atualizado (entrou na versão 1.0.5.7). Isso está na tabela de problemas e
  vem de informação do dono — não transformar em promessa de versão na abertura da página.
- As capturas são do sandbox de manuais. Os clientes das imagens (*Marina Oliveira*, *Rafael
  Dias*) e o endereço são fictícios, criados pelo script de cenário, e os pedidos foram
  cancelados depois: não há dado de cliente real nem telefone em imagem nenhuma.
