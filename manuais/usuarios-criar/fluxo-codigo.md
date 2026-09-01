# fluxo-codigo.md — Criar usuário e montar grupo de acesso

Mapeamento técnico da tela **Configuração → Usuários** (`/usuarios`): criação de usuário,
criação de grupo, senha, limite do plano e o que acontece com usuário **sem grupo**.
Documento interno — **não publicar**.

Levantado em 01/09/2026 no sandbox "BeeFood3 - Manual" (empresaID 38311), com o código do front
(`beefood-web-react`) em mãos e execução real em produção. O catálogo das permissões em si está
em `manuais/grupos-acesso/fluxo-codigo.md`.

---

## 1. Rotas e APIs

| Ação | Rota do front | API |
|------|---------------|-----|
| Listar usuários | `/usuarios` (aba Usuários) | `GET /api/empresa2/usuarios/{empresaID}/{usuarioID}` |
| Carregar um usuário | — | `GET` do `useUsuarioCRUD.carregarUsuario` |
| Criar / atualizar usuário | modal Novo/Editar Usuário | `POST /api/empresa2/usuario` |
| Alterar senha | modal Alterar Senha | `POST` do `useUsuarioCRUD` |
| Listar grupos | `/usuarios` (aba Grupos de Acesso) | `GET /api/empresa2/gruposAcesso/{empresaID}/{usuarioID}` |
| Criar / renomear grupo | modal Novo Grupo | `POST /api/empresa2/grupoAcesso` |
| Ligar/desligar permissão | modal do grupo | `POST /api/empresa2/grupoAcessoItem` (um por switch) |

A rota de listagem devolve `qtdUsuarios` (limite do plano) junto com o array `usuarios`.
Exemplo real do sandbox:

```json
{"empresaID": 38311, "qtdUsuarios": 99, "usuarios": [
  {"usuarioID": 88711, "login": "contato@beefood.com.br", "ativo": true, "funcionarioID": 194115,
   "gerente": true, "grupoAcessoID": 71879, "webAcesso": true, "principal": true,
   "nome": "BeeFood3 - Manual", "grupoAcessoDescricao": "Administrador2"}, ...]}
```

---

## 2. Campos do modal de usuário

`src/components/ModalEditarUsuario.tsx`.

| Campo | Estado | Regras |
|-------|--------|--------|
| **Login** | `login` | obrigatório (`toast.error("O login é obrigatório")`). Em edição, começa `disabled` e libera pelo botão de lápis (`loginEditavel`). No usuário **principal**, `loginBloqueado` = sempre travado |
| **Senha** | `senha` | o campo **só é renderizado quando `!isEdicao`**. Obrigatório na criação (`"A senha é obrigatória para novos usuários"`). **Não há validação de tamanho aqui** — o mínimo de 4 caracteres é só do `ModalAlterarSenhaUsuario.tsx:48` |
| **Funcionário** | `funcionarioID` | opcional. Define `usuario` no payload: `funcionarioSelecionado?.nome \|\| login.trim()` |
| **Grupo de Acesso** | `grupoAcessoID` | **opcional** — a opção `Nenhum` manda `undefined`. Ver seção 4 |
| **Ativo** | `ativo` | inicia `true` em usuário novo |
| **Gerente** | `gerente` | flag `_usuario.gerente`; ver `manuais/grupos-acesso/fluxo-codigo.md`, seção 8.1 |
| **Aplicativos** | `webAcesso` | gravado e lido, **sem nenhum consumo no front** além deste modal. `caixa.manual` tem `webAcesso: false` e entra no painel web normalmente — a flag não bloqueia o navegador |

Atalhos: **F2** salva, **Esc** fecha (`useEffect` com `keydown`). Na tela, **F1** abre o modal de
novo usuário (`Usuarios.tsx:182`).

O payload de atualização leva um `log` com os valores anteriores de `login`, `ativo`,
`funcionarioID`, `gerente`, `grupoAcessoID` e `webAcesso` — é o que alimenta o Histórico de
Alterações.

---

## 3. Limite do plano

`src/pages/Usuarios.tsx:75-84`:

```ts
const qtdAtual = usuarios.length;
const podeAdicionarUsuario = !loading && qtdUsuarios > 0 && qtdAtual < qtdUsuarios;
```

- `qtdAtual` conta **todos** os registros devolvidos pela API, **inclusive inativos**.
  Comprovado em produção: com 5 usuários, desativar um manteve o contador em **5/99**.
- Quando o limite é atingido, o botão fica `disabled` com `title="Limite de usuários atingido"`
  e o texto do contador ganha `text-destructive`.
- Não existe rota de exclusão de usuário na tela — só o switch `ativo`.

---

## 4. Usuário sem grupo de acesso vê quase tudo

Este é o achado que motiva a seção 4 do manual. A opção **Nenhum** manda `grupoAcessoID:
undefined`, e o servidor devolve o `grupoAcessoUsuario` **com todas as chaves liberadas**.

Medição pela API (`GET /api/empresa2/empresaConfig/{empresaID}/{usuarioID}/1`, com o token de
cada usuário):

| Usuário | `grupoAcessoID` | chaves | `false` |
|---------|----------------:|-------:|--------:|
| `estoque.manual` (criado sem grupo) | `null` | 352 | **7** |
| `caixa.manual` (grupo Acesso Funcionário) | 71880 | 352 | **108** |

As 7 chaves `false` do usuário sem grupo são exatamente as que **não dependem do grupo**:
`copiarIfood`, `copiarImagem` e `migrarDados` (que exigem Função Gerente) e
`financeiro.items.fluxoCaixa.enabled` (tela "Em breve!").

A causa está no front, em `usePermissions`: toda consulta usa `?? true`, então chave ausente
libera. Como o objeto vem inteiro com `visible: true`, o efeito é o mesmo. Confirmado também
visualmente: o menu lateral do usuário sem grupo traz KDS, Histórico de Vendas, Aplicativos,
Pix Online, WhatsApp, Desempenho, Cardápio Digital e Cardápio no Tablet, que o grupo restrito
escondia.

---

## 5. Criação de grupo: nasce liberado

`src/components/ModalEditarGrupoAcesso.tsx:144-166`. Com `isNovo`, o modal mostra **só** o campo
Descrição; ao salvar, `criarGrupo` devolve o `grupoAccessoID`, o grupo entra no cache local e
`fetchDetalhes` carrega a árvore de permissões no mesmo modal.

Estado inicial medido em produção no grupo **Acesso Estoque** (71881), recém-criado: os **38
switches de item pai** vieram todos `data-state="checked"`. Ou seja, **grupo novo não restringe
nada** — é preciso desligar item por item.

---

## 6. Alterar senha

`src/components/ModalAlterarSenhaUsuario.tsx`:

```ts
if (!senha.trim())            toast.error("Digite a nova senha");
if (senha !== confirmar)      toast.error("As senhas não coincidem");
if (senha.length < 4)         toast.error("A senha deve ter pelo menos 4 caracteres");
```

Não pede a senha atual. Quem tem a permissão **Usuários** (item `Empresa → Usuários` do grupo)
redefine a senha de qualquer pessoa, inclusive do usuário principal.

---

## 7. Estado do sandbox depois deste manual

Criados para as capturas, e **mantidos** (não há como excluir):

| O que | Valor |
|-------|-------|
| Usuário | `estoque.manual` / `manual123`, usuarioID **124781**, grupo **Acesso Estoque**, ativo, não gerente |
| Grupo | **Acesso Estoque**, grupoAcessoID **71881**, com as 93 permissões **ligadas** |

O contador do plano passou de **4/99** para **5/99**. O usuário foi desativado e reativado
durante o teste do contador; terminou **ativo**.

> Se um manual futuro precisar de um usuário "sem grupo" para comparação, **não use o
> `estoque.manual`** (ele agora tem grupo). O `gerentemanual` (88993) segue sem grupo, mas a
> senha dele não está registrada.
