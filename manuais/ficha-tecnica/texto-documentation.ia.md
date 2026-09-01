# texto-documentation.ia.md — Ficha Técnica

## PROMPT (copiar e colar)

Em **Estoque**, crie um novo item de menu por último chamado **Ficha Técnica**.

Leia APENAS os arquivos abaixo (não varra o resto do projeto):

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/ficha-tecnica/ficha-tecnica.md`
2. Imagens (nesta ordem), em `beefood-web-react-manual/manuais/ficha-tecnica/imagens-tratadas/`:
   `01-insumos-lista.png`, `02-insumo-cadastro.png`, `03-insumo-estoque.png`,
   `04-ficha-adicionar.png`, `05-ficha-completa.png`, `06-produto-custos.png`,
   `07-ficha-adicional-carne.png`, `08-ficha-adicional-bacon.png`, `09-ficha-porcao.png`,
   `10-estoque-coluna-ficha.png`, `11-pdv-dois-adicionais.png`, `12-movimentacoes-venda.png`,
   `13-ficha-editar-linha.png`, `14-ficha-remover.png`, `15-insumo-receita.png`

NÃO leia outros arquivos (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `capturar.py`,
`imagens-puras/`).

- Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa".
- pt-BR, didático; destacar os campos obrigatórios; manter os quadros de atenção (o de conversão
  de unidade e o de custo em dobro) em destaque.
- Não publicar nada do `fluxo-codigo.md`.

## Estrutura da página (na ordem do `.md`)

1. O que a ficha técnica faz (custo e baixa de estoque)
2. Não confunda com outras duas telas (Receita/Produção e ficha de consumo)
3. Antes de começar
4. Parte 1 — Cadastrar os insumos (+ quadro **gramas ÷ 1000**)
5. Parte 2 — Montar a ficha do lanche
6. Parte 3 — Ler o custo e a margem
7. Parte 4 — A ficha do adicional
8. Parte 5 — A porção: granel, litro e embalagem
9. Parte 6 — Ver quem já tem ficha
10. Parte 7 — A prova: vender e ver o estoque baixar
11. Parte 8 — Manter a ficha viva
12. Insumo que vem de uma receita
13. Limites que você precisa conhecer
14. Perguntas frequentes
15. Resumo do exemplo
16. Manuais relacionados

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|-------|----------------------------------|------|---------|
| 1 | `01-insumos-lista.png` | com setas | Lista de insumos em Estoque → Meu Estoque |
| 2 | `02-insumo-cadastro.png` | com setas | Cadastro do insumo: descrição, custo e unidade |
| 3 | `03-insumo-estoque.png` | com setas | Aba Estoque do insumo: controlar estoque e mínimo |
| 4 | `04-ficha-adicionar.png` | com setas | Adicionar um insumo à ficha técnica |
| 5 | `05-ficha-completa.png` | com setas | Ficha completa do lanche com o Custo Total |
| 6 | `06-produto-custos.png` | com setas | Custo, Custo Ficha Técnica, Custo Total e margem |
| 7 | `07-ficha-adicional-carne.png` | com setas | Ficha técnica do adicional Carne 100g |
| 8 | `08-ficha-adicional-bacon.png` | contexto | Ficha técnica do adicional Bacon |
| 9 | `09-ficha-porcao.png` | com setas | Ficha da porção: granel, litro e embalagem |
| 10 | `10-estoque-coluna-ficha.png` | com setas | Coluna Ficha Técnica (Sim/Não) na lista do estoque |
| 11 | `11-pdv-dois-adicionais.png` | com setas | Pedido no PDV com dois adicionais de carne |
| 12 | `12-movimentacoes-venda.png` | com setas | Movimentações geradas pela venda |
| 13 | `13-ficha-editar-linha.png` | com setas | Editar a quantidade de uma linha da ficha |
| 14 | `14-ficha-remover.png` | com setas | Confirmação de remoção de insumo |
| 15 | `15-insumo-receita.png` | com setas | Insumo com custo controlado por uma receita |

## Observações de conteúdo

- O quadro de conversão (gramas ÷ 1000) é o ponto mais importante do manual: mantenha a tabela
  inteira e o alerta de `0,05` × `0,005`.
- Manter o aviso de que **Custo e Custo Ficha Técnica somam**.
- Manter as três lições da Parte 7 (baixa no *Receber*, quantidade multiplica, insumo sem controle
  de estoque não movimenta).
- Não publicar IDs de produto, endpoints nem nomes de arquivo do código.
