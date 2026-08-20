# MEMÓRIA — Manual de Campanhas Inteligentes

> Memória detalhada deste manual (fluxo, uso, decisões e estado), para retomar a qualquer momento.
> Ver também a memória geral: `../../MEMORIA-GERAL.md`.

Status: ✅ **Concluído** — Última atualização: 2026-08-20

---

## 1. Escopo do manual

Definido pelo dono: **explicar as campanhas que já vêm como padrão**, os campos, as variáveis
das mensagens e os parâmetros dos passos 1, 2 e 3. Não é um tutorial de criação — criar campanha
do zero fica para um manual seguinte, de **receitas** combinando segmentação com campanhas
inteligentes (registrado no checklist como ideia).

Arquivo final: `campanhas-inteligentes.md`. Mapa técnico: `fluxo-codigo.md`.

---

## 2. Conteúdo da pasta

```
manuais/campanhas-inteligentes/
├─ MEMORIA.md                    (este arquivo)
├─ campanhas-inteligentes.md     (manual final — 20 imagens)
├─ fluxo-codigo.md               (mapa do código: modelos, defaults, variáveis, endpoints)
├─ texto-documentation.ia.md     (prompt de publicação)
├─ annotate.py                   (gera imagens-tratadas a partir de imagens-puras)
├─ imagens-puras/                (22 originais — backup)
└─ imagens-tratadas/             (20 usadas no manual)
```

As puras `06-variacao-detalhe.png` e `21-novo-como-comecar.png` **não** foram para tratadas:
a 06 era a mesma variação da 17, mas sem variação automática no texto; a 21 é a tela "como você
quer começar", que pertence ao manual de criação, fora deste escopo.

A numeração das tratadas tem lacunas (06 e 21) porque o nome do arquivo é o mesmo da captura —
a ordem de leitura do manual está no `texto-documentation.ia.md`.

---

## 3. Onde a funcionalidade fica

**Não é item de menu.** É a terceira aba de **Food Marketing → Campanhas WhatsApp**:
`/food-marketing/campanhas-whatsapp?tab=automacao`. Só existe no desktop.

Permissão: **itemID 167 / formularioID 127** — os mesmos das Campanhas WhatsApp. Quem vê uma
aba vê a outra; não existe permissão separada, apesar de a chave JSON `campanhaInteligente` ser
distinta de `campanhaWhatsApp`.

---

## 4. O que foi capturado, e como

Ambiente: conta **BeeFood3 - Manual** (`contato@beefood.com.br`), produção, tema claro (a conta
já estava em tema claro). Playwright no Cloud Agent, viewport 1440×900 com
`device_scale_factor=1.5` → imagens 2160×1350.

Seis scripts curtos, um por etapa, em `/tmp/cap/` (não versionados):

| Script | Imagens |
|--------|---------|
| `cap01_lista.py` | 01 lista, 02 card ativo, 03 card rascunho |
| `cap02_passos12.py` | 04 passo 1, 05 passo 2, 06 variação, 07 aviso sem link |
| `cap03_passo3.py` | 08 agenda, 09/10 anti-banimento, 11 alerta, 12 ritmo |
| `cap04_variaveis.py` | 13 gatilho por evento, 14/15 variáveis, 16 spintax |
| `cap05_resultado.py` | 17 variação com spintax, 18 resultado, 19 histórico |
| `cap06_ativar_modelos.py` | 20 diálogo de ativação, 21/22 modelos |

### Nada foi alterado no ambiente

O editor **não tem auto-save**: só grava no **SALVAR (F2)** ou ao confirmar a ativação. Isso
permitiu abrir as campanhas, navegar pelos três passos e até mexer nos campos apenas para
fotografar, saindo sempre por **CANCELAR (ESC)**.

Duas telas exigiram cuidado extra:

- **Alerta de risco do Anti Banimento** (imagem 11): foi preciso desligar o switch e clicar em
  **SALVAR (F2)**. É seguro porque o `handleSave` retorna antes de qualquer chamada de API quando
  a proteção está desligada e o risco não foi confirmado (`AutomacaoEditorModal.tsx`, linhas
  204-208). Saída por **VOLTAR E ATIVAR (ESC)**, e o switch foi religado antes de fechar.
- **Diálogo de ativação** (imagem 20): o switch do card apenas abre o diálogo
  (`onCheckedChange` → `setConfirmAtivar`); a ativação só ocorre ao confirmar. Foi usado na
  **Aniversário**, que está em rascunho, e cancelado.

Ao fim, a Aniversário continuava em **Rascunho** e as quatro campanhas ativas seguiram ativas —
conferido pela API depois da captura.

### Detalhes de captura

- O widget flutuante de suporte (`div.fixed.bottom-6`, 56×56 no canto inferior esquerdo) cobria
  o valor de receita do card de carrinho abandonado. Escondido por CSS
  (`page.add_style_tag`) só no momento do screenshot.
- A aba leva de 10 a 16 segundos para carregar os cards; o editor, cerca de 10 segundos.
- Recortes de card e de bloco foram feitos com `locator.screenshot()`, não com corte manual.
- `full_page=True` não muda nada nesta tela: a rolagem é interna ao container.

---

## 5. Decisões de conteúdo

1. **O manual abre pelo alerta**, não pela definição. Quatro campanhas já estão enviando
   mensagem em qualquer conta, e essa é a informação que o leitor precisa primeiro.
2. **A tabela da configuração de fábrica é o centro do manual.** Os valores saíram de
   `modelos.js`, não da tela, porque a tela mostra o que a loja tem hoje — que pode ter sido
   ajustado.
3. **A concordância errada da tela não foi reproduzida.** O produto escreve "Nossos campanhas
   inteligentes", "Novo campanha inteligente", "Campanha inteligente salvo". O manual escreve em
   português correto, citando o rótulo literal apenas quando manda clicar num botão.
4. **Variação automática ensinada pela ajuda da tela**, não pelo texto da campanha de
   aniversário: a instância do sandbox está com o texto antigo, sem `{a|b}` (ver achado 1
   abaixo). O exemplo real veio da campanha de carrinho abandonado.
5. **Telefone do cliente coberto na imagem pura**, não só na tratada. O repositório é público;
   nenhum dado pessoal pode ser versionado em nenhuma das duas pastas.

---

## 6. Achados que valem para qualquer conta

**1. Instância antiga não recebe a melhoria do modelo.** A campanha **Aniversário** do sandbox
tem 4 variações **sem** variação automática (`"Feliz aniversário, {{primeiro_nome}}! ..."`),
enquanto o modelo no código atual traz `"{Feliz aniversário|Parabéns pelo seu dia}, ..."`. A
**Carrinho abandonado**, por sua vez, está igual ao modelo, com as 9 variações e spintax. Ou
seja: campanha criada por um seed anterior fica congelada. É o caso de usar **Restaurar padrão**
para trazer os textos novos — e o manual diz isso na seção de ligar e pausar.

**2. Parâmetro ajustado não volta ao padrão.** A Carrinho abandonado do sandbox está com
**Esperar antes de enviar = 5 min**, e não os 15 de fábrica. A imagem 13 mostra 5, e o texto do
manual explica que o padrão é 15 — o `texto-documentation.ia.md` avisa para não "corrigir" a
legenda.

**3. Prévia não sorteia a variação automática.** Ela troca as variáveis por exemplos, mas mantém
`{quase pronto|quase completo}` visível. O sorteio só acontece no envio, e isso é comprovável no
**Histórico**: o texto cadastrado `{Olá|Oi}, {{primeiro_nome}}! ...` chegou ao cliente como
"Olá Bruno! ...".

**4. O link enviado leva a marcação da campanha.** No histórico, `{{meu_link}}` saiu como
`https://menu.beefood.com.br/beefood3?a=35` — o `a=35` é o id da campanha, e é assim que o Pixel
atribui a venda. É a razão técnica de a variável ser obrigatória, e o manual explica isso em
linguagem de usuário.

**5. A descrição do card do BeeBot está errada no produto.** "Recebeu o cardápio e não pediu"
mostra "Traz de volta quem já comprou e sumiu", porque o modelo usa `tipo: RECUPERACAO`. O
manual descreve o comportamento correto e ignora a frase do card.

---

## 7. Estado deixado no sistema

Nada alterado. As seis campanhas seguem como estavam em 20/08/2026:

| Campanha | Estado | Envios |
|---|---|---|
| Carrinho abandonado | Ativo | 1 envio, 1 pedido, R$ 34,02 |
| Recebeu o cardápio e não pediu | Ativo | 1 envio, 1 pedido, R$ 3,89 |
| Recuperador de vendas | Ativo | — |
| Cashback parado | Ativo | — |
| Boas-vindas / 2ª compra | Pausado | — |
| Aniversário | Rascunho | — |

---

## 8. Possíveis próximos incrementos

- **Receitas de campanhas** (segmentação + campanha inteligente): o manual extra pedido pelo
  dono, já registrado como ideia no checklist.
- Aba **Indicadores** da mesma página (analytics de BeeBot, campanha e campanha inteligente),
  não coberta por nenhum manual.
- Criar campanha **do zero** e aplicar modelo: a tela "como você quer começar" já está capturada
  em `imagens-puras/21-novo-como-comecar.png`.
