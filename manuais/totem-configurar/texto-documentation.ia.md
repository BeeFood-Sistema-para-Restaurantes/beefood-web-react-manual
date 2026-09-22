# texto-documentation.ia.md — Totem de Autoatendimento: pôr no ar e configurar

## PROMPT (copiar e colar)

Em **Aplicativos**, adicione um item de menu por último chamado **Totem de
Autoatendimento — Configurar**.

Leia APENAS os arquivos abaixo:

    10|1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/totem-configurar/totem-configurar.md`
2. Imagens (nesta ordem):
   - `beefood-web-react-manual/manuais/totem-configurar/imagens-tratadas/01-aplicativos-card-totem.png`
   - `beefood-web-react-manual/manuais/totem-configurar/imagens-tratadas/02-modal-configuracao-topo.png`
   - `beefood-web-react-manual/manuais/totem-configurar/imagens-tratadas/03-modal-configuracao-meio.png`
   - `beefood-web-react-manual/manuais/totem-configurar/imagens-tratadas/04-modal-configuracao-fim.png`
   - `beefood-web-react-manual/manuais/totem-configurar/imagens-tratadas/05-modal-pagamentos.png`
   - `beefood-web-react-manual/manuais/totem-configurar/imagens-tratadas/06-totem-pagamento.png`
   - `beefood-web-react-manual/manuais/totem-configurar/imagens-tratadas/07-modal-aparencia.png`
   - `beefood-web-react-manual/manuais/totem-configurar/imagens-tratadas/08-totem-espera.png`
    20|   - `beefood-web-react-manual/manuais/totem-configurar/imagens-tratadas/09-modal-download.png`
   - `beefood-web-react-manual/manuais/totem-configurar/imagens-tratadas/10-totem-cardapio-sem-foto-setor.png`
   - `beefood-web-react-manual/manuais/totem-configurar/imagens-tratadas/11-painel-setor-foto.png`
   - `beefood-web-react-manual/manuais/totem-configurar/imagens-tratadas/12-painel-foto-setor-banco.png`
   - `beefood-web-react-manual/manuais/totem-configurar/imagens-tratadas/13-totem-cardapio-com-foto-setor.png`
   - `beefood-web-react-manual/manuais/totem-configurar/imagens-tratadas/14-totem-pedido-feito.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter os **pares painel → tela do cliente** (Pagamentos com a
    30|  tela de pagamento, Aparência com a tela de espera, e o pedido concluído).
- Destacar: a tela **não tem botão Salvar** (grava a cada clique, e os campos de
  texto pouco depois da digitação); **Dinheiro é o único meio que dispensa
  pinpad**; a **URL do totem deve ser tratada como senha**.
- Manter a regra da foto: **foto de setor** muda a coluna da esquerda (texto ×
  miniaturas) e vale a decisão "ou todos ou nenhum"; **produto sem foto** não vira
  lista, vira cartão com imagem quebrada.
- Manter a explicação do desconto por forma de pagamento com os dois caminhos
  exatos (**Cadastros → Formas Recebimento** e **Cardápio Digital → Pagamento
  Online**), porque o totem só aplica o que já está cadastrado.
    40|- **SEO**: manter as palavras de busca do lojista nos títulos e na FAQ (*totem de
  autoatendimento*, *configurar totem*, *URL do totem*, *modo kiosk*, *totem sem
  maquininha*, *pagar em dinheiro no totem*, *foto do setor no totem*). Não trocar
  por sinônimos genéricos nem resumir a FAQ.
- Não publicar o rodapé interno.

## Estrutura da página

1. Antes de começar
2. Onde fica a configuração do totem
    50|3. Aba Configuração — como o pedido funciona (meio de consumo e impressão; nota
   fiscal, observação, idioma e identificação; senha, acréscimo e mensagem final)
4. Aba Pagamentos — o que o cliente pode usar para pagar (+ como o cliente vê)
5. Aba Aparência — a cara do aparelho (+ como o cliente vê)
6. Aba Cardápios — totem que vende por mais de uma loja
7. Aba Download — pôr o totem no ar
8. A foto do setor muda o layout do cardápio (sem foto, onde cadastrar, com foto)
9. O pedido concluído: mensagem final e senha
10. Problemas comuns
11. Perguntas frequentes
    60|12. Manuais relacionados

## Anexo — legendas

| Ordem | Arquivo | Tipo | Legenda |
|-------|---------|------|---------|
| 1 | `01-aplicativos-card-totem.png` | com setas | O card do Totem, na faixa Presencial de Aplicativos |
| 2 | `02-modal-configuracao-topo.png` | com setas | Aba Configuração: meio de consumo e impressão |
| 3 | `03-modal-configuracao-meio.png` | com setas | Emissão fiscal, observação, idiomas e identificação do cliente |
| 4 | `04-modal-configuracao-fim.png` | com setas | Senha do administrador, acréscimo e mensagem final |
    70|| 5 | `05-modal-pagamentos.png` | com setas | Aba Pagamentos: os seis meios e a forma de recebimento |
| 6 | `06-totem-pagamento.png` | com setas | A tela de pagamento do cliente, com o desconto por forma |
| 7 | `07-modal-aparencia.png` | com setas | Aba Aparência: tema, cor, logotipo, capa e slides |
| 8 | `08-totem-espera.png` | com setas | A tela de espera do totem |
| 9 | `09-modal-download.png` | com setas | Aba Download: a URL do totem e o modo kiosk |
| 10 | `10-totem-cardapio-sem-foto-setor.png` | com setas | Setor sem foto: coluna de texto no totem |
| 11 | `11-painel-setor-foto.png` | com setas | O cadastro do setor e o botão ADICIONAR FOTO |
| 12 | `12-painel-foto-setor-banco.png` | com setas | A janela da foto do setor e o Banco de imagens |
| 13 | `13-totem-cardapio-com-foto-setor.png` | com setas | Setor com foto: tira de miniaturas no totem |
| 14 | `14-totem-pedido-feito.png` | com setas | Pedido concluído no totem: mensagem final e senha |
    80|
As imagens 6, 8, 10, 13 e 14 são telas do **aparelho** (1080×1920, retrato) —
publicar sem redimensionar para o texto do totem continuar legível.
