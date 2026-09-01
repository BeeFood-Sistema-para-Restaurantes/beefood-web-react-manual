# texto-documentation.ia.md — Grupos de Acesso (estudo completo)

## PROMPT (copiar e colar)

Em **Configuração**, crie um novo item de menu por último chamado **Grupos de Acesso**.

Leia APENAS os arquivos abaixo (não varra o resto do projeto):

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/grupos-acesso/grupos-acesso.md`
2. Imagens (nesta ordem):
   - `beefood-web-react-manual/manuais/grupos-acesso/imagens-tratadas/01-usuarios-aba-usuarios.png`
   - `beefood-web-react-manual/manuais/grupos-acesso/imagens-tratadas/20-cadastro-usuario-gerente.png`
   - `beefood-web-react-manual/manuais/grupos-acesso/imagens-tratadas/02-aba-grupos-de-acesso.png`
   - `beefood-web-react-manual/manuais/grupos-acesso/imagens-tratadas/03-modal-grupo-todas-permissoes.png`
   - `beefood-web-react-manual/manuais/grupos-acesso/imagens-tratadas/04-filtro-por-recurso.png`
   - `beefood-web-react-manual/manuais/grupos-acesso/imagens-tratadas/05-busca-permissao.png`
   - `beefood-web-react-manual/manuais/grupos-acesso/imagens-tratadas/06-acoes-do-cardapio.png`
   - `beefood-web-react-manual/manuais/grupos-acesso/imagens-tratadas/30a-lista-cardapio-completo.png`
   - `beefood-web-react-manual/manuais/grupos-acesso/imagens-tratadas/30b-produto-completo.png`
   - `beefood-web-react-manual/manuais/grupos-acesso/imagens-tratadas/31-comparativo-sem-editar.png`
   - `beefood-web-react-manual/manuais/grupos-acesso/imagens-tratadas/32-comparativo-sem-preco.png`
   - `beefood-web-react-manual/manuais/grupos-acesso/imagens-tratadas/33-comparativo-sem-ativo.png`
   - `beefood-web-react-manual/manuais/grupos-acesso/imagens-tratadas/33b-comparativo-menu-card-sem-ativo.png`
   - `beefood-web-react-manual/manuais/grupos-acesso/imagens-tratadas/34-comparativo-menu-card-sem-excluir.png`
   - `beefood-web-react-manual/manuais/grupos-acesso/imagens-tratadas/34b-comparativo-menu-opcoes-sem-excluir.png`
   - `beefood-web-react-manual/manuais/grupos-acesso/imagens-tratadas/35-comparativo-sem-novo-lote.png`
   - `beefood-web-react-manual/manuais/grupos-acesso/imagens-tratadas/36-comparativo-menu-cardapio.png`

NÃO leia outros arquivos (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

- Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa".
- pt-BR, didático; destacar obrigatórios; **não publicar** o rodapé "Referências internas".
- As tabelas do catálogo (seção 4) são o coração do conteúdo: preserve todas as linhas.
- Sete das imagens são **comparativos lado a lado** (dois painéis com título "Com…" e "Sem…").
  Apresente cada uma em largura cheia, para os dois lados ficarem legíveis.

## Estrutura da página (na ordem do `grupos-acesso.md`)

1. O mapa geral — as 93 permissões, as 10 categorias e os três comportamentos
2. Onde tudo se configura — Configuração → Usuários, cadastro do usuário, modal do grupo,
   filtro por categoria e busca
3. Seis regras que evitam dor de cabeça
4. Catálogo completo, por categoria (10 tabelas)
5. A tela de cadastro de produto, restrição por restrição (7 sub-seções + o que não dá para
   restringir)
6. As restrições de dentro do Caixa
7. O que o grupo de acesso não controla
8. Uma permissão, duas telas
9. Perfis prontos
10. Resumo: quero que ele não consiga…
11. Dicas finais

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|-------|----------------------------------|------|---------|
| 1 | `01-usuarios-aba-usuarios.png` | com setas | Configuração → Usuários: as duas abas e o grupo de cada pessoa |
| 2 | `20-cadastro-usuario-gerente.png` | com setas | Cadastro do usuário: Grupo de Acesso, Gerente e Aplicativos |
| 3 | `02-aba-grupos-de-acesso.png` | com setas | Aba Grupos de Acesso, com os grupos da empresa |
| 4 | `03-modal-grupo-todas-permissoes.png` | com setas | O modal de permissões, agrupado por categoria |
| 5 | `04-filtro-por-recurso.png` | com setas | O filtro aberto, com as dez categorias |
| 6 | `05-busca-permissao.png` | com setas | Busca por "caixa" dentro do modal |
| 7 | `06-acoes-do-cardapio.png` | com setas | Os seis sub-itens de Cadastro de Cardápio |
| 8 | `30a-lista-cardapio-completo.png` | com setas | Lista do Cardápio com todas as permissões ligadas |
| 9 | `30b-produto-completo.png` | com setas | Cadastro de produto com todas as permissões ligadas |
| 10 | `31-comparativo-sem-editar.png` | comparativo | Campos do produto com e sem *Editar (exceto preço)* |
| 11 | `32-comparativo-sem-preco.png` | comparativo | Preço de Venda e Custo com e sem *Editar Preço* (idênticos) |
| 12 | `33-comparativo-sem-ativo.png` | comparativo | Aba Cardápios com e sem *Editar Ativo* |
| 13 | `33b-comparativo-menu-card-sem-ativo.png` | comparativo | Menu do produto com e sem *Editar Ativo* |
| 14 | `34-comparativo-menu-card-sem-excluir.png` | comparativo | Menu do produto com e sem *Excluir* |
| 15 | `34b-comparativo-menu-opcoes-sem-excluir.png` | comparativo | Menu OPÇÕES com e sem *Excluir* |
| 16 | `35-comparativo-sem-novo-lote.png` | comparativo | Cabeçalho do Cardápio com e sem *Adicionar Novo* e *Editar em Lote* |
| 17 | `36-comparativo-menu-cardapio.png` | comparativo | Menu lateral com e sem *Cadastro de Cardápio* |

## Observações de conteúdo

- O estudo tem duas mensagens que não podem ser suavizadas na publicação:
  **(a)** *Editar Preço* e *Editar (exceto preço)* travam campos **sem mudar a aparência** deles;
  **(b)** não existe permissão para esconder o **Custo** do produto.
- A seção 7 (o que o grupo **não** controla) responde à maioria das dúvidas de suporte —
  mantenha-a inteira, inclusive a lista de integrações.
- Não publicar `fluxo-codigo.md` nem `MEMORIA.md`: eles têm nomes de chaves internas, itemIDs e
  o método do experimento.
