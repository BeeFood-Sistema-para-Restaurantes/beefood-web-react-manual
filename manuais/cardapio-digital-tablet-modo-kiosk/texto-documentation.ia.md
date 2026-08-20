# texto-documentation.ia.md — Modo Kiosk (travar o tablet no cardápio)

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.
> O projeto do manual **já está anexo no contexto** — o prompt aponta os **arquivos exatos** a ler.
>
> ⚠️ **Só publicar depois de subir as 21 imagens** para `imagens-tratadas/`. A lista completa,
> com os nomes exatos, está na `MEMORIA.md`.
>
> ⚠️ **Confirmar a seção do menu** antes de colar: o manual é de aplicativo Android, e o prompt
> abaixo assume a seção **Aplicativos**.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Aplicativos**, adicione um **item de menu por último** chamado **"Modo Kiosk — Travar o Tablet"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/cardapio-digital-tablet-modo-kiosk.md`

2. **Imagens (use estas 21, nesta ordem):**
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/01-login.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/02-selecionar-cardapio.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/03-home-logo.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/04-senha-administracao.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/05-painel-administracao.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/06-assistente-inicio.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/07-aviso-acessibilidade.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/08-android-acessibilidade.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/09-android-servico-kiosk.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/10-android-confirmar-servico.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/11-android-servico-ativo.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/12-assistente-1de2.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/13-android-launcher.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/14-android-launcher-selecionado.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/15-assistente-pronto.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/16-kiosk-ativado.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/17-app-fixado.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/19-home-travada.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/18-painel-destravar.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/20-destravado.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/imagens-tratadas/21-trava-basica.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `imagens-puras/`).

**Como montar a página:**

- Use o conteúdo do `cardapio-digital-tablet-modo-kiosk.md` **exatamente como está** (títulos, seções, tabelas e o FAQ). Não resuma e não reordene.
- Insira as 21 imagens na ordem acima — que é a ordem em que aparecem no `.md`. **Atenção:** a `19-home-travada.png` vem **antes** da `18-painel-destravar.png`; isso é proposital (o teste da Parte 5 vem antes do destravamento da Parte 6).
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- As imagens são de **contexto** (telas reais do aplicativo, sem setas nem números). Não invente setas nem referências numeradas.
- Idioma **português do Brasil**, tom didático (usuário final).
- Mantenha em destaque: a **senha da Administração é a mesma do login** do aplicativo; os botões físicos de **volume e ligar/desligar continuam funcionando** (limitação do Android); a **trava básica é menos segura** que a avançada; as permissões são concedidas **uma única vez por tablet**.
- Este é um manual de **aplicativo Android no tablet**. Não descreva o painel web — o evento *Travar* da tela Cardápio Digital Tablet é outra função e não faz parte deste manual.
- Não publique o rodapé de referências internas nem qualquer conteúdo técnico.

---

## Estrutura da página (na ordem do `.md`)

1. Introdução (o que o manual ensina + versão do app e do Android nas capturas)
2. **Antes de começar** (requisitos e os dois avisos importantes)
3. **Visão geral do processo** (os 5 passos)
4. **Parte 1** — Entrar no aplicativo
5. **Parte 2** — Abrir a tela de Administração
6. **Parte 3** — Conceder as duas permissões (Acessibilidade e Tela inicial padrão)
7. **Parte 4** — Ativar a trava
8. **Parte 5** — Conferir se está travado
9. **Parte 6** — Destravar o tablet
10. **Alternativa: trava básica (sem permissões)**
11. **Perguntas frequentes** (7 perguntas)

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-login.png` | contexto | Tela de login do aplicativo com usuário e senha preenchidos |
| 2 | `02-selecionar-cardapio.png` | contexto | Tela de seleção de cardápio com duas opções listadas |
| 3 | `03-home-logo.png` | contexto | Tela inicial do cardápio, com o logo no canto superior esquerdo |
| 4 | `04-senha-administracao.png` | contexto | Tela de Administração pedindo a senha de acesso |
| 5 | `05-painel-administracao.png` | contexto | Tela de Administração com as opções Atualizar, Travar e Configurar trava avançada |
| 6 | `06-assistente-inicio.png` | contexto | Assistente de trava mostrando as duas permissões pendentes |
| 7 | `07-aviso-acessibilidade.png` | contexto | Aviso explicando o uso do serviço de acessibilidade |
| 8 | `08-android-acessibilidade.png` | contexto | Configurações de Acessibilidade do Android com o serviço do aplicativo na lista |
| 9 | `09-android-servico-kiosk.png` | contexto | Tela do serviço Modo Kiosk com a chave desativada |
| 10 | `10-android-confirmar-servico.png` | contexto | Confirmação do Android para permitir o serviço |
| 11 | `11-android-servico-ativo.png` | contexto | Tela do serviço Modo Kiosk com a chave ativada |
| 12 | `12-assistente-1de2.png` | contexto | Assistente mostrando a permissão de acessibilidade concedida |
| 13 | `13-android-launcher.png` | contexto | Pergunta do Android sobre qual aplicativo usar como tela inicial |
| 14 | `14-android-launcher-selecionado.png` | contexto | Opção Cardápio Mesa/Comanda selecionada na lista |
| 15 | `15-assistente-pronto.png` | contexto | Assistente com as duas permissões concedidas e o botão Ativar modo kiosk |
| 16 | `16-kiosk-ativado.png` | contexto | Mensagem confirmando que o tablet está bloqueado |
| 17 | `17-app-fixado.png` | contexto | Aviso do Android informando que o aplicativo está fixado |
| 18 | `19-home-travada.png` | contexto | Cardápio continua na tela mesmo após apertar o botão Início |
| 19 | `18-painel-destravar.png` | contexto | Tela de Administração com o botão Destravar |
| 20 | `20-destravado.png` | contexto | Tela de Administração de volta ao estado destravado |
| 21 | `21-trava-basica.png` | contexto | Assistente oferecendo a opção de trava básica |

---

## Observações de conteúdo

- As capturas são do aplicativo **Cardápio Mesa/Comanda versão 1.0.2.8**, em tablet **Android 15**. Se o app mudar de versão e as telas mudarem, refazer as capturas antes de republicar.
- As telas mostram a conta de teste **BeeFood3 - Manual** (e **TESTES 1** na seleção de cardápio). São credenciais descartáveis, pode publicar.
- **Não** publique nada do `fluxo-codigo.md` (rotas de API, eventos do painel, permissões internas).
- O texto de origem é `c:\projetos\beetech-appgarcom-android\docs\manual-modo-kiosk.md`. Se ele for atualizado, refazer a cópia em vez de editar aqui — o procedimento está na `MEMORIA.md`.
