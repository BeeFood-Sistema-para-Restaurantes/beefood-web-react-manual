# MEMORIA.md — Integração FoodCRM

## Escopo
Manual do usuário final ensinando a **conectar o BeeFood ao FoodCRM** (CRM para restaurantes). A
integração faz o BeeFood **enviar as vendas automaticamente, diariamente de madrugada**, para o FoodCRM.
É necessária **uma credencial** — a **API Key / Token** (`fcrm_...`) — gerada no FoodCRM e colada no
BeeFood, **por cardápio digital**.

## Origem
- Solicitado pelo dono do FoodCRM (Andrey). Login FoodCRM: `beefood@foodcrm.com.br` / `Beefood@0501`.
- URL FoodCRM: `https://app.foodcrm.com.br/`.
- Fluxo indicado: menu **Integrações → botão Acessar a documentação → API Key / Token**; no BeeFood,
  **Aplicativos → FoodCRM**.

## Fluxo validado (ao vivo)
1. FoodCRM → **Integrações** → **Acessar a documentação** → drawer "API de integração" → copiar **API Key / Token**.
2. BeeFood → **Aplicativos** → **Marketing e CRM** → card **FoodCRM** → cardápio → **+ Adicionar** →
   colar **API key** → **Ativo** ligado → **SALVAR (F2)**.
3. Confirma status **Ativo** no cardápio (chave mascarada `fcrm_..._••••••`). **Salvo de verdade** no sandbox.

## Descobertas importantes
- O botão **"Acessar a documentação"** NÃO abre página externa; abre um **drawer lateral à direita**
  ("API de integração") com Código da loja + API Key/Token. (A tentativa de abrir em nova aba deu popup
  em branco — o conteúdo real é o drawer.)
- No BeeFood, o modal de credencial pede **apenas** a `api_key` (`fcrm_...`) — o **Código da loja não é usado**.
- Existe também um **card "BeeFood"** no FoodCRM com um formulário reverso (Webhook + Código da loja +
  Token + Url do cardápio + Salvar). É caminho alternativo; **não** entrou no manual (usuário confirmou
  documentar o fluxo "Acessar a documentação").
- FoodCRM tem tema claro (Toggle color mode); manual capturado em **tema claro** para manter o padrão.
- Havia um modal "WhatsApp Desconectado" bloqueando a navegação inicial (pointer-events none nos menus);
  resolvido com **Ignorar por 24h**.

## Imagens (6, todas em imagens-tratadas/)
1. `01-foodcrm-integracoes.png` — FoodCRM → menu Integrações (1) + botão Acessar a documentação (2).
2. `02-foodcrm-api-token.png` — drawer API de integração: API Key/Token (1) + Copiar (2).
3. `03-beefood-aplicativos-card.png` — BeeFood → menu Aplicativos (1) + card FoodCRM (2).
4. `04-beefood-modal-cardapios.png` — modal Credenciais por Cardápio: status Não configurado (1) + Adicionar (2).
5. `05-beefood-modal-apikey.png` — modal de credencial: API key (1) + Ativo (2) + SALVAR (3).
6. `06-beefood-ativo.png` — cardápio com status Ativo (1) + botão Editar (2).

`imagens-puras/` = originais (backup). `imagens-tratadas/` = fonte única usada no manual (setas verdes numeradas).

## Credenciais de teste (sandbox, conta de testes)
- FoodCRM: `beefood@foodcrm.com.br` / `Beefood@0501` (conta "BeeFood Teste").
- API Key / Token: `fcrm_3bd2e0c3_Eb6H5KdG_SgbWAvBTB2g-wgX5Rfnh1aC`.
- Código da loja: `cb0484ad-0432-4981-976f-a1a920ed723c`.
- Chaves mantidas visíveis por serem de conta de testes (decisão do usuário).

## Observação de código
Ver `fluxo-codigo.md`. Componentes: `FoodCrmModal.tsx`, `FoodCrmConfigModal.tsx`, `useFoodCrm.ts`.
APIs: GET/POST/DELETE `/api/empresa2/foodcrm`. Config por `filialID` (cardápio). Envio diário (madrugada).

## Status
Concluído. Commit + push feitos. CHECKLIST/README/MEMORIA-GERAL atualizados.
