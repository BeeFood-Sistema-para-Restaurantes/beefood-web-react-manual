# fluxo-codigo.md — #122 Cupom e cashback no totem

Leitura do `beefood-web-react` em 22/09/2026 (`fcb00ac`), mais o que foi **medido
no aparelho em produção** — o front do totem não está em repositório clonado, e
as frases da tela do cliente vieram de fotografar e ler o DOM, não de código.

Marca no próprio código de quando o totem entrou no CRM
(`CashbackConfiguracaoCRMTab.tsx`):

```ts
    10|// rev: 2026-06-03 — libera Totem em cashback e cupom de desconto
```

## O que o totem pede ao abrir

```
GET /api/venda2/cupomDescontoAtivo/{empresa}/0?tipo=totem
GET /api/totem2/filial/{empresa}/{filial}/0
```

A primeira devolve os cupons; a segunda, a configuração de cashback da filial.
**O totem não grava cupom nem cashback** — ele é leitor.
    20|
Campos por cupom na resposta (medidos): `id`, `titulo`, `subtitulo`,
`beneficio`, `regras[]`, `valorMinimo`, `primeiraCompra`,
`limitarUmUsoCliente`, `formasPagamento[]`, `dependeDosItens`. O array
`regras[]` já vem **em texto pronto** — é o backend que traduz cadastro em
frase, e o aparelho só desenha uma linha por item.

## O cupom no painel

`src/components/crm/ModalEditarCupomCRM.tsx`.

    30|| Bloco | Campo | Observação |
|-------|-------|------------|
| Canais de Visibilidade | `delivery`, `pdv`, `mesas`, **`totem`** | quatro chaves independentes |
| Tipo | `tipoDesc`: `DESC` (Desconto), `FRET` (Frete Grátis), `PROD` (Produto) | — |
| Regras | `valorMinimo`, `limitarUmUsoCliente`, `limitarQtd`/`limitarQtdValor`, `primeiraCompra`, `exibirBeebot`, `apenasRetiradaConsumo`, `naoAplicarEmPromocao`, `validarTelefoneSms` | cada uma tem frase correspondente no totem |
| Avançadas | `formasPagamento[]`, modo de regra (libera × restringe), `setoresLibera`/`produtosLibera`, `setoresRestrito`/`produtosRestrito` | — |

**Frete Grátis desliga o totem, e trava a chave**:

```ts
totem: formData.tipoDesc === 'FRET' ? false : formData.totem
```

    40|O mesmo vale para `pdv` e `mesas`, tanto no render (`disabled`) quanto no
payload de salvamento. É o primeiro item dos problemas comuns do manual.

**SMS.** O texto de apoio da própria tela é a fonte da regra que o manual
repete:

> "O cliente recebe um código por SMS e precisa digitá-lo para usar o cupom.
> Vale apenas no **cardápio digital** e no **totem**, onde o cliente monta o
> próprio pedido — no balcão o cupom é aceito sem confirmação. Consome créditos
> de SMS da sua conta (**Food Marketing → SMS**). Sem saldo disponível, o cupom
> é liberado normalmente, sem validação."

    50|E há um aviso condicional que só aparece quando a combinação não faz sentido:

```tsx
{formData.validarTelefoneSms && !formData.delivery && !formData.totem && (
  … "Este cupom não está disponível no cardápio digital nem no totem, então a
     confirmação por SMS não será aplicada." )}
```

## O cashback no painel

`src/components/crm/cashback/CashbackConfiguracaoCRMTab.tsx` +
`src/hooks/useCashbackCRM.ts`.
    60|
```ts
const MODALIDADES = [
  { key: 'cashBackCDDelivery',      label: 'Pedidos via cardápio digital delivery (padrão)', lockedTrue: true },
  { key: 'cashBackCDPresencial',    label: 'Pedidos presenciais via cardápio digital' },
  { key: 'cashBackDeliveryManual',  label: 'Pedidos manuais delivery' },
  { key: 'cashBackDeliveryMesas',   label: 'Pedidos de mesas / comandas' },
  { key: 'cashBackDeliveryPDV',     label: 'Pedidos via PDV' },
  { key: 'cashBackDeliveryTotem',   label: 'Pedidos via Totem' },   // ← este manual
];
```

    70|Quem amarra a modalidade à venda é `src/utils/cashbackPagamentoConfig.ts`:

```ts
if (tipo === 'DELIVERY') {
  if (codigoServico === 'A') return filial.cashBackDeliveryTotem === true;
  …
}
```

Ou seja: **venda de totem é `tipo = DELIVERY` com `codigoServico = 'A'`** — a
mesma marca que o #123 usa para achar a venda no painel. As flags são lidas do
`config_cache` (`src/utils/configCache.ts`), por filial.
    80|
Percentual: `cashBackPorReal` (único) ou um campo por dia
(`cashBackSegundaPorReal` … `cashBackDomingoPorReal`) com a chave
`cashBackDefinirPorDia`. O dia desmarcado desliga ganho **e** uso — está escrito
na tela em vermelho. Validade: `cashBackExpiraDias`.

## O que foi medido no aparelho (22/09/2026)

Configuração da filial 39202 lida em `/api/totem2/filial`:
`cashBackAtivo = true`, `cashBackDeliveryTotem = true`,
`cashBackPorReal = 0,03`, `cashBackExpiraDias = 35`.
    90|
Telas, com o cliente **Teste Manual** (15) 99999-8888:

| Tela do totem | Texto medido |
|---------------|--------------|
| Identificação | *"Insira seu telefone e ganhe 3% de cashback"* |
| Confirmação | *"Cashback disponível R$ 1,19"* + botão **USAR R$ 1,19**, e o selo **7 CUPONS DISPONÍVEIS** |
| Barra do total | *"Você ganhará de cashback R$ 0,84"* — 3% de R$ 28,00 |

Os sete cupons e as frases que o aparelho escreveu:

   100|| Código | Benefício | Linhas na tela |
|--------|-----------|----------------|
| `FIRST` | 15% | selo **LOGIN** • *Válido apenas para a primeira compra.* |
| `SMS` | 5% | *O pedido precisa ter: Combos (Burger + Porção + Bebida), Bacon.* • *Não vale para itens que já estão em promoção.* • *Válido apenas para retirada ou consumo no local.* • *Válido apenas para pagamento em: PIX Bee, PIX Online, Dinheiro.* • *É preciso confirmar seu telefone por SMS para usar.* |
| `SEMDESCONTO` | 10% | *Não vale para itens que já estão em promoção.* |
| `10%BEBIDA` | 10% | *O desconto vale apenas sobre: Bebidas.* |
| `10%DINHEIRO` | 10% | *Válido apenas para pagamento em: Dinheiro.* |
| `10%SETIVERBOX` | 10% | *O pedido precisa ter: (Box) Batata frita.* |
| `PIX15%` | 15% | *Válido apenas para pagamento em: PIX Bee, PIX Online.* • *É preciso confirmar seu telefone por SMS para usar.* |

O selo **LOGIN** apareceu **só** no `FIRST`, que é o único com
   110|`primeiraCompra`. Os dois cupons com `validarTelefoneSms` não ganharam o selo —
eles pedem o SMS na hora de aplicar. O manual afirma exatamente isso, e nada
além: a regra completa do selo está no front do totem, que não temos.

A tabela "de onde sai cada frase" do manual é a leitura cruzada desta medição
com o cadastro dos sete cupons no painel.

## Fora de escopo

- **Aplicar** o cupom no aparelho: o ensaio parou na tela de confirmação e
  nenhum cupom foi usado, para não sujar o cadastro de uso do CRM.
   120|- O **processamento noturno** do saldo (`Fila Processamento`) não foi medido —
  o manual só repete o aviso da própria tela.
