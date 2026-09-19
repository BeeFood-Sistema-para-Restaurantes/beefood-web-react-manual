#!/usr/bin/env node
/**
 * cenario.js — monta, move e conclui um cenário de Gestão de Entregas 2.0 na sandbox.
 *
 * Existe porque **todo manual deste bloco precisa de um cenário montado à mão**: a tela
 * abre vazia, o entregador não aparece no mapa sem ping de GPS, e o relatório Operação de
 * Entrega só mostra número depois que alguém entregou. Montar isso clicando dá meia hora
 * por manual e sai diferente cada vez.
 *
 * ---------------------------------------------------------------------------------------
 * NENHUMA CREDENCIAL MORA AQUI
 * ---------------------------------------------------------------------------------------
 * Este repositório é **público**. O script não tem senha, host nem segredo: ele carrega
 * tudo do clone do backend, pelo caminho em `--backend` (ou `BEETECH_BACKEND`):
 *
 *   src/services/tokenService.js            -> assina o JWT do painel
 *   src/config/execSQLProc.js e friends     -> MSSQL do ERP (via o seeder)
 *   scripts/seed-gestao-entregas.js         -> cria os pedidos
 *
 * A única coisa que fica em `CONFIG` são IDs da sandbox, que não são segredo.
 *
 * O Aurora é a exceção: o pool do backend usa o driver `mysql` (callback) e queremos
 * `mysql2/promise`. As credenciais são lidas do próprio arquivo de config do backend, com
 * expressão regular, em vez de copiadas para cá.
 *
 * ---------------------------------------------------------------------------------------
 * COMO ELE EVITA ESTRAGO
 * ---------------------------------------------------------------------------------------
 * 1. **Lista branca de alvo** literal (38311/39202). Passar outra empresa aborta. Semear
 *    pedido falso em loja real seria pior que qualquer bug: o lojista sairia entregando.
 * 2. **Só escreve em `posicao` e `entregador_status`** no Aurora, e só para o funcionário
 *    passado em `--entregador`. Rota e parada vão pela **API**, nunca por SQL — assim o
 *    log do ERP, o socket e o `rota_evento` acontecem como no uso real.
 * 3. **`--dry-run`** em tudo que escreve.
 * 4. Os pedidos herdam o marcador `[SEED-ENTREGAS]` do seeder, e a janela de ±6 h da
 *    `viewDeliveryFilaAguardandoEntrega` tira o lote da tela sozinha.
 *
 * ---------------------------------------------------------------------------------------
 * USO
 * ---------------------------------------------------------------------------------------
 *   node cenario.js estado
 *   node cenario.js limpar-fantasma
 *   node cenario.js semear --qtd 4 [--offset 0] [--pronto 1,3]
 *   node cenario.js presenca --entregador 194115 --status DISPONIVEL|PAUSA|OFFLINE
 *   node cenario.js andar --entregador 194115 --para -23.4930,-47.4548 [--passos 6] [--pausa 1]
 *   node cenario.js rota-criar --pedidos 59515246,59515250 [--entregador 194115]
 *   node cenario.js rota-prontos --pedidos 59515246
 *   node cenario.js rota-despachar --rota 121
 *   node cenario.js parada-entregar --rota 121 --pedido 59515246
 *   node cenario.js rota-finalizar --rota 121
 *   node cenario.js rota-excluir --rota 121
 *   node cenario.js ciclo-completo [--qtd 3]      <- o que dá dado de HOJE ao relatório
 *
 * Todos aceitam `--backend <caminho>`, `--empresa`, `--filial`, `--usuario` e `--dry-run`.
 */

'use strict';

const fs = require('fs');
const path = require('path');

// ---------------------------------------------------------------------------
// Configuração da sandbox — IDs, não segredos
// ---------------------------------------------------------------------------

const CONFIG = {
    empresaID: 38311,
    filialID: 39202,
    usuarioID: 88711,
    // Coordenada da loja "BeeFood3 - Manual", lida do GET /painel. Serve de origem do
    // trajeto e de base da distância.
    loja: { lat: -23.5061438, lng: -47.4657927 },
    api: 'https://app3.beetechapi.be',
    backend: process.env.BEETECH_BACKEND
        || path.join(process.env.HOME || '', 'refs', 'beetech-server-node-2.0'),
};

// Literal de propósito: destravar exige editar o arquivo, não passar uma flag.
const ALVOS_PERMITIDOS = [{ empresaID: 38311, filialID: 39202 }];

// No Aurora só estas duas tabelas são escritas, e é o que a Lambda de rastreamento faz.
const TABELAS_GRAVAVEIS = new Set(['posicao', 'entregador_status']);

// ---------------------------------------------------------------------------
// Flags
// ---------------------------------------------------------------------------

function lerFlags() {
    const argv = process.argv.slice(2);
    const comando = argv[0];
    const valor = (nome) => {
        const i = argv.indexOf(nome);
        return i >= 0 ? argv[i + 1] : undefined;
    };
    const lista = (nome) => {
        const v = valor(nome);
        return v ? v.split(',').map((x) => Number(x.trim())).filter(Number.isFinite) : [];
    };
    if (valor('--backend')) CONFIG.backend = valor('--backend');
    return {
        comando,
        empresaID: Number(valor('--empresa') || CONFIG.empresaID),
        filialID: Number(valor('--filial') || CONFIG.filialID),
        usuarioID: Number(valor('--usuario') || CONFIG.usuarioID),
        entregador: valor('--entregador') ? Number(valor('--entregador')) : null,
        status: (valor('--status') || '').toUpperCase() || null,
        qtd: Number(valor('--qtd') || 4),
        offset: Number(valor('--offset') || 0),
        pedidos: lista('--pedidos'),
        pronto: lista('--pronto'),
        rota: valor('--rota') ? Number(valor('--rota')) : null,
        pedido: valor('--pedido') ? Number(valor('--pedido')) : null,
        para: valor('--para'),
        passos: Number(valor('--passos') || 6),
        pausa: Number(valor('--pausa') || 1),
        modoSeco: argv.includes('--dry-run'),
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

function exigirBackend() {
    if (!fs.existsSync(CONFIG.backend)) {
        abortar('clone do backend não encontrado',
            `${CONFIG.backend}\n  Passe --backend <caminho> ou defina BEETECH_BACKEND.`);
    }
    if (!fs.existsSync(path.join(CONFIG.backend, 'node_modules', 'mssql'))) {
        abortar('dependências do backend não instaladas',
            `cd ${CONFIG.backend} && npm install --no-save mssql mysql2`);
    }
}

function doBackend(rel) {
    return require(path.join(CONFIG.backend, rel));
}

// ---------------------------------------------------------------------------
// JWT do painel — assinado com o segredo do backend, não copiado para cá
// ---------------------------------------------------------------------------

let JWT = null;

function jwtDoPainel(f) {
    if (JWT) return JWT;
    const { generateToken } = doBackend('src/services/tokenService');
    JWT = generateToken({ usuarioID: f.usuarioID, empresaID: f.empresaID }).token;
    return JWT;
}

// ---------------------------------------------------------------------------
// Aurora — credenciais lidas do arquivo de config do backend
// ---------------------------------------------------------------------------

let cxAurora = null;

/**
 * O backend declara cada campo como `chave: process.env.X || 'literal'`, às vezes com a
 * quebra de linha entre os dois. A expressão regular aceita o prefixo de ambiente
 * opcional e atravessa a quebra — ler só `chave: 'literal'` não achava nada e o script
 * abortava dizendo que o clone estava errado, quando o errado era a leitura.
 *
 * A variável de ambiente, se estiver definida aqui, ganha: é o mesmo `||` do backend, e é
 * o que permite ao dono rodar contra outro banco sem editar nada.
 */
function credenciaisAurora() {
    const candidatos = [
        'src/config/initMySqlServerGestaoEntrega.js',
        'src/config/execMySQLQueryGestaoEntrega.js',
    ];
    for (const rel of candidatos) {
        const arq = path.join(CONFIG.backend, rel);
        if (!fs.existsSync(arq)) continue;
        const txt = fs.readFileSync(arq, 'utf8');
        const pega = (chave) => {
            const re = new RegExp(
                `\\b${chave}\\s*:\\s*(?:process\\.env\\.(\\w+)\\s*\\|\\|\\s*)?['"\`]([^'"\`]+)['"\`]`,
                's');
            const m = txt.match(re);
            if (!m) return null;
            return (m[1] && process.env[m[1]]) || m[2];
        };
        const cred = {
            host: pega('host'), user: pega('user'),
            password: pega('password'), database: pega('database') || 'entregas',
        };
        if (cred.host && cred.user && cred.password) return cred;
    }
    abortar('não achei as credenciais do Aurora no clone do backend',
        `procurei em: ${candidatos.join(', ')}`);
}

async function aurora() {
    if (cxAurora) return cxAurora;
    const mysql = require(path.join(CONFIG.backend, 'node_modules', 'mysql2', 'promise'));
    const cred = credenciaisAurora();
    cxAurora = await mysql.createConnection({
        ...cred, port: 3306, timezone: 'Z', connectTimeout: 20000,
    });
    return cxAurora;
}

/** Sentinela de escrita: só `posicao` e `entregador_status`, e só por funcionário. */
async function gravarAurora(tabela, sql, params, f) {
    if (!TABELAS_GRAVAVEIS.has(tabela)) {
        abortar('escrita em tabela fora da lista branca do Aurora', tabela);
    }
    if (f.modoSeco) {
        console.log(`  [dry-run] ${tabela}: ${sql.replace(/\s+/g, ' ').slice(0, 90)}…`);
        return { affectedRows: 0 };
    }
    const cx = await aurora();
    const [r] = await cx.execute(sql, params);
    return r;
}

// ---------------------------------------------------------------------------
// HTTP
// ---------------------------------------------------------------------------

async function chamar(metodo, caminho, corpo, f) {
    const url = `${CONFIG.api}${caminho}`;
    if (f.modoSeco && metodo !== 'GET') {
        console.log(`  [dry-run] ${metodo} ${caminho}`);
        if (corpo) console.log(`            ${JSON.stringify(corpo)}`);
        return { resultado: true, modoSeco: true };
    }
    const res = await fetch(url, {
        method: metodo,
        headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${jwtDoPainel(f)}`,
        },
        body: corpo ? JSON.stringify(corpo) : undefined,
    });
    const txt = await res.text();
    let dados;
    try { dados = txt ? JSON.parse(txt) : null; } catch { dados = txt; }
    if (res.status >= 400) {
        throw new Error(`${metodo} ${caminho} -> ${res.status} ${JSON.stringify(dados)}`);
    }
    return dados;
}

const ctxRota = (f) => ({
    empresaID: f.empresaID, filialID: f.filialID,
    usuarioID: f.usuarioID, usuario: 'cenario.js',
});

// ---------------------------------------------------------------------------
// Leitura do painel
// ---------------------------------------------------------------------------

async function painel(f) {
    return chamar('GET',
        `/api/entrega2/gestao/painel/${f.empresaID}/${f.filialID}/${f.usuarioID}`, null, f);
}

async function mostrarEstado(f) {
    const p = await painel(f);
    console.log(`\nloja: ${String(p.loja.nome).trim()}  (${p.loja.latitude}, ${p.loja.longitude})`);
    console.log(`resumo: ${JSON.stringify(p.resumoPedidos)}`);

    console.log(`\npedidos (${p.pedidos.length}):`);
    for (const x of p.pedidos) {
        console.log(`  ${String('#' + x.numeroPreVenda).padEnd(7)} id=${x.preVendaID}`
            + `  ${String(x.status).padEnd(11)} ${String(x.idadeMinutos + ' min').padStart(7)}`
            + `  rota=${x.rotaID ?? '-'}  ${String(x.enderecoResumo || '').slice(0, 42)}`);
    }

    console.log(`\nentregadores (${p.entregadores.length}):`);
    for (const e of p.entregadores) {
        const pos = e.latitude != null
            ? `pos há ${e.posicaoIdadeMinutos} min, ${e.distanciaLojaMetros} m da loja`
            : 'sem posição';
        console.log(`  ${e.funcionarioID}  ${String(e.nome).padEnd(20).slice(0, 20)}`
            + `  ${String(e.status).padEnd(10)} rota=${e.rotaIDAtual ?? '-'}  ${pos}`);
    }

    console.log(`\nrotas (${p.rotas.length}):`);
    for (const r of p.rotas) {
        console.log(`  rota ${r.rotaID} ${String(r.codigo || '').padEnd(3)}`
            + ` ${String(r.status).padEnd(10)} entregador=${r.funcionarioID ?? '-'}`
            + `  origem=${r.origem}  paradas=${(r.paradas || []).length}`
            + `  idade=${r.idadeMinutos} min`);
        for (const s of r.paradas || []) {
            console.log(`      ${s.ordem}. #${s.numeroPedido} id=${s.preVendaID}`
                + ` ${String(s.status).padEnd(10)} ${String(s.enderecoResumo || '').slice(0, 38)}`);
        }
    }
    return p;
}

// ---------------------------------------------------------------------------
// Rota fantasma
// ---------------------------------------------------------------------------

/**
 * `entregador_status.rotaIDAtual` apontando para rota que já não existe deixa o
 * entregador **ocupado para sempre**: o despacho automático o ignora e o painel mostra
 * vínculo com uma rota que ninguém vê. É a sujeira que mais estraga captura em silêncio.
 */
async function limparFantasma(f) {
    const cx = await aurora();
    const [linhas] = await cx.query(
        `SELECT s.funcionarioID, s.rotaIDAtual
           FROM entregador_status s
           LEFT JOIN rota r ON r.id = s.rotaIDAtual
          WHERE s.filialID = ? AND s.rotaIDAtual IS NOT NULL AND r.id IS NULL`,
        [f.filialID]);

    if (!linhas.length) {
        console.log('nenhuma rota fantasma nesta filial.');
        return 0;
    }
    for (const l of linhas) {
        console.log(`  entregador ${l.funcionarioID} aponta para rota ${l.rotaIDAtual},`
            + ' que não existe — limpando');
        await gravarAurora('entregador_status',
            `UPDATE entregador_status SET rotaIDAtual = NULL
              WHERE filialID = ? AND funcionarioID = ? AND rotaIDAtual = ?`,
            [f.filialID, l.funcionarioID, l.rotaIDAtual], f);
    }
    console.log(`${linhas.length} vínculo(s) fantasma limpo(s).`);
    return linhas.length;
}

// ---------------------------------------------------------------------------
// Semear pedidos
// ---------------------------------------------------------------------------

/**
 * A idade do pedido é o que decide três coisas na tela, e por isso o seeder a controla em
 * vez de deixar no `GETDATE()`: acima de **6 h** o pedido sai da view e não aparece;
 * acima de **120 min** ele cai no freio de arranque do despacho automático; e o rótulo
 * "há N min" do painel é lido dela. O seeder distribui as idades entre 5 e 100 min.
 */
async function semear(f) {
    exigirBackend();
    const { semearLote } = doBackend('scripts/seed-gestao-entregas.js');
    const { ctx, criados } = await semearLote({
        empresaID: f.empresaID, filialID: f.filialID, usuarioID: f.usuarioID,
        qtd: f.qtd, offsetEndereco: f.offset, modoSeco: f.modoSeco,
        conferirPainel: false,
    });
    const ids = (criados || []).map((c) => c.preVendaID);
    if (ids.length) console.log(`\npreVendaIDs criados: ${ids.join(',')}`);
    return { ctx, ids, criados: criados || [] };
}

async function marcarProntos(f, preVendaIDs) {
    exigirBackend();
    const { promoverSituacao } = doBackend('scripts/seed-gestao-entregas.js');
    for (const id of preVendaIDs) {
        if (f.modoSeco) { console.log(`  [dry-run] PRONTO em ${id}`); continue; }
        await promoverSituacao({ filialID: f.filialID }, id, 'PRONTO');
        console.log(`  pedido ${id} -> PRONTO`);
    }
}

// ---------------------------------------------------------------------------
// Presença e movimento do entregador
// ---------------------------------------------------------------------------

/**
 * A presença vai pela **API do app** (Basic Auth global, sem JWT) e não por SQL, porque é
 * ela que abre e fecha `entregador_sessao` e dispara o socket que o painel escuta. Um
 * `UPDATE` direto deixaria a sessão aberta e o painel sem evento.
 */
async function presenca(f) {
    if (!f.entregador) abortar('falta --entregador');
    const status = f.status || 'DISPONIVEL';
    if (!['OFFLINE', 'DISPONIVEL', 'PAUSA', 'EM_ROTA'].includes(status)) {
        abortar('status inválido', status);
    }
    const corpo = {
        empresaID: f.empresaID, filialID: f.filialID, funcionarioID: f.entregador,
        online: status !== 'OFFLINE', status,
        origemFim: status === 'OFFLINE' ? 'MANUAL' : undefined,
    };
    if (f.modoSeco) {
        console.log(`  [dry-run] POST /presenca ${JSON.stringify(corpo)}`);
        return;
    }
    const res = await fetch(`${CONFIG.api}/api/entrega2/gestao/presenca`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // Basic do gate global. Lido do middleware do backend, não escrito aqui.
            Authorization: 'Basic ' + Buffer.from(basicDoBackend()).toString('base64'),
        },
        body: JSON.stringify(corpo),
    });
    console.log(`  presença ${f.entregador} -> ${status}: ${await res.text()}`);
}

function basicDoBackend() {
    const arq = path.join(CONFIG.backend, 'src/api/middleware/gateGlobalMiddleware.js');
    if (!fs.existsSync(arq)) abortar('gateGlobalMiddleware.js não encontrado', arq);
    const txt = fs.readFileSync(arq, 'utf8');
    const m = txt.match(/'name'\]\s*===\s*'([^']+)'\s*&&\s*user\['pass'\]\s*===\s*'([^']+)'/);
    if (!m) abortar('não achei o par Basic no gateGlobalMiddleware.js');
    return `${m[1]}:${m[2]}`;
}

const metros = (a, b) => {
    const R = 6371000, r = Math.PI / 180;
    const dLat = (b.lat - a.lat) * r, dLng = (b.lng - a.lng) * r;
    const h = Math.sin(dLat / 2) ** 2
        + Math.cos(a.lat * r) * Math.cos(b.lat * r) * Math.sin(dLng / 2) ** 2;
    return Math.round(2 * R * Math.asin(Math.sqrt(h)));
};

const espera = (ms) => new Promise((r) => setTimeout(r, ms));

/**
 * Grava ping de GPS igual à Lambda de rastreamento: uma linha em `posicao` e o
 * `entregador_status` recebendo a **mais recente**.
 *
 * A Lambda em si não é chamável de fora: ela exige `x-api-key` guardada num `.env`
 * gitignored. Escrever aqui chega ao mesmo estado, porque é o que ela faz.
 *
 * `dataHoraServidor` é **UTC** (`UTC_TIMESTAMP()`), e é dele que sai o "há N min" do
 * mapa. Usar `NOW()` numa instância em outro fuso mostraria o entregador com horas de
 * atraso e o cron de timeout o derrubaria por engano.
 */
async function ping(f, lat, lng, rotaID) {
    const dist = metros(CONFIG.loja, { lat, lng });
    await gravarAurora('posicao',
        `INSERT INTO posicao (empresaID, filialID, funcionarioID, latitude, longitude,
                              precisaoMetros, velocidadeMs, bateria, origem, rotaID,
                              dataHoraCelular, dataHoraServidor)
         VALUES (?,?,?,?,?, 12.0, 6.5, 88, 'BACKGROUND', ?, UTC_TIMESTAMP(), UTC_TIMESTAMP())`,
        [f.empresaID, f.filialID, f.entregador, lat, lng, rotaID ?? null], f);

    await gravarAurora('entregador_status',
        `UPDATE entregador_status
            SET ultimaLatitude = ?, ultimaLongitude = ?,
                dataHoraUltimaPosicao = UTC_TIMESTAMP(),
                distanciaLojaMetros = ?, precisaoMetros = 12.0, bateria = 88,
                appVersao = '1.0.0-cenario'
          WHERE filialID = ? AND funcionarioID = ?`,
        [lat, lng, dist, f.filialID, f.entregador], f);

    return dist;
}

/** Caminha em linha reta da posição atual (ou da loja) até o destino, em N passos. */
async function andar(f) {
    if (!f.entregador) abortar('falta --entregador');
    if (!f.para) abortar('falta --para lat,lng');
    const [lat, lng] = f.para.split(',').map(Number);
    if (!Number.isFinite(lat) || !Number.isFinite(lng)) abortar('--para inválido', f.para);

    let origem = { ...CONFIG.loja };
    let rotaID = null;
    if (!f.modoSeco) {
        const cx = await aurora();
        const [[st]] = await cx.query(
            `SELECT ultimaLatitude, ultimaLongitude, rotaIDAtual FROM entregador_status
              WHERE filialID = ? AND funcionarioID = ?`, [f.filialID, f.entregador]);
        if (st && st.ultimaLatitude != null) {
            origem = { lat: Number(st.ultimaLatitude), lng: Number(st.ultimaLongitude) };
        }
        rotaID = st ? st.rotaIDAtual : null;
    }

    console.log(`  de ${origem.lat.toFixed(6)},${origem.lng.toFixed(6)}`
        + ` até ${lat},${lng} em ${f.passos} passos`);
    for (let i = 1; i <= f.passos; i++) {
        const t = i / f.passos;
        const p = { lat: origem.lat + (lat - origem.lat) * t,
            lng: origem.lng + (lng - origem.lng) * t };
        const d = await ping(f, Number(p.lat.toFixed(7)), Number(p.lng.toFixed(7)), rotaID);
        console.log(`   passo ${i}/${f.passos}: ${p.lat.toFixed(6)},${p.lng.toFixed(6)}`
            + ` — ${d} m da loja`);
        if (i < f.passos) await espera(f.pausa * 1000);
    }
}

// ---------------------------------------------------------------------------
// Rota — sempre pela API, nunca por SQL
// ---------------------------------------------------------------------------

/**
 * O corpo das rotas de rota espera `{preVendaID, numeroPreVenda, numeroPedido}`, e os dois
 * números servem só para rotular o log do ERP.
 *
 * **Pedido e parada não têm o mesmo formato no snapshot.** Em `pedidos` vem
 * `numeroPreVenda` e `numeroPedido`; em `rotas[].paradas` vem só `numeroPedido`, e ele
 * carrega o número da pré-venda quando o pedido é do balcão. Ler o campo errado devolvia
 * `undefined` no log sem erro nenhum — daí a normalização acontecer num lugar só.
 */
async function pedidosParaCorpo(f, ids) {
    const p = await painel(f);
    const porID = new Map();
    for (const x of p.pedidos) {
        porID.set(x.preVendaID, {
            preVendaID: x.preVendaID,
            numeroPreVenda: x.numeroPreVenda ?? null,
            numeroPedido: x.numeroPedido ?? null,
        });
    }
    for (const r of p.rotas) {
        for (const s of r.paradas || []) {
            if (porID.has(s.preVendaID)) continue;
            porID.set(s.preVendaID, {
                preVendaID: s.preVendaID,
                numeroPreVenda: s.numeroPedido ?? null,
                numeroPedido: s.numeroPedido ?? null,
            });
        }
    }
    return ids.map((id) => {
        const x = porID.get(id);
        if (!x) abortar('pedido não está no painel', String(id));
        return x;
    });
}

async function rotaCriar(f) {
    if (!f.pedidos.length) abortar('falta --pedidos');
    const pedidos = f.modoSeco ? f.pedidos.map((id) => ({ preVendaID: id }))
        : await pedidosParaCorpo(f, f.pedidos);
    let entregador = null;
    if (f.entregador) {
        const p = await painel(f);
        const e = (p.entregadores || []).find((x) => x.funcionarioID === f.entregador);
        entregador = { funcionarioID: f.entregador, nome: e ? e.nome : String(f.entregador) };
    }
    const res = await chamar('POST', '/api/entrega2/gestao/rota', {
        ...ctxRota(f), pedidos,
        funcionarioID: entregador ? entregador.funcionarioID : null,
        entregadorNome: entregador ? entregador.nome : null,
    }, f);
    console.log(`  rota criada: ${JSON.stringify(res)}`);
    return res;
}

async function rotaProntos(f) {
    if (!f.pedidos.length) abortar('falta --pedidos');
    const pedidos = await pedidosParaCorpo(f, f.pedidos);
    const res = await chamar('POST', '/api/entrega2/gestao/pedidos/prontos',
        { ...ctxRota(f), pedidos }, f);
    console.log(`  marcados prontos: ${JSON.stringify(res)}`);
}

/**
 * Despachar **não** é organização interna: grava `ENTREGA` no ERP e isso atravessa o
 * `SituacaoDeliveryUpdater`, que notifica marketplace, manda para a impressora e
 * enfileira WhatsApp. É o comando com mais efeito colateral deste arquivo.
 */
async function rotaDespachar(f) {
    if (!f.rota) abortar('falta --rota');
    const res = await chamar('PUT', `/api/entrega2/gestao/rota/${f.rota}/despachar`,
        { ...ctxRota(f) }, f);
    console.log(`  rota ${f.rota} despachada: ${JSON.stringify(res)}`);
}

async function paradaEntregar(f) {
    if (!f.rota) abortar('falta --rota');
    if (!f.pedido) abortar('falta --pedido (o preVendaID da parada)');
    const [parada] = await pedidosParaCorpo(f, [f.pedido]);
    const res = await chamar('PUT',
        `/api/entrega2/gestao/rota/${f.rota}/paradas/${f.pedido}/entregar`,
        { ...ctxRota(f), pedidos: [parada] }, f);
    console.log(`  parada ${f.pedido} entregue: ${JSON.stringify(res)}`);
    return res;
}

async function rotaFinalizar(f) {
    if (!f.rota) abortar('falta --rota');
    const res = await chamar('PUT', `/api/entrega2/gestao/rota/${f.rota}/finalizar`,
        { ...ctxRota(f) }, f);
    console.log(`  rota ${f.rota} finalizada: ${JSON.stringify(res)}`);
    return res;
}

async function rotaExcluir(f) {
    if (!f.rota) abortar('falta --rota');
    const p = await painel(f);
    const r = (p.rotas || []).find((x) => x.rotaID === f.rota);
    if (!r) abortar('rota não está no painel', String(f.rota));
    const pedidos = await pedidosParaCorpo(f, (r.paradas || []).map((s) => s.preVendaID));
    const res = await chamar('POST', `/api/entrega2/gestao/rota/${f.rota}/excluir`,
        { ...ctxRota(f), pedidos, entregadorNome: null }, f);
    console.log(`  rota ${f.rota} excluída: ${JSON.stringify(res)}`);
}

// ---------------------------------------------------------------------------
// Ciclo completo — é o que faz o relatório ter número de HOJE
// ---------------------------------------------------------------------------

/**
 * O relatório **Operação de Entrega** mede pedido entregue, com entregador atribuído e
 * carimbo de despacho. Nenhum desses três existe num pedido só semeado: é preciso
 * atravessar a rota inteira. Este comando faz isso de uma vez, na ordem em que acontece
 * na vida real, e é o pré-requisito dos dois manuais de relatório.
 */
async function cicloCompleto(f) {
    console.log('\n=== 1. limpando rota fantasma ===');
    await limparFantasma(f);

    console.log('\n=== 2. semeando pedidos ===');
    const { criados } = await semear(f);
    const ids = criados.map((c) => c.preVendaID);
    if (!ids.length && !f.modoSeco) abortar('o seeder não criou pedido nenhum');

    console.log('\n=== 3. marcando todos como PRONTO ===');
    await marcarProntos(f, ids);

    const entregador = f.entregador || 194115;
    console.log(`\n=== 4. entregador ${entregador} disponível na loja ===`);
    await presenca({ ...f, entregador, status: 'DISPONIVEL' });
    await ping({ ...f, entregador }, CONFIG.loja.lat, CONFIG.loja.lng, null);

    console.log('\n=== 5. criando a rota com o entregador ===');
    const criada = await rotaCriar({ ...f, pedidos: ids, entregador });
    const rotaID = criada && (criada.rotaID || (criada.rota && criada.rota.rotaID));
    if (!rotaID && !f.modoSeco) abortar('não consegui o rotaID da resposta',
        JSON.stringify(criada));

    console.log(`\n=== 6. despachando a rota ${rotaID} ===`);
    await rotaDespachar({ ...f, rota: rotaID });

    console.log('\n=== 7. entregando parada por parada, andando entre elas ===');
    const p = await painel(f);
    const rota = (p.rotas || []).find((x) => x.rotaID === rotaID);
    for (const s of (rota && rota.paradas || [])) {
        if (s.latitude != null) {
            await andar({ ...f, entregador, para: `${s.latitude},${s.longitude}`, passos: 3 });
        }
        await paradaEntregar({ ...f, rota: rotaID, pedido: s.preVendaID });
    }

    console.log(`\n=== 8. finalizando a rota ${rotaID} ===`);
    await rotaFinalizar({ ...f, rota: rotaID });

    console.log('\n=== 9. entregador de volta para offline ===');
    await presenca({ ...f, entregador, status: 'OFFLINE' });

    console.log(`\nCICLO COMPLETO. rota ${rotaID}, ${ids.length} entregas concluídas hoje.`);
    console.log('O relatório Desempenho > Delivery > Operação de Entrega já tem o que medir.');
    return { rotaID, ids };
}

// ---------------------------------------------------------------------------

const COMANDOS = {
    estado: mostrarEstado,
    'limpar-fantasma': limparFantasma,
    semear,
    presenca,
    andar,
    'rota-criar': rotaCriar,
    'rota-prontos': rotaProntos,
    'rota-despachar': rotaDespachar,
    'parada-entregar': paradaEntregar,
    'rota-finalizar': rotaFinalizar,
    'rota-excluir': rotaExcluir,
    'ciclo-completo': cicloCompleto,
};

async function main() {
    const f = lerFlags();
    if (!f.comando || !COMANDOS[f.comando]) {
        console.log('Comandos: ' + Object.keys(COMANDOS).join(', '));
        console.log('\nVeja o cabeçalho deste arquivo para o uso de cada um.');
        process.exit(f.comando ? 1 : 0);
    }
    validarAlvo(f);
    if (f.modoSeco) console.log('--dry-run: nada será escrito.');
    console.log(`empresa ${f.empresaID} / filial ${f.filialID} / usuário ${f.usuarioID}`);

    await COMANDOS[f.comando](f);

    if (cxAurora) await cxAurora.end();
}

if (require.main === module) {
    main().catch((e) => {
        console.log('\nERRO:', e && e.stack ? e.stack : e);
        process.exit(1);
    });
}

// O `smoke-app.js` monta os cenários do **app** em cima daqui: quem fala com a API de rota
// continua sendo este arquivo, para existir um lugar só onde a rota é criada e despachada.
module.exports = {
    CONFIG,
    painel,
    presenca,
    ping,
    andar,
    semear,
    marcarProntos,
    rotaCriar,
    rotaDespachar,
    paradaEntregar,
    rotaFinalizar,
    rotaExcluir,
    limparFantasma,
    cicloCompleto,
    basicDoBackend,
    aurora,
    gravarAurora,
    exigirBackend,
    doBackend,
    abortar,
    validarAlvo,
};
