# MEMÓRIA — Manual do Modo Kiosk (Cardápio Digital Tablet)

> Memória detalhada deste manual (fluxo, uso, decisões e estado), para retomar a qualquer momento.
> Ver também a memória geral: `../../MEMORIA-GERAL.md`.

Status: 🔨 **Texto pronto — faltam as 21 imagens** — Última atualização: 2026-08-20

---

## 1. Escopo do manual

O manual é **só do aplicativo Android** *Cardápio Mesa/Comanda*, no próprio tablet. Ensina o
gestor a travar o aparelho no cardápio:

1. Entrar no app (login e seleção de cardápio).
2. Abrir a tela de **Administração** (toque no logo, no canto superior esquerdo + senha).
3. Conceder as duas permissões do Android pelo assistente (**Acessibilidade** e
   **Launcher padrão**).
4. **ATIVAR MODO KIOSK**.
5. Conferir se travou (botão Início e barra de notificações).
6. **DESTRAVAR** quando precisar.

Fecha com a alternativa da **trava básica** (screen pinning, sem permissões) e um FAQ de sete
perguntas.

**Fora do escopo:** o painel web. O evento `TRAVAR` da aba Tablets é outra coisa — está
mapeado no `fluxo-codigo.md`, com a tabela que diferencia as três travas.

Arquivo final: `cardapio-digital-tablet-modo-kiosk.md`.

## 2. Origem do texto — copiado, não reescrito

O manual **já veio escrito** pelo dono, em
`c:\projetos\beetech-appgarcom-android\docs\manual-modo-kiosk.md`. Seguindo o que o
repositório já fez nos manuais **#8 (99 Entrega)** e **#11 (Uber Direct)**, o arquivo foi
copiado **como está**, sem reinterpretar. As duas únicas alterações:

- caminhos `images/kiosk/` → `imagens-tratadas/`;
- fim de linha CRLF → LF.

Comprovação:

```bash
diff <(sed 's|images/kiosk/|imagens-tratadas/|g' manual-modo-kiosk.md | tr -d '\r') \
     manuais/cardapio-digital-tablet-modo-kiosk/cardapio-digital-tablet-modo-kiosk.md
# sem saída
```

> **Se o texto de origem for atualizado, refazer a cópia** com esse mesmo comando, em vez de
> editar o arquivo aqui.

## 3. O que ainda falta: as 21 imagens

O `.md` chegou como arquivo (foi para `~/.cursor/projects/workspace/uploads/`), mas as
**imagens só chegaram como imagem no chat, não como arquivo em disco** — a pasta de uploads
recebeu apenas o `.md`, e nenhum `.png` novo apareceu no sistema de arquivos.

**Para fechar o manual:** anexar os 21 PNG do jeito que o `.md` foi anexado (aí eles caem em
disco), ou commitá-los numa branch. Origem:
`c:\projetos\beetech-appgarcom-android\docs\images\kiosk\`.

Os nomes têm de ser exatamente estes, em `imagens-tratadas/` (e cópia em `imagens-puras/`):

| # | Arquivo | Tela |
|---|---------|------|
| 1 | `01-login.png` | Login do app, e-mail e senha preenchidos |
| 2 | `02-selecionar-cardapio.png` | *Selecione um cardápio* (BeeFood3 - Manual / TESTES 1) |
| 3 | `03-home-logo.png` | Tela inicial do cardápio, com o logo no topo à esquerda |
| 4 | `04-senha-administracao.png` | *Administração* pedindo a senha, com o teclado aberto |
| 5 | `05-painel-administracao.png` | Painel destravado: ATUALIZAR, TRAVAR, CONFIGURAR TRAVA AVANÇADA |
| 6 | `06-assistente-inicio.png` | *Bloquear tablet (Modo Kiosk)* — 0 de 2 permissões |
| 7 | `07-aviso-acessibilidade.png` | *Uso do serviço de acessibilidade* (consentimento) |
| 8 | `08-android-acessibilidade.png` | Android → Acessibilidade, serviço em *Apps baixados* |
| 9 | `09-android-servico-kiosk.png` | Página do serviço com a chave desativada |
| 10 | `10-android-confirmar-servico.png` | Android pedindo *Permitir* controle total |
| 11 | `11-android-servico-ativo.png` | Página do serviço com a chave ativada (azul) |
| 12 | `12-assistente-1de2.png` | Assistente — 1 de 2, Acessibilidade em verde |
| 13 | `13-android-launcher.png` | *Definir app de início padrão?* com o Pixel marcado |
| 14 | `14-android-launcher-selecionado.png` | Mesma tela com *Cardápio Mesa/Comanda* marcado |
| 15 | `15-assistente-pronto.png` | Assistente — 2 de 2 e o botão **ATIVAR MODO KIOSK** |
| 16 | `16-kiosk-ativado.png` | Alerta *Tablet bloqueado (Modo Kiosk)* |
| 17 | `17-app-fixado.png` | Aviso do Android *O app está fixado* |
| 18 | `19-home-travada.png` | Cardápio na tela depois do teste do botão Início |
| 19 | `18-painel-destravar.png` | Painel travado: ATUALIZAR e **DESTRAVAR** |
| 20 | `20-destravado.png` | Painel de volta ao estado destravado |
| 21 | `21-trava-basica.png` | Assistente com **PULAR E USAR TRAVA BÁSICA AGORA** (laranja) |

> A ordem de exibição não é a ordem numérica: a `19` aparece **antes** da `18`, porque o teste
> da Parte 5 vem antes do destravamento da Parte 6. É assim no texto de origem — manter.

**Não haverá `annotate.py`.** As capturas do dono já são as definitivas, sem setas nem
números — o texto não referencia número de seta em nenhum ponto. Por isso todas entram em
`imagens-tratadas/` como imagens de contexto, igual ao que foi feito nos manuais importados
(#7, #8, #11).

## 4. Histórico (o caminho até aqui)

| Quando | O que aconteceu |
|--------|-----------------|
| 1ª rodada | Pedido chegou citando o `manual-modo-kiosk.md` e a pasta `images` como anexos. **Nada chegou ao VM.** Escrevi um rascunho com o escopo errado (o painel web) e mapeei o código do painel. |
| 2ª rodada | O dono mandou as 21 imagens no chat e esclareceu: **o manual é só no tablet**. Informou o caminho de origem, `c:\projetos\beetech-appgarcom-android\docs\manual-modo-kiosk.md`. Testei o acesso ao repositório do app no Bitbucket: **sem acesso** (o `BITBUCKET_TOKEN` alcança só o `beetech-server-node-2.0`). |
| 3ª rodada | O `.md` foi anexado de um jeito que **caiu em disco**. Manual copiado, escopo corrigido, `texto-documentation.ia.md` escrito. Sobraram só as imagens. |

**Lição principal, já registrada no `MEMORIA-GERAL.md`:** anexo do chat não chega ao VM por
padrão. Quando cai em `~/.cursor/projects/workspace/uploads/`, chegou; se não estiver lá, não
chegou. Vale conferir essa pasta antes de concluir que o material não existe.

## 5. Decisões tomadas

- **Copiar, não reescrever.** O texto do dono já está no tom certo e descreve telas que eu não
  tenho como validar sozinho (o código do app é inacessível). Reescrever só criaria risco de
  divergência.
- **Descartei o rascunho da 1ª rodada.** Ele documentava o painel web, que o dono disse
  explicitamente não ser o assunto. O trabalho não foi perdido: virou o `fluxo-codigo.md`.
- **Mantive o `fluxo-codigo.md`** com uma tabela que separa as três travas. Foi a confusão que
  me fez errar o escopo na primeira rodada, e é a mesma confusão que o suporte tende a ter.
- **`texto-documentation.ia.md` já escrito**, mas a publicação depende das imagens.

## 6. Detalhes técnicos que o texto de origem traz

- Versão do app nas capturas: **1.0.2.8**, em tablet **Android 15**.
- A senha da tela de **Administração** é a **mesma do login** do app.
- As duas permissões: **Acessibilidade** (detecta a tentativa de sair e devolve o app) e
  **Launcher padrão** (faz o botão Início abrir o cardápio).
- **Volume e power não são bloqueáveis** sem provisionar o tablet como *Device Owner*, o que
  exige reset de fábrica. Está avisado na própria tela do assistente.
- A trava **sobrevive ao reinício** do tablet.
- Fabricantes como Xiaomi e Motorola podem matar o app em segundo plano: marcar o app como
  **sem restrição** na otimização de bateria.
