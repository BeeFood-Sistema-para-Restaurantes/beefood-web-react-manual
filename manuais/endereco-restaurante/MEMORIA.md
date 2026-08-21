# MEMÓRIA — Manual #34 Endereço do restaurante

> Memória deste manual: decisões, descobertas e estado do ambiente.

Última atualização: 2026-08-21

---

## 1. Escopo

Pré-requisito único dos quatro manuais de área de entrega (#35 mapa, #36 KM, #37 bairro,
#38 CEP Fixo). Documenta o passo 1 (mapa + modal do número) e o passo 2 (os quatro cards).
Não ensina a configurar nenhum tipo.

---

## 2. Descobertas

- Com lat/lng já gravados, a aba abre no **passo 3**. Para voltar ao endereço: **Alterar**
  no cartão Localização. `button:has-text('Alterar')` pega também **Alterar tema** — usar
  regex `^Alterar$`.
- O número é obrigatório no modal. A busca do Places às vezes não devolve número.
- Só um tipo fica ativo. Os cadastros dos outros tipos permanecem no banco.
- O cardápio digital cacheia a config da filial: 1 a 2 minutos para o cliente ver a troca.
- Clone do Bitbucket `beetech-beeshop-nuxt` falhou com a secret `BITBUCKET_CARDAPIO_DIGITAL`
  (x-token-auth e x-bitbucket-api-token-auth). Estudo do menu foi no site ao vivo.

---

## 3. Sandbox

Empresa **BeeFood3 - Manual**, `filialID=39202`. Endereço de exemplo:
Rua Professor Osório Maia, 281, Vila Carvalho, Sorocaba – SP, CEP 18060-120.
Coordenadas `-23.4918182, -47.4642059`. Fuso Brasília (UTC-3).

Tema das capturas: claro (`theme` / `beefood-theme` = `light`).

---

## 4. Imagens

Painel 2160×1350. Não usamos `03-endereco-confirmado` (quase igual à 02) nem
`05-busca-sugestoes` (dropdown não apareceu de forma estável).
