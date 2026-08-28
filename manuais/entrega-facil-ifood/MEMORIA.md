# MEMORIA.md — #59 Entrega Fácil iFood

## Escopo
Migração do artigo
[Entrega Fácil iFood – Como Solicitar Entregador para pedidos Delivery](https://ajuda.beefood.com.br/baseconhecimento/entrega-facil-ifood-como-solicitar-entregador-para-pedidos-delivery/).
Mesma mentalidade da fila #49–#57: prints do **portal/Gestor iFood** e do
WhatsApp **copiados**; telas em que o BeeFood **mostra o caminho novo**
(Aplicativos, credencial iFood, Delivery, Novo Pedido) recapturadas no tema claro
(Playwright 1440×900 DPR 1.5).

## Origem
Pedido do dono em 28/08/2026. Não estava nos oito itens de
`PLANO-MIGRACAO-AJUDA.md`. Sandbox BeeFood3 (`contato@beefood.com.br`).

## Imagens
| Arquivo | Tipo | O quê |
|---------|------|-------|
| `01-aplicativos-entrega-facil.png` | setas | Aplicativos → card Entrega Fácil iFood |
| `02-modal-entrega-facil.png` | setas | Modal: como habilitar + Delivery + Manual |
| `03-modal-ifood-credenciais.png` | setas | iFood → Credenciais (vazio no sandbox) |
| `03b-ifood-novo-cardapio.png` | setas | Nova Credencial: Merchant ID + SALVAR |
| `04-delivery.png` | setas | Delivery + Novo Pedido (F1) |
| `04b-novo-pedido.png` | setas | Tipo (Retirada/Entrega) + Selecionar entregador |
| `07-portal-ifood-entrega-sob-demanda.png` | contexto | Portal iFood → Entrega Sob Demanda (artigo) |
| `08-portal-ifood-app-beefood.png` | contexto | Portal de Aplicativos → BeeFood Ativo |
| `09-gestor-ifood.png` | contexto | Gestor: via Sob Demanda |
| `10-whatsapp-acompanhamento.png` | contexto | BeeBot: link meupedido.ifood.com.br |

## Decisões
- Windows *Solicitar Entrega Fácil iFood* virou **Selecionar entregador →
  iFood Entrega Fácil** (`ModalAlterarMotorista`).
- Cotação e pagamento **não** foram fotografados: o sandbox **não tem**
  credencial iFood (`Nenhuma credencial configurada`) nem pedido delivery
  aberto. O texto descreve a tela nova (`ModalIfoodEntregaFacil`) lida no
  código — não reaproveitamos print do Windows.
- O checkbox *Incluir frete ao valor do pedido* **não existe** no web; não
  entrou no manual.
- Cancelar: sem lixeira no `VendaDetalhes` para esse serviço. O manual manda
  usar o Gestor e o Histórico de Alterações.
- Merchant ID do 03b: ensaio, **não gravado**.
- Novo Pedido 04b: aberto só para o print; **não salvo**.
- Maps Google: aponta o manual #51 em vez de recapturar a chave.

## Status
Concluído — aguardando publicação do dono.
