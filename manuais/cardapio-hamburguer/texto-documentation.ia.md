# Prompt para publicar o manual — Cardápio: hambúrguer (#28)

> Cole o texto abaixo na IA de documentação do app, junto com as 16 imagens da pasta
> `imagens-tratadas/`, na ordem da tabela do fim.

---

## Instrução

Publique um manual de usuário final chamado **"Cardápio — hambúrguer"**, na seção **Cardápio**.
Use o conteúdo de `manuais/cardapio-hamburguer/cardapio-hamburguer.md` como fonte, **sem
reescrever o texto** — ele já está no padrão dos outros manuais publicados.

**Publique depois do manual "Cardápio — fundamentos"**, que este referencia em dois pontos (o
fluxo básico e a Parte 8 da edição em lote).

### Estrutura a preservar

1. O que este manual acrescenta (a tabela das três perguntas da hamburgueria)
2. O exemplo do manual e os pré-requisitos
3. Parte 1 — Cadastrar os complementos (com preço, sem preço, sem foto)
4. Parte 2 — Grupo do ponto da carne (Brinde + Obrigatório)
5. Parte 3 — Grupo dos adicionais (Normal)
6. Parte 4 — Grupo de retirada (Brinde com mínimo 0)
7. Parte 5 — Cadastrar o hambúrguer
8. Parte 6 — Vincular os três grupos, na ordem certa
9. Parte 7 — Conferir no PDV (obrigatório, bloqueio, Brinde, adicionais, retirada, carrinho)
10. Parte 8 — Reaproveitar os grupos em outro lanche
11. Resumo das contas
12. Dica extra — reajuste em lote
13. Perguntas frequentes
14. Manuais relacionados

### Pontos que NÃO podem se perder

- **Preço zero no complemento é o que garante o preço zero na venda.** Marcar o grupo como
  Brinde declara a intenção, mas o sistema soma o **valor da opção** — se o complemento tiver
  preço, ele ainda aparece na conta.
- **O Obrigatório valida no clique**: o botão Adicionar ao carrinho **continua habilitado** e o
  bloqueio vem como aviso *Seleção obrigatória — Por favor, selecione as opções do grupo "Ponto
  da carne"*. Depois de escolher, o selo vermelho vira um check verde.
- **A ordem dos grupos precisa ser ajustada na mão**: vinculados de uma vez, entram todos com
  ordem 1 e em ordem alfabética. Deixe na ordem da pergunta do atendente.
- **Grupo compartilhado muda todos os produtos vinculados** — para lista própria, clonar.
- **Aqui o preço fica no produto** (R$ 28,00), diferente da pizza, em que o produto vai a
  R$ 0,00 e o preço vem dos sabores.
- **As opções de Brinde aparecem no pedido** e vão para a cozinha; só não somam valor.
- **Foto é opcional** — itens de retirada não precisam.
- No reajuste em lote, **filtrar pelo grupo Adicionais**: os grupos de ponto e retirada precisam
  continuar em R$ 0,00.

### Números conferidos no PDV (não alterar)

| Situação | Total |
|----------|-------|
| Só o X-Burger | R$ 28,00 |
| + Ao ponto (Brinde) | **R$ 28,00** |
| + Bacon R$ 3,00 e Cheddar R$ 2,00 (Normal) | **R$ 33,00** |
| + Sem cebola (Brinde) | **R$ 33,00** |

---

## Imagens, na ordem

Todas em `manuais/cardapio-hamburguer/imagens-tratadas/`.

| # | Arquivo | Tipo | Legenda / o que mostra |
|---|---------|------|------------------------|
| 1 | `01-complementos.png` | setas | Os dez complementos · 1 ponto da carne (com foto, sem preço) · 2 adicional (com preço) · 3 retirada (sem foto, sem preço) |
| 2 | `02-grupo-ponto-detalhes.png` | setas | Grupo Ponto da carne · 1 Obrigatório · 2 Brinde · 3 Mínimo 1 · 4 Máximo 1 |
| 3 | `03-grupo-ponto-opcoes.png` | setas | Opções do grupo Brinde · 1 R$ 0,00 em todas |
| 4 | `04-grupo-adicionais-detalhes.png` | setas | Grupo Adicionais · 1 Normal · 2 Mínimo 0 · 3 Máximo 5 |
| 5 | `05-grupo-adicionais-opcoes.png` | setas | Opções com preço · 1 o valor que soma |
| 6 | `06-grupo-retirar-detalhes.png` | setas | Grupo Retirar ingredientes · 1 Brinde · 2 Mínimo 0 · 3 Máximo 3 |
| 7 | `07-produto-xburger.png` | setas | Produto X-Burger · 1 ADICIONAR FOTO · 2 Preço de Venda R$ 28,00 · 3 Descrição |
| 8 | `08-produto-grupos.png` | setas | Três grupos vinculados · 1 coluna Tipo (Brinde, Normal, Brinde) · 2 ordem e setas de reordenar |
| 9 | `09-pdv-obrigatorio.png` | setas | PDV, grupo obrigatório · 1 selo Obrigatório · 2 "Escolha 1" · 3 total R$ 28,00 |
| 10 | `14-pdv-obrigatorio-bloqueia.png` | setas | Tentativa de adicionar sem escolher · 1 aviso **Seleção obrigatória** |
| 11 | `10-pdv-brinde-nao-soma.png` | setas | Ponto escolhido · 1 check verde · 2 opção sem `+R$` · 3 total ainda **R$ 28,00** |
| 12 | `11-pdv-adicionais.png` | setas | Adicionais somando · 1 contador 2/5 · 2 adicional com `+R$` · 3 total **R$ 33,00** |
| 13 | `12-pdv-retirar.png` | setas | Retirada marcada · 1 Sem cebola · 2 total **R$ 33,00** (igual) |
| 14 | `13-pdv-carrinho.png` | setas | Carrinho · 1 as quatro escolhas listadas, incluindo as de Brinde · 2 Valor Final R$ 33,00 |
| 15 | `15-xsalada-grupos.png` | setas | X-Salada com os grupos compartilhados · 1 Adicionais · 2 Retirar ingredientes |
| 16 | `16-cardapio-final.png` | contexto | Os dois lanches no setor Lanches, com foto |

> A imagem 10 da lista (`14-pdv-obrigatorio-bloqueia.png`) tem número de arquivo fora de
> sequência porque foi capturada depois, quando descobrimos que o Obrigatório valida no clique.
> Publique na posição da tabela, logo após a `09`.

---

## Observações para quem publica

- Manual **somente desktop**: o cadastro de cardápio é feito no painel web.
- Nenhuma venda foi finalizada: os totais vêm da tela de venda e do carrinho.
- Não há dado de cliente em nenhuma captura.
- Se numa versão futura o botão Adicionar ao carrinho passar a ficar desabilitado com grupo
  obrigatório pendente, a Parte 7 precisa de ajuste.
