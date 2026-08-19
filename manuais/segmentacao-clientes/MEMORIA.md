# MEMÓRIA — Manual de Segmentação de Clientes

> Memória detalhada deste manual. Ver também: `../../MEMORIA-GERAL.md`.

Status: 🔨 **Em execução** — estudo concluído e plano aprovado em 2026-08-19.

---

## 1. Escopo aprovado pelo dono

Manual ensinando a **criar segmentações de clientes**, com **vários exemplos práticos** de
restaurante. Decisões dele:

- Foco em exemplos: a galeria de casos é a parte principal, não um apêndice.
- **Pode criar públicos de teste no sandbox e deixá-los salvos** — não precisa excluir depois.
- Desktop apenas (padrão dos manuais anteriores).
- Numeração `1, 2, 3` no texto (nunca `①②③`).

---

## 2. Onde fica

**Food Marketing → Segmentação de Cliente** (singular no menu), rota
`/food-marketing/segmentacao-cliente`. Badge **NOVO** no menu lateral.

Permissão: itemID **292** no grupo de acesso (`segmentacaoCliente`), com formularioID 165. Os
endpoints do backend **não revalidam** o itemID — a restrição é de interface.

---

## 3. O conceito que o manual precisa acertar

**Um público não é uma lista de clientes — é uma receita.** A tabela `segmentacao` guarda
apenas `regraJson`; nada de "clientes do público X" fica materializado. Toda vez que o público
é usado (teste, exportação, campanha), o servidor recalcula quem se encaixa naquele momento.

**Filtro primário, sempre aplicado e não configurável.** Antes de qualquer regra, a base é
restrita a clientes com:

1. telefone com 10 dígitos ou mais,
2. `ativo = 1`,
3. `aceitaWhatsapp = 1`.

```sql
where empresaID = @empresaID
  and isnull(ativo, 0) = 1
  and isnull(aceitaWhatsapp, 0) = 1
  and len(isnull(telefonePrincipal, '')) >= 10
```

É por isso que o percentual mostrado na tela é sobre **essa base elegível**, e não sobre o total
de clientes cadastrados. Sem explicar isso, o número parece errado.

---

## 4. O catálogo real — 37 campos em 9 grupos

Conferido **na API de produção** (`GET /cliente2/segmentacao/campos/{empresaID}/{usuarioID}`),
não pelo mock do front. Os dois divergem em alguns rótulos; vale o da API.

| Grupo | Qtd | Campos |
|-------|-----|--------|
| Cliente | 3 | Cardápio, Origem do cadastro, Tipo de pessoa (PF/PJ) |
| Indicadores | 9 | Total de pedidos, Total gasto (R$), Ticket médio (R$), Nota média de avaliação, Última nota de avaliação, Dias sem comprar, Tempo de cliente (dias), Data da primeira compra, Data da última compra |
| RFV | 4 | Classificação RFV (público), Recência (1-5), Frequência (1-5), Valor monetário (1-5) |
| Aniversário | 3 | Mês de aniversário (1-12), Dias até o aniversário, Data de nascimento |
| Cashback | 2 | Saldo de cashback (R$), Possui saldo de cashback |
| Cupom | 3 | Já usou cupom de desconto, Qtd. de cupons usados, Cupons usados (código) |
| Endereço | 5 | Bairro, Cidade, Estado (UF), CEP, Distância (km) |
| Vendas | 7 | Setores comprados, Produtos comprados, Categoria favorita (setor mais comprado), Produto favorito, Dias da semana que comprou, Períodos do dia que comprou, Cadência média entre pedidos (dias) |
| Canais | 1 | Canais onde comprou |

As 12 classificações RFV vêm com emoji: 🏆 Campeões, 💎 Fiéis, 🌱 Promissores, 🆕 Novos
Clientes, ⭐ Potenciais Fiéis, ⭐ Em Potenciais, ⚠️ Precisam de Atenção, 💤 Quase Dormentes,
🔥 Em Risco, ❄️ Hibernando, ❌ Perdidos, 🚨 Não Posso Perder.

Os 13 canais: iFood, Aiqfome, UaiRango, Delivery Much, Rappi, 99Food, Keeta, Cardápio Digital,
Autoatendimento, PDV, Mesas / Comanda, Delivery (entrega), Delivery (retirada).

### Atenção: os rótulos dos operadores na tela NÃO são os da API

O front reescreve os rótulos (`src/components/segmentacao/labels.ts`). Vale o da tela:

| Na API | **Na tela (usar no manual)** |
|--------|------------------------------|
| está em | **é um de** |
| não está em | **não é nenhum de** |
| maior que | **é maior que** |
| maior ou igual a | **é maior ou igual a** |
| menor que | **é menor que** |
| menor ou igual a | **é menor ou igual a** |
| entre | **está entre** |
| antes de | **é antes de** |
| depois de | **é depois de** |
| não está vazio | **está preenchido** |
| verdadeiro / falso | **sim** / **não** |

Iguais nos dois: é igual a, é diferente de, contém, não contém, começa com, termina com,
está vazio, está entre as datas.

O front também troca alguns nomes de campo: `filialID` vira **Cardápio**, `recencia` vira
**Recência (R) — 1 a 5**, `tipoCliente` vira **Tipo de pessoa (PF/PJ)**.

### Semânticas que só o código revelou

- **Campos de lista respondem a "algum item satisfaz".** Se o cliente comprou por três canais e
  a regra filtra por um, ele entra. Vale para Canais, Bairro, Produtos, Setores, Períodos.
- **"Dias sem comprar" e "Tempo de cliente" são calculados na hora**, com a data do servidor
  Node (não com o fuso da empresa).
- **Cliente sem compra tem esses campos nulos** e a comparação numérica **falha** — ele fica de
  fora de qualquer regra do tipo "dias sem comprar > X".
- **"Possui saldo de cashback" é qualquer valor acima de zero** (um centavo conta). O público
  fixo da BeeFood usa `>= 3` justamente para evitar saldos irrisórios.
- **Cupom não tem recorte de período** — é histórico vitalício de usos.
- **Aniversário sai de `_cliente.dataAbertura`**, tratada como data de nascimento.
  `Dias até o aniversário = 0` significa "é hoje".
- **Texto compara sem acento e sem diferenciar maiúsculas.**
- **Operador desconhecido faz a condição ser ignorada** (vira verdadeiro) — não gera erro.

### Duas lacunas — declarar como lacuna, não inventar

1. **A fórmula de "Total de pedidos", "Total gasto" e "Ticket médio"** está num ETL que
   preenche `_clienteProcessado`, fora do repositório do servidor. Não dá para afirmar se
   vendas canceladas entram, nem como o ticket é ponderado.
2. **Os limiares do RFV** (o que faz alguém ser "Campeão" e não "Fiel", e os scores 1 a 5) estão
   na procedure `funcSelect_Cliente_RFV`, que não está versionada. O manual deve explicar o RFV
   como conceito e dizer que a classificação é calculada pelo sistema, sem prometer limiares.

---

## 5. Como as regras se combinam

Árvore JSON de grupos e condições:

```json
{ "operadorLogico": "and", "negar": false, "condicoes": [ ... ] }
```

O motor suporta aninhamento sem limite e negação, mas **o construtor visual só oferece uma
lista plana com E/OU** — sem subgrupos e sem "NÃO". O E/OU escolhido vale para **todas** as
condições da lista, não é por linha.

---

## 6. Modelos prontos (9) e públicos fixos (4)

### Modelos prontos — botão **Modelos prontos**, viram cópia editável

| Nome | Categoria | Regra exata |
|------|-----------|-------------|
| Clientes sumidos (reconquista) | Reconquista | pedidos ≥ 2 **E** dias sem comprar ≥ 30 |
| Inativos há mais de 90 dias | Reconquista | dias sem comprar ≥ 90 |
| Incentivar a 2ª compra | Fidelização | pedidos = 1 **E** dias sem comprar ≤ 30 |
| Clientes VIP (alto valor) | Fidelização | frequência ≥ 4 **E** valor monetário ≥ 4 |
| Cashback parado (traga de volta) | Reconquista | possui saldo de cashback |
| Hora de pedir de novo (cadência) | Reconquista | cadência ≤ 15 dias **E** dias sem comprar > 18 |
| Tirar dos marketplaces (pedido direto) | Margem | comprou em marketplace **E** nunca em canal próprio |
| Sensíveis a desconto | Promoção | já usou cupom |
| Aniversariantes da semana | Datas comemorativas | dias até o aniversário ≤ 7 |

### Públicos fixos da BeeFood — só leitura, alimentam as automações

| Nome | Regra |
|------|-------|
| Clientes novos (1º pedido, 6 a 30 dias) | pedidos = 1 **E** dias sem comprar entre 6 e 30 |
| Clientes sumidos (31 a 90 dias sem comprar) | pedidos ≥ 2 **E** dias sem comprar entre 31 e 90 |
| Cashback parado (R$ 3,00 ou mais) | saldo ≥ 3 |
| Aniversariantes do dia | dias até o aniversário = 0 |

As janelas dos fixos não se sobrepõem de propósito (novos param em 30, sumidos começam em 31),
para o mesmo cliente não receber duas automações.

> **Detalhe do sandbox:** os 4 públicos fixos aparecem **duplicados** na lista (8 registros).
> É característica do ambiente de teste, não do produto. Evitar capturas que mostrem isso.

---

## 7. A base do sandbox e o que rende exemplo

**15 clientes elegíveis** (base pequena, mas suficiente). Distribuição de RFV: Perdidos 6,
Hibernando 3, Fieis 2, Em potenciais 2, Em risco 1, Quase dormentes 1.

Testado via `POST /cliente2/segmentacao/processar` com `somenteContagem: true` — 37 regras
candidatas. As que rendem número visível:

| Regra testada | Clientes | % |
|---------------|---------:|--:|
| Nunca usou cupom | 13 | 86,7% |
| Comprou no Cardápio Digital | 11 | 73,3% |
| Comprou no almoço (manhã/tarde) | 12 | 80% |
| Pessoa física | 10 | 66,7% |
| Comprou à noite | 9 | 60% |
| Só um pedido na vida | 8 | 53,3% |
| 2 ou mais pedidos | 7 | 46,7% |
| Cadência ≤ 30 dias | 7 | 46,7% |
| RFV Perdidos | 6 | 40% |
| Tem cashback parado | 6 | 40% |
| Total gasto > 100 | 5 | 33,3% |
| RFV em risco de sumir | 5 | 33,3% |
| Tem endereço cadastrado | 5 | 33,3% |
| Ticket médio > 50 | 4 | 26,7% |
| 5 ou mais pedidos | 4 | 26,7% |
| Comprou no fim de semana | 4 | 26,7% |
| 1ª compra pequena e sumiu | 4 | 26,7% |
| Total gasto > 300 | 3 | 20% |
| Só à noite, nunca no almoço | 3 | 20% |
| RFV Fiéis ou Campeões | 2 | 13,3% |
| Sumidos (2+ pedidos, 30+ dias) | 2 | 13,3% |
| Já usou cupom | 2 | 13,3% |

**Dão zero neste sandbox — evitar nas capturas:** aniversariantes (qualquer janela), comprou
pelo iFood, avaliações (nota média), sem comprar há 180+ dias, comprou de madrugada, VIP por
RFV (frequência ≥ 4 e valor ≥ 4), só marketplace.

---

## 8. Onde está o código

| Camada | Caminho |
|--------|---------|
| Front (lista) | `~/refs/beefood-web-react/src/pages/FoodMarketingSegmentacaoLista.desktop.tsx` |
| Front (editor) | `src/components/segmentacao/SegmentacaoEditorModal.tsx`, `ConstrutorRegra.tsx`, `CondicaoLinha.tsx`, `ValorInput.tsx`, `SeletorCampoModal.tsx` |
| Front (rótulos) | `src/components/segmentacao/labels.ts` |
| Backend (motor) | `~/refs/beetech-server-node-2.0/src/models/segmentacao/processarSegmentacao.js` |
| Backend (catálogo) | `src/models/segmentacao/engine/campos.js` |
| Backend (avaliador) | `src/models/segmentacao/engine/avaliador.js`, `operadores.js` |
| Backend (fontes) | `src/models/segmentacao/dataSources.js` |
| Backend (modelos) | `src/models/segmentacao/modelosTop.js`, `publicosFixos.js` |
| Backend (rotas) | `src/api/routes/clienteRouter2.js`, prefixo `/cliente2/segmentacao` |
| Documentação | `~/refs/beetech-server-node-2.0/docs/segmentacao/` (API.md, schema.sql) |

### Como testar uma regra sem mexer na tela

`POST /api/cliente2/segmentacao/processar` com `{empresaID, usuarioID, regra, somenteContagem}`.
O `usuarioID` **é obrigatório no corpo** (o middleware recusa sem ele, com a mensagem
"Parâmetros empresaID e usuarioID são obrigatórios"), embora o controller só use o `empresaID`.
