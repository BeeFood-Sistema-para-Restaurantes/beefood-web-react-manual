# fluxo-codigo.md — #58 Pick n Go! (uso interno, NÃO publicar)

Fonte antiga: [Pick N Go! – Como solicitar cotação e entregador](https://ajuda.beefood.com.br/baseconhecimento/pick-n-go-como-solicitar-cotacao-e-entregador-para-delivery/) (Windows). Tela nova = painel web.

## Front (`~/refs/beefood-web-react`)

- Card **Aplicativos → Entrega → Pick N Go!** (`app.id === 'pickngo'`) em `src/data/appCategories.ts`.
- Modal de config: `src/components/aplicativos/PickngoModal.tsx`.
  - Campos: `appId`, `appKey`, radios `manual` / `auto_preparo` / `auto_entrega`, `frota`, `origens`.
  - Origens (só se automático): `ORIGENS_AGILIZONE` em `src/hooks/useAgilizone.ts` — IFOOD, 99FOOD, KEETA, AIQFOME, RAPPI, DELIVERYMUCH, UAIRANGO, CARDAPIO_MANUAL.
  - Grava com **SALVAR E SAIR (F2)** via `usePickngo` → `POST /api/empresa2/pickngo`.
  - Lê `GET /api/empresa2/pickngo/{empresaID}/{usuarioID}`.
  - Botão AJUDA ainda aponta para o artigo antigo do ajuda.beefood (destino desta migração).
- Mobile: `MobilePickngoPage.tsx` — **não documentar** (manuais são desktop).
- Serviço: `src/services/entrega/pickngo.ts`
  - Cotação `POST /api/entrega2/png/cotacao/{empresa}/{filial}/{usuario}/{preVendaID}`
  - Formas `GET /api/entrega2/png/formasPagamento/{empresa}/{filial}/{usuario}`
  - Pedido `POST /api/entrega2/png/pedido` (`formaPagamentoID` opcional)
  - Cancelar `POST /api/entrega2/png/pedidoCancelar/{empresa}/{filial}/{usuario}/{preVendaID}`
- Modal de cotação: `src/components/ModalPickNGoCotacao.tsx`
  - Com cotação: taxa cobrada, taxa entregador, distância km, **Confirmar Entrega**
  - Sem cotação (frota): só forma de pagamento + **Enviar para Pick n Go**
  - Pré-seleção: `resolverFormaPagamentoIDPickNGo` (`src/utils/pickngoFormaPagamento.ts`)
- Lista de serviços: `ModalAlterarMotorista` — id `ENTREGA_TERCEIRIZADA_IDS.PICK_N_GO` (`-3`).
  - Ativo se `credenciaisEntrega.entregaPickNGoAtiva` (`GET /api/entregas/credencialAtiva/...`).
  - Pré-cotação paralela com iFood Entrega Fácil e 99 Entrega (`useCotacoesEntregaParalelas`).
  - Frota terceirizada: um pedido por vez; frota (`frota === 1`) permite vários.
- Delivery: `src/pages/Delivery.tsx` (`handlePickNGoClick` / `handlePickNGoConfirm`).
- Detalhes: `VendaDetalhes.tsx` — *Entregue por Pick n Go!*, lixeira *Cancelar entrega Pick n Go!*.
- Histórico: `ModalHistoricoAlteracoes` na tela de Delivery.

## O que mudou em relação ao Windows

| Artigo antigo | Web novo |
|---------------|----------|
| Menu Aplicativos → Delivery Entrega → Pick N Go! | **Aplicativos → Entrega → Pick N Go!** |
| Botão *Solicitar Entrega Pick N Go!* no rodapé do pedido | **Adicionar Entregador** → card **Pick n Go!** |
| Cotação e pagamento em duas janelas (CONTINUAR > / CONFIRMAR) | Um modal: cotação + forma + **Confirmar Entrega** |
| Sem filtro de origem | **Origens da sincronização automática** |
| Sem frota própria na tela antiga | Switch **Frota própria** (pula cotação) |
| Cancelar no rodapé | Lixeira na guia **Entregador** |

## Sandbox (28/08/2026)

- BeeFood3: modal abre vazio (`appId`/`appKey` sem valor). **Não gravei** credencial fictícia.
- Delivery sem pedidos abertos; cotação real exige App ID/App Key válidos da Pick n Go!.
- Prints de operação (cotação, vínculo, cancelar) ficaram em texto — sem inventar tela.
