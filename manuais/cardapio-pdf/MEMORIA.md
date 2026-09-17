# MEMÓRIA — #102 Gerar Cardápio em PDF

Pasta: `manuais/cardapio-pdf/` · Manual: `cardapio-pdf.md` · 12 imagens
Produzido em 17/09/2026, em **produção**, na conta sandbox
**BeeFood3 - Manual** (`contato@beefood.com.br`, `empresaID 38311`).

## Pedido do dono

> "faça git pull em beefood-web-react e crie um novo manual sobre o menu Cardápio →
> Cardápio em PDF — *Gerar Cardápio em PDF*. crie um SEO friendly para buscar
> possíveis de clientes para nosso MCP de manual conseguir buscar no texto do manual.
> estude e crie o manual, sem parar."

O `git pull` trouxe justamente o código novo do gerador (último commit
`6e1ac75`, com `src/utils/cardapioPdfAcesso.ts` e a série de correções do PDF:
margens, fundo preto da logo, renderização do setor, máscara do telefone).

## Por que o recurso pode não aparecer

`utils/cardapioPdfAcesso.ts` libera por empresa: `CARDAPIO_PDF_EMPRESAS = [38311]`
(e qualquer conta em `isDevelopment`). Some o item do menu, o atalho do menu de ações
e a rota `/cardapio-pdf` (redireciona para `/cardapio`). O sandbox é **exatamente**
a empresa liberada — deu para capturar tudo em produção. O manual abre avisando que o
recurso está em liberação.

## Dois caminhos de acesso (os dois documentados)

1. Menu lateral **Cardápio → Cardápio em PDF** — página cheia, último item do grupo.
2. **Cardápio → Produtos → três pontinhos → Gerar cardápio em PDF** — mesmo editor,
   em janela. No celular é só esse caminho (tela cheia).

## Achados que viraram texto do manual

- **Nada é salvo.** `useCardapioPdfProjeto` é `useState` puro: fechar o gerador zera
  itens, layout e marca. Virou aviso na abertura, na seção 2 e na FAQ.
- **Editar item na etapa 1 não altera o cadastro** (`overrides` só no PDF). Foi o
  gancho para uma dica real: a descrição do sandbox traz linhas internas
  (*"Tags / X-salada, x salada, cheese salada"*) que aparecem no PDF — o lugar de
  limpar é ali, sem mexer no produto.
- **O QR Code é montado na etapa 3.** O canvas do `qrcode.react` vive escondido
  dentro do `StepMarca`; quem vai da etapa 1 direto ao download (ou aperta F2) baixa
  a capa **sem** o quadradinho. Provado nas capturas: a prévia da etapa 1 (imagem 03)
  não tem QR e a da etapa 3 (imagem 08) tem. Está no manual como aviso e em
  *Problemas comuns*; o `capturar.py` passa pela etapa 3 antes de baixar.
- **Clássico sai com foto**, apesar da descrição "só texto": `projetoPadrao()` liga
  `mostrarFotos`. Só o Fotográfico obriga (switch travado).
- **Peso do arquivo**: mesmo cardápio (68 itens, 8 seções) deu **4,4 MB / 5 páginas**
  com fotos e **57 KB / 4 páginas** só com texto. Virou tabela na seção 8, receita do
  WhatsApp e item de *Problemas comuns*.
- Preço do impresso tem quatro origens (presencial é o padrão) e produto fora da
  tabela de preço cai no presencial.
- Só produto **ativo** entra; seção sem item marcado desaparece do PDF.
- Telefone, endereço, redes sociais e logo já vêm preenchidos do cadastro (empresa +
  configurações do cardápio digital); a logo é achatada na cor de fundo (PNG
  transparente sairia preto).

## SEO (pedido explícito do dono)

O texto foi escrito com as palavras que o lojista digita, não com o nome interno da
tela: *cardápio em PDF*, *gerar cardápio em PDF*, *cardápio impresso*, *imprimir
cardápio*, *cardápio para imprimir*, *cardápio de mesa*, *cardápio A4*, *cardápio
A5*, *cardápio com foto*, *cardápio sem preço*, *cardápio com QR Code*, *cardápio
para gráfica*, *mandar cardápio no WhatsApp*, *cardápio de parede / estilo lousa*,
*modelo de cardápio*, *cardápio de balcão*.

Onde eles entram: título, primeiro parágrafo (lista de usos), tabela dos cinco
modelos (com "bom para" por tipo de casa), seção **9. Receitas rápidas** (uma linha
por intenção de busca) e uma FAQ escrita em forma de pergunta de usuário
("Como eu gero o cardápio do meu restaurante em PDF para imprimir?", "Dá para
imprimir em A5?", "Quero um cardápio leve para mandar no WhatsApp"). A instrução de
publicação (`texto-documentation.ia.md`) proíbe resumir a FAQ e trocar esses termos
por sinônimos genéricos.

## Capturas

`capturar.py` tem uma etapa por imagem (`menu`, `acoes`, `etapa1`, `etapa1_secao`,
`etapa2_modelo`, `etapa2_layout`, `etapa2_mostrar`, `etapa3_marca`, `etapa3_capa`,
`etapa4`, `pdf`, `pdf_sem_fotos`, `render`) e imprime as caixas dos elementos já na
escala da imagem (`caixa()`) — as coordenadas do `annotate.py` saíram daí, sem chutar
pixel no PNG reduzido.

Cuidados desta tela:

- A prévia é desenhada em canvas pelo `pdf.js` e **demora**. `esperar_previa()`
  aguarda o `img[alt="Página 1 do cardápio"]`; sem isso a captura sai com o skeleton
  *Montando a prévia...*.
- Trocar de etapa não recarrega a página: o `capturar.py` reabre `/cardapio-pdf`
  para cada imagem, garantindo estado limpo (e é por isso que a etapa 3 precisa ser
  visitada de propósito quando o QR importa).
- Imagens **06** e **07** são recorte da coluna de ajustes (`crop=(316,160,1250,1320)`)
  + faixa branca à direita (`pad_right=140`): os controles ocupam a coluna inteira e
  não sobrava espaço vazio para os números. Padrão já registrado na `MEMORIA-GERAL.md`.
- A **09** ficou com badge apontando para a capa na prévia; a **08** aponta para o QR
  Code já montado.

### Imagens 11 e 12 são montagens do PDF de verdade

Novidade deste manual: o PDF baixado virou imagem. `capturar.py pdf` e
`capturar.py pdf_sem_fotos` baixam quatro arquivos em `/tmp`
(`cardapio-pdf-manual.pdf`, `cardapio-fotografico.pdf`, `cardapio-quadro.pdf`,
`cardapio-classico-texto.pdf`); `capturar.py render` usa **PyMuPDF** (110 dpi) para
gravar as páginas em `imagens-puras/pdf-*.png`; e o `montar()` do `annotate.py` põe
as páginas lado a lado num fundo cinza, com legenda em cima:

- **11-pdf-pronto.png** — capa (página 1) + página de itens (página 2), com 7 números
  ligando cada parte do papel ao ajuste que a controla.
- **12-modelos.png** — mesmo cardápio em Clássico (só texto), Fotográfico e Quadro.

As coordenadas dos números da 11 saíram do próprio PDF: `page.search_for()` e
`get_image_info()` do PyMuPDF devolvem as caixas em pontos, multiplicadas por
110/72. Reproduzir sem os PDFs continua possível — o `montar()` lê os PNG já
renderizados de `imagens-puras/`.

Sobras em `imagens-puras/` que **não** entram no manual: `aviso-pdf-baixado.png`
(toast *Cardápio em PDF gerado.*, usado como prova) e `extra-etapa2-so-texto.png`
(editor com as fotos desligadas).

## Ambiente: nada foi alterado

O gerador não grava nada — nem no cadastro, nem em configuração. Foram baixados
quatro PDFs (arquivos locais) e nenhum produto, preço ou setor foi tocado.
