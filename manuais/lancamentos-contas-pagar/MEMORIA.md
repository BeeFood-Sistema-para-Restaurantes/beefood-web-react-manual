# MEMORIA.md — #66 Lançamentos: contas a pagar

## Escopo
Despesa lançada à mão em **Financeiro → Lançamentos → Contas a
pagar**. Prova: **Aluguel do ponto** R$ 800 Pix (única, marcada
paga) e **Máquina de café** 2× R$ 150 Boleto (só a 1/2 no mês
atual).

Não cobre: receita / venda (#67), cadastro de banco / fornecedor /
categoria, DRE, Relatório Pagamentos, taxa da maquininha (#65).

## Origem
Pedido do dono (30/08/2026) depois do merge do #65: fechar o par
**#66 / #67**. Estudo já estava na `MEMORIA-GERAL.md`.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-menu-lancamentos.png` | setas | Menu + aba pagar + Novo |
| `02-novo-dropdown.png` | setas | Despesa / Receita |
| `03-despesa-unico.png` | setas | Aluguel 800, Pix, Único |
| `04-lista-a-vencer.png` | setas | Vencem hoje 800 + cifrão |
| `05-confirmar-pago.png` | setas | Confirmar Pagamento |
| `06-lista-pago.png` | setas | Status Pago + card Pagos |
| `07-despesa-parcelado.png` | setas | Parcelado 2× 150 Boleto |
| `08-lista-parcelas.png` | setas | Máquina 1/2 + aluguel pago |

Sem borrão. 8 imagens. Descrições sem dado pessoal.

## Decisões
- Formas do lançamento = **topo** de Formas Pagamento (Dinheiro,
  Boleto, Pix, Cartão), não as da venda.
- Conta / fornecedor / categoria ficam vazios (0 contas bancárias
  no sandbox).
- Parcelado: o campo vira **Valor Parcela**; a 2/2 cai no mês
  seguinte — o filtro **Este mês** só mostra a 1/2.
- Pagar da lista: último botão da linha (cifrão) → **Confirmar
  Pagamento**.

## Estado deixado no sandbox
- **Aluguel do ponto** — despesa única R$ 800 Pix, **paga** em
  30/08/2026
- **Máquina de café (1/2)** — R$ 150 Boleto, vence 30/08/2026
  (aberta); **(2/2)** no mês seguinte
- Cashback Teste Manual: **R$ 5,00** intacto
- #886/#891 não pagas
- Descontos do #64 e taxas do #65 intactos

## Status
Concluído — aguardando publicação.
