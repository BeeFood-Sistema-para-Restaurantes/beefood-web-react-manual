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

2. **Imagens (use estas 16, nesta ordem):**
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/01-aplicativos-api-aberta.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/02-painel-credencial.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/03-criar-credencial.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/04-nova-credencial-tudo.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/05-nova-credencial-seis.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/06-credencial-criada.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/07-nb-configuracoes-integracoes.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/08-nb-card-beefood.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/09-nb-form-credencial.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/10-nb-cardapio-pagamentos.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/11-nb-verificacao.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/12-nb-integracao-configurada.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/13-nb-produtos-sinc.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/14-nb-importacao-opcoes.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/15-nb-importacao-concluida.png`
   - `beefood-web-react-manual/manuais/integracao-natural-bot/imagens-tratadas/16-nb-produtos-importados.png`

**NÃO leia outros arquivos** (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`,
`capturar-beefood.py`, `capturar-naturalbot.py`, `limpar-credencial.py`, `naturalbot.py`,
`conferir-setas.py`, `imagens-puras/`).

- Faça a apresentação das imagens **igual** aos outros manuais de **Aplicativos → API e MCP**
  (Entregas Expressas, Route Delivery).
- pt-BR, didático; o leitor é o **lojista**. Ele passa por telas de **duas empresas diferentes**
  e é ele quem clica nas duas — então deixe sempre claro **onde ele está**: as imagens 1 a 6 são
  do **BeeFood** e as imagens 7 a 16 são do **painel da Natural Bot**.
- **Este manual é só da ativação.** Repita, como o `.md` faz, que dúvida de uso da Natural Bot se
  tira com a Natural Bot. Não inventar passo de operação do robô.
- Não publicar o rodapé de referências internas.
- Palavras que o leitor vai buscar e que devem sobreviver na página: *Natural Bot*,
  *integrar BeeFood com Natural Bot*, *API Aberta*, *criar credencial*, *Client ID*,
  *Client Secret*, *seis acessos*, *webhook de status*, *gestor de PDV*, *Sinc. BeeFood*,
  *importar cardápio*, *sincronizar cardápio*, *de-para de pagamentos*, *credencial recusada*,
  *sandbox*, *ambiente de testes*, *status não volta*, *reciclar credencial*.

## Estrutura da página (na ordem do `.md`)

1. Título e abertura — o que a ativação faz e o aviso de que **o manual é só da ativação**: uso
   da Natural Bot é com a Natural Bot.
2. O que a integração faz — pedido entrando na loja, status voltando sozinho, cardápio importado
   e formas de pagamento casadas uma a uma.
3. Antes de começar — inclusive o aviso de que o card **API Aberta** está em liberação por
   etapas, e o cuidado com o envio do Client Secret.
4. **O aviso que fecha a seção:** a credencial se cria em **Aplicativos → API Aberta**, não no
   portal de desenvolvedor que a tela da Natural Bot cita. Pelo painel não há escolha de
   ambiente, e o que ele cria é sempre de produção.
5. **Parte 1 — No BeeFood: a credencial da Natural Bot** (Passos 1 a 6): o caminho no menu, a
   credencial principal que fica quieta, o **RECICLAR** que não se clica, o **CRIAR CREDENCIAL**,
   o diálogo que nasce com tudo ligado, o desligar até sobrarem os **seis** acessos e a tela
   **Credencial criada**.
6. **Parte 2 — No painel da Natural Bot: ligar a BeeFood** (Passos 7 a 12): Configurações →
   Integrações, o aviso de um gestor de PDV por vez, o card BeeFood, o formulário da credencial,
   cardápio e de-para de pagamentos, o resultado da verificação e a tela de integração já
   configurada com **Webhook de status: ativo**.
7. **Parte 3 — Sincronizar o cardápio** (Passos 13 a 16): **Cardápio → Produtos → Sinc.
   BeeFood**, as três opções da importação, o resumo do que entrou e a conferência na aba
   **Todos**.
8. Como fica o dia a dia — o status voltando, a importação manual, como trocar credencial ou
   cardápio e como parar de enviar pedidos.
9. Quando algo não funciona — tabela sintoma/verificação.
10. Perguntas frequentes.
11. Precisa de ajuda? e Onde continuar.

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Onde | Tipo | Legenda |
|---|---|---|---|---|
| 1 | `01-aplicativos-api-aberta.png` | BeeFood | com setas (2) | O menu **Aplicativos** e o card **API Aberta**, na seção **API e MCP** |
| 2 | `02-painel-credencial.png` | BeeFood | com setas (2) | A aba **Credencial** e a **Credencial principal**, que é a mesma exibida no portal `docs.beefood.app` |
| 3 | `03-criar-credencial.png` | BeeFood | com setas (2) | O **RECICLAR** que não se clica e o **CRIAR CREDENCIAL**, no fim do cartão |
| 4 | `04-nova-credencial-tudo.png` | BeeFood | com setas (3) | O diálogo **Nova credencial adicional** como ele abre: todos os recursos ligados, com o nome do acesso embaixo de cada interruptor |
| 5 | `05-nova-credencial-seis.png` | BeeFood | com setas (5) | O mesmo diálogo com só os **seis** acessos da Natural Bot: Pedidos, Catálogo, Loja e Webhooks |
| 6 | `06-credencial-criada.png` | BeeFood | com setas (3) | A tela **Credencial criada**, com o **clientId** e o **clientSecret** |
| 7 | `07-nb-configuracoes-integracoes.png` | Natural Bot | com setas (3) | **Configurações → Integrações** e o aviso de que só um **gestor de PDV** fica ativo por vez |
| 8 | `08-nb-card-beefood.png` | Natural Bot | com setas (2) | O card **BeeFood** entre os gestores de PDV, com a chave e o botão **CONFIGURAR** / **EDITAR** |
| 9 | `09-nb-form-credencial.png` | Natural Bot | com setas (5) | O formulário da credencial, com a lista dos seis acessos, o aviso de webhook, **Client ID**, **Client secret** e **Conectar** |
| 10 | `10-nb-cardapio-pagamentos.png` | Natural Bot | com setas (4) | A escolha do **Cardápio**, o de-para das **formas de pagamento**, o **Ligar a integração ao salvar** e o **Salvar** |
| 11 | `11-nb-verificacao.png` | Natural Bot | com setas (3) | O resultado da verificação feita na BeeFood, com a linha de sucesso, um aviso amarelo e o **Concluir** |
| 12 | `12-nb-integracao-configurada.png` | Natural Bot | com setas (5) | **Integração já configurada**: resumo, **Editar Integração**, a chave **Integração ligada**, o **Webhook de status: ativo** e o **Ir para Produtos** |
| 13 | `13-nb-produtos-sinc.png` | Natural Bot | com setas (2) | **Cardápio → Produtos** e o botão **Sinc. BeeFood** |
| 14 | `14-nb-importacao-opcoes.png` | Natural Bot | com setas (3) | O diálogo **Importação de produtos — BeeFood**, com as três opções desmarcadas e o **Importar** |
| 15 | `15-nb-importacao-concluida.png` | Natural Bot | com setas (3) | **Importação concluída**, com a conta de categorias, produtos, variações e opções |
| 16 | `16-nb-produtos-importados.png` | Natural Bot | com setas (2) | A aba **Todos** da lista de Produtos, com os itens que vieram da BeeFood |

## Observações de conteúdo

- **O eixo da página são os seis acessos, e não há atalho.** Diferente do Route Delivery, aqui a
  credencial **não** serve como vem: ela nasce com tudo ligado e o leitor precisa desligar o que
  não é dos seis. Manter as duas imagens do mesmo diálogo (4 e 5) — é a diferença entre "confira"
  e "mexa".
- **`webhook:read` e `webhook:write` são o coração do manual.** São eles que deixam a Natural Bot
  cadastrar sozinha o aviso que traz o status de volta, e por isso **não existe Parte 3 de
  webhook** aqui, ao contrário dos manuais de Entregas Expressas e Route Delivery. Dizer isso em
  voz alta: quem já integrou um dos outros dois espera essa etapa.
- **Manter o aviso do RECICLAR.** Ele fica a um clique do **CRIAR CREDENCIAL**, na mesma tela, e é
  o único botão da página que derruba integração em funcionamento.
- **Manter o aviso do gestor de PDV.** Ativar a BeeFood desativa automaticamente o gestor
  anterior na Natural Bot; é a frase da tela dela, e é irreversível sem reconfigurar o outro.
- **O aviso amarelo da imagem 11 fica.** Ele é real (*o canal delivery deste cardápio não aceita
  pedidos de entrega nem de retirada*) e ensina a ler a verificação: a linha verde é o que diz se
  a credencial foi aceita; o amarelo é configuração do cardápio no BeeFood.
- **As três opções da importação são destrutivas em graus diferentes.** A tabela depois da imagem
  14 é obrigatória, e a instrução da primeira rodada é deixar as três desmarcadas.
- **A aba Todos não é detalhe.** A lista de Produtos abre na primeira categoria, que pode estar
  vazia, e já houve quem concluísse que a importação falhou por isso.
- **Nada de uso do robô.** Qualquer pergunta sobre atendimento, impressão, campanha ou cupom vai
  para o suporte Natural Bot — está escrito duas vezes no `.md`, de propósito.
- As imagens do painel da Natural Bot são da loja de testes (**Filial do parça**), e não há dado
  de cliente em nenhuma delas.
