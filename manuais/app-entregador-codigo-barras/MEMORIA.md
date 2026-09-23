# MEMÓRIA — #114 Código de barras

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `app-entregador-codigo-barras.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

## Por que este manual existe, mesmo com o #104 já falando de código de barras

O dono pediu, em 18/09/2026: *"falta incluir a leitura de código de barras → como ativar o
parâmetro, ler o pedido, etc etc"*. O #104 tem uma seção que **liga** a etiqueta, mas ela está
dentro do fluxo de liberar o entregador, e o #104 não mostra o leitor do celular — ele apontava
para este manual, que ainda não existia.

Decisão: **um manual com as duas metades**, painel e celular. Quem procura "código de barras"
resolve numa página só. O #104 mantém a seção e o link.

## O primeiro manual do app

É o primeiro da série que usa os prints do material recebido, e por isso ele definiu a técnica que
os outros cinco reaproveitam:

- **`cabeca-app.py`** (miolo comum) em vez do `cabeca-annotate.py`: os prints do app não têm
  `.geo.json` — não saíram de Playwright — então as coordenadas são **fração**, não pixel.
- **`copiar()`** traz o print do material, recorta por fração (a tela do celular tem 1440x3120 e
  quase sempre sobra faixa preta) e reamostra para largura fixa.
- **`com_margem()`** foi a descoberta da rodada. A primeira tentativa pôs etiqueta e seta **dentro**
  da tela: cobriram o título, o texto do botão azul e o VOLTAR. Tela de celular é estreita e cheia;
  não há canto vazio. Com uma margem clara à esquerda, a seta entra pela borda e o print fica
  inteiro visível.
- **`copiar_pura()`** traz captura de outro manual. As duas telas do painel (`01` e `02`) são as
  mesmas do #104 — recapturar daria imagem idêntica com outro nome. A **anotação** é própria: lá a
  caixinha é um passo do cadastro, aqui é o assunto da página.

## O que eu esperava e não era assim

| Eu esperava | O que é |
|---|---|
| O leitor ser conferência ("bipar para ver o que é") | É **despacho**, com o mesmo código do botão do painel: cliente avisado, marketplace avisado, cupom impresso |
| Loja sem o recurso receber erro na leitura | O servidor responde **200** e não faz nada. A tela diz sucesso e o pedido não muda — decisão registrada no doc 19, para não dizer "erro" a quem só não contratou |
| Qualquer código de barras servir | **Só EAN-13.** QR Code não reage |
| A caixinha estar na primeira aba do layout | Está na **terceira** (*Texto Padrão*), no fim de um formulário longo |
| A faixa de status ter **cinco** mensagens | Tem **seis**. Faltava *Erro: {mensagem}* |

O caso do 200 é o que mais mudou o manual: virou pergunta do FAQ. Sem ela, o lojista procuraria
defeito na impressora ou na câmera.

A **sexta mensagem** apareceu depois, relendo o estudo de fonte que veio no material do dono
(`estudo/01-o-que-o-app-faz-hoje.md`, seção 2.10, lida em `BarcodeScannerModal.js`). A tabela do manual
juntava as duas de erro em *"Erro… (vermelha)"*, e com isso perdia a única distinção que muda o que o
entregador faz: **`Erro na leitura, tente novamente`** é o envio que não saiu do celular, e ler de novo
resolve; **`Erro: {mensagem}`** é a loja respondendo e recusando, e ler de novo repete a resposta. A
tabela e o FAQ passaram a separar as duas, e o manual ganhou a dica que fica sob a faixa da câmera
(*Posicione o código de barras na faixa da câmera*), que também não estava escrita em lugar nenhum.

Vale reter de onde ela veio: **de reler o que já estava no disco**, não de captura nova. O material
que o dono manda tem mais valor que as imagens dele.

## Decisões de imagem

- **O rodapé do app (`04`) não tem etiqueta numerada.** As quatro abas ficam encostadas, e
  qualquer número cobriria o nome de alguma. Moldura verde e citação no texto resolvem.
- **A etiqueta EAN-13 (`07`) entra por `passthrough()`**: não há o que apontar numa imagem que é só
  o código.
- **O endereço do cliente no cupom já vem borrado da pura**, do #104 — o repositório é público, e a
  regra é borrar na pura, não só na tratada.
- **A imagem dentro da faixa da câmera é composta**, e isso está declarado no material: o emulador
  não tem câmera física. Fora da faixa, nada foi alterado. O manual do usuário não menciona (é
  bastidor), mas o `fluxo-codigo.md` registra.

## O que falta

**Nada, e nada está pedido.** As 26 capturas pedidas ao dono
([`../gestao-entregas/pedidos/capturas-app.md`](../gestao-entregas/pedidos/capturas-app.md)) eram de
outros assuntos — notificação, troca de entregador, rota ao vivo, falhas e iPhone —, e nenhuma era de
código de barras.

**Chegou a existir um pedido para trocar a imagem composta por uma real e fotografar as faixas de
resultado, e ele foi recusado.** Duas razões, e as duas são boas:

- as três fotos de **resultado** (*Pedido lido com sucesso!*, *Erro na leitura*, *Pedido já lido.*)
  seriam quatro imagens quase iguais de uma faixa colorida, para ensinar o que **seis frases numa
  tabela** já ensinam melhor — e a tabela permite comparar as seis de uma vez, o que nenhuma sequência
  de fotos permite;
- a de **enquadramento** substituiria a composição por uma captura real, o que é melhor em princípio,
  mas custaria montar um pôster de cena virtual no emulador para ganhar precisão numa imagem que o
  `fluxo-codigo.md` já declara como montada. Não é proporcional.

A composição fica, declarada, que é o combinado: **imagem montada pode ficar, imagem montada sem aviso
não pode.** Nada fora da faixa da câmera foi alterado.
