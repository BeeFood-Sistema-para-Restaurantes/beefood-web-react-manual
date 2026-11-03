# fluxo-codigo.md — #132 Código de barras envia pedido para PRONTO

> **Não publicar** — material interno. Leitura do `beefood-web-react` em 03/11/2026
> (`86f756f`, *"Adicionou opção de código de barras"*), na cópia de referência
> `~/refs/beefood-web-react`.

## Onde cada peça mora

| Peça | Arquivo |
|---|---|
| A caixinha nova | `src/components/ModalEditarImpressaoLayout.tsx`, aba `texto`, card *Texto padrão Delivery* |
| Decisão de imprimir o código | `src/lib/cupom-pedido-utils.ts`, em `gerarLinhasCupomPedido` |
| Desenho do EAN-13 | `src/lib/impressao-service.ts` (`calcularChecksumEAN13`, `gerarEAN13SVG`) |
| Impressão pelo navegador | `src/lib/impressao-service.ts` (`imprimirViaIframe`, iframe `beefood-print-frame`) |
| Leitor de teclado | `src/hooks/useLeitorCodigoBarras.ts` |
| Regras puras da leitura | `src/utils/leitorPedidoDelivery.ts` |
| Quem liga o leitor na fila | `src/pages/Delivery.tsx` e `src/hooks/useDeliveryData.ts` |
| Ler e salvar o layout | `src/hooks/useImpressaoLayout.ts` |

A caixinha só é desenhada quando `!isCozinha` — por isso ela não existe no layout do *Cupom
Cozinha*, e o cupom de cozinha nunca imprime código de barras.

## A API

| Operação | Chamada |
|---|---|
| Ler os layouts da empresa | `GET /api/empresa2/impressaoLayout/{empresaID}/{usuarioID}` |
| Salvar um layout | `POST /api/empresa2/impressaoLayout` com o layout inteiro + `empresaID`, `usuarioID`, `usuario`, `log` |
| Mover a situação do pedido | `POST /datasnap/rest/venda2/atualizaSituacaoDelivery` |

O campo novo é `beeCodigoBarrasPronto`, booleano, ao lado do antigo
`beeEntregaCodigoBarras`. Os dois vêm no mesmo objeto de layout, um por tipo
(`DELIVERY`, `SETOR`, `GARCOM`).

## As duas flags não são a mesma coisa

É o ponto que dá forma ao manual. Em `cupom-pedido-utils.ts` o bloco do código de barras
saiu de dentro do `if` do endereço e passou a ter duas condições independentes:

```ts
const imprimirAppEntregador =
  !!config?.beeEntregaCodigoBarras
  && (beetechPlanoID === 5 || entregaAtiva)
  && isDelivery && venda.tipoPedido === 'DELIVERY' && !!endereco && !!venda.preVendaID;

// Flag PRONTO: qualquer pedido do módulo Delivery, sem gate de plano.
const imprimirPronto = !!config?.beeCodigoBarrasPronto && isDelivery && !!venda.preVendaID;

if (imprimirAppEntregador || imprimirPronto) {
  linhas.push({ pularLinha: true });
  linhas.push({ codigoBarras: venda.preVendaID!.toString() });
  linhas.push({ pularLinha: true });
}
```

| | `beeCodigoBarrasPronto` | `beeEntregaCodigoBarras` |
|---|---|---|
| Rótulo na tela | Código de barras envia pedido para PRONTO | Código de Barras App Entrega |
| Condição | `isDelivery` (ou seja, `venda.tipo === 'DELIVERY'`) | `tipoPedido === 'DELIVERY'` **e** endereço |
| Plano | nenhum gate | `beetechPlanoID === 5` ou `entregaAtiva` |
| Quem bipa | a cozinha, na tela Delivery | o entregador, no aplicativo |

O `||` é o que garante que **ligar as duas não imprime dois códigos**: o bloco entra uma vez.

## O número do código

`gerarEAN13SVG` completa com zeros à esquerda e calcula o dígito verificador:

```ts
const base = digits.padStart(12, '0').slice(-12);
// pesos 1 e 3 alternados; dv = (10 - soma % 10) % 10
```

Então o `preVendaID` `62987841` sai como `0000629878417`. As barras são `<rect>` num `<svg>`
— **não há texto embaixo**, e é por isso que o manual avisa que o código não é para ler.

Na volta, `candidatosDoCodigo` (em `leitorPedidoDelivery.ts`) tira o que não é dígito, tira os
zeros à esquerda e, para 12 dígitos ou mais, também oferece o valor **sem o último dígito** —
o verificador. É o que faz o mesmo leitor aceitar o EAN-13 do cupom e o número cru do pedido.

## O leitor

`useLeitorCodigoBarras` escuta `keydown` no `window`, em fase de captura, e **está sempre
ligado** (`ativo = true` nas duas chamadas). Não existe configuração de usuário para ele:

- `minDigitos = 6` — rajada menor que isso é ignorada;
- o buffer zera quando o intervalo entre dois dígitos passa de **50 ms**, o que descarta
  digitação à mão;
- fecha no **Enter** ou num tempo de **100 ms** sem tecla;
- `ignorar()` devolve `true` para `INPUT`, `TEXTAREA`, `SELECT`, `isContentEditable` e
  sempre que existe `[role="dialog"]` ou `[role="alertdialog"]` na página.

Esses dois últimos pontos são a razão do aviso do Passo 4: foco fora dos campos e nenhuma
janela aberta.

## O que acontece ao achar o pedido

`podeMarcarPronto` só aceita `AGUARDANDO` e `PREPARO`. Os três avisos possíveis:

| Situação | Aviso |
|---|---|
| Código não casa com nenhum pedido da lista | *Pedido não encontrado no Delivery* (destrutivo, com `Código lido: …`) |
| Pedido fora de AGUARDANDO/PREPARO | *Pedido #N já está em {rótulo}* |
| Caminho feliz | `handleDrop(null, 'PRONTO', pedido)` e *Pedido #N marcado como Pronto* |

A busca é feita em `pedidosFormatados`, a lista da tela — por isso cupom de outro dia ou de
outra filial cai no primeiro caso.

**A lógica está duplicada** em `src/pages/Delivery.tsx` e em `src/hooks/useDeliveryData.ts`,
com o mesmo corpo. Não é problema do manual, mas quem mexer num lado precisa mexer no outro.

## Fora do navegador

O cupom impresso na impressora térmica não passa por aqui: quem monta é o
`BeeFood3_Impressao.exe`, no Windows, e o código de barras entrou nele na versão **1.0.5.7**
(informação do dono, não verificada por nós). O `layoutImpressaoBridge.ts` reaproveita
`gerarLinhasCupomPedido`, mas é a ponte da APK, não o módulo do Windows.

## Como isto foi conferido no sandbox

O `capturar.py` desta pasta semeia dois pedidos pela rota da própria tela
(`POST /api/venda2/salvar`), um de retirada e um de entrega, e fotografa. A prova de que a
flag nova funciona está no par:

| Flags | Cupom da retirada | Cupom da entrega |
|---|---|---|
| `beeEntregaCodigoBarras=true`, `beeCodigoBarrasPronto=false` | **sem** código | **com** código |
| as duas ligadas | **com** código | **com** código |

Ou seja: o código no cupom de **retirada** só pode ter vindo da flag nova. Depois, bipar
`0000629878417` com o teclado moveu o pedido `62987841` de `PREPARO` para `PRONTO`.
