# MEMÓRIA — Manual #37 Configuração por bairro

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `area-entrega-bairro.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Última atualização: 2026-08-21 (refação do zero)

Pré-requisito: #34. Flag: `tipoEntregaCep`.

O dono limpou todos os grupos. Exemplo do zero: um grupo **Bairro** com **Centro**
(Sorocaba), frete R$ 6,50, frete grátis R$ 45,00, +8 min, entregador R$ 3,50.

O botão **+** do modal é obrigatório — sem ele o SALVAR grava grupo vazio.

Teste no cardápio: o cliente **busca o bairro Centro**, completa a rua
**Arthur Gomes, 13** e vê **R$ 6,50**. Sem tela de *Calculando…* / bairro de fora.

Ctrl+K (busca rápida do painel) intercepta cliques; Escape fecha.
