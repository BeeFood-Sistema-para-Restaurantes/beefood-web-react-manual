# MEMÓRIA GERAL — Boas práticas para criação de manuais BeeFood

> Memória mestre do projeto de manuais. **Ler SEMPRE no início de cada sessão.**
> Cada manual tem ainda sua própria `MEMORIA.md` dentro da sua pasta.

Última atualização: 2026-08-19 (captura com Playwright no Cloud Agent; correção do acesso ao
código em sessão; versão de produção; #2 no índice)

---

## 1. Objetivo

Criar **manuais de funcionalidades para o USUÁRIO FINAL** do sistema BeeFood, combinando:
- **Código** do projeto `beefood-web-react` (`C:\projetos\beefood-web-react`) → entender a lógica real.
- **Produção** (`https://beefood.app`) → capturar telas reais.

Saída: arquivos **`.md`** + imagens anotadas.

---

## 2. Estrutura de pastas (PADRÃO — seguir sempre)

```
C:\beefood-web-react-manual\
├─ MEMORIA-GERAL.md            <- esta memória (boas práticas, contas, ferramentas)
└─ manuais\
   └─ <nome-do-manual>\        <- UMA PASTA POR MANUAL (ex.: caixa, delivery, pdv...)
      ├─ MEMORIA.md                 <- memória detalhada do manual (fluxo, uso, decisões, estado)
      ├─ <nome>.md                  <- o manual final (para o usuário)
      ├─ fluxo-codigo.md            <- mapeamento técnico (a partir do código)
      ├─ texto-documentation.ia.md  <- PROMPT pronto p/ criar o manual no app (ver seção 12)
      ├─ annotate.py                <- script de anotação (setas/números) deste manual
      ├─ imagens-puras\             <- screenshots ORIGINAIS (BACKUP, nunca referenciado)
      └─ imagens-tratadas\          <- TODAS as imagens do manual (com setas + contexto). Única pasta referenciada
```

**Regra de ouro:** ao iniciar um manual novo, criar uma pasta nova em `manuais\<nome>\`
com TODAS as subpastas/arquivos acima.

---

## 3. Boas práticas de imagens

1. **Sempre salvar a imagem PURA primeiro** em `imagens-puras\` (backup, **nunca referenciado** no `.md` nem no `texto-documentation.ia.md`).
2. Depois gerar a versão **tratada** em `imagens-tratadas\` via `annotate.py`. **`imagens-tratadas\` deve conter TODAS as imagens usadas no manual:** as principais com setas + as de **contexto** (sem setas, via `passthrough()` do `annotate.py`). Assim só essa pasta é referenciada.
3. Nomeação sequencial por etapa: `NN-descricao.png` (ex.: `03-modal-abrir-caixa.png`).
4. **Poucas fotos, sem excesso** — apenas as essenciais de cada etapa.
5. Cada foto essencial leva **setas verdes + número**. O texto do manual referencia cada número e
   destaca campos **obrigatórios (\*)**.
   - **Numeração:** usar SEMPRE números normais **`1.`, `2.`, `3.`** (com ponto). **NÃO** usar
     números circulados (①②③) nem em parênteses — no texto, nas tabelas e nas legendas.
6. As imagens em produção saem em **1508×1274** (DPR alto). `annotate.py` usa coordenadas
   em **frações 0..1**, então independe da resolução.

### Como anotar (Pillow)
- Requisitos: Python 3.10+ e Pillow (já instalados nesta máquina).
- `annotate.py` lê de `imagens-puras\` e escreve em `imagens-tratadas\`.
- Config por imagem: lista de marcadores `(numero, alvo_x, alvo_y, badge_x, badge_y)` em frações.
- Rodar dentro da pasta do manual: `python annotate.py`.
- **Sempre conferir visualmente** as imagens tratadas e ajustar coordenadas se necessário.

---

## 4. Padrão de escrita do manual (.md)

- Idioma: **português do Brasil**, tom didático para usuário final.
- Estrutura: Título → objetivo → pré-requisitos → etapas numeradas → dicas.
- Cada etapa: passos numerados + imagem tratada + **tabela** relacionando **nº da seta** (`1.`, `2.`, `3.` — números normais, nunca ①②③) → campo → o que fazer.
- Sinalizar claramente o que é **obrigatório**.
- Caminhos de imagem no `.md` são **relativos** à pasta do manual: `imagens-tratadas/arquivo.png`.

---

## 5. Contas de acesso (produção https://beefood.app)

| Conta | Login | Senha | Observação |
|-------|-------|-------|------------|
| beefood1 | `beefood1` | `beefood123` | Conta de teste inicial (tem caixas históricos). |
| **BeeFood3 - Manual** | `contato@beefood.com.br` | `1q2w3e4r` | **Sandbox dedicado aos manuais.** Usar esta. |

> Login em `/login` (campos "Login de acesso" e "Senha", botão **ENTRAR**). Demora ~2-4s.
> **Trocar de conta:** menu de usuário (ícone pessoa, canto sup. direito) → **Sair**.

---

## 6. Ferramentas e procedimentos (navegador)

### No Windows (máquina do dono) — MCP do navegador

- MCP `cursor-ide-browser`: `browser_navigate`, `browser_snapshot`, `browser_take_screenshot`,
  `browser_click`, `browser_fill`, `browser_press_key`, `browser_lock`.
- Fluxo de lock: `navigate` → `lock` → interações → `unlock`.
- Screenshots brutos caem em `C:\Users\T-GAMER\AppData\Local\Temp\cursor\screenshots\`.
  Copiar os escolhidos para `imagens-puras\` do manual.
- **Tema:** SEMPRE **claro/branco** nas capturas. Ativar pelo botão **"Alterar tema"** (canto sup. direito).
- Refs do snapshot mudam a cada render — pegar snapshot novo antes de clicar se der "Element not found".

### No Cloud Agent (Linux) — capturar com Playwright

O MCP `cursor-ide-browser` **não existe** no Cloud Agent. Lá o navegador é o **Playwright**
(instalado pelo `.cursor/install.sh`), dirigido por script Python. O que funcionou no #2:

- Rodar com `export PATH="$HOME/.local/bin:$PATH"`.
- Logar uma vez e reaproveitar a sessão: `storage_state` salvo em arquivo e passado ao
  `new_context` — evita relogar em cada script (o login leva ~10s).
- `viewport={"width":1440,"height":900}` com `device_scale_factor=1.5` → imagens 2160×1350,
  nítidas o bastante para ler os valores das tabelas.
- Salvar o `screenshot` **direto** em `imagens-puras/` do manual.
- Fechar o **banner promocional** do topo antes de capturar (botão × do banner), senão ele
  aparece em todas as imagens.
- **Esperar bastante:** os modais de caixa levam de 8 a 13 segundos para carregar os dados.
- **Sempre escopar o clique dentro do modal certo:**
  `page.locator('div[role="dialog"]').filter(has_text="...").last`. As tabelas de fundo têm os
  mesmos textos e as mesmas classes (`bg-green-500`, badges "Débito"), e o clique vai para o
  elemento errado ou fica preso em "subtree intercepts pointer events".
- Quando a tela oferecer **atalho de teclado**, prefira-o ao clique (ex.: `Control+3` para
  escolher Débito no pagamento, `Enter` para confirmar). É mais robusto que caçar seletor.
- Dividir a captura em **scripts curtos por etapa**, deixando as ações irreversíveis (pagar,
  fechar caixa) em scripts separados dos idempotentes — assim é possível repetir a parte que
  falhou sem repetir o que não tem volta.

---

## 7. Regras de segurança em produção

- Decisão vigente: o ambiente "BeeFood3 - Manual" é **sandbox** → pode-se executar fluxos reais
  (abrir caixa, criar venda baixa, pagar) para o manual ficar fiel.
- Em contas que NÃO sejam sandbox: **não** finalizar vendas/pagamentos reais sem autorização.
- Nunca fazer ações destrutivas/irreversíveis sem confirmar com o usuário.

### Técnica do ensaio (para passos irreversíveis)

Muitas telas só gravam no clique final (fechar caixa, conferir, confirmar). Nesses casos,
**execute o fluxo inteiro uma vez sem o clique final**, capture tudo, revise as imagens e só
então repita para valer. Foi assim nos manuais de fechar caixa e de segunda conferência, e
evitou queimar cenários que não têm volta. Ao automatizar, mantenha o passo irreversível num
script separado dos idempotentes.

---

## 8. Stack do projeto (código) — referência

React 18 + TypeScript + Vite + Tailwind + shadcn/ui; react-router-dom v6; Supabase + API DataSnap
(`/datasnap/rest/...`); @tanstack/react-query; react-hook-form + zod. Versão em produção: `v3.190826.x`
(conferida em 19/08/2026 no rodapé do menu lateral).
Estrutura: `src/pages`, `src/components`, `src/hooks`, `src/contexts`, `src/integrations`.
Obs.: ainda **não existe `spec.md`** no projeto (a regra do projeto pede criar — pendente).

### Onde fica o código (por máquina)

| Máquina | Caminho do `beefood-web-react` |
|---------|--------------------------------|
| Windows (dono) | `C:\projetos\beefood-web-react` |
| Cloud Agent | `~/refs/beefood-web-react` (clone raso, **somente leitura**) |

No Cloud Agent o clone é feito pelo `.cursor/install.sh`. Para o clone funcionar são
necessárias **duas** liberações: o repositório precisa estar selecionado no **GitHub App do
Cursor** (configurações da org) **e** listado em `repositoryDependencies` no
`.cursor/environment.json` — esse campo não clona nada, ele só inclui o repositório no token
gerado para o ambiente. Faltando qualquer uma das duas, o clone falha com
`Repository not found`.

**O acesso vale durante a sessão inteira** (verificado em 2026-08-19). Dentro da sessão o
`git fetch origin main` em `~/refs/beefood-web-react` funciona normalmente, e `gh` também
enxerga o repositório. Ou seja: **dá para atualizar o código no meio do trabalho**, sem
precisar de uma sessão nova.

> Correção: até 2026-08-04 esta seção afirmava que o escopo valia só durante o install e que
> o código ficava congelado. Não é mais o caso.

Para conferir o que o token alcança: `gh api /installation/repositories -q '.total_count,
(.repositories[].full_name)'`. Hoje retorna **2**: `beefood-web-react` e
`beefood-web-react-manual`. Qualquer outro repositório (ex.: os de servidor, usados para
importar manuais de integração) responde **404** — e 404 aqui é ambíguo: significa "não
existe" **ou** "não liberado". Para liberar, são necessárias as duas coisas descritas acima
(GitHub App + `repositoryDependencies`).

---

## 9. Índice de manuais

| Manual | Pasta | Status |
|--------|-------|--------|
| Caixa (abrir, receber, consultar) | `manuais\caixa\` | ✅ Concluído |
| Fechar caixa (vendas pendentes, 1ª conferência, quebra) | `manuais\caixa-fechar\` | ✅ Concluído |
| Segunda conferência (dupla checagem, resolve a quebra) | `manuais\caixa-conferencia-2\` | ✅ Concluído |
| Reforma Tributária (IBS/CBS) | `manuais\reforma-tributaria-ibscbs\` | ✅ Concluído |
| Ativação Aiqfome V2 | `manuais\ativacao-aiqfome\` | ✅ Concluído |
| Integração Machine | `manuais\integracao-machine\` | ✅ Concluído |
| Integração 99 Entrega | `manuais\integracao-99-entrega\` | ✅ Concluído |
| Integração Repediu | `manuais\integracao-repediu\` | ✅ Concluído |
| Integração FoodCRM | `manuais\integracao-foodcrm\` | ✅ Concluído |
| Integração Uber Direct | `manuais\integracao-uber-direct\` | ✅ Concluído |

---

## 10. Como retomar o trabalho (checklist de início de sessão)

1. Ler este `MEMORIA-GERAL.md`.
2. Ler a `MEMORIA.md` do manual em andamento (se houver).
3. Logar em `contato@beefood.com.br` e ativar tema claro.
4. Conferir estado da funcionalidade no sistema antes de capturar.

---

## 11. Versionamento (Git/GitHub) — REGRA DE COMMIT POR AÇÃO

- Repositório remoto: `git@github.com:BeeFood-Sistema-para-Restaurantes/beefood-web-react-manual.git` (branch `main`).
- **REGRA DE OURO:** após **cada ação relevante** (criar/editar manual, gerar imagens,
  ajustar `annotate.py`, atualizar memórias, etc.), fazer **`commit` + `push` automaticamente**
  (sempre os dois!) — sem precisar pedir autorização. Mensagens claras e descritivas em português.
- **Sempre subir tudo:** todo commit deve ser seguido de `git push origin main`. Não deixar
  commits acumulados só localmente.
- Padrão de mensagem: verbo no presente + escopo. Ex.:
  `docs(caixa): adiciona etapa de consulta do valor em caixa`,
  `chore(anotacao): setas em verde e mais sutis`,
  `feat(manual): inicia manual de delivery`.
- Não versionar segredos novos: usar `.gitignore` (ex.: `credenciais.local.md`, `.env`).
  > **Decisão do dono:** as contas usadas são de uma **empresa de TESTES** (credenciais
  > descartáveis). Portanto as senhas PODEM ficar versionadas e o repositório PODE ser
  > **público** sem problema. Não tratar essas credenciais como segredo crítico.

---

## 12. `texto-documentation.ia.md` — PROMPT pronto por manual (OBRIGATÓRIO)

Para o dono **publicar** um manual, ele cola um **texto de criação** no construtor de documentação do
app (que gera a página dentro do BeeFood). Por isso, **todo manual concluído DEVE ter** um arquivo
`texto-documentation.ia.md` na sua pasta, contendo esse texto **pronto para copiar e colar**.

**Princípio:** o projeto do manual **já vem anexo no contexto**. O prompt deve ser **direto e listar os
arquivos EXATOS a ler** (o `<nome>.md` + os caminhos das imagens em `imagens-tratadas/`) e dizer
explicitamente **"NÃO varra/leia o resto do projeto"** (nada de `fluxo-codigo.md`, `MEMORIA*.md`,
`annotate.py`, `imagens-puras/`). Isso evita que a IA leia o projeto inteiro.

**O que o arquivo deve conter:**
1. Um bloco **PROMPT (copiar e colar)** com:
   - **Onde criar o menu** (ex.: "Em **Fiscal**, crie um novo item por último chamado **\<Nome\>**").
   - **Lista explícita dos arquivos a ler** (somente esses): o **`<nome>.md`** (conteúdo na íntegra) e os **caminhos de cada imagem** em `imagens-tratadas/` (na ordem).
   - Frase clara de **"NÃO ler outros arquivos do projeto"**.
   - A instrução: **"faça a apresentação das imagens igual ao menu 'Abrir Caixa'"** (padrão de referência).
2. **Estrutura da página** (seções, na ordem do `<nome>.md`).
3. **Tabela de imagens** na ordem, com tipo (contexto / com setas) e legenda.
4. **Observações de conteúdo** (idioma, destaques obrigatórios, o que NÃO publicar — ex.: `fluxo-codigo.md`).

**Modelo mínimo:**

```md
# texto-documentation.ia.md — <Nome do Manual>

## PROMPT (copiar e colar)
Em <Seção>, adicione um item de menu por último chamado "<Nome>".

Leia APENAS os arquivos abaixo (não varra o resto do projeto):
1. Conteúdo (use na íntegra): beefood-web-react-manual/manuais/<pasta>/<nome>.md
2. Imagens (nesta ordem): beefood-web-react-manual/manuais/<pasta>/imagens-tratadas/<arquivos...>

NÃO leia outros arquivos (fluxo-codigo.md, MEMORIA*.md, annotate.py, imagens-puras/).

- Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa".
- pt-BR, didático; destacar obrigatórios; não publicar o rodapé "Referências internas".

## Anexo — legendas das imagens (na ordem)
| Ordem | Arquivo (em imagens-tratadas/) | Tipo | Legenda |
| ... |
```

> Referência viva: `manuais\reforma-tributaria-ibscbs\texto-documentation.ia.md`.
