# fluxo-codigo.md — #123 O pedido do totem no painel

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `totem-venda-no-painel.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Leitura do `beefood-web-react` em 22/09/2026 (`fcb00ac`), mais a **venda real**
feita no aparelho no mesmo dia (pré-venda 1152 e 1153, pedidos 69 e 70).

## A marca que identifica a venda do totem

`src/utils/cashbackPagamentoConfig.ts` é o arquivo que deixa a regra explícita:

```ts
    10|if (tipo === 'DELIVERY') {
  if (codigoServico === 'A') return filial.cashBackDeliveryTotem === true;
  …
}
```

**Venda de totem = `tipo` DELIVERY + `codigoServico` `'A'`.** Foi por esse par
que as 32 vendas antigas do sandbox foram achadas na API do histórico, antes de
existir a venda nova.

Na interface, o mesmo pedido tem **dois rótulos**, e isso está no manual:

    20|| Tela | Rótulo | Onde está no código |
|------|--------|---------------------|
| Card da venda | **AutoAtendimento** | `VendaDetalhes.tsx` imprime `venda.origem` cru, e o backend manda `AutoAtendimento`. O valor não está no `iconMap`, então cai no ícone genérico de documento |
| Delivery (chip) / Histórico (filtro e coluna) | **Totem** | `deliveryOrigensAlerta.ts`, `origemIcon.ts`, `historicoVendasHelpers.ts` e `Delivery.tsx` mapeiam `'Totem' → autoatendimentoIcon` |
| Desempenho | **Autoatendimento** | rótulo do relatório (iframe de `relatorios.beefood.com.br`) |

Três nomes para a mesma coisa é exatamente o tipo de detalhe que faz o lojista
achar que perdeu a venda — virou linha nos problemas comuns e na FAQ.

## As telas

    30|| Tela | Arquivo | O que o manual usa |
|------|---------|--------------------|
| Delivery | `src/pages/Delivery.tsx` | os chips de filtro (incluindo **Totem** e **Sem pagamento**) e as colunas AGUARDANDO/PREPARO/PRONTO/EM ENTREGA |
| Card da venda | `src/components/VendaDetalhes.tsx` | Tipo, Origem, Cliente, Produtos, Formas de Pagamento, Valor Total, **ACEITAR PEDIDO**, **PAGAMENTO**, *Imprimir Cupom ao aceitar* |
| Histórico | `POST /api/venda2/historicoVendas` | filtro de período, **Origem**, colunas Origem/Nº Pedido/Descontos/Valor Total e o botão Excel |
| Desempenho | iframe `relatorios.beefood.com.br` | menu **Vendas → Origem**, *Filtrar por Origem* e o gráfico por período |

O **Desempenho é um iframe** — para automatizar, é preciso `frame_locator`. Está
registrado aqui porque custou tempo na captura.

## A venda real (22/09/2026)

    40|Pedido montado no aparelho, pago em **Dinheiro**, com a técnica do ensaio (o
roteiro rodou inteiro até a tela de pagamento sem confirmar, e só depois repetiu
com `VALENDO=1`).

| Dado | Valor |
|------|-------|
| Venda / Pedido | 1152 / 69 (e 1153 / 70, a segunda passada) |
| Tipo | Consumo Local (`DELIVERY` + `consumoLocal`) |
| Origem no card | **AutoAtendimento** |
| Produto | One Burger, 1x R$ 28,00 |
| Forma | Dinheiro, **Não pago** |
    50|| Desconto | R$ 0,28 (1% da forma *Dinheiro*, cadastrado em Cadastros → Formas Recebimento) |
| Valor total | R$ 27,72 |
| Mesa | 12 (a configuração do totem está em *Informar Número da Mesa*) |
| Cliente | Teste Manual, (15) 99999-8888 |

O aviso do totem antes de confirmar é literal e explica o resto do manual:

> "Confirmar pagamento em dinheiro? O pedido será enviado para a cozinha e
> deverá ser feito pagamento no caixa."

Daí a venda nascer **Aberto / Não pago** e cair no chip **Sem pagamento**.
    60|
## Desempenho, conferido no dia

Período 23/08 a 22/09/2026, chip **Autoatendimento**: **R$ 97,74**, **3 vendas**,
ticket **R$ 32,58**. São as duas vendas de hoje (R$ 27,72 cada) mais uma de
26/08 (R$ 42,30) que já existia no sandbox. O Histórico, filtrado nos últimos 15
dias, mostra **2 de 2** — a diferença de período entre as duas telas virou linha
nos problemas comuns.

## Cenário anterior do sandbox

   70|Levantado por `POST /api/venda2/historicoVendas` em 21/09/2026 (1.143 vendas de
01/01/2025 a 21/09/2026):

| Origem | Vendas |
|--------|--------|
| Manual | 836 |
| Cardápio Digital | 237 |
| **Totem** | **32** |
| AIQFome | 21 |
| iFood | 8 |
| 99Food | 6 |
    80|| Keeta | 3 |

As 32 do totem estavam em 05 a 08/2026 (nenhuma recente), todas `DELIVERY` +
`BALCAO`, 23 com `consumoLocal` e **mesa nula em todas**. Dava para documentar
relatório, mas não o pedido do dia — por isso a decisão de fazer a venda.

## Fora de escopo

- **KDS**: o manual diz que o pedido segue para a cozinha como qualquer outro, sem
  captura da tela. A loja de teste não tem impressora de produção, e a tela do KDS
  abre em outra aba (`Delivery` → ícone externo).
- **Aceite automático**: o card mostra o botão manual. O chip *Aceite automático*
    90|  do Delivery não foi mexido.
- A venda **não foi recebida no caixa** nem cancelada: ela ficou aberta no
  sandbox, do jeito que o manual descreve.
