# BeeFood — Manuais de Funcionalidades

Repositório de **manuais de uso (usuário final)** do sistema BeeFood (`https://beefood.app`),
construídos a partir do código do projeto `beefood-web-react` e de capturas de tela reais em produção.

## Estrutura

```
.
├─ MEMORIA-GERAL.md            # Boas práticas, padrões, contas e ferramentas (ler primeiro)
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
| Reforma Tributária (IBS/CBS) | [`manuais/reforma-tributaria-ibscbs/`](manuais/reforma-tributaria-ibscbs/reforma-tributaria.md) | ✅ Concluído |
| Ativação Aiqfome V2 | [`manuais/ativacao-aiqfome/`](manuais/ativacao-aiqfome/ativacao-aiqfome.md) | ✅ Concluído |
| Integração Machine (entregas) | [`manuais/integracao-machine/`](manuais/integracao-machine/integracao-machine.md) | ✅ Concluído |
| Integração 99 Entrega | [`manuais/integracao-99-entrega/`](manuais/integracao-99-entrega/integracao-99-entrega.md) | ✅ Concluído |
| Integração Repediu (CRM) | [`manuais/integracao-repediu/`](manuais/integracao-repediu/integracao-repediu.md) | ✅ Concluído |

## Padrão visual das anotações

- Setas e números em **verde** (tom dos botões do sistema), finos e sutis.
- Coordenadas em frações (0..1) — independem da resolução da imagem.
- Regerar imagens tratadas: dentro da pasta do manual, rodar `python annotate.py`.

## Requisitos para gerar/anotar imagens

- Python 3.10+ e [Pillow](https://python-pillow.org/) (`pip install pillow`).

---

© BeeFood. Uso interno.
