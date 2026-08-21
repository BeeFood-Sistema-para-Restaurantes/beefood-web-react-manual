# Fluxo de código — Endereço do restaurante

> Mapeamento técnico do que o manual **#34 Configurar endereço do restaurante** documenta.
> Fonte: `beefood-web-react` e `beetech-server-node-2.0`, somente leitura. Levantado em
> 21/08/2026, versão **v3.200826.2051** em produção.

Os quatro tipos (mapa, KM, bairro, CEP Fixo) estão nos `fluxo-codigo.md` dos manuais #35–#38.

---

## 1. Onde fica

| Item | Valor |
|------|-------|
| Página | `src/pages/CardapioDigital.tsx` |
| Rota | `/cardapio-digital?tab=areaEntrega` |
| Aba | `src/components/cardapio-digital/AreaEntregaTab.tsx` |
| Passo 1 | `AreaEntregaStep1.tsx` (Google Maps + modal Confirmar Endereço) |
| Passo 2 | `AreaEntregaStep2.tsx` (quatro cards) |
| Passo 3 | `AreaEntregaStep3.tsx` (delega para Config*) |
| Hook | `src/hooks/useAreaEntregaConfig.ts` |
| Mobile | `src/components/mobile/cardapio-digital/MobileAreaEntregaTab.tsx` |

Se a filial já tem `latitude`/`longitude`, o assistente **abre no passo 3**.

---

## 2. Tipos e flags

O front usa o union `km | raio | bairro | cep` e grava quatro booleanos (só um verdadeiro):

| Card na tela | Tipo | Flag |
|--------------|------|------|
| Quilometragem KM | `km` | `tipoEntregaKM` |
| Raio/Área | `raio` | `tipoEntregaMapa` |
| Bairro e CEP | `bairro` | `tipoEntregaCep` |
| CEP Único | `cep` | `tipoEntregaCepFixo` |

Trocar o tipo **não apaga** as faixas/áreas/grupos dos outros.

---

## 3. Endpoints

| Ação | Método | Caminho |
|------|--------|---------|
| Ler config | GET | `/api/empresaDelivery2/cardapioDigital/areaAtendimento/config/{empresa}/{filial}/{usuario}` |
| Salvar endereço | POST | `.../areaAtendimento/configEndereco` |
| Salvar tipo | POST | `.../areaAtendimento/configTipoEntrega` |

O passo 1 também persiste `fusoHorarioID` (lista de fusos vem no GET).

---

## 4. Modal Confirmar Endereço

Aberto ao escolher uma sugestão do Places ou ao avançar sem número. Campo `número` é
obrigatório no front. Complemento é opcional.

---

## 5. Cache do cardápio digital

O BeeShop lê a filial de um cache (`cacheBeeShop.js`). Mudança de tipo/endereço **não é
instantânea** no `menu.beefood.com.br` — o manual fala 1 a 2 minutos, alinhado ao que o
dono pediu e ao TTL observado no backend (faixa de minutos, não segundos).
