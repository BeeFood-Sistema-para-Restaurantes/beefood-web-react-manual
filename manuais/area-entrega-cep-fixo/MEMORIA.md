# MEMÓRIA — Manual #38 Configuração por CEP Fixo

Última atualização: 2026-08-21

Pré-requisito: #34. Flag: `tipoEntregaCepFixo`.

Sandbox: CEP `18060-120`, valor **R$ 7,00** (gravado via API depois que o `fill` na máscara
de moeda gerou R$ 20.007,00). Máscara de moeda/CEP no painel e no menu: **digitar tecla a
tecla**; `fill()` não dispara o React/Vue.

A tela **não grava sozinha** — único tipo da área de entrega com botão Salvar explícito no
passo 3 (além dos modais de KM/bairro).
