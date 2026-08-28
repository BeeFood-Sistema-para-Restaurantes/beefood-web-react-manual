# MEMORIA.md — #59 Entrega Fácil iFood

## Escopo
Migração do artigo
[Entrega Fácil iFood – Como Solicitar Entregador para pedidos Delivery](https://ajuda.beefood.com.br/baseconhecimento/entrega-facil-ifood-como-solicitar-entregador-para-pedidos-delivery/).
Mesma mentalidade da fila #49–#57: prints do **portal/Gestor iFood** e do
WhatsApp **copiados**; telas em que o BeeFood **mostra o caminho novo**
recapturadas no tema claro (Playwright 1440×900 DPR 1.5).

## Origem
Pedido do dono em 28/08/2026. Não estava nos oito itens de
`PLANO-MIGRACAO-AJUDA.md`. Sandbox BeeFood3 (`contato@beefood.com.br`).
Ajuste no mesmo dia: iFood ativado na loja; fluxo operacional é **criar
pedido → detalhes → Adicionar Entregador → lista** (não o Novo Pedido).
Cotação **não** foi clicada — o dono pediu para não testar agora.

## Imagens
| Arquivo | Tipo | O quê |
|---------|------|-------|
| `01-aplicativos-entrega-facil.png` | setas | Aplicativos → card Entrega Fácil iFood |
| `02-modal-entrega-facil.png` | setas | Modal: como habilitar + Delivery + Manual |
| `03-modal-ifood-credenciais.png` | setas | iFood → Credenciais (Merchant ID **Ativo**) |
| `03b-ifood-novo-cardapio.png` | setas | Nova Credencial: Merchant ID + SALVAR |
| `04-delivery.png` | setas | Delivery com pedido no quadro |
| `04b-detalhes-pedido.png` | setas | Detalhes → **Adicionar Entregador** |
| `05-lista-entregadores.png` | setas | Modal Alterar Entregador → iFood Entrega Fácil |
| `07-portal-ifood-entrega-sob-demanda.png` | contexto | Portal iFood → Entrega Sob Demanda (artigo) |
| `08-portal-ifood-app-beefood.png` | contexto | Portal de Aplicativos → BeeFood Ativo |
| `09-gestor-ifood.png` | contexto | Gestor: via Sob Demanda |
| `10-whatsapp-acompanhamento.png` | contexto | BeeBot: link meupedido.ifood.com.br |

## Decisões
- Windows *Solicitar Entrega Fácil iFood* virou **detalhes do pedido →
  Adicionar Entregador → iFood Entrega Fácil** (`ModalAlterarMotorista`).
- Cotação e pagamento **não** foram fotografados: o dono pediu para **não
  clicar** no iFood da lista (cotação de teste indisponível). O texto descreve
  a tela nova (`ModalIfoodEntregaFacil`) lida no código.
- O checkbox *Incluir frete ao valor do pedido* **não existe** no web; não
  entrou no manual.
- Cancelar: sem lixeira no `VendaDetalhes` para esse serviço. O manual manda
  usar o Gestor e o Histórico de Alterações.
- Merchant ID do 03b: ensaio, **não gravado**.
- Prints 04/04b/05: pedido #17 (manual, em Preparo). Dado pessoal (nome,
  telefone, endereço) coberto na imagem **pura**.
- Cache `entrega_cache` no sandbox atrasou o `entregaIfoodAtiva`; depois de
  limpar, o iFood Entrega Fácil saiu **sem** *Não configurado*.

## Status
Concluído — aguardando publicação do dono.
