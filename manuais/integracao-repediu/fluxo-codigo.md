# fluxo-codigo.md — Integração Repediu (uso interno, NÃO publicar)

> Mapeamento técnico a partir do código `beefood-web-react` e do comportamento observado em produção.
> **Não publicar** este arquivo no manual do usuário.

## 1. Onde fica no app

- Menu **Aplicativos** (`src/pages/Aplicativos.tsx`) → seção **Marketing e CRM** → card **Repediu**
  (`src/data/appCategories.ts`).
- Componentes (versão do checkout local):
  - `src/components/apps/RepediuModal.tsx` — lista os cardápios/filiais e o status; botão **Configurar**.
  - `src/components/apps/RepediuConfigModal.tsx` — formulário de credenciais (SALVAR F2 / CANCELAR ESC).
  - `src/hooks/useRepediu.ts` — busca e salva as configs via API.
  - Mobile: `src/components/mobile/aplicativos/MobileRepediuPage.tsx` e `MobileRepediuConfig.tsx`.

## 2. API (DataSnap / empresa2)

Via `createApiUrl(...)` + `getAuthenticatedHeaders()` (header extra `ngrok-skip-browser-warning: true`).

### Buscar configurações
```
GET /api/empresa2/repediu/{empresaID}/{usuarioID}
→ RepediuConfig[]   (corpo vazio = sem configs)
```

### Salvar / atualizar
```
POST /api/empresa2/repediu
body: {
  empresaID, filialID, usuarioID, usuario,
  nomeFantasia, clientId, clientSecret
  // update: inclui `id` e `log` (dados originais para auditoria)
}
```

### Tipo `RepediuConfig` (local)
```ts
interface RepediuConfig {
  id: number | null;
  empresaID: number;
  filialID: number | null;   // config por cardápio/filial
  clientId: string | number | null;
  clientSecret: string | null;
  ultima: string | null;     // última sincronização
  historico: string | null;
}
```

## 3. Regras de UI observadas

- **Por cardápio/filial:** a configuração é feita para cada cardápio digital (chave `filialID`).
- **Tracker de Vendas** (Client ID + Client Secret): validação exige **os dois** preenchidos ou **ambos
  em branco** (no local, `isValid = clientId && clientSecret`).
- **Client Secret** tem toggle de visibilidade (ícone de olho — `Eye`/`EyeOff`).
- Atalhos: **F2** salva, **ESC** fecha.
- Status no card: local usa "Configurado / Não configurado"; **produção** usa
  "**Tracker de Vendas ativo/inativo**" e "**Tracker de Cardápio Digital ativo**".

## 4. Divergência local × produção (IMPORTANTE)

O checkout local está **atrás** da produção:
- **Local:** `RepediuConfigModal.tsx` só tem **Client ID / Client Secret** (tracker de vendas).
- **Produção (24/07/2026):** o formulário **Configurar Repediu** tem **dois trackers**:
  - **Tracker de Vendas** → Client ID + Client Secret.
  - **Tracker de Cardápio Digital** → **Chave do tracker (Write Key)** (independente).
  - Status por cardápio: "Tracker de Vendas ativo/inativo" + "Tracker de Cardápio Digital ativo".

A **Write Key** vem do módulo **Web/App Analytics → Configuração** do Repediu (SDK de rastreamento),
diferente do Client ID/Secret (que vem de **Integrações → Fontes de dados**).

## 5. Onde as credenciais são geradas (Repediu)

| Credencial | Caminho no Repediu | URL |
|------------|--------------------|-----|
| Client ID / Client Secret | Integrações → Fontes de dados → card BeeFood → **Habilitado** | `app.repediu.com.br/integrations` |
| Write Key | Web/App Analytics → Configuração → card BeeFood → **Habilitar** → **Gerar chave** | `app.repediu.com.br/analytics/config` |

## 6. Pendência do projeto (regra do dono)
Ainda **não existe `spec.md`** em `beefood-web-react` (a regra pede criar) — pendente, fora do escopo deste manual.
