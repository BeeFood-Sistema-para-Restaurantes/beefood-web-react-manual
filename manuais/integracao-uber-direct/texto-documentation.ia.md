# texto-documentation.ia.md — Integração Uber Direct

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.
> O projeto do manual **já está anexo no contexto** — o prompt aponta os **arquivos exatos** a ler.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Aplicativos** (seção **Entrega/Integrações**), adicione um manual
chamado **"Configurar Uber Direct no BeeFood"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra, sem reescrever):**
   `beefood-web-react-manual/manuais/integracao-uber-direct/integracao-uber-direct.md`

2. **Imagens (use estas 20, na ordem de aparição no manual):**
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
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-20.png`
   - `beefood-web-react-manual/manuais/integracao-uber-direct/imagens-tratadas/uber-direct-00.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `integracao-uber-direct.md` **exatamente como está** (seções, textos e tabelas) — o
  texto já está pronto, **não reescrever nem interpretar**.
- Insira as 20 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Idioma **português do Brasil**, tom didático (usuário final / restaurante).
- Mantenha em destaque: **cada loja tem a própria conta e o próprio cartão** na Uber; o cadastro é no site
  **direct.uber.com/accounts**; o webhook a cadastrar é `https://entregas.beefoodapi.be/api/uberDirect/webhook`
  (evento **event.delivery_status**); as 3 credenciais (**Customer ID / Client ID / Client Secret**) vêm de
  **Desenvolvedor → Chaves de API** e são coladas em **Aplicativos → Entregas → Uber Direct**.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Legenda |
|------:|----------------------------------|---------|
| 1 | `uber-direct-01.png` | Uber → informar **telefone ou e-mail** e Continuar |
| 2 | `uber-direct-02.png` | Uber → **código de verificação** (4 dígitos) |
| 3 | `uber-direct-03.png` | Uber → **senha** da conta |
| 4 | `uber-direct-04.png` | Uber Direct → **nome do restaurante** |
| 5 | `uber-direct-05.png` | Uber Direct → **tipo de empresa** |
| 6 | `uber-direct-06.png` | Uber Direct → **endereço** da empresa |
| 7 | `uber-direct-07.png` | Uber Direct → **CNPJ** do restaurante |
| 8 | `uber-direct-08.png` | Uber Direct → aceitar **Termos** e Enviar |
| 9 | `uber-direct-09.png` | Painel → **Gerenciamento → Pagamento** |
| 10 | `uber-direct-10.png` | **Configurar o pagamento** |
| 11 | `uber-direct-11.png` | **Dados do cartão** |
| 12 | `uber-direct-12.png` | **Adicionar cartão** |
| 13 | `uber-direct-13.png` | Painel → **Desenvolvedor** |
| 14 | `uber-direct-14.png` | Aba **Webhooks** |
| 15 | `uber-direct-15.png` | **+ Criar webhook** |
| 16 | `uber-direct-16.png` | **URL do webhook** + evento **event.delivery_status** |
| 17 | `uber-direct-17.png` | **Salvar** webhook |
| 18 | `uber-direct-18.png` | Aba **Chaves de API** |
| 19 | `uber-direct-20.png` | Copiar **ID do usuário / ID de cliente / Client Secret** |
| 20 | `uber-direct-00.png` | BeeFood → menu **Aplicativos** (colar credenciais em Entregas → Uber Direct) |
