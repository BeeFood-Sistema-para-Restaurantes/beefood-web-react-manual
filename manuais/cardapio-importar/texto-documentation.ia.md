# texto-documentation.ia.md — #130 Importar cardápio

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Cardápio**, adicione um manual por último chamado
**"Importar cardápio"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/cardapio-importar/cardapio-importar.md`

2. **Imagens (use estas 18, nesta ordem):**
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/01-copiar-ifood-vazio.png`
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/02-modal-url-ifood.png`
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/03-importacao-na-fila.png`
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/04-importacao-em-andamento.png`
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/05-importacao-concluida.png`
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/06-produtos-importados.png`
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/07-grupos-opcoes-importados.png`
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/08-digitalizar-arquivo.png`
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/09-digitalizar-revisao.png`
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/10-digitalizar-assistente.png`
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/11-digitalizar-confirmar.png`
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/12-digitalizar-resultado.png`
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/13-excel-passo1.png`
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/14-excel-mapeamento.png`
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/15-excel-resultado.png`
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/16-clonagem-credenciais.png`
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/17-clonagem-previa.png`
   - `beefood-web-react-manual/manuais/cardapio-importar/imagens-tratadas/18-clonagem-confirmacao.png`

**NÃO leia outros arquivos** (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`,
`capturar-*.py`, `conferir-setas.py`, `diagnostico.py`, `imagens-puras/`).

- Faça a apresentação das imagens **igual** ao menu **"Abrir Caixa"**.
- pt-BR, didático; o leitor é o **lojista**, e muitas vezes um lojista **novo**, montando o
  cardápio no primeiro dia de sistema.
- **A página é uma só, com quatro caminhos.** Não quebrar em quatro manuais: a decisão de qual
  usar é metade do valor da página, e a tabela *Qual caminho é o seu* tem de ficar logo no
  começo, antes de qualquer passo.
- Não publicar o rodapé de referências internas.
- Palavras que o leitor vai buscar e que devem sobreviver na página: *importar cardápio*,
  *copiar cardápio do iFood*, *importar cardápio do iFood*, *trazer cardápio do iFood*,
  *link do iFood*, *digitalizar cardápio*, *cardápio por foto*, *importar cardápio em PDF*,
  *importar produtos por Excel*, *importar planilha de produtos*, *template de importação*,
  *importar complementos*, *clonar cardápio*, *copiar cardápio de outra empresa*,
  *produtos duplicados depois de importar*, *NCM com zero à esquerda*,
  *desfazer importação de cardápio*.

## Estrutura da página (na ordem do `.md`)

1. Título e abertura — os **quatro** caminhos, todos terminando em *Cardápio → Produtos*, e o
   aviso de que todos **somam** ao cardápio atual.
2. **Qual caminho é o seu** — a tabela de decisão (o que você tem → qual caminho → onde fica → o
   que ele traz), mais as duas frases que ela não cabe: a combinação iFood + outro caminho, e o
   fato de **nenhum** caminho conferir duplicata.
3. Antes de começar — permissão por item de menu, qual cardápio recebe, a ausência de desfazer e
   o link do iFood em mãos.
4. **Caminho 1 — Copiar do iFood** (Passos 1 a 6): o menu e o estado vazio, o link e o cardápio
   destino, a fila, o andamento, o *Concluído* e a conferência do cardápio (duas imagens de
   contexto, sem seta).
5. **Caminho 2 — Copiar de Imagem** (Passos 7 a 11): o envio com formatos e instruções
   adicionais, a revisão do que a IA leu, o **Assistente do Cardápio**, o *Confirmar envio* e o
   resumo do que foi cadastrado.
6. **Caminho 3 — Importar por planilha Excel** (Passos 12 a 14): o botão **Importar**, os avisos
   amarelos, o **BAIXAR TEMPLATE** e a tabela das colunas, o mapeamento automático e o resultado
   linha por linha.
7. **Caminho 4 — Clonar e importar** (Passos 15 a 17): as credenciais da **outra** empresa, a
   prévia com o aviso de duplicação, os impostos opcionais e a confirmação.
8. **Depois de importar, confira isto** — seis itens, com destaque para o **produto duplicado que
   é opção de combo**.
9. Quando algo não funciona — tabela sintoma/verificação.
10. Perguntas frequentes.
11. Precisa de ajuda? e Onde continuar.

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Caminho | Tipo | Legenda |
|---|---|---|---|---|
| 1 | `01-copiar-ifood-vazio.png` | iFood | com setas (2) | O item **Copiar do iFood** no submenu **Cardápio** e o botão único da tela, antes da primeira importação |
| 2 | `02-modal-url-ifood.png` | iFood | com setas (4) | O formulário: **URL do Restaurante no iFood**, o botão de colar, o **Cardápio Destino** e o **CONFIRMAR (F2)** |
| 3 | `03-importacao-na-fila.png` | iFood | com setas (2) | O cartão **Aguardando processamento…** com o selo **Na fila — posição N** e o botão **Cancelar** |
| 4 | `04-importacao-em-andamento.png` | iFood | com setas (3) | A extração em curso: a mensagem que gira, o contador de **produtos processados** e a porcentagem |
| 5 | `05-importacao-concluida.png` | iFood | com setas (2) | O selo **Concluído** e o contador igualado (**41/41 produtos processados**) |
| 6 | `06-produtos-importados.png` | iFood | contexto | **Cardápio → Produtos** com os setores e as fotos que vieram do iFood |
| 7 | `07-grupos-opcoes-importados.png` | iFood | contexto | **Cardápio → Grupo de Opções** com os complementos importados |
| 8 | `08-digitalizar-arquivo.png` | imagem | com setas (4) | **Digitalize seu Cardápio**: formatos e limite, a miniatura do arquivo, as **Instruções adicionais** e o **Continuar** |
| 9 | `09-digitalizar-revisao.png` | imagem | com setas (4) | A revisão do que a IA leu: itens e categorias, os botões Copiar/baixar/**Excel**, a lista extraída e o **Continuar** |
| 10 | `10-digitalizar-assistente.png` | imagem | com setas (3) | O **Assistente do Cardápio** corrigindo um preço por frase, e o item já alterado na lista |
| 11 | `11-digitalizar-confirmar.png` | imagem | com setas (1) | O diálogo **Confirmar envio** — o ponto sem volta deste caminho |
| 12 | `12-digitalizar-resultado.png` | imagem | com setas (1) | **Cardápio importado com sucesso!** e os cartões de setores, produtos, complementos, grupos e opções |
| 13 | `13-excel-passo1.png` | Excel | com setas (4) | **Importar Produtos via Excel**, passo 1: o botão **Importar**, os avisos de nome/NCM/CEST, a área do arquivo e o **BAIXAR TEMPLATE** |
| 14 | `14-excel-mapeamento.png` | Excel | com setas (5) | O **Mapeamento de colunas**: registros encontrados, **Coluna do Excel**, **Campo do Sistema**, **Exemplo** e o **IMPORTAR (F2)** |
| 15 | `15-excel-resultado.png` | Excel | com setas (4) | O resultado: **Enviados / Sucesso / Falhas**, a coluna **Status** linha por linha e o **FECHAR (ESC)** |
| 16 | `16-clonagem-credenciais.png` | clonagem | com setas (5) | **Clonar e importar**, aba **Cardápio de outra empresa**: usuário e senha do usuário principal da origem |
| 17 | `17-clonagem-previa.png` | clonagem | com setas (5) | A prévia: a empresa de origem, o que existe lá, o aviso **Esta empresa já tem cadastro** e a opção de copiar os impostos |
| 18 | `18-clonagem-confirmacao.png` | clonagem | com setas (1) | A confirmação **Copiar cadastro**, com o botão **COPIAR** |

## Observações de conteúdo

- **O eixo da página é a escolha do caminho.** O leitor chega sabendo o que tem (loja no iFood,
  cardápio no papel, planilha, outra empresa) e não sabendo o nome da tela. A tabela de decisão
  resolve isso em uma olhada, e por isso ela vem antes de qualquer passo.
- **A ordem dos caminhos não é alfabética nem casual:** o iFood vem primeiro porque monta o
  cardápio inteiro, e os outros três entram como complemento. Foi nessa ordem que as capturas
  foram feitas, e as imagens contam essa história — a 06 e a 07 já mostram o cardápio cheio.
- **Manter o aviso de que ninguém confere duplicata.** Vale para os quatro caminhos, é o erro
  mais caro do leitor (importar duas vezes) e não tem desfazer.
- **A explicação do produto duplicado é conteúdo verificado, não suposição.** Depois de importar
  do iFood, 11 nomes vieram em par, e em todos os casos um dos dois cadastros é o item usado como
  **opção de combo**. O manual manda conferir em **Grupo de Opções** antes de excluir, porque
  apagar o cadastro errado deixa o combo sem escolha. Não simplificar isso para "pode apagar".
- **A mensagem rotativa da importação do iFood não é etapa.** São catorze frases que giram a cada
  dez segundos. O manual diz que o andamento de verdade está no contador e na barra — não
  transformar as frases em lista de etapas.
- **O selo que libera o leitor é o verde *Concluído*.** *Finalizando importação…* significa que
  ainda falta gravar cadastro; está na tabela de problemas e não deve sair.
- **A digitalização por imagem é um aplicativo separado**, carregado dentro do painel. Tudo o que
  a página afirma sobre ela veio da observação da tela no ar. Não inventar comportamento que não
  esteja no texto.
- **No Excel, só o nome é obrigatório** e o conselho do NCM/CEST como texto é do próprio aviso da
  tela. Manter os dois.
- **Na clonagem, a credencial é da outra empresa**, e a própria empresa **não** pode ser a
  origem. O subtítulo da tela fala em copiar "entre cardápios desta empresa", o que vale para a
  aba de **área de entrega** — o manual explica a diferença, e essa frase precisa sobreviver.
- As capturas são do sandbox de manuais, com dados de teste: a loja copiada do iFood é pública, e
  o cardápio digitalizado é um cardápio fictício desenhado para a captura. Não há dado de cliente
  em imagem nenhuma.
