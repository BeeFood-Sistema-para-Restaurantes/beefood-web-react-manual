# MEMORIA.md — Estudo completo dos grupos de acesso

Manual **#72**. Estudo de **todas** as permissões de Configuração → Usuários → Grupos de Acesso,
categorizado, com foco no efeito de cada uma na tela — e, em especial, no **cadastro de
produto**.

Última atualização: 01/09/2026.

---

## 1. O pedido

Estudo completo de todos os grupos de acesso, explicado **categorizado** para facilitar o
entendimento. O dono destacou duas coisas: (a) algumas permissões refletem direto em telas como
o cadastro de produto, outras apenas escondem telas — a explicação precisa separar os dois
casos; (b) nas restrições de produto, mostrar **exatamente como a tela fica**.

Complementa o **#13** (`manuais/caixa-restricoes/`), que cobria apenas as restrições de caixa.
No `CHECKLIST-MANUAIS.md` este assunto estava como ideia futura ("Usuários e permissões").

---

## 2. Números do levantamento

| Medida | Valor |
|--------|------:|
| Permissões na tela de Grupos de Acesso | **93** (38 itens pai + 55 sub-itens) |
| Categorias (`recurso`) | **10** |
| Chaves no `grupoAcessoUsuario` | **352** |
| Permissões que agem **dentro** de uma tela | **9** |
| Permissões que produzem **cadeado** em vez de sumiço | 6 (via `enabled` de Aplicativos) |
| Chaves `.visible` que **nenhum** switch controla | **75** |
| Grupos no sandbox | 2 (Administrador2 = 71879; Acesso Funcionário = 71880) |

---

## 3. Como o levantamento foi feito

O backend (`beetech-server-node-2.0`) **não estava clonado** nesta sessão — só o front. Sem o
código do servidor não havia como ler o mapeamento item → chave, então ele foi levantado por
**experimento em produção**, no sandbox.

**Codificação binária.** Cada uma das 93 permissões recebeu um código de 7 bits. Em 7 rodadas,
desligamos as permissões cujo bit da rodada valia 1 e lemos o `grupoAcessoUsuario` do usuário
de teste. A assinatura de bits em que cada chave ficou `false` identifica a permissão. Custou
7 rodadas em vez de 93, cerca de 18 minutos.

Detalhes que valem para qualquer experimento assim:

- **85 segundos** de espera entre o POST e a leitura. Testado: com 85 s, duas leituras espaçadas
  de 12 s deram o mesmo resultado nas 8 rodadas (0 chaves instáveis). Com menos, oscila.
- **Uma rodada de baseline** com as 93 ligadas é obrigatória: ela separa o que não depende do
  grupo. Foi assim que apareceram as três permissões que dependem da Função Gerente.
- **Não use o próprio grupo.** O experimento rodou no grupo 71880 (Acesso Funcionário), com o
  usuário `caixa.manual`. O operador continuou no Administrador2, intacto.
- **Salve o estado original antes de começar** (`/tmp/beefood/estado-original-71880.json`) e
  restaure ao final. O grupo 71880 voltou exatamente ao que era: 35 ligadas de 93.
- **O método tem um ponto cego:** chave que depende de duas permissões gera assinatura combinada
  que pode coincidir com o código de uma terceira. Aconteceu com três chaves do Desempenho, e
  cada uma foi reconferida por teste individual.

### Leitura das permissões pela API

`GET /api/empresa2/empresaConfig/{empresaID}/{usuarioID}/1` devolve o `grupoAcessoUsuario`, mas
**só do usuário do próprio token** — com o token do Principal e o `usuarioID` do restrito a
resposta é **401**. Foi preciso manter dois contextos do Playwright abertos: um logado como
Principal (para os POSTs) e um como `caixa.manual` (para as leituras).

O `config_cache` do `localStorage` e a resposta da API vêm em **base64 + zlib** (`pako.inflate`
no front). Em Python, `base64.b64decode` + `zlib.decompress` resolve.

Token no `localStorage`: `beefood_auth_token`, ofuscado com XOR pela chave
`bf2024_secure_key_token` e base64 (`src/lib/api.ts`). Para chamar a API de dentro da página,
é mais simples decodificar em JS via `page.evaluate` do que replicar em Python.

---

## 4. Achados que ninguém sabia

1. **Dados da Empresa esconde também os Parâmetros.** Confirmado por teste individual: desligar
   só essa permissão apaga `configuracao.items.empresa` **e** `configuracao.items.parametros`.
   Não existe permissão separada para Parâmetros — logo, não há como dar Parâmetros sem dar o
   cadastro da empresa.
2. **Cardápio - Exibir / Ocultar Produtos leva Rodízio e Preço Programado.** Já se sabia (do
   #69) que o Preço Programado usa a permissão `rodizio`; o que faltava era saber que o switch
   que a controla é o do Exibir / Ocultar.
3. **Copiar do iFood, Copiar de Imagem e Migrar Dados não obedecem ao grupo.** Ficaram `false`
   na rodada com as 93 permissões **ligadas**: dependem da **Função Gerente**.
4. **Os cabeçalhos de grupo do Desempenho não têm switch.** `vendas`, `produtos` e `clientes`
   ficam `false` sozinhos quando todos os relatórios de dentro estão desligados.
5. **O relatório *Entregador (Taxa / KM)* não tem permissão.** Existe no cache
   (`delivery.items.entregador`), mas não há item na tela de grupos.
6. **Nenhuma integração da tela de Aplicativos é controlável por grupo.** As 44 chaves
   `.visible` de aplicativos nunca mudaram. Só a permissão **Aplicativos** (que esconde a tela
   inteira) e alguns `enabled` (que produzem cadeado) têm efeito.
7. **As 11 abas do Cardápio Digital não têm permissão individual.** A aba **Avisos** não tem nem
   chave no JSON.
8. **Início, Meus Links, Manual e Suporte não saem do menu.**
9. **Os cabeçalhos Cadastros, Configuração e Fiscal ficam sempre visíveis** — um grupo sem
   nenhum item de Configuração ainda vê o cabeçalho, vazio.
10. **As três sub-permissões do caixa não geram chave nenhuma** no `grupoAcessoUsuario`: elas
    agem na API do caixa (é o mecanismo do #13). Ou seja, o grupo de acesso tem dois canais de
    efeito, e só um aparece no `config_cache`.
11. **`estoqueNegativo` não responde a nenhum switch**, embora o modal do produto consulte essa
    permissão para o switch *Aceita Estoque Negativo*.

---

## 5. A tela de produto — o que foi comprovado

Sete cenários montados no grupo 71880, cada um com login novo de `caixa.manual`:

| Cenário | Efeito observado |
|---------|------------------|
| todas ligadas | tela completa (referência) |
| sem **Editar (exceto preço)** | Setor, Etiqueta, Unidade e o botão de IA ficam apagados; Nome, Código, Código de Barras e Descrição **mantêm a aparência normal** e apenas deixam de aceitar digitação (`readOnly`) |
| sem **Editar Preço** | Preço de Venda e Custo viram `readOnly`; o valor continua à vista |
| sem **Editar Ativo** | chaves Ativo / Delivery / Presencial / Totem apagadas (aba **Cardápios**) e o menu `⋮` do card perde as três ações de ativação |
| sem **Excluir** | menu **OPÇÕES** sem *Excluir Produto*; `⋮` do card sem *Excluir*; setor sem lixeira |
| sem **Adicionar Novo** + **Editar em Lote** | somem **+ Novo Produto (F1)**, **+ Novo Setor** e **Editar em Lote** |
| sem **Cadastro de Cardápio** | o grupo Cardápio sai do menu e `/cardapio?tab=produtos` **redireciona para `/`** (verificado) |

**Cuidado ao planejar as capturas:** as chaves Ativo / Delivery / Presencial **não estão na aba
Produto**, e sim na aba **Cardápios**. Print da aba Produto no cenário "sem Editar Ativo" sai
idêntico ao completo. O mesmo vale para *Excluir*, que só aparece com o menu **OPÇÕES** aberto.

**Evidência objetiva além do print:** em cada cenário foi gravado um dump JSON do
`readOnly`/`disabled` de todos os `input` e `[role=switch]` do modal
(`/tmp/beefood/produto-*.json`, `/tmp/beefood/cardapios-*.json`). É o que sustenta a afirmação
de que o campo *parece* editável e não é.

---

## 6. Armadilhas de captura nesta sessão

- **O clique em "OPÇÕES" abriu a aba "Grupo de Opções".** O texto colide. Use
  `button:text-is("OPÇÕES")`.
- **Pesquisa de NPS ("Como está sendo sua experiência?") cobre a tela** depois do login do
  usuário restrito. Fecha com `button:has-text("FECHAR (ESC)")` — e pode reaparecer, então vale
  rodar a limpeza duas vezes.
- **O overlay do modal escurece a página inteira**, inclusive o menu lateral. Isso não é tema
  escuro: as capturas com modal aberto ficam com o fundo cinza mesmo em tema claro.
- **Tema claro:** `context.add_init_script` gravando `beefood-theme = 'light'` funciona e é mais
  confiável que clicar no botão de tema (que alterna, e pode deixar escuro se já estava claro).
- **A expansão dos sub-itens no modal do grupo** não sai por `svg.lucide-chevron-right`: o
  clique é no `div` do título (`onClick={() => toggleExpanded(...)}`).
- **`storage_state` regravado com permissão desligada congela o `config_cache`.** Para cada
  cenário, faça **login novo** em contexto limpo em vez de reaproveitar a sessão.

---

## 7. Ambiente

| Item | Valor |
|------|-------|
| Conta | BeeFood3 - Manual (`contato@beefood.com.br` / `1q2w3e4r`), empresaID **38311**, usuarioID **88711**, grupo Administrador2 (71879), **gerente** |
| Usuário de teste | `caixa.manual` / `manual123`, usuarioID **122583**, grupo Acesso Funcionário (71880), **não gerente** |
| Outro usuário no mesmo grupo | `atendente.parametros` (122977) — cuidado: mexer no 71880 afeta os dois |
| Produto usado nas capturas | **Combo One Burger** (R$ 28,00), setor Combos |
| Referências de código | `~/refs/beefood-web-react`; hub de relatórios clonado em `/tmp/beefood-reports-hub` |

O `/admin` aparece no menu do funcionário restrito: `podeAcessarAdmin()` usa uma **allowlist de
empresaIDs** (`src/utils/adminBeetech.ts`) e o sandbox está nela. Não é permissão de grupo e não
entra no manual.

---

## 8. Estado do grupo 71880 ao fim da sessão

Restaurado ao original (35 ligadas de 93) pelo `mapear.py restaurar`. As permissões do cardápio
foram mexidas depois, nas capturas — **conferir e restaurar** se o sandbox for reutilizado:
o estado original tinha **Cadastro de Cardápio e os seis sub-itens ligados**.

---

## 9. Scripts da sessão (em `/tmp/beefood/`, fora do repositório)

| Script | Papel |
|--------|-------|
| `login.py` | login e contexto do Playwright (tema claro forçado) |
| `api.py` | chamadas à API de dentro da página + descompressão base64/zlib |
| `dump_grupos.py` | árvore completa dos dois grupos |
| `dump_cache.py` | `config_cache` decodificado |
| `mapear.py` | rodadas binárias + `restaurar` |
| `analisar.py` | reconstrói permissão → chaves |
| `confirmar.py` | testes individuais das suspeitas |
| `tabelas.py` | gera as tabelas do catálogo |
| `capturar_config.py` | telas da tela de grupos |
| `capturar_produto.py` / `capturar_produto2.py` | cenários da tela de produto |
| `capturar_menu.py` | menu lateral com e sem o Cardápio |
