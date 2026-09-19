# Grave os prints aqui

As pastas já existem com o nome certo. Cada print vai em `<pasta>/prints/<nome>.png`, com o nome
exato da tabela em `../1-pedido/capturas-app.md` — sem renomear, sem recortar, sem anotar.

```
capturas-2/
├── 16-notificacoes/prints/            01-aviso-chegando.png  02-lista-depois-do-toque.png
├── 17-troca-de-entregador/prints/     01-aviso-de-remocao.png  02-lista-sem-o-pedido.png
├── 18-ciclo-completo/prints/          01-rota-recebida.png  02-em-rota.png  03-primeira-parada.png
│                                      04-cobranca-concluida.png  05-lista-sem-a-rota.png
│                                      06-historico-do-dia.png
├── 19-sem-internet/prints/            01-lista-sem-carregar.png  02-plataforma-nao-carrega.png
├── 20-permissao-e-presenca/prints/    01-localizacao-recusada.png  02-pilula-sem-nuvem.png
├── 21-listas-vazias/prints/           01-entregas-vazia.png  02-historico-vazio.png
├── 22-erros-de-cobranca/prints/       01-soma-precisa-fechar.png  02-nao-foi-possivel-cobrar.png
│                                      03-pedido-ja-pago.png  04-falta-finalizar.png
├── 23-rota-com-problema/prints/       01-despacho-nao-confirmado.png  02-falha-melhor-rota.png
│                                      03-duas-rotas.png
├── 24-plataforma-sem-confirmacao/prints/  01-selo-keeta.png
├── 25-ios/prints/                     01-lista-entregas.png  02-detalhes-entrega.png
├── _ferramentas/emulador/             capturar.ps1  elementos.ps1
└── RELATORIO.md                       ← escreva este arquivo, ele é parte da entrega
```

A pasta `18-ciclo-completo` é a única que **não** se faz sozinho: ela depende da janela combinada
com o operador do painel, descrita em `../1-pedido/janela-117.md`. Seis fotos de seis pedidos
diferentes não servem — tem de ser o mesmo pedido nas duas telas.

Pasta que ficar vazia não é problema, desde que o `RELATORIO.md` diga por quê.

## O `RELATORIO.md`

Três coisas, e a terceira é a que faz o material ser confiável:

1. a **versão do app** e a data da captura;
2. o **aparelho**: emulador (qual AVD, qual Android) ou aparelho físico, qual;
3. **uma linha por print que saiu diferente do pedido**, dizendo o que aconteceu antes, e uma linha
   por print que **não saiu**, dizendo por quê. Print que saiu como pedido não precisa de linha.
