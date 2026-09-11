# MEMORIA.md — Taxa de serviço opcional no cupom

Manual **#98**. 11/09/2026. Conta **BeeFood3 - Manual** (`contato@beefood.com.br`).

## Decisões

- O pedido do dono: editar o layout do cupom e pôr a mensagem no **rodapé**.
  Não usamos o print anexo; as cinco imagens foram capturadas de novo no
  Playwright, tema claro.
- A frase gravada no sandbox foi `TAXA DE SERVIÇO OPCIONAL`, nos dois rodapés
  (Delivery e Presencial). O campo Delivery estava com `teste` / `teste2`; o
  cabeçalho Delivery foi alinhado a `BeeFood3 - Manual`.
- `**texto**` **não** vira negrito: `textoParaLinhas` só quebra em `\n` e manda
  `pequeno: true`. Asterisco sairia no papel. Por isso o exemplo vai sem `**`.
- Prova na venda **#940** (Mesa 17, Bruno, 05/09/2026): Batata frita R$ 19,90 +
  Serviço 10% R$ 1,99 = R$ 21,69. O rodapé novo entra em reimpressão — não
  precisa de venda nova.
- Cupom via iframe `#beefood-print-frame` (mesmo truque do #74). BeeImpressão
  abortado (`localhost:1316`) para cair no fallback do navegador.

## Imagens

| Arquivo | Setas | Uso |
|---------|------:|-----|
| `01-aba-layout.png` | 2 | Configuração → Impressão → Layout → Cupom Pedido |
| `02-modal-abas.png` | 1 | Aba Texto Padrão |
| `03-texto-rodape.png` | 3 + moldura | Os dois rodapés + SALVAR E FECHAR |
| `04-detalhe-venda.png` | 2 | Taxa no pedido + impressora do cupom |
| `05-cupom-presencial.png` | 2 | Serviço (10%) e a frase no papel (recorte 0–72%) |

## Estado deixado no sandbox

Rodapé Delivery = rodapé Presencial = `TAXA DE SERVIÇO OPCIONAL`. Cabeçalhos
`BeeFood3 - Manual`. Nada recebido, nada excluído.
