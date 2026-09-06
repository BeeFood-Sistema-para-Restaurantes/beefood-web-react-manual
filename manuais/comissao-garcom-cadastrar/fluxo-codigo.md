# Fluxo de código — #83 Comissão do garçom: cadastrar e lançar

Documento interno: **não publicar**.

## Onde vive

| Caminho | Rota | Componente |
|---------|------|------------|
| Cadastros → Funcionários | `/cadastro-funcionarios` | `CadastroFuncionarios.tsx` + `ModalEditarFuncionario.tsx` |
| Configuração → Usuários | `/usuarios` | `ModalEditarUsuario.tsx` |
| Mesas → Novo Pedido | `/mesas` | `ModalPedidos` + `PedidoFields` |

Aba Função: radio `garcom` revela `#comissao` (0–100). API `POST /datasnap/rest/empresa2/funcionario`.

Não existe `comissao` no cadastro de produto. A linha do item no pedido carrega
`comissao` (%) e `comissaoValor` (R$) a partir do funcionário identificado.

## Quem identifica o garçom

`pedidoBuilder` grava `mesa.funcionarioID` com
`funcionarioIDOperador ?? userSession.funcionarioID`.

`PedidoFields` pré-preenche `garcomSelecionado` com `funcionarioIDEfetivo` (login ou
operador). Escolher o nome na mesa **sem** estar logado como ele / sem operador **não**
gera comissão — confirmação do dono em 06/09/2026.

Três origens válidas: app do garçom; usuário com `funcionarioID`; código do operador
(`operadorPDV`). Manual do operador: #42, slug `parametros-codigo-operador`.

## Atalho F2 no usuário

`ModalEditarUsuario` **não** escuta F2. O botão diz SALVAR (F2), mas só o clique grava.
O modal de funcionário escuta F2 de verdade.

## Relatório (prova)

Desempenho iframe `https://relatorios.beefood.com.br` →
`presencial-pedidos-mobile`. API
`GET /api/relatorio2/relatorioMobileComissao/{empresa}/{início}/{fim}/{horaIni}/{horaFim}`.
Componente `RelatorioPedidosMobile.tsx` (reports-hub). Filtro padrão situação RECEBIDO.

## Help

Registrar em `help-manuais.ts`:

- `/cadastro-funcionarios` → slug `comissao-garcom-cadastrar`
- `/mesas` → acrescentar o mesmo slug
- `/desempenho` → `relatorio-comissao-garcom` e `relatorio-taxa-servico`
