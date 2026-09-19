# Smoketests — como refazer os cenários e as capturas

Tudo que o manual mostra é reexecutável. Este arquivo é o roteiro: monta o cenário, captura, e
desmonta no fim.

---

## 1. O emulador

```powershell
# subir o Pixel 7 Pro em pt-BR (o locale precisa vir na subida; `adb root` derruba a instância)
emulator -avd Pixel_7_Pro -prop persist.sys.locale=pt-BR

# o app precisa do Metro do projeto
cd C:\projetos\beetech-entregador
yarn start

# GPS em Sorocaba, senão o Google Maps calcula rota a partir do Vale do Silício
adb emu geo fix -47.4657927 -23.5061438
```

**Se o app mostrar "Unable to load script"**, o emulador perdeu a rota de rede e não alcança o
Metro em `10.0.2.2:8081`. Reciclar o Wi-Fi virtual resolve:

```powershell
adb shell svc wifi disable; adb shell svc wifi enable
adb shell ip route     # precisa ter uma rota default por wlan0
```

**Para começar do login**, como no capítulo 01:

```powershell
adb shell pm clear com.beetechentregador
```

---

## 2. O cenário em banco

O gerador vive no projeto do servidor, em
`beetech-server-node-3.0/scripts/cenario-app-entregador.js`. Ele reaproveita o `semearLote` do
seed de entregas e cria sempre o mesmo pedido: **1x Combo One Burger** com One Burger, Batata
frita e Coca Cola 350ml.

```powershell
cd C:\projetos\beetech-server-node-3.0

# ver o que aconteceria, sem escrever nada
node scripts\cenario-app-entregador.js --empresa 38311 --filial 39202 --perfil lista --dry-run

# quatro entregas abertas (lista, detalhes, mapa, melhor rota, cobrança, finalizar)
node scripts\cenario-app-entregador.js --empresa 38311 --filial 39202 --perfil lista

# as mesmas quatro, com as três primeiras agrupadas numa rota do painel
node scripts\cenario-app-entregador.js --empresa 38311 --filial 39202 --perfil lista --rota 3

# uma entrega só, para telas que precisam estar limpas
node scripts\cenario-app-entregador.js --empresa 38311 --filial 39202 --perfil unico

# um pedido iFood e um 99Food, os dois já pagos
node scripts\cenario-app-entregador.js --empresa 38311 --filial 39202 --perfil marketplace

# desmontar
node scripts\cenario-app-entregador.js --empresa 38311 --filial 39202 --limpar
```

Cada execução termina com a seção **CONFERÊNCIA — o que o app vai mostrar**, que lê a mesma API
que o app chama (`gestaoEntregaEntregadorEntregas`) e falha se a lista não vier como o cenário
prometeu. É o smoketest propriamente dito: se ele passa, a tela do app está pronta para a
captura.

**A limpeza não apaga pedido.** Ela desatribui o entregador, o que tira o pedido da lista e do
histórico do app sem mexer no que o ERP registrou. O recorte exige as três coisas juntas: filial
da lista branca, entregador da lista branca e o marcador `[MANUAL-ENTREGADOR]` na observação do
cliente. Rotas criadas pelo cenário são apagadas direto no Aurora, de propósito: o caminho
oficial mandaria WhatsApp de "entrega cancelada" ao entregador a cada limpeza.

**O que o cenário monta em cada perfil**

| Perfil | Pedidos | Para quê |
|---|---|---|
| `lista` | 4 — dinheiro com troco para R$ 50, Pix, débito e crédito; três no Centro e um no Campolim | capítulos 03 a 07, 11 a 13 |
| `unico` | 1 — dinheiro, troco para R$ 50, com complemento e observação | capítulos em que a tela precisa estar limpa |
| `marketplace` | 2 — um iFood e um 99Food, já pagos | capítulos 09 e 10 |

---

## 3. As capturas

```powershell
cd C:\projetos\beetech-entregador\docs\manual-gestao-entregas-2\smoketests\emulador

.\capturar.ps1 -Capitulo 03-lista-de-entregas -Nome 01-lista-com-quatro
.\capturar.ps1 -Capitulo 03-lista-de-entregas -Nome 02-card-em-detalhe -Espera 2
```

O script existe porque `adb exec-out screencap -p > arquivo.png` **corrompe o PNG no
PowerShell** — o redirecionamento trata binário como texto. Ele faz o caminho de dois passos
(`screencap` no `/sdcard`, depois `pull`) e recusa arquivo menor que 10 KB, que é o sintoma de
captura falhada.

Para achar onde tocar, `elementos.ps1` despeja a hierarquia da tela com as coordenadas de cada
elemento:

```powershell
.\elementos.ps1                 # tudo que está na tela
.\elementos.ps1 -Filtro COBRAR  # só o que casa com o texto
```

**Cuidado com o teclado.** Ele empurra a tela para cima, e uma coordenada colhida com o teclado
fechado erra o alvo depois que ele abre. Colha as coordenadas no mesmo estado em que vai tocar.

---

## 4. O código de barras

O emulador não consegue apontar a câmera para uma etiqueta, então o capítulo 08 mostra a imagem
composta e executa a leitura pela mesma rota que o leitor chama.

```powershell
cd C:\projetos\beetech-entregador\docs\manual-gestao-entregas-2\smoketests\codigo-de-barras

# gera o EAN-13 do pedido: o preVendaID com zeros à esquerda até 12 dígitos, mais o verificador
node gerar-ean13.js 59487819

# sobrepõe a etiqueta na faixa do leitor, a partir de uma captura da câmera aberta
.\compor-leitura.ps1 -Captura ..\..\08-codigo-de-barras\prints\01-leitor-aberto.png `
                     -CodigoBarras .\ean13-59487819.png `
                     -Saida ..\..\08-codigo-de-barras\prints\02-codigo-na-faixa.png
```

A movimentação em si é um `POST tentrega/lerCodigoBarras` com Basic Auth, idêntico ao que o app
envia ao reconhecer o código. O pedido sai de *PREPARO* para *ENTREGA* — e é isso que o capítulo
confere no banco.

---

## 5. Ordem sugerida para refazer o manual inteiro

1. Limpar o cenário e `pm clear` no app → capítulo **01** (login e permissões).
2. Sem pedido nenhum → capítulo **02** (disponibilidade) e a lista vazia do 01.
3. Perfil `lista` → capítulos **03**, **04**, **05**, **07**.
4. Limpar, perfil `lista --rota 3` → capítulo **06**.
5. Com o cenário ainda de pé → capítulos **11**, **12**, **13** (cada um consome um pedido).
6. Perfil `unico` → capítulo **08** (código de barras).
7. Limpar, perfil `marketplace` → capítulos **09** e **10**.
8. Depois de finalizar entregas nos capítulos 11 a 13 → capítulo **14** (histórico).
9. A qualquer momento, sem cenário → capítulo **15** (ajustes e sair).
10. Limpar o cenário.

**Os capítulos 11 a 13 consomem pedidos**: cada finalização tira um da lista. Rodando na ordem
acima, os quatro pedidos do perfil `lista` dão conta dos três capítulos e ainda alimentam o
histórico.
