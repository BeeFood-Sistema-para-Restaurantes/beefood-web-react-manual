# texto-documentation.ia.md — Integração Machine

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.
> O projeto do manual **já está anexo no contexto** — o prompt aponta os **arquivos exatos** a ler.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Aplicativos** (seção **Entrega/Integrações**), adicione um manual
chamado **"Integração Machine"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/integracao-machine/integracao-machine.md`

2. **Imagens (use estas 7, nesta ordem):**
   - `beefood-web-react-manual/manuais/integracao-machine/imagens-tratadas/machine-01.png`
   - `beefood-web-react-manual/manuais/integracao-machine/imagens-tratadas/machine-02.png`
   - `beefood-web-react-manual/manuais/integracao-machine/imagens-tratadas/machine-03.png`
   - `beefood-web-react-manual/manuais/integracao-machine/imagens-tratadas/machine-04.png`
   - `beefood-web-react-manual/manuais/integracao-machine/imagens-tratadas/machine-05.png`
   - `beefood-web-react-manual/manuais/integracao-machine/imagens-tratadas/machine-06.png`
   - `beefood-web-react-manual/manuais/integracao-machine/imagens-tratadas/machine-07.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `integracao-machine.md` exatamente como está (seções, textos e tabelas).
- Insira as 7 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Idioma **português do Brasil**, tom didático (usuário final / restaurante).
- Mantenha em destaque: credenciais vêm da **central Machine**; **Empresa ID (Machine)** é diferente do
  empresaID do BeeFood; a sincronização pode ser **manual ou automática**; cancelamento é pela **lixeira**
  na guia Entregador.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Legenda |
|------:|----------------------------------|---------|
| 1 | `machine-01.png` | Menu lateral → **Aplicativos** |
| 2 | `machine-02.png` | Aba **Entrega** → card **Machine** |
| 3 | `machine-03.png` | Tela de configuração da Machine (credenciais e opções) |
| 4 | `machine-04.png` | **Delivery**: localizar o pedido |
| 5 | `machine-05.png` | Botão **Adicionar Entregador** |
| 6 | `machine-06.png` | **Entrega Terceirizada → Machine** |
| 7 | `machine-07.png` | Guia Entregador — **Entregue por Machine** (lixeira p/ cancelar) |
