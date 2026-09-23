# MEMÓRIA — #104 Liberar o entregador

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `gestao-entregas-liberar-entregador.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Pasta: `manuais/gestao-entregas-liberar-entregador/` · Numeração: **#104** ·
Escrito em 18/09/2026 na sandbox **BeeFood3 - Manual** (`empresaID 38311`,
`filialID 39202`).

Primeiro manual do bloco **Gestão de Entregas 2.0** (plano em
[`PLANO-GESTAO-ENTREGAS.md`](../../.cursor/skills/manual-sistema/references/planos/PLANO-GESTAO-ENTREGAS.md)).
Ele existe por dois motivos: sem entregador cadastrado nenhum outro manual do bloco tem
cenário, e é ele que permite **aposentar o #57**.

## O recorte

Quatro passos, e nenhum deles é "a tela X tem os campos Y". A pergunta do lojista é *"como
eu ponho um motoboy novo para trabalhar?"*, e a resposta são dois cadastros em telas que
nem ficam perto uma da outra, mais uma configuração de impressão.

| Seção | Tela | Por que está aqui |
|---|---|---|
| 1 e 2 | Cadastros → Funcionários | a **pessoa**: é o que o painel de entregas lê |
| 3 | Configuração → Usuários | a **credencial**: é o que o app lê |
| 4 | Configuração → Impressão → Layout | o código de barras, que é como o motoboy confirma pelo celular |

## O que herdou do #57, e o que mudou

Herdou a Parte 1 do #57 (funcionário, usuário e código de barras), com prints novos, e a
foto do **cupom impresso** — que continua correta, porque o pé do cupom não mudou de
desenho. A Parte 2 do #57 (o app) **não** foi herdada: aquelas fotos são de uma versão
anterior do aplicativo e viram os manuais #111 a #116.

Três coisas que o #57 não dizia e este diz:

1. **Ler o código de barras é despachar.** O #57 dizia "o pedido fica atrelado a esse
   entregador", o que é verdade e é pouco: a leitura grava `ENTREGA`, avisa marketplace,
   imprime e enfileira WhatsApp. Está no `19-codigo-de-barras-no-3.md` do backend. Daí os
   dois avisos novos: não testar em pedido de cliente, e correção é pelo painel.
2. **A função é exclusiva.** *Garçom* e *Entregador* são rádio, não caixinha. Quem faz as
   duas coisas precisa de dois cadastros.
3. **Diária e valor por KM não afetam a entrega** — só o relatório de fechamento. O #57
   dizia "só para o seu controle", o que deixava o leitor na dúvida se travava algo.

## Decisões de captura

- **Recapturei tudo.** A primeira rodada tinha cinco telas sem `*.geo.json` e **não tinha a
  janela do usuário novo** — justamente onde mora o switch *Aplicativos*, que é a causa
  número um de "o app não aceita meu login". Manual de liberação sem essa tela seria manual
  incompleto.
- **Geometria pelo DOM.** Todas as setas saem de `getBoundingClientRect()` medido no mesmo
  instante do print (`/tmp/ge/c104.py`, `c104c.py`, `c104d.py`), como no #105.
- **Duas armadilhas de seletor**, que valem para os próximos manuais:
  - na janela do usuário, os rótulos *Funcionário* e *Gerente* também existem na **tabela
    atrás** da janela, e o seletor global mediu a camada de baixo. Escopo em
    `[role=dialog]` resolveu (`c104b.py`);
  - na lista de layouts, "o primeiro `svg` da linha" é o **ícone do rótulo**, não o lápis de
    editar. O lápis é o **último** botão da linha.
- **Nada foi alterado no sistema.** A caixinha *Código de Barras App Entrega* já estava
  marcada na sandbox, e o print é do estado real. Nenhum funcionário e nenhum usuário foram
  criados para este manual — as fichas mostradas são de cadastro que já existia
  (*Funcionário 1*) e da janela em branco de *Novo Usuário*.

## Aposentadoria do #57

O #57 pode sair do ar **quando os manuais #111 a #116 estiverem publicados**, e não agora:
este manual cobre a Parte 1 dele, mas a Parte 2 (usar o app) só é substituída pelo bloco do
app. Registrado também na linha do #57 no `CHECKLIST-MANUAIS.md`.

## Links que este manual faz

| Para | Estado |
|---|---|
| `../gestao-entregas-mapa-painel/` | ✅ existe (#105) |
| `../gestao-entregas-montar-rota/` | ✅ existe (#106) |
| `../entregador-quanto-recebe/` | ✅ existe (manual da taxa e do relatório Taxa/KM) |
| `../app-entregador-codigo-barras/` | ✅ existe (#114) |
| `../app-entregador-entrar/` | ✅ existe (#111) |
