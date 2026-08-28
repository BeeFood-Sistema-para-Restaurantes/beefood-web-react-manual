# MEMORIA.md — #58 Foody Delivery (gestão de entregas e rastreamento)

## Escopo
Migração do artigo [Foody Delivery – Gestão de Entregas e Rastreamento de Motoboys](https://ajuda.beefood.com.br/baseconhecimento/foody-delivery-gestao-de-entregas-e-rastreamento-de-motoboys/).
Mesma mentalidade da fila #49–#56 e do #57: prints do **painel Foody** e do WhatsApp
**copiados** para o repo; tela em que o BeeFood **salva** (Token / Token Webhook /
sincronização / origens) com print **novo** (tema claro, Playwright 1440×900 DPR 1.5).

## Origem
Pedido do dono em 28/08/2026. Não estava nos oito itens da fila `PLANO-MIGRACAO-AJUDA.md`.
Sandbox BeeFood3 (`contato@beefood.com.br`).

## Imagens
| Arquivo | Tipo | O quê |
|---------|------|-------|
| `01-foody-menu-apis.png` | contexto | Foody: Minha Conta → APIs e Hooks (artigo 2024) |
| `02-foody-criar-token.png` | contexto | Foody: Criar credencial API |
| `03-foody-criar-webhook.png` | contexto | Foody: Criar gatilho + URL do webhook |
| `04-aplicativos-foody.png` | setas | Aplicativos (1) → card Foody Delivery (2) |
| `05-modal-foody-config.png` | setas | Token, Token Webhook, sync manual, Salvar |
| `06-modal-foody-origens.png` | setas | PREPARO + origens (recurso novo, não existia no artigo) |
| `07-whatsapp-acompanhamento.png` | contexto | WhatsApp com link `app.foodydelivery.com/trk/...` |

## Decisões
- Caminho Windows (*Aplicativos → Delivery Entrega → Foody Delivery*) virou
  **Aplicativos → Entrega → Foody Delivery**.
- URL do webhook: o texto antigo tinha `.../datasnap/rest/entrega/fd/webhook`; o
  print oficial (e o que entra no manual) é `https://app.beetechapi.be/api/entrega/fd/webhook`.
- Recurso novo documentado: filtro **Origens da sincronização automática**
  (changelog do web: Machine, Foody, Lets Express, Pick n Go e Agilizone).
- Tokens no print do modal são os **exemplos públicos** do artigo antigo, preenchidos
  só para o screenshot. **Não foram gravados** no sandbox (FECHAR / ESC).
- Delivery do sandbox estava vazio e o histórico de vendas Delivery tem dado
  pessoal (nome/telefone). Não recapturamos despacho/cancelar para não vazar PII
  nem disparar Foody de verdade. O dia a dia ficou em texto, alinhado ao web
  (`Adicionar Entregador` → Entrega Terceirizada → Foody; lixeira para cancelar;
  Histórico de Alterações).
- Prints Windows de sincronizar/cancelar/histórico **não** migraram.

## Status
Concluído — aguardando publicação do dono.
