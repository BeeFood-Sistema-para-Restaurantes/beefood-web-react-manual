# MEMORIA.md — Taxa de serviço opcional no cupom

Manual **#98**. 11/09/2026. Conta **BeeFood3 - Manual** (`contato@beefood.com.br`).

## Decisões

- O pedido do dono: editar o layout do cupom e pôr a mensagem no **rodapé**.
  Não usamos o print anexo; as imagens foram capturadas no Playwright, tema claro.
- **Delivery não tem taxa de serviço.** A frase vai só no rodapé **Presencial**.
  O rodapé Delivery do sandbox ficou vazio (tinha `teste2` / depois a mesma
  frase; os dois foram limpos).
- QR Code do cardápio foi **desligado** no exemplo para o cupom ficar limpo
  (a frase cola no total, sem o bloco do menu). Código de barras do App
  Entrega ficou como estava.
- `**texto**` **não** vira negrito: `textoParaLinhas` só quebra em `\n`.
- Prova na venda **#940** (Mesa 17): Batata frita R$ 19,90 + Serviço 10%
  R$ 1,99 = R$ 21,69. Reimpressão — sem venda nova.
- Cupom via iframe `#beefood-print-frame` (#74). BeeImpressão abortado.

## Imagens

| Arquivo | Setas | Uso |
|---------|------:|-----|
| `01-aba-layout.png` | 2 | Configuração → Impressão → Layout → Cupom Pedido |
| `02-modal-abas.png` | 1 | Aba Texto Padrão |
| `03-texto-rodape.png` | 2 + moldura | Só o rodapé Presencial + SALVAR |
| `04-detalhe-venda.png` | 2 | Taxa no pedido + impressora do cupom |
| `05-cupom-presencial.png` | 2 | Serviço (10%) e a frase, sem QR (recorte 0–56%) |

## Estado deixado no sandbox

Rodapé Presencial = `TAXA DE SERVIÇO OPCIONAL`. Rodapé Delivery vazio.
`qrCodeCardapioDelivery` desligado. Cabeçalhos `BeeFood3 - Manual`. Nada
recebido, nada excluído.
