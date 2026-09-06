# texto-documentation.ia.md — Comissão do garçom: cadastrar e lançar

## PROMPT (copiar e colar)

Em **Cadastros**, adicione um item de menu por último chamado **Comissão do Garçom**.

Leia APENAS os arquivos abaixo (não varra o resto do projeto):

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/comissao-garcom-cadastrar/comissao-garcom-cadastrar.md`
2. Imagens (nesta ordem):
   - `beefood-web-react-manual/manuais/comissao-garcom-cadastrar/imagens-tratadas/01-lista-funcionarios.png`
   - `beefood-web-react-manual/manuais/comissao-garcom-cadastrar/imagens-tratadas/02-ana-dados.png`
   - `beefood-web-react-manual/manuais/comissao-garcom-cadastrar/imagens-tratadas/03-ana-funcao.png`
   - `beefood-web-react-manual/manuais/comissao-garcom-cadastrar/imagens-tratadas/04-usuario-ana.png`
   - `beefood-web-react-manual/manuais/comissao-garcom-cadastrar/imagens-tratadas/05-lista-usuarios.png`
   - `beefood-web-react-manual/manuais/comissao-garcom-cadastrar/imagens-tratadas/06-garcom-ana.png`
   - `beefood-web-react-manual/manuais/comissao-garcom-cadastrar/imagens-tratadas/07-pedido-ana.png`
   - `beefood-web-react-manual/manuais/comissao-garcom-cadastrar/imagens-tratadas/09-prova-comissao.png`

NÃO leia outros arquivos (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

- Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter o quadro dos três jeitos de identificar o garçom e os links
  para código do operador, app garçom, relatório de comissão e relatório de taxa.
- **Não publicar** o rodapé "Referências internas" nem senhas/logins de teste como
  instrução de produção — o exemplo Ana/Bruno pode ficar.

## Estrutura da página (na ordem do `.md`)

1. Comissão só existe quando o sistema sabe quem lançou
2. Cadastrar o garçom e o percentual
3. Vincular o usuário ao funcionário
4. Lançar logado como o garçom
5. A prova no relatório
6. Perguntas rápidas

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo | Tipo | Legenda |
|-------|---------|------|---------|
| 1 | `01-lista-funcionarios.png` | com setas | Cadastros → Funcionários, com Ana e Bruno |
| 2 | `02-ana-dados.png` | com setas | Aba Dados: nome e código de operador |
| 3 | `03-ana-funcao.png` | com setas | Aba Função: Garçom e Comissão 10% |
| 4 | `04-usuario-ana.png` | com setas | Novo usuário ligado à Ana |
| 5 | `05-lista-usuarios.png` | com setas | Lista com ana.garcom e bruno.garcom |
| 6 | `06-garcom-ana.png` | com setas | Novo pedido com Garçom já preenchido |
| 7 | `07-pedido-ana.png` | com setas | Mesa 16 com os dois itens e a taxa |
| 8 | `09-prova-comissao.png` | com setas | Relatório: Ana 10% e Bruno 5% |

## Observações de conteúdo

- A mensagem que não pode ser suavizada: **sem identidade (app / usuário / operador) não
  há comissão**, mesmo escolhendo o nome na mesa.
- Linkar Código do operador; não ensinar o teclado de novo.
- Não publicar `fluxo-codigo.md` nem `MEMORIA.md`.
