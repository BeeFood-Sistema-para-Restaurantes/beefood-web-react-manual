# fluxo-codigo.md — Integração Uber Direct (uso interno, NÃO publicar)

## 1. Onde fica no app (BeeFood)

- Menu **Aplicativos** (`src/pages/Aplicativos.tsx`) → seção **Entrega** → card **Uber Direct**
  (`src/data/appCategories.ts`, id `uber-direct`, ícone `src/assets/apps/uberdirect.png`,
  descrição "Solicite entregadores").
- **Atenção (estado do código no `git pull` de 04/08/2026):** o card ainda está marcado como
  `disabled: true, badge: 'Em breve!'` em `appCategories.ts`. Ou seja, na versão pública ainda pode não
  estar liberado para clique — a liberação depende de release/flag. O **fluxo de credenciais já existe**
  no backend/estrutura (ver abaixo).
- Flag de credencial ativa: `entregaUberDirectAtiva` em `src/hooks/useCredenciaisEntrega.ts`
  (interface `CredenciaisEntrega`), populada por `GET /api/entregas/credencialAtiva/{empresaID}/{filialID}/{usuarioID}/1`.

## 2. Credenciais (o que o usuário cola no BeeFood)

Três valores, obtidos no painel Uber Direct em **Desenvolvedor → Chaves de API**:

| Campo no BeeFood | Origem no Uber Direct |
|------------------|-----------------------|
| **Customer ID**  | ID do usuário |
| **Client ID**    | ID de cliente do desenvolvedor |
| **Client Secret**| Client Secret (usar "Mostrar" antes de copiar) |

Fluxo: colar os 3 campos em **Aplicativos → Entregas → Uber Direct** → **Salvar** → **Testar conexão**.

## 3. Webhook (notificações de entrega)

- Endpoint a cadastrar no painel Uber (Desenvolvedor → Webhooks → Criar webhook):
  **`https://entregas.beefoodapi.be/api/uberDirect/webhook`**
- Evento: **event.delivery_status** (status da entrega: entregador saiu / a caminho / entregue).
- É o que permite o BeeFood acompanhar o status em tempo real.

## 4. Modelo de negócio

- **Cada loja tem a própria conta Uber + Uber Direct + cartão.** Não compartilhar entre filiais.
- Pagamento das corridas é cobrado **pela Uber, direto no cartão** cadastrado. O BeeFood **não** cobra
  as entregas (diferente de modelos com cobrança centralizada por parceiro).
- Cadastro feito no site da Uber: **https://direct.uber.com/accounts** (conta pessoal Uber → conta
  Uber Direct do restaurante → cartão → webhook → chaves de API).

## 5. Origem do conteúdo

- Importado de `C:\projetos\beefood3-server-entregas\docs\uber-direct`.
- Existiam **dois** arquivos de texto prontos:
  - `onboarding-uber-direct.md` — versão MDX (com `<Steps>`, `<Callout>`), rótulos "Faturação / Programador / Gestão / Chaves API".
  - `onboarding-uber-direct-preview.md` — versão **plain markdown**, rótulos "Pagamento / Desenvolvedor / Gerenciamento / Chaves de API".
- Para o repositório foi usada a **versão preview (plain markdown)**, por ser a que casa com o padrão dos
  outros manuais (### + tabelas + `>` para callouts), ajustando apenas os caminhos de imagem
  (`imagens/` → `imagens-tratadas/`). Nenhum texto foi reinterpretado.

## 6. Imagens

21 imagens no fonte (`uber-direct-00`..`20`, sem `19`). O manual usa 20 (todas exceto a inexistente 19).
Já vinham prontas (com destaques) — apenas copiadas para `imagens-puras/` (backup) e `imagens-tratadas/`
(fonte única usada no manual).
