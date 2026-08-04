# MEMORIA.md — Integração Uber Direct

## Escopo
Manual do usuário final ensinando a **configurar o Uber Direct no BeeFood**: criar/entrar na conta Uber,
cadastrar o restaurante no Uber Direct, cadastrar o cartão, configurar o webhook, **copiar a Chave de
autenticação do webhook** e as credenciais (**ID do usuário / ID de cliente / Client Secret**), e colar
tudo em **Aplicativos → Entregas → Uber Direct**.

## Origem
- Importado de `C:\projetos\beefood3-server-entregas\docs\uber-direct`.
- **Texto e imagens já vinham prontos** — instrução do dono: apenas **copiar e organizar no padrão**,
  **sem reinterpretar** (igual ao #8 99 Entrega).
- Havia dois `.md`: `onboarding-uber-direct.md` (MDX com Steps/Callout) e
  `onboarding-uber-direct-preview.md` (plain markdown). Usei o **preview** como `integracao-uber-direct.md`.
  Único ajuste: caminhos `imagens/` → `imagens-tratadas/`.

## Histórico de importação
- **04/08/2026 (1ª versão):** 20 imagens (`00`..`18` + `20`), 9 passos.
- **04/08/2026 (reimport — "faça o merge novamente"):** fonte atualizada. Agora:
  - **10 passos** — novo **passo 8: copiar a Chave de autenticação do webhook** (3 pontinhos → Editar → Copiar).
  - Conjunto de imagens virou **`01`..`21`** (removida a `00`; novas `19` e `21`; várias reexportadas).
  - Surgiram docs de API no fonte (`api-conta/credencial/entrega/webhook.md`, `README.md`,
    `schema-add-marketplace-ids.sql`) — consolidadas no `fluxo-codigo.md`.
  - Refiz imagens (limpei puras+tratadas e recopiei), reescrevi o manual, o `texto-documentation.ia.md`
    (21 imagens) e o `fluxo-codigo.md`.

## Estrutura
- `integracao-uber-direct.md` — manual (conteúdo do preview, verbatim; só caminhos de imagem ajustados).
- `fluxo-codigo.md` — técnico/uso interno (rotas, tabelas, OAuth, webhook HMAC + signing key, modelo de negócio).
- `texto-documentation.ia.md` — prompt (lista os 21 arquivos de imagem + o manual).
- `imagens-puras/` (backup) e `imagens-tratadas/` (fonte do manual) — 21 imagens cada.

## Pontos-chave
- **Cada loja = conta Uber + Uber Direct + cartão próprios** (não compartilhar entre filiais).
- Cadastro em **direct.uber.com/accounts**.
- Webhook: `https://entregas.beefoodapi.be/api/uberDirect/webhook` (evento **event.delivery_status**);
  a **webhook_signing_key** valida o HMAC — por isso o passo 8 pede copiá-la.
- 3 credenciais em **Desenvolvedor → Chaves de API** → coladas no BeeFood + a chave do webhook.
- Pagamento cobrado **pela Uber no cartão**; o BeeFood não cobra as entregas.

## Observação de código
Card `uber-direct` em `appCategories.ts` ainda `disabled: 'Em breve!'` (git pull 04/08/2026);
flag `entregaUberDirectAtiva` já existe em `useCredenciaisEntrega.ts`. Ver `fluxo-codigo.md`.

## Status
Concluído (reimportado). Commit + push feitos. CHECKLIST/README/MEMORIA-GERAL atualizados. Aguardando publicação do dono.
