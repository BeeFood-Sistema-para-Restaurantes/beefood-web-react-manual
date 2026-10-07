# texto-documentation.ia.md — Programa de pontos (#126)

## PROMPT (copiar e colar)

Em **Fidelidade (CRM)**, crie um novo item de menu, logo depois de **Cashback — operar**, chamado
**Programa de pontos**.

Leia APENAS os arquivos abaixo (não varra o resto do projeto):

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/programa-pontos/programa-pontos.md`
2. Imagens (nesta ordem):
   - `beefood-web-react-manual/manuais/programa-pontos/imagens-tratadas/01-ativar-programa-pontos.png`
   - `beefood-web-react-manual/manuais/programa-pontos/imagens-tratadas/02-regras-de-acumulo.png`
   - `beefood-web-react-manual/manuais/programa-pontos/imagens-tratadas/03-bonus-e-taxa-de-entrega.png`
   - `beefood-web-react-manual/manuais/programa-pontos/imagens-tratadas/04-recompensas-de-desconto.png`
   - `beefood-web-react-manual/manuais/programa-pontos/imagens-tratadas/05-recompensas-de-produto.png`
   - `beefood-web-react-manual/manuais/programa-pontos/imagens-tratadas/06-cardapio-faixa-pontos.png`
   - `beefood-web-react-manual/manuais/programa-pontos/imagens-tratadas/07-cardapio-perfil-programa-pontos.png`
   - `beefood-web-react-manual/manuais/programa-pontos/imagens-tratadas/08-cardapio-meus-pontos.png`
   - `beefood-web-react-manual/manuais/programa-pontos/imagens-tratadas/09-cardapio-recompensas.png`
   - `beefood-web-react-manual/manuais/programa-pontos/imagens-tratadas/10-cardapio-trocar-pontos.png`
   - `beefood-web-react-manual/manuais/programa-pontos/imagens-tratadas/11-cardapio-resgate-aplicado.png`
   - `beefood-web-react-manual/manuais/programa-pontos/imagens-tratadas/12-banner-pontos-computador.png`
   - `beefood-web-react-manual/manuais/programa-pontos/imagens-tratadas/13-historico-de-pontos.png`
   - `beefood-web-react-manual/manuais/programa-pontos/imagens-tratadas/14-saldo-por-cliente.png`
   - `beefood-web-react-manual/manuais/programa-pontos/imagens-tratadas/15-extrato-do-cliente.png`
   - `beefood-web-react-manual/manuais/programa-pontos/imagens-tratadas/16-adicionar-pontos.png`
   - `beefood-web-react-manual/manuais/programa-pontos/imagens-tratadas/17-fila-de-processamento.png`

NÃO leia outros arquivos (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `cenario.py`,
`capturar-*.py`, `imagens-puras/`).

- Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa".
- pt-BR, didático; o leitor é o **lojista**. A funcionalidade é nova, então a página precisa
  explicar o conceito antes de ensinar os campos.
- Não publicar o rodapé de referências internas.
- Palavras que o leitor vai buscar e que devem sobreviver na página: *programa de pontos*,
  *fidelidade por pontos*, *como ativar pontos*, *pontos por real*, *trocar pontos por desconto*,
  *resgatar pontos*, *produto grátis com pontos*, *pontos expiram*, *cliente não ganhou ponto*,
  *cashback ou pontos*, *migrar cashback para pontos*, *bônus de boas-vindas*.

## Estrutura da página (na ordem do `.md`)

1. Título e abertura — o que é, e **onde funciona**: sistema BeeFood, cardápio digital, totem e
   cardápio digital tablet. Dizer que as telas mostradas são as do **cardápio digital**.
2. Para que serve — pontos criam **meta**, cashback devolve dinheiro; e o aviso de que os dois
   **não convivem no mesmo cardápio**.
3. Antes de começar — permissão (a mesma do Cashback), cardápio digital publicado, a escolha entre
   pontos e cashback, e o crédito que só acontece de madrugada.
4. **1. Ligar o programa** — o caminho no menu, a aba Configuração, a faixa da madrugada, o switch,
   o auto-save sem botão de salvar e o diálogo de exclusividade com o cashback (citado na íntegra).
5. **2. Quanto o cliente ganha, por quanto tempo e em quais canais** — a régua, a validade **por
   crédito**, o canal travado e os cinco opcionais, e o quadro de exemplo.
6. **3. Bônus de boas-vindas e pontos sobre a taxa de entrega** — e a correção do nome: *Entrega
   grátis com pontos* faz **acumular** sobre a taxa, não dar frete grátis.
7. **4. Recompensas de desconto** — cadastro, a equivalência em compras, a escada de três
   recompensas e como se dá entrega grátis de verdade.
8. **5. Recompensas de produto** — cadastro, a linha `Produto #número`, o aviso para **conferir no
   cardápio depois de cadastrar** e a recomendação de escolher produto sem grupo obrigatório.
9. **6. O que o cliente vê no cardápio digital** — faixa amarela, selo no produto, Perfil,
   *Meus pontos* com o extrato (e o motivo que o cliente lê) e a vitrine com *Faltam N pts*.
10. **7. O resgate acontece na sacola** — os dois cartões, RESGATAR/INSUFICIENTE/ADICIONAR, e o
    depois do resgate: REMOVER, as outras apagadas e o total menor.
11. **8. A mesma coisa no computador** — o cartão na coluna da direita, mesmo link.
12. **9. Acompanhar no painel** — Histórico, Saldo por Cliente, o extrato do cliente e a janela de
    crédito manual.
13. **10. A fila de processamento** — os contadores e *Venda sem consumidor*.
14. **11. Trocar de cashback para pontos (e voltar)** — as duas migrações, irreversíveis.
15. **12. Os outros canais** — tabela de canal por canal, **só texto**.
16. Perguntas frequentes.
17. Precisa de ajuda? e Onde continuar.

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|---|---|---|---|
| 1 | `01-ativar-programa-pontos.png` | com setas (5) | A aba **Configuração** do Programa de pontos: o caminho no menu, a faixa do processamento da madrugada, o switch de ativação e os botões de migração |
| 2 | `02-regras-de-acumulo.png` | com setas (5) | O cartão **Regras de acúmulo**: pontos por R$ 1,00, validade em dias, as seis modalidades (a primeira travada) e o quadro de exemplo |
| 3 | `03-bonus-e-taxa-de-entrega.png` | com setas (5) | **Bônus de boas-vindas** e **Entrega grátis com pontos**, com o subtítulo que explica o que o segundo cartão realmente faz |
| 4 | `04-recompensas-de-desconto.png` | com setas (5) | **Recompensas de desconto**: três recompensas cadastradas com a equivalência em compras, a lixeira e o formulário de cadastro |
| 5 | `05-recompensas-de-produto.png` | com setas (5) | **Recompensas de produto**: uma linha mostrando o código do produto, outra mostrando o nome, e o seletor de produto |
| 6 | `06-cardapio-faixa-pontos.png` | com setas (3) | A home do cardápio digital no celular: a faixa **Acumule pontos a cada compra**, o selo de presente no produto resgatável e **Perfil** no rodapé |
| 7 | `07-cardapio-perfil-programa-pontos.png` | com setas (2) | O menu do **Perfil** do cliente identificado, com o item **Programa de pontos** |
| 8 | `08-cardapio-meus-pontos.png` | com setas (6) | A tela **Meus pontos**: o saldo, o extrato com *Ganhou* e *Usou*, e o motivo digitado no painel aparecendo para o cliente |
| 9 | `09-cardapio-recompensas.png` | com setas (6) | A vitrine **O que você pode ganhar**: as regras em uma frase, as recompensas e os selos **Disponível** e **Faltam 59 pts** |
| 10 | `10-cardapio-trocar-pontos.png` | com setas (6) | A sacola com os dois cartões de pontos: o ganho deste pedido e as recompensas, com **RESGATAR**, **INSUFICIENTE** e **ADICIONAR** |
| 11 | `11-cardapio-resgate-aplicado.png` | com setas (5) | A sacola depois do resgate: **REMOVER**, as outras recompensas apagadas e o total caindo de R$ 29,00 para R$ 19,00 |
| 12 | `12-banner-pontos-computador.png` | com setas (2) | O mesmo cardápio no computador: o programa vira um cartão na coluna da direita |
| 13 | `13-historico-de-pontos.png` | com setas (4) | A aba **Histórico**: busca, filtro por tipo, a coluna **Tipo** (Ganhou, Usou, CANCELOU, Migrou) e a coluna **Pontos** com sinal |
| 14 | `14-saldo-por-cliente.png` | com setas (4) | A aba **Saldo por Cliente**: os quatro totais, **Novo Saldo**, o saldo de cada cliente e o olho que abre o extrato |
| 15 | `15-extrato-do-cliente.png` | com setas (5) | O extrato de um cliente no painel lateral: saldo, **ADICIONAR/REMOVER/TRANSFERIR**, os três cartões de resumo e o motivo à vista |
| 16 | `16-adicionar-pontos.png` | com setas (4) | A janela **Adicionar pontos**: pontos, validade opcional, o **Motivo** obrigatório e **CONFIRMAR (F2)** |
| 17 | `17-fila-de-processamento.png` | com setas (4) | A aba **Fila Processamento**: os quatro contadores, a coluna **Status** e a mensagem *Venda sem consumidor* |

## Observações de conteúdo

- **A seção 5 avisa que a recompensa de produto pode não aparecer para o cliente.** Não é
  pessimismo: foi medido, e está documentado no `fluxo-codigo.md`. Se o produto corrigir o
  desencontro de código do produto, **esse aviso sai da página** — e só ele, o resto da seção
  continua valendo.
- **Manter o aviso de que o Motivo é lido pelo cliente** nas seções 6 e 9 e no FAQ. É a informação
  deste manual com maior chance de evitar um constrangimento real.
- **Manter o nome errado explicado, não corrigido.** O cartão se chama *Entrega grátis com pontos* e
  faz outra coisa; a página explica a diferença em vez de inventar um nome melhor, porque o leitor
  vai procurar pelo rótulo que está na tela dele.
- **A seção 12 é só texto, de propósito.** Totem e tablet não têm tela de pontos para fotografar, e
  tabela de canal por canal se lê melhor que print de tela sem o recurso.
- As capturas são do cardápio de demonstração `menu.beefood.com.br/beefood3` com o cliente de teste
  **(15) 99999-8888**. Telefones de outros clientes saem **borrados na imagem pura**, porque o
  repositório é público.
