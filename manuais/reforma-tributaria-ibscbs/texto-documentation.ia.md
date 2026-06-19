# texto-documentation.ia.md — Reforma Tributária (IBS/CBS)

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.
> Fonte do conteúdo: `reforma-tributaria.md` (texto) + **`imagens-tratadas/`** (todas as imagens do manual).
> Obs.: `imagens-puras/` é só backup — **não referenciar**.

---

## PROMPT (copiar e colar)

Em **Fiscal**, crie um **novo item de menu por último** chamado **"Reforma Tributária"**.

Monte a página com base no projeto anexo `beefood-web-react-manual\manuais\reforma-tributaria-ibscbs`:
- O texto/passo a passo está em **`reforma-tributaria.md`** (use-o como conteúdo, na íntegra).
- **Todas as imagens** estão em **`imagens-tratadas\`** (as principais já vêm com setas verdes e números; as de contexto, sem setas). **Use somente esta pasta.**
- **Faça a apresentação das imagens igual ao menu "Abrir Caixa"** (mesmo tamanho, posição, legendas e estilo).

### Estrutura da página (seguir o `reforma-tributaria.md`)

1. **Introdução** — o que é a Reforma Tributária (IBS/CBS) e os **6 campos** por produto
   (CST IBS/CBS, cClassTrib, % Red. Alíquota, Alíq. IBS UF (%), Alíq. IBS Mun. (%), Alíq. CBS (%)).
2. **Onde ficam os campos** — menu **Fiscal → Edição Fiscal** (somente desktop) e como exibir o grupo de colunas "IBS/CBS (Reforma)".
3. **Passo a passo de edição** (selecionar produto → EDITAR IMPOSTOS → preencher → revisar → concluir).
4. **Como aparece na nota** — exemplo **ilustrativo/fictício** (não emite XML/NFC-e).
5. **Dúvidas rápidas**.

### Imagens (na ordem, com as legendas)

| Ordem | Arquivo (todos em `imagens-tratadas/`) | Tipo | Legenda |
|------:|------------------------------------------|------|---------|
| 1 | `01-edicao-fiscal-grade.png` | contexto | Tela **Edição Fiscal** (planilha de produtos) |
| 2 | `02-grupos-colunas-ibscbs.png` | contexto | Ativando o grupo de colunas **"IBS/CBS (Reforma)"** |
| 3 | `03-colunas-ibscbs-grade.png` | contexto | Colunas de IBS/CBS visíveis na planilha |
| 4 | `04-produto-selecionado-editar-impostos.png` | **com setas** | ① marcar produto · ② botão **EDITAR IMPOSTOS** |
| 5 | `07-cst-catalogo-carregado.png` | **com setas** | ① busca de CST · ② opção **000 – Tributação integral** |
| 6 | `08-modal-preenchido.png` | **com setas** | ① CST IBS/CBS · ② cClassTrib · ③ Alíq. IBS UF · ④ Alíq. CBS · ⑤ **PRÓXIMO** |
| 7 | `09-revisar-alteracoes.png` | **com setas** | ① alterações a aplicar · ② **CONFIRMAR (F2)** |
| 8 | `10-concluido.png` | contexto | Tela **"Concluído! 1 produto atualizado"** |

### Observações para o conteúdo

- Idioma: **português do Brasil**, tom didático (usuário final).
- Cada imagem com setas deve vir acompanhada da **tabela "Nº da seta → campo → o que fazer"** (já pronta no `reforma-tributaria.md`).
- Deixar **destacado** que: a tela é **somente desktop**; editar **grava no produto mas não emite nota** (é reversível); o exemplo da nota é **fictício**.
- **Não** publicar o rodapé "Referências internas" nem o arquivo `fluxo-codigo.md` (uso interno).
