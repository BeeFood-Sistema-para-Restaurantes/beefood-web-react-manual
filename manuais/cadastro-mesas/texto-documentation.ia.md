# texto-documentation.ia.md — Cadastrar mesas e gerar o QR Code

## PROMPT (copiar e colar)

Em **Cadastros**, crie um novo item de menu por último chamado **Cadastrar mesas e gerar o QR Code**.

Leia APENAS os arquivos abaixo (não varra o resto do projeto):

1. Conteúdo (use na íntegra):
    10|   `beefood-web-react-manual/manuais/cadastro-mesas/cadastro-mesas.md`
2. Imagens (nesta ordem), em `beefood-web-react-manual/manuais/cadastro-mesas/imagens-tratadas/`:
   `01-menu-cadastros.png`, `02-tela-mesas.png`, `03-nova-mesa.png`, `05-editar-mesa.png`,
   `06-excluir-mesa.png`, `07-lote-conflito.png`, `08-lote-previsao.png`, `09-lote-resultado.png`,
   `10-qr-tipos.png`, `11-qr-gate-comanda.png`, `12-qr-recomendacao.png`,
   `13-qr-cardapio-presencial.png`, `14-qr-codigo-mesa.png`, `15-codigo-barras.png`,
   `16-mapa-salao.png`, `17-folha-impressa.png`, `18-cardapio-celular.png`

NÃO leia outros arquivos (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

    20|- Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. É um manual **de cadastro**: o leitor está montando a loja. Mantenha o passo a
  passo e as tabelas "Nº → o que fazer" logo depois de cada imagem.
- Manter a tabela dos **três tipos de QR Code** (cliente × operador) — é a parte que mais gera
  dúvida.
- Manter os avisos em destaque: **Ativo não é Livre**, **prefira desativar a excluir**, e que o QR
  do cardápio **gera pela faixa**, mesmo que a mesa não exista.
- Manter a seção final **Exemplo prático** na ordem em que está: cadastro → lote → QR → folha
  impressa → mapa do salão.
- Não publicar nada do `fluxo-codigo.md` (rotas, nomes de arquivo, formato interno do código).
    30|
## Estrutura da página (na ordem do `.md`)

1. Onde fica
2. A tela de mesas
3. Cadastrar uma mesa
4. Editar e excluir
5. Criar o salão inteiro de uma vez
6. Os três tipos de QR Code (Cardápio Digital Presencial / Código da Mesa / Código de Barras)
7. O que o cadastro habilita no dia a dia
    40|8. Exemplo prático: montando um salão de 19 mesas
9. Resumo
10. Perguntas frequentes
11. Manuais relacionados

## Anexo — legendas das imagens (na ordem em que aparecem no texto)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|-------|----------------------------------|------|---------|
| 1 | `01-menu-cadastros.png` | com setas | Menu lateral: **Cadastros → Mesas** |
    50|| 2 | `02-tela-mesas.png` | com setas | A tela: Nova Mesa, busca, contador, Criar em Lote e Gerar QR Code |
| 3 | `03-nova-mesa.png` | com setas | Modal **Nova Mesa**: código, descrição e Ativo |
| 4 | `05-editar-mesa.png` | com setas | Modal **Editar Mesa**, com o botão Excluir |
| 5 | `06-excluir-mesa.png` | com setas | Confirmação de exclusão, que repete a descrição da mesa |
| 6 | `07-lote-conflito.png` | com setas | Criar em Lote com **Conflito de numeração** |
| 7 | `08-lote-previsao.png` | com setas | Criar em Lote com a faixa livre e a previsão |
| 8 | `09-lote-resultado.png` | com setas | A lista depois do lote, com o contador atualizado |
| 9 | `10-qr-tipos.png` | com setas | Os três tipos de QR Code |
| 10 | `11-qr-gate-comanda.png` | com setas | A pergunta **Você usa Comanda no seu estabelecimento?** |
| 11 | `12-qr-recomendacao.png` | contexto | O comparativo QR de mesa × QR de comanda |
    60|| 12 | `13-qr-cardapio-presencial.png` | com setas | Faixa de mesas e os QR Codes do cardápio gerados |
| 13 | `14-qr-codigo-mesa.png` | com setas | QR Code **Código da Mesa** (leitura no PDV) |
| 14 | `15-codigo-barras.png` | com setas | Código de barras EAN-13 das mesas |
| 15 | `16-mapa-salao.png` | com setas | A tela Mesas/Comandas com as mesas cadastradas |
| 16 | `17-folha-impressa.png` | contexto | A folha de QR Codes pronta para imprimir e recortar |
| 17 | `18-cardapio-celular.png` | contexto | O cardápio abrindo no celular do cliente |

## Observações de conteúdo

- A imagem **`10-qr-tipos.png`** é a chave do manual: publique grande o suficiente para o leitor
   70|  ler as três descrições.
- As imagens **`17`** e **`18`** fecham o exemplo prático. Não separe uma da outra.
- Não afirmar que o cardápio do celular mostra o número da mesa na tela — o número vai no link do
  QR Code.
- Não publicar nomes de campo da API, rotas, IDs de mesa nem o formato interno do código lido pelo
  PDV.
