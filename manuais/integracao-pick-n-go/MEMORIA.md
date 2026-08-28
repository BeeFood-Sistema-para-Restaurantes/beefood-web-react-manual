# MEMORIA.md — #62 Pick n Go! (cotação e entregador)

## Escopo
Migração do artigo [Pick N Go! – Como solicitar cotação e entregador para Delivery](https://ajuda.beefood.com.br/baseconhecimento/pick-n-go-como-solicitar-cotacao-e-entregador-para-delivery/).
Mesma mentalidade da fila #49–#57: **não** reusar print do BeeFood Windows; capturar a **tela nova**
em que se cola App ID / App Key (Playwright, tema claro, 1440×900, DPR 1.5).

## Origem
Pedido do dono em 28/08/2026. Não estava nos oito itens de `PLANO-MIGRACAO-AJUDA.md`.
Sandbox BeeFood3 (`contato@beefood.com.br`).

## Imagens
| Arquivo | Tipo | O quê |
|---------|------|-------|
| `01-aplicativos-pick-n-go.png` | setas | Aplicativos → Entrega → card **Pick N Go!** |
| `02-modal-credenciais.png` | setas | Modal: App ID, App Key, sync **manual**, SALVAR E SAIR |
| `03-modal-origens.png` | setas | Sync **PREPARO** + origens (Todas desligado, checkboxes visíveis) |

## Decisões
- Artigo antigo = Windows (botão no rodapé, duas janelas de cotação/pagamento). Web = card em
  Aplicativos + **Adicionar Entregador** + um modal de cotação.
- Recursos **novos** que o artigo não tinha: filtro de **origens** e switch **Frota própria**.
- Cotação / vínculo / cancelar: descritos pelo código (`ModalPickNGoCotacao`, `VendaDetalhes`).
  Sandbox **sem** App ID/App Key; Delivery vazio no momento da captura. Não gravei credencial
  fictícia e não reciclei print Windows.
- WhatsApp (link de acompanhamento) e entregador **Pick n Go!** mantidos do artigo antigo —
  comportamento de produto, não inventado.
- Pré-requisito Google Maps aponta para o #51, sem repetir o tutorial da chave.
- Ensaio do Passo 3: radio PREPARO + desligar *Todas as origens* só para o print; **FECHAR** sem salvar.

## Status
Concluído — aguardando publicação do dono.
