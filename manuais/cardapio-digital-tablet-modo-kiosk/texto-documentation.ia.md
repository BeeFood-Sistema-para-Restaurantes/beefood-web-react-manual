# texto-documentation.ia.md — Modo Kiosk (travar o tablet no cardápio)

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.
> O projeto do manual **já está anexo no contexto** — o prompt aponta os **arquivos exatos** a ler.
>
> ✅ As 19 imagens já estão em `imagens-tratadas/`, conferidas pelo `validar-imagens.py`. A
> lista, com os nomes exatos e a tela de cada uma, está na `MEMORIA.md`.
>
> ⚠️ **Confirmar a seção do menu** antes de colar: o manual é de aplicativo Android, e o prompt
> abaixo assume a seção **Aplicativos**.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Aplicativos**, adicione um **item de menu por último** chamado **"Modo Kiosk — Travar o Tablet"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/cardapio-digital-tablet-modo-kiosk/cardapio-digital-tablet-modo-kiosk.md`

2. **Imagens (use estas 19, nesta ordem):**
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

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**

- Use o conteúdo do `cardapio-digital-tablet-modo-kiosk.md` **exatamente como está** (títulos, seções, tabelas e o FAQ). Não resuma e não reordene.
- Insira as 19 imagens na ordem acima — que é a ordem em que aparecem no `.md`. **Atenção:** a `19-home-travada.png` vem **antes** da `18-painel-destravar.png`; isso é proposital (o teste da Parte 4 vem antes do destravamento da Parte 5).
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- **Dezessete imagens trazem setas verdes com números**, e esses números são citados no texto de cada passo — em tabelas "Nº → o que fazer". Mantenha as tabelas junto da imagem correspondente e **não renumere nada**: o número da tabela tem de ser o mesmo desenhado na imagem. Não recorte as imagens, para não cortar setas.
- Só a `19-home-travada.png` e a `20-destravado.png` são de contexto, sem seta — de propósito, e o texto explica por quê.
- Idioma **português do Brasil**, tom didático (usuário final).
- Mantenha em destaque: a **senha da Administração é a mesma do login** do aplicativo; os botões físicos de **volume e ligar/desligar continuam funcionando** (limitação do Android); a **trava básica é menos segura** que a avançada; as permissões são concedidas **uma única vez por tablet**.
- Este é um manual de **aplicativo Android no tablet**. Não descreva o painel web — o evento *Travar* da tela Cardápio Digital Tablet é outra função e não faz parte deste manual.
- O manual **não cobre o login** no aplicativo: começa com o tablet já aberto no cardápio. Não acrescente passos de entrada com usuário e senha.
- Não publique o rodapé de referências internas nem qualquer conteúdo técnico.

---

## Estrutura da página (na ordem do `.md`)

1. Introdução (o que o manual ensina + versão do app e do Android nas capturas + o aviso de que os números verdes das imagens são citados no texto)
2. **Antes de começar** (requisitos e o aviso dos botões físicos)
3. **Visão geral do processo** (os 4 passos)
4. **Parte 1** — Abrir a tela de Administração
5. **Parte 2** — Conceder as duas permissões (Acessibilidade e Tela inicial padrão)
6. **Parte 3** — Ativar a trava
7. **Parte 4** — Conferir se está travado
8. **Parte 5** — Destravar o tablet
9. **Alternativa: trava básica (sem permissões)**
10. **Perguntas frequentes** (7 perguntas)

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Setas | Legenda |
|------:|----------------------------------|:-----:|---------|
| 1 | `03-home-logo.png` | 1 | Tela inicial do cardápio, com o logo no canto superior esquerdo |
| 2 | `04-senha-administracao.png` | 2 | Tela de Administração pedindo a senha de acesso |
| 3 | `05-painel-administracao.png` | 2 | Tela de Administração com as opções Atualizar, Travar e Configurar trava avançada |
| 4 | `06-assistente-inicio.png` | 4 | Assistente de trava mostrando as duas permissões pendentes |
| 5 | `07-aviso-acessibilidade.png` | 2 | Aviso explicando o uso do serviço de acessibilidade |
| 6 | `08-android-acessibilidade.png` | 1 | Configurações de Acessibilidade do Android com o serviço do aplicativo na lista |
| 7 | `09-android-servico-kiosk.png` | 1 | Tela do serviço Modo Kiosk com a chave desativada |
| 8 | `10-android-confirmar-servico.png` | 1 | Confirmação do Android para permitir o serviço |
| 9 | `11-android-servico-ativo.png` | 1 | Tela do serviço Modo Kiosk com a chave ativada |
| 10 | `12-assistente-1de2.png` | 3 | Assistente mostrando a permissão de acessibilidade concedida |
| 11 | `13-android-launcher.png` | 1 | Pergunta do Android sobre qual aplicativo usar como tela inicial |
| 12 | `14-android-launcher-selecionado.png` | 2 | Opção Cardápio Mesa/Comanda selecionada na lista |
| 13 | `15-assistente-pronto.png` | 2 | Assistente com as duas permissões concedidas e o botão Ativar modo kiosk |
| 14 | `16-kiosk-ativado.png` | 2 | Mensagem confirmando que o tablet está bloqueado |
| 15 | `17-app-fixado.png` | 1 | Aviso do Android informando que o aplicativo está fixado |
| 16 | `19-home-travada.png` | — | Cardápio continua na tela mesmo após apertar o botão Início |
| 17 | `18-painel-destravar.png` | 1 | Tela de Administração com o botão Destravar |
| 18 | `20-destravado.png` | — | Tela de Administração de volta ao estado destravado |
| 19 | `21-trava-basica.png` | 2 | Assistente oferecendo a opção de trava básica |

---

## Observações de conteúdo

- As capturas são do aplicativo **Cardápio Mesa/Comanda versão 1.0.2.8**, em tablet **Android 15**. Se o app mudar de versão e as telas mudarem, refazer as capturas antes de republicar.
- **Não há dado pessoal a cobrir.** As duas telas que mostravam a conta de teste eram as de login e de seleção de cardápio, e saíram do manual junto com a antiga Parte 1.
- As setas e os números são desenhados pelo `annotate.py` da própria pasta, que lê `imagens-puras/` e escreve `imagens-tratadas/`. Nunca edite as tratadas à mão: ajuste as coordenadas no script e rode de novo.
- **Não** publique nada do `fluxo-codigo.md` (rotas de API, eventos do painel, permissões internas).
- O texto de origem é `c:\projetos\beetech-appgarcom-android\docs\manual-modo-kiosk.md`. Se ele for atualizado, refazer a cópia em vez de editar aqui — o procedimento está na `MEMORIA.md`.
