# texto-documentation.ia.md — Cadastrar comandas e gerar o QR Code

## PROMPT (copiar e colar)

Em **Cadastros**, crie um novo item de menu por último chamado **Cadastrar comandas e gerar o QR Code**.

Leia APENAS os arquivos abaixo (não varra o resto do projeto):

1. Conteúdo (use na íntegra):
    10|   `beefood-web-react-manual/manuais/cadastro-comandas/cadastro-comandas.md`
2. Imagens (nesta ordem), em `beefood-web-react-manual/manuais/cadastro-comandas/imagens-tratadas/`:
   `01-menu-cadastros.png`, `02-tela-comandas.png`, `03-nova-comanda.png`,
   `04-excluir-comanda.png`, `05-lote-previsao.png`, `06-lote-resultado.png`, `07-qr-tipos.png`,
   `08-qr-cardapio-presencial.png`, `09-folha-impressa.png`, `10-qr-codigo-comanda.png`,
   `11-codigo-barras.png`, `12-mapa-comandas.png`

NÃO leia outros arquivos (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

- Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa".
    20|- pt-BR, didático. É um manual **de cadastro**, par do manual de mesas. Mantenha o passo a passo e
  as tabelas "Nº → o que fazer" logo depois de cada imagem.
- Manter os dois quadros de destaque: **por que o QR de comanda é melhor que o de mesa** e que o
  **código tem de ser o número impresso na comanda física**.
- Manter a seção final **Exemplo prático: 30 comandas em circulação** na ordem em que está.
- Publicar este manual **junto ou depois** do de mesas: os dois se citam.
- Não publicar nada do `fluxo-codigo.md`.

## Estrutura da página (na ordem do `.md`)

    30|1. Onde fica
2. A tela de comandas
3. Cadastrar uma comanda
4. Editar e excluir
5. Criar a faixa inteira de uma vez
6. Os três tipos de QR Code
7. O que o cadastro habilita no dia a dia
8. Exemplo prático: 30 comandas em circulação
9. Resumo
10. Perguntas frequentes
    40|11. Manuais relacionados

## Anexo — legendas das imagens (na ordem em que aparecem no texto)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|-------|----------------------------------|------|---------|
| 1 | `01-menu-cadastros.png` | com setas | Menu lateral: **Cadastros → Comandas** |
| 2 | `02-tela-comandas.png` | com setas | A tela: Nova Comanda, busca, contador, Criar em Lote e Gerar QR Code |
| 3 | `03-nova-comanda.png` | com setas | Modal **Nova Comanda**: código, descrição e Ativo |
| 4 | `04-excluir-comanda.png` | com setas | Confirmação de exclusão, que repete a descrição |
    50|| 5 | `05-lote-previsao.png` | com setas | Criar em Lote com a previsão da faixa |
| 6 | `06-lote-resultado.png` | com setas | A lista depois do lote, com o contador atualizado |
| 7 | `07-qr-tipos.png` | com setas | Os três tipos de QR Code |
| 8 | `08-qr-cardapio-presencial.png` | com setas | Faixa de comandas e os QR Codes gerados |
| 9 | `09-folha-impressa.png` | contexto | A folha pronta para imprimir e colar nas comandas |
| 10 | `10-qr-codigo-comanda.png` | com setas | QR Code **Código da Comanda** (leitura no PDV) |
| 11 | `11-codigo-barras.png` | com setas | Código de barras EAN-13 das comandas |
| 12 | `12-mapa-comandas.png` | com setas | A aba **Comandas** da tela Mesas/Comandas |

## Observações de conteúdo

    60|- A imagem **`09-folha-impressa.png`** é o que o leitor vai imprimir de verdade: publique grande.
- Manter a explicação de que o QR do cardápio gera **pela faixa informada**, mesmo que a comanda
  não exista no cadastro.
- Não publicar nomes de campo da API, rotas, IDs nem o formato interno do código lido pelo PDV.
