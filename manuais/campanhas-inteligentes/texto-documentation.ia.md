# texto-documentation.ia.md — Campanhas Inteligentes

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.
> O projeto do manual **já está anexo no contexto** — o prompt aponta os **arquivos exatos** a ler.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Food Marketing**, adicione um **item de menu por último** chamado **"Campanhas Inteligentes"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/campanhas-inteligentes/campanhas-inteligentes.md`

2. **Imagens (use estas 20, nesta ordem):**
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/01-lista-campanhas.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/02-card-anatomia.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/03-card-rascunho.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/22-modelos-prontos.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/04-passo1-publico-segmentacao.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/13-passo1-gatilho-evento.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/05-passo2-variacoes.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/17-variacao-com-spintax.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/07-aviso-sem-link.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/14-modal-variaveis.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/15-variaveis-bloqueadas.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/16-spintax.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/08-passo3-agenda.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/09-anti-banimento-ligado.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/10-anti-banimento-desligado.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/11-alerta-risco-banimento.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/12-intervalo-e-ritmo.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/20-dialogo-ativar.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/18-resultado.png`
   - `beefood-web-react-manual/manuais/campanhas-inteligentes/imagens-tratadas/19-historico.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**

- Use o conteúdo do `campanhas-inteligentes.md` exatamente como está (seções, textos e tabelas).
- Insira as 20 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Use **números normais** (`1`, `2`, `3`) nas referências às setas — **não** use números circulados (①②③).
- Idioma **português do Brasil**, tom didático (usuário final).
- Mantenha em destaque, sem resumir:
  - que **quatro campanhas já vêm ligadas** na conta e por isso precisam ser revisadas;
  - a **tabela da configuração de fábrica** das seis campanhas — é a referência principal do manual;
  - que **`{{meu_link}}` é obrigatória** em toda variação, porque é o que permite medir a venda;
  - que **nove variáveis dependem do histórico** e aparecem com cadeado nas campanhas de carrinho abandonado e de cardápio sem pedido;
  - a diferença entre **chave simples com barra** (sorteio) e **chave dupla** (variável);
  - a proteção **Anti Banimento** e o alerta de risco ao desligá-la;
  - que **ligar não dispara mensagem na hora** — a campanha passa a observar os gatilhos.
- O manual é de **desktop**: as Campanhas Inteligentes não existem no aplicativo mobile. Não descreva versão mobile.
- Se o app permitir, cite a **Segmentação de Clientes** como leitura anterior e as **Campanhas de WhatsApp** como leitura complementar.

---

## Estrutura da página (na ordem do `.md`)

1. Introdução (o que o manual ensina)
2. **Onde encontrar** (com a tabela Campanhas × Campanhas Inteligentes)
3. **Antes de tudo: quatro campanhas já estão enviando**
4. **Como ler o card de uma campanha** (com a tabela dos três gatilhos)
5. **As seis campanhas padrão** (uma seção por campanha + tabela da configuração de fábrica)
6. **Passo 1 — Identificação e público**
7. **Passo 2 — A mensagem e suas variações** (com o link obrigatório)
8. **As variáveis das mensagens** (grupos, básicas, bloqueadas, foto, variação automática)
9. **Passo 3 — Agenda e anti-spam** (Anti Banimento e ritmo)
10. **Ligar e pausar** (e Restaurar padrão)
11. **Ler o resultado** (Resultado e Histórico)
12. **Dicas para não perder o número**

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-lista-campanhas.png` | com setas | 1 aba **Campanhas Inteligentes** · 2 selo **Ativo** · 3 chave liga/desliga · 4 **Pausado** · 5 **Rascunho** |
| 2 | `02-card-anatomia.png` | com setas | 1 estado · 2 selo **BeeFood** · 3 chave liga/desliga · 4 selo do gatilho · 5 receita gerada · 6 **Resultado** e **Histórico** |
| 3 | `03-card-rascunho.png` | com setas | 1 selo **Rascunho** · 2 **Revisar e ativar** |
| 4 | `22-modelos-prontos.png` | contexto | Os seis modelos prontos, com a descrição de cada campanha |
| 5 | `04-passo1-publico-segmentacao.png` | com setas | 1 **Cardápio** · 2 **Segmentação** · destaques em **Como esta automação funciona** e **Origem do público** |
| 6 | `13-passo1-gatilho-evento.png` | com setas | 1 **Esperar antes de enviar (min)** · 2 a frase-resumo da janela · destaques em **Origem do público** e **Considerar eventos das últimas (h)** |
| 7 | `05-passo2-variacoes.png` | contexto | O passo 2 com as variações da mensagem |
| 8 | `17-variacao-com-spintax.png` | com setas | 1 trecho com variação automática · 2 **Prévia** · destaque na tag obrigatória e em **Inserir variável** |
| 9 | `07-aviso-sem-link.png` | contexto | O aviso que aparece quando a mensagem fica sem o link do cardápio |
| 10 | `14-modal-variaveis.png` | contexto | O catálogo de variáveis, com busca e categorias |
| 11 | `15-variaveis-bloqueadas.png` | contexto | Variáveis com cadeado: dependem do histórico e não funcionam neste gatilho |
| 12 | `16-spintax.png` | contexto | A ajuda da variação automática, com exemplos |
| 13 | `08-passo3-agenda.png` | com setas | 1 **Dias da semana** · 2 **Horário de início** · 3 **Anti Banimento** · 4 **Intervalo mín. entre mensagens** · destaque no aviso do cardápio aberto |
| 14 | `09-anti-banimento-ligado.png` | contexto | A proteção ligada, com a janela de dias |
| 15 | `10-anti-banimento-desligado.png` | contexto | A proteção desligada e o aviso de risco |
| 16 | `11-alerta-risco-banimento.png` | contexto | O alerta **Atenção: risco alto de perder seu número!** |
| 17 | `12-intervalo-e-ritmo.png` | contexto | **Intervalo mín. entre mensagens** e **Ritmo: envios por dia** |
| 18 | `20-dialogo-ativar.png` | contexto | A confirmação para ligar uma campanha |
| 19 | `18-resultado.png` | contexto | **Resultado**: jornadas, envios e ROI da campanha |
| 20 | `19-historico.png` | com setas | 1 **Exportar CSV** · 2 a mensagem como o cliente recebeu · 3 **Converteu?** |

---

## Observações de conteúdo

- Os números das imagens são reais, da conta de testes "BeeFood3 - Manual": a campanha de
  carrinho abandonado tem 1 envio, 1 pedido e R$ 34,02 de receita. O manual não promete
  resultados; usa os números apenas para explicar onde cada informação aparece.
- Na imagem `13-passo1-gatilho-evento.png` o campo **Esperar antes de enviar** mostra **5
  minutos**, porque a loja de testes ajustou esse valor. O padrão de fábrica é **15 minutos**, e
  o texto do manual já explica isso. **Não troque** a legenda nem o texto para 5 minutos.
- Na imagem `19-historico.png` o **telefone do cliente foi coberto de propósito**. Mantenha a
  imagem como está.
- **Não** publique nada do `fluxo-codigo.md` (itemIDs, rotas de API, nomes de campo do banco,
  chaves dos modelos) nem os achados internos sobre o sandbox.
- O manual **não** descreve como criar uma campanha do zero em detalhe: isso fica para o manual
  seguinte, de receitas de campanhas com segmentação. Se for enriquecer o texto, não invente
  esse conteúdo.
