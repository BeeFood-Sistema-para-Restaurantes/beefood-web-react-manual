# fluxo-codigo.md — #78 Classificação RFV (uso interno, NÃO publicar)

## Telas

- Lista: `src/pages/Clientes.tsx` — botão RFV + `?` + chips (só grupos com `count > 0`).
- Limites: `src/components/ModalRFVParametros.tsx` — POST salva; **Resetar Padrão** chama reset.
- Ajuda dos 11 grupos: `src/components/ModalRFVClassificacao.tsx` (texto fixo no front).
- Ficha, aba Indicadores: `src/components/ModalCadastroCliente.tsx` — só leitura; selo + círculos R/F/V; “Atualizado a cada 24h”.
- Relatório: `beefood-reports-hub` → `AnaliseRFV.tsx` (Desempenho → Clientes → Análise RFV).
- O mesmo grupo também aparece em `BaseClientes.tsx` (gráfico Classificação RFV).

Rotas: `/clientes`, `/food-marketing/segmentacao-cliente`,
`/food-marketing/campanhas-whatsapp`,
`/food-marketing/campanhas-whatsapp?tab=automacao`,
`/food-marketing/campanhas-sms`.

## API (app3.beetechapi.be)

- `GET /api/cliente2/rfvParametro/{empresaID}/{usuarioID}`
- `POST /api/cliente2/rfvParametro` — body com as 3 escalas + `log` (valores antigos)
- `POST /api/cliente2/rfvReset` — `{ empresaID, usuarioID }`
- Cadastro (notas no cliente): `GET /datasnap/rest/cliente2/cadastro/{empresa}/{usuario}/{todos}/1`
- Catálogo da segmentação: `GET /api/cliente2/segmentacao/campos/{empresa}/{usuario}`

Hook: `src/hooks/useRFVParametros.ts`.

A procedure que **calcula** as notas (`funcSelect_Cliente_RFV` / job ~24h) **não está no
front**. Não há endpoint “recalcular agora”.

## Como a nota vira grupo (front da ajuda)

- R, F, V cada um 1–5, pelos limites da modal.
- **V nos parâmetros = ticket médio.** Na ficha o círculo V está rotulado “Total gasto”,
  mas a nota do sandbox (João: ticket R$ 34,89 → V=2; total R$ 1.919 → seria V=5)
  segue o ticket. Vale a modal de parâmetros.
- **FV** = média arredondada de F e V.
- Grupo = cruzamento R × FV. “Potenciais Fiéis” e “Em potenciais” são o **mesmo**
  quadrado (R 4–5, FV 2–3); a lista usa os dois `value` (`Potenciais Fieis` /
  `Em potenciais`).
- 11 grupos, não 12. A segmentação lista “12 opções” porque os dois nomes aparecem
  no multiselect.

Ordem do relatório (`AnaliseRFV.tsx`): Campeões → Fiéis → Em risco → Não posso
perder → Precisam de atenção → Em potenciais → Novos → Promissores → Quase
dormentes → Hibernando → Perdidos.

## Propagação ao editar limite

`ModalRFVParametros.updateField`:

- Recência: editar `rN_max` preenche `r(N-1)_min = max+1`. R1 não tem máximo.
- Frequência / Valor: editar o mínimo de cima preenche o máximo de baixo
  (F: −1 pedido; V: −0,01). F5 e V5 não têm máximo.

## Onde o RFV entra (mapa real do front)

Dois jeitos, não um:

1. **Direto no WhatsApp em massa**
   - Atalho **Campanha RFV**: `ModalNovaCampanhaRFV.tsx` (dropdown
     “Nova Campanha Filtro Avançado” em `WhatsAppEnviosMassaTab.tsx`).
   - **Adicionar → RFV** numa campanha já aberta: `ModalAdicionarPorRFV.tsx`
     (`ModalEditarCampanha.tsx`).
   - Os dois leem `cliente.classificacao` da lista de cadastro. Incluem
     “Sem classificação”.
2. **Pela segmentação** (recalcula o público na hora)
   - 4 campos no catálogo: `classificacao`, `recencia`, `frequencia`,
     `valorMonetario`.
   - WhatsApp: atalho **Campanha Segmentação Cliente**
     (`ModalNovaCampanhaSegmentacao`).
   - Inteligente: `origemPublico = SEGMENTACAO` + `segmentacaoID`.
   - SMS: passo 2, modo **Por segmentação** → `POST /sms2/campanha/segmentacao`.
     SMS **não** tem atalho RFV direto.

```
rfvParametro  →  job diário grava classificacao/recencia/frequencia/valorMonetario
              ├── WhatsApp: Campanha RFV / Adicionar por RFV
              └── segmentação
                    ├── WhatsApp: Campanha Segmentação Cliente
                    ├── inteligente (SEGMENTACAO)
                    └── SMS (passo 2)
```

Quatro inteligentes padrão usam `SEGMENTACAO` + público fixo (não são filtro RFV
de fábrica):

| Campanha | Chave do público | Filtro real |
|----------|------------------|-------------|
| Recuperador de vendas | `fixo-sumidos` | dias sem comprar ≥ 30 |
| Cashback parado | `fixo-cashback` | saldo de cashback |
| Aniversário | `fixo-aniversario` | aniversário |
| Boas-vindas | `fixo-novos` | clientes novos |

O usuário **pode** trocar o campo Segmentação por um público seu que filtre
`classificacao` / R / F / V. Carrinho (`PIXEL_CARRINHO`) e BeeBot sem compra
(`BEEBOT_SEM_COMPRA`) não passam por segmentação.

WhatsApp em massa (#15, aprovado sem pasta) tem RFV **e** segmentação como
caminhos da lista (além de avulso, filtro avançado e Excel). SMS (#18) entra
**só** via segmentação.

Cupom, cashback, PDV e Pixel **não** leem `cliente.classificacao`. O modelo
pronto de segmentação **Clientes VIP** filtra `frequencia` 4–5 e
`valorMonetario` 4–5 (notas RFV, não o grupo). O mock `em-risco` (Em risco +
Hibernando) existe no front; o #14 publicado lista 9 modelos e não inclui
esse — o texto do #78 cita só o VIP, que o #14 já documenta.

## Padrão ao vivo no sandbox (BeeFood3, 2026-09-02)

Confirmado na modal, não só no código:

- R: 5 / 16 / 30 / 48 / ≥49
- F: ≥12 / 9–11 / 5–8 / 2–4 / ≤1
- V (ticket): ≥100 / 80–99,99 / 50–79,99 / 30–49,99 / ≤29,99

Chips com gente: Fiéis 2, Em potenciais 11, Precisam de atenção 1, Em risco 2,
Hibernando 1, Perdidos 9. Sem Campeão, Novo, Promissor, Quase dormente, Não
posso perder, Potenciais fiéis.

Permissão: a mesma da tela Clientes. RFV não tem itemID próprio.
