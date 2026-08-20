# Prompt para publicar o manual — Cardápio: açaí (#30)

> Cole o texto abaixo na IA de documentação do app, junto com as 15 imagens da pasta
> `imagens-tratadas/`, na ordem da tabela do fim.

---

## Instrução

Publique um manual de usuário final chamado **"Cardápio — açaí"**, na seção **Cardápio**. Use o
conteúdo de `manuais/cardapio-acai/cardapio-acai.md` como fonte, **sem reescrever o texto** — ele
já está no padrão dos outros manuais publicados.

**Publique depois do manual "Cardápio — fundamentos"**, que este referencia em dois pontos (o
fluxo básico e a Parte 8 da edição em lote).

### Estrutura a preservar

1. O problema do açaí (por que um grupo só não resolve)
2. O exemplo do manual e os pré-requisitos
3. Parte 1 — Cadastrar os complementos (incluso sem preço, extra com preço)
4. Parte 2 — Grupo dos inclusos (Brinde com limite)
5. Parte 3 — Grupo dos extras (Normal)
6. Parte 4 — A cobertura, compartilhada pelos três tamanhos (com a aba Produtos)
7. Parte 5 — Um produto por tamanho
8. Parte 6 — Vincular os três grupos em cada tamanho
9. Parte 7 — Conferir no PDV (aberto, limite dos inclusos, extras, cobertura, carrinho)
10. Resumo das contas
11. Dica extra — reajuste em lote
12. Perguntas frequentes
13. Manuais relacionados

### Pontos que NÃO podem se perder

- **Não existe "os 3 primeiros grátis" no BeeFood.** O grupo limita **quantidade**, não valor. A
  regra se traduz com **dois grupos**: um **Brinde** com o limite dos inclusos e um **Normal**
  com os pagos. Este é o assunto central do manual.
- **O que cria o "até 3 inclusos" é o Máximo do grupo Brinde** — ele trava a quarta seleção.
- **O limite não mostra mensagem**: o checkbox simplesmente fica desabilitado. Diferente do grupo
  Obrigatório, que avisa por toast.
- **A lista pode ser maior que o limite** (quatro opções, limite três).
- **Um produto por tamanho** é a recomendação, com os **mesmos grupos compartilhados** — a
  alteração de preço vale para os três de uma vez.
- **A aba Produtos do grupo** mostra em quantos produtos ele está; a faixa amarela avisa antes de
  qualquer alteração.
- No reajuste em lote, **filtrar pelo grupo de extras**: o grupo dos inclusos precisa continuar em
  R$ 0,00. E lembrar que, com grupos compartilhados, o reajuste atinge os três tamanhos.

### Números conferidos no PDV (não alterar)

| Situação | Total |
|----------|-------|
| Açaí 500 ml | R$ 22,00 |
| + Granola, Banana e Paçoca (inclusos) | **R$ 22,00** |
| + Creme de avelã R$ 6,00 e Morango R$ 3,00 | **R$ 31,00** |
| + Calda de chocolate R$ 2,00 | **R$ 33,00** |

---

## Imagens, na ordem

Todas em `manuais/cardapio-acai/imagens-tratadas/`.

| # | Arquivo | Tipo | Legenda / o que mostra |
|---|---------|------|------------------------|
| 1 | `01-complementos.png` | setas | Complementos do açaí · 1 incluso sem preço · 2 extra com preço |
| 2 | `02-grupo-inclusos-detalhes.png` | setas | Grupo dos inclusos · 1 Brinde · 2 Mínimo 0 · 3 **Máximo 3** |
| 3 | `03-grupo-inclusos-opcoes.png` | setas | Opções · 1 R$ 0,00 em todas |
| 4 | `04-grupo-extras-detalhes.png` | setas | Grupo dos extras · 1 Normal · 2 Mínimo 0 · 3 Máximo 5 |
| 5 | `05-grupo-extras-opcoes.png` | setas | Opções · 1 o preço que soma |
| 6 | `06-grupo-cobertura-detalhes.png` | setas | Grupo Cobertura · 1 aviso de grupo compartilhado · 2 Normal |
| 7 | `14-grupo-produtos-3x.png` | setas | Aba Produtos do grupo · 1 contador **Produtos (3)** · 2 os três tamanhos |
| 8 | `07-produto-acai500.png` | setas | Produto · 1 Nome com o tamanho · 2 Preço do tamanho |
| 9 | `08-produto-grupos.png` | setas | Grupos vinculados · 1 coluna Tipo · 2 Qtd. Mín. e Qtd. Máx. |
| 10 | `09-pdv-inicial.png` | setas | PDV aberto · 1 "Escolha 0 a 3" · 2 total R$ 22,00 |
| 11 | `10-pdv-inclusos-limite.png` | setas | Limite dos inclusos · 1 contador **3/3** · 2 quarta opção **bloqueada** · 3 total ainda R$ 22,00 |
| 12 | `11-pdv-extras.png` | setas | Extras somando · 1 contador 2/5 · 2 extra com `+R$` · 3 total **R$ 31,00** |
| 13 | `12-pdv-cobertura.png` | setas | Cobertura · 1 calda escolhida · 2 total **R$ 33,00** |
| 14 | `13-pdv-carrinho.png` | setas | Carrinho · 1 as seis escolhas listadas · 2 Valor Final R$ 33,00 |
| 15 | `15-cardapio-final.png` | contexto | Os três tamanhos no setor Açaí, com foto |

> As imagens `14-...` e `07-...` aparecem fora da ordem numérica do arquivo porque a aba
> Produtos do grupo foi capturada junto com o grupo Cobertura. Publique na ordem da tabela.

---

## Observações para quem publica

- Manual **somente desktop**: o cadastro de cardápio é feito no painel web.
- Nenhuma venda foi finalizada: os totais vêm da tela de venda e do carrinho.
- Não há dado de cliente em nenhuma captura.
- Açaí **por peso** não é coberto aqui (usa balança) — o texto já avisa na FAQ.
