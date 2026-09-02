# MEMORIA.md — #77 Cardápio digital presencial e QR Code

Manual **#77**. Ligar o canal presencial, os parâmetros e gerar o QR
Code — na **Configurações** e em **Meus Links**.

Última atualização: 02/09/2026.

---

## Escopo

Card **Presencial (Mesas/Comandas)** em **Cardápio Digital → Configurações**:
ligar o canal, cadastro / e-mail / nascimento, opções do garçom,
fechamento de conta e os **três geradores de QR**. Mais o grupo
**Cardápios Presencial** de **Meus Links**: link
`presencial.beefood.com.br`, selects de mesa/comanda, cardápio de
visualização, gerador em passos e o aviso *Recomendamos gerar QR
Code de Comanda*.

Não cobre: horário (#32), pausa (#33), app do garçom (#40), taxa de
mesa (#41), kiosk (#24), cadastro de mesas, código da mesa do PDV
(só a tabela “não confundir”).

---

## Origem

Pedido do dono (02/09/2026): estudar o presencial + QR (parâmetros e
geração) e **já produzir**. Follow-up no mesmo turno: incluir **Meus
Links** e seguir sem parar.

---

## Imagens (11 tratadas)

| Arquivo | Origem | O que aponta |
|---------|--------|--------------|
| `01-onde-fica.png` | viewport Configurações | aba, card, switch, link, 3 botões QR |
| `02-parametros.png` | recorte do card (`01-card-presencial`) | cadastro, e-mail, nasc., garçom, fechar conta |
| `03-garcom-opcoes.png` | modal (switch ligado só para o print) | um item + FECHAR |
| `04-qr-geral.png` | modal QR Code Presencial | QR, Download, Imprimir |
| `05-qr-mesa.png` | modal QR Mesa 1–6 | intervalo, Gerar, Imprimir Todos |
| `06-meus-links.png` | painel Meus Links, Sem mesa | grupo presencial + visualização |
| `07-meus-links-mesa.png` | idem, **Mesa 2** | select, URL `?mesa=2`, ícones |
| `09b-recomendacao-comanda.png` | `UsaComandaGate` (`09c-gate-comanda`) | mesa × comanda + botão |
| `08-gerador-passo1.png` | Meus Links → gerador | Mesas ou Comandas |
| `09-tipo-qr.png` | passo 2 do gerador | Cardápio Digital × Código da Mesa |
| `10-cardapio-digital.png` | tira (público) | Pedir (`/?tipo=p`) × visualização |

Puras extras (contexto, não tratadas): `00-admin-full`,
`05-qr-mesa-vazio`, `05b-qr-comanda-vazio`, `06-meus-links-topo`,
`06b-meus-links-gerador`, `07-meus-links-lista-mesa`,
`10-cel-presencial-home`, `10b-cel-mesa2`, `11-cel-visualizacao`,
`12-cel-presencial-dominio`, `09b-depois-tipo`.

---

## Decisões

- Um manual só (#77). Pasta `cardapio-digital-presencial-qrcode`.
- Prova no cardápio **público** (`?tipo=p` e
  `cardapio.beefood.com.br`), não no preview sticky (o alternador
  Delivery/Presencial depende de **Consumo no Local**, que é do card
  Delivery).
- Não clicar switch “só para ver”: auto-save 800 ms. O switch do
  garçom foi ligado só para o print do modal e **restaurado**.
- Gerar QR 1–6 no modal é local; não altera o servidor.
- Código da Mesa (`empresaID_N`) fica de fora, só na tabela.
- Meus Links: só o grupo **Cardápios Presencial**. Delivery (origem,
  balcão, multilojas) não entra.
- Texto usa **Mesa 2** (a primeira cadastrada no sandbox; não há
  Mesa 1).
- O aviso de comanda entra no manual: ele existe em Meus Links e
  **não** nos 3 botões da Configurações.

---

## Estado deixado no sandbox

Conta **BeeFood3 - Manual** (`contato@beefood.com.br`). Dump de
02/09/2026, sem mudança permanente de parâmetro:

| Campo | Valor |
|-------|-------|
| `linkAcesso` | `beefood3` |
| `qrCodePresencial` | ligado |
| `presencialGarcomOpcoes` | **desligado** (restaurado depois do print) |
| `pFechaConta` | ligado |
| cadastro | rápido (nome + telefone) |
| e-mail / nascimento | Opcional |
| `consumoLocal` | ligado |
| mesas | 2 a 11 (não existe Mesa 1) |
| comandas | existem (o gate disparou) |

Cardápio público no momento da captura: status **Fechado** (grade
presencial / horário) — documentado no FAQ e na Parte 5.

---

## Status

Concluído no repositório. Publicação é do dono.
