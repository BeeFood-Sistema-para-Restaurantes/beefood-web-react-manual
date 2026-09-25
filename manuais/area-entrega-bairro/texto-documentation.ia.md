# Prompt para publicar o manual — Configuração por bairro (#37)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `area-entrega-bairro.md`
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

Publique **"Configuração por bairro"** na seção **Cardápio Digital**, usando
`manuais/area-entrega-bairro/area-entrega-bairro.md` **sem reescrever**. Depende do #34.

### Pontos que NÃO podem se perder

- O nome do bairro precisa ser o **mesmo do correio**.
- O botão **+** inclui o bairro na tabela; sem ele o grupo sai vazio.
- O mesmo modal tem rádios **CEP** e **Faixa CEP**.
- Exemplo: grupo **Centro** / R$ 6,50 / frete grátis R$ 45,00.
- Teste no cardápio: o cliente **busca o bairro Centro**, completa a rua
  **Arthur Gomes, 13** e vê **R$ 6,50**.
- **1 a 2 minutos** para o cardápio; o cliente deve **Trocar** o endereço.

### Imagens, na ordem

| # | Arquivo | Tipo |
|---|---------|------|
| 1 | `01-step2-bairro.png` | setas |
| 2 | `05-lista-bairro-pronta.png` | setas |
| 3 | `03-modal-bairro.png` | setas |
| 4 | `04-modal-bairro-preenchido.png` | setas |
| 5 | `06-menu-bairro-busca.png` | setas |
| 6 | `07-menu-bairro-form.png` | setas |
| 7 | `08-menu-bairro-perto.png` | setas |
