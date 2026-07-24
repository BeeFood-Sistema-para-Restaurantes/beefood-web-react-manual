# fluxo-codigo.md — Integração FoodCRM (uso interno, NÃO publicar)

## 1. Onde fica no app

- Menu **Aplicativos** (`src/pages/Aplicativos.tsx`) → seção **Marketing e CRM** → card **FoodCRM**
  (`src/data/appCategories.ts`, id `foodcrm`, `isNew: true`, descrição "CRM para restaurantes").
- Ao clicar no card (`app.id === 'foodcrm'`), abre `FoodCrmModal` (state `foodCrmModalOpen`).
- Componentes (desktop):
  - `src/components/apps/FoodCrmModal.tsx` — lista os cardápios/filiais com status e botões **Adicionar / Editar / Excluir**.
  - `src/components/apps/FoodCrmConfigModal.tsx` — formulário de credencial (campo **API key** + switch **Ativo**; SALVAR F2 / CANCELAR ESC).
  - `src/hooks/useFoodCrm.ts` — busca, salva e exclui as credenciais via API.
- Componentes (mobile): `src/components/mobile/aplicativos/MobileFoodCrmPage.tsx` e `MobileFoodCrmConfig.tsx`.
- Ícone: `src/assets/apps/foodcrm.png.asset.json`.

## 2. Dados / API (hook `useFoodCrm.ts`)

Tipo `FoodCrmConfig`: `{ id, empresaID, filialID, api_key, ativo, historico, dataProcessamento }`.

- **GET** `/api/empresa2/foodcrm/{empresaID}/{usuarioID}` → lista de `FoodCrmConfig` (uma por cardápio/filial).
- **POST** `/api/empresa2/foodcrm` → cria/atualiza. Body: `{ empresaID, usuarioID, api_key, ativo }`
  - criação: inclui `filialID`.
  - edição: inclui `id`, `usuario` e `log` (valores anteriores).
- **DELETE** `/api/empresa2/foodcrm` → body `{ id, empresaID, usuarioID, usuario }`.
- `maskApiKey()` mascara a chave para exibição (mantém `fcrm_<parte>_••••••`).

A lista de cardápios (filiais) vem de `usePixOnlineConfig` (`pixConfig.cardapios`); o modal cruza cada
cardápio com a `FoodCrmConfig` correspondente por `filialID`.

## 3. Regras de UI observadas

- **API key** é obrigatória para habilitar **SALVAR** (`isValid = apiKey.trim().length > 0`).
- Placeholder e texto de ajuda indicam o formato **`fcrm_...`** e que a chave é gerada no FoodCRM → Integrações.
- Switch **Ativo** (default ligado) controla se os pedidos são enviados.
- Status por cardápio: **Ativo** / **Inativo** (configurado mas desligado) / **Não configurado**.
- Exibe `dataProcessamento` como "Última sincronização" quando presente.

## 4. Lado FoodCRM (app.foodcrm.com.br)

- **Integrações** (`/integrations`) → botão **"Acessar a documentação"** abre um **drawer lateral direito**
  "API de integração" com: **Código da loja** (uuid), **API Key / Token** (`fcrm_...`), **Gerar novo token**,
  **Ver documentação da API**.
- A chave `fcrm_...` desse painel é a que vai no campo **API key** do BeeFood. **Código da loja não é usado no BeeFood.**
- Existe também um **card "BeeFood"** na mesma página que abre outro drawer (Webhook + Código da loja +
  Token/Apikey + Url do cardápio + Salvar). É um **caminho alternativo/reverso** (registro de webhook no
  FoodCRM) e **não** faz parte do fluxo documentado no manual do usuário.
- A conta usada nos testes tem **tema claro** disponível ("Toggle color mode") — o manual foi capturado em tema claro.

## 5. Natureza da integração

- BeeFood → FoodCRM: **envio de vendas em lote, diário (madrugada)**. Não é tempo real.
- Autenticação por **API Key / Token** (`fcrm_...`), por cardápio/filial.

## 6. Credenciais de teste usadas (sandbox)

- FoodCRM: `beefood@foodcrm.com.br` / `Beefood@0501` — conta "BeeFood Teste".
  - API Key / Token de teste: `fcrm_3bd2e0c3_Eb6H5KdG_SgbWAvBTB2g-wgX5Rfnh1aC`
  - Código da loja de teste: `cb0484ad-0432-4981-976f-a1a920ed723c`
- BeeFood: sandbox "BeeFood3 - Manual" (login do manual). Cardápio configurado e **salvo de verdade** (Ativo).
