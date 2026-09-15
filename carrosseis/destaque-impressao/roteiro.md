# Carrossel — Destaque na impressão

- **Novidade:** [Destaque na impressão: a bebida não fica mais para trás](https://beefood.app/novidades/destaque-impressao) — Novidade, 15/09/2026
- **Áreas:** Impressão, Cardápio, Aplicativos
- **Manual que aprofunda:** [`manuais/destaque-impressao/`](../../manuais/destaque-impressao/destaque-impressao.md) (#99)
- **Formato:** 4:5 (1080×1350) · 7 slides
- **Gancho:** o problema já tem gambiarra conhecida no salão — canetinha vermelha na
  lata, durex colorido na comanda. A novidade é o sistema fazendo isso sozinho.

## Slides

| # | Arquivo | Tipo | Ideia única | Imagem |
|---|---------|------|-------------|--------|
| 1 | `01-capa.html` | capa | A bebida não fica mais para trás | — |
| 2 | `02-problema.html` | texto | Quem confere a sacola não lê o cupom inteiro | — |
| 3 | `03-onde-ligar.html` | print | Um interruptor abaixo de Descrição | `imagens-puras/03-modal-recorte.png` (captura própria) |
| 4 | `04-em-lote.html` | passos | Todas as bebidas de uma vez, pelo Editar em Lote | — |
| 5 | `05-no-papel.html` | print | O cupom real, com a linha em fundo escuro | `manuais/destaque-impressao/imagens-puras/05-cupom-pedido.png` (reaproveitada do manual) |
| 6 | `06-vale-lembrar.html` | texto | Marcar tudo anula o efeito | — |
| 7 | `07-cta.html` | mockup + CTA | O passo a passo está no manual | `imagens-puras/04-novidades-celular.png` (captura própria) |

## Decisões de roteiro

O slide 5 usa o **cupom de verdade** do manual #99, não um desenho. É a prova
da novidade: quem lê reconhece o próprio cupom e a linha preta salta. Um cupom
desenhado em CSS ficaria mais bonito e valeria menos — existe o modelo
`antes-depois.html` na skill para quando não houver captura real.

O slide 3 é um **recorte** da faixa *Descrição → interruptor*, não o modal
inteiro. Modal de 727 px reduzido para a largura do slide fica ilegível no feed,
e o carrossel não é manual: ele mostra onde fica, não ensina a preencher.

O app do Entregador ficou **fora**. A novidade cita a confirmação de entrega no
aplicativo, mas o emulador Android não sobe no Cloud Agent
(`MEMORIA-GERAL.md`, seção 6) e carrossel com mockup inventado mente para o
leitor. Quando houver captura de aparelho real, entra como slide 7 e o CTA vira 8.

## Capturas

```bash
# página pública e lista de produtos (sem clique)
python .cursor/skills/carrossel-novidades/scripts/capturar.py destaque-impressao \
    --url https://beefood.app/novidades --nome 01-pagina-novidades --publico
python .cursor/skills/carrossel-novidades/scripts/capturar.py destaque-impressao \
    --rota /cardapio --nome 02-cardapio-produtos

# telas que exigem clique
python carrosseis/destaque-impressao/capturar-telas.py
```

De `imagens-puras/`, os slides usam `03-modal-recorte.png` e
`04-novidades-celular.png`. As outras três ficam como **fonte**: o
`03-modal-produto.png` é de onde o recorte sai, e as duas primeiras são contexto
da rodada de captura. Mesmo princípio dos manuais — a pura é backup, não é a arte.

Produto do exemplo: **Coca Cola 350ml** do setor **Bebidas** (BeeFood3 - Manual).
O sandbox tem dois produtos com esse nome — o script clica pelo cartão do setor,
não pelo nome solto.

## Render

```bash
python .cursor/skills/carrossel-novidades/scripts/renderizar.py \
    carrosseis/destaque-impressao --contato
```

## Legenda para publicar

> A bebida esquecida na sacola tem solução no cadastro, não na canetinha vermelha.
>
> O campo **Destaque na impressão** faz a linha do produto ou do complemento sair
> com fundo escuro e letra clara no Cupom Pedido e na ficha da cozinha — no
> presencial e no delivery.
>
> Liga em **Cardápio → Produtos** (ou Complementos), logo abaixo de Descrição.
> Para marcar todas as bebidas de uma vez, use o **Editar em Lote** com o setor
> filtrado.
>
> Um aviso: use com critério. O destaque só chama atenção quando poucos itens o
> têm — marcar tudo anula o efeito.
>
> Passo a passo completo no manual **Destaque na impressão**, dentro do sistema.
>
> #beefood #restaurante #delivery #gestaoderestaurante #pdv
