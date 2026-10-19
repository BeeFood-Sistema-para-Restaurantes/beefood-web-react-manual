# texto-documentation.ia.md — #129 Route Delivery

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Aplicativos** (seção **Entrega**), adicione um manual por
último chamado **"Route Delivery"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/integracao-route-delivery/integracao-route-delivery.md`

2. **Imagens (use estas 14, nesta ordem):**
   - `beefood-web-react-manual/manuais/integracao-route-delivery/imagens-tratadas/01-aplicativos-api-aberta.png`
   - `beefood-web-react-manual/manuais/integracao-route-delivery/imagens-tratadas/02-painel-credencial.png`
   - `beefood-web-react-manual/manuais/integracao-route-delivery/imagens-tratadas/03-criar-credencial.png`
   - `beefood-web-react-manual/manuais/integracao-route-delivery/imagens-tratadas/04-nova-credencial.png`
   - `beefood-web-react-manual/manuais/integracao-route-delivery/imagens-tratadas/05-credencial-criada.png`
   - `beefood-web-react-manual/manuais/integracao-route-delivery/imagens-tratadas/06-rd-cartao-beefood.png`
   - `beefood-web-react-manual/manuais/integracao-route-delivery/imagens-tratadas/07-rd-vincular-loja.png`
   - `beefood-web-react-manual/manuais/integracao-route-delivery/imagens-tratadas/08-rd-integracao-ativa.png`
   - `beefood-web-react-manual/manuais/integracao-route-delivery/imagens-tratadas/09-rd-liberar-na-chegada.png`
   - `beefood-web-react-manual/manuais/integracao-route-delivery/imagens-tratadas/10-rd-canais-marketplace.png`
   - `beefood-web-react-manual/manuais/integracao-route-delivery/imagens-tratadas/11-rd-endereco-webhook.png`
   - `beefood-web-react-manual/manuais/integracao-route-delivery/imagens-tratadas/12-aba-webhooks.png`
   - `beefood-web-react-manual/manuais/integracao-route-delivery/imagens-tratadas/13-novo-webhook.png`
   - `beefood-web-react-manual/manuais/integracao-route-delivery/imagens-tratadas/14-webhook-ativo.png`

**NÃO leia outros arquivos** (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `importar.py`,
`capturar-painel.py`, `conferir-setas.py`, `imagens-puras/`).

- Faça a apresentação das imagens **igual** aos outros manuais de **Aplicativos → Entrega**
  (Entregas Expressas, Let's Express, Foody Delivery, Pick N Go!).
- pt-BR, didático; o leitor é o **lojista**. Ele passa por telas de **duas empresas diferentes**,
  e numa delas ele nem é quem clica — então deixe sempre claro **onde ele está** e **quem faz**:
  as imagens 1 a 5, 12, 13 e 14 são do **BeeFood** e são ele quem executa; as imagens 6 a 11 são
  do **Route Delivery** e mostram o que a **equipe do parceiro** faz.
- Não publicar o rodapé de referências internas.
- Palavras que o leitor vai buscar e que devem sobreviver na página: *Route Delivery*,
  *integrar BeeFood ao Route Delivery*, *API Aberta*, *criar credencial*, *credencial da API*,
  *Client ID*, *Client Secret*, *webhook*, *cadastrar webhook*, *secret do webhook*,
  *vincular loja*, *pedido não chega no Route Delivery*, *credencial recusada*, *sandbox*,
  *ambiente de testes*, *despachado*, *entregue*, *chamar entregador*, *reciclar credencial*.

## Estrutura da página (na ordem do `.md`)

1. Título e abertura — o que a integração faz, e **quem faz cada parte**: a loja cria a
   credencial, a equipe Route Delivery vincula a loja, a loja volta para cadastrar o webhook.
2. **O aviso que abre o manual:** a credencial e o webhook se cadastram em **Aplicativos → API
   Aberta**, não no portal de desenvolvedor. É o recado principal da página, e tem de aparecer
   antes do primeiro passo.
3. O que a integração faz — a lista do que entra, do que **não** entra (retirada, balcão, mesa) e
   o padrão de chamar o entregador quando a loja marca **Pronto**.
4. Antes de começar — inclusive o aviso de que o card **API Aberta** está em liberação por
   etapas, e o cuidado com o envio do Client Secret.
5. **Parte 1 — No BeeFood: a credencial do Route Delivery** (Passos 1 a 5): o caminho no menu, a
   credencial principal que fica quieta, as permissões *Pedidos* e *Loja*, o aviso do
   **RECICLAR**, o **CRIAR CREDENCIAL**, o diálogo que já nasce com tudo ligado e a tela
   **Credencial criada** com os dois valores.
6. **Parte 2 — No Route Delivery: a equipe vincula a sua loja** (Passos 6 a 9): o cartão BeeFood,
   o **Vincular loja** com a caixa *Credencial do sandbox* desmarcada, o **Ativar integração** e
   as duas escolhas a combinar (quando o entregador é chamado e os canais de marketplace).
7. **Parte 3 — De volta ao BeeFood: o webhook** (Passos 10 a 12): o endereço que vem do parceiro,
   os **três** eventos, a autenticação Basic **em branco** e o **Secret do webhook** que volta
   para a equipe.
8. **Parte 4 — Acompanhando os pedidos**: a tela **Operação** do parceiro e a lista *Últimos
   eventos* (sem imagem — é texto).
9. Como funciona no dia a dia — os cinco passos do ciclo, o cancelamento e as 2 horas da
   primeira busca.
10. Quando algo não funciona — tabela sintoma/verificação.
11. Perguntas frequentes.
12. Precisa de ajuda? e Onde continuar.

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Onde | Tipo | Legenda |
|---|---|---|---|---|
| 1 | `01-aplicativos-api-aberta.png` | BeeFood | com setas (2) | O menu **Aplicativos** e o card **API Aberta**, na seção **API e MCP** |
| 2 | `02-painel-credencial.png` | BeeFood | com setas (2) | A aba **Credencial** e a **Credencial principal**, que é a mesma exibida no portal `docs.beefood.app` |
| 3 | `03-criar-credencial.png` | BeeFood | com setas (4) | As **Permissões** com *Pedidos* e *Loja*, o **RECICLAR** que não se clica e o **CRIAR CREDENCIAL** |
| 4 | `04-nova-credencial.png` | BeeFood | com setas (3) | O diálogo **Nova credencial adicional**, que já nasce com todos os recursos liberados |
| 5 | `05-credencial-criada.png` | BeeFood | com setas (3) | A tela **Credencial criada**, com o **clientId** e o **clientSecret** para enviar ao parceiro |
| 6 | `06-rd-cartao-beefood.png` | Route Delivery | com setas (2) | O cartão **BeeFood** em **Integrações**, com o selo **Ativa** e o resumo de lojas, eventos e erros |
| 7 | `07-rd-vincular-loja.png` | Route Delivery | com setas (5) | O **Vincular loja**: comércio, Client ID, Client Secret, a caixa *Credencial do sandbox* e o **Testar credencial e vincular** |
| 8 | `08-rd-integracao-ativa.png` | Route Delivery | com setas (2) | O topo da tela com o selo **Ativa** e o botão **Pausar integração** |
| 9 | `09-rd-liberar-na-chegada.png` | Route Delivery | com setas (1) | A opção **Liberar o pedido para os entregadores assim que chegar** |
| 10 | `10-rd-canais-marketplace.png` | Route Delivery | com setas (2) | **Trazer também os pedidos destes canais** (iFood, 99Food, Keeta, aiqfome) e o **Buscar pedidos agora** |
| 11 | `11-rd-endereco-webhook.png` | Route Delivery | com setas (4) | A linha da loja: o **endereço do webhook** com o botão **Copiar**, e o campo onde o **secret** é colado depois |
| 12 | `12-aba-webhooks.png` | BeeFood | com setas (1) | A aba **Webhooks** e o botão **NOVO WEBHOOK** |
| 13 | `13-novo-webhook.png` | BeeFood | com setas (5) | O formulário **Novo webhook**: URL, os **três** eventos, o e-mail de contato e a autenticação Basic **em branco** |
| 14 | `14-webhook-ativo.png` | BeeFood | com setas (4) | O **Secret do webhook** exibido uma única vez e a linha do webhook com o selo **Ativo** |

## Observações de conteúdo

- **O eixo da página é a troca de caminho.** O artigo do parceiro ensina a criar a credencial no
  portal de desenvolvedor, marcando permissão e trocando o ambiente de *Sandbox* para
  *Produção*. Aqui o caminho é **Aplicativos → API Aberta → CRIAR CREDENCIAL**: três cliques,
  permissões já ligadas e **nenhuma escolha de ambiente** — é nela que mora o erro mais comum,
  criar em Sandbox e ficar esperando pedido que nunca chega.
- **A credencial é dedicada ao parceiro, de propósito.** Não é capricho: ela pode ser desligada
  ou excluída depois sem derrubar nenhuma outra integração, e a credencial principal — que é a
  que o portal mostra — fica intacta. Manter essa justificativa no Passo 2.
- **Manter o aviso do RECICLAR.** Ele fica logo acima do **CRIAR CREDENCIAL** na mesma tela, e é
  o único botão da página que derruba uma integração em funcionamento.
- **A autenticação Basic fica em branco** — ao contrário do manual do Entregas Expressas, onde
  os campos recebem usuário e senha do parceiro. Não copiar o aviso do outro manual: aqui o
  risco é preencher **um** dos dois campos, porque o BeeFood exige os dois juntos ou nenhum.
- **O *Secret do webhook* é a última etapa, não um detalhe.** O Route Delivery precisa dele: a
  equipe cola o valor na linha da loja, no painel dela. Sem isso a linha fica em *Falta o secret
  do webhook* e a integração só funciona pela busca a cada 5 segundos.
- **O texto dentro da imagem 10 contradiz o manual de propósito**, e isso está tratado: ele é do
  parceiro e manda criar o webhook no portal BeeFood Developers. A nota logo abaixo da imagem
  explica que o endereço e os eventos valem, e só o caminho muda.
- **A etiqueta `sandbox` visível na imagem 11 é do exemplo do parceiro**, e o manual avisa que,
  seguindo este caminho, ela não deve aparecer. Não remover esse aviso: sem ele o leitor acha
  que errou.
- **O que é informação do parceiro está marcado como tal** no manual (as 5 tentativas que
  desativam o webhook, a busca a cada 5 s ou 30 s, as 2 horas da primeira busca, o pedido que
  vira despachado e entregue). Não transformar em promessa de tela do BeeFood.
- As seis imagens do Route Delivery vêm do **artigo público** dele, e só mostram valores de
  exemplo — não há dado de cliente nelas.
