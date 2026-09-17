# texto-documentation.ia.md — #103 Venda Sugestiva (UpSell)

## PROMPT (copiar e colar)

Em **Cardápio**, adicione um item de menu chamado **Venda Sugestiva (UpSell)**, por
último.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/venda-sugestiva-upsell/venda-sugestiva-upsell.md`
2. Imagens (nesta ordem):
   - `.../imagens-tratadas/01-menu-acoes.png`
   - `.../imagens-tratadas/02-janela-geral.png`
   - `.../imagens-tratadas/03a-janela-vazia.png`
   - `.../imagens-tratadas/03-janela-escolha.png`
   - `.../imagens-tratadas/03b-toast-salvo.png`
   - `.../imagens-tratadas/04-menu-produto.png`
   - `.../imagens-tratadas/05-aba-cadastro.png`
   - `.../imagens-tratadas/06-limite.png`
   - `.../imagens-tratadas/07-delivery.png`
   - `.../imagens-tratadas/08-presencial.png`
   - `.../imagens-tratadas/09-relatorio-delivery.png`
   - `.../imagens-tratadas/09-relatorio-delivery-listas.png`
   - `.../imagens-tratadas/10-relatorio-presencial.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `capturar*.py`,
`imagens-puras/`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter as tabelas de setas (nº → item → o que fazer) embaixo de
  cada imagem.
- **Não citar as sugestões automáticas do carrinho.** O manual é só da venda
  sugestiva configurável (upsell). O relatório é compartilhado com elas, mas isso não
  entra no texto.
- Avisar, no começo, que o recurso está **em liberação** e que a opção pode não
  aparecer (falar com o suporte). Não citar `empresaID`.
- Repetir os quatro avisos operacionais: (a) o limite é **6 produtos** por produto;
  (b) a **ordem** da faixa *Selecionados* é a ordem que o cliente vê; (c) a aba do
  cadastro **salva sozinha** (as duas janelas exigem **SALVAR (F2)**); (d) produto
  inativo, em falta, oculto naquele cardápio ou **já na sacola** não é oferecido.
- Manter a seção **6.2** (tablet e totem) mesmo sem imagem: é onde o lojista descobre
  que a mesma lista vale para os aplicativos.
- Manter as seções **8. O que vale a pena sugerir**, **Problemas comuns** e
  **Perguntas frequentes** inteiras — são elas que respondem à busca do lojista
  (*venda sugestiva*, *upsell*, *sugerir produto no cardápio digital*, *aumentar
  ticket médio*, *que tal levar junto*, *vender mais no delivery*).
- Não publicar rotas de API, nomes de componente, `empresaID` nem atalhos internos
  além de F2 (salvar) e ESC (fechar/cancelar), que aparecem na própria tela.

## Estrutura da página (mesma numeração do `.md`)

- Antes de começar
- 1. Os três caminhos para configurar
- 2. Caminho 1 — pelo menu de ações da tela Cardápio
  - 2.1 Escolher os produtos que serão sugeridos
- 3. Caminho 2 — pelos três pontinhos do produto
- 4. Caminho 3 — pela aba Venda Sugestiva do cadastro do produto
- 5. As regras da lista (limite de 6, como desligar, o que o cliente não vê)
- 6. Como fica para o cliente — cardápio digital delivery
  - 6.1 Cardápio digital presencial (mesa e comanda)
  - 6.2 Cardápio no tablet e totem de autoatendimento
- 7. O relatório: quanto a sugestão vendeu
  - 7.1 O mesmo relatório no presencial
- 8. O que vale a pena sugerir
- Problemas comuns
- Perguntas frequentes
- Manuais relacionados

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|-------|----------------------------------|------|---------|
| 1 | `01-menu-acoes.png` | com setas | Menu de ações da tela Cardápio com a opção Venda Sugestiva (UpSell) |
| 2 | `02-janela-geral.png` | com setas | Janela Venda Sugestiva (UpSell): busca, filtro de setores, *Somente configurados*, selo *Configurado* e a linha *Sugere:* |
| 3 | `03a-janela-vazia.png` | contexto | Janela de escolha ainda sem nenhum produto marcado (0/6) |
| 4 | `03-janela-escolha.png` | com setas | Quatro produtos marcados: caixinha, faixa *Selecionados*, contador e SALVAR (F2) |
| 5 | `03b-toast-salvo.png` | com setas | Aviso *Venda sugestiva salva com 4 produtos* |
| 6 | `04-menu-produto.png` | com setas | Três pontinhos do produto com a opção Venda Sugestiva |
| 7 | `05-aba-cadastro.png` | com setas | Aba Venda Sugestiva no cadastro do produto, com a etiqueta *Salvo automaticamente* |
| 8 | `06-limite.png` | com setas | Limite de 6 atingido e caixinhas apagadas |
| 9 | `07-delivery.png` | com setas | Tira de 3 celulares: a sugestão aparece, o produto sugerido abre, os dois na sacola (delivery) |
| 10 | `08-presencial.png` | com setas | Tira de 2 celulares: a mesma janela no presencial, com o preço do canal, e a sacola |
| 11 | `09-relatorio-delivery.png` | com setas | Desempenho → Delivery → Sugestões: caminho, período, os três números e Exportar Excel |
| 12 | `09-relatorio-delivery-listas.png` | contexto | Mais Sugeridos por Valor e Mais Sugeridos por Quantidade |
| 13 | `10-relatorio-presencial.png` | com setas | Desempenho → Presencial → Sugestões |

## Observações para a publicação

- As imagens 9 e 10 são tiras de celular (cardápio público). Publicar cada uma como
  uma imagem só, sem cortar os aparelhos.
- A imagem 13 (presencial) aparece com os cartões zerados de propósito: é o exemplo
  sem sugestão aceita no período. O texto já explica.
- Linkar, quando existirem: **Cardápio — fundamentos**, **Exibir / Ocultar**,
  **Preço Programado**, **Cardápio digital presencial e QR Code** e **Cashback —
  configurar o programa**.
- Não publicar o `fluxo-codigo.md`.
