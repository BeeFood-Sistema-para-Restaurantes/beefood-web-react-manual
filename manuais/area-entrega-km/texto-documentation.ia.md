# Prompt para publicar o manual — Configuração por KM (#36)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `area-entrega-km.md`
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

Publique **"Configuração por KM"** na seção **Cardápio Digital**, usando
`manuais/area-entrega-km/area-entrega-km.md` **sem reescrever**. Depende do #34.

### Pontos que NÃO podem se perder

- A distância começa no pin da loja (**R. Caramuru, 108**).
- Cada faixa é um **teto** (“até X km”). Quem passa da maior fica de fora.
- Frete grátis, tempo adicional e valor do entregador (este último só no relatório).
  Frete grátis **0** = não usa a regra.
- Teste no cardápio: o cliente **busca o CEP 18035-490**, confirma o número **13** e vê
  **R$ 5,99** (faixa de 3 km).
- **1 a 2 minutos** para o cardápio atualizar; o cliente deve **Trocar** o endereço.

### Imagens, na ordem

| # | Arquivo | Tipo |
|---|---------|------|
| 1 | `01-step2-km.png` | setas |
| 2 | `05-lista-km-pronta.png` | setas |
| 3 | `03-modal-km-vazio.png` | setas |
| 4 | `04-modal-km-preenchido.png` | setas |
| 5 | `06-menu-km-busca.png` | setas |
| 6 | `07-menu-km-form.png` | setas |
| 7 | `08-menu-km-perto.png` | setas |
