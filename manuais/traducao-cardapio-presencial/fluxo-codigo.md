# fluxo-codigo.md — #100 Tradução do cardápio presencial

Mapeamento técnico (leitura de `beefood-web-react`, `git pull` em 16/09/2026 —
`bdb7106`). A tradução nasceu nos commits de 10/09 (`da3049d`) e 13/09
(`de63fe5`).

## Peça central

`src/components/cardapio/BandeiraIdioma.tsx` — arquivo novo, concentra tudo:

| Export | Papel |
|--------|-------|
| `IdiomaTraducao` | `'pt' \| 'en' \| 'es'` |
| `TraducaoCardapio` | `Record<idioma, Record<chave, texto>> \| null`. **O português fica fora do objeto** |
| `IDIOMAS` | rótulos *Português / Inglês / Espanhol* (viram `aria-label` das bandeiras) |
| `temTraducaoContratada()` | `qtdAA > 0 \|\| qtdTablet > 0` no `config_cache` — é o que faz as bandeiras existirem |
| `valorTraduzido(t, idioma, chave)` | leitura; `pt` devolve `''` (o formulário usa o campo real) |
| `definirValorTraduzido(...)` | escrita imutável: campo vazio sai do JSON, idioma sem campo some, objeto vazio vira `null` |
| `idiomaTemConteudo(...)` | a **bolinha verde** na bandeira |
| `SeletorIdiomaTraducao` | as três bandeiras (SVG inline — emoji de bandeira vira "BR"/"US" no Chrome do Windows) |
| `RotuloIdiomaAtivo` | etiqueta *Inglês* / *Espanhol* ao lado do rótulo do campo |
| `CLASSE_CAMPO_TRADUZIDO` | `border-primary/60 ring-1 ring-primary/30` — a borda destacada |
| `parseTraducao` | aceita objeto **ou** string JSON (bases antigas) |

Trocar de bandeira é só troca de visão sobre o mesmo `formData`: não salva,
não descarta. O salvamento é o do cadastro (`SALVAR E SAIR (F2)`), que manda
`traducao` no mesmo payload.

## Onde aparece

| Tela | Campo (rótulo) | Chave no JSON | Arquivo |
|------|----------------|---------------|---------|
| Setor | Nome Interno do Setor (`titulo`) | `setor` | `ModalEditarSetor.tsx` |
| Produto | Nome (`nome`) | `descricao` | `ModalEditarProduto.tsx` |
| Produto | Descrição (`descricao`) | `descritivo` | `ModalEditarProduto.tsx` |
| Complemento | Nome / Descrição (mesmo modal, `isComplemento`) | `descricao` / `descritivo` | `ModalEditarProduto.tsx` |
| Grupo de opções | Nome do Grupo de Opção (`descricao`) | `descricao` | `ModalEditarGrupoOpcao.tsx` |
| Produto no painel mobile | Nome / Descrição | idem | `mobile/cardapio/MobileEditarProdutoPage.tsx` |

Detalhes que valem para o manual:

- O seletor de bandeiras aparece **uma vez por modal** (ao lado do Nome / do
  título). O idioma escolhido vale para todos os campos traduzíveis daquele
  cadastro — no produto, Nome **e** Descrição trocam juntos.
- `placeholder` durante a tradução = o texto em português (`formData.nome`,
  `formData.descricao`). É o "texto apagado dentro do campo".
- `useEffect(() => setIdiomaEdicao('pt'), [isOpen, produtoID])`: ao abrir
  outro cadastro a visão volta para o português.
- **Sub-setores não têm tradução** (só a chave `setor`, do título).
- **Nome Público do setor (`tituloWeb`) não tem tradução.**
- **Editar em Lote não tem o campo** — nenhum arquivo de lote importa
  `BandeiraIdioma`.
- `handleMelhorarDescricaoIA` (`useEditarProdutoLogic.ts`) lê e grava
  `formData.descricao`, ou seja o **português**, mesmo com a bandeira do
  inglês selecionada. O botão reescreve o cadastro, não traduz.

## Persistência

Payload dos três POSTs (só inclui `traducao` quando `temTraducaoContratada()`):

- Setor: `POST /api/produto2/cardapio/setor` (`useSalvarSetor.ts`)
- Produto/complemento: `useSalvarProduto.ts`
- Grupo: `POST /api/produto2/cardapio/grupoOpcao` (`useGrupoOpcaoDetalhes.ts`)

Leitura vem nos **detalhes**, não nas listagens:

| Rota | Devolve `traducao`? |
|------|---------------------|
| `GET /api/produto2/cardapio/setor/{empresa}/{usuario}/{setorID}` | sim |
| `GET /api/produto2/cardapio/produto/{empresa}/{usuario}/{produtoID}` | sim |
| `GET /api/produto2/cardapio/grupoOpcao/{empresa}/{usuario}/{grupoID}` | sim |
| `GET /api/produto2/cardapio/setores/...`, `cardapio2/cardapio`, `cardapio2/grupoOpcoes` | **não** (listagens ignoram o campo) |

Exemplo real gravado no sandbox (16/09/2026):

```json
{ "en": { "descricao": "Breaded Onion Rings",
          "descritivo": "Portion with 8 breaded onion rings" },
  "es": { "descricao": "Aros de cebolla empanizados",
          "descritivo": "Porción con 8 aros de cebolla empanizados" } }
```

## Totem

`src/components/tef/TotemConfigModal.tsx` — aba **Configuração**, grupo
**Idiomas**, `CheckRow` **Habilitar tradução** (`aaTraducao`). O texto de
apoio do próprio produto é a fonte da regra de fallback:

> "Exibe as bandeiras de idioma no totem. O cliente escolhe entre português,
> inglês e espanhol. Produto ou setor sem tradução cadastrada continua
> aparecendo em português."

O modal **salva sozinho** (`update()` chama `persist()` a cada clique, como
Parâmetros). Ele só abre pelo card do Totem em `Aplicativos` quando
`qtdAA > 0`; abaixo disso o card abre a modal informativa de venda.

**Não existe interruptor equivalente para o tablet** no painel — nenhuma
tela de `cardapio-digital-tablet/` importa `BandeiraIdioma` nem tem campo de
idioma. O aplicativo do tablet (`com.cardapiodigitalmesacomanda`) não está
acessível no Cloud Agent, então o manual não afirma nada sobre a tela dele
além do que o cadastro alimenta.

## Fora de escopo (checado, não é tradução)

`statusTraduzido` em `useGrupoOpcoesCardapio.ts` / `ProdutoGrupoOpcoesTab.tsx`
é o rótulo da **formação de preço** (Normal, Brinde, Valor da Maior,
Proporcional). Nada a ver com idioma.
