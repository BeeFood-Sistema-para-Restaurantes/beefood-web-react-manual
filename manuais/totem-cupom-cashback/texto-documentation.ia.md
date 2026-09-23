# texto-documentation.ia.md — Cupom e cashback no totem

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `totem-cupom-cashback.md`
  e das imagens listados neste prompt.
- **Não publique**, em nenhuma seção: rota ou URL de API (`/api/...`); nome de campo,
  de arquivo, de componente, de tabela ou de coluna; bloco de código, JSON ou
  `campo=true`; nem as palavras *backend*, *endpoint*, *payload*, *array*, *bundle*.
  Se a frase só faz sentido para quem programa, ela não entra. Única exceção: a URL
  completa de webhook que o lojista copia para o painel do parceiro.
- Se você leu **qualquer outro arquivo** desta pasta — `fluxo-codigo.md`,
  `MEMORIA.md`, `annotate.py`, `capturar.py` —, **descarte o que leu**: são anotações
  internas de quem produziu o manual.
- Em 23/09/2026 uma página publicada saiu com a rota da API do cupom e dois nomes de
  campo do cashback, porque esta regra não estava aqui em cima.

Em **Fidelidade (CRM)**, adicione um item de menu por último chamado **Cupom e
cashback no totem**.

Leia APENAS os arquivos abaixo:

    10|1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/totem-cupom-cashback/totem-cupom-cashback.md`
2. Imagens (nesta ordem):
   - `beefood-web-react-manual/manuais/totem-cupom-cashback/imagens-tratadas/01-crm-cupons-canal-totem.png`
   - `beefood-web-react-manual/manuais/totem-cupom-cashback/imagens-tratadas/02-crm-cupom-canais-regras.png`
   - `beefood-web-react-manual/manuais/totem-cupom-cashback/imagens-tratadas/03-crm-cupom-avancadas.png`
   - `beefood-web-react-manual/manuais/totem-cupom-cashback/imagens-tratadas/04-crm-cashback-modalidades.png`
   - `beefood-web-react-manual/manuais/totem-cupom-cashback/imagens-tratadas/05-crm-cashback-percentual.png`
   - `beefood-web-react-manual/manuais/totem-cupom-cashback/imagens-tratadas/06-totem-identificacao-cashback.png`
   - `beefood-web-react-manual/manuais/totem-cupom-cashback/imagens-tratadas/07-totem-confirmacao-cupom-cashback.png`
    20|   - `beefood-web-react-manual/manuais/totem-cupom-cashback/imagens-tratadas/08-totem-cupons-regras.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter a tabela das **duas chaves** na abertura (canal *Totem*
  no cupom e modalidade *Pedidos via Totem* no cashback).
- Manter a tabela **"De onde sai cada frase"** (regra do CRM → texto que o totem
  escreve) e a seção numerada **"Por que o cupom não apareceu no totem?"**.
- Destacar: o totem **não configura** cupom nem cashback, ele lê o CRM; cliente
    30|  que **pula a identificação** não tem cashback nem cupom com login; **dia
  desmarcado** desliga ganho e uso do cashback; o saldo é processado **na
  madrugada**; cupom de **Frete Grátis** não vale no totem.
- Manter a distinção entre **saldo disponível** (compras anteriores, pode usar
  agora) e **você ganhará** (crédito desta compra).
- **SEO**: manter as palavras de busca do lojista nos títulos e na FAQ (*cupom no
  totem*, *cashback no totem*, *cupom não aparece no totem*, *desconto no
  autoatendimento*, *cupom de primeira compra*, *confirmar telefone por SMS*).
  Não trocar por sinônimos genéricos nem resumir a FAQ.
- Não publicar o rodapé interno.
    40|
## Estrutura da página

1. Antes de começar
2. O cupom só aparece no totem com o canal Totem ligado
3. Dentro do cupom: o canal à esquerda, as regras à direita
4. Configurações avançadas: pagamento e itens que liberam o cupom
5. Cashback: ligar a modalidade Pedidos via Totem
6. O percentual que o totem anuncia
7. Como o cliente vê: a oferta antes do telefone
    50|8. Como o cliente vê: o selo de cupons e o saldo na confirmação
9. Como o cliente vê: as regras do cupom em texto (+ De onde sai cada frase)
10. Por que o cupom não apareceu no totem?
11. Problemas comuns
12. Perguntas frequentes
13. Manuais relacionados

## Anexo — legendas

| Ordem | Arquivo | Tipo | Legenda |
    60||-------|---------|------|---------|
| 1 | `01-crm-cupons-canal-totem.png` | com setas | A lista de cupons filtrada pelo canal Totem |
| 2 | `02-crm-cupom-canais-regras.png` | com setas | O cupom: canais de visibilidade e regras na mesma tela |
| 3 | `03-crm-cupom-avancadas.png` | com setas | Configurações avançadas: formas de pagamento, setores e produtos |
| 4 | `04-crm-cashback-modalidades.png` | com setas | O programa de cashback e a modalidade Pedidos via Totem |
| 5 | `05-crm-cashback-percentual.png` | com setas | O percentual de cashback por dia da semana |
| 6 | `06-totem-identificacao-cashback.png` | com setas | O totem oferecendo cashback antes do telefone |
| 7 | `07-totem-confirmacao-cupom-cashback.png` | com setas | Selo de cupons, saldo de cashback e o "você ganhará" |
| 8 | `08-totem-cupons-regras.png` | com setas | A lista de cupons no totem, com as regras em texto e o selo LOGIN |

    70|As imagens 6, 7 e 8 são telas do **aparelho** (1080×1920, retrato) — publicar sem
redimensionar para as frases das regras continuarem legíveis.
