# MEMORIA.md — Integração 99 Entrega

## Escopo
Manual do usuário final ensinando a **configurar e usar a integração de entregas 99 Entrega** no BeeFood:
cadastrar cartão no painel da 99, obter as credenciais de API (Modo de desenvolvedor), cadastrar o webhook,
colar as credenciais no BeeFood (Aplicativos → Entregas → 99 Entrega), despachar um pedido com cotação e
acompanhar/cancelar.

## Origem
Importado de `C:\projetos\beefood3-server-entregas\docs\nn-entregas`:
- `onboarding-99-entrega.md` → **copiado como está** para `integracao-99-entrega.md` (texto já pronto,
  **sem reescrita/interpretação** a pedido do dono). Único ajuste: caminhos das imagens `imagens/` →
  `imagens-tratadas/`.
- `api-cotacao.md` + `schema.sql` → consolidados no `fluxo-codigo.md` (uso interno, não publicar).

## Imagens
15 imagens **já prontas** (com setas/caixas verdes na origem) — apenas copiadas, **sem retoque**:

| Arquivo | Passo | Conteúdo |
|---------|-------|----------|
| `99-entrega-01.png` | 1 | Painel 99 → **Configurações de pagamento** |
| `99-entrega-02.png` | 1 | Método de pagamento → **Gerenciar** |
| `99-entrega-03.png` | 1 | 99Pay → **Adicionar cartão** |
| `99-entrega-04.png` | 1 | Dados do cartão → **Adicionar** |
| `99-entrega-05.png` | 2 | Painel 99 → **Modo de desenvolvedor** |
| `99-entrega-06.png` | 2 | Webhook → campo **URL (Insira o webhook)** |
| `99-entrega-07.png` | 2 | Credenciais: **ID do cliente / Segredo do cliente / Chave de assinatura** |
| `99-entrega-08.png` | 3 | BeeFood → menu **Aplicativos** |
| `99-entrega-09.png` | 3 | Seção **Entregas → 99 Entrega** |
| `99-entrega-10.png` | 4 | Modal de credenciais no BeeFood → **SALVAR (F2)** |
| `99-entrega-11.png` | 5 | Delivery — pedido #8 na coluna **Preparo** |
| `99-entrega-12.png` | 5 | Detalhe do pedido → **Adicionar Entregador** |
| `99-entrega-13.png` | 5 | **Entrega Terceirizada → 99 Entrega** |
| `99-entrega-14.png` | 5 | Modal de cotação (distância/tempo/frete) → **CONFIRMAR (F2)** |
| `99-entrega-15.png` | 5 | Guia Entregador — **Entregue por 99 Entrega** (lixeira p/ cancelar) |

- `imagens-puras/` = backup dos originais.
- `imagens-tratadas/` = **única fonte** referenciada no manual (aqui é cópia idêntica, pois já vieram tratadas).

## Decisões
- **Não interpretar/reescrever** o texto — o dono já entregou o manual pronto. Só padronizamos a pasta e
  os caminhos de imagem.
- Não usar `annotate.py` (imagens já anotadas na origem).

## Pontos a destacar
- É preciso **cadastrar cartão** no painel da 99 antes de operar.
- 3 credenciais vêm do **Modo de desenvolvedor** da 99: ID do cliente, Segredo do cliente, Chave de assinatura.
- Webhook a cadastrar na 99: `https://entregas.beetechapi.be/api/99Entrega/webhook`.
- Cancelamento só **antes** de o entregador retirar o pedido.

## Status
Concluído — aguardando publicação pelo dono.
