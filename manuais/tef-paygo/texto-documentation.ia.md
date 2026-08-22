# texto-documentation.ia.md — #53 TEF PayGo (Client PayGo)

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Configuração**, adicione um manual por último chamado **"TEF PayGo"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/tef-paygo/tef-paygo.md`

2. **Imagens (use estas 15, nesta ordem):**
   - `beefood-web-react-manual/manuais/tef-paygo/imagens-tratadas/01-pinpad.png`
   - `beefood-web-react-manual/manuais/tef-paygo/imagens-tratadas/02-exemplo-pdc.png`
   - `beefood-web-react-manual/manuais/tef-paygo/imagens-tratadas/03-paygo-chave.png`
   - `beefood-web-react-manual/manuais/tef-paygo/imagens-tratadas/04-paygo-cnpj-pdc.png`
   - `beefood-web-react-manual/manuais/tef-paygo/imagens-tratadas/05-adm-configuracao.png`
   - `beefood-web-react-manual/manuais/tef-paygo/imagens-tratadas/06-senha-tecnica.png`
   - `beefood-web-react-manual/manuais/tef-paygo/imagens-tratadas/07-id-ponto-captura.png`
   - `beefood-web-react-manual/manuais/tef-paygo/imagens-tratadas/08-ip-servidor.png`
   - `beefood-web-react-manual/manuais/tef-paygo/imagens-tratadas/09-adm-instalacao.png`
   - `beefood-web-react-manual/manuais/tef-paygo/imagens-tratadas/10-senha-instalacao.png`
   - `beefood-web-react-manual/manuais/tef-paygo/imagens-tratadas/11-cnpj-cliente.png`
   - `beefood-web-react-manual/manuais/tef-paygo/imagens-tratadas/12-instalacao-ok.png`
   - `beefood-web-react-manual/manuais/tef-paygo/imagens-tratadas/13-erro-autenticacao.png`
   - `beefood-web-react-manual/manuais/tef-paygo/imagens-tratadas/14-reset-acbr.png`
   - `beefood-web-react-manual/manuais/tef-paygo/imagens-tratadas/15-beefood-lista-tef.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `tef-paygo.md` exatamente como está (seções, textos e tabelas).
- Insira as 15 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Idioma **português do Brasil**, tom didático (usuário final / restaurante).
- Mantenha em destaque: Client PayGo no Windows (PDC, senha 314159, IP) + cadastro em Configuração → TEF → Novo TEF PayGo (título/vias, sem StoneCode).
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-pinpad.png` | contexto | Pinpad |
| 2 | `02-exemplo-pdc.png` | contexto | Exemplo PDC |
| 3 | `03-paygo-chave.png` | contexto | Chave no Client PayGo |
| 4 | `04-paygo-cnpj-pdc.png` | contexto | CNPJ e PDC |
| 5 | `05-adm-configuracao.png` | contexto | ADM → Configuração |
| 6 | `06-senha-tecnica.png` | contexto | Senha técnica |
| 7 | `07-id-ponto-captura.png` | contexto | ID ponto de captura |
| 8 | `08-ip-servidor.png` | contexto | IP servidor |
| 9 | `09-adm-instalacao.png` | contexto | ADM → Instalação |
| 10 | `10-senha-instalacao.png` | contexto | Senha na instalação |
| 11 | `11-cnpj-cliente.png` | contexto | CNPJ |
| 12 | `12-instalacao-ok.png` | contexto | Instalação OK |
| 13 | `13-erro-autenticacao.png` | contexto | Erro de autenticação |
| 14 | `14-reset-acbr.png` | contexto | Reset ACBr |
| 15 | `15-beefood-lista-tef.png` | setas | Novo TEF PayGo (F2) |
