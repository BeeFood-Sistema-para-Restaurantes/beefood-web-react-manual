# texto-documentation.ia.md — Taxa de serviço opcional no cupom

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `cupom-taxa-servico-opcional.md`
  e das imagens listados neste prompt.
- **Não publique**, em nenhuma seção: rota ou URL de API (`/api/...`); nome de campo,
  de arquivo, de componente, de tabela ou de coluna; bloco de código, JSON ou
  `campo=true`; nem as palavras *backend*, *endpoint*, *payload*, *array*, *bundle*.
  Se a frase só faz sentido para quem programa, ela não entra. Única exceção: a URL
  completa de webhook que o lojista copia para o painel do parceiro.
- Se você leu **qualquer outro arquivo** desta pasta — `fluxo-codigo.md`,
  `MEMORIA.md`, `annotate.py`, `capturar.py` —, **descarte o que leu**: são anotações
  internas de quem produziu o manual.
- Em 23/09/2026 uma página publicada saiu com a rota da API do cupom e dois nomes de
  campo do cashback, porque esta regra não estava aqui em cima.

Em **Impressão**, adicione um item de menu por último chamado **Taxa de serviço
opcional no cupom**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/cupom-taxa-servico-opcional/cupom-taxa-servico-opcional.md`
2. Imagens (nesta ordem):
   - `beefood-web-react-manual/manuais/cupom-taxa-servico-opcional/imagens-tratadas/01-aba-layout.png`
   - `beefood-web-react-manual/manuais/cupom-taxa-servico-opcional/imagens-tratadas/02-modal-abas.png`
   - `beefood-web-react-manual/manuais/cupom-taxa-servico-opcional/imagens-tratadas/03-texto-rodape.png`
   - `beefood-web-react-manual/manuais/cupom-taxa-servico-opcional/imagens-tratadas/04-detalhe-venda.png`
   - `beefood-web-react-manual/manuais/cupom-taxa-servico-opcional/imagens-tratadas/05-cupom-presencial.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR. Manter a tabela **O que este texto faz (e o que não faz)**.
- Linkar taxa obrigatória (#41) e relatório de taxa (#85).
- Destacar: a frase vai **só no rodapé Presencial** (Delivery não tem taxa);
  **SALVAR E FECHAR** (não é auto-save); asterisco não vira negrito.
- Não publicar o rodapé interno.

## Estrutura da página

1. O que este texto faz (e o que não faz)
2. Abra o Cupom Pedido
3. Vá em Texto Padrão
4. Escreva no Rodapé
5. A taxa continua no pedido
6. O que sai no papel
7. Perguntas rápidas

## Anexo — legendas

| Ordem | Arquivo | Tipo | Legenda |
|-------|---------|------|---------|
| 1 | `01-aba-layout.png` | com setas | Layout → Cupom Pedido |
| 2 | `02-modal-abas.png` | com setas | Aba Texto Padrão |
| 3 | `03-texto-rodape.png` | com setas | Rodapé Presencial e SALVAR |
| 4 | `04-detalhe-venda.png` | com setas | Taxa 10% na venda 940 + impressora |
| 5 | `05-cupom-presencial.png` | com setas | Serviço (10%) e a frase no rodapé (sem QR) |
