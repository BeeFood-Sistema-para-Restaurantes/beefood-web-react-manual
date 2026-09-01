# MEMORIA.md — Criar usuário e montar grupo de acesso

Manual **#76**. Passo a passo operacional de dar acesso a alguém: criar o grupo, criar o
usuário, ligar os dois, trocar senha e desativar. Complementa o **#75**
(`manuais/grupos-acesso/`), que é o catálogo das 93 permissões.

Última atualização: 01/09/2026.

---

## 1. O pedido

Sequência do #75. No `CHECKLIST-MANUAIS.md`, o item "Usuários e permissões" previa "1 a 2
manuais: criar usuário, montar grupo de acesso e o que cada permissão faz". O #75 fechou o "o
que cada permissão faz"; este fecha o "criar usuário e montar grupo".

---

## 2. O achado que organizou o manual

**Usuário criado sem grupo de acesso vê quase o sistema inteiro.** O campo Grupo de Acesso
aceita **Nenhum**, é esse o valor inicial, e salvar assim não gera aviso.

Medido pela API, com o token de cada usuário:

| Usuário | grupoAcessoID | chaves | `false` |
|---------|--------------:|-------:|--------:|
| `estoque.manual` (sem grupo) | `null` | 352 | **7** |
| `caixa.manual` (Acesso Funcionário) | 71880 | 352 | **108** |

As 7 são as que não dependem do grupo (Copiar do iFood, Copiar de Imagem, Migrar Dados — todas
de Função Gerente — e o Fluxo Caixa, que é "Em breve!").

Por isso o manual **inverte a ordem intuitiva**: cria o grupo no Passo 1 e o usuário no Passo 2.
Assim, no momento de salvar o usuário, já existe grupo para escolher.

---

## 3. Outros pontos confirmados em produção

| Afirmação | Como foi confirmada |
|-----------|---------------------|
| Grupo novo nasce com **tudo ligado** | criado o grupo *Acesso Estoque*; os 38 switches de item pai vieram `checked` |
| Não existe excluir usuário | a tela só tem o switch `ativo`; não há rota de exclusão |
| Desativar **não** libera vaga no plano | contador ficou `5/99` com o usuário ativo e `5/99` com ele inativo |
| Senha só é digitada na criação | o campo Senha só renderiza quando `!isEdicao` |
| Mínimo de 4 caracteres é do **Alterar Senha**, não da criação | validação está em `ModalAlterarSenhaUsuario.tsx:48`; a criação só exige não-vazia |
| O login do usuário **principal** é travado | aviso âmbar "Usuário principal…" e campo `disabled` |
| Alterar senha **não** pede a senha atual | o modal tem só Nova Senha e Confirmar Senha |
| O switch **Aplicativos** (`webAcesso`) não bloqueia o painel web | `caixa.manual` tem `webAcesso: false` e entra pelo navegador |

---

## 4. Estado do sandbox — LER ANTES DE REUTILIZAR

Criados para este manual e **impossíveis de excluir**:

| O que | Valor |
|-------|-------|
| Usuário | `estoque.manual` / `manual123`, usuarioID **124781**, grupo **Acesso Estoque**, ativo, não gerente, sem funcionário |
| Grupo | **Acesso Estoque**, grupoAcessoID **71881**, 93 permissões **ligadas** |

O contador do plano passou de **4/99** para **5/99**.

> **Se precisar de um usuário "sem grupo" para outro manual, não use o `estoque.manual`** — ele
> recebeu grupo na seção 6 deste manual. O `gerentemanual` (88993) está sem grupo, mas a senha
> dele não está registrada em lugar nenhum.

Contas de teste do sandbox, atualizadas:

| Login | Senha | Grupo | Gerente |
|-------|-------|-------|---------|
| `contato@beefood.com.br` | `1q2w3e4r` | Administrador2 | sim (Principal) |
| `caixa.manual` | `manual123` | Acesso Funcionário | não |
| `atendente.parametros` | *(não registrada)* | Acesso Funcionário | não |
| `estoque.manual` | `manual123` | Acesso Estoque | não |
| `gerentemanual` | *(não registrada)* | — | sim |

---

## 5. Armadilhas de captura desta sessão

- **A pesquisa de NPS** ("Como está sendo sua experiência?") aparece depois do login e cobre a
  tela. O botão dela é **FECHAR (ESC)** — o mesmo texto do botão de vários modais do sistema.
  Filtrar o diálogo pelo texto antes de clicar, senão a limpeza fecha o modal que você quer
  fotografar. Foi o que quebrou duas rodadas de captura no #75.
- **O `Select` de Grupo de Acesso é o último `combobox` do modal**; o primeiro é o de
  Funcionário. `page.locator('div[role="dialog"] button[role="combobox"]').last` resolve.
- **Mostrar a senha digitada** (para a captura ficar útil) sai com
  `page.locator('input#senha ~ button').first.click()`.
- Depois de salvar o usuário, a lista **reordena**: o novo entra no fim. Não confie na posição
  para clicar; use o texto do login.

---

## 6. Scripts da sessão (em `/tmp/beefood/`, fora do repositório)

| Script | Papel |
|--------|-------|
| `capturar_criacao.py` | criar usuário (`usuario`) e criar grupo (`grupo`) |
| `capturar_ajustes.py` | escolher grupo, alterar senha, aviso do usuário principal |
| `provar_sem_grupo.py` | compara pela API o que o servidor devolve com e sem grupo |
| `comparar_sem_grupo.py` | prints dos dois menus laterais |
| `testar_inativo.py` | desativa, confere o contador do plano e reativa |
