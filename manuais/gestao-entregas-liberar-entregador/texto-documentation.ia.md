# texto-documentation.ia.md — #104 Liberar o entregador

## PROMPT (copiar e colar)

Dentro do menu **Gestão de Entregas**, crie a página **Liberar o entregador: cadastro,
acesso ao app e código de barras**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/gestao-entregas-liberar-entregador/gestao-entregas-liberar-entregador.md`
2. Imagens (nesta ordem):
   - `.../imagens-tratadas/01-lista-funcionarios.png`
   - `.../imagens-tratadas/02-funcionario-dados.png`
   - `.../imagens-tratadas/03-funcionario-funcao.png`
   - `.../imagens-tratadas/04-usuarios-lista.png`
   - `.../imagens-tratadas/05-usuario-novo.png`
   - `.../imagens-tratadas/06-impressao-layout.png`
   - `.../imagens-tratadas/07-cupom-texto-padrao.png`
   - `.../imagens-tratadas/08-cupom-impresso.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`,
`*.geo.json`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter as tabelas de setas (nº → onde → o que faz) embaixo de cada
  imagem.
- Manter os **dois links de download** do aplicativo (Google Play e App Store) como links
  de verdade.
- Manter, sem enxugar, os quatro avisos que o cliente erra na prática:
  (a) **são dois cadastros** — funcionário e usuário —, e faltar um dá sintoma em lugar
  diferente;
  (b) o switch **Aplicativos** desligado faz o app recusar login e senha corretos;
  (c) o campo **Funcionário** em *Nenhum* deixa o app entrar e não mostrar entrega;
  (d) a função é **exclusiva**: marcar *Garçom* desmarca *Entregador*.
- Manter a seção que diz que **ler o código de barras é despachar**, com a lista do que isso
  dispara (situação do pedido, marketplace, impressão, WhatsApp) e os dois avisos que vêm
  dela: não testar o leitor em pedido de cliente, e correção é pelo painel.
- Manter a frase de que o código só sai em **delivery com entrega**.
- Manter a tabela **Problemas comuns** inteira.
- Manter a tabela final **Onde continuar**.
- Avisar, no começo, que a **Gestão de Entregas está em liberação** e que a tela pode ainda
  não aparecer para todos (falar com o suporte). Não citar `empresaID`.
- Não publicar rotas de API, nomes de tabela, nomes de procedure, nomes de componente nem
  `empresaID`. Em especial: não citar `lerCodigoBarras`, `SituacaoDeliveryUpdater` nem
  `beeEntregaCodigoBarras`.
- Não citar gate comercial nem plano: se o recurso não estiver liberado, o caminho do
  lojista é o suporte.
- Não citar o `cenario.js` nem nada de bastidor de captura.

## Estrutura da página (mesma numeração do `.md`)

- Para que serve
- Antes de começar (com os dois links de download)
- 1. Cadastrar o funcionário
- 2. Marcar a função Entregador
- 3. Criar o usuário do celular (+ Conferir se deu certo)
- 4. Ligar o código de barras no cupom (+ O que acontece quando o motoboy lê o código)
- Problemas comuns
- Onde continuar

## Anexo — legendas das imagens (na ordem)

1. `01-lista-funcionarios.png` — A lista de funcionários, com a contagem de entregadores e
   a coluna Função.
2. `02-funcionario-dados.png` — A ficha do funcionário, aba **Dados**.
3. `03-funcionario-funcao.png` — A aba **Função** com *Entregador* marcado, diária e valor
   por KM.
4. `04-usuarios-lista.png` — A lista de usuários, com o selo *Entregador* na coluna Função.
5. `05-usuario-novo.png` — A ficha do usuário novo: login, senha, funcionário vinculado e o
   switch **Aplicativos**.
6. `06-impressao-layout.png` — A aba **Layout**, com o **Cupom Pedido**.
7. `07-cupom-texto-padrao.png` — A caixinha **Código de Barras App Entrega**, na aba *Texto
   Padrão*.
8. `08-cupom-impresso.png` — O cupom impresso, com o código de barras no pé.
