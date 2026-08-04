# MEMORIA.md — Integração Uber Direct

## Escopo
Manual do usuário final ensinando a **configurar o Uber Direct no BeeFood**: criar/entrar na conta Uber,
cadastrar o restaurante no Uber Direct, cadastrar o cartão, configurar o webhook e colar as credenciais
(**Customer ID / Client ID / Client Secret**) em **Aplicativos → Entregas → Uber Direct**.

## Origem
- Importado de `C:\projetos\beefood3-server-entregas\docs\uber-direct`.
- **Texto e imagens já vinham prontos** — instrução do dono: apenas **copiar e organizar no padrão**,
  **sem reinterpretar** (igual ao #8 99 Entrega).
- Havia dois `.md`: `onboarding-uber-direct.md` (MDX com Steps/Callout) e
  `onboarding-uber-direct-preview.md` (plain markdown). Usei o **preview** (plain markdown) como
  `integracao-uber-direct.md`, por ser o que casa com o padrão do repositório. Único ajuste:
  caminhos de imagem `imagens/` → `imagens-tratadas/`.

## Estrutura criada
- `integracao-uber-direct.md` — manual (conteúdo do preview, verbatim, só caminhos de imagem ajustados).
- `fluxo-codigo.md` — técnico/uso interno (credenciais, webhook, estado do card no código, modelo de negócio).
- `texto-documentation.ia.md` — prompt para o construtor de documentação (lista os 20 arquivos de imagem + o manual).
- `imagens-puras/` — 20 imagens originais (backup).
- `imagens-tratadas/` — 20 imagens (fonte única usada no manual). Já vinham com destaques; só copiadas.

## Pontos-chave do manual
- **Cada loja = uma conta Uber + Uber Direct + cartão próprios** (não compartilhar entre filiais).
- Cadastro no site **direct.uber.com/accounts**: conta Uber → conta Uber Direct (CNPJ/endereço/termos) →
  cartão (Gerenciamento → Pagamento) → webhook (Desenvolvedor → Webhooks) → chaves (Desenvolvedor → Chaves de API).
- Webhook: `https://entregas.beefoodapi.be/api/uberDirect/webhook` (evento **event.delivery_status**).
- Pagamento cobrado **pela Uber no cartão**; o BeeFood não cobra as entregas.
- No fim: colar as 3 credenciais no BeeFood e **Testar conexão**.

## Observação de código
Card `uber-direct` em `appCategories.ts` ainda está `disabled: 'Em breve!'` no `git pull` de 04/08/2026;
flag `entregaUberDirectAtiva` já existe em `useCredenciaisEntrega.ts`. Ver `fluxo-codigo.md`.

## Imagens (20; sem a 19, que não existe no fonte)
`uber-direct-00` (Aplicativos BeeFood) e `01`..`18` + `20`. Ordem de aparição no manual:
01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,20,00.

## Status
Concluído. Commit + push feitos. CHECKLIST/README/MEMORIA-GERAL atualizados. Aguardando publicação do dono.
