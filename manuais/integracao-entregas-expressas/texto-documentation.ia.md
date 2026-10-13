# texto-documentation.ia.md — #127 Entregas Expressas

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Aplicativos** (seção **Entrega**), adicione um manual por
último chamado **"Entregas Expressas"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/integracao-entregas-expressas/integracao-entregas-expressas.md`

2. **Imagens (use estas 11, nesta ordem):**
   - `beefood-web-react-manual/manuais/integracao-entregas-expressas/imagens-tratadas/01-aplicativos-api-aberta.png`
   - `beefood-web-react-manual/manuais/integracao-entregas-expressas/imagens-tratadas/02-painel-api-aberta.png`
   - `beefood-web-react-manual/manuais/integracao-entregas-expressas/imagens-tratadas/03-permissoes-da-credencial.png`
   - `beefood-web-react-manual/manuais/integracao-entregas-expressas/imagens-tratadas/04-nova-credencial.png`
   - `beefood-web-react-manual/manuais/integracao-entregas-expressas/imagens-tratadas/05-ee-cadastrar-integracao.png`
   - `beefood-web-react-manual/manuais/integracao-entregas-expressas/imagens-tratadas/06-ee-colar-credencial.png`
   - `beefood-web-react-manual/manuais/integracao-entregas-expressas/imagens-tratadas/07-ee-quando-vira-entrega.png`
   - `beefood-web-react-manual/manuais/integracao-entregas-expressas/imagens-tratadas/08-aba-webhooks.png`
   - `beefood-web-react-manual/manuais/integracao-entregas-expressas/imagens-tratadas/09-novo-webhook.png`
   - `beefood-web-react-manual/manuais/integracao-entregas-expressas/imagens-tratadas/10-webhook-ativo.png`
   - `beefood-web-react-manual/manuais/integracao-entregas-expressas/imagens-tratadas/11-ee-pedido-no-painel.png`

**NÃO leia outros arquivos** (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `importar.py`,
`capturar-painel.py`, `conferir-setas.py`, `imagens-puras/`).

- Faça a apresentação das imagens **igual** aos outros manuais de **Aplicativos → Entrega**
  (Let's Express, Foody Delivery, Pick N Go!).
- pt-BR, didático; o leitor é o **lojista**. Ele vai e volta entre duas telas de empresas
  diferentes, então deixe sempre claro **em qual das duas** ele está: as imagens 1 a 4 e 8 a 10
  são do **BeeFood**; as 5 a 7 e 11 são do **Entregas Expressas**.
- Não publicar o rodapé de referências internas.
- Palavras que o leitor vai buscar e que devem sobreviver na página: *Entregas Expressas*,
  *integrar BeeFood ao Entregas Expressas*, *API Aberta*, *Client ID*, *Client Secret*,
  *webhook*, *cadastrar webhook*, *credencial da API*, *pedido não chega no Entregas Expressas*,
  *credencial recusada*, *sandbox*, *ambiente de testes*, *despachado*, *entregue*,
  *chamar entregador*, *reciclar credencial*.

## Estrutura da página (na ordem do `.md`)

1. Título e abertura — o que a integração faz, a ordem das três etapas e o aviso de que **o
   webhook é obrigatório**.
2. **O aviso que abre o manual:** tudo se cadastra em **Aplicativos → API Aberta**, não no
   portal de desenvolvedor. É o recado principal da página, e tem de aparecer antes do primeiro
   passo.
3. O que a integração faz — a lista do que entra e do que **não** entra (retirada, balcão, mesa
   e pedido entregue pela logística do marketplace).
4. Antes de começar — inclusive o aviso de que o card **API Aberta** está em liberação por
   etapas e pode não aparecer na conta do leitor.
5. **Parte 1 — No BeeFood: a credencial** (Passos 1 a 4): o caminho no menu, a credencial
   principal que **já existe**, o ícone de olho que revela o Client Secret quantas vezes
   precisar, as permissões *Pedidos* e *Loja*, o aviso do **RECICLAR** e a credencial opcional
   só para o parceiro.
6. **Parte 2 — No Entregas Expressas** (Passos 5 a 7): cadastrar a integração, colar e **testar**
   a credencial, a caixa *Onde pegar a credencial* que deve ser ignorada, os campos de coleta e
   pagamento, e as escolhas de quando o pedido vira entrega.
7. **Parte 3 — De volta ao BeeFood: o webhook** (Passos 8 a 10): a aba **Webhooks**, os cinco
   eventos, a confusão de nomes na autenticação Basic e o **Secret do webhook** que aparece
   uma vez.
8. **Parte 4 — O pedido chegando**: a marca *PEDIDO VIA BEEFOOD* no painel do parceiro.
9. Como funciona no dia a dia — os cinco passos do ciclo, e o que acontece com cancelamento
   antes e depois da coleta.
10. Quando algo não funciona — tabela sintoma/verificação.
11. Perguntas frequentes.
12. Precisa de ajuda? e Onde continuar.

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Onde | Tipo | Legenda |
|---|---|---|---|---|
| 1 | `01-aplicativos-api-aberta.png` | BeeFood | com setas (2) | O menu **Aplicativos** e o card **API Aberta**, na seção **API e MCP** |
| 2 | `02-painel-api-aberta.png` | BeeFood | com setas (4) | O painel da API Aberta na aba **Credencial**: Client ID, o ícone de olho que revela o Client Secret e o selo **Ativa** |
| 3 | `03-permissoes-da-credencial.png` | BeeFood | com setas (5) | As **Permissões** da credencial, com *Pedidos* e *Loja*, o **SALVAR PERMISSÕES**, o **RECICLAR** que não se clica e o **CRIAR CREDENCIAL** |
| 4 | `04-nova-credencial.png` | BeeFood | com setas (3) | O diálogo **Nova credencial adicional**, que já nasce com todos os recursos liberados |
| 5 | `05-ee-cadastrar-integracao.png` | Entregas Expressas | com setas (2) | **Configurações › Integrações › BeeFood** e o botão **CADASTRAR INTEGRAÇÃO** |
| 6 | `06-ee-colar-credencial.png` | Entregas Expressas | com setas (3) | O formulário da loja: **Client ID**, **Client Secret** e **Testar credencial** |
| 7 | `07-ee-quando-vira-entrega.png` | Entregas Expressas | com setas (5) | **Quando o pedido vira entrega**: a opção recomendada, os marketplaces, o retorno, a atualização do status na BeeFood e o tempo de espera |
| 8 | `08-aba-webhooks.png` | BeeFood | com setas (1) | A aba **Webhooks** com a lista vazia e o botão **NOVO WEBHOOK** |
| 9 | `09-novo-webhook.png` | BeeFood | com setas (5) | O formulário **Novo webhook**: URL, os cinco eventos, o e-mail de contato e a autenticação Basic |
| 10 | `10-webhook-ativo.png` | BeeFood | com setas (4) | O **Secret do webhook** exibido uma única vez e a linha do webhook com o selo **Ativo** |
| 11 | `11-ee-pedido-no-painel.png` | Entregas Expressas | com setas (4) | O pedido vindo da BeeFood no painel do parceiro, com a observação **PEDIDO VIA BEEFOOD** |

## Observações de conteúdo

- **O eixo da página é a troca de caminho.** O artigo do parceiro ensina pelo portal de
  desenvolvedor; aqui o caminho é **Aplicativos → API Aberta**. Não é só comodidade: pelo painel
  não existe a escolha de ambiente, e é nela que mora o erro mais comum — criar a credencial em
  *Sandbox* e ficar esperando pedido que nunca chega.
- **Manter o aviso dos nomes que colidem.** No webhook, os campos do BeeFood chamam-se
  *clientId (usuário)* e *clientSecret (senha)*, mas o que vai ali é o **Usuário** e a **Senha**
  do Entregas Expressas, não a credencial da API. Sem esse aviso, o leitor cola os valores
  errados e o webhook passa a ser recusado do outro lado.
- **Manter a diferença entre os dois segredos.** O *Secret do webhook* é da BeeFood, para quem
  recebe conferir que o aviso é legítimo; o Entregas Expressas não pede por ele. São coisas
  diferentes com nomes parecidos, e as duas aparecem na mesma tela.
- **Manter o aviso do RECICLAR.** É o único botão desta página que derruba uma integração em
  funcionamento, sem pedir nada além de uma confirmação.
- **O que é informação do parceiro está marcado como tal** no manual (as 5 falhas seguidas que
  desativam o webhook, a conferência a cada 10 minutos, o pedido que vira despachado e
  entregue). Não transformar em promessa de tela do BeeFood.
- As quatro imagens do Entregas Expressas vêm do artigo público dele, e o telefone e o e-mail
  que apareciam na tela do pedido saem **cobertos já na imagem pura**, porque o repositório é
  público.
