# MEMORIA.md — Integração Uber Direct

## Escopo
Manual do usuário final ensinando a **configurar o Uber Direct no BeeFood** e usá-lo no dia a dia:
criar/entrar na conta Uber, cadastrar o restaurante no Uber Direct, cadastrar o cartão, configurar o
webhook, **copiar a Chave de autenticação do webhook** e as credenciais (**ID do usuário / ID de
cliente / Client Secret**), colar tudo em **Aplicativos → Entregas → Uber Direct** e, por fim,
**despachar / acompanhar / cancelar** pedidos.

## Origem
- Importado de `C:\projetos\beefood3-server-entregas\docs\uber-direct`.
- **Texto e imagens já vinham prontos** — instrução do dono: apenas **copiar e organizar no padrão**,
  **sem reinterpretar** (igual ao #8 99 Entrega).
- Havia dois `.md`: `onboarding-uber-direct.md` (MDX com Steps/Callout) e
  `onboarding-uber-direct-preview.md` (plain markdown). Usei o **preview** como `integracao-uber-direct.md`.
  Único ajuste: caminhos `imagens/` → `imagens-tratadas/`.
- **04/08/2026:** manual recriado do zero (a pedido: "delete e copie novamente como se fosse novo").
  Conteúdo: **12 passos**, **27 imagens** (`01`..`27`), com as seções "Como funciona no dia a dia" e
  "Status — o que você vê no BeeFood".

## Estrutura
- `integracao-uber-direct.md` — manual (conteúdo do preview, verbatim; só caminhos de imagem ajustados).
- `fluxo-codigo.md` — técnico/uso interno (front + rotas, tabelas, OAuth, webhook HMAC + signing key, negócio).
- `texto-documentation.ia.md` — prompt (lista os 27 arquivos de imagem + o manual).
- `imagens-puras/` (backup) e `imagens-tratadas/` (fonte do manual) — 27 imagens cada.

## Pontos-chave
- **Cada loja = conta Uber + Uber Direct + cartão próprios** (não compartilhar entre filiais).
- Cadastro em **direct.uber.com/accounts**.
- Webhook: `https://entregas.beefoodapi.be/api/uberDirect/webhook` (evento **event.delivery_status**);
  a **webhook_signing_key** valida o HMAC — por isso o passo 8 pede copiá-la.
- 3 credenciais em **Desenvolvedor → Chaves de API** + a chave do webhook → coladas no BeeFood.
- Pagamento cobrado **pela Uber no cartão**; o BeeFood não cobra as entregas.

## Observação de código (git pull 04/08/2026)
- A integração **saiu do "Em breve!"** e está **ativa** no BeeFood:
  card `uber-direct` em `appCategories.ts` com `isNew: true` (sem `disabled`).
- Já existem no front: `components/aplicativos/UberDirectModal.tsx` (modal de credencial),
  `hooks/useUberDirectCredencial.ts` e `services/entrega/uberdirect.ts` (cotação/pedido/cancelar).
- O modal do BeeFood corresponde exatamente ao **passo 10** do manual (campos ID do usuário,
  ID de cliente do desenvolvedor, Client Secret, Chave de autenticação + switch Integração ativa).
- Botão **AJUDA** do modal aponta para `https://ajuda3.beefood.com.br/integracao-uber-direct`
  (destino de publicação deste manual). Ver `fluxo-codigo.md`.

## Status
Concluído (recriado do zero). Commit + push feitos. CHECKLIST/README atualizados. Aguardando publicação do dono.
