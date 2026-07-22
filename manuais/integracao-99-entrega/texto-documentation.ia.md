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

2. **Imagens (use estas 15, nesta ordem):**
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-01.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-02.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-03.png`
   - `beefood-web-react-manual/manuais/integracao-99-entrega/imagens-tratadas/99-entrega-04.png`
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

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `integracao-99-entrega.md` **exatamente como está** (seções, textos e tabelas) — o
  texto já está pronto, **não reescrever nem interpretar**.
- Insira as 15 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Idioma **português do Brasil**, tom didático (usuário final / restaurante).
- Mantenha em destaque: cadastrar **cartão** na 99 antes de operar; as 3 credenciais vêm do **Modo de
  desenvolvedor** da 99; webhook a cadastrar: `https://entregas.beetechapi.be/api/99Entrega/webhook`;
  cancelamento só **antes** de o entregador retirar o pedido.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Legenda |
|------:|----------------------------------|---------|
| 1 | `99-entrega-01.png` | Painel 99 → **Configurações de pagamento** |
| 2 | `99-entrega-02.png` | Método de pagamento → **Gerenciar** |
| 3 | `99-entrega-03.png` | 99Pay → **Adicionar cartão** |
| 4 | `99-entrega-04.png` | Dados do cartão → **Adicionar** |
| 5 | `99-entrega-05.png` | Painel 99 → **Modo de desenvolvedor** |
| 6 | `99-entrega-06.png` | Webhook → campo **URL (Insira o webhook)** |
| 7 | `99-entrega-07.png` | Credenciais: **ID do cliente / Segredo do cliente / Chave de assinatura** |
| 8 | `99-entrega-08.png` | BeeFood → menu **Aplicativos** |
| 9 | `99-entrega-09.png` | Seção **Entregas → 99 Entrega** |
| 10 | `99-entrega-10.png` | Modal de credenciais no BeeFood → **SALVAR (F2)** |
| 11 | `99-entrega-11.png` | **Delivery**: localizar o pedido (#8) |
| 12 | `99-entrega-12.png` | Detalhe do pedido → **Adicionar Entregador** |
| 13 | `99-entrega-13.png` | **Entrega Terceirizada → 99 Entrega** |
| 14 | `99-entrega-14.png` | Cotação (distância/tempo/frete) → **CONFIRMAR (F2)** |
| 15 | `99-entrega-15.png` | Guia Entregador — **Entregue por 99 Entrega** (lixeira p/ cancelar) |
