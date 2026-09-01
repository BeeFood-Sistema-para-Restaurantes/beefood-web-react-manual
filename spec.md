# BeeFood — Manuais (spec)

Repositório de manuais de usuário final do BeeFood (`https://beefood.app`).

## Stack

- Markdown + imagens PNG (puras + tratadas com `annotate.py`)
- Python 3.10+ e Pillow para anotações
- Playwright para capturas no Cloud Agent
- Código de referência: `beefood-web-react` e `beetech-server-node-2.0` (somente leitura)

## Estrutura

```
manuais/<nome>/
├── <nome>.md
├── fluxo-codigo.md
├── MEMORIA.md
├── texto-documentation.ia.md
├── annotate.py
├── imagens-puras/
└── imagens-tratadas/
```

## Conta sandbox

**BeeFood3 - Manual** — `contato@beefood.com.br`

## Planos executados

| Plano | Manuais | Documento |
|-------|---------|-----------|
| Cardápio por segmento | #27–#31 (concluídos) | [`PLANO-CARDAPIO.md`](PLANO-CARDAPIO.md) |
| Avisos do cardápio digital | #47 (concluído) | `manuais/cardapio-digital-avisos/` |
| Capas e Destaques | #48 (concluído) | `manuais/cardapio-digital-capas-destaques/` |
| Área de entrega | #34–#38 (refação 21/08/2026) | `manuais/endereco-restaurante/` + `manuais/area-entrega-*` |
| Parâmetros (Configuração) | #39–#46 concluídos (Opção B — 8 manuais) | [`PLANO-PARAMETROS.md`](PLANO-PARAMETROS.md) |
| Migração do ajuda.beefood | #49–#56 (concluídos 22/08/2026) | [`PLANO-MIGRACAO-AJUDA.md`](PLANO-MIGRACAO-AJUDA.md) |
| BeeFood Entregador (app motoboy) | #57 (concluído 26/08/2026) | `manuais/app-entregadores/` |
| IA ChatGPT no WhatsApp | #58 (concluído 28/08/2026) | `manuais/ia-chatgpt-whatsapp/` |
| Campanhas SMS | #18 (concluído 28/08/2026) | `manuais/campanhas-sms/` |
| Cupom de Desconto (campos + cardápio) | #21 (concluído 28/08/2026) | `manuais/cupom-desconto/` |
| Cashback — configurar o programa | #19 (concluído 29/08/2026) | `manuais/cashback-configurar/` |
| Cashback — operar no dia a dia | #20 (concluído 29/08/2026) | `manuais/cashback-operar/` |
| Desconto nas formas de recebimento | #64 (concluído 30/08/2026) | `manuais/cardapio-digital-desconto-formas/` |
| Taxas das formas de recebimento | #65 (concluído 30/08/2026) | `manuais/taxas-formas-pagamento/` |
| Lançamentos: contas a pagar | #66 (concluído 30/08/2026) | `manuais/lancamentos-contas-pagar/` |
| Lançamentos: contas a receber | #67 (concluído 30/08/2026) | `manuais/lancamentos-contas-receber/` |
| Exibir / Ocultar | #68 (concluído 30/08/2026) | `manuais/exibir-ocultar/` |
| Preço Programado | #69 (concluído 30/08/2026) | `manuais/preco-programado/` |
| Agendamento do cardápio digital | #70 (concluído 30/08/2026) | `manuais/cardapio-digital-agendamento/` |
| Produto só com agendamento (encomenda) | #73 (concluído 31/08/2026) | `manuais/cardapio-digital-agendamento-produto/` |
| Aparência e layout do cardápio digital | #71 (concluído 30/08/2026) | `manuais/cardapio-digital-aparencia-layout/` |
| Ficha técnica (hambúrguer) | #72 (concluído 01/09/2026) | [`PLANO-FICHA-TECNICA.md`](PLANO-FICHA-TECNICA.md) + `manuais/ficha-tecnica/` |
| Entrega Fácil iFood | #59 (concluído 28/08/2026) | `manuais/entrega-facil-ifood/` |
| Let's Express | #60 (concluído 28/08/2026) | `manuais/integracao-lets-express/` |
| Foody Delivery | #61 (concluído 28/08/2026) | `manuais/integracao-foody-delivery/` |
| Pick n Go! | #62 (concluído 28/08/2026) | `manuais/integracao-pick-n-go/` |
| Uai Rango | #63 (concluído 28/08/2026) | `manuais/integracao-uai-rango/` |

## Estudos aguardando aprovação

| Estudo | Situação | Documento |
|--------|----------|-----------|
| **Numeração dos pedidos** (#74) | ⏸️ aguardando aprovação. As quatro regras foram confirmadas em dado real; falta decidir a pergunta dos dois caixas abertos e se o #44 é corrigido junto | [`PLANO-NUMERACAO-PEDIDOS.md`](PLANO-NUMERACAO-PEDIDOS.md) |
| Ficha técnica da **pizza** | ⏸️ em espera: aguarda a correção da pizza. O manual #72 já respondeu a dúvida técnica (opção repetida baixa em dobro) | [`PLANO-FICHA-TECNICA.md`](PLANO-FICHA-TECNICA.md), seção 9 |

Endereço da loja no sandbox (BeeFood3): **R. Caramuru, 108 — Vila Leão, Sorocaba – SP,
18040-370**. Endereço de entrega de teste nos quatro tipos: **R. Arthur Gomes, 13 — Centro,
Sorocaba – SP, 18035-490**. No cardápio, os manuais #35–#38 mostram a **busca** (CEP ou
bairro), o formulário depois da busca e o endereço confirmado com a taxa — sem tela de
*Calculando…*.

Regras que valem para qualquer manual com cenário montado no sandbox: limpar a base **antes de
cada manual** (o dono faz e avisa) e inserir **foto em todos os produtos e opções** dos exemplos,
sem documentar isso no texto.

## Captura (Playwright) — vale para todo manual

**Depois de cada clique, esperar o spinner sumir e só então contar 5 segundos
antes do print.** Não é regra do Delivery: é de qualquer tela.

1. Clique.
2. Se aparecer `Carregando...`, `Atualizando...`, `Calculando…` ou spinner,
   esperar sumir (20–30 s de folga).
3. **Mais 5 segundos** depois do spinner sumir.
4. Só então `screenshot`.

Print cedo demais sai com painel vazio. O #43 já saiu assim (e de novo com
`Atualizando...` no Pronto). A regra permanente está na `MEMORIA-GERAL.md`
(seção 6) — é o arquivo lido no início de cada sessão.

**Tira de celulares (cardápio público):** não publique vários prints altos
soltos. Monte uma tira (`montar_celulares` no `annotate.py`, padrão do #19/#20/#64).
Viewport do aparelho: **390×844** `device_scale_factor=2`. Puras individuais
são fonte; só a tira entra no `.md`. Detalhe na `MEMORIA-GERAL.md` (seção 3).

## Validação

```bash
python validar-imagens.py
python validar-imagens.py fiado
```
