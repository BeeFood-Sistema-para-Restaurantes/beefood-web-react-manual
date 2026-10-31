# MEMORIA.md — #131 Código de ativação de aparelho (Dispositivos)

## O pedido do dono

> *"faça o manual de cofigurações -> Dispositivos. o manual deve contemplar só como criar o
> codigo de ativação. na pagina de planos e preços ja mostra a quantidade por plano. a ideia é
> mostrar só como gerar o codigo pro nosso mcp conseguir encontrar essa informação. então é um
> manual simples. estude e faça sem parar."* — 24/10/2026

Duas coisas vieram pedidas e foram respeitadas ao pé da letra:

1. **O recorte é a geração do código.** Quantidade por plano não entra: isso é assunto da
   página de planos e preços, que não envelhece junto com o manual.
2. **O destino é o MCP de manual.** A página precisa ser achável por quem pergunta *"como
   ativo o App Garçom"* sem saber que a tela se chama *Dispositivos*. Daí o FAQ ser a seção
   mais longa de um manual curto: ele é o que o MCP vai casar com a pergunta do usuário.

## O que entrou e o que ficou fora

**Entrou:** abrir a tela, o botão **Ativar aparelho** de cada faixa, a janela que já abre com
o código, o QR dos aparelhos com câmera, o código esperando na lista, o **Cancelar** e a tela
de limite do plano.

**Ficou fora, de propósito:** a vitrine de aparelhos não contratados, o detalhe do aparelho, o
cadastro de TEF e a lupa de busca. Renomear e remover entraram só como resposta de FAQ, porque
quem bate no limite precisa saber que remover libera a vaga — mas não ganharam passo nem
imagem. Regra 0: imagem só entra se o leitor sair dela fazendo algo diferente.

## A descoberta que deu forma ao manual

O código **é gerado quando a janela abre** — não há botão de gerar. Em
`ModalAtivarDispositivo.tsx`, um `useEffect` com dependência `[aberto, tipo]` chama `gerar()`.
O único botão do caminho feliz é o **Copiar**.

Isso muda o Passo 2 inteiro: em vez de *"clique em gerar"*, o manual diz *"o código já aparece
gerado"*. Quem escreve de cabeça erra essa, porque toda tela parecida tem botão.

As outras três que o código entregou e o texto da tela não diz:

- **`comCamera` existe em exatamente dois tipos** (`APP_ENTREGADOR` e `TABLET`). Só neles a
  janela mostra o QR. Prometer QR para o totem seria errado.
- **Código aberto ocupa vaga** (`reservados` na cota). É a explicação do lojista que "tem
  aparelho sobrando" e recebe 409.
- **Quinze minutos**, e não "alguns minutos": `segundosParaExpirar` voltou 900 do sandbox, e a
  contagem da tela começa em 15:00.

## As capturas

`capturar.py` roda tudo de uma vez, no sandbox *BeeFood3 - Manual* (empresaID 38311), tema
claro, 1440x900 em escala 1,5 → puras de 2160x1350.

| Pura | O que é | Por que esse tipo de aparelho |
|---|---|---|
| `01-tela-dispositivos.png` | a tela como ela abre | a faixa do App Garçom é a primeira, e tem vaga livre |
| `02-modal-codigo-app-garcom.png` | a janela com o código | **sem câmera**: mostra o cartão do código sozinho, o caso mais comum |
| `03-modal-codigo-qr-app-entregador.png` | a mesma janela com QR | **com câmera**: a variação que o leitor precisa reconhecer |
| `04-modal-sem-vaga-totem.png` | a tela de limite | o Totem do sandbox usa 1 de 1, então o 409 acontece de verdade |
| `05-codigo-aguardando-ativacao.png` | o código na lista | tirada depois dos dois modais, com dois códigos abertos |

Três detalhes do script que vale guardar:

- **Cada abertura de janela consome uma vaga.** O script cancela no fim, pelo
  `POST /api/dispositivos2/pareamento/cancelar`, os códigos que ele mesmo criou. Sem isso o
  sandbox vai acumulando reserva e a próxima rodada cai em 409.
- **O botão *Atualizar* saía pintado** de foco/hover depois do clique, roubando a atenção da
  imagem 05. Resolvido com `document.activeElement.blur()` e um `mouse.move` para um ponto
  neutro antes do print.
- **O código aparece nas imagens** (`7MG-VTD`, `KJK-QMT`) e pode ficar versionado: ele já foi
  cancelado, vale quinze minutos e é de um sandbox descartável. Não é credencial.

## As setas

Catorze setas em cinco imagens, coordenadas em fração, medidas com a grade de frações.

Três das cinco imagens são janela sobre tela escurecida, e aí a etiqueta não cabe dentro da
caixa branca sem cobrir texto. Ela foi para a **faixa escurecida à esquerda da janela**, com a
seta apontando para dentro — o círculo verde com número branco continua legível sobre o
escurecido. É o que foi feito nas etiquetas da lista de passos, do QR e do aviso de limite.

Quatro pontas foram corrigidas depois de olhar o recorte em tamanho real: as duas etiquetas da
lista de passos encostavam no `1.` e no `3.`, a do código tocava o `D` de `7MG-VTD` e a de
*código aguardando ativação* encostava no `1` do texto. Em todas, a correção foi mover a ponta
de 4 a 6 milésimos — a regra da casa de **mirar a borda, não o centro**, com a margem que o
olho no print reduzido não mostra.

## Estado

Concluído. `conferir-setas.py` fecha em 14 setas e 0 falha; `validar-imagens.py` e
`indice-manuais.py --conferir` passam.

O sandbox ficou como estava: os dois códigos criados para as capturas foram cancelados na
mesma rodada, e nenhum aparelho foi ativado nem removido.
