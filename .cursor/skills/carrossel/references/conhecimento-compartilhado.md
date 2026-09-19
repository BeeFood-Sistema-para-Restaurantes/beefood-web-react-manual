# O que esta skill herda da skill de manual

Os manuais deste repositório resolveram, em quase cem rodadas de captura, uma
lista de problemas que o carrossel encontraria de novo do zero. Este arquivo é o
**mapa** desse conhecimento: ele diz o que abrir e por quê, e não repete o
conteúdo — memória duplicada envelhece em dois lugares e um deles fica errado.

A fronteira é simples: **a skill de manual continua dona de tudo isso.** Ela é a
`manual-sistema`, e os dois arquivos citados aqui moram nela:

- [`.cursor/skills/manual-sistema/references/MEMORIA-GERAL.md`](../../manual-sistema/references/MEMORIA-GERAL.md)
- [`.cursor/skills/manual-sistema/references/CHECKLIST-MANUAIS.md`](../../manual-sistema/references/CHECKLIST-MANUAIS.md)

Esta skill lê os dois e as pastas de `manuais/`, e **não escreve** em nenhum
deles.

## Quando o sandbox não tem o que fotografar

Antes de desenhar a tela em HTML, veja se o cenário pode ser **montado de
verdade**: é o assunto da skill
[`cenario-sandbox`](../../cenario-sandbox/SKILL.md). Ela ensina a descobrir de
onde um campo vem (smoke teste contra a API antes de qualquer SQL) e traz o que
já está medido no BeeFood — a origem do pedido é **derivada** do identificador de
plataforma, qual rota grava o quê, e a janela de horas das telas de fila, que olha
a **criação** do pedido e por isso não aceita pedido de ontem.

Tela real vence desenho sempre que der. O desenho em CSS continua sendo a saída
para o que a sandbox não consegue ter (uma segunda marca, por exemplo), não o
primeiro recurso.

## O que ler na `MEMORIA-GERAL.md`, por assunto

| Preciso de… | Seção | O que está lá |
|-------------|-------|---------------|
| capturar sem print quebrado | **6** | a espera obrigatória (spinner sumir + **5 s**), `storage_state`, `LANG` no processo para hora em 24 h, banner promocional, widget flutuante, pesquisa de NPS, modal que não é `role="dialog"`, lista com rolagem própria |
| entrar no sistema | **5** | conta sandbox **BeeFood3 - Manual**, a tela de login de 2026-08 (campo único), telefone de teste do cardápio, cache de 1 min do cardápio público |
| qualidade de imagem | **3** | resolução das capturas, tira de celulares, medir coordenada por grade de frações, dado pessoal coberto na **imagem pura** |
| não estragar o sandbox | **7** | telas com auto-save, a técnica do ensaio (`DRY=1`) antes de passo irreversível, ler no código o que grava |
| commit | **11** | commit + push após cada ação relevante, mensagem em português |
| o que já foi documentado | **9** e `CHECKLIST-MANUAIS.md` | índice dos manuais; serve para achar a fonte de verdade de uma funcionalidade |

Vale ler também as seções por funcionalidade (`### <manual> — #NN`) quando o
carrossel for daquele assunto: elas guardam o detalhe que não está na tela, do
tipo "opção repetida baixa em dobro" ou "mesa não consome número de pedido".

## Armadilhas do sandbox que já custaram uma rodada de captura

Estão na `MEMORIA-GERAL.md` com o caso completo. Aqui ficam as que mais pegam
quem está capturando para carrossel:

- **Nome de produto repetido.** A base tem 21 nomes duplicados. Clicar por texto
  abre o produto errado; clique pelo cartão dentro do setor.
- **Tela que salva sozinha.** Parâmetros e a configuração do Cashback gravam
  500–800 ms depois do clique, sem botão Salvar. Clicar "só para ver" já altera
  o ambiente.
- **Modal de NPS com o mesmo texto de botão dos outros modais.** Fechar por
  `FECHAR (ESC)` sem filtrar pelo título derruba o modal que você quer
  fotografar. O `limpar()` do `capturar.py` já filtra.
- **Detalhe da venda demora ~12 s** para montar. Ali a espera é de 14 s
  (`--espera 14000`), não de 5.
- **App Android não tem emulador no Cloud Agent.** Testado e documentado: o
  guest nunca inicia. Captura de app vem de **aparelho real**, e o caminho
  confirmado para ela chegar aqui é **zip numa URL pública** — link do arquivo,
  não da pasta, com compartilhamento aberto (seção 6). Enquanto o print não vem,
  o carrossel desenha a tela em CSS copiando o print de produção; o manual, não
  (ver abaixo).

## O que esta skill acrescenta

O manual e o carrossel querem coisas diferentes da mesma tela:

| | Manual | Carrossel |
|---|--------|-----------|
| Objetivo | ensinar a executar | fazer parar de rolar o feed |
| Imagem | tela cheia, com setas verdes numeradas (`annotate.py`) | recorte da região em mockup que sangra pela borda; para dirigir o olhar, `.realce` em CSS — nunca seta assada no arquivo |
| Texto | passo a passo, tabela nº → campo | publicação escrita a partir do fato, uma ideia por slide |
| Formato | `.md` + PNG anotado | PNG 1080×1350 |
| Fonte da verdade | o código e a tela | o manual e a novidade publicada |
| Tela sem captura | o manual **espera** o print real | o carrossel desenha a tela em CSS, copiando layout e fotos do print, e registra no `roteiro.md` o que é desenho |

Por isso as capturas do carrossel vivem em `carrosseis/<slug>/imagens-puras/` e
não em `manuais/`: são outro recorte, para outro fim. **O print do manual entra
como referência, e não como imagem do carrossel** — ele diz quais campos
existem, que valores são reais e qual tela prova o quê, e com isso a captura
própria fica barata. Colado na arte, ele traz o estado e o ruído de que o manual
precisava (ver *o print do manual é referência* na `SKILL.md`).

A única exceção é objeto **sem estado e sem moldura**: o cupom impresso é o mesmo
cupom, e o slide pode apontar para o arquivo do manual.

E quando o print **quase** serve, o carrossel captura de novo em vez de desenhar.
O cupom do manual *Destaque na impressão* destaca dois itens porque o manual
precisava ensinar que complemento também destaca; a capa precisava de um. Montar
no sandbox um pedido com só a bebida marcada e imprimir o cupom dele mantém a
imagem sendo impressão de verdade — ver `ganchar_cupom`/`salvar_cupom` no
`capturar.py` desta skill. O arquivo do manual segue intacto.

## Conhecimento próprio desta skill

- [`MEMORIA-CARROSSEIS.md`](MEMORIA-CARROSSEIS.md) — o histórico: o que foi
  tentado, o que o dono devolveu e por que cada regra existe.
- [`mockups.md`](mockups.md) — a prateleira: aparelhos desenhados, telas
  disponíveis, fotos de produto prontas e as medidas de uso.
- [`roteiro-e-copy.md`](roteiro-e-copy.md) — como o texto é escrito.

Aprendizado de captura genérica continua indo para a `MEMORIA-GERAL.md` — mas
quem escreve lá é quem está trabalhando no manual, não esta skill.
