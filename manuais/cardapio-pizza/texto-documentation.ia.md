# Prompt para publicar o manual — Cardápio: pizza (#29)

> Cole o texto abaixo na IA de documentação do app, junto com as 15 imagens da pasta
> `imagens-tratadas/`, na ordem da tabela do fim.

---

## Instrução

Publique um manual de usuário final chamado **"Cardápio — pizza"**, na seção **Cardápio**. Use o
conteúdo de `manuais/cardapio-pizza/cardapio-pizza.md` como fonte, **sem reescrever o texto** —
ele já está no padrão dos outros manuais publicados.

**Publique depois do manual "Cardápio — fundamentos"**, que este referencia em três pontos (o
fluxo básico, as quatro formações de preço e a Parte 8 da edição em lote).

### Estrutura a preservar

1. Por que pizza dá mais trabalho (as três coisas que definem uma pizza)
2. **O alerta sobre o Proporcional** — precisa ficar no começo, com destaque
3. A tabela comparativa dos dois modelos
4. O exemplo do manual e os pré-requisitos
5. Parte 1 — Sabores como complementos
6. Parte 2 — Modelo A: Valor da Maior
7. Parte 3 — Modelo B: Proporcional
8. Parte 4 — A borda
9. Parte 5 — Cadastrar a pizza (preço R$ 0,00)
10. Parte 6 — Vincular os grupos
11. Parte 7 — Conferir no PDV (quatro cenários + borda)
12. Resumo das contas
13. Qual modelo escolher
14. Dica extra — reajuste em lote
15. Perguntas frequentes
16. Manuais relacionados

### Pontos que NÃO podem se perder

- **Proporcional soma, não faz média.** Com o preço inteiro em cada sabor, dois sabores de
  R$ 40,00 e R$ 45,00 cobram **R$ 85,00**. Este é o alerta central do manual.
- **Para o Proporcional funcionar**, cada opção precisa ter o preço de **meia pizza**, o grupo
  precisa ter **mínimo 2 / máximo 2** e cada opção precisa ter **máximo 2**.
- **Valor da Maior é a recomendação para quem começa**: cadastro mais simples e o PDV avisa o
  operador sozinho (faixa azul *Regra especial: Será cobrado apenas o valor da opção mais cara
  selecionada*).
- **O produto precisa ter Preço de Venda R$ 0,00.** O preço base sempre soma ao que vem dos
  grupos; com R$ 40,00 no produto e R$ 40,00 no sabor, o cliente paga R$ 80,00.
- **O botão "+" do contador de quantidade não funciona** nesta versão: para repetir o mesmo
  sabor (pizza inteira), clique na **linha do sabor** duas vezes. O "−" funciona.
- **Vincule só um grupo de sabores por produto.**
- **Grupo compartilhado**: alterar a borda vale para todas as pizzas vinculadas (a própria tela
  avisa em faixa amarela).
- No reajuste em lote, **filtrar pelo grupo** antes de aplicar — os dois grupos de sabores têm
  valores diferentes para o mesmo sabor.

### Números conferidos no PDV (não alterar)

| Modelo | Situação | Total |
|--------|----------|-------|
| Valor da Maior | 1 sabor (Calabresa R$ 40,00) | R$ 40,00 |
| Valor da Maior | Calabresa + Portuguesa (R$ 45,00) | **R$ 45,00** |
| Proporcional | Calabresa nas duas metades (R$ 20,00 cada) | **R$ 40,00** |
| Proporcional | Calabresa + Portuguesa (R$ 20,00 + R$ 22,50) | **R$ 42,50** |
| Proporcional | Meio a meio + Borda Catupiry (R$ 8,00) | **R$ 50,50** |
| Erro comum | Proporcional com preço inteiro nos sabores | **R$ 85,00** |

---

## Imagens, na ordem

Todas em `manuais/cardapio-pizza/imagens-tratadas/`.

| # | Arquivo | Tipo | Legenda / o que mostra |
|---|---------|------|------------------------|
| 1 | `01-complementos-sabores.png` | setas | Sabores e bordas cadastrados · 1 preço inteiro do sabor · 2 "Usado 2 vezes" nos dois grupos |
| 2 | `02-grupo-maior-detalhes.png` | setas | Grupo Valor da Maior · 1 formação · 2 Mínimo 1 · 3 Máximo 2 |
| 3 | `03-grupo-maior-opcoes.png` | setas | Opções com preço **inteiro** · 1 Valor · 2 limite `0 - 1` |
| 4 | `04-grupo-prop-detalhes.png` | setas | Grupo Proporcional · 1 formação · 2 Mínimo 2 · 3 Máximo 2 |
| 5 | `05-grupo-prop-opcoes.png` | setas | Opções com preço de **metade** · 1 Valor · 2 limite `0 - 2` |
| 6 | `06-grupo-prop-opcao-expandida.png` | setas | Linha da opção aberta · 1 Máximo 2 · 2 Valor da metade · 3 SALVAR da linha |
| 7 | `07-grupo-borda.png` | setas | Grupo Borda · 1 aviso de grupo compartilhado · 2 limite `0 - 1` · 3 valor que soma |
| 8 | `08-produto-preco-zero.png` | setas | Produto · 1 ADICIONAR FOTO · 2 Setor Pizzas · 3 **Preço de Venda R$ 0,00** |
| 9 | `09-produto-grupos.png` | setas | Grupos vinculados · 1 coluna Tipo (a formação) · 2 Qtd. Mín. e Qtd. Máx. |
| 10 | `10-pdv-maior-1sabor.png` | setas | PDV, Valor da Maior, 1 sabor · 1 "Escolha 1 a 2" · 2 sabor marcado · 3 total R$ 40,00 |
| 11 | `11-pdv-maior-2sabores.png` | setas | PDV, Valor da Maior, meio a meio · 1 aviso azul da regra especial · 2 dois sabores marcados · 3 total **R$ 45,00** |
| 12 | `12-pdv-prop-inteira.png` | setas | PDV, Proporcional, pizza inteira · 1 "Escolha 2" e contador 2/2 · 2 quantidade 2 no mesmo sabor · 3 total R$ 40,00 |
| 13 | `13-pdv-prop-meio.png` | setas | PDV, Proporcional, meio a meio · 1 primeira metade · 2 segunda metade · 3 total **R$ 42,50** |
| 14 | `14-pdv-prop-borda.png` | setas | PDV com borda · 1 Borda Catupiry marcada · 2 total R$ 50,50 |
| 15 | `15-cardapio-final.png` | contexto | As duas pizzas no setor Pizzas, com foto |

---

## Observações para quem publica

- Manual **somente desktop**: o cadastro de cardápio é feito no painel web.
- Os **dois produtos** do manual existem só para comparar os modelos. O texto já diz que na loja
  real se escolhe um e se chama de *Pizza Média* — mantenha esse aviso.
- Nada foi cobrado de verdade: os totais vêm da tela de venda, sem finalizar pedido.
- Não há dado de cliente em nenhuma captura.
- Se o botão "+" do contador for corrigido numa versão futura, a Parte 7 e a FAQ precisam de
  ajuste.
