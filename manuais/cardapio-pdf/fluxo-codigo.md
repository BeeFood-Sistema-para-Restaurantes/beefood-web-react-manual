# Fluxo de código — Gerar Cardápio em PDF (#102)

Referência interna. Nada daqui vai para o manual do usuário.

## Onde fica

| Caminho | Arquivo |
|---------|---------|
| Menu lateral **Cardápio → Cardápio em PDF** (rota `/cardapio-pdf`) | `src/pages/CardapioPdf.tsx` + item em `src/components/AppSidebar.tsx` |
| Atalho **Gerar cardápio em PDF** no menu de ações da tela Cardápio | `src/pages/Cardapio.tsx` (desktop) e `src/components/mobile/cardapio/MobileCardapioPage.tsx` (celular) → `ModalCardapioPdf` |
| Editor (as 4 etapas + prévia) | `src/components/cardapio-pdf/CardapioPdfEditor.tsx` |
| Etapas | `steps/StepItens.tsx`, `steps/StepLayout.tsx`, `steps/StepMarca.tsx` |
| Documento PDF | `components/cardapio-pdf/CardapioPdfDocument.tsx` (`@react-pdf/renderer`) |
| Prévia em canvas | `components/cardapio-pdf/PreviewPdf.tsx` (`pdfjs-dist`) |
| Modelos | `components/cardapio-pdf/templates/registry.ts` |
| Estado do projeto | `hooks/useCardapioPdfProjeto.ts` |
| Dados dos cardápios | `hooks/useCardapiosPdfDados.ts` |
| Fotos dos produtos | `hooks/useImagensPdf.ts` + `utils/imagemParaDataUrl.ts` |
| Modelo de dados e helpers | `utils/cardapioPdfModel.ts` |
| Liberação por empresa | `utils/cardapioPdfAcesso.ts` |

## Liberação (importante para o manual)

```ts
// utils/cardapioPdfAcesso.ts
const CARDAPIO_PDF_EMPRESAS = [38311];
export const podeUsarCardapioPdf = () =>
  isDevelopment || CARDAPIO_PDF_EMPRESAS.includes(Number(getUserSession()?.empresaID));
```

`podeUsarCardapioPdf()` esconde o item do menu (`AppSidebar`), o atalho do menu de
ações e protege a rota (`App.tsx` redireciona para `/cardapio`). Em produção só as
empresas da lista veem o gerador — por isso o manual diz que o recurso está em
liberação e que o item pode não aparecer. A rota também passa por
`ProtectedRoute submenuKey="cardapio" submenuItemKey="produtos"`, ou seja, segue a
permissão de **Produtos** do grupo de acesso.

Tanto a página cheia quanto o modal carregam o editor com `lazy()` — o pacote do
`@react-pdf/renderer` + `pdfjs` fica fora do bundle principal.

## Dados que alimentam o PDF

`useCardapiosPdfDados` busca, para cada filial selecionada, dois endpoints já
existentes:

```
GET /datasnap/rest/produto2/cardapio/setores/{empresaID}/{filialID}/{usuarioID}
GET /datasnap/rest/produto2/cardapio/produtos/{empresaID}/{filialID}/{usuarioID}
```

`montarSecoes()` (em `cardapioPdfModel.ts`) monta as seções:

- só setores marcados (`setoresSelecionados`, chave `filialID:setorID`);
- só produtos **ativos** (`p.ativo`) e não ocultados (`produtosOcultos`);
- seção sem item sobra fora do PDF;
- ordem vem de `ordemSetores` / `ordemProdutos` (arrastar na etapa 1);
- nome/descrição/preço aceitam `overrides[produtoID]` — só no impresso, nada é
  gravado no cadastro;
- imagem = `p.s3Link`.

Preço conforme `origemPreco` (`precoDoProduto`):

| Opção na tela | Campo |
|---------------|-------|
| Preço presencial (padrão) | `vendaPresencial ?? venda` |
| Preço delivery | `vendaDelivery ?? venda` |
| Preço de venda (padrão) | `venda` |
| Tabela de preço | `valorFinalPresencial ?? valorFinal` da tabela; cai no presencial se o produto não estiver nela |

## Preenchimento automático (etapa 3)

O `CardapioPdfEditor` semeia a marca com o que já está cadastrado:

- **nome** ← `userData.nomeFantasia`;
- **logo** ← `filial.logo`, convertida em dataURL e achatada sobre a cor de fundo
  (`imagemParaDataUrl`, senão PNG transparente sai preto no PDF). `logoRemovida`
  impede que ela volte sozinha depois de o usuário remover;
- **telefone/endereço** ← `useEmpresaFilialDetalhes`;
- **redes** ← Instagram/Facebook de `useCardapioDigitalConfiguracoes`;
- **QR Code** ← sempre `https://presencial.beefood.com.br/{linkAcesso}` (campo
  somente leitura).

O canvas do QR (`qrcode.react`) vive **dentro do `StepMarca`**, escondido. O
`qrCodeDataUrl` só é gerado quando a etapa 3 é montada — quem pula da etapa 1 direto
para o download (F2) baixa a capa sem o quadradinho. O manual avisa: passe pela etapa
3 antes de baixar.

## Estado não é salvo

`useCardapioPdfProjeto` guarda tudo em `useState` (`projetoPadrao()`), sem
localStorage nem backend: **fechar o gerador zera as escolhas**. `semearSetores()`
marca todos os setores na primeira vez que um cardápio entra; `reiniciar()` é o botão
*Recomeçar do zero*.

## Documento (CardapioPdfDocument)

- Capa opcional (`capaAtiva`) com 4 layouts (`centralizada`, `imagemInteira`,
  `faixa`, `minimalista`) e chaves `capaMostrar*`.
- Cabeçalho `fixed` (repete em toda página) quando `mostrarCabecalho`.
- Rodapé `fixed` com `rodape || nome` e `pageNumber / totalPages` quando
  `mostrarNumeroPagina`.
- Colunas = `projeto.colunas || TEMPLATES[template].config.colunas`.
- `precoAbaixo = comFoto || colunas >= 3` — com foto ou 3 colunas o preço desce para
  baixo do nome; sem foto e com 1–2 colunas ele vai na mesma linha, com a guia
  pontilhada dos modelos `classico`/`quadro`.
- `minPresenceAhead` no título do setor evita título órfão no fim da página.
- `Font.registerHyphenationCallback` desliga a quebra de palavra com hífen.
- Fontes: Helvetica (sem serifa), Times (com serifa), Courier (máquina de escrever).
- `paginaPorCardapio` só vale com 2+ cardápios; `paginaPorSetor` quebra por setor.

Modelos (`registry.ts`):

| id | Nome | colunas | foto | guia | fonte do título |
|----|------|---------|------|------|-----------------|
| `classico` | Clássico | 2 | não | sim | sans |
| `elegante` | Elegante | 1 | não | não | serif (título centralizado) |
| `fotografico` | Fotográfico | 2 | **sim (obrigatória)** | não | sans |
| `compacto` | Compacto | 3 | não | não | sans |
| `quadro` | Quadro | 2 | não | sim | serif + paleta escura sugerida |

`mostrarFotos` começa **ligado** no `projetoPadrao()`: o Clássico sai com foto até
alguém desligar o switch. Só o Fotográfico obriga a foto (switch desabilitado).

## Fotos

`useImagensPdf` converte cada `s3Link` em dataURL JPEG via canvas
(`imagemParaDataUrl`, recorte central quadrado de 600 px, proxy `images.weserv.nl`
quando o CORS bloqueia). Foto que não carrega é ignorada — o item sai sem imagem. O
subtítulo do editor mostra "carregando fotos..." enquanto isso.

## Download

`CardapioPdfEditor.baixarPdf()` gera o blob com `pdf(<CardapioPdfDocument/>).toBlob()`
e dispara um `<a download>` com o nome `cardapio_<nome_slug>.pdf`. Sucesso → toast
"Cardápio em PDF gerado."; erro → "Não foi possível gerar o PDF. Tente novamente.".
No desktop, **F2** baixa e **ESC** fecha.

## Prévia

`PreviewPdf` gera o mesmo documento e desenha página por página com `pdfjs` num
canvas reaproveitado (escala máx. 1.3, JPEG 0.82). Enquanto isso mostra o skeleton
"Montando a prévia...". Mudança de texto é debounced em 400 ms; mudança de estrutura
(modelo, colunas, fotos) refaz na hora. Se alguma foto quebra, a prévia é remontada
sem imagens.

## Medidas observadas no ambiente de teste (empresa 38311)

| PDF | Páginas | Tamanho |
|-----|---------|---------|
| Clássico com fotos (68 itens, 8 seções) | 5 | 4,4 MB |
| Clássico só texto (mesmos itens) | 4 | 57 KB |
| Fotográfico | 6 | 4,4 MB |
| Quadro | 6 | 4,4 MB |
