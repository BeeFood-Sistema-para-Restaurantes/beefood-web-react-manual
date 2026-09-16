# O que esta skill herda da skill de manual

Os manuais deste repositório resolveram, em quase cem rodadas de captura, uma
lista de problemas que o carrossel encontraria de novo do zero. Este arquivo é o
**mapa** desse conhecimento: ele diz o que abrir e por quê, e não repete o
conteúdo — memória duplicada envelhece em dois lugares e um deles fica errado.

A fronteira é simples: **a skill de manual continua dona de tudo isso.** Esta
skill lê `MEMORIA-GERAL.md`, `CHECKLIST-MANUAIS.md` e as pastas de `manuais/`,
e **não escreve** em nenhum deles.

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
  o carrossel ilustra a tela com selo; o manual, não (ver abaixo).

## O que esta skill acrescenta

O manual e o carrossel querem coisas diferentes da mesma tela:

| | Manual | Carrossel |
|---|--------|-----------|
| Objetivo | ensinar a executar | fazer parar de rolar o feed |
| Imagem | tela cheia, com setas verdes numeradas (`annotate.py`) | recorte da região em mockup que sangra pela borda; para dirigir o olhar, `.realce` em CSS — nunca seta assada no arquivo |
| Texto | passo a passo, tabela nº → campo | publicação escrita a partir do fato, uma ideia por slide |
| Formato | `.md` + PNG anotado | PNG 1080×1350 |
| Fonte da verdade | o código e a tela | o manual e a novidade publicada |
| Tela sem captura | o manual **espera** o print real | o carrossel pode ilustrar, com selo, e registrar o print pendente |

Por isso as capturas do carrossel vivem em `carrosseis/<slug>/imagens-puras/` e
não em `manuais/`: são outro recorte, para outro fim. Quando o print do manual
serve exatamente, o slide **referencia** o arquivo do manual em vez de copiar.

E quando ele **quase** serve, o carrossel captura de novo em vez de desenhar. O
cupom do manual *Destaque na impressão* destaca dois itens porque o manual
precisava ensinar que complemento também destaca; a capa precisava de um. Montar
no sandbox um pedido com só a bebida marcada e imprimir o cupom dele mantém a
imagem sendo impressão de verdade — ver `ganchar_cupom`/`salvar_cupom` no
`capturar.py` desta skill. O arquivo do manual segue intacto.

## Conhecimento próprio desta skill

Fica em [`MEMORIA-CARROSSEIS.md`](MEMORIA-CARROSSEIS.md). Aprendizado de
captura genérica continua indo para a `MEMORIA-GERAL.md` — mas quem escreve lá é
quem está trabalhando no manual, não esta skill.
