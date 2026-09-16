# fluxo-codigo.md — #101 Domínio próprio e subdomínio pela tela

Mapeamento técnico da tela nova de **Domínio Próprio** (autoatendimento). Leitura de
`beefood-web-react` com `git pull` em 16/09/2026 — `72fa5c3`. A tela nasceu nos
commits de 16/09 (`6b923d7` *Adicionou nova tela de Domínio* e seguintes).

O backend **não** entra aqui: o `beetech-server-node-2.0` clonado nesta VM está em
`4a419d2` (10/09) e não tem nada de domínio, e o `git pull` do Bitbucket continua
falhando por falta de credencial (o `BITBUCKET_TOKEN` parou de autenticar em 01/09,
ver `MEMORIA-GERAL.md` seção 8). Todo o mapeamento abaixo é do front + respostas
reais da API de produção.

## Quem enxerga a tela nova

`src/utils/dominioAcesso.ts` (arquivo novo):

```ts
const DOMINIO_NOVO_EMPRESAS = [38311];
export const podeUsarDominioNovo = (): boolean =>
  isDevelopment || DOMINIO_NOVO_EMPRESAS.includes(Number(getUserSession()?.empresaID));
```

`src/pages/Aplicativos.tsx` escolhe entre as duas modais no mesmo card `dominio`:

| Empresa | Componente | O que faz |
|---------|-----------|-----------|
| liberada (hoje só a **38311**, que é o sandbox dos manuais) | `DominioAutoatendimentoModal` | assistente de 4 passos + situação + aba DNS |
| todas as outras | `DominioModal` | o modal antigo, que só manda **falar com o suporte** (é o manual #52) |

Ou seja: **em produção a tela nova já está no ar**, mas por enquanto apenas para a
empresa liberada. O manual #52 continua valendo para quem vê o modal antigo.

## Estrutura do componente

`src/components/apps/DominioAutoatendimentoModal.tsx` — um `Sheet` à direita
(`sm:max-w-2xl`) com um `Tabs` por fora de tudo:

| Tela (`tela`) | Componente | Conteúdo |
|---------------|-----------|----------|
| 1 | `dominio/StepCardapio.tsx` | um cartão por cardápio da conta + *Domínios removidos anteriormente* |
| 2 | `dominio/StepTipo.tsx` | os dois cartões: **Domínio próprio** (`APEX`) e **Subdomínio** (`SUBDOMINIO`) |
| 3 | `dominio/StepEndereco.tsx` | campo do endereço com verificação automática |
| 4 / `'situacao'` | `dominio/SituacaoDominio.tsx` | progresso, etapas, instrução de DNS, histórico e a aba **DNS** |

`dominio/StepperDominio.tsx` desenha as quatro bolinhas (**Cardápio → Tipo →
Endereço → Pronto**). As abas **Situação / DNS** só aparecem quando
`dominio.dnsGerenciavel`, e a aba **DNS** fica desabilitada (com tooltip
*"Disponível quando o domínio terminar de ser configurado"*) enquanto
`!dominio.ativo`.

## Rotas usadas (`src/hooks/useDominio.ts`, base `/api/dominio2`)

| Ação | Rota |
|------|------|
| listar cardápios + domínio de cada um + removidos | `GET /painel/{empresaID}/{usuarioID}` |
| situação + histórico de um domínio | `GET /dominio/{empresaID}/{usuarioID}/{dominioID}` |
| conferir o endereço digitado | `POST /verificar` `{empresaID, usuarioID, filialID, dominio, tipo}` |
| cadastrar | `POST /dominio` (mesmo corpo) |
| pedir nova verificação (*Já configurei*) | `POST /reenfileirar` `{empresaID, usuarioID, dominioID}` |
| excluir | `DELETE /dominio/{empresaID}/{usuarioID}/{dominioID}` |

E a aba DNS (`src/hooks/useDominioDns.ts`, base `/api/dominio2/dns`):

| Ação | Rota |
|------|------|
| registros + tipos + limites + histórico | `GET /{empresaID}/{usuarioID}/{dominioID}` |
| criar/alterar | `POST /` `{..., dominioID, nome, tipo, ttl, valores[]}` |
| remover | `DELETE /{empresaID}/{usuarioID}/{dominioID}?nome=&tipo=` |

A verificação do endereço roda com **debounce de 600 ms** e a cada `blur`, e o
`useRef` `pedido` descarta resposta atrasada — quem digita rápido não vê resultado
de um texto antigo.

## O que a verificação devolve

`POST /verificar` volta `ok: true/false`. Com `ok: false`, o `codigo` decide o que a
tela mostra (`StepEndereco.tsx`):

| `codigo` | Tratamento na tela |
|----------|--------------------|
| `FORMATO` | mensagem vermelha embaixo do campo |
| `EMAIL_NO_APEX` | cartão amarelo + botão **Usar `<sugestão>`** (troca para subdomínio) + *Falar com o suporte* |
| `CARDAPIO_INVALIDO` | cartão vermelho + **Escolher outro cardápio** |
| `CARDAPIO_JA_TEM_DOMINIO` | cartão vermelho + **Ver o domínio atual** |
| `OCUPADO_OUTRA_EMPRESA` | cartão vermelho + **Falar com o suporte** |

Com `ok: true` a tela monta três blocos: **Vão responder por este cardápio**
(`hosts`), os `avisos[]` em amarelo e **O próximo passo será**
(`oQueVaiPrecisar.texto`). O botão **CADASTRAR DOMÍNIO** só habilita com
`ok: true`.

Resposta real do sandbox para `cardapioteste.com.br` (APEX), 16/09/2026 — o domínio
ainda não resolvia no DNS e mesmo assim o cadastro foi liberado, com aviso:

```
hosts: cardapioteste.com.br, www.cardapioteste.com.br
aviso: "Não encontramos cardapioteste.com.br no DNS. Confirme que o domínio está
        registrado e ativo — nós não fazemos o registro de domínios, apenas o
        apontamento."
oQueVaiPrecisar: "Trocar os servidores DNS do domínio no painel do seu registrador."
```

## Situação, etapas e a instrução de DNS

O `GET /dominio/...` devolve o objeto `Dominio` (`src/types/dominio.ts`) já
mastigado para a tela: `progresso` (0–100), `etapas[]` com `estado`
(`concluido | atual | pendente | erro`) e os booleanos que viram badge em
`dominio/statusDominio.tsx`:

| Condição (nesta ordem) | Badge |
|------------------------|-------|
| `removendo` | **Removendo** (amarelo) |
| `precisaSuporte` | **Precisa de ajuda** (vermelho) |
| `ativo` | **No ar** (verde) |
| `aguardandoCliente` | **Aguardando você** (amarelo) |
| `emAndamento` | **Configurando...** (azul) |
| — | **Cadastrado** (neutro) |

As cinco etapas do sandbox: **Pedido registrado → Apontamento do DNS →
Certificado de segurança → Publicação → No ar**.

`instrucao` é o cartão azul (`dominio/InstrucaoDns.tsx`) e tem dois formatos:

- `tipo: 'NS'` → lista `nameServers[]` numerada, cada linha com botão de copiar,
  mais **Copiar todos**. É o caminho do **domínio próprio (APEX)**.
- `tipo: 'CNAME'` → três colunas **Tipo / Nome / Valor** (`registro`), cada uma
  copiável. É o caminho do **subdomínio**.

Nos dois casos entra o `avisoDemora` e o botão **Já configurei, verificar agora**,
que chama `POST /reenfileirar`.

Instrução real devolvida para `cardapioteste.com.br` (16/09/2026 14:31):

```
tipo: NS
nameServers: ns-991.awsdns-59.net, ns-62.awsdns-07.com,
             ns-1150.awsdns-15.org, ns-1648.awsdns-14.co.uk
avisoDemora: "Depois de trocar, a mudança pode levar algumas horas para valer em
              toda a internet."
```

Quando `instrucao` é `null` e `preparandoInstrucao` é `true`, a tela mostra
*"Estamos preparando os dados do seu DNS — isso leva cerca de 1 minuto"*. No
sandbox a instrução apareceu ~40 s depois do cadastro.

**Atualização automática:** enquanto `emAndamento`, o modal refaz o `GET` a cada
**8 s**; se estiver `aguardandoCliente`, a cada **30 s**. Quando o domínio vira
`ativo` durante o acompanhamento, sai o toast *"Seu domínio está no ar!"*.

## Aba DNS (só com o domínio no ar)

`dominio/dns/AbaDns.tsx` + `TabelaDns.tsx` + `FormularioDns.tsx` +
`HistoricoDns.tsx`. A resposta do `GET` traz `registros[]`, `tipos` (rótulo, ajuda
e exemplo por tipo), `limites` (`ttlMinimo`, `ttlMaximo`, `ttlPadrao`,
`maxRegistros`, `maxValores`), `usados` e `historico[]`.

- Registro com `protegido: true` mostra **cadeado** com o `motivoProtegido` no
  tooltip, e não tem editar nem excluir — são os registros que fazem o cardápio
  funcionar.
- No formulário, **Tipo** e **Nome** ficam travados na edição (a tela avisa: *"Para
  mudar o nome ou o tipo, remova este registro e crie outro"*).
- **Nome** vazio ou `@` vira o domínio raiz; o rodapé do campo mostra o nome
  completo que vai ser criado.
- TTL vem de `OPCOES_TTL` (`60, 300, 1800, 3600, 86400`, escritos por
  `duracaoLegivel`) + **Personalizado** dentro dos limites.
- Depois de salvar/remover, `propagacaoSegundos` vira o aviso azul *"pode levar até
  X para valer em todos os lugares"*, e a linha alterada fica destacada por 2 s.
- Erro **504** não vira toast: vira cartão amarelo com **Atualizar lista** (a
  gravação pode ter ido adiante mesmo com o tempo esgotado).
- O aviso *"Quer usar o e-mail do seu domínio?"* é fechável e guarda a escolha em
  `localStorage` (`dominio_dns_aviso_email_fechado`).

## Excluir

Botão **Excluir domínio** no rodapé da situação → `ConfirmationDialog` com o texto
*"O endereço `<domínio>` vai parar de funcionar…"* e confirmação **Excluir
(ENTER)**. Depois do `DELETE`, o modal volta para a lista de cardápios e o domínio
passa a aparecer em **Domínios removidos anteriormente** (o `painel` devolve
`removidos[]` com `removidoEm`).

## Armadilha do APEX (está no próprio texto da tela)

`StepTipo.tsx` avisa que, ao trocar os servidores DNS do domínio principal, **o
e-mail daquele domínio para de funcionar** até os registros MX serem recriados — e
que isso se resolve na aba **DNS** depois da propagação. É o motivo de o backend
recusar o APEX com `EMAIL_NO_APEX` quando encontra servidores de e-mail no domínio,
oferecendo o subdomínio como saída.
