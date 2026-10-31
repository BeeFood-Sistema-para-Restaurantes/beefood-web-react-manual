# fluxo-codigo.md — #131 Código de ativação de aparelho (Dispositivos)

> **Não publicar** — material interno. Leitura do `beefood-web-react` em 24/10/2026
> (`54473da`), na cópia de referência `~/refs/beefood-web-react`.

## Onde a tela mora

| Peça | Arquivo |
|---|---|
| Rota `/dispositivos` | `src/App.tsx` (`<Route path="dispositivos" element={<Dispositivos />} />`) |
| Item do menu | `src/components/AppSidebar.tsx`, em `configuracaoSubItems`, entre *Histórico Alteração* e *Caixa*, com `isNew: true` |
| Página | `src/pages/Dispositivos.tsx` |
| Janela de ativação | `src/components/dispositivos/ModalAtivarDispositivo.tsx` |
| Lista e cartão do código | `src/components/dispositivos/ListaDispositivos.tsx` |
| Dados e escrita | `src/hooks/useDispositivos.ts` |
| Acompanhamento do código | `src/hooks/useStatusPareamento.ts` |
| Catálogo dos tipos | `src/data/dispositivosCatalogo.ts` |
| Regras puras | `src/utils/dispositivosGestao.ts` |
| Tipos | `src/types/dispositivo.ts` |

O item do menu **não tem `permissionKey`**: quem vê o grupo *Configuração* vê *Dispositivos*.
A única permissão da tela é `configuracao/tef`, e ela governa só a faixa do TEF
(`podeMexerTef` / `podeAdicionarTef`).

## A API

Uma leitura e um punhado de escritas, todas em `/api/dispositivos2`:

| Operação | Chamada |
|---|---|
| Carregar a tela | `GET /api/dispositivos2/{empresaID}/{usuarioID}` → `{ cotas, dispositivos, pareamentosAbertos }` |
| Gerar o código | `POST /api/dispositivos2/pareamento` com `{ empresaID, usuarioID, usuario, tipo }` |
| Acompanhar o código | `GET /api/dispositivos2/pareamento/{pareamentoID}/status` a cada 2 s, só enquanto a janela está aberta |
| Cancelar o código | `POST /api/dispositivos2/pareamento/cancelar` com `{ …, pareamentoID }` |
| Remover aparelho | `POST /api/dispositivos2/remover` com `{ …, dispositivoID }` |
| Renomear aparelho | `POST /api/dispositivos2/atualizar` com `{ …, dispositivoID, apelido }` |

Dois códigos de status viram caminho de tela, e não erro:

- **409** em `pareamento` → `semVaga`, que desenha a tela de limite com **CONTRATAR MAIS**;
- **404** em `pareamento/cancelar` → `jaEncerrado`, que mostra *"Este código já foi usado ou
  expirou."* em vez de falha.

Toda leitura tem aborto em 20 s. A lista se renova sozinha a cada 60 s
(`RECARGA_AUTO_MS`) e a cada 30 s (`DISPOSITIVOS_POLL_MS`) enquanto existir código aberto.

## O que o manual precisava saber

**O código é gerado ao abrir a janela.** Em `ModalAtivarDispositivo.tsx`:

```tsx
useEffect(() => {
  if (!aberto) return;
  void gerar();
  return () => { rodada.current++; };
}, [aberto, tipo]);
```

Não existe botão *Gerar*. O único botão do caminho feliz é o **Copiar**, e o
`RefreshCw` (*Gerar outro código* / *Tentar novamente*) só aparece depois de expirar ou
falhar. Essa é a informação que o leitor não adivinha, e virou o miolo do Passo 2.

**O QR depende do tipo.** `META_TIPO` em `dispositivosCatalogo.ts` marca `comCamera` em
exatamente dois tipos — `APP_ENTREGADOR` e `TABLET`. Só neles a janela monta o par
`[qr, codigo]` em duas colunas e o terceiro passo troca *"digite o código"* por *"aponte a
câmera para o QR ou digite o código"*. No resto, o cartão do código vem sozinho e centrado.

**O prazo é de quinze minutos.** A API devolve `segundosParaExpirar`; o sandbox devolveu 900,
e a contagem da tela confirma (começa em 15:00). O relógio da tela nunca interpreta `expiraEm`:
`segundosRestantesDispositivo(segundos, decorridoMs)` desconta o tempo passado desde a
resposta, o que evita depender do relógio da máquina do lojista.

**Código aberto ocupa vaga.** A cota tem `total`, `usados`, `reservados` e `livres`, e
`reservados` são os códigos abertos. É o que explica a tela de limite citar *"Há N códigos
aguardando ativação. Eles ocupam uma vaga cada até ser usado ou expirar."* — e é a causa mais
comum do lojista achar que tem vaga e receber 409.

**Dois tipos não têm botão.** `PDV_MOBILE` tem `emBreve: true`, e no lugar do botão aparece o
selo *Gestão em breve*. `TEF` é desviado antes, para `SecaoTef`, porque usa cadastro legado
com limites próprios (`config.qtdTefStone` / `config.qtdTefPayGo`).

**A faixa só aparece se houver o que mostrar.** `tiposVisiveis` exige cota e, além dela, ou um
aparelho ativado, ou `total > 0`. O complemento (`tiposNaoContratados`) vai para a
`VitrineDispositivos`, que é oferta e não gestão — fora do escopo deste manual.

**Ativação bem-sucedida se resolve sozinha.** `useStatusPareamento` acompanha o pareamento;
em `ATIVADO` a janela dispara confete, chama `onAtivado` (que recarrega a lista) e se fecha
depois de `PAREAMENTO_SUCESSO_MS` (2,2 s). Não há botão de concluir — e por isso o manual não
manda clicar em nada no fim.

## Textos da tela, como estão no código

- Cabeçalho: **Dispositivos** / *"Aparelhos que estão usando o seu sistema. Cada aparelho
  ativado ocupa uma vaga do seu plano."*
- Linha de cota: `"{livres} de {total} livres"` — vermelha quando `livres === 0`; ou
  `"{n} aparelhos"` quando `total` é nulo.
- Linha de reserva: `"{n} código(s) aguardando ativação"`.
- Janela: **Ativar aparelho · {rótulo}** / *"Ativação de um novo aparelho no seu plano"*.
- Cartão do código: `codigoFormatado` em `font-mono`, **Copiar**, e a legenda *"Ou digite este
  código"* (com câmera) ou *"Digite este código no aparelho"* (sem câmera).
- Contagem: *"O código expira em M:SS"*.
- Limite: *"Você já usa todos os {total} aparelhos de {rótulo} do seu plano."* +
  *"Remova um aparelho da lista para ativar outro, ou contrate mais."* + **CONTRATAR MAIS**.
- Expirado: *"Este código expirou"* + **Gerar outro código**.
- Falha: `resultado.mensagem` ou *"Não foi possível gerar o código"* + **Tentar novamente**.
- Sucesso: *"Aparelho ativado"* + nome do aparelho + *"Ele já está na sua lista de
  aparelhos."*
- Remoção: *"A vaga fica livre na hora e você já pode ativar outro aparelho. Este sai do
  sistema em até uma hora, no próximo contato dele com o servidor."*
- Avisos: *"Código copiado"*, *"Código cancelado. A vaga está livre."*, *"Aparelho removido"*,
  *"Nome atualizado"*, *"Este código já foi usado ou expirou."*

## Rótulos dos tipos, como o sandbox devolveu

| Tipo | Rótulo | Câmera | Observação |
|---|---|---|---|
| `APP_GARCOM` | App Garçom | não | |
| `APP_GARCOM_POS` | App Garçom POS | não | |
| `APP_ENTREGADOR` | App Entregador | **sim** | |
| `TOTEM` | Totem de autoatendimento | não | |
| `TABLET` | Cardápio digital em tablet | **sim** | |
| `PDV_MOBILE` | PDV Mobile Offline | — | `emBreve`: sem botão |
| `TEF` | TEF | — | faixa própria, cadastro legado |

O rótulo vem da cota (da API), não do front: o manual cita os rótulos observados, e o
catálogo do front só guarda ícone, descrição e os sinalizadores `comCamera` / `emBreve`.
