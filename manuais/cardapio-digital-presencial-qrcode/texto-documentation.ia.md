# texto-documentation.ia.md — #77 Cardápio digital presencial e QR Code

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Cardápio Digital**, adicione um manual chamado
**"Cardápio digital presencial e QR Code"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/cardapio-digital-presencial-qrcode/cardapio-digital-presencial-qrcode.md`

2. **Imagens (use estas 11, nesta ordem):**
   - `beefood-web-react-manual/manuais/cardapio-digital-presencial-qrcode/imagens-tratadas/01-onde-fica.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-presencial-qrcode/imagens-tratadas/02-parametros.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-presencial-qrcode/imagens-tratadas/03-garcom-opcoes.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-presencial-qrcode/imagens-tratadas/04-qr-geral.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-presencial-qrcode/imagens-tratadas/05-qr-mesa.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-presencial-qrcode/imagens-tratadas/06-meus-links.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-presencial-qrcode/imagens-tratadas/07-meus-links-mesa.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-presencial-qrcode/imagens-tratadas/09b-recomendacao-comanda.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-presencial-qrcode/imagens-tratadas/08-gerador-passo1.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-presencial-qrcode/imagens-tratadas/09-tipo-qr.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-presencial-qrcode/imagens-tratadas/10-cardapio-digital.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `cardapio-digital-presencial-qrcode.md` exatamente como está (seções, textos e tabelas).
- Insira as 11 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"**.
- Idioma **português do Brasil**, tom didático.
- Mantenha em destaque: auto-save; Presencial ≠ Consumo no Local; os dois tipos de QR; o gerador da Configurações **não confere** o cadastro de mesas; Meus Links tem `presencial.beefood.com.br`, o cardápio de **visualização** (sem pedido) e o aviso *Recomendamos gerar QR Code de Comanda* (só neste painel).
- Aponte os manuais **"Horário de atendimento"** e **"Fechar a loja fora do horário"** como leitura complementar.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-onde-fica.png` | setas | Card Presencial: switch, link e os três QR |
| 2 | `02-parametros.png` | setas | Cadastro, e-mail, nascimento, garçom, fechamento |
| 3 | `03-garcom-opcoes.png` | setas | Modal Opções do Garçom |
| 4 | `04-qr-geral.png` | setas | QR Code Presencial (um código) |
| 5 | `05-qr-mesa.png` | setas | Intervalo de mesas gerado |
| 6 | `06-meus-links.png` | setas | Grupo Cardápios Presencial |
| 7 | `07-meus-links-mesa.png` | setas | Link amarrado à Mesa 2 |
| 8 | `09b-recomendacao-comanda.png` | setas | Aviso: use o QR da comanda |
| 9 | `08-gerador-passo1.png` | setas | Mesas ou Comandas |
| 10 | `09-tipo-qr.png` | setas | Cardápio Digital × Código da Mesa |
| 11 | `10-cardapio-digital.png` | tira | Pedir × só olhar (aba Pedidos) |
