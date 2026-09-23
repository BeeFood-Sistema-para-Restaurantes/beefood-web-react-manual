# MEMÓRIA — #120 Painel para Entregadores

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `painel-entregador.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Status: **concluído** em 19/09/2026. Pasta `manuais/painel-entregador/`, 4 imagens.
O estudo do código está em [`fluxo-codigo.md`](fluxo-codigo.md).

## Pedido do dono

> *"Acabamos de criar uma nova funcionalidade painel do entregador, é uma tela para
> acompanhamento dos entregadores. A ideia é que o restaurante disponibilize essa tela na
> área aonde os entregadores chegam e assim eles podem saber o status dos pedidos que eles
> vieram coletar, se está em preparo ou já ficou pronto. Evita ter que ficar se
> comunicando, ainda mais em alta demanda. Para esse teste, faça smoke testes inserindo
> pedidos na empresaID 38311 do iFood, Keeta, 99Food e cardápio digital, para que eles
> apareçam no painel em preparo e alguns pronto. O manual é simples e direto, não ensina
> criar pedidos, só mostra a visão. A ideia é documentar a mentalidade e também SEO para
> nosso MCP tirar dúvidas nesse sentido caso alguém pergunte. O app pode ser aberto pela
> tela delivery ou por /aplicativos."*

Depois, duas correções de rota: *"o smoke test deve ter pedidos da 99Food, iFood, Keeta e
Aiqfome, além do cardápio digital… não precisamos de muitos prints pra explicar essa
tela"* e *"você precisa consultar o banco de dados com smoke test pra ver como criar
pedidos desses marketplaces e depois fazer scripts manuais para inserir eles no banco de
dados… crie uma skill sobre isso ao finalizar."*

Por isso o manual tem **4 imagens** e não 9, e por isso saiu a skill
[`cenario-sandbox`](../../.cursor/skills/cenario-sandbox/SKILL.md).

## O achado que custou a sessão inteira

**`origem` não é campo de entrada de nenhuma rota — ela é derivada do identificador de
plataforma que o pedido carrega.** A tabela, os ensaios e a prova estão em
[`fluxo-codigo.md`](fluxo-codigo.md#achado-do-estudo-da-base-origem-é-derivada-não-digitada).

O caminho até lá, porque o erro é fácil de repetir:

1. Tentar `venda2/salvar` com os campos de marketplace. Nasce pedido, mas `origem` sai
   **Manual**. (`exp_origem.py`)
2. Farejar a rede do cardápio público e achar `tmesa/pedido`, que grava origem diferente.
   Só que ela fixa **Cardápio Digital**, e pede o `Authorization: Basic` do cardápio — sem
   ele, 401. (`pedido_cardapio.py`, `pedido_marketplace.py sondar`)
3. Procurar rota de integração: seis rotas de atualização não gravam identificador nenhum,
   e quinze nomes de rota nova dão 404. (`exp_ids.py`, `exp_rotas_erp.py`)
4. Ler a lista branca de colunas do `smoke-app.js` do bloco anterior e perceber que
   `origem` **não está nela** — e ainda assim aqueles pedidos aparecem como iFood.

## Como o cenário se monta

```bash
python pedido_marketplace.py semear     # cria os pedidos-base pelo tmesa/pedido
node   marketplace-db.js estampar --pedidos <ids> --gravar   # estampa o identificador
python smoketeste.py preparo|pronto <preVendaID>             # o painel só olha essas duas
python pedido_marketplace.py estado     # o que o painel enxerga agora
```

O `marketplace-db.js` só grava com `--gravar`, só nas colunas da lista branca, só na filial
39202 e só em pedido com o marcador `[SMOKE-PAINEL]` em `Observacoes`. Sem `--gravar` ele
imprime o `UPDATE` — e `plano` mostra o SQL de todos os canais **sem conectar em nada**,
que é como ele foi conferido nesta máquina.

**Nesta sessão o banco não foi alcançado.** `BITBUCKET_TOKEN` e
`BITBUCKET_CARDAPIO_DIGITAL` estão os dois inválidos (`Token is invalid, expired, or not
supported for this endpoint`), o clone do backend não existe e é nele que moram host e
senha do MSSQL. Quem estampou os pedidos de iFood, 99Food e Keeta do print foi **o dono**,
na máquina dele. Por isso o script passou a aceitar também
`BEETECH_MSSQL_HOST/_USER/_PASSWORD/_DATABASE`: assim ele deixa de depender do Bitbucket.

## Cenário no ar em 19/09/2026

| Coluna | Pedidos |
|---|---|
| EM PREPARO | iFood `#1133`, 99Food `#1135`, Keeta `#1137`, Cardápio Digital `#65` (atrasado, em vermelho) |
| PRONTO | iFood `#1134`, 99Food `#1136`, Keeta `#1138` |

O cartão vermelho do `#65` é proposital: ele é o único com prazo estourado, e é ele que
prova o alerta de atraso. O prazo da sandbox é `deliveryTempoEntregaMinutosMax = 53`, então
amarelo ~37 min, laranja ~45 min, vermelho depois de 53 min (`prazo.py` faz essa conta).

**AIQFome ficou de fora do print.** O canal está pronto no `marketplace-db.js` e no
`pedido_marketplace.py`, mas o lote estampado não incluiu um. Não faz falta no manual: o
texto fala de canais no plural e o ícone segue a mesma regra.

## Capturas

| Imagem | O que mostra | Setas |
|---|---|---|
| `01-painel-completo.png` | o painel inteiro, as duas colunas, os quatro canais e o cartão atrasado | 7 |
| `02-abrir-pela-tela-delivery.png` | o ⋮ do cabeçalho do Delivery e o item **Painel Entregador** | moldura + 1 |
| `03-abrir-por-aplicativos.png` | o card em Aplicativos e o botão **ABRIR PAINEL (F2)** | 2 |
| `04-detalhe-do-pedido.png` | o detalhe do pedido, só leitura | 4 |

Três armadilhas de captura que o `capturar.py` resolve, e que valem para qualquer manual:

- **Tema.** Ler `html.class` logo depois do `goto` às vezes diz `light` numa tela que ainda
  vai virar escura — a classe só se firma depois da hidratação. O jeito determinístico é
  gravar `localStorage.theme = 'light'` e **recarregar**.
- **O ⋮ do Delivery.** São 28 botões com o mesmo ícone na tela; o do cabeçalho é o de
  **menor `y`**. Pegar `.last` abre o menu de um cartão, e o print sai com *Alterar
  Situação / Alterar Entregador* em vez do menu certo.
- **Cobrir nome e telefone.** A varredura tem de ser por **nó de texto**, não por elemento
  folha: no detalhe do pedido o nome divide a caixa com o ícone de pessoa, e a busca por
  folha mediu **0 cobertos** numa tela que mostrava o nome. Quem diz o que cobrir é a
  própria API — os `nome` de `venda2/delivery`.

## Ambiente: o que foi alterado

- Pedidos criados na sandbox 38311/39202 com o marcador `[SMOKE-PAINEL]`, todos de
  delivery. `smoketeste.py limpar` reconhece o marcador novo e o antigo
  (`[SMOKE-PAINEL-ENTREGADOR]`, do primeiro lote).
- Pedido `59616164` foi para **AGUARDANDO** para tirar da foto um cartão antigo.
- Nada foi finalizado nem cancelado. **Pedido estampado nunca deve ser finalizado pelo
  app**: identificador de plataforma que não existe do outro lado faz a baixa tentar avisar
  o marketplace de verdade.
