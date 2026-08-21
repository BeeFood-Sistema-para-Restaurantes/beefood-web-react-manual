# BeeFood — Manuais de Funcionalidades

Repositório de **manuais de uso (usuário final)** do sistema BeeFood (`https://beefood.app`),
construídos a partir do código do projeto `beefood-web-react` e de capturas de tela reais em produção.

## Estrutura

```
.
├─ MEMORIA-GERAL.md            # Boas práticas, padrões, contas e ferramentas (ler primeiro)
├─ CHECKLIST-MANUAIS.md        # O que já foi feito, o que está na fila e o histórico
├─ validar-imagens.py          # Confere se as imagens referenciadas pelos manuais existem
└─ manuais/
   └─ <nome-do-manual>/        # Uma pasta por manual
      ├─ MEMORIA.md            # Memória detalhada do manual (fluxo, uso, decisões, estado)
      ├─ <nome>.md             # O manual final (para o usuário)
      ├─ fluxo-codigo.md       # Mapeamento técnico (a partir do código)
      ├─ annotate.py           # Script de anotação (setas/números) — Python + Pillow
      ├─ imagens-puras/        # Screenshots originais (backup, sem edição)
      └─ imagens-tratadas/     # Screenshots com setas/números (usados no manual)
```

## Manuais disponíveis

| Manual | Pasta | Status |
|--------|-------|--------|
| Caixa (abrir, receber pagamento, consultar) | [`manuais/caixa/`](manuais/caixa/caixa.md) | ✅ Concluído |
| Fechar caixa (vendas pendentes, conferência, quebra) | [`manuais/caixa-fechar/`](manuais/caixa-fechar/caixa-fechar.md) | ✅ Concluído |
| Segunda conferência (dupla checagem) | [`manuais/caixa-conferencia-2/`](manuais/caixa-conferencia-2/caixa-conferencia-2.md) | ✅ Concluído |
| Restrições de caixa (grupo de acesso) | [`manuais/caixa-restricoes/`](manuais/caixa-restricoes/caixa-restricoes.md) | ✅ Concluído |
| Reforma Tributária (IBS/CBS) | [`manuais/reforma-tributaria-ibscbs/`](manuais/reforma-tributaria-ibscbs/reforma-tributaria.md) | ✅ Concluído |
| Ativação Aiqfome V2 | [`manuais/ativacao-aiqfome/`](manuais/ativacao-aiqfome/ativacao-aiqfome.md) | ✅ Concluído |
| Integração Machine (entregas) | [`manuais/integracao-machine/`](manuais/integracao-machine/integracao-machine.md) | ✅ Concluído |
| Integração 99 Entrega | [`manuais/integracao-99-entrega/`](manuais/integracao-99-entrega/integracao-99-entrega.md) | ✅ Concluído |
| Integração Repediu (CRM) | [`manuais/integracao-repediu/`](manuais/integracao-repediu/integracao-repediu.md) | ✅ Concluído |
| Integração FoodCRM (CRM) | [`manuais/integracao-foodcrm/`](manuais/integracao-foodcrm/integracao-foodcrm.md) | ✅ Concluído |
| Integração Uber Direct (entregas) | [`manuais/integracao-uber-direct/`](manuais/integracao-uber-direct/integracao-uber-direct.md) | ✅ Concluído |
| Segmentação de clientes (Food Marketing) | [`manuais/segmentacao-clientes/`](manuais/segmentacao-clientes/segmentacao-clientes.md) | ✅ Concluído |
| Campanhas Inteligentes (Food Marketing) | [`manuais/campanhas-inteligentes/`](manuais/campanhas-inteligentes/campanhas-inteligentes.md) | ✅ Concluído |
| Fiado — operar no dia a dia | [`manuais/fiado/`](manuais/fiado/fiado.md) | ✅ Concluído |
| Fiado — cobrança agrupada | [`manuais/fiado-cobranca-agrupada/`](manuais/fiado-cobranca-agrupada/fiado-cobranca-agrupada.md) | ✅ Concluído |

## Padrão visual das anotações

- Setas e números em **verde** (tom dos botões do sistema), finos e sutis.
- Coordenadas em frações (0..1) — independem da resolução da imagem.
- Regerar imagens tratadas: dentro da pasta do manual, rodar `python annotate.py`.

## Antes de publicar um manual

```bash
python validar-imagens.py            # todos os manuais
python validar-imagens.py caixa      # só um
```

Falha (código 1) se algum manual referenciar imagem que não existe. Avisa também sobre imagem
órfã e sobre divergência entre o manual e o `texto-documentation.ia.md`.

## Requisitos para gerar/anotar imagens

- Python 3.10+ e [Pillow](https://python-pillow.org/) (`pip install pillow`).

---

© BeeFood. Uso interno.
