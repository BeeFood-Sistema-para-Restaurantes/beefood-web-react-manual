# Prompt para publicar o manual — Avisos do cardápio digital (#47)

> Cole o texto abaixo na IA de documentação do app, junto com as 11 imagens da pasta
> `imagens-tratadas/`, na ordem da tabela do fim.

---

## Instrução

Publique um manual de usuário final chamado **"Avisos do cardápio digital"**, na seção
**Cardápio Digital**. Use o conteúdo de
`manuais/cardapio-digital-avisos/cardapio-digital-avisos.md` como fonte, **sem reescrever
o texto** — ele já está no padrão dos outros manuais publicados.

### Estrutura a preservar

1. Duas coisas antes (sem data de calendário; sem botão Salvar na aba; atraso de 1 min)
2. Onde fica (menu Avisos, regras, dropzone)
3. Parte 1 — Enviar a imagem (cartaz 1:1, título obrigatório)
4. Parte 2 — Recado do feriado
5. Parte 3 — Horário novo com faixa
6. Parte 4 — Só no delivery
7. Parte 5 — Lista, ordem e apagar
8. Parte 6 — Cliente no computador
9. Parte 7 — Cliente no celular
10. Resumo, FAQ, manuais relacionados

### Pontos que NÃO podem se perder

- **Aviso não vende.** Sem call to action. Combo/produto é Destaque, não aviso.
- A imagem **é** a mensagem: cartaz quadrado, texto grande. Foto distante some no celular.
- **Não existe data de calendário** — só dia da semana. Feriado: ligar e depois pausar.
- **Título obrigatório.** Sem descrição, o toque no card **não abre** detalhe.
- Fechar o modal de um aviso novo **descarta**.
- Faixa de hora **não cruza meia-noite**; início tem que ser menor que o fim.
- Quem decide se está no ar é o **relógio do cliente**. Até 1 minuto de cache.
- Até **10** avisos. Sem nenhum, a faixa some.

---

## Imagens, na ordem

Todas em `manuais/cardapio-digital-avisos/imagens-tratadas/`.

| # | Arquivo | Tipo | Legenda / o que mostra |
|---|---------|------|------------------------|
| 1 | `01-aba-vazia.png` | setas | Aba vazia · 1 menu Avisos · 2 regras · 3 dropzone |
| 2 | `02-modal-titulo-vazio.png` | setas | Modal novo · 1 título * · 2 descrição · 3 SALVAR (F2) |
| 3 | `03-modal-feriado.png` | setas | Feriado · 1 cartaz · 2 título · 3 descrição · 4 dias · 5 SALVAR |
| 4 | `04-modal-horario.png` | setas | Faixa · 1 DOM off · 2 Dia inteiro off · 3 Início · 4 Fim |
| 5 | `05-modal-delivery.png` | setas | Canal · 1 Delivery · 2 Presencial off |
| 6 | `06-lista-tres-avisos.png` | setas | Lista · 1 dropzone · 2 feriado · 3 horário · 4 só delivery |
| 7 | `07-confirmar-remover.png` | setas | Remover · 1 REMOVER (ENTER) |
| 8 | `09-cardapio-desktop.png` | setas | Cardápio desktop · 1 feriado · 2 horário · 3 só delivery |
| 9 | `10-cardapio-desktop-modal.png` | contexto | Modal do aviso no computador (só fecha) |
| 10 | `11-cardapio-mobile.png` | setas | Cardápio mobile · 1 feriado · 2 horário |
| 11 | `12-cardapio-mobile-modal.png` | contexto | Modal do aviso no celular (FECHAR) |
