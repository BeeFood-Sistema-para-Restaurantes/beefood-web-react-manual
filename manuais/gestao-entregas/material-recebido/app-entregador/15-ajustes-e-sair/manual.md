# Manual 15 — Ajustes, permissões e sair

A quarta aba, **Ajustes**, não é uma tela de configurações: é o **menu do app**. De lá você
navega, confere as permissões do aparelho e encerra a sessão.

---

## O menu

[Entender o menu](01-menu-lateral.md)

![Menu lateral](prints/01-menu-lateral.png)

Cinco itens: **Entregas**, **Histórico**, **Código barras**, **Permissões** e **Sair**. Os três
primeiros são as mesmas abas do rodapé — o menu existe para chegar a **Permissões** e a
**Sair**, que não têm aba própria.

## Permissões

[Entender a tela de permissões](02-permissoes.md)

![Permissões](prints/02-permissoes.png)

Quatro permissões, cada uma com o que ela serve e se está **Ativa**:

| Permissão | Para que serve | O que quebra sem ela |
|---|---|---|
| Localização | acompanhar a entrega e montar rotas | o restaurante deixa de ver você no mapa |
| Localização em segundo plano | enviar a posição com o app minimizado | sua posição congela quando você sai do app |
| Câmera | ler o código de barras dos pedidos | o leitor da aba Código barras não abre |
| Notificações | avisar quando um pedido ou rota é seu | você só descobre entrega nova abrindo o app |

Tocar numa permissão abre as configurações do Android. O app não consegue ligá-las sozinho — só
o sistema faz isso.

**Vale conferir esta tela no começo do turno.** Uma permissão que o Android revogou (e ele
revoga, quando o app fica dias sem uso) não avisa: você só nota pelo problema.

## Sair

[Entender a confirmação de saída](03-confirmar-saida.md)

![Confirmar saída](prints/03-confirmar-saida.png)

**Sair do aplicativo?** — *Você vai encerrar a sessão neste aparelho. Para voltar a receber
entregas, será preciso entrar de novo.*

**SAIR** encerra a sessão e leva à tela de login (capítulo
[01](../01-primeiros-passos/manual.md)). **CANCELAR** volta ao menu.

**Sair não é ficar offline.** Para pausar sem perder a sessão, use a pílula de disponibilidade
do cabeçalho (capítulo [02](../02-disponibilidade/manual.md)). Sair é para o fim do expediente,
ou para passar o aparelho a outra pessoa.

**Ao sair, o app esquece o que era desta sessão.** Login, lista de entregas e as formas de
pagamento guardadas no aparelho são descartados — e é o que garante que o próximo a entrar não
veja nada do anterior.

## Se algo não funcionar

**Uma permissão está como inativa e eu não consigo ligar.** Toque nela para abrir as
configurações do Android e conceda por lá. Em alguns aparelhos, a localização em segundo plano
exige escolher **Permitir o tempo todo**.

**O ícone de recarregar na tela de permissões** relê o estado atual. Use depois de mexer nas
configurações do Android, para confirmar que o app enxergou a mudança.

**Saí sem querer.** Basta entrar de novo com o mesmo login. Nada de entrega se perde: a lista
vem do restaurante, não do aparelho.

---

## Como este capítulo foi produzido

Menu, tela de permissões e a folha de confirmação de saída foram capturados no emulador, com as
quatro permissões concedidas — por isso as quatro aparecem como **Ativa**.

A saída foi aberta e **cancelada**: sair encerraria a sessão que as capturas dos outros
capítulos usam. A tela de login que vem depois do SAIR é a mesma do capítulo 01, já
documentada lá.
