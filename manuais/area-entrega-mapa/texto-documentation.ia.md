# Prompt para publicar o manual — Configuração por mapa (#35)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `area-entrega-mapa.md`
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

Publique **"Configuração por mapa (área)"** na seção **Cardápio Digital**, usando
`manuais/area-entrega-mapa/area-entrega-mapa.md` **sem reescrever**. Depende do #34.

### Pontos que NÃO podem se perder

- Precisa do endereço da loja (#34) — **R. Caramuru, 108**.
- **Círculo** (clique e arraste) e **polígono** (ponto a ponto, com Voltar/Avançar/Resetar).
- Campos de cada região: nome, cor, ativo, **taxa**, **frete grátis**, **tempo adic.**,
  **entregador** (só no relatório).
- **Não entrega nessa região** bloqueia o ponto mesmo se outra área cobrir; esconde os
  quatro valores e pinta de preto.
- Só um tipo ativo; as áreas ficam salvas se trocar para KM.
- Cardápio: o cliente **busca o CEP 18035-490**, confirma o número **13** e vê a taxa
  da região (exemplo **R$ 5,99** no círculo de 2 km).
- Atualização em **1 a 2 minutos**; o cliente deve **Trocar** o endereço.

### Imagens, na ordem

| # | Arquivo | Tipo |
|---|---------|------|
| 1 | `02-step2-tipos.png` | setas |
| 2 | `03-nova-regiao-tipo.png` | setas |
| 3 | `04b-form-circulo-campos.png` | setas |
| 4 | `04c-nao-entrega.png` | setas |
| 5 | `04d-desenhando-poligono.png` | setas |
| 6 | `01-step3-regioes.png` | setas |
| 7 | `05-editar-regiao.png` | setas |
| 8 | `07-menu-busca.png` | setas |
| 9 | `08-menu-form.png` | setas |
| 10 | `09-menu-dentro-area.png` | setas |
