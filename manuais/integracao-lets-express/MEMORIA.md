# MEMORIA.md — #60 Integração Let's Express

## Escopo
Migração do artigo
[Let's Express – Como solicitar cotação e entregador para Delivery](https://ajuda.beefood.com.br/baseconhecimento/lets-express-como-solicitar-cotacao-e-entregador-para-delivery/).
Mesma mentalidade da fila #49–#56 e dos #57/#58: **não** reusar print do
BeeFood Windows; capturar a **tela nova** no web (tema claro, Playwright
1440×900 DPR 1.5).

## Origem
Pedido do dono em 28/08/2026. Não estava nos oito itens de
`PLANO-MIGRACAO-AJUDA.md`. Sandbox BeeFood3 (`contato@beefood.com.br`).

## Imagens
| Arquivo | Tipo | O quê |
|---------|------|-------|
| `01-aplicativos-lets-express.png` | setas | Aplicativos → Entrega → card Lets Express |
| `02-modal-credenciais.png` | setas | Api Key, Empresa ID, SALVAR E SAIR (F2) |
| `03-modal-sincronizacao.png` | setas | PREPARO + minutos + origens |
| `04-adicionar-entregador.png` | setas | Detalhe do pedido → Adicionar Entregador |
| `05-modal-entregador.png` | setas | Entrega Terceirizada → Lets Express |
| `06-modal-solicitar.png` | setas | Forma de pagamento, retorno, CONFIRMAR |

## Decisões
- Cotação: o artigo antigo já marcava *(Em manutenção)*. No web,
  `SERVICOS_COM_COTACAO` **não** inclui Let's Express (só iFood Entrega Fácil,
  Pick n Go, 99 Entrega e Uber Direct). O manual diz que não há cotação.
- Caminho Windows *Aplicativos → Delivery Entrega* virou
  **Aplicativos → Entrega → Lets Express**.
- Feature nova documentada: filtro **Origens da sincronização automática**.
- Prints do Windows (config, botão Solicitar, histórico, cancelar) **não**
  migrados.
- Sem pedido delivery aberto no kanban. O despacho foi ensaiado no
  **Histórico de Vendas**, venda **#865** (Delivery / AIQFome, já ENTREGUE).
  **CONFIRMAR não foi clicado** — a Let's Express real não recebeu pedido.
- Credencial dummy (`sua-api-key-lets-express` / `12345`) foi gravada só
  para o card ficar *ativo* no modal de entregador; **restaurada** no fim
  (`api_key` e `empresa_id` de volta a `null`, sync manual). GET
  `/api/empresa2/letsexpress/38311/88711` confirmou.
- Nome, telefone e endereço do cliente na pura 04–06 cobertos com blur
  (repositório público).
- Sem print de cancelamento: não havia pedido *Entregue por Lets Express*.
  O texto descreve a lixeira da seção Entregador.

## Status
Concluído — aguardando publicação do dono.
