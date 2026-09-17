# Como trabalhar neste repositório

Aqui se produz conteúdo sobre o sistema BeeFood, e existem **duas skills**. Antes
de escrever qualquer coisa, decida qual delas atende o pedido e leia o `SKILL.md`
dela até o fim.

| O pedido fala de… | Skill | Leia |
|---|---|---|
| manual, documentar tela, ajuda, passo a passo, "como usar" | `manual-sistema` | [`.cursor/skills/manual-sistema/SKILL.md`](.cursor/skills/manual-sistema/SKILL.md) |
| carrossel, post, arte, slides, divulgar novidade | `carrossel-novidades` | [`.cursor/skills/carrossel-novidades/SKILL.md`](.cursor/skills/carrossel-novidades/SKILL.md) |

As duas dividem o mesmo sandbox e as mesmas técnicas de captura de tela. O que
muda é o produto: uma ensina quem já usa o sistema, a outra vende o recurso para
quem ainda não conhece.

**A fronteira não se atravessa.** A skill de carrossel lê o material da de
manual, e não escreve nada dentro dele. Cada uma tem a sua memória, e o
aprendizado vai para a memória da skill que o descobriu:

| Skill | Memória | Saída |
|---|---|---|
| `manual-sistema` | `references/MEMORIA-GERAL.md` — **ler sempre no início da sessão** | `manuais/` |
| `carrossel-novidades` | `references/MEMORIA-CARROSSEIS.md` | `carrosseis/` |

Aprendizado de captura que serve para as duas (espera de spinner, conta de
teste, comportamento de tela) mora na `MEMORIA-GERAL.md`, e a skill de carrossel
mapeia o que ler em `references/conhecimento-compartilhado.md`.

## Regras que valem nas duas

- **Português do Brasil** em tudo: código, commit, documento e arte.
- **O repositório é público.** Nome, telefone e e-mail de cliente saem cobertos
  já na imagem **pura**, porque ela também é versionada. As credenciais de teste
  podem ficar versionadas: o ambiente é sandbox descartável.
- **Commit por ação relevante**, com mensagem clara em português, e `push` junto.
- **Nada de ação destrutiva** no sistema sem confirmar com o dono. Passo
  irreversível pede a técnica do ensaio (rodar o fluxo sem o clique final,
  revisar, e só então repetir para valer).
- `spec.md` tem a stack, as versões e o padrão de pastas. Leia antes de mexer na
  estrutura.
- **A tabela de manuais do `README.md` é gerada**, não editada à mão: ela fica
  entre os marcadores `INDICE-MANUAIS` e sai do
  `.cursor/skills/manual-sistema/scripts/indice-manuais.py`. Era mantida à mão e
  envelheceu para 63 linhas com 99 pastas.
