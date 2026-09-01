# texto-documentation.ia.md — Criar usuário e montar grupo de acesso

## PROMPT (copiar e colar)

Em **Configuração**, adicione um item de menu por último chamado **Criar Usuário e Grupo de
Acesso**.

Leia APENAS os arquivos abaixo (não varra o resto do projeto):

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/usuarios-criar/usuarios-criar.md`
2. Imagens (nesta ordem):
   - `beefood-web-react-manual/manuais/usuarios-criar/imagens-tratadas/01-aba-usuarios-limite-do-plano.png`
   - `beefood-web-react-manual/manuais/usuarios-criar/imagens-tratadas/05-modal-novo-grupo-vazio.png`
   - `beefood-web-react-manual/manuais/usuarios-criar/imagens-tratadas/07-grupo-novo-permissoes-iniciais.png`
   - `beefood-web-react-manual/manuais/usuarios-criar/imagens-tratadas/02-modal-novo-usuario-vazio.png`
   - `beefood-web-react-manual/manuais/usuarios-criar/imagens-tratadas/15-comparativo-com-e-sem-grupo.png`
   - `beefood-web-react-manual/manuais/usuarios-criar/imagens-tratadas/10-escolher-grupo-de-acesso.png`
   - `beefood-web-react-manual/manuais/usuarios-criar/imagens-tratadas/13-modal-alterar-senha.png`
   - `beefood-web-react-manual/manuais/usuarios-criar/imagens-tratadas/17-usuario-inativo-na-lista.png`
   - `beefood-web-react-manual/manuais/usuarios-criar/imagens-tratadas/14-usuario-principal-login-bloqueado.png`

NÃO leia outros arquivos (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

- Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa".
- pt-BR, didático; destacar obrigatórios; **não publicar** o rodapé "Referências internas".
- A seção 4 ("O erro mais caro") é o ponto central do manual — mantenha o destaque e os números.
- A imagem `15-comparativo-com-e-sem-grupo.png` é um **comparativo lado a lado** (dois menus com
  título). Apresente em largura cheia.
- Onde o texto cita o estudo **Grupos de Acesso**, crie um link para o item de menu daquele
  manual, se ele já estiver publicado.

## Estrutura da página (na ordem do `usuarios-criar.md`)

1. A tela de usuários — o contador do plano e as colunas
2. Passo 1 — criar o grupo de acesso (e o fato de ele nascer com tudo liberado)
3. Passo 2 — criar o usuário (os sete campos)
4. O erro mais caro: deixar o grupo em "Nenhum"
5. Passo 3 — ajustar as permissões do grupo (aponta para o estudo #75)
6. Trocar o grupo de alguém
7. Alterar a senha
8. Tirar o acesso de alguém (desativar, e o contador que não muda)
9. O usuário principal
10. Perguntas rápidas

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|-------|----------------------------------|------|---------|
| 1 | `01-aba-usuarios-limite-do-plano.png` | com setas | A aba Usuários: botão de criar, contador do plano e as colunas Função e Grupo de Acesso |
| 2 | `05-modal-novo-grupo-vazio.png` | com setas | Novo Grupo de Acesso: só o nome, e o aviso de que as permissões vêm depois |
| 3 | `07-grupo-novo-permissoes-iniciais.png` | com setas | O grupo recém-criado, com todas as permissões ligadas |
| 4 | `02-modal-novo-usuario-vazio.png` | com setas | Novo Usuário: Login, Senha, Funcionário, Grupo de Acesso e os três switches |
| 5 | `15-comparativo-com-e-sem-grupo.png` | comparativo | O menu de quem tem grupo restrito x de quem ficou sem grupo |
| 6 | `10-escolher-grupo-de-acesso.png` | com setas | O campo Grupo de Acesso aberto, com a opção Nenhum e os grupos da empresa |
| 7 | `13-modal-alterar-senha.png` | com setas | Alterar Senha: nova senha e confirmação |
| 8 | `17-usuario-inativo-na-lista.png` | com setas | Usuário desativado e o contador do plano inalterado |
| 9 | `14-usuario-principal-login-bloqueado.png` | com setas | O cadastro do usuário principal, com o login travado |

## Observações de conteúdo

- Duas mensagens não podem ser suavizadas: **(a)** usuário sem grupo enxerga quase tudo;
  **(b)** não existe excluir usuário, e desativar não libera vaga no plano.
- O switch **Gerente** merece o aviso que está no texto: ele dispensa a senha de gerente nas
  ações protegidas em Parâmetros.
- Não publicar `fluxo-codigo.md` nem `MEMORIA.md`: eles têm ids do sandbox, senhas de teste e
  nomes de chaves internas.
