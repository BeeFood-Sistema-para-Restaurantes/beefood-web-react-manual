# MEMORIA.md — Integração Repediu

## Escopo
Manual do usuário final ensinando a **conectar o BeeFood ao Repediu** (CRM para restaurantes), com as
**duas configurações independentes**:
- **Tracker de Vendas** → Client ID + Client Secret (gerados em Repediu → Integrações → Fontes de dados → BeeFood).
- **Tracker de Cardápio Digital** → Write Key (gerada em Repediu → Web/App Analytics → Configuração → BeeFood).
E o preenchimento/salvamento no BeeFood em **Aplicativos → Marketing e CRM → Repediu → Configurar**.

## Origem
Produzido do zero (não importado). Fluxo validado ao vivo em 24/07/2026:
- **Repediu:** `https://app.repediu.com.br` — login `integracao@beefood.com.br` (exigiu resolver captcha + 2FA;
  o dono destravou o login manualmente).
- **BeeFood:** `https://beefood.app` — sandbox `contato@beefood.com.br` (empresa **BeeFood3 - Manual**).

Autorizações do dono: **salvar de verdade** (integração ativa real) e **manter as chaves visíveis** nos
prints (conta de testes).

## Descoberta importante (captura de tela na Repediu)
Os painéis do Repediu abrem como **modal lateral à direita (~30% da tela)**. Para o `browser_take_screenshot`
capturar corretamente, é preciso:
1. Fazer **navegação completa por URL** (`browser_navigate`) antes de abrir o modal — navegar só pelos
   cliques do menu SPA deixava o screenshot **preso num frame antigo**.
2. Garantir o navegador **em foco/ativo**.

## Dados usados na captura (conta de teste — descartáveis)
- Client ID: `8314`
- Client Secret: `d1a4bea5-d135-4d2d-9fdc-c8917b29b4cf`
- Write Key (gerada nesta sessão): `c630a6ab12074db182c91ef18bd037f6`

## Imagens (10, em `imagens-tratadas/`)
| Arquivo | Passo | Tipo | Conteúdo |
|---------|-------|------|----------|
| `01-repediu-integracoes-beefood.png` | 1 | seta | Repediu → Integrações → card BeeFood → **Habilitado** |
| `02-repediu-credenciais-vendas.png` | 2 | setas | Painel: **client_id** (1) e **client_secret** (2) |
| `03-repediu-analytics-cards.png` | 3 | seta | Web/App Analytics → Configuração → card BeeFood → **Habilitar** |
| `04-repediu-writekey-gerar.png` | 4 | seta | Modal Chave de escrita → **Gerar chave** |
| `05-repediu-writekey-gerada.png` | 5 | setas | **Write key** (1) + botão **Copiar** (2) |
| `06-beefood-aplicativos-repediu.png` | 6 | setas | BeeFood → **Aplicativos** (1) → card **Repediu** (2) |
| `07-beefood-repediu-modal-status.png` | 7 | setas | Status (1) + botão **Configurar** (2) |
| `08-beefood-form-configurar.png` | 8 | contexto | Formulário com os dois trackers (passthrough) |
| `09-beefood-form-preenchido.png` | 9 | setas | Client ID (1), Client Secret (2), Write Key (3), **SALVAR** (4) |
| `10-beefood-repediu-ativo.png` | 10 | setas | **Tracker de Vendas ativo** (1) e **Cardápio Digital ativo** (2) |

- `imagens-puras/` = backup dos originais (nunca referenciado).
- `imagens-tratadas/` = **única fonte** referenciada no manual. Gerada por `annotate.py`.

## Pontos a destacar
- São **duas credenciais distintas**, geradas em **dois lugares diferentes** do Repediu.
- Tracker de Vendas: preencher **os dois** campos ou **nenhum**.
- Tracker de Cardápio Digital é **independente** do de Vendas.
- **Redefinir** a Write Key no Repediu invalida a antiga (precisa recolar a nova no BeeFood).

## Observação de código
O checkout local `beefood-web-react` está em versão **anterior** (o `RepediuConfigModal.tsx` tem só
Client ID/Secret). A **produção** já evoluiu para o formulário de **dois trackers** (com Write Key). Ver
`fluxo-codigo.md`.

## Status
Concluído — aguardando publicação pelo dono.
