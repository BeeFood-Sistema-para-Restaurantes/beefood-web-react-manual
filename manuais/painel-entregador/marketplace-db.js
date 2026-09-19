#!/usr/bin/env node
/**
 * marketplace-db.js — estampa o identificador de plataforma nos pedidos do smoke teste,
 * para o Painel para Entregadores mostrar o ícone de iFood, 99Food, Keeta e AIQFome.
 *
 * ---------------------------------------------------------------------------------------
 * POR QUE PRECISA DO BANCO
 * ---------------------------------------------------------------------------------------
 * `origem` **não é campo de entrada de nenhuma rota**. Está medido em três ensaios desta
 * pasta:
 *
 *   exp_origem.py     POST /api/venda2/salvar (tela /delivery) grava sempre `Manual`,
 *                     e descarta origem/marketPlace/ifoodShortReference/keetaId/nnID
 *                     nas três posições do corpo (raiz, `delivery`, `cliente`).
 *   pedido_cardapio + POST /datasnap/rest/tmesa/pedido (cardápio público) grava sempre
 *   pedido_marketplace  `Cardápio Digital`, mesmo recebendo os campos de plataforma.
 *   exp_ids.py        nenhuma das seis rotas de atualização de venda grava
 *                     ifoodLocalizer, nnID, keetaId ou aiqfomeId.
 *
 * E `origem` também não é coluna que se grave: ela é **derivada** do identificador que o
 * pedido carrega. A pista está na lista de colunas do `smoke-app.js` da Gestão de Entregas,
 * que escreve `ifoodLocalizer`, `nnID`, `keetaId` e `marketPlace` e **não** escreve
 * `origem` — e os pedidos que ele montou aparecem na API como iFood, 99Food e Keeta. O que
 * a base confirma, pedido por pedido:
 *
 *   ifoodLocalizer preenchido  -> iFood
 *   nnID preenchido            -> 99Food
 *   keetaId preenchido         -> Keeta
 *   aiqfomeId preenchido       -> AIQFome
 *   filialIDOrigem preenchido  -> Cardápio Digital
 *   nada disso                 -> Manual
 *
 * Então o caminho é: **criar o pedido pela rota do produto** (os scripts Python desta
 * pasta) e depois **estampar o identificador** — que é o único passo que precisa de banco.
 *
 * ---------------------------------------------------------------------------------------
 * NENHUMA CREDENCIAL MORA AQUI
 * ---------------------------------------------------------------------------------------
 * Este repositório é público. Host, usuário e senha do MSSQL saem do clone do backend, pelo
 * caminho em `--backend` (ou `BEETECH_BACKEND`), exatamente como no `cenario.js` do bloco de
 * Gestão de Entregas:
 *
 *   src/config/execSQLQuery.js      -> executa a query
 *   node_modules/mssql              -> tipos dos parâmetros
 *
 * Antes da primeira execução: `cd ~/refs/beetech-server-node-2.0 && npm install --no-save mssql`
 *
 * ---------------------------------------------------------------------------------------
 * COMO ELE EVITA ESTRAGO
 * ---------------------------------------------------------------------------------------
 * 1. **Só escreve com `--gravar`.** Sem a flag ele imprime o SQL e sai — o contrário do
 *    padrão de ferramenta de banco, e de propósito.
 * 2. **Lista branca de alvo** literal (38311/39202). Outra empresa aborta antes de conectar.
 * 3. **Lista branca de coluna:** só as do identificador de plataforma e as três do
 *    pagamento que acompanham pedido já pago. Nada fiscal, nada de valor de produto.
 * 4. **Sentinela de pedido:** o `WHERE` exige o marcador `[SMOKE-PAINEL]` que os scripts
 *    Python gravam em `Observacoes`. Pedido de verdade não tem o marcador, então não há
 *    como este arquivo alcançar um.
 * 5. **`UPDATE`, nunca `INSERT`.** O pedido nasce pela rota do produto, com número de
 *    venda, caixa e cliente coerentes. Inserir venda à mão produziria registro torto.
 * 6. **Nunca finalize pelo app** um pedido estampado aqui: identificador de plataforma que
 *    não existe do outro lado faz a baixa tentar avisar o marketplace de verdade.
 *
 * ---------------------------------------------------------------------------------------
 * USO
 * ---------------------------------------------------------------------------------------
 *   node marketplace-db.js plano                      # o SQL de cada canal, sem banco
 *   node marketplace-db.js estado                     # os pedidos do smoke teste na fila
 *   node marketplace-db.js estampar --pedidos 1,2,3,4          # ensaio (não grava)
 *   node marketplace-db.js estampar --pedidos 1,2,3,4 --gravar
 *   node marketplace-db.js estampar --pedidos 9 --canais keeta --gravar
 *   node marketplace-db.js limpar --pedidos 1,2 --gravar       # tira o identificador
 */

'use strict';

const fs = require('fs');
const path = require('path');

const CONFIG = {
    empresaID: 38311,
    filialID: 39202,
    backend: process.env.BEETECH_BACKEND
        || path.join(process.env.HOME || '', 'refs', 'beetech-server-node-2.0'),
};

// Literal de propósito: destravar exige editar o arquivo, não passar uma flag.
const ALVOS_PERMITIDOS = [{ empresaID: 38311, filialID: 39202 }];

/** O marcador que os scripts Python desta pasta gravam em `Observacoes`. */
const MARCADOR = '[SMOKE-PAINEL]';

/**
 * Colunas que este arquivo pode escrever em `_PreVenda`, e por que cada uma.
 *
 * A lista é curta porque é ela que impede um erro de digitação virar escrita em coluna
 * fiscal. Tudo aqui é campo que o cartão do painel lê, ou que acompanha pedido já pago.
 */
const COLUNAS_GRAVAVEIS = new Set([
    'correlationId',         // identificador de pedido iFood
    'ifoodLocalizer',        // localizador de 8 dígitos do iFood -> origem "iFood"
    'ifoodShortReference',   // a "Coleta" do iFood e o número curto do 99Food
    'nnID',                  // identificador de pedido 99Food -> origem "99Food"
    'keetaId',               // identificador de pedido Keeta -> origem "Keeta"
    'aiqfomeId',             // identificador de pedido AIQFome -> origem "AIQFome"
    'marketPlace',           // marca o pedido como de plataforma
    'tipoPagStr',            // forma prevista, texto — o painel mostra no detalhe
    'TipoPag',               // forma prevista, numérica
    'troco',                 // zero em pedido pago online
]);

/**
 * Os quatro canais. Os formatos imitam o que o `diagnostico.py` leu dos pedidos que já
 * existiam na base da sandbox — inclusive a forma de pagamento de cada plataforma.
 */
const CANAIS = {
    ifood: {
        origem: 'iFood',
        sets: {
            correlationId: '5f21a7c4-9b30-4d6e-8a15-73c0e2b41d99',
            ifoodLocalizer: '48739120',
            ifoodShortReference: '4821 - Coleta 7312',
            marketPlace: 1,
            tipoPagStr: 'PAGO ONLINE',
            TipoPag: 0,
            troco: 0,
        },
    },
    '99food': {
        origem: '99Food',
        sets: {
            nnID: '5764687241800912734',
            ifoodShortReference: '254118',
            marketPlace: 1,
            tipoPagStr: 'PIX',
            TipoPag: 0,
            troco: 0,
        },
    },
    keeta: {
        origem: 'Keeta',
        sets: {
            keetaId: '4900112233449871',
            marketPlace: 1,
            tipoPagStr: 'PAGO ONLINE',
            TipoPag: 0,
            troco: 0,
        },
    },
    aiqfome: {
        origem: 'AIQFome',
        sets: {
            aiqfomeId: '9820451',
            marketPlace: 1,
            tipoPagStr: 'PAGO ONLINE',
            TipoPag: 0,
            troco: 0,
        },
    },
};

/** `limpar` devolve o pedido ao estado de origem "Manual"/"Cardápio Digital". */
const LIMPEZA = {
    correlationId: null,
    ifoodLocalizer: null,
    ifoodShortReference: null,
    nnID: null,
    keetaId: null,
    aiqfomeId: null,
    marketPlace: null,
};

// ---------------------------------------------------------------------------
// Flags
// ---------------------------------------------------------------------------

function lerFlags() {
    const argv = process.argv.slice(2);
    const valor = (nome) => {
        const i = argv.indexOf(nome);
        return i >= 0 ? argv[i + 1] : undefined;
    };
    if (valor('--backend')) CONFIG.backend = valor('--backend');
    const lista = (nome) => (valor(nome) || '').split(',').map((x) => x.trim()).filter(Boolean);
    return {
        comando: argv[0] || 'plano',
        empresaID: Number(valor('--empresa') || CONFIG.empresaID),
        filialID: Number(valor('--filial') || CONFIG.filialID),
        pedidos: lista('--pedidos').map(Number).filter(Number.isFinite),
        canais: lista('--canais'),
        gravar: argv.includes('--gravar'),
    };
}

function abortar(motivo, detalhe) {
    console.log(`\nABORTADO: ${motivo}`);
    if (detalhe) console.log(`  ${detalhe}`);
    process.exit(1);
}

function validarAlvo(f) {
    const ok = ALVOS_PERMITIDOS.some(
        (a) => a.empresaID === f.empresaID && a.filialID === f.filialID);
    if (!ok) {
        abortar('alvo fora da lista branca',
            `empresa ${f.empresaID}, filial ${f.filialID} — só a sandbox é permitida`);
    }
}

function canaisEscolhidos(f) {
    const nomes = f.canais.length ? f.canais : Object.keys(CANAIS);
    const fora = nomes.filter((n) => !CANAIS[n]);
    if (fora.length) abortar('canal desconhecido', `${fora.join(', ')} — use ${Object.keys(CANAIS).join(', ')}`);
    return nomes;
}

// ---------------------------------------------------------------------------
// Backend — só é exigido quando há banco a tocar
// ---------------------------------------------------------------------------

function exigirBackend() {
    if (!fs.existsSync(CONFIG.backend)) {
        abortar('clone do backend não encontrado',
            `${CONFIG.backend}\n  Passe --backend <caminho> ou defina BEETECH_BACKEND.\n`
            + `  Sem o clone não há host nem senha do MSSQL: eles não moram neste repositório,\n`
            + `  que é público. Se o Bitbucket não estiver autenticando, é o token do ambiente\n`
            + `  (BITBUCKET_TOKEN) que precisa ser renovado — e secret novo só entra em VM nova.\n`
            + `  Enquanto isso, "node marketplace-db.js plano" mostra o SQL sem conectar.`);
    }
    if (!fs.existsSync(path.join(CONFIG.backend, 'node_modules', 'mssql'))) {
        abortar('dependência do backend não instalada',
            `cd ${CONFIG.backend} && npm install --no-save mssql`);
    }
}

function doBackend(rel) {
    return require(path.join(CONFIG.backend, rel));
}

async function ler(query, params = []) {
    exigirBackend();
    const execSQLQuery = doBackend('src/config/execSQLQuery');
    const r = await execSQLQuery(null, null, query, params);
    return Array.isArray(r) ? r : [];
}

// ---------------------------------------------------------------------------
// SQL
// ---------------------------------------------------------------------------

/**
 * O texto do `UPDATE`, com as quatro travas no próprio `WHERE`.
 *
 * `CHARINDEX`, não `LIKE`: em T-SQL os colchetes de `[SMOKE-PAINEL]` são classe de
 * caracteres, e `LIKE '[SMOKE-PAINEL]%'` devolve zero linha **em silêncio**. Lição herdada
 * do `smoke-app.js`, onde o LIKE achou 0 e o CHARINDEX achou 11.
 */
function sqlEstampar(f, pedidos, sets) {
    const pares = Object.entries(sets);
    return `UPDATE _PreVenda
               SET ${pares.map(([c], i) => `${c} = @v${i}`).join(', ')}
             WHERE preVendaID IN (${pedidos.join(',')})
               AND filialID = @pFilial
               AND CHARINDEX('${MARCADOR}', Observacoes) = 1`;
}

function conferirColunas(sets) {
    for (const col of Object.keys(sets)) {
        if (!COLUNAS_GRAVAVEIS.has(col)) abortar('coluna fora da lista branca', col);
    }
}

async function gravar(f, pedidos, sets, rotulo) {
    conferirColunas(sets);
    const texto = sqlEstampar(f, pedidos, sets);

    if (!f.gravar) {
        console.log(`\n  [ensaio] ${rotulo} — nada é gravado sem --gravar`);
        console.log(texto.split('\n').map((l) => `    ${l.trim()}`).join('\n'));
        console.log(`    parâmetros: ${JSON.stringify(sets)}`);
        return;
    }

    exigirBackend();
    const sql = doBackend('node_modules/mssql');
    const pares = Object.entries(sets);
    const params = pares.map(([, v], i) => ({
        name: `v${i}`,
        sqltype: typeof v === 'number' ? sql.Float
            : (v === null ? sql.VarChar(50) : sql.VarChar(80)),
        value: v,
    }));
    params.push({ name: 'pFilial', sqltype: sql.Int, value: f.filialID });

    await ler(texto, params);
    console.log(`  ${rotulo}: gravado em ${pedidos.join(', ')}`);
}

// ---------------------------------------------------------------------------
// Comandos
// ---------------------------------------------------------------------------

/** Mostra o que cada canal escreveria. Não conecta em nada — serve sem o backend. */
function cmdPlano(f) {
    console.log('== o que cada canal estampa em _PreVenda ==\n');
    console.log('A coluna `origem` não aparece em nenhum SET: ela é derivada do identificador.');
    console.log(`Sentinela: só pedido com "${MARCADOR}" em Observacoes, na filial ${f.filialID}.\n`);
    for (const nome of canaisEscolhidos(f)) {
        const { origem, sets } = CANAIS[nome];
        console.log(`--- ${nome} -> origem "${origem}" ---`);
        conferirColunas(sets);
        console.log(sqlEstampar(f, f.pedidos.length ? f.pedidos : ['<preVendaID>'], sets)
            .split('\n').map((l) => `  ${l.trim()}`).join('\n'));
        console.log(`  parâmetros: ${JSON.stringify(sets)}\n`);
    }
}

async function cmdEstado(f) {
    const linhas = await ler(
        `SELECT preVendaID, numeroPreVenda, SituacaoDelivery, marketPlace,
                ifoodLocalizer, nnID, keetaId, aiqfomeId, filialIDOrigem, Observacoes
           FROM _PreVenda
          WHERE filialID = ${f.filialID}
            AND CHARINDEX('${MARCADOR}', Observacoes) = 1
          ORDER BY preVendaID DESC`);
    console.log(`== ${linhas.length} pedidos do smoke teste na filial ${f.filialID} ==`);
    for (const l of linhas) {
        const canal = l.ifoodLocalizer ? 'iFood'
            : l.nnID ? '99Food'
                : l.keetaId ? 'Keeta'
                    : l.aiqfomeId ? 'AIQFome'
                        : l.filialIDOrigem ? 'Cardápio Digital' : 'Manual';
        console.log(`  ${l.preVendaID}  nº ${l.numeroPreVenda}  ${String(l.SituacaoDelivery).padEnd(10)} ${canal}`);
    }
}

async function cmdEstampar(f) {
    const canais = canaisEscolhidos(f);
    if (!f.pedidos.length) {
        abortar('nenhum pedido informado',
            'passe --pedidos <preVendaID,...> — um por canal, na ordem de --canais');
    }
    if (f.pedidos.length < canais.length) {
        abortar('menos pedidos que canais',
            `${f.pedidos.length} pedido(s) para ${canais.length} canal(is): `
            + `semeie mais com "python pedido_marketplace.py semear"`);
    }
    for (let i = 0; i < canais.length; i++) {
        const nome = canais[i];
        console.log(`\n== ${nome} -> origem "${CANAIS[nome].origem}" no pedido ${f.pedidos[i]} ==`);
        await gravar(f, [f.pedidos[i]], CANAIS[nome].sets, nome);
    }
    if (f.gravar) {
        console.log('\nO pedido continua na situação em que estava: o painel só olha PREPARO e');
        console.log('PRONTO. Mova com "python smoketeste.py preparo|pronto <preVendaID>".');
        console.log('\nATENÇÃO: não finalize esses pedidos pelo app do entregador. Identificador');
        console.log('de plataforma que não existe do outro lado faz a baixa tentar avisar o');
        console.log('marketplace de verdade. Use "limpar" quando terminar as fotos.');
    }
}

async function cmdLimpar(f) {
    if (!f.pedidos.length) abortar('nenhum pedido informado', 'passe --pedidos <preVendaID,...>');
    await gravar(f, f.pedidos, LIMPEZA, 'limpeza dos identificadores');
}

async function main() {
    const f = lerFlags();
    validarAlvo(f);
    switch (f.comando) {
        case 'plano': return cmdPlano(f);
        case 'estado': return cmdEstado(f);
        case 'estampar': return cmdEstampar(f);
        case 'limpar': return cmdLimpar(f);
        default: return abortar('comando desconhecido', f.comando);
    }
}

main().then(() => process.exit(0)).catch((e) => {
    console.error('\nERRO:', e && e.message ? e.message : e);
    process.exit(1);
});
