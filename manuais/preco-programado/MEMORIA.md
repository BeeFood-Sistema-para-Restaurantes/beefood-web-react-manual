# MEMORIA.md — #69 Preço Programado

## Escopo
Alterar preço por tabela (dias, horário, canais) sem mudar o cadastro.
Prova no cardápio: Milk Shake de Morango **R$ 15,12 | R$ 18,90 | −20%**.

Não cobre: Exibir/Ocultar, Rodízio, desconto de forma de recebimento
(#64), reajuste permanente do produto.

## Origem
Mesmo pedido do #68 (30/08/2026). Teste de campo passou (~1 min no
cache). Manual feito em seguida, sem perguntar.

Já existia prova antiga: tabela **Preço 24/08 13:35** (50% nos
burgers avulsos) — One Burger `R$ 14,00 | R$ 28,00 | -50%`. Não
mexemos nela.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-lista-preco-programado.png` | setas | Lista + menu + card Happy hour |
| `02-modal-config.png` | setas | Alterar Preço, Ativo, canais, dias |
| `03-modal-produtos.png` | setas | Milk Shake Desc. 20% / R$ 15,12 |
| `04-cel-milkshake.png` | pura | Fonte da tira — card com −20% |
| `04-cardapio-digital.png` | setas | Um celular (o card já é antes×depois) |

## Decisões
- Produto: **Milk Shake de Morango** (R$ 18,90 → 15,12). Não usar
  Combo One Burger.
- Tabela: **Happy hour milk-shake (manual)**, 7 dias, 3 canais.
- Comportamento fixo **Alterar Preço** (`ocultar=1`, `?preco=1`).
  Sem produto de rodízio. Permissão de menu = `rodizio`.
- Desconto em massa: só depois de **selecionar** o produto. Modal
  **Aplicar Desconto** → Porcentagem (%) → `20` → **APLICAR (F2)**;
  depois **SALVAR (F2)** no modal pai.
- A tira tem **1 aparelho**: o próprio card mostra preço novo +
  riscado + %. Não desativamos a tabela para um “antes” separado
  (o hide do #68 já consumiu as duas esperas de cache).
- Cache: até **5 minutos** (pedido do dono).

## Estado deixado no sandbox
- Tabela **Happy hour milk-shake (manual)** **ativa**.
- **Preço 24/08 13:35** intacta (50% burgers).
- Brownie do #68 continua oculto. Cashback R$ 5, #64–#67 intactos.
- Não pagar #886/#891; não gastar cashback do `(15) 99999-8888`.

## Status
Concluído — aguardando publicação.
