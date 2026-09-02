# MEMORIA.md — #77 Cardápio digital presencial e QR Code

## Escopo
Card **Presencial (Mesas/Comandas)** em **Cardápio Digital → Configurações**:
ligar o canal, os parâmetros (cadastro, e-mail, nascimento, garçom,
fechamento) e os **três geradores de QR**. Mais a sessão **Meus Links**
no presencial: link `presencial.beefood.com.br`, selects de mesa/comanda,
cardápio de visualização e o gerador em passos.

Não cobre: horário (#32), pausa (#33), app do garçom (#40), taxa de mesa
(#41), kiosk (#24), cadastro de mesas, código da mesa do PDV (só a
tabela “não confundir”).

## Origem
Pedido do dono (02/09/2026): estudar o presencial + QR (parâmetros e
geração) e **já produzir**. Follow-up no mesmo turno: incluir **Meus
Links**. Estudo no chat; execução nesta pasta.

## Imagens
Preenchido depois das capturas. Alvo: ~10 tratadas (setas + tira).

## Decisões
- Um manual só (#77). Pasta `cardapio-digital-presencial-qrcode`.
- Prova no cardápio público (`?tipo=p` e `cardapio.beefood.com.br`),
  não no preview sticky (o alternador Delivery/Presencial depende de
  **Consumo no Local**, que é do card Delivery).
- Não clicar switch “só para ver”: auto-save 800 ms.
- Gerar QR 1–6 no modal é local; não altera o servidor.
- Código da Mesa (`empresaID_N`) fica de fora, só na tabela.
- Meus Links: ensinar o grupo **Cardápios Presencial**; o grupo
  Delivery (origem, balcão, multilojas) não entra.

## Estado deixado no sandbox
Nenhum switch das configurações foi alterado de propósito. Conferir
depois das capturas.

## Status
Em execução.
