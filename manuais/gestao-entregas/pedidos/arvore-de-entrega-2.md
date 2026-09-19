# Grave os prints aqui

As pastas já existem com o nome certo. Cada print vai em `<pasta>/prints/<nome>.png`, com o nome
exato da tabela em `../1-pedido/capturas-app-2.md` — sem renomear, sem recortar, sem anotar.

```
capturas-3/
├── 26-codigo-de-barras/prints/    01-codigo-na-faixa.png  02-lido-com-sucesso.png
│                                  03-faixa-vermelha.png   04-pedido-ja-lido.png
├── 27-historico-vazio/prints/     01-historico-vazio.png
├── 28-abrir-sem-rede/prints/      01-app-sem-rede-do-zero.png
├── 29-fontes/                     BarcodeScannerModal.js  historico-index.js  entregas-index.js
├── _ferramentas/emulador/         capturar.ps1  elementos.ps1
└── RELATORIO.md                   ← escreva este arquivo, ele é parte da entrega
```

Seis fotos e três arquivos copiados. Nenhuma depende de outra pessoa — não há janela combinada nesta
rodada, e tudo sai de emulador, banco e printscreen.

Quatro coisas para saber antes de começar, e as duas primeiras são travas:

**Ler a etiqueta da pasta 26 DESPACHA o pedido de verdade.** Avisa o cliente e o marketplace. Só
bipe etiqueta de pedido semeado pelo `preparar --caso lista`, cujos clientes são sintéticos e sem
telefone.

**A pasta 27 precisa dos dois comandos novos**, nesta ordem: `historico-zerar`, a foto,
`historico-voltar`. Sem o `voltar`, as entregas ficam fora do relatório de operação.

**A `26/01` é a foto de maior valor e menor risco**, e é a primeira a tirar: ela não precisa que a
leitura dê certo, só que a câmera **veja** o código na faixa. É ela que tira do #114 a única imagem
composta do bloco. As outras três da pasta dependem de a leitura decodificar.

**A pasta 28 sai de um build de release do próprio repositório**, não da Play Store: release embute o
bundle, e por isso o app abre sem o Metro. No build de desenvolvimento, "abrir sem rede" derruba o app
antes de qualquer tela.

**A pasta 29 não é foto**: são três arquivos de fonte copiados como estão, para eu conferir o texto dos
manuais contra o código. Eles não vão para o repositório — leio, anoto o que interessa e descarto.

Pasta que ficar vazia não é problema, desde que o `RELATORIO.md` diga por quê. Nenhuma das seis
bloqueia manual.

## O `RELATORIO.md`

Três coisas, e a terceira é a que faz o material ser confiável:

1. a **versão do app** e a data da captura — se a pasta 28 sair de um build de release seu, diga a
   versão dele também;
2. o **aparelho**: qual AVD, qual Android. E, na pasta 26, **se a cena virtual funcionou ou não** —
   isso vale tanto quanto a foto, porque decide se o manual continua com a imagem composta;
3. **uma linha por print que saiu diferente do pedido**, dizendo o que aconteceu antes, e uma linha
   por print que **não saiu**, dizendo por quê. Print que saiu como pedido não precisa de linha.

Na rodada passada foi o item 3 que virou achado: o *Permissão necessária* no lugar da falha da melhor
rota mudou uma resposta do #113, e o "histórico vazio" com 22 entregas gerou os dois comandos novos do
script.
