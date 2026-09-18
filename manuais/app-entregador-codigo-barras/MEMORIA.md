# MEMÓRIA — #114 Código de barras

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

O caso do 200 é o que mais mudou o manual: virou pergunta do FAQ. Sem ela, o lojista procuraria
defeito na impressora ou na câmera.

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

Nada para este manual. As 12 capturas pedidas ao dono
([`../gestao-entregas/pedidos/capturas-app.md`](../gestao-entregas/pedidos/capturas-app.md)) são
de outros assuntos — notificação, troca de entregador, rota ao vivo, falhas e iPhone. Nenhuma
delas é de código de barras.
