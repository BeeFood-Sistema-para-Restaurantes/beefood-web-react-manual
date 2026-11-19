# texto-documentation.ia.md — #134 Natural Bot

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Aplicativos** (seção **API e MCP**), adicione um manual por
último chamado **"Natural Bot"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/integracao-natural-bot/integracao-natural-bot.md`

2. **Imagens (use estas 12, nesta ordem):**
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/01-aplicativos-api-aberta.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/02-criar-credencial.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/03-nova-credencial-seis.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/04-credencial-criada.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/05-nb-integracoes-beefood.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/06-nb-form-credencial.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/07-nb-cardapio-pagamentos.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/08-nb-verificacao.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/09-nb-integracao-configurada.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/10-nb-produtos-sinc.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/11-nb-importacao-opcoes.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/12-nb-importacao-concluida.png`

**NÃO leia outros arquivos** (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`,
`capturar-beefood.py`, `capturar-naturalbot.py`, `limpar-credencial.py`, `naturalbot.py`,
`conferir-setas.py`, `imagens-puras/`).

- Faça a apresentação das imagens **igual** aos outros manuais de **Aplicativos → API e MCP**
  (Entregas Expressas, Route Delivery).
- pt-BR, **direto ao ponto**; o leitor é o **lojista**. Ele passa por telas de **duas empresas
  diferentes** e é ele quem clica nas duas — deixe sempre claro **onde ele está**: as imagens 1 a
  4 são do **BeeFood** e as imagens 5 a 12 são do **painel da Natural Bot**.
- **Este manual é só da ativação.** Repita, como o `.md` faz, que dúvida de uso da Natural Bot se
  tira com a Natural Bot. Não inventar passo de operação do robô.
- **Não alongar.** O manual foi encurtado de propósito, e nada do que foi cortado deve voltar:
  não há foto do diálogo de permissões "como ele abre", não há foto da credencial principal e não
  há foto da lista de produtos já importada.
- Não publicar o rodapé de referências internas.
- Palavras que o leitor vai buscar e que devem sobreviver na página: *Natural Bot*,
  *integrar BeeFood com Natural Bot*, *API Aberta*, *criar credencial*, *Client ID*,
  *Client Secret*, *seis acessos*, *webhook de status*, *gestor de PDV*, *Sinc. BeeFood*,
  *importar cardápio*, *sincronizar cardápio*, *de-para de pagamentos*, *credencial recusada*,
  *sandbox*, *ambiente de testes*, *status não volta*, *reciclar credencial*.

## Estrutura da página (na ordem do `.md`)

1. Título e abertura — o que a ativação faz e o aviso de que **o manual é só da ativação**.
2. O que a integração faz — quatro linhas: pedido entrando, status voltando, cardápio importado,
   pagamentos casados.
3. Antes de começar — quatro pré-requisitos, mais a caixa que diz que **a credencial se cria em
   Aplicativos → API Aberta**, e não no portal de desenvolvedor que a tela da Natural Bot cita.
4. **Parte 1 — No BeeFood: a credencial da Natural Bot** (Passos 1 a 4): o caminho no menu, o
   `CRIAR CREDENCIAL` (com o `RECICLAR` que não se clica), o desligar até sobrarem os **seis**
   acessos e a tela **Credencial criada**.
5. **Parte 2 — No painel da Natural Bot: ligar a BeeFood** (Passos 5 a 9): a aba *Integrações* e
   o card BeeFood na mesma foto, o formulário da credencial, cardápio e de-para de pagamentos, a
   verificação e a tela de integração já configurada com **Webhook de status: ativo**.
6. **Parte 3 — Sincronizar o cardápio** (Passos 10 a 12): **Cardápio → Produtos → Sinc.
   BeeFood**, as três opções da importação e o resumo do que entrou.
7. Como fica o dia a dia.
8. Quando algo não funciona — tabela sintoma/verificação.
9. Perguntas frequentes.
10. Precisa de ajuda? e Onde continuar.

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Onde | Tipo | Legenda |
|---|---|---|---|---|
| 1 | `01-aplicativos-api-aberta.png` | BeeFood | com setas (2) | O menu **Aplicativos** e o card **API Aberta**, na seção **API e MCP** |
| 2 | `02-criar-credencial.png` | BeeFood | com setas (3) | A aba **Credencial** e, no fim do cartão, o **RECICLAR** que não se clica e o **CRIAR CREDENCIAL** |
| 3 | `03-nova-credencial-seis.png` | BeeFood | com setas (5) | O diálogo **Nova credencial adicional** como ele tem de ficar: só Pedidos, Catálogo, Loja e Webhooks |
| 4 | `04-credencial-criada.png` | BeeFood | com setas (3) | A tela **Credencial criada**, com o **clientId** e o **clientSecret** |
| 5 | `05-nb-integracoes-beefood.png` | Natural Bot | com setas (4) | **Configurações → Integrações**, o aviso de um **gestor de PDV** por vez e o card **BeeFood** com a chave e o botão **EDITAR** |
| 6 | `06-nb-form-credencial.png` | Natural Bot | com setas (5) | O formulário da credencial: a lista dos seis acessos, o aviso de webhook, **Client ID**, **Client secret** e **Conectar** |
| 7 | `07-nb-cardapio-pagamentos.png` | Natural Bot | com setas (4) | A escolha do **Cardápio**, o de-para das **formas de pagamento**, o **Ligar a integração ao salvar** e o **Salvar** |
| 8 | `08-nb-verificacao.png` | Natural Bot | com setas (3) | O resultado da verificação feita na BeeFood: a linha de sucesso, um aviso amarelo e o **Concluir** |
| 9 | `09-nb-integracao-configurada.png` | Natural Bot | com setas (5) | **Integração já configurada**: resumo, **Editar Integração**, a chave **Integração ligada**, o **Webhook de status: ativo** e o **Ir para Produtos** |
| 10 | `10-nb-produtos-sinc.png` | Natural Bot | com setas (2) | **Cardápio → Produtos** e o botão **Sinc. BeeFood** |
| 11 | `11-nb-importacao-opcoes.png` | Natural Bot | com setas (3) | O diálogo **Importação de produtos — BeeFood**, com as três opções desmarcadas e o **Importar** |
| 12 | `12-nb-importacao-concluida.png` | Natural Bot | com setas (3) | **Importação concluída**, com a conta de categorias, produtos, variações e opções |

## Observações de conteúdo

- **Duas imagens são costuradas, e a emenda tracejada tem de aparecer na publicação.** A 02 pula
  da linha de abas do painel para o `CRIAR CREDENCIAL`, que fica muito abaixo; a 05 pula do
  cabeçalho da aba *Integrações* para o card da BeeFood, que no painel do parceiro vem atrás de
  onze concorrentes. O tracejado diz que ali existe tela que não está na foto — não cortar nem
  retocar.
- **O eixo da página são os seis acessos.** Diferente do Route Delivery, aqui a credencial **não**
  serve como vem: ela nasce com tudo ligado e o leitor precisa desligar o que não é dos seis. A
  imagem 3 mostra o **estado final**, e o texto diz o que desligar — não pedir uma foto do estado
  inicial.
- **`webhook:read` e `webhook:write` são o coração do manual.** São eles que deixam a Natural Bot
  cadastrar sozinha o aviso que traz o status de volta, e por isso **não existe Parte 3 de
  webhook** aqui, ao contrário dos manuais de Entregas Expressas e Route Delivery. Dizer isso em
  voz alta: quem já integrou um dos outros dois espera essa etapa.
- **Manter o aviso do RECICLAR.** Ele fica a um clique do **CRIAR CREDENCIAL**, na mesma tela, e é
  o único botão da página que derruba integração em funcionamento.
- **Manter o aviso do gestor de PDV.** Ativar a BeeFood desativa automaticamente o gestor
  anterior na Natural Bot; é a frase da tela dela.
- **O aviso amarelo da imagem 8 fica.** Ele é real (*o canal delivery deste cardápio não aceita
  pedidos de entrega nem de retirada*) e ensina a ler a verificação: a linha verde diz se a
  credencial foi aceita; o amarelo é configuração do cardápio no BeeFood.
- **As três opções da importação são destrutivas em graus diferentes.** A tabela depois da imagem
  11 é obrigatória, e a instrução da primeira rodada é deixar as três desmarcadas.
- **A aba Todos é texto, não imagem.** A lista de Produtos abre na primeira categoria, que pode
  estar vazia, e já houve quem concluísse que a importação falhou por isso — o aviso está no fim
  do Passo 12.
- **Nada de uso do robô.** Qualquer pergunta sobre atendimento, impressão, campanha ou cupom vai
  para o suporte Natural Bot — está no `.md` duas vezes, de propósito.
- As imagens do painel da Natural Bot são da loja de testes (**Filial do parça**), e não há dado
  de cliente em nenhuma delas.
