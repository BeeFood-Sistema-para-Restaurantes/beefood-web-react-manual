---
name: manual-sistema
description: Produz manual de funcionalidade para o usuário final do BeeFood — passo a passo em markdown, com capturas reais de produção anotadas com setas verdes numeradas, e o prompt de publicação. Use quando o pedido falar de manual, documentar tela, explicar como usar, ajuda ou passo a passo. Não use para arte de divulgação — carrossel de Instagram tem skill própria (carrossel).
---

# Manual de funcionalidade do BeeFood

Transforma uma funcionalidade do sistema em **manual para quem usa o
restaurante**: o que a tela faz, na ordem em que a pessoa mexe nela, com
captura real de produção e seta numerada em cada campo que importa.

A matéria-prima são duas: o **código** do `beefood-web-react`, para entender o
que a tela grava de verdade, e a **produção** em `https://beefood.app`, para
fotografar. Nada é desenhado.

## Quando usar, e quando não

| Pedido | Onde ele é atendido |
|--------|---------------------|
| "cria o manual de X", "documenta a tela Y", "atualiza o manual Z" | **aqui** |
| "estuda o bloco X e propõe os manuais" | aqui — sai um `PLANO-X.md` em `references/planos/` |
| "faz um carrossel da novidade X", "post para o Instagram", "arte" | `carrossel` — **não é esta skill** |
| "faz smoke teste", "semeia pedido de marketplace", "insere no banco" | `cenario-sandbox` — a skill de apoio que monta o cenário |

As duas skills dividem o mesmo sandbox e as mesmas técnicas de captura. O que
muda é o produto: aqui sai passo a passo para quem opera; lá sai peça de venda
para quem ainda não conhece o recurso.

Esta skill escreve em `manuais/` e na própria pasta. A de carrossel escreve em
`carrosseis/` e **lê** o que está aqui — ela não altera a
[`MEMORIA-GERAL.md`](references/MEMORIA-GERAL.md) nem nada em `manuais/`.

## Leia antes de começar

Esta página é a porta de entrada, não o conteúdo. O conhecimento está em:

| Arquivo | O que tem |
|---------|-----------|
| [`references/MEMORIA-GERAL.md`](references/MEMORIA-GERAL.md) | **a memória mestre — ler SEMPRE no início da sessão.** Doze seções: padrão de pasta, de imagem, de escrita, contas, ferramentas, segurança, stack, índice dos manuais e o prompt de publicação |
| [`references/CHECKLIST-MANUAIS.md`](references/CHECKLIST-MANUAIS.md) | o que está pronto, o que está aprovado e o backlog com numeração (`#NN`) |
| [`references/planos/`](references/planos/) | estudo de um bloco inteiro antes de virar manual (cardápio, parâmetros, relatórios, entregador…) |
| `manuais/<nome>/MEMORIA.md` | a memória do manual em andamento |

Depois da memória geral, a ordem de retomada é a da seção 10 dela: plano do
bloco (se houver), `MEMORIA.md` do manual, login no sandbox com tema claro, e
conferir o estado da funcionalidade no sistema antes de fotografar.

## O fluxo

1. **Pauta.** O assunto vem do `CHECKLIST-MANUAIS.md` (com o número `#NN`) ou de
   um pedido direto. Bloco grande vira primeiro um plano em
   `references/planos/`, para o dono aprovar o recorte antes da produção.
2. **Código.** Ler no `beefood-web-react` o que a tela grava: se tem auto-save,
   em que linha o `handleSave` chama a API, o que cada switch faz de fato. Sai o
   `fluxo-codigo.md` da pasta do manual. Cinco minutos aqui evitam captura em
   cenário queimado.
3. **Cenário.** Conferir no sandbox se o estado que o manual precisa existe —
   e montá-lo quando não existir. Passo irreversível pede a **técnica do
   ensaio**: rodar o fluxo inteiro sem o clique final, revisar, e só então
   repetir para valer. Quando o estado é daqueles que a tela **não sabe criar**
   (pedido de iFood, pedido atrasado, pedido já pago), o caminho está na skill
   [`cenario-sandbox`](../cenario-sandbox/SKILL.md) — inclusive a ordem que evita
   ir direto ao banco.
4. **Captura.** Print de produção em `imagens-puras/`, numerado por etapa
   (`NN-descricao.png`). Tema claro, sempre. **Depois de cada clique, espere o
   spinner sumir e mais 5 segundos** — esta é a regra que mais se repete, e vale
   para todo manual.
5. **Anotação.** `annotate.py` da pasta do manual desenha seta verde e número
   sobre a pura e grava em `imagens-tratadas/`, que é a **única** pasta
   referenciada pelo `.md`. Coordenada em fração de 0 a 1, para não depender da
   resolução. Imagem de contexto entra por `passthrough()`.
6. **Escrita.** Título → objetivo → pré-requisitos → etapas numeradas → dicas.
   Cada etapa tem os passos, a imagem tratada e a tabela **nº da seta → campo →
   o que fazer**. Número só em duas posições: `(N)` no parágrafo imediatamente
   **antes** da imagem, ou na tabela imediatamente **depois** dela. Para seta de
   imagem anterior, escrever "a seta N da imagem acima".
7. **Publicação.** Todo manual concluído leva um `texto-documentation.ia.md`: o
   prompt pronto para o dono colar no construtor de documentação do app. Ele
   começa pela **REGRA ZERO** e só então lista os arquivos exatos a ler.

8. **Entrega.** Fechado o merge na `main`, a resposta ao dono termina com **a lista
   das pastas entregues e a instrução de leitura** — o que colar no construtor, o
   que ele pode ler e o que ele **não** pode. É isso que o dono repassa na hora de
   publicar. Forma exata na seção 11 da
   [`MEMORIA-GERAL.md`](references/MEMORIA-GERAL.md).

> **O manual é "como eu uso", nunca "como o sistema faz".** Rota de API, nome de
> campo, nome de arquivo e jargão de programador moram no `fluxo-codigo.md` e
> **não** entram no `<nome>.md` — nem num rodapé "não publicar", porque é o
> arquivo que o construtor lê na íntegra. Em 23/09/2026 uma página publicada saiu
> com a rota da API do cupom porque o construtor leu o `fluxo-codigo.md` da pasta
> por conta própria. Daí a REGRA ZERO na primeira linha do prompt, o aviso
> `⛔ DOCUMENTO INTERNO` no alto de cada arquivo interno, e o
> `conferir-vazamento.py`.

## Antes de dar por concluído

```bash
SK=.cursor/skills/manual-sistema/scripts

python $SK/validar-imagens.py                    # ou com <pasta-do-manual>
python $SK/conferir-vazamento.py                 # ou com <prefixo-de-pasta>
python $SK/indice-manuais.py                     # reescreve o índice do README
python $SK/indice-manuais.py --conferir          # só acusa, não escreve
```

O `validar-imagens.py` confere, em todos os manuais, se toda imagem referenciada
existe em `imagens-tratadas/`, se o prompt de publicação não lista imagem que o
manual não usa, e se há órfão na pasta. **Sai com código 1 quando falta imagem**,
porque manual com imagem faltando quebra em silêncio: o markdown continua válido,
o texto continua legível, e só quem abre a página publicada descobre.

O `conferir-vazamento.py` lê **só o arquivo publicável** de cada pasta e acusa rota
de API, nome de arquivo de código, `campo=true` e jargão de programador. Sai com
código 1 quando acha algo. Ele sabe poupar o que é conteúdo do lojista: URL de
webhook que se cola no painel do parceiro, "Resumo do caminho" dentro de bloco
cercado e jargão que é rótulo de tela.

O `indice-manuais.py` reescreve a tabela do `README.md` a partir das pastas,
lendo o título no H1 de cada manual. Ele existe porque a tabela era mantida à mão
e chegou a 99 pastas com 63 linhas: trinta e seis manuais prontos não apareciam
para quem abre o repositório, e nada quebrava.

Fechado o manual, atualizar três lugares à mão: a `MEMORIA.md` da pasta, o índice
da seção 9 da `MEMORIA-GERAL.md` e a linha do `CHECKLIST-MANUAIS.md`. O README
sai do script.

## O que nunca fazer

- **Printar tela ainda carregando.** É o erro que mais volta na revisão.
- **Publicar dado pessoal.** O repositório é público: nome, telefone e e-mail de
  cliente saem cobertos na imagem **pura**, não só na tratada, porque a pura
  também é versionada.
- **Número circulado** (①②③) em lugar nenhum — só `1.`, `2.`, `3.`.
- **Referenciar `imagens-puras/`** no `.md` ou no prompt de publicação. Ela é
  backup.
- **Falar de código no `<nome>.md`**: rota de API, nome de campo, nome de arquivo,
  *backend*, *endpoint*, *payload*. Nem num rodapé marcado "não publicar".
- **Ação destrutiva sem confirmar** com o dono, e venda ou pagamento real em
  conta que não seja o sandbox.
- **Desligar a permissão "Usuários"** do grupo `Administrador2`: o usuário
  Principal não ignora as restrições do grupo, e não há como religar de dentro
  do sistema.

## A estrutura que isto produz

```
manuais/<nome-do-manual>/
├── MEMORIA.md                  # memória do manual: fluxo, uso, decisões, estado
├── <nome>.md                   # o manual final, para o usuário
├── fluxo-codigo.md             # o que a tela faz de verdade, lido no código
├── texto-documentation.ia.md   # prompt de publicação
├── annotate.py                 # setas e números deste manual
├── imagens-puras/              # print original, backup, nunca referenciado
└── imagens-tratadas/           # toda imagem do manual — a única referenciada
```
