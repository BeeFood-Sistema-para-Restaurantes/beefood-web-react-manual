# MEMÓRIA GERAL — Boas práticas para criação de manuais BeeFood

> Memória mestre do projeto de manuais. **Ler SEMPRE no início de cada sessão.**
> Cada manual tem ainda sua própria `MEMORIA.md` dentro da sua pasta.

Última atualização: 2026-06-18 (adicionado versionamento Git + regra de commit por ação)

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
5. Cada foto essencial leva **setas vermelhas + número** (①②③...). O texto do manual
   referencia cada número e destaca campos **obrigatórios (\*)**.
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
- Cada etapa: passos numerados + imagem tratada + **tabela** relacionando Nº da seta → campo → o que fazer.
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

- MCP `cursor-ide-browser`: `browser_navigate`, `browser_snapshot`, `browser_take_screenshot`,
  `browser_click`, `browser_fill`, `browser_press_key`, `browser_lock`.
- Fluxo de lock: `navigate` → `lock` → interações → `unlock`.
- Screenshots brutos caem em `C:\Users\T-GAMER\AppData\Local\Temp\cursor\screenshots\`.
  Copiar os escolhidos para `imagens-puras\` do manual.
- **Tema:** SEMPRE **claro/branco** nas capturas. Ativar pelo botão **"Alterar tema"** (canto sup. direito).
- Refs do snapshot mudam a cada render — pegar snapshot novo antes de clicar se der "Element not found".

---

## 7. Regras de segurança em produção

- Decisão vigente: o ambiente "BeeFood3 - Manual" é **sandbox** → pode-se executar fluxos reais
  (abrir caixa, criar venda baixa, pagar) para o manual ficar fiel.
- Em contas que NÃO sejam sandbox: **não** finalizar vendas/pagamentos reais sem autorização.
- Nunca fazer ações destrutivas/irreversíveis sem confirmar com o usuário.

---

## 8. Stack do projeto (código) — referência

React 18 + TypeScript + Vite + Tailwind + shadcn/ui; react-router-dom v6; Supabase + API DataSnap
(`/datasnap/rest/...`); @tanstack/react-query; react-hook-form + zod. Versão em produção: `v3.180626.x`.
Estrutura: `src/pages`, `src/components`, `src/hooks`, `src/contexts`, `src/integrations`.
Obs.: ainda **não existe `spec.md`** no projeto (a regra do projeto pede criar — pendente).

---

## 9. Índice de manuais

| Manual | Pasta | Status |
|--------|-------|--------|
| Caixa (abrir, receber, consultar) | `manuais\caixa\` | ✅ Concluído |
| Reforma Tributária (IBS/CBS) | `manuais\reforma-tributaria-ibscbs\` | ✅ Concluído |

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
  ajustar `annotate.py`, atualizar memórias, etc.), **fazer um commit automaticamente** —
  sem precisar pedir autorização. Mensagens claras e descritivas em português.
- O **push** para o GitHub NÃO é automático a cada commit — fazer push quando o usuário pedir
  ou ao final de um bloco de trabalho.
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

**O que o arquivo deve conter:**
1. Um bloco **PROMPT (copiar e colar)** com:
   - **Onde criar o menu** (ex.: "Em **Fiscal**, crie um novo item por último chamado **\<Nome\>**").
   - Referência ao **projeto/pasta** do manual e ao **`<nome>.md`** (conteúdo na íntegra).
   - Referência **apenas** a **`imagens-tratadas\`** (contém TODAS as imagens; `imagens-puras\` NÃO é referenciada).
   - A instrução: **"faça a apresentação das imagens igual ao menu 'Abrir Caixa'"** (padrão de referência).
2. **Estrutura da página** (seções, na ordem do `<nome>.md`).
3. **Tabela de imagens** na ordem, com tipo (contexto / com setas) e legenda.
4. **Observações de conteúdo** (idioma, destaques obrigatórios, o que NÃO publicar — ex.: `fluxo-codigo.md`).

**Modelo mínimo:**

```md
# texto-documentation.ia.md — <Nome do Manual>

## PROMPT (copiar e colar)
Em <Seção>, crie um novo item de menu por último chamado "<Nome>".
Monte a página com base no projeto anexo beefood-web-react-manual\manuais\<pasta>:
- Texto/passo a passo em `<nome>.md` (use na íntegra).
- TODAS as imagens estão em `imagens-tratadas\` (use só esta pasta).
- Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa".

### Estrutura da página
1. ... (seções na ordem do .md)

### Imagens (na ordem, com legendas)
| Ordem | Arquivo | Tipo | Legenda |
| ... |

### Observações
- pt-BR, didático; destacar obrigatórios; NÃO publicar `fluxo-codigo.md`.
```

> Referência viva: `manuais\reforma-tributaria-ibscbs\texto-documentation.ia.md`.
