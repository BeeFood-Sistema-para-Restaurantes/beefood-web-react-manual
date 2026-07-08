# MEMORIA.md — Integração Machine

## Escopo
Manual do usuário final ensinando a **configurar e usar a integração de entregas Machine** no BeeFood:
solicitar credenciais, ativar em Aplicativos → Entrega → Machine, preencher a configuração, despachar um
pedido (manual/automático), acompanhar em tempo real e cancelar.

## Origem
Importado de `C:\projetos\beefood3-server-entregas\docs\machine`:
- `README.md` → base do manual do usuário (`integracao-machine.md`).
- `api-credencial.md` + `api-pedido-cancelamento.md` + `schema-webhook-empresaID.sql` → consolidados no
  `fluxo-codigo.md` (uso interno, não publicar).

## Imagens
7 imagens **já prontas** (com destaques em verde na origem) — apenas copiadas, **sem retoque**:

| Arquivo | Passo | Conteúdo |
|---------|-------|----------|
| `machine-01.png` | 2 | Menu lateral → **Aplicativos** |
| `machine-02.png` | 2 | Aba **Entrega** → card **Machine (NOVO)** |
| `machine-03.png` | 3 | Tela de configuração (Integração ativa, Api Key, Client ID/Secret, Empresa ID, forma de pagamento, retorno, sincronização) |
| `machine-04.png` | 5 | Delivery — pedido #660 na coluna **Preparo** |
| `machine-05.png` | 5 | Botão **Adicionar Entregador** |
| `machine-06.png` | 5 | **Entrega Terceirizada → Machine** selecionado |
| `machine-07.png` | 6 | Guia Entregador — **Entregue por Machine** (com lixeira p/ cancelar) |

- `imagens-puras/` = backup dos originais.
- `imagens-tratadas/` = **única fonte** referenciada no manual (aqui é cópia idêntica, pois já vieram tratadas).

## Melhorias aplicadas (interpretação)
- Reestruturado em 3 partes (solicitar credenciais → configurar → despachar/acompanhar).
- Tabelas de credenciais e opções de operação alinhadas ao que aparece na tela (machine-03).
- Adicionadas seções **Problemas comuns** e **Precisa de ajuda?**.
- Corrigido typo e mantido tom didático (usuário final / restaurante).

## Pontos a destacar
- Empresa ID (Machine) é **diferente** do empresaID do BeeFood.
- Sincronização pode ser **manual** ou automática (PREPARO/PRONTO); com automática o despacho é sozinho.
- Cancelamento é feito pela **lixeira** na guia Entregador.

## Status
Concluído — aguardando publicação pelo usuário.
