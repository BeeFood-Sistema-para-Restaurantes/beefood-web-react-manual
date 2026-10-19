# texto-documentation.ia.md — #128 Botão de WhatsApp no cardápio digital

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Cardápio Digital**, adicione um manual por último chamado
**"Botão de WhatsApp no cardápio digital"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/cardapio-digital-botao-whatsapp/cardapio-digital-botao-whatsapp.md`

2. **Imagens (use estas 7, nesta ordem):**
   - `beefood-web-react-manual/manuais/cardapio-digital-botao-whatsapp/imagens-tratadas/01-onde-fica.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-botao-whatsapp/imagens-tratadas/02-ligar-e-telefone.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-botao-whatsapp/imagens-tratadas/03-onde-o-botao-aparece.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-botao-whatsapp/imagens-tratadas/04-formato-do-botao.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-botao-whatsapp/imagens-tratadas/05-previa.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-botao-whatsapp/imagens-tratadas/06-cardapio-computador.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-botao-whatsapp/imagens-tratadas/07-cardapio-celular.png`

**NÃO leia outros arquivos** (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `capturar.py`,
`conferir-setas.py`, `imagens-puras/`).

- Faça a apresentação das imagens **igual** aos outros manuais de **Cardápio Digital**
  (Avisos do cardápio digital, Capas e Destaques).
- pt-BR, didático; o leitor é o **lojista**. As cinco primeiras imagens são do **painel**; as
  duas últimas são do **cardápio digital do cliente** (computador e celular).
- Não publicar o rodapé de referências internas.
- **Não juntar, resumir nem reescrever o bloco de Perguntas frequentes.** São 20 perguntas, e
  várias dizem quase a mesma coisa de propósito: é por elas que a busca do app e o MCP de manual
  encontram esta página quando o lojista pergunta *"como coloco o WhatsApp no cardápio"*.
  Perguntas parecidas fundidas em uma só derrubam exatamente o que elas servem para fazer.
- Palavras que o leitor vai buscar e que devem sobreviver na página: *botão de WhatsApp*,
  *WhatsApp no cardápio digital*, *botão flutuante de WhatsApp*, *falar no WhatsApp*,
  *como colocar WhatsApp no cardápio*, *ativar botão WhatsApp*, *desativar botão WhatsApp*,
  *canto da tela*, *lado da tela*, *cor do botão*, *mensagem pronta*, *{loja}*, *{link}*,
  *salvo automaticamente*, *por filial*, *prévia*.

## Estrutura da página (na ordem do `.md`)

1. Título e abertura — o que o botão faz (o cliente toca, o WhatsApp abre com a mensagem já
   escrita) e para quem serve.
2. **O recado que define o tamanho da página:** o manual monta **uma** configuração — flutuante,
   canto direito, celular e computador. A tela tem muito mais, e explica cada opção nela mesma.
   Esse aviso tem de aparecer na abertura, antes do primeiro passo: é o que justifica a página
   ser curta.
3. Antes de começar — conta com cardápio digital ativo, a aba em liberação por etapas e o número
   de WhatsApp (ou o do cadastro da filial).
4. **Passo 1** — onde fica a aba **Botão WhatsApp**, e o aviso de que **esta tela salva sozinha**
   (não existe botão Salvar; cada mudança já vale para o cliente).
5. **Passo 2** — ligar a chave, o telefone com DDI e DDD, a mensagem pronta e as variáveis
   `{loja}` e `{link}`. Inclui o aviso de que **não é o mesmo WhatsApp do cabeçalho da loja**
   (aquele é o *Exibir WhatsApp*, da aba *Configurações*).
6. **Passo 3** — **Flutuante sobre o cardápio** e as chaves *Celular e tablet* / *Computador*.
7. **Passo 4** — **Pílula**, tamanho 100%, texto do botão, **Direita** e a cor verde.
8. **Passo 5** — a prévia ao lado do formulário, e o que ela simula (*Loja aberta*, *Com itens na
   sacola*) antes de o cliente ver.
9. **Como fica no cardápio digital** — o resultado no computador e no celular, e o aviso de que
   o flutuante sobe quando a barra da sacola aparece.
10. **O que mais a tela oferece** — resumo sem imagem das outras posições, dos formatos, de
    *Quando aparece*, dos dias, do horário e dos canais. É um resumo de propósito: a tela
    explica cada opção embaixo dela.
11. Quando algo não funciona — tabela sintoma/verificação.
12. Perguntas frequentes (20 perguntas — **manter todas**).
13. Precisa de ajuda? e Onde continuar.

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Onde | Tipo | Legenda |
|---|---|---|---|---|
| 1 | `01-onde-fica.png` | painel | com setas (2) | O menu **Cardápio Digital** com a aba **Botão WhatsApp**, e a mesma aba na linha do topo |
| 2 | `02-ligar-e-telefone.png` | painel | com setas (3) | O cartão **Botão de WhatsApp**: a chave de ligar, o **Telefone com DDI e DDD** e a **Mensagem** pronta |
| 3 | `03-onde-o-botao-aparece.png` | painel | com setas (2) | **Onde o botão aparece**, com *Flutuante sobre o cardápio* escolhido, e **Em quais telas** com os dois aparelhos ligados |
| 4 | `04-formato-do-botao.png` | painel | com setas (5) | **Formato** (Pílula), **Tamanho**, **Texto do botão**, **Lado da tela** (Direita) e **Cor do botão** |
| 5 | `05-previa.png` | painel | com setas (3) | A prévia do cardápio: o seletor **Celular / Computador**, o botão com o contorno tracejado da prévia e as chaves de simulação |
| 6 | `06-cardapio-computador.png` | cardápio do cliente | com setas (1) | O botão **Falar no WhatsApp** flutuando no canto inferior direito do cardápio aberto no computador |
| 7 | `07-cardapio-celular.png` | cardápio do cliente | com setas (1) | O mesmo botão no celular, acima da barra de navegação |

## Observações de conteúdo

- **O eixo da página é mostrar o recurso, não esgotar a tela.** O pedido do dono foi explícito:
  *"a ideia é mostrar a funcionalidade e não ensinar fazer 100% das possibilidades… já que a tela
  é auto explicativa"*. Se a página crescer para cobrir as cinco posições e os catorze formatos,
  ela deixa de fazer o que foi pedido. Uma configuração, o resultado nos dois aparelhos, e o
  resto em uma seção de resumo.
- **Manter o aviso do salvamento automático.** É a única tela do cardápio digital sem botão
  Salvar. Quem mexe achando que precisa confirmar já mudou o cardápio do cliente.
- **Manter a separação dos dois WhatsApp.** O ícone entre as redes sociais da loja é o *Exibir
  WhatsApp* da aba *Configurações*; este botão é outro recurso. A própria tela avisa isso numa
  caixa azul, e sem o aviso o leitor acha que ligou duas vezes a mesma coisa.
- **Manter o "por filial".** A configuração é da filial, não da empresa. Quem tem duas lojas
  configura uma e jura que o sistema perdeu a outra.
- **A pergunta de quantos cliques o botão recebeu tem resposta honesta e deve continuar assim.**
  O cardápio registra o clique no Pixel, mas **não existe hoje tela no painel com esse total
  separado**. Não transformar em promessa de relatório.
- **O telefone da imagem é falso de propósito** (`47 99999-8888`, o número do próprio
  *placeholder* do campo), e a conta é a de sandbox. O repositório é público.
