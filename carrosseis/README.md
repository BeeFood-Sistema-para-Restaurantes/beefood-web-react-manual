# Carrosséis de novidades

Arte publicável sobre as novidades do BeeFood: prints reais do sistema, mockups
e slides exportados no tamanho do Instagram.

O **como fazer** está na skill, não aqui:
[`.cursor/skills/carrossel/SKILL.md`](../.cursor/skills/carrossel/SKILL.md).
Esta pasta guarda só o que foi produzido.

Os manuais seguem em [`manuais/`](../manuais/), com o foco deles — passo a passo
com setas numeradas para o usuário final. A skill de carrossel **lê** aquele
material e não o altera.

## Índice

| Carrossel | Novidade | Formato | Slides | Entrega |
|-----------|----------|---------|--------|---------|
| [`destaque-impressao/`](destaque-impressao/roteiro.md) | [Destaque na impressão](https://beefood.app/novidades/destaque-impressao) — 15/09/2026 | 4:5 | 8 | [`.zip`](destaque-impressao/entrega/destaque-impressao.zip) · [copy](destaque-impressao/copy-instagram.txt) |
| [`traducao-cardapio-presencial/`](traducao-cardapio-presencial/roteiro.md) | [Cardápio presencial em inglês e espanhol](https://beefood.app/novidades/traducao-cardapio-presencial) — 16/09/2026 | 4:5 | 7 | [`.zip`](traducao-cardapio-presencial/entrega/traducao-cardapio-presencial.zip) · [copy](traducao-cardapio-presencial/copy-instagram.txt) |
| [`cardapio-capas-destaques/`](cardapio-capas-destaques/roteiro.md) | [Capas, destaques e avisos com imagem e vídeo](https://beefood.app/novidades/cardapio-digital-avisos-banners-capas-midia) — 13/08/2026 | 4:5 | 7 | [`.zip`](cardapio-capas-destaques/entrega/cardapio-capas-destaques.zip) · [copy](cardapio-capas-destaques/copy-instagram.txt) |
| [`desconto-forma-pagamento/`](desconto-forma-pagamento/roteiro.md) | [Desconto ou acréscimo por forma de pagamento](https://beefood.app/novidades/desconto-acrescimo-forma-pagamento) — 17/08/2026 | 4:5 | 7 | [`.zip`](desconto-forma-pagamento/entrega/desconto-forma-pagamento.zip) · [copy](desconto-forma-pagamento/copy-instagram.txt) |

O número de slides é o que a novidade tem de assunto, entre 6 e 8 — não é uma
medida fixa.

## Estrutura de cada pasta

```
<slug>/
├── roteiro.md            # fato→ângulo→ideia de uso→slide, e decisões de arte
├── copy-instagram.txt    # legenda, primeiro comentário e texto alternativo
├── capturar-telas.py     # só quando a captura exige clique
├── midias.json           # só quando a novidade é a mídia que o lojista sobe
├── traducoes.json        # só quando a captura injeta conteúdo na API
├── imagens-puras/        # prints como saíram do navegador, nunca editados
├── slides/               # NN-nome.html (fragmentos de body)
├── png/                  # a arte final, 1080x1350
├── entrega/<slug>.zip    # png + copy, o arquivo que vai para quem publica
└── folha-de-contato.png  # todos os slides numa imagem
```

## Comandos

```bash
SKILL=.cursor/skills/carrossel/scripts

python $SKILL/pauta.py                          # o que há para contar
python $SKILL/pauta.py --slug <slug>            # material bruto de um item
python $SKILL/capturar.py <slug> --rota /cardapio --nome 02-produtos
python $SKILL/renderizar.py carrosseis/<slug> --contato
python $SKILL/conferir-texto.py <slug>          # o texto foi reescrito?
python $SKILL/empacotar.py <slug>               # zip de entrega (png + copy)
```
