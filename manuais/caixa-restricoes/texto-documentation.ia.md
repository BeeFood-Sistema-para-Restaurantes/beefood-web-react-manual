# texto-documentation.ia.md — Restrições de caixa (grupo de acesso)

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.
> O projeto do manual **já está anexo no contexto** — o prompt aponta os **arquivos exatos** a ler.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Caixa**, adicione um **item de menu por último** chamado **"Restrições de Caixa"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/caixa-restricoes/caixa-restricoes.md`

2. **Imagens (use estas 20, nesta ordem):**
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/01-grupos-de-acesso.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/03-caixa-completo.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/05-modal-caixa-completo.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/02-modal-editar-grupo.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/04-menu-sem-caixa.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/06-listagem-sem-valores.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/07-resumo-vazio.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/08-conferencia-completa.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/09-conferencia-cega.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/10-listagem-so-aberto.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/11-modal-sem-transferir.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/12-switch-cadastro-de-caixas.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/13-menu-config-com-caixa.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/14-menu-config-sem-caixa.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/15-funcao-gerente.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/16-caixa-sem-cancelamentos.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/17-cadastro-de-caixas.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/18-usuario-fixo.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/19-caixa-so-o-seu.png`
   - `beefood-web-react-manual/manuais/caixa-restricoes/imagens-tratadas/20-parametro-caixa-por-usuario.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**

- Use o conteúdo do `caixa-restricoes.md` exatamente como está (seções, textos e tabelas "Nº da seta → campo").
- A estrutura é **por restrição**, cada uma em um par **"Como configurar"** + **"Como fica o caixa"**. Mantenha esse par — é o formato pedido.
- Insira as 20 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Use **números normais** (`1`, `2`, `3`) nas referências às setas — **não** use números circulados (①②③).
- Idioma **português do Brasil**, tom didático (usuário final).
- Mantenha em destaque, sem resumir:
  - **cada switch salva na hora** (não há "salvar tudo no final");
  - **nunca desligar "Usuários"** no próprio grupo;
  - **o usuário Principal não é exceção** às restrições do grupo;
  - a **busca esconde os sub-itens** — buscar "Abrir e Fechar" não mostra os três filhos, buscar "caixa" mostra;
  - a **conferência cega** (restrição 2) é o caso de uso mais forte do manual;
  - na restrição 7, a regra é **invertida** (só fica restrito quem **tem** um caixa no nome) e **o gerente também fica restrito**;
  - o parâmetro **"Caixa por Usuário" não restringe o caixa**, apesar da descrição na tela;
  - a tela de **Parâmetros salva sozinha**, sem botão Salvar.
- **Não** prometa permissão para sangria ou acréscimo: ela não existe hoje.
- O manual é de **desktop**. Não descreva a versão mobile.
- Se o app permitir, cite "Abrir Caixa", "Fechar Caixa" e "Segunda Conferência" como leituras relacionadas.

---

## Estrutura da página (na ordem do `.md`)

1. Introdução (as sete restrições e onde ficam)
2. **Por que restringir o caixa**
3. **Onde tudo se configura**
4. **Antes de começar — três avisos importantes**
5. **O caixa completo — o ponto de partida**
6. **Restrição 1** — Abrir e Fechar Caixa
7. **Restrição 2** — Visualizar Valores de Referência (com a conferência cega)
8. **Restrição 3** — Visualizar Caixas Fechados
9. **Restrição 4** — Transferência de Operações
10. **Restrição 5** — Cadastro de Caixas
11. **Restrição 6** — Função Gerente
12. **Restrição 7** — Cada usuário vê só o seu caixa
13. **E o parâmetro "Caixa por Usuário"?**
14. **Resumo — quero que ele não consiga...**
15. **Dicas finais**

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-grupos-de-acesso.png` | com setas | 1 menu **Usuários** · 2 aba **Grupos de Acesso** · 3 o grupo a editar |
| 2 | `03-caixa-completo.png` | com setas | 1 aba **Cancelamentos** · 2 colunas **Saldo Final**, **Conf. Saldo Final** e **Quebra de Caixa** · 3 botões de ação |
| 3 | `05-modal-caixa-completo.png` | com setas | 1 **TRANSFERIR** · 2 ícones de **Cancelamentos** e **Excluídos** · 3 painel **Resumo** |
| 4 | `02-modal-editar-grupo.png` | com setas | 1 **Buscar permissão** · 2 **Abrir e Fechar Caixa** · 3 **Visualizar Valores de Referência** · 4 **Visualizar Caixas Fechados** · 5 **Transferência de Operações** |
| 5 | `04-menu-sem-caixa.png` | com setas | 1 o vão onde ficava o menu **Caixa** · 2 a tela do funcionário restrito |
| 6 | `06-listagem-sem-valores.png` | com setas | 1 as três colunas de dinheiro sumiram · 2 coluna **Ações**, só com a lupa |
| 7 | `07-resumo-vazio.png` | com setas | 1 **Nenhum resumo disponível** |
| 8 | `08-conferencia-completa.png` | com setas | 1 **Entrada**, **Saída** e **Saldo** · 2 **1ª Conferência** · 3 **Diferença** |
| 9 | `09-conferencia-cega.png` | com setas | 1 só **Forma de Pagamento** e **1ª Conferência** · 2 o campo de contagem, sem referência |
| 10 | `10-listagem-so-aberto.png` | com setas | 1 apenas o caixa **Em aberto** · 2 **Mostrando 1-1 de 1** |
| 11 | `11-modal-sem-transferir.png` | com setas | 1 o vão do **TRANSFERIR** · 2 o vão dos ícones de **Cancelamentos** e **Excluídos** |
| 12 | `12-switch-cadastro-de-caixas.png` | com setas | 1 busca por "cadastro de caixas" · 2 o switch **Cadastro de Caixas** |
| 13 | `13-menu-config-com-caixa.png` | com setas | 1 item **Caixa** no menu Configuração |
| 14 | `14-menu-config-sem-caixa.png` | com setas | 1 o item **Caixa** sumiu entre **Migrar Dados** e **TEF** |
| 15 | `15-funcao-gerente.png` | com setas | 1 **Grupo de Acesso** · 2 switch **Gerente** |
| 16 | `16-caixa-sem-cancelamentos.png` | com setas | 1 só a aba **Listagem de Caixa** |
| 17 | `17-cadastro-de-caixas.png` | com setas | 1 menu **Configuração → Caixa** · 2 coluna **Usuário Fixo** · 3 a linha do caixa |
| 18 | `18-usuario-fixo.png` | com setas | 1 **Usuário Fixo** · 2 switch **Ativo** · 3 **SALVAR (F2)** |
| 19 | `19-caixa-so-o-seu.png` | com setas | 1 **Usuário Abertura** só com o próprio login · 2 **Mostrando 1-1 de 1** |
| 20 | `20-parametro-caixa-por-usuario.png` | com setas | 1 a descrição do parâmetro · 2 o switch |

---

## Observações de conteúdo

- O exemplo é real (conta de testes "BeeFood3 - Manual"). O usuário restrito é `caixa.manual`,
  do grupo **Acesso Funcionário**; o gerente é `contato@beefood.com.br`, do grupo
  **Administrador2**. Se preferir, troque os logins do exemplo por nomes genéricos na publicação.
- Cada efeito mostrado foi obtido desligando **uma** permissão por vez e religando em seguida.
  As imagens de referência (2, 3, 8 e 13 na ordem acima) existem para o leitor comparar.
- A seção sobre o parâmetro **"Caixa por Usuário"** corrige a descrição da própria tela. Não
  suavize esse trecho: o objetivo é impedir que o leitor ligue o parâmetro achando que
  restringiu o caixa.
- **Não** publique nada do `fluxo-codigo.md` (itemIDs, rotas de API, nomes de tabela, caches) nem
  o rodapé "Referências internas" do `.md`.
