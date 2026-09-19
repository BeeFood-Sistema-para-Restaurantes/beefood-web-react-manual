# Como trabalhar neste repositório

Aqui se produz conteúdo sobre o sistema BeeFood. Há **duas skills de produto** —
uma escreve manual, a outra faz carrossel — e **uma de apoio**, que monta na
sandbox o cenário que as duas precisam fotografar. Antes de escrever qualquer
coisa, decida qual atende o pedido e leia o `SKILL.md` dela até o fim.

| O pedido fala de… | Skill | Leia |
|---|---|---|
| manual, documentar tela, ajuda, passo a passo, "como usar" | `manual-sistema` | [`.cursor/skills/manual-sistema/SKILL.md`](.cursor/skills/manual-sistema/SKILL.md) |
| carrossel, post, arte, slides, divulgar novidade **ou função do sistema** | `carrossel` | [`.cursor/skills/carrossel/SKILL.md`](.cursor/skills/carrossel/SKILL.md) |
| smoke teste, semear pedido, forjar origem, marketplace de teste, inserir no banco — ou **falta dado na tela para fotografar** | `cenario-sandbox` | [`.cursor/skills/cenario-sandbox/SKILL.md`](.cursor/skills/cenario-sandbox/SKILL.md) |

As duas dividem o mesmo sandbox e as mesmas técnicas de captura de tela. O que
muda é o produto: uma ensina quem já usa o sistema, a outra vende o recurso para
quem ainda não conhece. A de carrossel tem **dois gêneros** — novidade
publicada e função do sistema (uma página de `beefood.com.br`, um tema, um
segmento) — e o que muda entre eles é o leitor: na novidade ele já é cliente, na
função ele pode estar escolhendo sistema.

**A fronteira não se atravessa.** A skill de carrossel lê o material da de
manual, e não escreve nada dentro dele. Cada uma tem a sua memória, e o
aprendizado vai para a memória da skill que o descobriu:

| Skill | Memória | Saída |
|---|---|---|
| `manual-sistema` | `references/MEMORIA-GERAL.md` — **ler sempre no início da sessão** | `manuais/` |
| `carrossel` | `references/MEMORIA-CARROSSEIS.md` | `carrosseis/` |
| `cenario-sandbox` | o próprio `SKILL.md` | nada — ela mexe no **sandbox**, e os scripts moram na pasta do manual que os pediu |

Aprendizado de captura que serve para as duas (espera de spinner, conta de
teste, comportamento de tela) mora na `MEMORIA-GERAL.md`, e a skill de carrossel
mapeia o que ler em `references/conhecimento-compartilhado.md`. Aprendizado de
**cenário** — de onde um campo vem, qual rota grava o quê, como escrever no banco
sem risco — mora na `cenario-sandbox`.

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
