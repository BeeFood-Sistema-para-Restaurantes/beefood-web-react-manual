# texto-documentation.ia.md — Integração 99 Entrega

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.
> O projeto do manual **já está anexo no contexto** — o prompt aponta os **arquivos exatos** a ler.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Aplicativos** (seção **Entrega/Integrações**), adicione um manual
chamado **"Integração 99 Entrega"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra, sem reescrever):**
   `beefood-web-react-manual/manuais/integracao-99-entrega/integracao-99-entrega.md`

2. **Imagens (use estas 20, nesta ordem):**
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-05.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-06.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-07.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-08.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-09.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-10.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-11.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-12.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-13.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-14.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-15.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-16.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-17.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-18.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-19.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-20.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-21.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-22.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-23.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-24.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `integracao-99-entrega.md` **exatamente como está** (seções, textos e tabelas) — o
  texto já está pronto, **não reescrever nem interpretar**.
- Insira as 20 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Idioma **português do Brasil**, tom didático (usuário final / restaurante).
- Mantenha em destaque: o pagamento da integração é **somente boleto** (análise da 99); é preciso pedir o
  **ambiente de produção** no Modo de desenvolvedor (também com análise); as 3 credenciais (**ID do cliente
  / Segredo do cliente / Chave de assinatura**) vêm do **Modo de desenvolvedor** da 99; webhook a cadastrar:
  `https://entregas.beetechapi.be/api/99Entrega/webhook`; cancelamento só **antes** de o entregador retirar o pedido.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Legenda |
|------:|----------------------------------|---------|
| 1 | `99-entrega-05.png` | Configurações de pagamento — solicitar **boleto** |
| 2 | `99-entrega-06.png` | Selecionar **Boleto** |
| 3 | `99-entrega-07.png` | **Confirmar** solicitação de boleto |
| 4 | `99-entrega-08.png` | Boleto **pendente de análise** |
| 5 | `99-entrega-09.png` | Painel após aprovação → **Modo de desenvolvedor** |
| 6 | `99-entrega-10.png` | **Ambiente de produção** |
| 7 | `99-entrega-11.png` | **Enviar** solicitação de produção |
| 8 | `99-entrega-12.png` | **Confirmar** envio |
| 9 | `99-entrega-13.png` | Ambiente de produção **pendente de análise** |
| 10 | `99-entrega-14.png` | **Modo de desenvolvedor** no painel 99 |
| 11 | `99-entrega-15.png` | Cadastro do **webhook** na 99 |
| 12 | `99-entrega-16.png` | Credenciais: **ID do cliente / Segredo do cliente / Chave de assinatura** |
| 13 | `99-entrega-17.png` | BeeFood → menu **Aplicativos** |
| 14 | `99-entrega-18.png` | Seção **Entregas → 99 Entrega** |
| 15 | `99-entrega-19.png` | Tela de credenciais no BeeFood → **Salvar** |
| 16 | `99-entrega-20.png` | **Delivery**: localizar o pedido (DELIVERY) |
| 17 | `99-entrega-21.png` | Detalhe do pedido → **Adicionar Entregador** |
| 18 | `99-entrega-22.png` | Selecionar **99 Entrega** (cotação automática) |
| 19 | `99-entrega-23.png` | Visualizar cotação → **Confirmar** |
| 20 | `99-entrega-24.png` | Pedido **vinculado à 99 Entrega** (lixeira p/ cancelar) |
