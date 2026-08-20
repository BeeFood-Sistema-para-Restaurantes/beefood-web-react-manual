# MEMÓRIA — Manual do Cardápio Digital Tablet / Modo Kiosk

> Memória detalhada deste manual (fluxo, uso, decisões e estado), para retomar a qualquer momento.
> Ver também a memória geral: `../../MEMORIA-GERAL.md`.

Status: 🔨 **Em execução — BLOQUEADO** (aguardando o material anexado) — Última atualização: 2026-08-20

---

## 1. O pedido

> "crie um manual sobre cardápio digital tablet -> modo kiosk, com base nas imagens e texto
> anexo. `images` `manual-modo-kiosk.md` (você não precisa emular o projeto, já está tudo
> pronto nos arquivos anexos, estude interprete e crie o manual em uma PR)"

O pedido veio logo depois da sessão que concluiu que **não dá para rodar emulador Android no
Cloud Agent** (registrado na seção 6 do `MEMORIA-GERAL.md`). A intenção era clara: não
precisa capturar tela, o material já existe.

## 2. O bloqueio — os anexos não chegaram ao Cloud Agent

**Nem o `manual-modo-kiosk.md` nem a pasta `images` existem nesta máquina.** Foi procurado:

| Onde | Resultado |
|------|-----------|
| `/workspace` (o próprio repositório) | árvore limpa, nada com `kiosk` no nome |
| Todo o histórico do repositório (`git rev-list --all`) | nenhum arquivo com `kiosk` ou `tablet` |
| Todas as branches remotas do repositório de manuais | nenhuma traz o arquivo |
| `~/refs/beefood-web-react` (front, atualizado) | `kiosk` só aparece em `TotemConfigModal.tsx`, e é o **Totem Windows** |
| `~/refs/beetech-server-node-2.0` (backend, atualizado) | `docs/tablet/` só tem `historico-cardapio-digital-tablet/API.md` |
| Bitbucket — as 81 branches do backend | as branches recentes com `docs/` têm sempre o mesmo conteúdo |
| Bitbucket — outros repositórios do workspace `beetechbr` | o `BITBUCKET_TOKEN` alcança **só** `beetech-server-node-2.0` |
| Sistema de arquivos inteiro (`find /`) | nada |

**Conclusão:** arquivo anexado pelo chat do Cursor **não é copiado para o VM do Cloud Agent**.
Ele fica no contexto da conversa; se o texto não vier inline na mensagem, o agente não tem
como abri-lo. Lição registrada também no `MEMORIA-GERAL.md`.

**Como desbloquear (qualquer um dos caminhos):**

1. **Melhor caminho** — commitar `manual-modo-kiosk.md` e a pasta `images/` numa branch deste
   repositório (por exemplo em `manuais/cardapio-digital-tablet-modo-kiosk/imagens-puras/`) e
   pedir a continuação.
2. Colar o conteúdo do `manual-modo-kiosk.md` **direto no corpo da mensagem** (as imagens
   continuariam faltando).
3. Se o material estiver num repositório Bitbucket do app Android, criar um **Repository
   Access Token** com escopo *Repositories: Read* para ele, guardar em outro secret e
   adicionar a entrada em `REFERENCIAS_BITBUCKET`, no `.cursor/install.sh` — lembrando que
   **secret só entra em VM nova**.

## 3. O que foi entregue mesmo assim

- `fluxo-codigo.md` — mapeamento técnico completo e **verificado** do Cardápio Digital
  Tablet: rota, permissão, as três abas, regras de status/bateria, limite contratado, os seis
  eventos, o corpo do POST, o controller do servidor e os rótulos do modal de layout. Esse
  trabalho vale independentemente do anexo.
- `cardapio-digital-tablet-modo-kiosk.md` — **rascunho** do manual, cobrindo tudo o que é
  comprovável hoje (etapas 1 a 6, feitas pelo painel). O que depende do anexo está marcado
  com `[PENDENTE — ANEXO]`.

**Não foi criado o `texto-documentation.ia.md`** de propósito: é o prompt de publicação, e o
manual não pode ser publicado nesse estado.

## 4. O que ainda falta

| Item | Depende de |
|------|-----------|
| Etapa 7 — travar o aparelho pelo Android | o anexo (não escrevi por conta própria para não divergir do procedimento oficial) |
| As 5 imagens marcadas como `[PENDENTE — ANEXO]` | as capturas do anexo, ou capturas novas do painel |
| `annotate.py` e as imagens em `imagens-tratadas/` | ter as imagens puras |
| `texto-documentation.ia.md` | o manual estar fechado |
| Revisão dos rótulos do app Android | o anexo (o app novo não tem documentação pública) |

## 5. Decisões tomadas

- **Não inventar o procedimento do Android.** Modo kiosk em Android tem pelo menos três
  caminhos diferentes (fixação de tela, launcher dedicado e MDM com Device Owner). Escolher um
  por conta própria teria boa chance de contradizer o que a BeeFood recomenda. Preferi deixar
  a seção marcada como pendente.
- **Escopo do rascunho = o que o painel faz.** O `TRAVAR` do painel é a parte do modo kiosk
  que existe hoje no produto e é 100% verificável no código. É um manual útil por si só.
- **Nome da pasta:** `cardapio-digital-tablet-modo-kiosk`, seguindo o padrão de um diretório
  por manual.

## 6. Descobertas úteis (não perder)

- **"Kiosk" aparece em dois lugares distintos do produto.** No `TotemConfigModal.tsx` existe
  o *Modo Kiosk* do **Totem Windows** — dois `.cmd` que abrem `totem.beefood.app` no Edge ou
  no Chrome com `--kiosk`. **Não é** o tablet. Não confundir os dois ao escrever.
- **Evento é fila, não comando.** `POST /api/tablet2/criarEvento` só grava a linha
  (`call autoatendimento.procInsertEvento`). O tablet executa no próximo contato — daí os
  estados *Pendente* e *Processado* na aba Eventos.
- **O `ATUALIZAR` tem efeito colateral no servidor:** dispara
  `processarCacheSetorProdutoGrupo(empresaID, "produto,setor,grupo,grupoOpcao")`.
- **Estourar o limite contratado desloga o tablet sozinho** (`activeCount = online + ausente`,
  contando todas as filiais). Nenhuma trava segura isso — vale um aviso no manual.
- **Divergência de rótulo do `tipoLayout`:** o card da aba Layout chama de *Grade* (1) e
  *Lista* (2); o modal de configuração chama os mesmos valores de *Lista Completa* (1) e
  *Por Etapas* (2).
- **Dois pacotes Android.** O app atual é `com.cardapiodigitalmesacomanda` (*Cardápio Digital
  Mesa/Comanda*), que é para onde o painel aponta. A base de conhecimento pública ainda
  documenta o antigo, `com.beegarcom` (*BeeGarçom — Cardápio Digital Tablet*).
- **Fontes oficiais aproveitadas no rascunho:**
  - `beefood.app/novidades` — app 1.0.2.6 (27/04/2026): retorno automático aos destaques
    após 5 minutos sem interação e proteção do carrinho por 60 segundos.
  - `ajuda.beefood.com.br` (artigo do app antigo) — requisitos do tablet (Android 11 / 2 GB
    mínimo; Android 14 / 4 GB recomendado) e a definição do *Travar* ("bloqueia os botões de
    voltar, para que os usuários não consigam sair do aplicativo").
- **O backend tem precedente de manual em `docs/`:** `docs/multilojas/manual-multilojas.md`.
  Reforça a hipótese de que o `manual-modo-kiosk.md` do dono vive num repositório de
  servidor/app ao qual este ambiente não tem acesso.

## 7. Estado do sandbox

Não verificado. A conta **BeeFood3 - Manual** provavelmente **não tem tablet físico
registrado**, então a aba Tablets deve cair no estado vazio (o card com o vídeo do YouTube e
o botão *Baixar App Android*). Para capturar as telas das etapas 2 a 5 seria preciso ao menos
um aparelho aparecendo na listagem — o que reforça usar as imagens do anexo.
