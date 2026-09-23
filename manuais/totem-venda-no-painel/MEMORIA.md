# MEMORIA.md — #123 O pedido do totem no painel

## Pedido do dono

Terceiro manual do bloco do totem, recortado em 22/09/2026 e aprovado com *"pode
fazer, sem parar"*. No plano:

> "O outro lado do balcão: o pedido do totem chegando no Delivery, no Histórico de
> Vendas (com o filtro de origem), na ficha da cozinha e no Desempenho por
> origem. (…) o manual usa **uma venda nova, feita por nós, paga em Dinheiro**,
    10|> para o leitor ver a venda do dia."

Plano do bloco: [`PLANO-TOTEM.md`](../../.cursor/skills/manual-sistema/references/planos/PLANO-TOTEM.md).

## Escopo

Onde a venda do totem aparece no painel e o que a operação precisa fazer com ela.
Quatro telas: Delivery, card da venda, Histórico de Vendas e Desempenho.

Fica fora: configurar o totem (#121) e o CRM no totem (#122).

    20|## A decisão de produção: uma venda de verdade

O sandbox tinha 32 vendas de totem, mas a mais recente era de **26/08/2026**.
Manual de relatório com dado de mês passado ensina menos: o leitor quer ver a
venda do dia, no lugar em que ele vai olhar.

Então o pedido foi feito no aparelho, com a **técnica do ensaio**:

1. `python3 capturar.py ensaio` — o roteiro inteiro até a tela de pagamento, sem
   tocar em nada que grave. Conferido o resumo de tela impresso pelo script;
2. `VALENDO=1 python3 capturar.py pedido` — a mesma sequência, agora clicando em
    30|   **SIM, VOU PAGAR EM DINHEIRO**. Sem a variável, o script para antes do clique.

**Dinheiro** foi escolhido porque é o único meio que fecha **sem pinpad**, e a
NFC-e está desligada no sandbox — ou seja, nenhum documento fiscal foi emitido.

Resultado: **duas** vendas, não uma. A tela de sucesso fica poucos segundos no ar
e o script tirou quatro fotos em sequência para pegar a senha; na passada
seguinte, o pedido foi refeito para garantir a captura do quadro do Delivery com
o cartão recente. As duas aparecem nas imagens (chip *Totem 2*, *Mostrando 1-2 de
2*) e o manual não finge que é uma só.

    40|As vendas ficaram **abertas e não pagas** no sandbox, como o manual descreve. Nada
foi recebido no caixa nem cancelado.

## Os dados da venda

| Dado | Valor |
|------|-------|
| Venda / Pedido | 1152 / 69 e 1153 / 70, 22/09/2026 |
| Produto | One Burger, 1x R$ 28,00 |
| Forma | Dinheiro, **Não pago** |
| Desconto | R$ 0,28 — 1% da forma *Dinheiro* (Cadastros → Formas Recebimento) |
| Total | R$ 27,72 |
    50|| Mesa | 12 |
| Cliente | Teste Manual, (15) 99999-8888 (o telefone de teste da `MEMORIA-GERAL`) |
| Desempenho, 30 dias | R$ 97,74 · 3 vendas · ticket R$ 32,58 |

## O achado que virou seção

**O mesmo pedido tem três nomes.** No card da venda a origem é
**AutoAtendimento**; no chip do Delivery e no filtro do Histórico é **Totem**; no
Desempenho é **Autoatendimento**. Na leitura do código: `VendaDetalhes.tsx`
imprime `venda.origem` cru (e o valor nem está no mapa de ícones, por isso o ícone
genérico), enquanto os filtros usam o rótulo `'Totem'` dos helpers de origem.

    60|É a causa provável de "minha venda do totem desapareceu" — entrou nos problemas
comuns e na FAQ.

## Imagens (7)

A numeração das tratadas **tem lacunas de propósito**: as puras `01` (tela de
pagamento) e `03` (pedido concluído) foram capturadas por este script, mas são
publicadas no **#121**, onde fazem par com a configuração. Aqui ficam:

| Arquivo | Conteúdo |
|---------|----------|
| `02-totem-dinheiro.png` | O aviso *"o pedido será enviado para a cozinha e deverá ser feito pagamento no caixa"* |
    70|| `04-painel-delivery-pedido-totem.png` | O quadro do Delivery com o chip **Totem** e os cartões com #Mesa 12 |
| `05-painel-pedido-detalhe.png` | O card da venda: Origem **AutoAtendimento**, Dinheiro **Não pago**, ACEITAR PEDIDO |
| `06-painel-historico-filtro-origem.png` | O filtro do Histórico, com o chip **Totem** marcado |
| `07-painel-historico-lista-totem.png` | A lista filtrada: duas vendas, coluna Origem e *Mostrando 1-2 de 2* |
| `08-painel-desempenho-origem.png` | Desempenho → Vendas → Origem, com o chip **Autoatendimento** |
| `09-painel-desempenho-autoatendimento.png` | O mesmo relatório filtrado: R$ 97,74, 3 vendas, ticket R$ 32,58 |

Recortes do `annotate.py`: `PAGINA` (0, 86, 2160, 1290) e `PAGINA_ALTA` (até
1330), com faixa branca no alto; o card da venda usa recorte próprio
(1345, 200, 2160, 1350) com `pad_right`, porque ele é uma coluna estreita à
   80|direita da tela.

O filtro por origem **também serve à privacidade**: sem ele, o quadro do Delivery
e a lista do Histórico mostrariam nome e telefone de outros pedidos do sandbox, e
o repositório é público. Filtrar deixou só o cliente de teste na imagem.

## Decisões de texto

- O manual começa **no aviso do totem**, não no painel: é ele que explica por que
  a venda nasce sem pagamento.
- Seção própria para o **fim do dia** (pedido em dinheiro pendente, nota fiscal
   90|  quando a NFC-e está desligada, senha × número do pedido, desconto da forma).
- A **cozinha/KDS** é citada em uma frase, sem imagem: a loja de teste não tem
  impressora de produção e a tela do KDS abre em outra aba. Melhor uma frase
  honesta do que uma captura inventada.
- A diferença de período entre **Histórico** (15 dias) e **Desempenho** (30 dias)
  está nos problemas comuns, porque os números não batem entre as duas telas.

## Scripts

- `capturar.py` — `ensaio`, `pedido` (com `VALENDO=1`), `delivery`, `detalhe`,
  `historico`, `desempenho`. O **Desempenho é um iframe**: acesso por
   100|  `frame_locator('iframe[src*="relatorios"]')`.
- `annotate.py` — setas em pixels da imagem já recortada.

Manha do aparelho: o teclado numérico **ignora** `click()` por JavaScript (ele
escuta evento de ponteiro) — telefone e mesa precisam de `click(force=True)`.

## Status

Concluído — 7 imagens, manual, fluxo de código e prompt de publicação.
