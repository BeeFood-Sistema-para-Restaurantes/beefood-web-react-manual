# Domínio próprio no cardápio digital: como configurar o seu endereço, alterar a zona DNS e excluir

Hoje o seu cardápio digital tem um endereço do BeeFood, do tipo
`menu.beefood.com.br/beefood3`. Funciona, mas não é o endereço que está na fachada,
no cartão nem no Instagram. Com o **domínio próprio**, o cliente abre o cardápio em
`www.seurestaurante.com.br` — e é o mesmo cardápio, os mesmos produtos, os mesmos
pedidos.

Antes isso passava pelo suporte. Agora você faz tudo na tela, em
**Aplicativos → Domínio Próprio**: escolhe o cardápio, digita o endereço, o BeeFood
devolve o que você precisa configurar no seu registrador e a própria tela acompanha
o processo até o domínio ficar **No ar**.

> O BeeFood **não vende domínio**. Você precisa já ter um domínio registrado
> (Registro.br, GoDaddy, HostGator, Hostinger, Cloudflare, Locaweb…). O que fazemos
> é o apontamento desse domínio para o seu cardápio.

---

## Antes de começar

1. **Um domínio já registrado** e no ar (pago, sem pendência com o registrador).
2. **Acesso ao painel do registrador**, aquele em que você comprou o domínio. É lá
   que você vai colar o que a tela mostrar.
3. **Decidir o tipo**: usar o domínio principal (`seurestaurante.com.br`) ou criar um
   endereço novo (`cardapio.seurestaurante.com.br`). A diferença está na Parte 2 —
   ela muda o que você precisa fazer no registrador e, no caso do domínio principal,
   mexe no e-mail.
4. Cada cardápio da conta aceita **um** domínio por vez. Para trocar, exclua o atual
   (Parte 6) e cadastre outro.

---

## 1. Abrir a tela do Domínio Próprio

No menu lateral, clique em **Aplicativos** (1). Desça até o grupo **Marketing e CRM**
e abra **Domínio Próprio** (2).

![Aplicativos → Domínio Próprio](imagens-tratadas/01-aplicativos-dominio.png)

| Nº | Item | O que fazer |
|----|------|-------------|
| 1. | **Aplicativos** | Menu lateral, abre a lista de aplicativos e integrações. |
| 2. | **Domínio Próprio** | Card do grupo *Marketing e CRM*. Abre o painel do domínio. |

O painel abre pela direita e tem quatro passos no topo: **Cardápio → Tipo →
Endereço → Pronto**. Nada é gravado até o botão **CADASTRAR DOMÍNIO** do passo 3.

---

## 2. Passo 1: escolher o cardápio

Clique no cardápio que vai receber o domínio (1). Embaixo do nome aparece o endereço
atual dele, o `menu.beefood.com.br/...`.

![Passo 1 — escolher o cardápio](imagens-tratadas/02-escolher-cardapio.png)

| Nº | Item | O que fazer |
|----|------|-------------|
| 1. | **Cartão do cardápio** | Clique nele para seguir. Se a sua conta tem mais de um cardápio (multi lojas), escolha o certo — o domínio vale só para esse. |

Detalhes desta tela:

- Cardápio que **já tem domínio** mostra o endereço e uma etiqueta de situação
  (**No ar**, **Configurando...**, **Aguardando você**). Clicar nele abre a situação
  desse domínio, não um cadastro novo.
- **Domínios removidos anteriormente** é só histórico: lista o que já foi excluído.

---

## 3. Passo 2: domínio próprio ou subdomínio?

Aqui os dois caminhos se separam. Leia com calma, porque a escolha muda o que você
vai fazer no registrador.

![Passo 2 — domínio próprio ou subdomínio](imagens-tratadas/03-escolher-tipo.png)

| | **Domínio próprio** | **Subdomínio** |
|-|---------------------|----------------|
| Exemplo | `seurestaurante.com.br` | `cardapio.seurestaurante.com.br` |
| Endereço | o principal, já com o `www` incluído | um endereço novo |
| O que você faz no registrador | troca os **servidores DNS** (4 endereços) | cria **um registro CNAME** |
| Mexe no que já existe? | **Sim.** O domínio passa a ser gerenciado pelo BeeFood | **Não.** O site e o e-mail atuais continuam como estão |
| E-mail do domínio | **para de funcionar** até você recriar os registros na aba DNS | não muda nada |
| Indicado para | quem quer o endereço principal no cardápio | quem já tem site ou e-mail no domínio |

> **Se você usa e-mail nesse domínio** (`contato@seurestaurante.com.br`), pense duas
> vezes antes de escolher **Domínio próprio**. Ao trocar os servidores DNS, o e-mail
> deixa de receber mensagens até os registros serem recriados na aba **DNS** (Parte
> 5). Quando o BeeFood detecta servidores de e-mail no domínio, a própria tela
> sugere o subdomínio.

A Parte 4 segue com o **domínio próprio**. Se você escolheu **Subdomínio**, pule para
a Parte 7.

---

## 4. Parte 1 — domínio próprio: digitar e conferir o endereço

Digite o domínio **sem** `https://` e **sem** `www` (o `www` entra sozinho). Enquanto
você digita, o BeeFood confere o endereço e mostra o resultado logo abaixo.

![Passo 3 — endereço conferido](imagens-tratadas/04-endereco-conferido.png)

| Nº | Item | O que fazer |
|----|------|-------------|
| 1. | **Qual é o endereço?** * | Digite só o domínio: `cardapioteste.com.br`. O check verde à direita indica que ele foi aprovado. |
| 2. | **Vão responder por este cardápio** | Confira os endereços que vão abrir o cardápio — no domínio próprio são dois: com e sem `www`. |
| 3. | **Aviso amarelo** | Recado, não erro. Aqui ele diz que o domínio ainda não foi encontrado no DNS. Confirme com o seu registrador que o domínio está ativo. |
| 4. | **CADASTRAR DOMÍNIO** | Grava o pedido. Só habilita depois da conferência aprovar o endereço. |

O bloco **O próximo passo será** adianta o que vem depois — no domínio próprio,
trocar os servidores DNS no painel do registrador.

Se o endereço for recusado, a tela explica o motivo e oferece a saída:

| Mensagem | O que significa | O que fazer |
|----------|-----------------|-------------|
| Endereço inválido (em vermelho, no campo) | falta o `.com.br`, sobrou `https://`, tem espaço | corrija o texto |
| O domínio tem e-mail configurado | trocar os DNS derrubaria o e-mail | use o **subdomínio** sugerido no botão |
| Este cardápio já tem um domínio | um cardápio, um domínio | veja o domínio atual ou exclua-o antes |
| Endereço em uso por outra empresa | o domínio está cadastrado em outra conta BeeFood | fale com o suporte pelo link da própria tela |

---

## 5. Parte 1 — domínio próprio: trocar os servidores DNS

Depois de **CADASTRAR DOMÍNIO**, a tela avisa que o pedido foi registrado e passa a
preparar os dados do seu DNS (1). Isso leva cerca de **um minuto**; deixe a tela
aberta, os dados aparecem sozinhos.

![Domínio cadastrado, preparando os dados do DNS](imagens-tratadas/05-cadastrado-preparando.png)

| Nº | Item | O que fazer |
|----|------|-------------|
| 1. | **Estamos preparando os dados do seu DNS** | Só esperar. A lista de etapas acima mostra em que ponto o processo está. |

Quando termina, aparece o cartão **Troque os servidores DNS do seu domínio** com os
**quatro servidores** que você precisa levar para o painel do seu registrador.

![Os quatro servidores DNS](imagens-tratadas/06-instrucao-ns.png)

| Nº | Item | O que fazer |
|----|------|-------------|
| 1. | **Copiar todos** | Copia os quatro servidores de uma vez. Cada linha também tem um botão próprio de copiar. |
| 2. | **Os quatro servidores DNS** | No painel do registrador, **substitua** os servidores atuais por estes quatro. Não some com os antigos: troque. |
| 3. | **Já configurei, verificar agora** | Clique **depois** de gravar no registrador. Assim o BeeFood confere na hora, em vez de esperar a próxima verificação automática. |

No painel do registrador esse campo aparece com nomes diferentes: *Servidores DNS*,
*Alterar servidores DNS*, *Nameservers*, *DNS personalizado* ou *Usar servidores de
outro provedor*. É sempre a mesma coisa: quatro linhas para colar.

Enquanto o domínio espera por você, a etiqueta ao lado do nome fica em **Aguardando
você**, e a tela se atualiza sozinha. A troca de servidores DNS **pode levar algumas
horas** para valer em toda a internet — é normal, e não há nada a fazer nesse tempo
além de esperar.

---

*Manual em produção — as partes de domínio no ar, alteração da zona DNS, exclusão e
subdomínio entram quando a troca de DNS do domínio de teste for concluída.*
