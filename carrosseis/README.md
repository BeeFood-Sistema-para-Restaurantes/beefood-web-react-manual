# Carrosséis de novidades

Arte publicável sobre as novidades do BeeFood: prints reais do sistema, mockups
e slides exportados no tamanho do Instagram.

O **como fazer** está na skill, não aqui:
[`.cursor/skills/carrossel-novidades/SKILL.md`](../.cursor/skills/carrossel-novidades/SKILL.md).
Esta pasta guarda só o que foi produzido.

Os manuais seguem em [`manuais/`](../manuais/), com o foco deles — passo a passo
com setas numeradas para o usuário final. A skill de carrossel **lê** aquele
material e não o altera.

## Índice

| Carrossel | Novidade | Formato | Slides | Entrega |
|-----------|----------|---------|--------|---------|
| [`destaque-impressao/`](destaque-impressao/roteiro.md) | [Destaque na impressão](https://beefood.app/novidades/destaque-impressao) — 15/09/2026 | 4:5 | 8 | [`.zip`](destaque-impressao/entrega/destaque-impressao.zip) · [copy](destaque-impressao/copy-instagram.txt) |

## Estrutura de cada pasta

```
<slug>/
├── roteiro.md            # fato→ângulo→slide e decisões de arte
├── copy-instagram.txt    # legenda, primeiro comentário e texto alternativo
├── capturar-telas.py     # só quando a captura exige clique
├── imagens-puras/        # prints como saíram do navegador, nunca editados
├── slides/               # NN-nome.html (fragmentos de body)
├── png/                  # a arte final, 1080x1350
├── entrega/<slug>.zip    # png + copy, o arquivo que vai para quem publica
└── folha-de-contato.png  # todos os slides numa imagem
```

## Comandos

```bash
SKILL=.cursor/skills/carrossel-novidades/scripts

python $SKILL/pauta.py                          # o que há para contar
python $SKILL/pauta.py --slug <slug>            # material bruto de um item
python $SKILL/capturar.py <slug> --rota /cardapio --nome 02-produtos
python $SKILL/renderizar.py carrosseis/<slug> --contato
python $SKILL/conferir-texto.py <slug>          # o texto foi reescrito?
python $SKILL/empacotar.py <slug>               # zip de entrega (png + copy)
```
