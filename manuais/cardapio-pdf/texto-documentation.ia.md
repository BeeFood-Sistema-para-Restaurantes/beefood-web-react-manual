# texto-documentation.ia.md — #102 Gerar Cardápio em PDF

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `cardapio-pdf.md`
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

Em **Cardápio**, adicione um item de menu chamado **Cardápio em PDF**, depois de
*Preço Programado*.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/cardapio-pdf/cardapio-pdf.md`
2. Imagens (nesta ordem):
   - `.../imagens-tratadas/01-menu-cardapio-pdf.png`
   - `.../imagens-tratadas/02-acoes-gerar-pdf.png`
   - `.../imagens-tratadas/03-etapa1-cardapios-itens.png`
   - `.../imagens-tratadas/04-etapa1-itens-editaveis.png`
   - `.../imagens-tratadas/05-etapa2-modelos.png`
   - `.../imagens-tratadas/06-etapa2-pagina-fotos.png`
   - `.../imagens-tratadas/07-etapa2-o-que-mostrar.png`
   - `.../imagens-tratadas/08-etapa3-marca.png`
   - `.../imagens-tratadas/09-etapa3-capa.png`
   - `.../imagens-tratadas/10-etapa4-revisar-baixar.png`
   - `.../imagens-tratadas/11-pdf-pronto.png`
   - `.../imagens-tratadas/12-modelos.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `capturar.py`,
`imagens-puras/`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR. Manter as tabelas de setas (nº → item → o que fazer) embaixo de cada imagem.
- **SEO (prioridade deste manual):** manter no texto, sem trocar por sinônimos
  genéricos e sem resumir, os termos de busca do lojista — *cardápio em PDF*,
  *gerar cardápio em PDF*, *cardápio impresso*, *imprimir cardápio*, *cardápio para
  imprimir*, *cardápio de mesa*, *cardápio A4*, *cardápio A5*, *cardápio com foto*,
  *cardápio sem preço*, *cardápio com QR Code*, *cardápio para gráfica*, *mandar o
  cardápio no WhatsApp*, *cardápio de parede / estilo lousa*, *modelo de cardápio*.
  Manter as seções **9. Receitas rápidas** e **Perguntas frequentes** inteiras: são
  elas que respondem à busca.
- Avisar, no começo, que o recurso está **em liberação** e que o item pode não
  aparecer no menu (falar com o suporte). Não citar `empresaID`.
- Repetir os três avisos operacionais: (a) o gerador **não salva** as escolhas —
  monte e baixe na mesma sessão; (b) o que se edita na etapa 1 (nome, descrição,
  preço) vale **só para o PDF**, não altera o cadastro nem o cardápio digital;
  (c) passe pela **etapa 3** antes de baixar, senão a capa sai sem o QR Code.
- Manter os números de peso do arquivo (4,4 MB com fotos × 57 KB só texto) — é o
  argumento do cardápio para WhatsApp.
- Não publicar rotas de API, nomes de componente, `empresaID` nem atalhos internos
  além de F2 (baixar) e ESC (fechar), que aparecem na própria tela.

## Estrutura da página

1. Antes de começar
2. Abrir o gerador de cardápio em PDF
3. Como o gerador funciona (as 4 etapas + prévia)
4. Etapa 1 — quais itens entram no cardápio impresso
   4.1 Mudar nome, descrição e preço só no impresso
5. Etapa 2 — modelo, tamanho do papel e fotos
   5.1 O que aparece em cada item
6. Etapa 3 — sua marca, o QR Code e a capa
7. Etapa 4 — revisar e baixar o PDF
8. Como fica o PDF pronto
9. O mesmo cardápio em três modelos
10. Receitas rápidas
11. Problemas comuns
12. Perguntas frequentes
13. Manuais relacionados

## Observações para a publicação

- As imagens 11 e 12 são páginas do PDF gerado (não são telas do sistema): manter a
  legenda que já está na imagem e o texto que explica cada número.
- O manual não substitui nenhum outro. Linkar, quando existirem: **Cadastro de
  produtos e setores**, **Exibir / Ocultar**, **Cardápio digital presencial e QR
  Code**, **Aparência e layout do cardápio digital** e **Tabela de preço**.
