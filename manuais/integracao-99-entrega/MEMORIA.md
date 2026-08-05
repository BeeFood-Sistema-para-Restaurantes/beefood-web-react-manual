# MEMORIA.md — Integração 99 Entrega

## Escopo
Manual do usuário final ensinando a **configurar e usar a integração de entregas 99 Entrega** no BeeFood:
solicitar **boleto** (único meio de pagamento da integração; análise da 99), pedir o **ambiente de
produção** no Modo de desenvolvedor (também com análise), cadastrar o **webhook**, copiar as 3 credenciais
de API, colá-las no BeeFood (Aplicativos → Entregas → 99 Entrega), despachar um pedido com cotação e
acompanhar/cancelar.

## Origem
Importado de `C:\projetos\beefood3-server-entregas\docs\nn-entregas`:
- `onboarding-99-entrega.md` → **copiado como está** para `integracao-99-entrega.md` (texto já pronto,
  **sem reescrita/interpretação** a pedido do dono). Único ajuste: caminhos das imagens `imagens/` →
  `imagens-tratadas/`.
- `api-cotacao.md` + `schema*.sql` → consolidados no `fluxo-codigo.md` (uso interno, não publicar).

## Histórico
- **1ª versão (jul/2026):** fluxo baseado em **cartão**, 15 imagens (`01`..`15`).
- **05/08/2026 — recriado do zero** (a pedido: "delete e copie novamente de beefood3-server-entregas").
  A fonte foi **totalmente atualizada**:
  - Pagamento da integração agora é **somente boleto** (não é mais cartão). Surgiram os passos de
    **solicitar boleto** e **pedir ambiente de produção**, ambos com **análise da 99**.
  - Manual passou a ter **7 passos** e cobre também **despachar / acompanhar / cancelar**.
  - Conjunto de imagens virou **`01`..`24`**. O texto atual referencia **`05`..`24`** (20 imagens);
    as `01`..`04` são do fluxo antigo de **cartão** e **não são citadas** — ficam só em `imagens-puras/`.

## Imagens
- `imagens-puras/` = **backup dos originais** → 24 imagens (`01`..`24`).
- `imagens-tratadas/` = **única fonte** referenciada no manual → 20 imagens (`05`..`24`), já prontas
  (setas/caixas na origem), **sem retoque**.

## Decisões
- **Não interpretar/reescrever** o texto — o dono já entregou o manual pronto. Só padronizamos a pasta e
  os caminhos de imagem.
- Não usar `annotate.py` (imagens já anotadas na origem).
- `01`..`04` (cartão) descartadas do manual por não serem citadas no texto novo; mantidas em `imagens-puras/`.

## Pontos a destacar
- Pagamento da integração é **exclusivamente boleto** — cartão não se aplica.
- Boleto e ambiente de produção passam por **análise da 99**; o suporte BeeFood agiliza.
- 3 credenciais vêm do **Modo de desenvolvedor** da 99: ID do cliente, Segredo do cliente, Chave de assinatura.
- Webhook a cadastrar na 99: `https://entregas.beetechapi.be/api/99Entrega/webhook`.
- Cancelamento só **antes** de o entregador retirar o pedido.

## Status
Concluído (recriado do zero) — aguardando publicação pelo dono.
