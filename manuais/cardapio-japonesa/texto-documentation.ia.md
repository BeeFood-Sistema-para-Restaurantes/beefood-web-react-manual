# Prompt para publicar o manual — Cardápio: comida japonesa (#31)

> Cole o texto abaixo na IA de documentação do app, junto com as 14 imagens da pasta
> `imagens-tratadas/`, na ordem da tabela do fim.

---

## Instrução

Publique um manual de usuário final chamado **"Cardápio — comida japonesa"**, na seção
**Cardápio**. Use o conteúdo de `manuais/cardapio-japonesa/cardapio-japonesa.md` como fonte,
**sem reescrever o texto** — ele já está no padrão dos outros manuais publicados.

**Publique depois do manual "Cardápio — fundamentos"**, que este referencia em dois pontos (o
fluxo básico e a Parte 8 da edição em lote). É o **último dos cinco manuais de cardápio**
(#27 fundamentos, #28 hambúrguer, #29 pizza, #30 açaí, #31 japonesa).

### Estrutura a preservar

1. O desafio do combinado (as três exigências e a ideia dos blocos de peças)
2. O exemplo do manual e os pré-requisitos
3. Parte 1 — Cadastrar as peças e os extras
4. Parte 2 — O grupo da montagem (contagem exata)
5. Parte 3 — Os extras e os adicionais
6. Parte 4 — Cadastrar os produtos
7. Parte 5 — Conferir no PDV (combinado, contagem exata, extras, carrinho, temaki)
8. Resumo das contas
9. Dica extra — reajuste em lote
10. Perguntas frequentes
11. Manuais relacionados

### Pontos que NÃO podem se perder

- **Mínimo igual ao Máximo é o que cria a contagem exata.** Com 4 e 4, o cliente precisa escolher
  quatro e não consegue escolher cinco.
- **Cada opção é um bloco de 5 peças**, não uma peça. Com mínimo/máximo 20 seriam vinte cliques
  por combinado; com blocos, são quatro. Essa é a ideia central do manual.
- **A quantidade de peças não existe como campo** — ela vai no **nome** do complemento
  (`Hot Roll (5 peças)`), que é o que aparece no PDV e no carrinho.
- **O Máximo da OPÇÃO é o que permite repetir o mesmo item** (o `0 - 4`). Sem ele, o cliente só
  escolheria quatro peças diferentes.
- **Com o grupo cheio (4/4), o clique é ignorado e não aparece aviso nenhum.** Para trocar uma
  escolha é preciso diminuir no botão **−**.
- **O botão "+" do contador não funciona** nesta versão: para aumentar, clique na linha da opção.
- **Preço fechado = Brinde no grupo de montagem + opções com R$ 0,00.**
- **A descrição do produto faz parte do cadastro** em item que o cliente monta: ela responde
  "quantas peças eu escolho?".
- O grupo **Extras** é o **mesmo** no combinado e no temaki — reaproveitar, não duplicar.
- No reajuste em lote, **filtrar pelo grupo**: as peças precisam continuar em R$ 0,00, senão o
  combinado deixa de ser preço fechado.

### Números conferidos no PDV (não alterar)

| Produto | Situação | Total |
|---------|----------|-------|
| Combinado 20 peças | 2× Hot Roll + Uramaki + Niguiri (4/4) | **R$ 89,00** |
| Combinado 20 peças | + Shoyu extra R$ 2,00 | **R$ 91,00** |
| Temaki Salmão | sozinho | R$ 24,00 |
| Temaki Salmão | + Cream cheese R$ 4,00 | **R$ 28,00** |

---

## Imagens, na ordem

Todas em `manuais/cardapio-japonesa/imagens-tratadas/`.

| # | Arquivo | Tipo | Legenda / o que mostra |
|---|---------|------|------------------------|
| 1 | `01-complementos.png` | setas | Complementos · 1 extra com preço · 2 bloco de peças sem preço |
| 2 | `02-grupo-pecas-detalhes.png` | setas | Grupo da montagem · 1 Obrigatório · 2 Brinde · 3 Mínimo 4 · 4 **Máximo 4** |
| 3 | `03-grupo-pecas-opcoes.png` | setas | Opções · 1 limite da opção `0 - 4` · 2 R$ 0,00 em todas |
| 4 | `04-grupo-pecas-opcao-expandida.png` | setas | Linha da opção aberta · 1 Máximo 4 · 2 Valor zero |
| 5 | `05-grupo-extras-detalhes.png` | setas | Grupo Extras · 1 Normal · 2 Máximo 3 |
| 6 | `06-grupo-adicionais-temaki.png` | setas | Adicionais do temaki · 1 o preço que soma |
| 7 | `07-produto-combinado.png` | setas | Produto · 1 Nome com a quantidade · 2 **Preço fechado R$ 89,00** · 3 Descrição com a regra |
| 8 | `08-produto-grupos.png` | setas | Grupos vinculados · 1 coluna Tipo (Brinde e Normal) · 2 Qtd. Mín. e Qtd. Máx. |
| 9 | `09-pdv-combinado-inicial.png` | setas | PDV aberto · 1 "Escolha 4" e selo Obrigatório · 2 total R$ 89,00 |
| 10 | `10-pdv-contagem-exata.png` | setas | Contagem exata · 1 contador **4/4** com check verde · 2 a mesma peça em **2** · 3 a peça de fora em **0** · 4 total ainda **R$ 89,00** |
| 11 | `11-pdv-combinado-extras.png` | setas | Extras · 1 grupo Extras 1/3 · 2 extra com `+R$` · 3 total **R$ 91,00** |
| 12 | `12-pdv-carrinho.png` | setas | Carrinho · 1 a montagem com `2x` e `1x` · 2 Valor Final R$ 91,00 |
| 13 | `13-pdv-temaki.png` | setas | Temaki · 1 grupo Extras reaproveitado · 2 adicional marcado · 3 total **R$ 28,00** |
| 14 | `14-cardapio-final.png` | contexto | O combinado e o temaki no setor Comida Japonesa |

---

## Observações para quem publica

- Manual **somente desktop**: o cadastro de cardápio é feito no painel web.
- Nenhuma venda foi finalizada: os totais vêm da tela de venda e do carrinho.
- Não há dado de cliente em nenhuma captura.
- **Rodízio não é coberto** aqui — tem tela própria no menu Cardápio e o texto avisa na FAQ.
- Se numa versão futura o botão "+" do contador passar a funcionar, a Parte 5 e a FAQ precisam de
  ajuste.
