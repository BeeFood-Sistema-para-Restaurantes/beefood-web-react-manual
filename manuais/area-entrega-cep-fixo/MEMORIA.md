# MEMÓRIA — Manual #38 Configuração por CEP Fixo

Última atualização: 2026-08-21 (refação do zero)

Pré-requisito: #34. Flag: `tipoEntregaCepFixo`.

Sandbox limpo (`cepFixo=00000000`). Exemplo: CEP **18035-490** (Arthur Gomes, 13) e
frete **R$ 7,00**. O CEP da loja é **18040-370** — se cadastrar o da loja, o endereço de
teste fica de fora. No cardápio o cliente **busca o CEP** (não só o endereço já
selecionado). Sem tela de *Calculando…*.

Máscara de moeda/CEP: **digitar tecla a tecla**; `fill()` não dispara o React/Vue.

A tela **não grava sozinha** — único tipo da área de entrega com botão Salvar explícito no
passo 3 (além dos modais de KM/bairro).
