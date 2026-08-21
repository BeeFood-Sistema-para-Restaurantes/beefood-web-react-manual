# MEMÓRIA — #39 Senha gerente

Status: ✅ Concluído em 21/08/2026. Sandbox BeeFood3 - Manual (`empresaID` 38311).

## Decisões

- Usuário novo `atendente.parametros` / `manual123`, Gerente OFF, grupo Acesso Funcionário (71880). **Não** reusar `contato@` nem `caixa.manual`.
- Prova principal: PDV → Editar Valores → modal **Liberação de Desconto**.
- `geDescMax` preenchido com 10 (a tela pode mostrar `010`). O teto vale inclusive para gerente (`useDescontoGuard`).
- `motivoCancelamento` ficou OFF na prova da senha para o modal de senha aparecer direto. Quando ON, o motivo vem antes (`useDescontoGuard`).
- Senha do gerente na validação: a do `contato@` — **não publicar** no texto do manual.

## Capturas

Playwright 1440×900, DPR 1.5, tema claro, `LANG=pt_BR.UTF-8`. Novidades do Sistema interceptam cliques — dismiss com **AGORA NÃO (ESC)**.

O clique por coordenada no ícone % abriu o Ctrl+K; o botão certo é `button` com texto `%` no rodapé do pedido.

## Estado deixado

Usuário `atendente.parametros` **mantido**. Switches de senha gerente ligados (os 6) + teto 10. Motivo e operador foram religados/desligados ao longo do bloco — ver MEMORIA dos #42+.
