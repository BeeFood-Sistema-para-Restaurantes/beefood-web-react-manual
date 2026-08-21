# MEMÓRIA — Manual #34 Endereço do restaurante

> Memória deste manual: decisões, descobertas e estado do ambiente.

Última atualização: 2026-08-21 (refação do zero)

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
- Campo da API: `endereco` (não `rua`).

---

## 3. Sandbox

Empresa **BeeFood3 - Manual**, `filialID=39202`.

Endereço da loja (já atualizado pelo dono; o manual **redigita o mesmo**):
**R. Caramuru, 108 — Vila Leão, Sorocaba – SP, 18040-370**.
Coordenadas `-23.5061438, -47.4657927`. Fuso Brasília (UTC-3).

Endereço de entrega de teste (sempre este, nos quatro tipos):
**R. Arthur Gomes, 13 — Centro, Sorocaba – SP, 18035-490**.

Tema das capturas: claro (`theme` / `beefood-theme` = `light`).

---

## 4. Imagens

Painel 2160×1350. `03-endereco-confirmado` ficou nas puras (quase igual à 02) e não entra
no manual. `05-busca-sugestoes` entra — é a digitação de *Rua Caramuru, 108, Vila Leão,
Sorocaba*.
