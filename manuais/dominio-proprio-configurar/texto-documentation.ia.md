# texto-documentation.ia.md — #101 Domínio próprio e subdomínio pela tela

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `dominio-proprio-configurar.md`
  e das imagens listados neste prompt.
- **Não publique**, em nenhuma seção: rota ou URL de API (`/api/...`); nome de campo,
  de arquivo, de componente, de tabela ou de coluna; bloco de código, JSON ou
  `campo=true`; nem as palavras *backend*, *endpoint*, *payload*, *array*, *bundle*.
  Se a frase só faz sentido para quem programa, ela não entra. Única exceção: a URL
  completa de webhook que o lojista copia para o painel do parceiro.
- Se você leu **qualquer outro arquivo** desta pasta — `fluxo-codigo.md`,
  `MEMORIA.md`, `annotate.py`, `capturar.py` —, **descarte o que leu**: são anotações
  internas de quem produziu o manual.
- Em 23/09/2026 uma página publicada saiu com a rota da API do cupom e dois nomes de
  campo do cashback, porque esta regra não estava aqui em cima.

Em **Cardápio Digital**, adicione um item de menu chamado **Domínio próprio e
subdomínio**, logo depois do manual de domínio antigo (#52).

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/dominio-proprio-configurar/dominio-proprio-configurar.md`
2. Imagens (nesta ordem):
   - `.../imagens-tratadas/01-aplicativos-dominio.png`
   - `.../imagens-tratadas/02-escolher-cardapio.png`
   - `.../imagens-tratadas/03-escolher-tipo.png`
   - `.../imagens-tratadas/04-endereco-conferido.png`
   - `.../imagens-tratadas/05-cadastrado-preparando.png`
   - `.../imagens-tratadas/06-instrucao-ns.png`
   - `.../imagens-tratadas/07-dominio-no-ar.png`
   - `.../imagens-tratadas/08-aba-dns.png`
   - `.../imagens-tratadas/09-form-registro.png`
   - `.../imagens-tratadas/10-registro-criado.png`
   - `.../imagens-tratadas/11-propagacao.png`
   - `.../imagens-tratadas/12-historico-dns.png`
   - `.../imagens-tratadas/13-excluir-botao.png`
   - `.../imagens-tratadas/14-confirmar-exclusao.png`
   - `.../imagens-tratadas/15-apos-exclusao.png`
   - `.../imagens-tratadas/16-subdominio-conferido.png`
   - `.../imagens-tratadas/17-instrucao-cname.png`
   - `.../imagens-tratadas/18-subdominio-no-ar.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `capturar.py`,
`imagens-puras/`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR. Manter as tabelas de setas (nº → item → o que fazer) embaixo de cada imagem.
- Este manual **substitui** o pedido por suporte do #52 na parte de configuração.
  Do #52 continua valendo só a **verificação na Meta**: linkar, não repetir.
- Destacar as diferenças entre os dois caminhos: **domínio próprio** troca os
  servidores DNS (mexe no e-mail, ganha a aba **DNS**) e **subdomínio** só cria um
  CNAME (não mexe em nada do que já existe).
- Deixar claro que o BeeFood **não vende domínio** e que o link
  `menu.beefood.com.br/...` **continua funcionando** depois de tudo.
- **SEO**: manter os títulos e as perguntas com as palavras de busca do usuário
  (*domínio próprio no cardápio*, *usar meu domínio no lugar do link do BeeFood*,
  *como apontar meu domínio*, *criar CNAME do cardápio*, *e-mail parou depois de
  trocar o DNS*, *quanto tempo leva a propagação*, *excluir domínio do cardápio*).
  Não trocar por sinônimos genéricos nem resumir a FAQ.
- Não publicar `empresaID`, rotas de API nem nomes de componente.

## Estrutura da página

1. Antes de começar
2. Abrir a tela do Domínio Próprio
3. Passo 1: escolher o cardápio
4. Passo 2: domínio próprio ou subdomínio?
5. Parte 1 — domínio próprio: digitar e conferir o endereço
6. Parte 1 — domínio próprio: trocar os servidores DNS
7. Parte 1 — domínio próprio: o domínio no ar
8. Parte 1 — domínio próprio: alterar a zona DNS
9. Parte 1 — domínio próprio: excluir o domínio
10. Parte 2 — subdomínio: digitar e conferir o endereço
11. Parte 2 — subdomínio: criar o CNAME
12. Parte 2 — subdomínio: o subdomínio no ar
13. Problemas comuns
14. Perguntas frequentes
15. Manuais relacionados (#52 para a verificação na Meta)

## Anexo — legendas

| Ordem | Arquivo | Tipo | Legenda |
|-------|---------|------|---------|
| 1 | `01-aplicativos-dominio.png` | com setas | Onde fica o card Domínio Próprio |
| 2 | `02-escolher-cardapio.png` | com setas | Passo 1 — o cardápio que recebe o domínio |
| 3 | `03-escolher-tipo.png` | contexto | Os dois caminhos: domínio próprio e subdomínio |
| 4 | `04-endereco-conferido.png` | com setas | Endereço conferido, com o aviso do e-mail |
| 5 | `05-cadastrado-preparando.png` | com setas | Cadastrado, preparando os dados do DNS |
| 6 | `06-instrucao-ns.png` | com setas | Os quatro servidores DNS para colar no registrador |
| 7 | `07-dominio-no-ar.png` | com setas | Domínio no ar, com as cinco etapas concluídas |
| 8 | `08-aba-dns.png` | com setas | Aba DNS: a zona, com os registros de cadeado |
| 9 | `09-form-registro.png` | com setas | Formulário do registro (MX do e-mail) |
| 10 | `10-registro-criado.png` | com setas | Registro criado, com lápis e lixeira |
| 11 | `11-propagacao.png` | com setas | Aviso de propagação depois de alterar |
| 12 | `12-historico-dns.png` | com setas | Histórico da zona, com Antes e Depois |
| 13 | `13-excluir-botao.png` | com setas | Excluir domínio, no rodapé do painel |
| 14 | `14-confirmar-exclusao.png` | com setas | Confirmação da exclusão |
| 15 | `15-apos-exclusao.png` | com setas | Cardápio livre e a lista de removidos |
| 16 | `16-subdominio-conferido.png` | com setas | Endereço do subdomínio conferido |
| 17 | `17-instrucao-cname.png` | com setas | Tipo, Nome e Valor do CNAME |
| 18 | `18-subdominio-no-ar.png` | com setas | Subdomínio no ar |
