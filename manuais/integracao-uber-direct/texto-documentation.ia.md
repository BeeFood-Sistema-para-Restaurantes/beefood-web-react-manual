# Prompt para gerar a página de documentação — Integração Uber Direct

Você é um assistente que vai **montar a página de ajuda** da integração **Uber Direct** do BeeFood
(a ser publicada em `https://ajuda3.beefood.com.br/integracao-uber-direct`).

## Leia SOMENTE estes arquivos

1. **Texto do manual (use verbatim):**
   - `beefood-web-react-manual/manuais/integracao-uber-direct/integracao-uber-direct.md`

2. **Imagens (use estas 27, na ordem de aparição no manual):**
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-01.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-02.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-03.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-04.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-05.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-06.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-07.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-08.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-09.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-10.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-11.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-12.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-13.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-14.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-15.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-16.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-17.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-18.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-19.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-20.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-21.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-22.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-23.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-24.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-25.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-26.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-27.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `imagens-puras/`).

## Como montar a página

- Use o conteúdo do `integracao-uber-direct.md` **exatamente como está** (seções, textos e tabelas) — o
  texto já está pronto, **não reescrever nem interpretar**.
- Insira as 27 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- Idioma: **português do Brasil**.
- Público: **dono/operador do restaurante** (linguagem simples e direta).

## Pontos-chave a destacar

- O cadastro da conta é feito **no site da Uber** (`direct.uber.com/accounts`); só o passo final é no BeeFood.
- Cada loja precisa de **conta Uber + Uber Direct + cartão próprios**.
- A **URL do webhook** deve ser exatamente `https://entregas.beefoodapi.be/api/uberDirect/webhook`, com o evento **event.delivery_status**.
- É obrigatório copiar 4 valores: **Chave de autenticação do webhook**, **ID do usuário**, **ID de cliente do desenvolvedor** e **Client Secret** — todos colados em **Aplicativos → Entregas → Uber Direct** no BeeFood.
- O pagamento das corridas é cobrado **pela Uber no cartão cadastrado**; o BeeFood não cobra as entregas.

## Legendas das imagens

| # | Arquivo | Legenda sugerida |
|---|---------|------------------|
| 1 | `uber-direct-01.png` | Informar telefone/e-mail na conta Uber |
| 2 | `uber-direct-02.png` | Código de verificação da conta Uber |
| 3 | `uber-direct-03.png` | Inserir a senha da conta Uber |
| 4 | `uber-direct-04.png` | Nome do restaurante no cadastro Uber Direct |
| 5 | `uber-direct-05.png` | Selecionar o tipo de empresa |
| 6 | `uber-direct-06.png` | Endereço da empresa |
| 7 | `uber-direct-07.png` | CNPJ do restaurante |
| 8 | `uber-direct-08.png` | Aceitar os termos e enviar |
| 9 | `uber-direct-09.png` | Menu Gerenciamento → Pagamento |
| 10 | `uber-direct-10.png` | Botão Configurar o pagamento |
| 11 | `uber-direct-11.png` | Preencher dados do cartão |
| 12 | `uber-direct-12.png` | Adicionar cartão |
| 13 | `uber-direct-13.png` | Menu Desenvolvedor |
| 14 | `uber-direct-14.png` | Aba Webhooks → + Criar webhook |
| 15 | `uber-direct-15.png` | URL do webhook + evento event.delivery_status |
| 16 | `uber-direct-16.png` | 3 pontinhos → Editar (webhook) |
| 17 | `uber-direct-17.png` | Copiar a Chave de autenticação |
| 18 | `uber-direct-18.png` | Aba Chaves de API (ID do usuário / Client ID / Client Secret) |
| 19 | `uber-direct-19.png` | BeeFood → menu Aplicativos |
| 20 | `uber-direct-20.png` | Seção Entregas → Uber Direct |
| 21 | `uber-direct-21.png` | Preencher os campos e Salvar no BeeFood |
| 22 | `uber-direct-22.png` | Delivery → localizar o pedido |
| 23 | `uber-direct-23.png` | Pedido → Adicionar Entregador |
| 24 | `uber-direct-24.png` | Selecionar Uber Direct |
| 25 | `uber-direct-25.png` | Cotação (distância/tempo/frete) → Confirmar |
| 26 | `uber-direct-26.png` | Pedido vinculado ao Uber Direct |
| 27 | `uber-direct-27.png` | Cancelar entrega no campo Entregador |
