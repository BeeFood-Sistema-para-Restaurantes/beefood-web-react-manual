# Fluxo de código — Configuração por mapa

> Manual **#35**. Fonte: `beefood-web-react` + `beetech-server-node-2.0`, 21/08/2026.

| Item | Valor |
|------|-------|
| Flag | `tipoEntregaMapa` |
| UI | `ConfigRaioArea.tsx` (Leaflet: círculo e polígono) |
| Hook | `useAreaEntregaMapa.ts` |
| GET/POST/DELETE | `/api/empresaDelivery2/cardapioDigital/areaAtendimento/mapa` |

Campos da região: nome, cor, ativo, `naoEntrega` (switch **Não entrega nessa região**),
taxa, frete grátis, tempo adicional, valor do entregador, geometria círculo (centro + raio)
ou polígono (vértices).

O cardápio (`cacheBeeShop`) usa o ponto geocodificado do CEP+número do cliente e testa
inclusão nas áreas ativas. Fora de todas: *Endereço fora da área de atendimento*.
