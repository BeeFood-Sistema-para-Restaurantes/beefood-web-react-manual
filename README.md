# BeeFood — Manuais e carrosséis

Conteúdo sobre o sistema BeeFood (`https://beefood.app`), produzido a partir do código
do projeto `beefood-web-react` e de capturas de tela reais em produção.

São **duas skills**, cada uma com o seu fluxo, e duas pastas de saída.

| Skill | O que produz | Escreve em |
|-------|--------------|------------|
| [`manual-sistema`](.cursor/skills/manual-sistema/SKILL.md) | manual de uso para o usuário final: passo a passo com setas verdes numeradas | `manuais/` |
| [`carrossel-novidades`](.cursor/skills/carrossel-novidades/SKILL.md) | carrossel de Instagram sobre uma novidade: prints, mockups, PNG 1080×1350 | `carrosseis/` |

A de carrossel **lê** o material da de manual — captura, contas, comportamento já
conferido no sistema — e não escreve nada dentro dela. Cada skill tem a sua memória:
[`MEMORIA-GERAL.md`](.cursor/skills/manual-sistema/references/MEMORIA-GERAL.md) e
[`MEMORIA-CARROSSEIS.md`](.cursor/skills/carrossel-novidades/references/MEMORIA-CARROSSEIS.md).

## Estrutura

```
.
├─ AGENTS.md                   # Qual skill atende qual pedido
├─ spec.md                     # Stack, versões e padrão de pastas
├─ .cursor/skills/
│  ├─ manual-sistema/          # Skill: fazer manual
│  │  ├─ SKILL.md              # O fluxo, em sete passos
│  │  ├─ references/           # MEMORIA-GERAL.md, CHECKLIST-MANUAIS.md e planos/
│  │  └─ scripts/              # validar-imagens.py e indice-manuais.py
│  └─ carrossel-novidades/     # Skill: fazer carrossel
│     ├─ SKILL.md
│     ├─ references/           # MEMORIA-CARROSSEIS.md, mockups, roteiro e copy
│     ├─ scripts/              # pauta, captura, render, empacotamento
│     └─ assets/               # base.css, fotos de produto, mídia de exemplo
├─ manuais/
│  └─ <nome-do-manual>/        # Uma pasta por manual
│     ├─ MEMORIA.md            # Memória detalhada do manual (fluxo, uso, decisões, estado)
│     ├─ <nome>.md             # O manual final (para o usuário)
│     ├─ fluxo-codigo.md       # Mapeamento técnico (a partir do código)
│     ├─ annotate.py           # Script de anotação (setas/números) — Python + Pillow
│     ├─ imagens-puras/        # Screenshots originais (backup, sem edição)
│     └─ imagens-tratadas/     # Screenshots com setas/números (usados no manual)
└─ carrosseis/
   └─ <slug>/                  # Uma pasta por carrossel — índice em carrosseis/README.md
```

## Manuais disponíveis

Gerado das pastas de `manuais/`, com o título lido do H1 de cada manual. Para
atualizar depois de criar um manual:
`python .cursor/skills/manual-sistema/scripts/indice-manuais.py`.
O **status** e a fila ficam no
[`CHECKLIST-MANUAIS.md`](.cursor/skills/manual-sistema/references/CHECKLIST-MANUAIS.md).

<!-- INDICE-MANUAIS:inicio -->

| Manual | Pasta |
|--------|-------|
| App do entregador: receber na porta | [`app-entregador-cobranca/`](manuais/app-entregador-cobranca/app-entregador-cobranca.md) |
| Código de barras: ligar a etiqueta e ler o pedido no aplicativo | [`app-entregador-codigo-barras/`](manuais/app-entregador-codigo-barras/app-entregador-codigo-barras.md) |
| App do entregador: instalar, entrar e ficar disponível | [`app-entregador-entrar/`](manuais/app-entregador-entrar/app-entregador-entrar.md) |
| App do entregador: as entregas do dia e o histórico | [`app-entregador-entregas-do-dia/`](manuais/app-entregador-entregas-do-dia/app-entregador-entregas-do-dia.md) |
| App do entregador: pedido de iFood e de 99Food | [`app-entregador-marketplace/`](manuais/app-entregador-marketplace/app-entregador-marketplace.md) |
| App do entregador: chegar no endereço | [`app-entregador-rota/`](manuais/app-entregador-rota/app-entregador-rota.md) |
| BeeFood Entregador — aplicativo para motoboy | [`app-entregadores/`](manuais/app-entregadores/app-entregadores.md) |
| Manual — App do Garçom (parâmetros) | [`app-garcom-parametros/`](manuais/app-garcom-parametros/app-garcom-parametros.md) |
| Manual da Configuração por Bairro | [`area-entrega-bairro/`](manuais/area-entrega-bairro/area-entrega-bairro.md) |
| Manual da Configuração por CEP Fixo | [`area-entrega-cep-fixo/`](manuais/area-entrega-cep-fixo/area-entrega-cep-fixo.md) |
| Manual da Configuração por KM | [`area-entrega-km/`](manuais/area-entrega-km/area-entrega-km.md) |
| Manual da Configuração por Mapa (Área) | [`area-entrega-mapa/`](manuais/area-entrega-mapa/area-entrega-mapa.md) |
| Ativação da integração Aiqfome V2 no BeeFood | [`ativacao-aiqfome/`](manuais/ativacao-aiqfome/ativacao-aiqfome.md) |
| Autorizar o contador | [`autorizar-contador/`](manuais/autorizar-contador/autorizar-contador.md) |
| Manual — Cadastrar comandas e gerar o QR Code | [`cadastro-comandas/`](manuais/cadastro-comandas/cadastro-comandas.md) |
| Manual — Cadastrar mesas e gerar o QR Code | [`cadastro-mesas/`](manuais/cadastro-mesas/cadastro-mesas.md) |
| Manual do Caixa — Abrir, receber um pagamento e consultar o valor | [`caixa/`](manuais/caixa/caixa.md) |
| Manual do Caixa — Segunda conferência (dupla checagem) | [`caixa-conferencia-2/`](manuais/caixa-conferencia-2/caixa-conferencia-2.md) |
| Manual do Caixa — Fechar o caixa e conferir os valores | [`caixa-fechar/`](manuais/caixa-fechar/caixa-fechar.md) |
| Manual do Caixa — Restrições por grupo de acesso | [`caixa-restricoes/`](manuais/caixa-restricoes/caixa-restricoes.md) |
| Manual — Campanhas Inteligentes | [`campanhas-inteligentes/`](manuais/campanhas-inteligentes/campanhas-inteligentes.md) |
| Manual — Campanhas de SMS | [`campanhas-sms/`](manuais/campanhas-sms/campanhas-sms.md) |
| Campanhas de WhatsApp | [`campanhas-whatsapp/`](manuais/campanhas-whatsapp/campanhas-whatsapp.md) |
| Manual do Cardápio — Açaí | [`cardapio-acai/`](manuais/cardapio-acai/cardapio-acai.md) |
| Agendamento do cardápio digital | [`cardapio-digital-agendamento/`](manuais/cardapio-digital-agendamento/cardapio-digital-agendamento.md) |
| Produto só com agendamento (encomenda) | [`cardapio-digital-agendamento-produto/`](manuais/cardapio-digital-agendamento-produto/cardapio-digital-agendamento-produto.md) |
| Aparência e layout do cardápio digital | [`cardapio-digital-aparencia-layout/`](manuais/cardapio-digital-aparencia-layout/cardapio-digital-aparencia-layout.md) |
| Manual de Avisos do Cardápio Digital | [`cardapio-digital-avisos/`](manuais/cardapio-digital-avisos/cardapio-digital-avisos.md) |
| Manual de Capas e Destaques | [`cardapio-digital-capas-destaques/`](manuais/cardapio-digital-capas-destaques/cardapio-digital-capas-destaques.md) |
| Desconto e acréscimo nas formas de recebimento | [`cardapio-digital-desconto-formas/`](manuais/cardapio-digital-desconto-formas/cardapio-digital-desconto-formas.md) |
| Cardápio digital presencial e QR Code | [`cardapio-digital-presencial-qrcode/`](manuais/cardapio-digital-presencial-qrcode/cardapio-digital-presencial-qrcode.md) |
| Manual do Modo Kiosk — travar o tablet no cardápio | [`cardapio-digital-tablet-modo-kiosk/`](manuais/cardapio-digital-tablet-modo-kiosk/cardapio-digital-tablet-modo-kiosk.md) |
| Manual do Cardápio — Fundamentos | [`cardapio-fundamentos/`](manuais/cardapio-fundamentos/cardapio-fundamentos.md) |
| Manual do Cardápio — Hambúrguer | [`cardapio-hamburguer/`](manuais/cardapio-hamburguer/cardapio-hamburguer.md) |
| Manual do Cardápio — Comida Japonesa | [`cardapio-japonesa/`](manuais/cardapio-japonesa/cardapio-japonesa.md) |
| Cardápio em PDF: como gerar o cardápio impresso do restaurante (A4 ou A5, com foto, QR Code e capa) | [`cardapio-pdf/`](manuais/cardapio-pdf/cardapio-pdf.md) |
| Manual do Cardápio — Pizza | [`cardapio-pizza/`](manuais/cardapio-pizza/cardapio-pizza.md) |
| Cashback — configurar o programa | [`cashback-configurar/`](manuais/cashback-configurar/cashback-configurar.md) |
| Cashback — operar no dia a dia | [`cashback-operar/`](manuais/cashback-operar/cashback-operar.md) |
| Manual — Classificação RFV | [`classificacao-rfv/`](manuais/classificacao-rfv/classificacao-rfv.md) |
| Comissão do garçom: cadastrar e lançar | [`comissao-garcom-cadastrar/`](manuais/comissao-garcom-cadastrar/comissao-garcom-cadastrar.md) |
| Cupom de Desconto — todos os campos e o que o cliente vê | [`cupom-desconto/`](manuais/cupom-desconto/cupom-desconto.md) |
| Como deixar a taxa de serviço opcional no cupom | [`cupom-taxa-servico-opcional/`](manuais/cupom-taxa-servico-opcional/cupom-taxa-servico-opcional.md) |
| Manual — Pagamento automático no Delivery | [`delivery-pagamento-auto/`](manuais/delivery-pagamento-auto/delivery-pagamento-auto.md) |
| Destaque na impressão: como destacar bebidas e produtos no cupom | [`destaque-impressao/`](manuais/destaque-impressao/destaque-impressao.md) |
| Domínio próprio no Cardápio Digital (e verificação na Meta) | [`dominio-proprio/`](manuais/dominio-proprio/dominio-proprio.md) |
| Domínio próprio no cardápio digital: como configurar o seu endereço, alterar a zona DNS e excluir | [`dominio-proprio-configurar/`](manuais/dominio-proprio-configurar/dominio-proprio-configurar.md) |
| Manual do Endereço do Restaurante | [`endereco-restaurante/`](manuais/endereco-restaurante/endereco-restaurante.md) |
| Entrega Fácil iFood — solicitar entregador no Delivery | [`entrega-facil-ifood/`](manuais/entrega-facil-ifood/entrega-facil-ifood.md) |
| Quanto o entregador recebe: taxa, valor, diária e KM | [`entregador-quanto-recebe/`](manuais/entregador-quanto-recebe/entregador-quanto-recebe.md) |
| Exibir e ocultar produtos | [`exibir-ocultar/`](manuais/exibir-ocultar/exibir-ocultar.md) |
| Fechamento Fiscal | [`fechamento-fiscal/`](manuais/fechamento-fiscal/fechamento-fiscal.md) |
| Manual do Fiado — Operar no dia a dia | [`fiado/`](manuais/fiado/fiado.md) |
| Manual do Fiado — Cobrança agrupada | [`fiado-cobranca-agrupada/`](manuais/fiado-cobranca-agrupada/fiado-cobranca-agrupada.md) |
| Manual da Ficha Técnica — o custo do prato | [`ficha-tecnica/`](manuais/ficha-tecnica/ficha-tecnica.md) |
| Manual — Cadastrar forma de recebimento (Delivery, Presencial e PDV) | [`formas-recebimento/`](manuais/formas-recebimento/formas-recebimento.md) |
| Gaveta de dinheiro — configuração pela impressora | [`gaveta-dinheiro/`](manuais/gaveta-dinheiro/gaveta-dinheiro.md) |
| Avisos de WhatsApp da entrega | [`gestao-entregas-avisos-whatsapp/`](manuais/gestao-entregas-avisos-whatsapp/gestao-entregas-avisos-whatsapp.md) |
| Uma entrega do começo ao fim: painel e aplicativo lado a lado | [`gestao-entregas-ciclo-completo/`](manuais/gestao-entregas-ciclo-completo/gestao-entregas-ciclo-completo.md) |
| Despachar a rota e acompanhar no mapa | [`gestao-entregas-despachar/`](manuais/gestao-entregas-despachar/gestao-entregas-despachar.md) |
| Despacho automático: as sete regras | [`gestao-entregas-despacho-automatico/`](manuais/gestao-entregas-despacho-automatico/gestao-entregas-despacho-automatico.md) |
| Fechar a entrega no painel | [`gestao-entregas-fechar-entrega/`](manuais/gestao-entregas-fechar-entrega/gestao-entregas-fechar-entrega.md) |
| Liberar o entregador: cadastro, acesso ao app e código de barras | [`gestao-entregas-liberar-entregador/`](manuais/gestao-entregas-liberar-entregador/gestao-entregas-liberar-entregador.md) |
| Ler o mapa e o painel de entregas | [`gestao-entregas-mapa-painel/`](manuais/gestao-entregas-mapa-painel/gestao-entregas-mapa-painel.md) |
| Montar a rota: agrupar pedidos e escolher o entregador | [`gestao-entregas-montar-rota/`](manuais/gestao-entregas-montar-rota/gestao-entregas-montar-rota.md) |
| Estudo completo dos grupos de acesso | [`grupos-acesso/`](manuais/grupos-acesso/grupos-acesso.md) |
| Manual do Horário de Atendimento | [`horario-atendimento/`](manuais/horario-atendimento/horario-atendimento.md) |
| Inteligência Artificial do ChatGPT no WhatsApp | [`ia-chatgpt-whatsapp/`](manuais/ia-chatgpt-whatsapp/ia-chatgpt-whatsapp.md) |
| BeeFood + 99 Entrega — Guia de integração | [`integracao-99-entrega/`](manuais/integracao-99-entrega/integracao-99-entrega.md) |
| Integração FoodCRM — envie suas vendas automaticamente para o CRM | [`integracao-foodcrm/`](manuais/integracao-foodcrm/integracao-foodcrm.md) |
| Foody Delivery — gestão de entregas e rastreamento de motoboys | [`integracao-foody-delivery/`](manuais/integracao-foody-delivery/integracao-foody-delivery.md) |
| Let's Express — solicitar entregador para Delivery | [`integracao-lets-express/`](manuais/integracao-lets-express/integracao-lets-express.md) |
| Integração Machine — despache entregas pelo BeeFood | [`integracao-machine/`](manuais/integracao-machine/integracao-machine.md) |
| Pick N Go! — cotar e solicitar entregador no Delivery | [`integracao-pick-n-go/`](manuais/integracao-pick-n-go/integracao-pick-n-go.md) |
| Integração Repediu — sincronize vendas e rastreie o cardápio digital | [`integracao-repediu/`](manuais/integracao-repediu/integracao-repediu.md) |
| Ativar integração Uai Rango | [`integracao-uai-rango/`](manuais/integracao-uai-rango/integracao-uai-rango.md) |
| Configurar Uber Direct no BeeFood | [`integracao-uber-direct/`](manuais/integracao-uber-direct/integracao-uber-direct.md) |
| Lançamentos — contas a pagar | [`lancamentos-contas-pagar/`](manuais/lancamentos-contas-pagar/lancamentos-contas-pagar.md) |
| Lançamentos — contas a receber | [`lancamentos-contas-receber/`](manuais/lancamentos-contas-receber/lancamentos-contas-receber.md) |
| Manual de Fechar a Loja Fora do Horário | [`loja-fechar-pausa/`](manuais/loja-fechar-pausa/loja-fechar-pausa.md) |
| Mapas do Google no Cardápio Digital | [`mapas-google/`](manuais/mapas-google/mapas-google.md) |
| Mercado Pago — cartão de crédito no Cardápio Digital | [`mercado-pago/`](manuais/mercado-pago/mercado-pago.md) |
| Manual — Taxa e obrigatoriedades de mesa | [`mesas-taxa-obrigatorias/`](manuais/mesas-taxa-obrigatorias/mesas-taxa-obrigatorias.md) |
| Manual — Entendendo a numeração dos pedidos | [`numeracao-pedidos/`](manuais/numeracao-pedidos/numeracao-pedidos.md) |
| Manual — Parâmetros gerais | [`parametros-geral/`](manuais/parametros-geral/parametros-geral.md) |
| Manual — Balança no PDV | [`pdv-balanca/`](manuais/pdv-balanca/pdv-balanca.md) |
| Manual — Fichas de consumo no PDV | [`pdv-fichas/`](manuais/pdv-fichas/pdv-fichas.md) |
| Manual — Número do pedido e cupom no PDV | [`pdv-numero-cupom/`](manuais/pdv-numero-cupom/pdv-numero-cupom.md) |
| BeeFood Pixel Analytics — ler o funil do cardápio | [`pixel-analytics/`](manuais/pixel-analytics/pixel-analytics.md) |
| Pixel da Meta + API de Conversões — rastreie o cardápio digital | [`pixel-meta-api/`](manuais/pixel-meta-api/pixel-meta-api.md) |
| Pixel da Meta somente — caminho antigo (só o Pixel ID) | [`pixel-meta-somente/`](manuais/pixel-meta-somente/pixel-meta-somente.md) |
| Portal do contador | [`portal-contador/`](manuais/portal-contador/portal-contador.md) |
| Preço programado | [`preco-programado/`](manuais/preco-programado/preco-programado.md) |
| Reforma Tributária (IBS/CBS) — Configurando os campos fiscais do produto | [`reforma-tributaria-ibscbs/`](manuais/reforma-tributaria-ibscbs/reforma-tributaria.md) |
| Relatório de comissão do garçom | [`relatorio-comissao-garcom/`](manuais/relatorio-comissao-garcom/relatorio-comissao-garcom.md) |
| Relatório Operação de Entrega: onde o tempo da entrega se perde | [`relatorio-operacao-entrega/`](manuais/relatorio-operacao-entrega/relatorio-operacao-entrega.md) |
| Relatório de taxa de serviço | [`relatorio-taxa-servico/`](manuais/relatorio-taxa-servico/relatorio-taxa-servico.md) |
| Manual — Segmentação de Clientes | [`segmentacao-clientes/`](manuais/segmentacao-clientes/segmentacao-clientes.md) |
| Manual — Senha do gerente | [`senha-gerente/`](manuais/senha-gerente/senha-gerente.md) |
| Taxas das formas de recebimento (faturado e realizado) | [`taxas-formas-pagamento/`](manuais/taxas-formas-pagamento/taxas-formas-pagamento.md) |
| TEF PayGo (Client PayGo) — instalar no Windows e cadastrar no BeeFood | [`tef-paygo/`](manuais/tef-paygo/tef-paygo.md) |
| TEF Stone (AutoTEF) — configurar no Windows e no BeeFood | [`tef-stone/`](manuais/tef-stone/tef-stone.md) |
| Tradução do cardápio presencial: como traduzir o cardápio do tablet e do totem | [`traducao-cardapio-presencial/`](manuais/traducao-cardapio-presencial/traducao-cardapio-presencial.md) |
| Transferir item entre mesas e comandas | [`transferencia-itens-mesas/`](manuais/transferencia-itens-mesas/transferencia-itens-mesas.md) |
| Criar usuário e montar grupo de acesso | [`usuarios-criar/`](manuais/usuarios-criar/usuarios-criar.md) |
| Venda Sugestiva (UpSell): sugerir produtos no cardápio digital e aumentar o ticket médio | [`venda-sugestiva-upsell/`](manuais/venda-sugestiva-upsell/venda-sugestiva-upsell.md) |
| Manual — Vínculo Marketplace | [`vinculo-marketplace/`](manuais/vinculo-marketplace/vinculo-marketplace.md) |
| Atender no BeeBot | [`whatsapp-atendimento-beebot/`](manuais/whatsapp-atendimento-beebot/whatsapp-atendimento-beebot.md) |
| Conectar o WhatsApp (QR Code) | [`whatsapp-conectar/`](manuais/whatsapp-conectar/whatsapp-conectar.md) |
| Histórico de mensagens do WhatsApp | [`whatsapp-historico/`](manuais/whatsapp-historico/whatsapp-historico.md) |
| Indicadores de WhatsApp e BeeBot | [`whatsapp-indicadores/`](manuais/whatsapp-indicadores/whatsapp-indicadores.md) |
| Notificações de cada etapa do pedido | [`whatsapp-notificacoes/`](manuais/whatsapp-notificacoes/whatsapp-notificacoes.md) |
| Pedidos pelo chat no WhatsApp | [`whatsapp-pedidos-chat/`](manuais/whatsapp-pedidos-chat/whatsapp-pedidos-chat.md) |
| Respostas automáticas no WhatsApp | [`whatsapp-respostas/`](manuais/whatsapp-respostas/whatsapp-respostas.md) |
| Resumo diário e semanal no WhatsApp | [`whatsapp-resumo-diario/`](manuais/whatsapp-resumo-diario/whatsapp-resumo-diario.md) |

<!-- INDICE-MANUAIS:fim -->

## Padrão visual das anotações

- Setas e números em **verde** (tom dos botões do sistema), finos e sutis.
- Coordenadas em frações (0..1) — independem da resolução da imagem.
- Regerar imagens tratadas: dentro da pasta do manual, rodar `python annotate.py`.

## Antes de publicar um manual

```bash
SK=.cursor/skills/manual-sistema/scripts

python $SK/validar-imagens.py           # todos os manuais
python $SK/validar-imagens.py caixa     # só um
python $SK/indice-manuais.py            # atualiza o índice acima
```

O `validar-imagens.py` falha (código 1) se algum manual referenciar imagem que não existe. Avisa
também sobre imagem órfã e sobre divergência entre o manual e o `texto-documentation.ia.md`.
O `indice-manuais.py` reescreve a tabela de manuais deste arquivo a partir das pastas.

## Requisitos para gerar/anotar imagens

- Python 3.10+ e [Pillow](https://python-pillow.org/) (`pip install pillow`).

---

© BeeFood. Uso interno.
