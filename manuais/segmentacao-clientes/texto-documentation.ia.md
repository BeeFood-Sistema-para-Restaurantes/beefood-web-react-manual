# texto-documentation.ia.md — Segmentação de Clientes

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.
> O projeto do manual **já está anexo no contexto** — o prompt aponta os **arquivos exatos** a ler.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Food Marketing**, adicione um **item de menu por último** chamado **"Segmentação de Clientes"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/segmentacao-clientes/segmentacao-clientes.md`

2. **Imagens (use estas 9, nesta ordem):**
   - `beefood-web-react-manual/manuais/segmentacao-clientes/imagens-tratadas/01-lista.png`
   - `beefood-web-react-manual/manuais/segmentacao-clientes/imagens-tratadas/03-seletor-campo.png`
   - `beefood-web-react-manual/manuais/segmentacao-clientes/imagens-tratadas/04-primeira-regra.png`
   - `beefood-web-react-manual/manuais/segmentacao-clientes/imagens-tratadas/05-resultado-teste.png`
   - `beefood-web-react-manual/manuais/segmentacao-clientes/imagens-tratadas/06-duas-regras-e.png`
   - `beefood-web-react-manual/manuais/segmentacao-clientes/imagens-tratadas/07-duas-regras-ou.png`
   - `beefood-web-react-manual/manuais/segmentacao-clientes/imagens-tratadas/08-detalhes.png`
   - `beefood-web-react-manual/manuais/segmentacao-clientes/imagens-tratadas/09-clientes-do-publico.png`
   - `beefood-web-react-manual/manuais/segmentacao-clientes/imagens-tratadas/02-modelos-prontos.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**

- Use o conteúdo do `segmentacao-clientes.md` exatamente como está (seções, textos e tabelas "Nº da seta → campo").
- A seção **"Oito segmentações para copiar"** é o coração do manual. Publique os oito exemplos na íntegra, cada um com o problema, a tabela de filtros e o "o que fazer". Não resuma nem corte exemplos.
- Insira as 9 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Use **números normais** (`1`, `2`, `3`) nas referências às setas — **não** use números circulados (①②③).
- Idioma **português do Brasil**, tom didático (usuário final).
- Mantenha em destaque, sem resumir:
  - **a segmentação é uma receita, não uma lista** — ela se recalcula a cada uso;
  - **a base elegível**: só entram clientes com telefone válido, ativos e que aceitam mensagem no WhatsApp, e é sobre essa base que o percentual é calculado;
  - **a pegadinha dos campos em reais**: digitar `50` resulta em R$ 0,50; para R$ 50,00 é preciso digitar `5000` ou `50,00`;
  - **o E / OU vale para a lista inteira**, não por linha;
  - **filtros de lista guardam tudo o que o cliente já fez** — daí o truque das duas linhas do exemplo 7;
  - os **públicos com selo BeeFood** são só leitura e se personalizam por **duplicar**.
- O manual é de **desktop**. Não descreva a versão mobile.
- Se o app permitir, cite as **Campanhas de WhatsApp** e as **Campanhas Inteligentes** como leituras seguintes.

---

## Estrutura da página (na ordem do `.md`)

1. Introdução (o que o manual ensina)
2. **Por que segmentar**
3. **O conceito mais importante: é uma receita, não uma lista** (com a base elegível)
4. **A tela**
5. **Criando a primeira segmentação** (escolher o filtro, montar a regra, testar)
6. **Combinando filtros: E ou OU**
7. **Depois de salvar** (detalhes, ver clientes)
8. **Modelos prontos** e os públicos com selo BeeFood
9. **Oito segmentações para copiar**
10. **Outros filtros que valem conhecer**
11. **E depois? Onde o público é usado**
12. **Dicas finais**

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-lista.png` | com setas | 1 **Nova segmentação** · 2 **Modelos prontos** · 3 aviso da base elegível · 4 selo **BeeFood** · 5 ações da linha |
| 2 | `03-seletor-campo.png` | com setas | 1 os **37 campos** disponíveis · 2 busca por nome ou categoria · 3 as nove categorias · 4 o cartão de um filtro |
| 3 | `04-primeira-regra.png` | com setas | 1 **Nome da segmentação** · 2 **Ativa** · 3 o filtro · 4 o operador · 5 o valor · 6 **ADICIONAR REGRA** · 7 **TESTAR PÚBLICO** · 8 **SALVAR (F2)** |
| 4 | `05-resultado-teste.png` | com setas | 1 o percentual · 2 quantos de quantos elegíveis · 3 **Ver clientes** |
| 5 | `06-duas-regras-e.png` | com setas | 1 primeira condição · 2 o seletor **E / OU** · 3 segunda condição · 4 valor em reais |
| 6 | `07-duas-regras-ou.png` | com setas | 1 filtro de opções com vários valores · 2 **OU** marcado · 3 valor em reais |
| 7 | `08-detalhes.png` | com setas | 1 **FILTROS ESCOLHIDOS** · 2 o tamanho do público · 3 **Editar** · 4 **Exportar Excel** |
| 8 | `09-clientes-do-publico.png` | com setas | 1 o total de clientes · 2 busca dentro do público · 3 os indicadores de cada cliente |
| 9 | `02-modelos-prontos.png` | com setas | 1 a categoria do modelo · 2 **Pré-visualizar** · 3 **Usar este modelo** |

---

## Observações de conteúdo

- Os exemplos são reais: as oito segmentações foram criadas na conta de testes
  "BeeFood3 - Manual" e os números citados (8 clientes, 6 clientes, 53,3%...) são o resultado
  medido numa base de **15 clientes elegíveis**. O manual já avisa que no restaurante do leitor
  os números serão outros.
- Na imagem `09-clientes-do-publico.png` os **dados pessoais estão borrados de propósito**. O
  manual explica isso em uma linha; mantenha o aviso.
- **Não** publique nada do `fluxo-codigo.md` (itemIDs, rotas de API, nomes de tabela, caches,
  nomes internos de campo) nem o rodapé "Referências internas" do `.md`.
- O manual **não promete** limiares do RFV nem a fórmula do ticket médio: esses cálculos ficam
  fora do código que pudemos verificar. Se for enriquecer o texto, não invente esses números.
