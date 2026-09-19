#!/usr/bin/env node
/**
 * smoke-app.js — monta e confere os cenários que faltam de foto no app do entregador.
 *
 * O `cenario.js` ao lado monta o que o **painel** precisa. Este monta o que a **tela do
 * celular** precisa, e a diferença não é de grau: a lista do app não sai do painel nem da
 * rota, sai de uma coluna do pedido (`FuncionarioIDMotoboy`) e de duas situações de
 * delivery. Pedido sem essa coluna preenchida não existe para o app, por mais bonito que
 * esteja na tela do operador.
 *
 * Ele existe porque as capturas que faltam nos manuais #111 a #117 não são "abrir a tela e
 * fotografar": cada uma exige um estado que ninguém alcança clicando — pedido de
 * marketplace já pago, pedido com saldo zerado, entrega tirada do entregador no meio,
 * histórico vazio, rota chegando ao vivo. Cada `--caso` deste arquivo é **uma foto pedida**
 * em `../pedidos/capturas-app.md`.
 *
 * ---------------------------------------------------------------------------------------
 * NENHUMA CREDENCIAL MORA AQUI
 * ---------------------------------------------------------------------------------------
 * Igual ao `cenario.js`, e pelo mesmo motivo (o repositório é público): host, senha e
 * segredo são lidos do clone do backend, pelo caminho em `--backend` ou `BEETECH_BACKEND`.
 * O que fica escrito neste arquivo são IDs da sandbox, que não são segredo, e os textos de
 * identificador de marketplace, que são inventados.
 *
 * ---------------------------------------------------------------------------------------
 * COMO ELE EVITA ESTRAGO
 * ---------------------------------------------------------------------------------------
 * 1. **Lista branca de alvo** (38311/39202), herdada do `cenario.js`. Outra empresa aborta.
 * 2. **Sentinela de escrita no ERP**: `UPDATE` só em `_PreVenda`, só em `preVendaID` que
 *    este arquivo criou ou achou com o marcador do seeder, só nas colunas da lista branca
 *    `COLUNAS_GRAVAVEIS`, e sempre com `filialID` da lista branca no `WHERE`.
 * 3. **Escrita com data no passado exige `--permitir-passado`.** Mexer em data de entrega é
 *    o único caso que altera histórico, e histórico é o que o relatório soma.
 * 4. **`--dry-run` em tudo.**
 * 5. **`limpar` não apaga pedido.** Ele desatribui o entregador, que é o que tira o pedido
 *    da tela do app sem mexer no que o ERP registrou — mesma escolha do gerador do dono. O
 *    `arquivar-fila` vai um passo além, para o painel, e também não apaga: manda o pedido
 *    para `AGUARDANDO`, que é o estado que as duas telas ignoram.
 *
 * ---------------------------------------------------------------------------------------
 * USO
 * ---------------------------------------------------------------------------------------
 *   node smoke-app.js casos                        <- a lista, com a foto de cada um
 *   node smoke-app.js estado                       <- o que o app está vendo agora
 *   node smoke-app.js preparar --caso lista
 *   node smoke-app.js preparar --caso rota-viva
 *   node smoke-app.js preparar --caso marketplace
 *   node smoke-app.js preparar --caso keeta
 *   node smoke-app.js preparar --caso pago
 *   node smoke-app.js preparar --caso notificacao
 *   node smoke-app.js preparar --caso troca --de 194115 --para 194116
 *   node smoke-app.js preparar --caso historico-vazio
 *   node smoke-app.js preparar --caso historico-dias --permitir-passado
 *   node smoke-app.js janela-117 --fase 1          <- o roteiro do #117, fase por fase
 *   node smoke-app.js conferir
 *   node smoke-app.js limpar                       <- tira da tela do app
 *   node smoke-app.js arquivar-fila                <- tira da fila do painel, lotes antigos
 *
 * Todos aceitam `--backend`, `--empresa`, `--filial`, `--usuario`, `--entregador` e
 * `--dry-run`.
 */

'use strict';

const fs = require('fs');
const path = require('path');

const cen = require('./cenario.js');

const CONFIG = {
    ...cen.CONFIG,
    // O entregador de captura: `BeeFood3 - Manual`. É o único com app instalado no emulador
    // do dono, e é ele que aparece nos quinze capítulos do material.
    entregador: 194115,
    // O segundo entregador serve a um caso só: a entrega ser **tirada** do primeiro.
    entregadorAlternativo: 194116,
    estado: path.join(__dirname, '.smoke-app-estado.json'),
};

/**
 * Colunas que este arquivo pode escrever em `_PreVenda`, e por que cada uma.
 *
 * A lista é curta de propósito: é ela que impede um erro de digitação virar escrita em
 * coluna fiscal. Tudo aqui é campo que a tela do app lê, nada mais.
 */
const COLUNAS_GRAVAVEIS = new Set([
    'FuncionarioIDMotoboy',  // é ela que põe o pedido na lista do app
    'SituacaoDelivery',      // o app ignora AGUARDANDO e ENTREGUE
    'ValorPago',             // zera o "Cobrar R$" — é assim que pedido pago se comporta
    'troco',                 // alimenta o "Troco para quanto?"
    'TipoPag',               // forma prevista, numérica
    'tipoPagStr',            // forma prevista, texto — é o que o rodapé mostra
    'TipoPagBandeiraStr',    // bandeira prevista
    'correlationId',         // identificador de pedido iFood
    'ifoodLocalizer',        // localizador de 8 dígitos do iFood
    'ifoodShortReference',   // referência curta (a "Coleta") e o localizador do 99Food
    'nnID',                  // identificador de pedido 99Food
    'keetaId',               // identificador de pedido Keeta — selo sem confirmação
    'marketPlace',           // marca o pedido como de plataforma
    'DataHoraEntregue',      // carimbo de entrega: histórico e relatório
    'dataEntrega',           // data de entrega prevista/realizada
    'HoraEntrega',           // hora de entrega prevista/realizada
]);

/** Só com `--permitir-passado`: são as três que mexem em histórico já fechado. */
const COLUNAS_DE_DATA = new Set(['DataHoraEntregue', 'dataEntrega', 'HoraEntrega']);

// ---------------------------------------------------------------------------
// Flags
// ---------------------------------------------------------------------------

function lerFlags() {
    const argv = process.argv.slice(2);
    const valor = (n) => {
        const i = argv.indexOf(n);
        return i >= 0 ? argv[i + 1] : undefined;
    };
    if (valor('--backend')) cen.CONFIG.backend = valor('--backend');
    return {
        comando: argv[0],
        caso: valor('--caso') || null,
        fase: valor('--fase') ? Number(valor('--fase')) : null,
        empresaID: Number(valor('--empresa') || CONFIG.empresaID),
        filialID: Number(valor('--filial') || CONFIG.filialID),
        usuarioID: Number(valor('--usuario') || CONFIG.usuarioID),
        entregador: Number(valor('--entregador') || CONFIG.entregador),
        de: Number(valor('--de') || CONFIG.entregador),
        para: Number(valor('--para') || CONFIG.entregadorAlternativo),
        dias: Number(valor('--dias') || 2),
        permitirPassado: argv.includes('--permitir-passado'),
        modoSeco: argv.includes('--dry-run'),
    };
}

const abortar = cen.abortar;

// ---------------------------------------------------------------------------
// Estado entre execuções
// ---------------------------------------------------------------------------

/**
 * O arquivo de estado guarda os `preVendaID` semeados e as rotas criadas.
 *
 * Existe por causa da sentinela: o seeder só autoriza `UPDATE` em pedido criado **na mesma
 * execução**, e a janela do #117 acontece em fases, em execuções diferentes, com o dono
 * fotografando entre uma e outra. Sem memória, a fase 3 não teria autorização para mexer
 * no pedido que a fase 1 criou — e a alternativa (uma execução só, de vinte minutos, com o
 * emulador do outro lado) não sobrevive a nenhum imprevisto.
 *
 * É um arquivo local, ignorado pelo git, e só de IDs.
 */
function lerEstado() {
    try {
        return JSON.parse(fs.readFileSync(CONFIG.estado, 'utf8'));
    } catch {
        return { pedidos: [], rotas: [], caso: null, criadoEm: null };
    }
}

function gravarEstado(e, f) {
    if (f.modoSeco) {
        console.log(`  [dry-run] estado: ${JSON.stringify(e)}`);
        return;
    }
    fs.writeFileSync(CONFIG.estado, JSON.stringify(e, null, 2) + '\n');
}

// ---------------------------------------------------------------------------
// ERP — leitura e escrita com sentinela
// ---------------------------------------------------------------------------

function execSQL() {
    cen.exigirBackend();
    return cen.doBackend('src/config/execSQLQuery');
}

async function ler(query, params = []) {
    const r = await execSQL()(null, null, query, params);
    return Array.isArray(r) ? r : [];
}

/** O marcador que o seeder do backend grava em `Observacoes` de todo pedido que ele cria. */
const MARCADOR = '[SEED-ENTREGAS]';

/**
 * Os pedidos de teste que **ainda estão na fila do painel**, de qualquer lote.
 *
 * `CHARINDEX`, não `LIKE`: em T-SQL os colchetes de `[SEED-ENTREGAS]` são classe de
 * caracteres, então `LIKE '[SEED-ENTREGAS]%'` devolve zero linha em silêncio. Está medido no
 * próprio seeder — LIKE 0, CHARINDEX 11.
 */
async function pedidosSemeadosNaFila(f) {
    return ler(
        `SELECT preVendaID, numeroPreVenda, SituacaoDelivery FROM _PreVenda
          WHERE filialID = ${f.filialID}
            AND CHARINDEX('${MARCADOR}', Observacoes) = 1
            AND SituacaoDelivery IN ('PREPARO', 'PRONTO', 'ENTREGA')
          ORDER BY preVendaID`);
}

/**
 * `UPDATE` em `_PreVenda` com quatro travas: tabela, coluna, pedido conhecido e filial.
 *
 * "Pedido conhecido" é o que o arquivo de estado responde. Deixar o chamador informar o ID
 * e confiar nele seria a mesma coisa que não ter sentinela nenhuma.
 */
async function atualizar(f, preVendaIDs, sets) {
    const conhecidos = new Set(lerEstado().pedidos);
    const alvos = preVendaIDs.map(Number).filter(Number.isFinite);
    if (!alvos.length) {
        // Em `--dry-run` a lista chega vazia porque o seeder não criou pedido nenhum: o
        // que interessa é ver **quais colunas** o caso escreveria, e isso dá para mostrar.
        if (f.modoSeco) {
            console.log(`  [dry-run] UPDATE _PreVenda SET ${Object.keys(sets).join(', ')}`);
            console.log(`            ${JSON.stringify(sets)}  (alvo: os pedidos do lote)`);
            return;
        }
        abortar('nenhum pedido para atualizar');
    }

    const desconhecidos = alvos.filter((id) => !conhecidos.has(id));
    if (desconhecidos.length) {
        abortar('pedido fora do estado deste script',
            `${desconhecidos.join(', ')} — semeie com "preparar" antes, ou apague `
            + `${path.basename(CONFIG.estado)} se o lote for antigo`);
    }
    for (const col of Object.keys(sets)) {
        if (!COLUNAS_GRAVAVEIS.has(col)) abortar('coluna fora da lista branca', col);
        if (COLUNAS_DE_DATA.has(col) && !f.permitirPassado) {
            abortar('escrita em data de entrega exige --permitir-passado', col);
        }
    }

    const pares = Object.entries(sets);
    const texto = `UPDATE _PreVenda SET ${pares.map(([c], i) => `${c} = @v${i}`).join(', ')}
                    WHERE preVendaID IN (${alvos.join(',')}) AND filialID = @pFilial`;
    const sql = cen.doBackend('node_modules/mssql');
    const params = pares.map(([, v], i) => ({
        name: `v${i}`,
        sqltype: typeof v === 'number' ? sql.Float : (v === null ? sql.VarChar(50) : sql.VarChar(80)),
        value: v,
    }));
    params.push({ name: 'pFilial', sqltype: sql.Int, value: f.filialID });

    if (f.modoSeco) {
        console.log(`  [dry-run] ${texto.replace(/\s+/g, ' ')}`);
        console.log(`            ${JSON.stringify(sets)}`);
        return;
    }
    await execSQL()(null, null, texto, params);
    console.log(`  ${alvos.length} pedido(s) atualizado(s): ${JSON.stringify(sets)}`);
}

/**
 * O total do pedido, que é o valor usado para zerar a cobrança nos casos de pedido pago.
 *
 * Em `--dry-run` não há pedido para consultar, e é por isso que ela devolve zero em vez de
 * montar um `IN ()` vazio — que o SQL Server recusa com erro de sintaxe.
 */
async function totalDe(f, preVendaID) {
    if (!preVendaID) return 0;
    const [linha] = await ler(
        `SELECT ValorTOtal FROM _PreVenda
          WHERE preVendaID = ${Number(preVendaID)} AND filialID = ${f.filialID}`);
    return linha ? Number(linha.ValorTOtal) : 0;
}

/** O que o app vai ver, lido da **mesma** função que a API do app lê. */
async function pedidosDoApp(f) {
    return ler(
        `SELECT preVendaID, numeroPreVenda, situacaoDelivery, cliente, endereco, numero,
                bairro, complemento, valorTotal, cobrarDoCliente, troco, tipoPagStr,
                ifoodLocalizer, nnID, keetaId
           FROM funcSelect_Entregador_Pedidos3(${f.empresaID}, ${f.entregador})
          ORDER BY preVendaID`);
}

// ---------------------------------------------------------------------------
// A API do app — a conferência que vale
// ---------------------------------------------------------------------------

/**
 * Chama a **rota do app**, não a do painel. É a diferença entre "o banco está certo" e "a
 * tela vai mostrar": entre os dois moram o agrupamento de rota, o filtro de situação e a
 * ordenação por distância, e já aconteceu de o banco estar certo e a tela vir vazia.
 */
async function apiDoApp(f) {
    cen.exigirBackend();
    const url = `${cen.CONFIG.api}/api/entrega2/gestao/entregador`
        + `/${f.empresaID}/${f.filialID}/${f.usuarioID}/${f.entregador}`;
    const res = await fetch(url, {
        headers: {
            Authorization: 'Basic ' + Buffer.from(cen.basicDoBackend()).toString('base64'),
        },
    });
    const txt = await res.text();
    if (res.status >= 400) abortar(`a API do app respondeu ${res.status}`, txt.slice(0, 200));
    return JSON.parse(txt);
}

async function mostrarEstado(f) {
    const est = lerEstado();
    console.log(`\núltimo caso preparado: ${est.caso || '(nenhum)'}`
        + `${est.criadoEm ? '  em ' + est.criadoEm : ''}`);
    console.log(`pedidos no estado: ${est.pedidos.join(', ') || '(nenhum)'}`);
    console.log(`rotas no estado:   ${est.rotas.join(', ') || '(nenhuma)'}`);

    const app = await apiDoApp(f);
    console.log(`\n=== o que o app do entregador ${f.entregador} está vendo ===`);
    console.log(`pedidos: ${app.pedidos.length}   rotas: ${app.rotas.length}`);
    for (const p of app.pedidos) {
        const selo = p.ifoodLocalizer ? ' [iFood]'
            : p.nnID ? ' [99Food]' : p.keetaId ? ' [Keeta]' : '';
        console.log(`  #${String(p.numeroPreVenda || p.numeroPedido).padEnd(6)}`
            + ` id=${p.preVendaID}  ${String(p.situacaoDelivery).padEnd(9)}`
            + `  total=${fmt(p.valorTotal)} cobrar=${fmt(p.cobrarDoCliente)}`
            + `  ${String(p.tipoPagStr || '').slice(0, 30).padEnd(30)}${selo}`);
        console.log(`          ${String(p.endereco || '')}, ${p.numero || ''}`
            + ` - ${p.bairro || ''}${p.complemento ? ' - ' + p.complemento : ''}`);
    }
    for (const r of app.rotas) {
        console.log(`  rota ${r.rotaID} ${r.codigo || ''} ${r.status}`
            + `  paradas=${(r.paradas || []).length}`);
        for (const s of r.paradas || []) {
            console.log(`      ${s.ordem}. #${s.numeroPedido} id=${s.preVendaID} ${s.status}`);
        }
    }
    return app;
}

const fmt = (v) => (v == null ? '-' : Number(v).toFixed(2).replace('.', ','));

// ---------------------------------------------------------------------------
// Peças reaproveitadas pelos casos
// ---------------------------------------------------------------------------

const flags = (f, extra = {}) => ({
    empresaID: f.empresaID, filialID: f.filialID, usuarioID: f.usuarioID,
    entregador: f.entregador, modoSeco: f.modoSeco, qtd: 4, offset: 0,
    pedidos: [], pronto: [], passos: 3, pausa: 1, ...extra,
});

/** Semeia, marca PRONTO e guarda os IDs no estado — o início de quase todo caso. */
async function semearEAtribuir(f, qtd, offset = 0) {
    await cen.limparFantasma(flags(f));

    console.log(`\n=== semeando ${qtd} pedido(s) ===`);
    const { criados } = await cen.semear(flags(f, { qtd, offset }));
    const ids = (criados || []).map((c) => c.preVendaID);
    if (!ids.length && !f.modoSeco) abortar('o seeder não criou pedido nenhum');

    const est = lerEstado();
    est.pedidos = [...new Set([...est.pedidos, ...ids])];
    est.criadoEm = new Date().toISOString();
    gravarEstado(est, f);

    console.log('\n=== marcando como PRONTO ===');
    await cen.marcarProntos(flags(f), ids);

    console.log(`\n=== atribuindo ao entregador ${f.entregador} ===`);
    await atualizar(f, ids, { FuncionarioIDMotoboy: f.entregador });
    return ids;
}

/** Cria a rota pela API do painel e guarda o `rotaID` no estado, para as fases seguintes. */
async function criarRota(f, ids) {
    if (!ids.length) {
        if (f.modoSeco) {
            console.log('  [dry-run] POST /rota com os pedidos do lote');
            return null;
        }
        abortar('nenhum pedido para pôr na rota');
    }
    const criada = await cen.rotaCriar(flags(f, { pedidos: ids }));
    const rotaID = criada && (criada.rotaID || (criada.rota && criada.rota.rotaID));
    if (rotaID) {
        const est = lerEstado();
        est.rotas = [...new Set([...est.rotas, rotaID])];
        gravarEstado(est, f);
    }
    return rotaID;
}

async function entregadorNaLoja(f) {
    console.log(`\n=== entregador ${f.entregador} disponível, parado na loja ===`);
    await cen.presenca(flags(f, { status: 'DISPONIVEL' }));
    await cen.ping(flags(f), cen.CONFIG.loja.lat, cen.CONFIG.loja.lng, null);
}

// ---------------------------------------------------------------------------
// Os casos
// ---------------------------------------------------------------------------

const CASOS = {
    // -----------------------------------------------------------------------
    lista: {
        foto: 'a base de tudo: quatro entregas abertas na lista do app',
        manuais: '#112, #113, #116',
        async montar(f) {
            const ids = await semearEAtribuir(f, 4);

            // Uma forma de pagamento por pedido, porque é o que a tela mostra no rodapé e
            // o que decide se a folha de troco aparece.
            await atualizar(f, [ids[0]], {
                TipoPag: 1, tipoPagStr: 'Dinheiro', troco: 50.0,
            });
            await atualizar(f, [ids[1]], { TipoPag: 0, tipoPagStr: 'PIX', troco: 0.0 });
            await atualizar(f, [ids[2]], {
                TipoPag: 2, tipoPagStr: 'Cartão de Débito', TipoPagBandeiraStr: 'Visa', troco: 0.0,
            });
            await atualizar(f, [ids[3]], { TipoPag: 3, tipoPagStr: 'Cartão de Crédito', troco: 0.0 });
            console.log('\nquatro formas diferentes: dinheiro com troco, Pix, débito e crédito.');
        },
        conferir: (app) => [
            ['quatro entregas na lista', app.pedidos.length === 4,
                `achei ${app.pedidos.length}`],
            ['nenhuma rota, para a lista ser a lista solta', app.rotas.length === 0,
                `achei ${app.rotas.length} rota(s)`],
            ['um pedido em dinheiro, para a folha de troco existir',
                app.pedidos.some((p) => /dinheiro/i.test(p.tipoPagStr || '')),
                'nenhum pedido em dinheiro'],
        ],
    },

    // -----------------------------------------------------------------------
    'rota-viva': {
        foto: 'rota chegando ao vivo: três paradas numa rota **não despachada**, mais uma solta',
        manuais: '#113, #117',
        async montar(f) {
            const ids = await semearEAtribuir(f, 4);
            await entregadorNaLoja(f);

            console.log('\n=== criando a rota com as três primeiras, já com entregador ===');
            await criarRota(f, ids.slice(0, 3));
            console.log('\nA rota NÃO foi despachada de propósito: é o INICIAR ROTA verde que');
            console.log('o entregador precisa ver no cabeçalho, e ele desaparece depois do despacho.');
            console.log('O quarto pedido ficou solto, para a faixa OUTRAS ENTREGAS (1) existir.');
        },
        conferir: (app) => [
            ['uma rota na tela do app', app.rotas.length === 1,
                `achei ${app.rotas.length}`],
            ['três paradas na rota',
                (app.rotas[0] && (app.rotas[0].paradas || []).length) === 3,
                `achei ${(app.rotas[0] && (app.rotas[0].paradas || []).length) || 0}`],
            ['a rota ainda não despachada, para o INICIAR ROTA aparecer',
                Boolean(app.rotas[0]) && app.rotas[0].status !== 'DESPACHADA',
                `status ${app.rotas[0] && app.rotas[0].status}`],
            ['o pedido solto da faixa OUTRAS ENTREGAS', app.pedidos.length >= 1,
                'nenhum pedido fora da rota'],
        ],
    },

    // -----------------------------------------------------------------------
    marketplace: {
        foto: 'um pedido de iFood e um de 99Food, os dois já pagos',
        manuais: '#115',
        async montar(f) {
            const ids = await semearEAtribuir(f, 2, 4);
            const [ifood, nnfood] = ids;

            // Os formatos são os que aparecem em produção: localizador de 8 dígitos e
            // referência curta no iFood; id longo de 19 dígitos no 99Food. O `ValorPago`
            // igual ao total é o que zera o "Cobrar R$" e faz o app esconder a cobrança.
            console.log('\n=== pedido de iFood ===');
            await atualizar(f, [ifood], {
                correlationId: '7d3f1b90-5c42-4e18-9a77-2f6b0c8d4e11',
                ifoodLocalizer: '48731502',
                ifoodShortReference: '1851 - Coleta 3983',
                marketPlace: 1,
                tipoPagStr: 'PAGO ONLINE',
                TipoPag: 0,
                troco: 0.0,
                ValorPago: await totalDe(f, ifood),
            });

            console.log('\n=== pedido de 99Food ===');
            await atualizar(f, [nnfood], {
                nnID: '5764687241800647938',
                ifoodShortReference: '254023',
                marketPlace: 1,
                tipoPagStr: 'PIX',
                TipoPag: 0,
                troco: 0.0,
                ValorPago: await totalDe(f, nnfood),
            });

            console.log('\nOs dois nascem pagos: o app mostra COBRAR R$ 0,00 e o botão de');
            console.log('confirmação da plataforma, sem INICIAR COBRANÇA.');
            console.log('\nATENÇÃO: não finalize esses dois pelo botão do app. Identificador de');
            console.log('plataforma que não existe do outro lado faz a baixa tentar avisar o');
            console.log('marketplace de verdade. Use "limpar" quando terminar as fotos.');
        },
        conferir: (app) => [
            ['um pedido com localizador de iFood', app.pedidos.some((p) => p.ifoodLocalizer),
                'nenhum'],
            ['um pedido com identificador de 99Food', app.pedidos.some((p) => p.nnID),
                'nenhum'],
            ['os dois com cobrança zerada, porque nasceram pagos',
                app.pedidos.filter((p) => Number(p.cobrarDoCliente) === 0).length >= 2,
                `${app.pedidos.filter((p) => Number(p.cobrarDoCliente) === 0).length} com zero`],
        ],
    },

    // -----------------------------------------------------------------------
    keeta: {
        foto: 'pedido de plataforma **sem** botão de confirmação — só o selo',
        manuais: '#115',
        async montar(f) {
            const ids = await semearEAtribuir(f, 1, 6);
            await atualizar(f, ids, {
                keetaId: '4900112233445566',
                marketPlace: 1,
                tipoPagStr: 'PAGO ONLINE',
                TipoPag: 0,
                troco: 0.0,
                ValorPago: await totalDe(f, ids[0]),
            });
            console.log('\nKeeta entra como selo e nada mais: o app não tem tela de confirmação');
            console.log('para ela. É a foto que falta na última pergunta do #115.');
        },
        conferir: (app) => [
            ['um pedido com identificador Keeta', app.pedidos.some((p) => p.keetaId), 'nenhum'],
            ['nenhum iFood nem 99Food na tela, para o selo aparecer sozinho',
                app.pedidos.every((p) => !p.ifoodLocalizer && !p.nnID),
                'há pedido de outra plataforma na lista'],
        ],
    },

    // -----------------------------------------------------------------------
    pago: {
        foto: 'a tela **Pedido já pago** — saldo zero sem marketplace',
        manuais: '#116',
        async montar(f) {
            const ids = await semearEAtribuir(f, 1, 7);
            await atualizar(f, ids, {
                ValorPago: await totalDe(f, ids[0]), troco: 0.0,
                TipoPag: 1, tipoPagStr: 'Dinheiro',
            });
            console.log('\nO pedido tem saldo zero e nenhum identificador de plataforma. O app');
            console.log('mostra COBRAR R$ 0,00 e, ao tentar cobrar, a folha "Pedido já pago".');
        },
        conferir: (app) => [
            ['um pedido só na lista', app.pedidos.length === 1, `achei ${app.pedidos.length}`],
            ['a cobrança zerada', Boolean(app.pedidos[0])
                && Number(app.pedidos[0].cobrarDoCliente) === 0,
                `cobrar = ${app.pedidos[0] && app.pedidos[0].cobrarDoCliente}`],
        ],
    },

    // -----------------------------------------------------------------------
    notificacao: {
        foto: 'o aviso do BeeFood Entregador chegando na tela',
        manuais: 'apêndice de notificações',
        async montar(f) {
            console.log('Este caso precisa do app **aberto e online** antes de rodar: o aviso');
            console.log('chega no instante da atribuição, e é ele que a foto quer.\n');
            await entregadorNaLoja(f);

            const ids = await semearEAtribuir(f, 1, 8);
            console.log('\nO pedido foi atribuído agora. O aviso sai do servidor neste instante —');
            console.log('fotografe a tela do celular, e depois a lista já com a entrega nova.');
            return ids;
        },
        conferir: (app) => [
            ['o pedido novo já na lista do app', app.pedidos.length >= 1, 'lista vazia'],
        ],
    },

    // -----------------------------------------------------------------------
    troca: {
        foto: 'a entrega sendo **tirada** do entregador, e a lista depois sem ela',
        manuais: '#112',
        async montar(f) {
            const ids = await semearEAtribuir(f, 1, 9);
            console.log(`\n=== passando o pedido de ${f.de} para ${f.para} ===`);
            console.log('Fotografe o aviso chegando, e depois a lista sem aquele pedido.');
            await atualizar(f, ids, { FuncionarioIDMotoboy: f.para });
            return ids;
        },
        conferir: (app, f) => [
            [`o pedido saiu da lista do entregador ${f.entregador}`,
                app.pedidos.every(
                    (p) => Number(p.preVendaID) !== Number(lerEstado().pedidos.at(-1))),
                'ele continua lá'],
        ],
    },

    // -----------------------------------------------------------------------
    'historico-vazio': {
        foto: 'a lista e o histórico vazios — *Nenhuma entrega no período*',
        manuais: '#111, #112',
        async montar(f) {
            const est = lerEstado();
            if (!est.pedidos.length) {
                console.log('Nada semeado por este script. Se ainda houver pedido na tela do app,');
                console.log('ele veio de outro lote: desatribua pelo painel ou pelo gerador do dono.');
            } else {
                console.log(`\n=== desatribuindo ${est.pedidos.length} pedido(s) ===`);
                await atualizar(f, est.pedidos, { FuncionarioIDMotoboy: null });
            }
            console.log('\nA aba Entregas fica vazia e o Histórico mostra *Nenhuma entrega no');
            console.log('período*. São duas fotos, e as duas só existem com a lista limpa.');
        },
        conferir: (app) => [
            ['a aba Entregas vazia', app.pedidos.length === 0,
                `ainda há ${app.pedidos.length} pedido(s)`],
            ['nenhuma rota sobrando', app.rotas.length === 0,
                `ainda há ${app.rotas.length} rota(s)`],
        ],
    },

    // -----------------------------------------------------------------------
    'historico-dias': {
        foto: 'o histórico **agrupado por dia**, com dias anteriores',
        manuais: '#112',
        async montar(f) {
            if (!f.permitirPassado) {
                abortar('este caso escreve data de entrega no passado',
                    'rode de novo com --permitir-passado, sabendo que ele mexe em '
                    + 'histórico — e que o relatório Operação de Entrega soma por data');
            }
            const est = lerEstado();
            const entregues = await ler(
                `SELECT preVendaID FROM _PreVenda
                  WHERE preVendaID IN (${(est.pedidos.length ? est.pedidos : [0]).join(',')})
                    AND filialID = ${f.filialID} AND SituacaoDelivery = 'ENTREGUE'`);
            if (!entregues.length) {
                abortar('nenhum pedido entregue no estado deste script',
                    'rode "preparar --caso lista" e conclua as entregas pelo app antes');
            }
            // Um dia por pedido, do mais recente para trás: é o que faz o histórico ter
            // mais de um cabeçalho de dia, que é a foto pedida.
            let dia = 1;
            for (const { preVendaID } of entregues) {
                const d = new Date(Date.now() - dia * 86400000);
                const data = d.toISOString().slice(0, 10);
                console.log(`\n=== pedido ${preVendaID} passa a constar entregue em ${data} ===`);
                await atualizar(f, [preVendaID], {
                    DataHoraEntregue: `${data} 19:${String(10 + dia * 7).padStart(2, '0')}:00`,
                    dataEntrega: data,
                    HoraEntrega: `19:${String(10 + dia * 7).padStart(2, '0')}:00`,
                });
                dia = Math.min(dia + 1, f.dias);
            }
            console.log('\nO histórico do app passa a ter mais de um dia. Lembre que o relatório');
            console.log('Operação de Entrega lê esta mesma data: o que foi movido sai do total');
            console.log('de hoje.');
        },
        conferir: () => [],
    },
};

// ---------------------------------------------------------------------------
// A janela do #117 — o manual que precisa dos dois lados no mesmo pedido
// ---------------------------------------------------------------------------

/**
 * O #117 mostra o **mesmo pedido** nas duas telas, e é o único manual do bloco que não dá
 * para montar por partes: ou as duas metades são capturadas no mesmo pedido, ou o manual
 * mente. As fases existem para o dono fotografar entre uma e outra, sem pressa, com o
 * número do pedido batendo nos dois lados.
 *
 * Quem roda cada fase sou eu, do painel. O que o dono faz é fotografar quando eu avisar.
 */
const FASES_117 = [
    {
        n: 1,
        titulo: 'três pedidos prontos na loja, nenhum atribuído',
        fotos: ['painel: a fila com os três pedidos e o mapa com o pin do entregador online'],
        async rodar(f) {
            await cen.limparFantasma(flags(f));

            // A foto desta fase é "três pedidos prontos na fila", e fila com lote antigo
            // dentro estraga a foto em silêncio. Aconteceu no ensaio: 18 pedidos de teste.
            const sobra = await pedidosSemeadosNaFila(f);
            if (sobra.length) {
                abortar(`a fila do painel tem ${sobra.length} pedido(s) de teste de lote anterior`,
                    'rode "arquivar-fila" antes — a primeira foto do #117 é a fila com três '
                    + 'pedidos, e lote velho no meio dela estraga a foto');
            }

            // Offset 0 de propósito: os três primeiros endereços da lista do seeder são os
            // mais próximos entre si (menos de 500 m), e rota de três paradas espalhadas por
            // 10 km não é a rota que o manual quer contar.
            const { criados } = await cen.semear(flags(f, { qtd: 3, offset: 0 }));
            const ids = (criados || []).map((c) => c.preVendaID);
            const est = lerEstado();
            est.pedidos = [...new Set([...est.pedidos, ...ids])];
            est.caso = 'janela-117';
            est.criadoEm = new Date().toISOString();
            gravarEstado(est, f);
            await cen.marcarProntos(flags(f), ids);
            await entregadorNaLoja(f);
            console.log(`\npedidos desta janela: ${ids.join(', ')}`);
            console.log('ANOTE os números: eles têm de aparecer nas fotos dos dois lados.');
        },
    },
    {
        n: 2,
        titulo: 'a rota criada e atribuída — o app recebe',
        fotos: [
            'painel: o painel de rotas com a rota nova e o entregador escolhido',
            'app: a lista com o grupo ROTA recém-chegado, mostrando 0 de 3',
        ],
        async rodar(f) {
            const ids = lerEstado().pedidos.slice(-3);
            const rotaID = await criarRota(f, ids);
            console.log(`\nrota ${rotaID} criada com ${ids.length} paradas, não despachada.`);
        },
    },
    {
        n: 3,
        titulo: 'o despacho — pelo painel, para o app ver a rota já em rota',
        fotos: [
            'painel: a rota despachada, com o carimbo de saída',
            'app: o cabeçalho com a etiqueta *em rota* e o botão ABRIR NO MAPS',
        ],
        async rodar(f) {
            const rotaID = lerEstado().rotas.at(-1);
            if (!rotaID) abortar('nenhuma rota no estado — rode a fase 2');
            await cen.rotaDespachar(flags(f, { rota: rotaID }));
            console.log('\nDespachada. O cliente recebeu o aviso de saída, se o WhatsApp estiver');
            console.log('ligado, e o marketplace foi informado nos pedidos que têm plataforma.');
        },
    },
    {
        n: 4,
        titulo: 'o entregador andando — o pin se move no mapa do painel',
        fotos: ['painel: o mapa com o pin longe da loja e o rastro da rota'],
        async rodar(f) {
            const rotaID = lerEstado().rotas.at(-1);
            const p = await cen.painel(flags(f));
            const rota = (p.rotas || []).find((x) => x.rotaID === rotaID);
            const parada = (rota && rota.paradas || []).find((s) => s.latitude != null);
            if (!parada) abortar('a rota não tem parada com coordenada');
            await cen.andar(flags(f, { para: `${parada.latitude},${parada.longitude}`, passos: 6 }));
        },
    },
    {
        n: 5,
        titulo: 'a primeira entrega concluída',
        fotos: [
            'app: a tela de sucesso da cobrança, ou a folha de finalizar',
            'painel: a parada marcada como entregue e o contador em 1 de 3',
        ],
        async rodar(f) {
            console.log('Esta fase é do **app**: quem dá a baixa é o entregador, na porta do');
            console.log('cliente, porque é isso que o manual mostra. Eu só confiro depois.\n');
            const app = await apiDoApp(f);
            const rota = app.rotas[0];
            console.log(`rota ${rota ? rota.rotaID : '-'}: `
                + `${(rota && rota.paradas || []).map((s) => s.status).join(', ') || '-'}`);
            console.log('\nQuando a baixa acontecer, rode "conferir" para o painel e o app');
            console.log('contarem a mesma história.');
        },
    },
    {
        n: 6,
        titulo: 'o resto da rota, e o fechamento',
        fotos: [
            'painel: a rota sem paradas abertas, pronta para finalizar',
            'app: a lista sem os pedidos da rota',
        ],
        async rodar(f) {
            const rotaID = lerEstado().rotas.at(-1);
            const p = await cen.painel(flags(f));
            const rota = (p.rotas || []).find((x) => x.rotaID === rotaID);
            for (const s of (rota && rota.paradas || [])) {
                if (s.status === 'ENTREGUE') continue;
                await cen.paradaEntregar(flags(f, { rota: rotaID, pedido: s.preVendaID }));
            }
            await cen.rotaFinalizar(flags(f, { rota: rotaID }));
        },
    },
    {
        n: 7,
        titulo: 'o depois: relatório e histórico',
        fotos: [
            'painel: Operação de Entrega com a data de hoje, já contando estas entregas',
            'app: o histórico do dia com as três',
        ],
        async rodar(f) {
            await cen.presenca(flags(f, { status: 'OFFLINE' }));
            console.log('\nO ciclo fechou. O relatório Desempenho > Delivery > Operação de Entrega');
            console.log('com a data de hoje já conta estas entregas, e o histórico do app também.');
        },
    },
];

async function janela117(f) {
    if (!f.fase) {
        console.log('\nA janela do #117 acontece em sete fases. Entre uma e outra, as fotos.\n');
        for (const fa of FASES_117) {
            console.log(`  fase ${fa.n} — ${fa.titulo}`);
            for (const foto of fa.fotos) console.log(`           📷 ${foto}`);
        }
        console.log('\n  node smoke-app.js janela-117 --fase 1');
        return;
    }
    const fase = FASES_117.find((x) => x.n === f.fase);
    if (!fase) abortar('fase inexistente', String(f.fase));
    console.log(`\n=== FASE ${fase.n}: ${fase.titulo} ===`);
    await fase.rodar(f);
    console.log('\n--- fotos desta fase ---');
    for (const foto of fase.fotos) console.log(`  📷 ${foto}`);
    if (fase.n < FASES_117.length) {
        console.log(`\nDepois das fotos: node smoke-app.js janela-117 --fase ${fase.n + 1}`);
    }
}

// ---------------------------------------------------------------------------
// Comandos
// ---------------------------------------------------------------------------

function listarCasos() {
    console.log('\ncasos — cada um é uma foto pedida em ../pedidos/capturas-app.md\n');
    for (const [nome, c] of Object.entries(CASOS)) {
        console.log(`  ${nome.padEnd(17)} ${c.foto}`);
        console.log(`  ${' '.repeat(17)} manuais: ${c.manuais}`);
    }
    console.log('\n  janela-117        o roteiro de sete fases do manual dos dois lados');
    console.log('\nE dois de limpeza, que resolvem telas diferentes:');
    console.log('  limpar            tira da tela do app — desatribui o entregador');
    console.log('  arquivar-fila     tira da fila do painel — manda lote antigo para AGUARDANDO\n');
}

async function preparar(f) {
    const caso = CASOS[f.caso];
    if (!caso) {
        console.log(`caso desconhecido: ${f.caso || '(nenhum)'}`);
        listarCasos();
        process.exit(1);
    }
    console.log(`\n=== CASO ${f.caso} — ${caso.foto} ===`);
    await caso.montar(f);

    const est = lerEstado();
    est.caso = f.caso;
    gravarEstado(est, f);

    if (f.modoSeco) return;
    console.log('\n--- conferência ---');
    await conferir(f);
}

/**
 * A conferência é o smoketest propriamente dito: lê a API do app e verifica o que a tela
 * vai mostrar. Se ela passa, pode fotografar; se falha, a foto sairia errada e ninguém
 * notaria até o manual estar publicado.
 */
async function conferir(f) {
    const app = await mostrarEstado(f);
    const nome = f.caso || lerEstado().caso;
    const caso = CASOS[nome];
    if (!caso) {
        console.log('\n(sem caso para conferir — passe --caso para verificar as regras dele)');
        return;
    }
    const checagens = caso.conferir(app, f) || [];
    let falhas = 0;
    console.log(`\nregras do caso ${nome}:`);
    for (const [rotulo, ok, detalhe] of checagens) {
        console.log(`  ${ok ? 'OK    ' : 'FALHOU'}  ${rotulo}${ok ? '' : ` — ${detalhe}`}`);
        if (!ok) falhas++;
    }
    if (!checagens.length) console.log('  (este caso não tem regra automática)');
    if (falhas) {
        console.log(`\n${falhas} regra(s) falharam: NÃO fotografe ainda.`);
        process.exitCode = 1;
    } else if (checagens.length) {
        console.log('\nTudo certo. A tela está pronta para a captura.');
    }
}

/**
 * Limpar é desatribuir, não apagar.
 *
 * O pedido continua no ERP, como qualquer pedido de teste, e sai da tela do app na hora.
 * Apagar exigiria um caminho de DELETE que pudesse errar o alvo — e o seeder do backend já
 * recusou esse caminho pelo mesmo motivo. As rotas criadas aqui saem pela API de exclusão,
 * que é o caminho que o operador usa.
 */
async function limpar(f) {
    const est = lerEstado();
    for (const rotaID of est.rotas) {
        try {
            await cen.rotaExcluir(flags(f, { rota: rotaID }));
        } catch (e) {
            console.log(`  rota ${rotaID}: ${e.message.slice(0, 120)}`);
        }
    }
    if (est.pedidos.length) {
        await atualizar(f, est.pedidos, { FuncionarioIDMotoboy: null });
    }
    await cen.presenca(flags(f, { status: 'OFFLINE' }));
    gravarEstado({ pedidos: [], rotas: [], caso: null, criadoEm: null }, f);
    console.log('\nLimpo. Os pedidos continuam no ERP, sem entregador — fora da tela do app.');
}

/**
 * Tira da **fila do painel** os pedidos de teste de lotes anteriores.
 *
 * Descoberto no ensaio da janela do #117: `limpar` tira o pedido da tela do app, mas ele
 * continua em *Pedidos sem rota* no painel por até 6 h. Depois de uma tarde de ensaios a fila
 * tinha 18 pedidos de teste — e a primeira foto do #117 é justamente "três pedidos prontos".
 *
 * `AGUARDANDO` é o estado certo para isso: a view do painel filtra
 * `PREPARO`/`PRONTO`/`ENTREGA`/`ENTREGUE`, e o app ignora `AGUARDANDO`. O pedido sai das duas
 * telas sem ser apagado e sem entrar na conta de entregas do dia — o que `ENTREGUE` faria,
 * inflando o relatório Operação de Entrega.
 *
 * A sentinela aqui é outra, e é mais forte que a do arquivo de estado: o `WHERE` exige o
 * **marcador do seeder** em `Observacoes`. Pedido de verdade não tem esse marcador, então não
 * há como este comando alcançar um.
 */
async function arquivarFila(f) {
    const alvos = await pedidosSemeadosNaFila(f);
    if (!alvos.length) {
        console.log('\nA fila do painel não tem pedido de teste. Nada a arquivar.');
        return;
    }
    console.log(`\n${alvos.length} pedido(s) de teste na fila do painel:`);
    for (const p of alvos) {
        console.log(`  #${p.numeroPreVenda}  id=${p.preVendaID}  ${p.SituacaoDelivery}`);
    }

    const texto = `UPDATE _PreVenda SET SituacaoDelivery = 'AGUARDANDO', FuncionarioIDMotoboy = NULL
                    WHERE filialID = @pFilial
                      AND CHARINDEX('${MARCADOR}', Observacoes) = 1
                      AND SituacaoDelivery IN ('PREPARO', 'PRONTO', 'ENTREGA')`;
    if (f.modoSeco) {
        console.log(`\n  [dry-run] ${texto.replace(/\s+/g, ' ')}`);
        return;
    }
    const sql = cen.doBackend('node_modules/mssql');
    await execSQL()(null, null, texto, [{ name: 'pFilial', sqltype: sql.Int, value: f.filialID }]);
    gravarEstado({ pedidos: [], rotas: [], caso: null, criadoEm: null }, f);
    console.log(`\n${alvos.length} pedido(s) fora da fila. O painel abre limpo para a captura.`);
}

const COMANDOS = {
    casos: async () => listarCasos(),
    estado: mostrarEstado,
    preparar,
    conferir,
    limpar,
    'arquivar-fila': arquivarFila,
    'janela-117': janela117,
};

async function main() {
    const f = lerFlags();
    if (!f.comando || !COMANDOS[f.comando]) {
        console.log('Comandos: ' + Object.keys(COMANDOS).join(', '));
        console.log('\nVeja o cabeçalho deste arquivo para o uso de cada um.');
        process.exit(f.comando ? 1 : 0);
    }
    cen.validarAlvo(f);
    if (f.modoSeco) console.log('--dry-run: nada será escrito.');
    console.log(`empresa ${f.empresaID} / filial ${f.filialID} / entregador ${f.entregador}`);

    await COMANDOS[f.comando](f);
}

if (require.main === module) {
    main().then(() => process.exit(process.exitCode || 0)).catch((e) => {
        console.log('\nERRO:', e && e.stack ? e.stack : e);
        process.exit(1);
    });
}

module.exports = { CASOS, FASES_117, COLUNAS_GRAVAVEIS };
