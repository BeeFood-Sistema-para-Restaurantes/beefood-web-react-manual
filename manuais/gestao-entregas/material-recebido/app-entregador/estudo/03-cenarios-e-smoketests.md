# Cenários e smoketests — desenho proposto

Como cada capítulo do manual vai ser montado, conferido e reexecutado. Nada aqui foi executado
ainda: o `cenario-entregador.js` não existe, e o único comando desta página que já rodou foram os
dois `GET` de conferência da §4.

Alvo único: **empresa 38311 / filial 39202**, usuário **88711**, entregador **194115**
(`BeeFood3 - Manual`).

---

## 1. O ciclo de um capítulo

```
1. limpar          node scripts/cenario-entregador.js --limpar
2. semear          node scripts/cenario-entregador.js --<cenário do capítulo>
3. conferir        GET /api/entrega2/gestao/entregador/38311/39202/88711/194115
4. operar          adb: dump da tela → toque → digitação
5. capturar        adb shell screencap + adb pull → prints/NN-nome.png
6. explicar        NN-nome.md, um por print
7. costurar        manual.md do capítulo
8. registrar       smoketests/NN-<capítulo>.md — roteiro reexecutável
```

O passo 3 existe para separar dois tipos de falha que se parecem na tela do celular: "o cenário
não foi criado" e "o app não mostrou o cenário". Conferir o payload antes de olhar o app resolve
isso em dez segundos em vez de meia hora.

---

## 2. Os cenários, capítulo por capítulo

| Cenário | Comando proposto | Estado que produz | Capítulos |
|---|---|---|---|
| Vazio | `--limpar` | `pedidos: 0`, `rotas: 0` | 01, 02, 03 (tela vazia), 15 |
| Avulsos | `--avulsos 3` | 3 pedidos sem rota, um deles `PRONTO` | 03, 04, 05 |
| Muitos avulsos | `--avulsos 5` | habilita o botão **MELHOR ROTA GOOGLE MAPS (5)** | 07 |
| Rota | `--rota 3` | 3 pedidos + rota associada ao 194115, **não despachada** | 06 |
| Destaque | `--avulsos 1 --destaque` | um item e uma opção marcados, para a folha de confirmação | 04 |
| Troco previsto | `--avulsos 1 --troco 50` | rodapé com a coluna **TROCO** preenchida | 04, 11 |
| Pago | `--avulsos 1 --pago` | `saldo 0` → o app mostra **FINALIZAR** e **Pedido já pago** | 11, 13 |
| Parcial | `--avulsos 1 --parcial` | metade paga → bloco **JÁ REGISTRADO** e saldo menor | 11 |
| iFood | `--avulsos 1 --marketplace ifood` | habilita **CONFIRMAR ENTREGA IFOOD** | 09 |
| 99Food | `--avulsos 1 --marketplace 99food` | habilita **CONFIRMAR ENTREGA 99FOOD** | 10 |
| Entregue | `--avulsos 1 --entregar` | popula o histórico do dia | 14 |
| Código de barras | `--avulsos 1` + o `preVendaID` impresso pelo script | o número que o código de barras precisa codificar | 08 |

Três destes dependem de coisas que eu preciso **medir antes de escrever o script**, e não vou
supor:

1. **`--marketplace`** — o nome exato das colunas de `_PreVenda` que alimentam `ifoodLocalizer`,
   `ifoodLocalizador`, `nnID` e `nnLocator` no payload do app. Confiro por
   `INFORMATION_SCHEMA.COLUMNS` e pelo próprio `GET` depois de gravar.
2. **`--troco`** — o app extrai o troco do texto de `tipoPagStr` ("troco para …"). O formato
   exato que ele reconhece sai da leitura do `Detalhes.js`, não de tentativa.
3. **`--pago` / `--parcial`** — lançar pagamento significa passar pela mesma escrita do PDV, que
   **exige caixa aberto** e **lança no caixa real**. Esses dois cenários ficam bloqueados até a
   decisão 2 do estudo.

---

## 3. Os scripts propostos

### 3.1 `beetech-server-node-3.0/scripts/cenario-entregador.js`

Casca fina sobre o que existe. Reusa `semearLote` e `promoverSituacao` do
`seed-gestao-entregas.js`, os models de rota do `gestaoEntrega/` e as conexões já configuradas —
nada de segunda implementação, pelo mesmo motivo que o servidor não criou uma segunda porta de
escrita de pagamento: duas versões da mesma regra divergem na primeira correção feita em um lado
só.

Regras que ele herda e mantém:

- **lista branca literal `38311/39202`**, `--empresa` e `--filial` obrigatórios;
- marcador `[SEED-ENTREGAS]` na observação de toda venda criada, que é o que permite a limpeza
  seletiva;
- `--dry-run` que mostra o que faria sem escrever nada.

E uma regra nova, que o manual exige: ao fim de cada execução ele **imprime o `preVendaID`, o
`numeroPedido`, o endereço e o valor de cada pedido criado**, porque são esses números que
aparecem nos prints e que o texto do manual precisa citar.

### 3.2 `beetech-server-node-3.0/scripts/abrir-caixa-teste.js`

Só se a decisão 2 for "sim". Confere se há caixa aberto na filial, abre se não houver, e imprime
o `caixaID`. Fecha nada: fechar caixa é operação de loja, e um script que fecha caixa é uma arma
carregada apontada para o financeiro de uma filial real.

### 3.3 Helpers de emulador, em `smoketests/`

| Arquivo | O que faz |
|---|---|
| `capturar.ps1` | `screencap` + `pull` com nome sequencial na pasta do capítulo. Existe porque `adb exec-out screencap -p > arquivo` **corrompe o PNG no PowerShell** |
| `elementos.ps1` | `uiautomator dump` + lista de nós clicáveis com texto e coordenada do centro — para eu tocar por nome, não por pixel adivinhado |
| `preparar-emulador.ps1` | locale pt-BR, densidade/tamanho de tela estáveis entre capturas, e conferência de que o app está instalado e o Metro respondendo |

O `preparar-emulador.ps1` tem um propósito além da conveniência: **prints de tamanhos diferentes
entre capítulos deixam o manual com cara de colagem.** Fixar o estado do emulador uma vez é mais
barato que recortar imagem depois.

---

## 4. Conferências de leitura que já funcionam

Estas duas rodaram e são a base do smoketest de ambiente. São leitura pura, sem efeito:

```powershell
# 1) o login existe e devolve o contexto que todas as URLs exigem
$h = @{ Authorization = ('Basic ' + [Convert]::ToBase64String(
        [Text.Encoding]::ASCII.GetBytes('beetech:1q2w3e4r'))); 'app-name' = 'bee-entregador' }
$b = @{ usuario = 'contato@beefood.com.br'; senha = '1q2w3e4r' } | ConvertTo-Json
Invoke-RestMethod -Method Post -ContentType 'application/json' -Headers $h -Body $b `
  -Uri 'https://app.beetechapi.be/datasnap/rest/tusuario/validaBeeEntregador'
# → usuarioID 88711, empresaID 38311, filialID 39202, funcionarioID 194115, "BeeFood3 - Manual"

# 2) o que o app vai ver na lista de entregas, antes de abrir o app
Invoke-RestMethod -Headers $h `
  -Uri 'https://app3.beetechapi.be/api/entrega2/gestao/entregador/38311/39202/88711/194115'
# → em 17/09: pedidos = 0, rotas = 0
```

O segundo comando é o passo 3 do ciclo (§1) e vale para todo capítulo: se o pedido não está aqui,
não vale abrir o app.

---

## 5. Formato do roteiro de smoketest

Um `.md` por capítulo, em `smoketests/`, com esta forma — curta de propósito, para ser seguida
por outra pessoa sem ler o estudo:

```markdown
# Smoketest 06 — Rota

Pré-condição: emulador ligado, app instalado, sessão do contato@beefood.com.br.

## Cenário
node scripts/cenario-entregador.js --empresa 38311 --filial 39202 --rota 3

## Conferência
GET .../gestao/entregador/38311/39202/88711/194115
Esperado: rotas[0].qtdParadas = 3, despachada = false, pedidos[].rotaID preenchido.

## Passos
| # | Ação no app | Esperado |
|---|---|---|
| 1 | Abrir a aba Entregas | Cabeçalho "ROTA {código}", "0 de 3 entregues", botão INICIAR ROTA |
| 2 | Tocar INICIAR ROTA | Abre o Google Maps com as 3 paradas na ordem |
| 3 | Voltar ao app | O botão virou ABRIR NO MAPS e aparece "em rota" |

## Limpeza
node scripts/cenario-entregador.js --empresa 38311 --filial 39202 --limpar
```

---

## 6. Riscos deste desenho

1. **Escrita em produção.** É o risco de fundo de tudo (§1.1 do estudo). A lista branca é a única
   trava, e ela é literal no código do script.
2. **Baixa dispara efeito externo.** Finalizar entrega move o pedido no ERP e avisa cliente e
   marketplace. Nos pedidos semeados o telefone do cliente é nulo e não há ID de marketplace —
   então nem WhatsApp nem marketplace saem. **O cenário de marketplace fake rompe essa garantia**,
   e é por isso que a decisão 3 propõe finalizar aqueles dois pedidos por script com a notificação
   desligada.
3. **Pagamento entra no caixa real.** Com o `funcionarioID` 194115 assinando cada lançamento, o
   que é bom para a conciliação: o manual lista valor, hora e forma de cada pagamento de teste.
4. **WhatsApp ao entregador.** Associar rota ao 194115 enfileira a mensagem de nova entrega para o
   telefone da própria loja de teste. Um WhatsApp por rota criada, esperado.
5. **A UI pode não ser navegável por `adb` em dois pontos** — campo de valor com teclado e o site
   do parceiro dentro da WebView. Onde travar, eu aviso em vez de insistir.
6. **Repetir captura depois de mudança de código.** Se o app mudar durante o trabalho, os prints
   do capítulo afetado envelhecem. O roteiro de smoketest é o que torna recapturar barato — é uma
   das razões de ele existir.
