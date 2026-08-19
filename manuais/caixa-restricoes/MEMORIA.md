# MEMÓRIA — Manual de Restrições de Caixa (por grupo de acesso)

> Memória detalhada deste manual. **O estudo está concluído**; falta produzir.
> Ver também: `../../MEMORIA-GERAL.md`, `../caixa-fechar/` e `../caixa-conferencia-2/`.

Status: 🔨 **Em execução** — estudo concluído em 2026-08-19, produção pendente.

---

## 1. Escopo aprovado pelo dono

Manual **único** explicando **todas** as restrições de caixa que podem ser aplicadas a um
usuário, como configurar cada uma e como o caixa fica depois.

Decisões dele, já fechadas:

- **Formato:** dividido por restrição, em pares — *como fazer 1 e como fica*, *como fazer 2 e
  como fica*, e assim por diante. Não é por perfil de usuário.
- **Escopo completo:** inclui o que não está no grupo de acesso (Função Gerente, parâmetro
  Caixa por Usuário, Cadastro de Caixas).
- **Numeração `1, 2, 3`** no texto (nunca `①②③`).
- Autorizado **criar usuário de teste** e **mexer nos switches** do grupo "Acesso Funcionário".
- Mobile fora do escopo (padrão dos manuais anteriores).

---

## 2. Onde se configura

**Configuração → Usuários → aba Grupos de Acesso → clicar no grupo** abre o modal
*Editar Grupo: \<nome\>*, com as permissões agrupadas por recurso, busca e filtro.

Dois comportamentos da tela que precisam entrar no manual:

1. **Cada switch salva na hora**, individualmente. O botão **Salvar** do rodapé serve apenas
   para o campo **Descrição** do grupo.
2. A **busca esconde os sub-itens** quando o texto não casa com eles. Buscar "Abrir e Fechar"
   não mostra as sub-permissões; buscar "caixa" mostra. Isso engana quem procura.

API por trás: `GET /api/empresa2/grupoAcesso/{empresaID}/{usuarioID}/{grupoAcessoID}` lista os
itens; `POST /api/empresa2/grupoAcessoItem` grava cada toggle.

---

## 3. As restrições e o efeito de cada uma (TESTADO)

Todos os efeitos abaixo foram comprovados ao vivo em 19/08/2026, desligando uma permissão por
vez e observando o caixa do usuário restrito. Tudo foi religado depois.

| # | Restrição | Onde | Efeito ao DESLIGAR | Flag na API de caixa |
|---|-----------|------|--------------------|----------------------|
| 1 | **Abrir e Fechar Caixa** | Grupo → Venda | O menu **Caixa** desaparece e o acesso direto a `/caixa` redireciona para a home | `sidebar.menu.caixa` |
| 2 | **Visualizar Valores de Referência** | sub-item de 1 | Somem as colunas **Saldo Final**, **Conf. Saldo Final** e **Quebra de Caixa** na listagem; o painel **Resumo** fica "Nenhum resumo disponível"; na conferência somem **Entrada, Saída, Saldo e Diferença**; somem os botões **Reabrir Caixa** e **Ver Conferência** | `itemID136` |
| 3 | **Visualizar Caixas Fechados** | sub-item de 1 | A listagem passa a mostrar **só o caixa aberto** (no teste: de 10 linhas para 1) | `itemID212` |
| 4 | **Transferência de Operações** | sub-item de 1 | Só o botão **TRANSFERIR** desaparece | `itemID227` |
| 5 | **Cadastro de Caixas** | Grupo → Empresa | Esconde **Configuração → Caixa** (cadastro dos terminais) | `submenus.configuracao.items.caixa` |
| 6 | **Função Gerente** | Cadastro do **usuário** | Sem ela, a aba **Cancelamentos** não aparece | flag `gerente` do cache |

A restrição **2** é a mais interessante do manual: ela cria uma **conferência cega** — o
operador digita o que contou sem ver quanto o sistema esperava.

### Duas dúvidas que já foram respondidas por teste

- **Usuário Principal NÃO tem bypass.** Desligamos "Transferência de Operações" no grupo
  Administrador2 e o botão TRANSFERIR desapareceu para o `contato@beefood.com.br`
  (`itemID227: false`). Ou seja: dá para testar no próprio login — mas **nunca desligar
  "Usuários"**, senão o próprio acesso à tela de permissões é perdido e não há como religar.
- **Sangria e Acréscimo não têm permissão própria.** O usuário restrito lançou um acréscimo e
  o servidor respondeu **200**. Quem tem "Abrir e Fechar Caixa" opera o caixa. O erro
  *"Usuário sem permissão para realizar operações no caixa"* que existe no front é defensivo,
  para outro cenário.

---

## 4. O QUE FALTA (a única pendência do estudo)

**Parâmetro "Caixa por Usuário"** — em **Configuração → Parâmetros**, com a descrição em tela
*"Cada usuário tem e só consegue ver seu próprio caixa"*. No cache do usuário aparece como
`caixaPorUsuario`, e está **ligado** no sandbox.

**O comportamento observado contradiz a descrição:** com o parâmetro ligado, o usuário
`caixa.manual` **viu os 10 caixas** da listagem (inclusive os abertos por outro usuário) e
**conseguiu lançar uma operação** no caixa aberto pelo `contato@beefood.com.br`.

Hipóteses a confirmar:

1. O parâmetro age apenas na **abertura** (cada usuário abre o seu caixa, sem compartilhar o
   mesmo caixa aberto), não na visualização.
2. Ele depende de algo mais (função, permissão) para filtrar a listagem.
3. O filtro existe mas é aplicado no backend só em certas rotas.

**Como resolver:** ler o backend (ver seção 6). Procurar por `caixaPorUsuario` nas rotas
`caixa2/caixaListagem`, `caixa2/caixaDetalhes` e `caixa2/abrir`. Alternativa empírica: desligar
o parâmetro, comparar a listagem do usuário restrito antes e depois, e religar.

**Só depois disso o manual pode ser escrito "completo"**, como o dono pediu.

---

## 5. Ambiente de teste já preparado

| Item | Valor |
|------|-------|
| Usuário restrito | **`caixa.manual`** / senha **`manual123`** |
| Grupo dele | **Acesso Funcionário** (`grupoAcessoID` 71880) |
| Função Gerente | **não** marcada (de propósito — é o que esconde Cancelamentos) |
| Usuário admin | `contato@beefood.com.br` / `1q2w3e4r` — **Principal**, Gerente, grupo **Administrador2** (`grupoAcessoID` 71879) |
| Estado dos switches | **tudo religado** ao final do estudo |
| Sujeira conhecida | um acréscimo de **R$ 0,01** com observação "teste de permissao - manual" no caixa aberto |

No grupo **Acesso Funcionário**, "Cadastro de Caixas" já vem **desligado** — é o cenário da
restrição 5 sem precisar mexer em nada.

### Técnica de teste que funcionou

Dois contextos de navegador no mesmo script Playwright: um logado como **admin** (que liga e
desliga o switch) e outro como **restrito** (que recarrega `/caixa` e observa). Entre cada
teste, religar a permissão para isolar as variáveis.

Para localizar o switch de um sub-item: buscar **"caixa"** no campo *Buscar permissão...*,
expandir o item "Abrir e Fechar Caixa" pelo chevron e mapear switch → rótulo via
`page.evaluate`, porque os switches não têm rótulo acessível próprio.

Ler as flags do resultado direto das respostas de `caixaListagem` e `caixaDetalhes`, em vez de
inferir pela tela — é mais confiável e mostra a causa, não só o efeito.

---

## 6. Onde está o código

| Camada | Caminho |
|--------|---------|
| Front (tela de grupos) | `~/refs/beefood-web-react/src/components/ModalEditarGrupoAcesso.tsx`, `src/pages/Usuarios.tsx`, `src/hooks/useGrupoAcessoDetalhes.ts` |
| Front (consumo) | `src/hooks/usePermissions.ts`, `src/utils/configCache.ts`, `src/components/ProtectedRoute.tsx` |
| Front (caixa) | `src/pages/Caixa.tsx`, `src/components/CaixaVerModal.tsx`, `src/components/CaixaFecharModal.tsx`, `src/hooks/useCaixaData.ts` |
| Parâmetro | `src/pages/Parametros.tsx` (rótulo "Caixa por Usuário") |
| **Backend** | `~/refs/beetech-server-node-2.0` (branch `beefood-web-react`) — **só existe a partir da sessão em que o secret `BITBUCKET_TOKEN` já esteja injetado** |

O cache de permissões do usuário logado fica no `localStorage`, chave `config_cache`, em
**base64 + zlib**. Para inspecionar: `base64 -d` e descomprimir (em Python,
`zlib.decompress(base64.b64decode(valor))`).

---

## 7. Plano de produção (quando o estudo fechar)

1. Resolver a pendência do **Caixa por Usuário** (seção 4).
2. Capturar, para cada uma das 7 restrições, o par **como configurar** (o switch na tela do
   grupo) e **como fica** (a tela do usuário restrito).
3. Comparar sempre com o caixa completo, para o "antes e depois" ficar evidente.
4. Escrever `caixa-restricoes.md`, `fluxo-codigo.md` e `texto-documentation.ia.md` no padrão,
   com `annotate.py` (copiar o de `../caixa-conferencia-2/`, que já tem fallback de fonte).
5. Fechar o item **#13** no `CHECKLIST-MANUAIS.md`.

Estimativa de imagens: cerca de duas por restrição (configuração + efeito), mais uma de
contexto da tela de grupos — algo entre 12 e 15.
