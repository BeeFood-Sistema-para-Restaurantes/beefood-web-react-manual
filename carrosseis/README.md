# Carrosséis

Arte publicável sobre o BeeFood: telas reais do sistema, mockups e slides
exportados no tamanho do Instagram. Dois gêneros, e a diferença é o leitor —
**novidade** fala com quem já é cliente e **função do sistema** fala também com
quem está escolhendo sistema.

O **como fazer** está na skill, não aqui:
[`.cursor/skills/carrossel/SKILL.md`](../.cursor/skills/carrossel/SKILL.md).
Esta pasta guarda só o que foi produzido.

Os manuais seguem em [`manuais/`](../manuais/), com o foco deles — passo a passo
com setas numeradas para o usuário final. A skill de carrossel **lê** aquele
material e não o altera.

## Índice

A pasta é numerada pela **ordem de entrega**, e o número faz parte do nome: a
listagem do diretório já sai na ordem em que as peças foram publicadas, e o
`.zip` chega ao cliente com o mesmo prefixo. Ordem alfabética não diz nada sobre
um acervo assim, e "entregue" escrito por extenso em toda linha também não.

| # | Carrossel | Gênero | Fonte | Formato | Slides | Entrega |
|---|-----------|--------|-------|---------|--------|---------|
| 1 | [`01-destaque-impressao/`](01-destaque-impressao/roteiro.md) | Novidade | [Destaque na impressão](https://beefood.app/novidades/destaque-impressao) — 15/09/2026 | 4:5 | 8 | [`.zip`](01-destaque-impressao/entrega/01-destaque-impressao.zip) · [copy](01-destaque-impressao/copy-instagram.txt) |
| 2 | [`02-traducao-cardapio-presencial/`](02-traducao-cardapio-presencial/roteiro.md) | Novidade | [Cardápio presencial em inglês e espanhol](https://beefood.app/novidades/traducao-cardapio-presencial) — 16/09/2026 | 4:5 | 7 | [`.zip`](02-traducao-cardapio-presencial/entrega/02-traducao-cardapio-presencial.zip) · [copy](02-traducao-cardapio-presencial/copy-instagram.txt) |
| 3 | [`03-cardapio-capas-destaques/`](03-cardapio-capas-destaques/roteiro.md) | Novidade | [Capas, destaques e avisos com imagem e vídeo](https://beefood.app/novidades/cardapio-digital-avisos-banners-capas-midia) — 13/08/2026 | 4:5 | 7 | [`.zip`](03-cardapio-capas-destaques/entrega/03-cardapio-capas-destaques.zip) · [copy](03-cardapio-capas-destaques/copy-instagram.txt) |
| 4 | [`04-desconto-forma-pagamento/`](04-desconto-forma-pagamento/roteiro.md) | Novidade | [Desconto ou acréscimo por forma de pagamento](https://beefood.app/novidades/desconto-acrescimo-forma-pagamento) — 17/08/2026 | 4:5 | 7 | [`.zip`](04-desconto-forma-pagamento/entrega/04-desconto-forma-pagamento.zip) · [copy](04-desconto-forma-pagamento/copy-instagram.txt) |
| 5 | [`05-dark-kitchen-multimarcas/`](05-dark-kitchen-multimarcas/roteiro.md) | **Função** | [Sistema para Dark Kitchen](https://beefood.com.br/sistema-dark-kitchen/) | 4:5 | 7 | [`.zip`](05-dark-kitchen-multimarcas/entrega/05-dark-kitchen-multimarcas.zip) · [copy](05-dark-kitchen-multimarcas/copy-instagram.txt) |
| 6 | [`06-totem-autoatendimento/`](06-totem-autoatendimento/roteiro.md) | **Função** | [Totem de Autoatendimento](https://beefood.com.br/totem-de-autoatendimento/) — o endereço público é uma casca; a página vem de um app externo | 4:5 | 9 | [`.zip`](06-totem-autoatendimento/entrega/06-totem-autoatendimento.zip) · [copy](06-totem-autoatendimento/copy-instagram.txt) |
| 7 | [`07-cardapio-digital-tablet/`](07-cardapio-digital-tablet/roteiro.md) | **Função** | [Cardápio Digital no Tablet](https://beefood.com.br/cardapio-digital-tablet/) — página inteira, servida pelo próprio site | 4:5 | 9 | [`.zip`](07-cardapio-digital-tablet/entrega/07-cardapio-digital-tablet.zip) · [copy](07-cardapio-digital-tablet/copy-instagram.txt) |

O número de slides é o que o assunto pede, entre 6 e 9 — não é uma medida fixa.
Peça de função não leva data nem pílula de novidade: ela é perene, e pode ser
republicada.

## Estrutura de cada pasta

```
NN-<slug>/
├── roteiro.md            # fato→ângulo→ideia de uso→slide, e decisões de arte
├── copy-instagram.txt    # legenda, primeiro comentário e texto alternativo
├── capturar-telas.py     # só quando a captura exige clique
├── telas/                # tela DESENHADA (HTML), quando o sandbox não tem o cenário
├── midias.json           # só quando a novidade é a mídia que o lojista sobe
├── traducoes.json        # só quando a captura injeta conteúdo na API
├── imagens-puras/        # prints como saíram do navegador, nunca editados
├── slides/               # NN-nome.html (fragmentos de body)
├── png/                  # a arte final, 1080x1350
├── entrega/NN-<slug>.zip # png + copy, o arquivo que vai para quem publica
└── folha-de-contato.png  # todos os slides numa imagem
```

## Comandos

```bash
SKILL=.cursor/skills/carrossel/scripts

python $SKILL/pauta.py                          # o que há para contar
python $SKILL/pauta.py --slug <slug>            # material bruto de um item
python $SKILL/pauta.py --pagina <url>           # pauta de função, de uma página do site
python $SKILL/capturar.py <slug> --rota /cardapio --nome 02-produtos
python $SKILL/renderizar.py carrosseis/<slug> --contato
python $SKILL/desenhar-telas.py <slug>          # telas/*.html -> imagens-puras/*.png
python $SKILL/conferir-texto.py <slug>          # o texto foi reescrito?
python $SKILL/conferir-texto.py <slug> --fonte <url>   # quando a fonte é o site
python $SKILL/empacotar.py <slug>               # zip de entrega (png + copy)
```
