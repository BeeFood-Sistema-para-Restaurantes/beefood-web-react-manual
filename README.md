# BeeFood — Manuais de Funcionalidades

Repositório de **manuais de uso (usuário final)** do sistema BeeFood (`https://beefood.app`),
construídos a partir do código do projeto `beefood-web-react` e de capturas de tela reais em produção.

## Estrutura

```
.
├─ MEMORIA-GERAL.md            # Boas práticas, padrões, contas e ferramentas (ler primeiro)
├─ CHECKLIST-MANUAIS.md        # O que já foi feito, o que está na fila e o histórico
├─ PLANO-CARDAPIO.md           # Plano aprovado dos manuais #27–#31 (cardápio por segmento)
├─ PLANO-MIGRACAO-AJUDA.md     # Fila #49–#56 (migração do ajuda.beefood.com.br)
├─ PLANO-NUMERACAO-PEDIDOS.md  # Estudo do #74 (número da venda × número do pedido)
├─ validar-imagens.py          # Confere se as imagens referenciadas pelos manuais existem
└─ manuais/
   └─ <nome-do-manual>/        # Uma pasta por manual
      ├─ MEMORIA.md            # Memória detalhada do manual (fluxo, uso, decisões, estado)
      ├─ <nome>.md             # O manual final (para o usuário)
      ├─ fluxo-codigo.md       # Mapeamento técnico (a partir do código)
      ├─ annotate.py           # Script de anotação (setas/números) — Python + Pillow
      ├─ imagens-puras/        # Screenshots originais (backup, sem edição)
      └─ imagens-tratadas/     # Screenshots com setas/números (usados no manual)
```

## Manuais disponíveis

| Manual | Pasta | Status |
|--------|-------|--------|
| Caixa (abrir, receber pagamento, consultar) | [`manuais/caixa/`](manuais/caixa/caixa.md) | ✅ Concluído |
| Fechar caixa (vendas pendentes, conferência, quebra) | [`manuais/caixa-fechar/`](manuais/caixa-fechar/caixa-fechar.md) | ✅ Concluído |
| Segunda conferência (dupla checagem) | [`manuais/caixa-conferencia-2/`](manuais/caixa-conferencia-2/caixa-conferencia-2.md) | ✅ Concluído |
| Restrições de caixa (grupo de acesso) | [`manuais/caixa-restricoes/`](manuais/caixa-restricoes/caixa-restricoes.md) | ✅ Concluído |
| Reforma Tributária (IBS/CBS) | [`manuais/reforma-tributaria-ibscbs/`](manuais/reforma-tributaria-ibscbs/reforma-tributaria.md) | ✅ Concluído |
| Ativação Aiqfome V2 | [`manuais/ativacao-aiqfome/`](manuais/ativacao-aiqfome/ativacao-aiqfome.md) | ✅ Concluído |
| Integração Machine (entregas) | [`manuais/integracao-machine/`](manuais/integracao-machine/integracao-machine.md) | ✅ Concluído |
| Integração 99 Entrega | [`manuais/integracao-99-entrega/`](manuais/integracao-99-entrega/integracao-99-entrega.md) | ✅ Concluído |
| Integração Repediu (CRM) | [`manuais/integracao-repediu/`](manuais/integracao-repediu/integracao-repediu.md) | ✅ Concluído |
| Integração FoodCRM (CRM) | [`manuais/integracao-foodcrm/`](manuais/integracao-foodcrm/integracao-foodcrm.md) | ✅ Concluído |
| Integração Uber Direct (entregas) | [`manuais/integracao-uber-direct/`](manuais/integracao-uber-direct/integracao-uber-direct.md) | ✅ Concluído |
| Segmentação de clientes (Food Marketing) | [`manuais/segmentacao-clientes/`](manuais/segmentacao-clientes/segmentacao-clientes.md) | ✅ Concluído |
| Campanhas Inteligentes (Food Marketing) | [`manuais/campanhas-inteligentes/`](manuais/campanhas-inteligentes/campanhas-inteligentes.md) | ✅ Concluído |
| Fiado — operar no dia a dia | [`manuais/fiado/`](manuais/fiado/fiado.md) | ✅ Concluído |
| Fiado — cobrança agrupada | [`manuais/fiado-cobranca-agrupada/`](manuais/fiado-cobranca-agrupada/fiado-cobranca-agrupada.md) | ✅ Concluído |
| Cardápio — fundamentos (produto, grupo de opções, complementos, lote) | [`manuais/cardapio-fundamentos/`](manuais/cardapio-fundamentos/cardapio-fundamentos.md) | ✅ Concluído |
| Cardápio — pizza (Valor da Maior e Proporcional) | [`manuais/cardapio-pizza/`](manuais/cardapio-pizza/cardapio-pizza.md) | ✅ Concluído |
| Cardápio — hambúrguer (Brinde e grupo obrigatório) | [`manuais/cardapio-hamburguer/`](manuais/cardapio-hamburguer/cardapio-hamburguer.md) | ✅ Concluído |
| Cardápio — açaí (inclusos com limite e tamanhos) | [`manuais/cardapio-acai/`](manuais/cardapio-acai/cardapio-acai.md) | ✅ Concluído |
| Cardápio — comida japonesa (contagem exata e preço fechado) | [`manuais/cardapio-japonesa/`](manuais/cardapio-japonesa/cardapio-japonesa.md) | ✅ Concluído |
| Horário de atendimento (grade semanal do cardápio digital) | [`manuais/horario-atendimento/`](manuais/horario-atendimento/horario-atendimento.md) | ✅ Concluído |
| Fechar a loja fora do horário (pausas e switches de canal) | [`manuais/loja-fechar-pausa/`](manuais/loja-fechar-pausa/loja-fechar-pausa.md) | ✅ Concluído |
| Avisos do cardápio digital (recado sem CTA) | [`manuais/cardapio-digital-avisos/`](manuais/cardapio-digital-avisos/cardapio-digital-avisos.md) | ✅ Concluído |
| Capas e Destaques (banners com imagem e vídeo) | [`manuais/cardapio-digital-capas-destaques/`](manuais/cardapio-digital-capas-destaques/cardapio-digital-capas-destaques.md) | ✅ Concluído |
| BeeFood Entregador (app do motoboy) | [`manuais/app-entregadores/`](manuais/app-entregadores/app-entregadores.md) | ✅ Concluído |
| Entrega Fácil iFood | [`manuais/entrega-facil-ifood/`](manuais/entrega-facil-ifood/entrega-facil-ifood.md) | ✅ Concluído |
| Let's Express | [`manuais/integracao-lets-express/`](manuais/integracao-lets-express/integracao-lets-express.md) | ✅ Concluído |
| Foody Delivery | [`manuais/integracao-foody-delivery/`](manuais/integracao-foody-delivery/integracao-foody-delivery.md) | ✅ Concluído |
| Pick n Go! | [`manuais/integracao-pick-n-go/`](manuais/integracao-pick-n-go/integracao-pick-n-go.md) | ✅ Concluído |
| Uai Rango | [`manuais/integracao-uai-rango/`](manuais/integracao-uai-rango/integracao-uai-rango.md) | ✅ Concluído |
| IA ChatGPT no WhatsApp | [`manuais/ia-chatgpt-whatsapp/`](manuais/ia-chatgpt-whatsapp/ia-chatgpt-whatsapp.md) | ✅ Concluído |
| Campanhas SMS (Food Marketing) | [`manuais/campanhas-sms/`](manuais/campanhas-sms/campanhas-sms.md) | ✅ Concluído |
| Cupom de Desconto (campos + cardápio) | [`manuais/cupom-desconto/`](manuais/cupom-desconto/cupom-desconto.md) | ✅ Concluído |
| Cashback — configurar o programa | [`manuais/cashback-configurar/`](manuais/cashback-configurar/cashback-configurar.md) | ✅ Concluído |
| Cashback — operar no dia a dia | [`manuais/cashback-operar/`](manuais/cashback-operar/cashback-operar.md) | ✅ Concluído |
| Desconto e acréscimo nas formas de recebimento (cardápio digital) | [`manuais/cardapio-digital-desconto-formas/`](manuais/cardapio-digital-desconto-formas/cardapio-digital-desconto-formas.md) | ✅ Concluído |
| Taxas das formas de recebimento (faturado e realizado) | [`manuais/taxas-formas-pagamento/`](manuais/taxas-formas-pagamento/taxas-formas-pagamento.md) | ✅ Concluído |
| Ficha técnica (custo do prato e baixa de estoque) | [`manuais/ficha-tecnica/`](manuais/ficha-tecnica/ficha-tecnica.md) | ✅ Concluído |
| Produto só com agendamento (encomenda) | [`manuais/cardapio-digital-agendamento-produto/`](manuais/cardapio-digital-agendamento-produto/cardapio-digital-agendamento-produto.md) | ✅ Concluído |

## Padrão visual das anotações

- Setas e números em **verde** (tom dos botões do sistema), finos e sutis.
- Coordenadas em frações (0..1) — independem da resolução da imagem.
- Regerar imagens tratadas: dentro da pasta do manual, rodar `python annotate.py`.

## Antes de publicar um manual

```bash
python validar-imagens.py            # todos os manuais
python validar-imagens.py caixa      # só um
```

Falha (código 1) se algum manual referenciar imagem que não existe. Avisa também sobre imagem
órfã e sobre divergência entre o manual e o `texto-documentation.ia.md`.

## Requisitos para gerar/anotar imagens

- Python 3.10+ e [Pillow](https://python-pillow.org/) (`pip install pillow`).

---

© BeeFood. Uso interno.
