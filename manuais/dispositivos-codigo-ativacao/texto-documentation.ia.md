# texto-documentation.ia.md — #131 Código de ativação de aparelho (Dispositivos)

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Configuração**, adicione um manual por último chamado
**"Código de ativação de aparelho (Dispositivos)"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/dispositivos-codigo-ativacao/dispositivos-codigo-ativacao.md`

2. **Imagens (use estas 5, nesta ordem):**
   - `beefood-web-react-manual/manuais/dispositivos-codigo-ativacao/imagens-tratadas/01-tela-dispositivos.png`
   - `beefood-web-react-manual/manuais/dispositivos-codigo-ativacao/imagens-tratadas/02-modal-codigo-app-garcom.png`
   - `beefood-web-react-manual/manuais/dispositivos-codigo-ativacao/imagens-tratadas/03-modal-codigo-qr-app-entregador.png`
   - `beefood-web-react-manual/manuais/dispositivos-codigo-ativacao/imagens-tratadas/05-codigo-aguardando-ativacao.png`
   - `beefood-web-react-manual/manuais/dispositivos-codigo-ativacao/imagens-tratadas/04-modal-sem-vaga-totem.png`

**NÃO leia outros arquivos** (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `capturar.py`,
`conferir-setas.py`, `imagens-puras/`).

- Faça a apresentação das imagens **igual** ao menu **"Abrir Caixa"**.
- A ordem das imagens **não** é a ordem do nome do arquivo: a `04` (sem vaga) entra por último,
  porque no `.md` ela pertence à seção *Quando não há vaga livre*, depois do Passo 4.
- pt-BR, didático; o leitor é o **lojista** com o aparelho na mão, querendo pôr o App Garçom,
  o App Entregador, o totem ou o tablet para funcionar agora.
- **Manual curto, de propósito.** Ele cobre só a geração do código de ativação. A quantidade de
  aparelhos de cada plano é assunto da página de **planos e preços** e não entra aqui.
- Não publicar o rodapé de referências internas.
- Palavras que o leitor vai buscar e que devem sobreviver na página: *código de ativação*,
  *ativar aparelho*, *ativar dispositivo*, *gerar código*, *ativar App Garçom*,
  *ativar App Entregador*, *ativar totem*, *ativar tablet*, *QR de ativação*,
  *código expirou*, *código aguardando ativação*, *cancelar código*,
  *já uso todos os aparelhos do plano*, *vagas do plano*, *remover aparelho*,
  *renomear aparelho*, *Configurações Dispositivos*.

## Estrutura da página (na ordem do `.md`)

1. Título e abertura — o que é o código, o formato `XXX-XXX`, e o aviso de que o QR é a
   alternativa nos aparelhos com câmera. O parágrafo que diz o que **não** está aqui
   (quantidade por plano) deve ficar.
2. Antes de começar — acesso ao grupo *Configuração*, aplicativo já instalado, vaga livre e os
   quinze minutos de validade.
3. **Passo 1** — abrir *Configuração → Dispositivos*: o item do menu, a linha de vagas e o
   botão **Ativar aparelho** de cada faixa, mais o aviso de que o código é **por tipo**.
4. **Passo 2** — a janela já abre com o código gerado: os três passos, o código, o **Copiar** e
   a contagem. Mais o aviso de que o código **já reservou uma vaga**.
5. **Passo 3** — informar o código no aparelho, e a variação do QR nos aparelhos com câmera
   (App Entregador e cardápio digital em tablet).
6. **Passo 4** — o código na lista depois de fechar a janela, e o **Cancelar** que devolve a
   vaga.
7. **Quando não há vaga livre** — a janela de limite e as duas saídas sem mexer no plano.
8. Quando algo não funciona — tabela sintoma/verificação.
9. Perguntas frequentes.
10. Precisa de ajuda? e Onde continuar.

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Seção | Tipo | Legenda |
|---|---|---|---|---|
| 1 | `01-tela-dispositivos.png` | Passo 1 | com setas (3) | A tela **Dispositivos**: o item no grupo *Configuração*, a linha **15 de 15 livres** e o botão **Ativar aparelho** da faixa |
| 2 | `02-modal-codigo-app-garcom.png` | Passo 2 | com setas (4) | A janela **Ativar aparelho · App Garçom** com o código já gerado, o **Copiar** e a contagem |
| 3 | `03-modal-codigo-qr-app-entregador.png` | Passo 3 | com setas (2) | A mesma janela no **App Entregador**: o terceiro passo cita a câmera e aparece o **QR** ao lado do código |
| 4 | `05-codigo-aguardando-ativacao.png` | Passo 4 | com setas (3) | A lista com **1 código aguardando ativação**, o cartão tracejado com a contagem e o **Cancelar** |
| 5 | `04-modal-sem-vaga-totem.png` | Quando não há vaga livre | com setas (2) | A janela de limite do plano (**0 de 1 livres** no Totem) e o botão **CONTRATAR MAIS** |

## Observações de conteúdo

- **O ponto que o leitor não adivinha é que não existe botão de gerar.** O código sai pronto
  quando a janela abre. Essa frase é o miolo do manual e não deve ser suavizada para "clique em
  gerar".
- **O código é por tipo de aparelho.** O do *App Garçom* não ativa um *App Entregador*. É o erro
  mais provável de quem tem vários aplicativos, e está no aviso do Passo 1 e na tabela de
  problemas.
- **Código aberto ocupa vaga.** É o que explica o leitor que "tem aparelho sobrando" e ainda
  assim recebe o aviso de limite. Manter o aviso do Passo 2, a linha *N código(s) aguardando
  ativação* do Passo 4 e a pergunta correspondente no FAQ.
- **Quinze minutos** é o prazo real do código, lido da própria contagem da tela (ela começa em
  15:00). Não arredondar para "alguns minutos".
- **O QR só existe nos aparelhos com câmera** — App Entregador e cardápio digital em tablet.
  Totem, App Garçom e App Garçom POS mostram apenas o código. Não prometer QR para todos.
- **Dois tipos não usam código:** o *PDV Mobile Offline*, que aparece com o selo **Gestão em
  breve**, e o **TEF**, que tem cadastro próprio na mesma tela. Os dois estão na tabela de
  problemas porque o leitor vai procurar o botão e não achar.
- **Cancelar código e remover aparelho são coisas diferentes.** Cancelar joga fora um código que
  ninguém usou; remover desativa um aparelho em uso, e ele só sai do sistema em até uma hora.
  A página explica os dois, e essa distinção não pode se perder.
- **Quantidade por plano fica fora da página, de propósito.** Quando o leitor bate no limite, o
  manual o manda para **CONTRATAR MAIS** ou para a página de planos e preços — não repete
  tabela de plano, que envelhece.
- As capturas são do sandbox de manuais, com aparelhos de teste. Os códigos que aparecem nas
  imagens (`7MG-VTD`, `KJK-QMT`) já foram cancelados e expiraram: não há dado de cliente nem
  credencial válida em imagem nenhuma.
