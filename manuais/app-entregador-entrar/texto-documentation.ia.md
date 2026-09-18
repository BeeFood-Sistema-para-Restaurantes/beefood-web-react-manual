# texto-documentation.ia.md — #111 App do entregador: instalar, entrar e ficar disponível

## PROMPT (copiar e colar)

Dentro do menu **Gestão de Entregas**, crie a página **App do entregador: instalar, entrar e
ficar disponível**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/app-entregador-entrar/app-entregador-entrar.md`
2. Imagens (nesta ordem):
   - `.../imagens-tratadas/01-permissao-localizacao.png`
   - `.../imagens-tratadas/02-permitir-o-tempo-todo.png`
   - `.../imagens-tratadas/03-permissao-camera.png`
   - `.../imagens-tratadas/04-login.png`
   - `.../imagens-tratadas/05-senha-visivel.png`
   - `.../imagens-tratadas/06-erro-credencial.png`
   - `.../imagens-tratadas/07-permissao-notificacoes.png`
   - `.../imagens-tratadas/08-tela-de-trabalho.png`
   - `.../imagens-tratadas/09-folha-disponibilidade.png`
   - `.../imagens-tratadas/10-tres-pilulas.png`
   - `.../imagens-tratadas/11-menu.png`
   - `.../imagens-tratadas/12-permissoes.png`
   - `.../imagens-tratadas/13-confirmar-saida.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter as tabelas de setas (nº → onde → o que fazer) embaixo de cada imagem.
- Avisar, no começo, que a **Gestão de Entregas está em liberação** e que o aplicativo do
  entregador pode ainda não estar disponível para todas as lojas (falar com o suporte). Não citar
  `empresaID`.
- **Este manual é para o entregador**, não para o operador do painel. O tom é de quem vai usar o
  celular na rua. Deixar isso claro na abertura, e apontar para o manual de *Liberar o
  entregador* quem precisa criar o acesso.
- Manter, sem enxugar:
  (a) que as permissões são pedidas **antes** do login, e a de notificações **depois**;
  (b) por que **Exata** e não *Aproximada*, e por que **Permitir o tempo todo** e não *durante o
  uso do app* — com a explicação prática do celular no bolso;
  (c) que **Apenas esta vez** deve ser evitada;
  (d) que **não existe recuperação de senha** no aplicativo, e que a mensagem de erro é a mesma
  para senha errada, e-mail inexistente e acesso desativado;
  (e) que a sessão **não cai** sozinha: só sai quem usa o SAIR;
  (f) o ponto central da disponibilidade — a pílula **informa, não bloqueia**; entrega chega em
  PAUSA e em OFFLINE, e as entregas já na lista continuam sendo do entregador;
  (g) que **sair é diferente de ficar offline**;
  (h) que o aplicativo **não liga permissão nenhuma** — quem concede é o Android — e a
  recomendação de conferir a tela de Permissões no começo do turno, porque o Android revoga por
  inatividade sem avisar;
  (i) que a lista mostra **apenas** os pedidos no nome daquele entregador.
- Não publicar rotas de API, nomes de tabela, nomes de coluna nem nomes de arquivo do aplicativo.
  Em particular: não citar `validaBeeEntregador`, `entrega2/gestao/presenca`, `AsyncStorage`,
  `apiN3` nem `EntregadorLocationReportingHost`.
- Não citar bastidor de captura: nem emulador, nem material recebido.
- A senha que aparece na imagem da senha revelada é de conta de teste. Não comentar isso na
  página; só não usar o valor como exemplo no texto.

## Estrutura da página (mesma numeração do `.md`)

- Para que serve
- Antes de começar
- 1. As permissões que o celular pede
- 2. Entrar
- 3. A tela de trabalho
- 4. Avisar se você está rodando
- 5. O menu, as permissões e o sair
- Perguntas frequentes
- Onde continuar

## Anexo — legendas das imagens (na ordem)

1. `01-permissao-localizacao.png` — O pedido de localização do Android, com Exata e Aproximada e
   as três respostas.
2. `02-permitir-o-tempo-todo.png` — As configurações do Android, com *Permitir o tempo todo*
   marcada e *Usar local exato* ligado.
3. `03-permissao-camera.png` — O pedido de câmera.
4. `04-login.png` — A tela de login: Usuário, Senha e ENTRAR.
5. `05-senha-visivel.png` — A senha revelada pelo olho, e o olho cortado que esconde de novo.
6. `06-erro-credencial.png` — A faixa vermelha *Usuário e/ou Senha inválidos.*
7. `07-permissao-notificacoes.png` — O pedido de notificações, depois do login.
8. `08-tela-de-trabalho.png` — A aba Entregas vazia: menu, título, pílula ONLINE, ATUALIZAR e as
   quatro abas.
9. `09-folha-disponibilidade.png` — A folha *Sua disponibilidade* com Online, Em pausa, Offline,
   o aviso em cinza e CANCELAR.
10. `10-tres-pilulas.png` — As três pílulas lado a lado: ONLINE verde, PAUSA laranja e OFFLINE
    cinza.
11. `11-menu.png` — O menu do aplicativo, com os cinco itens.
12. `12-permissoes.png` — A tela de Permissões, com os quatro cartões e o selo Ativa.
13. `13-confirmar-saida.png` — A confirmação *Sair do aplicativo?*, com SAIR e CANCELAR.
