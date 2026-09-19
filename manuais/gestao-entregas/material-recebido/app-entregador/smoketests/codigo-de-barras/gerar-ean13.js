/**
 * Gera o PNG de um código de barras EAN-13 a partir do `preVendaID` de um pedido.
 *
 * Existe para o capítulo 08 do manual. O leitor do app aceita **só EAN-13** e trata o código
 * lido assim (`BarcodeScannerModal.js`):
 *
 *     const scannedPreVendaID = parseInt(data.slice(0, -1), 10);
 *
 * Ou seja: joga fora o último dígito (o verificador) e lê o resto como número do pedido. Então
 * o código de um pedido é o `preVendaID` preenchido com zeros à esquerda até 12 dígitos, mais o
 * dígito verificador do EAN-13.
 *
 * Uso:
 *   node gerar-ean13.js 59487819
 *   node gerar-ean13.js 59487819 saida.png
 *
 * Sem dependências de propósito: desenha as barras e escreve o PNG com o `zlib` do Node, para
 * o script rodar em qualquer máquina sem `npm install`.
 */

const fs = require('fs');
const path = require('path');
const zlib = require('zlib');

// ---------------------------------------------------------------------------
// EAN-13
// ---------------------------------------------------------------------------

const L = ['0001101', '0011001', '0010011', '0111101', '0100011',
           '0110001', '0101111', '0111011', '0110111', '0001011'];
const G = ['0100111', '0110011', '0011011', '0100001', '0011101',
           '0111001', '0000101', '0010001', '0001001', '0010111'];
const R = ['1110010', '1100110', '1101100', '1000010', '1011100',
           '1001110', '1010000', '1000100', '1001000', '1110100'];

/** Qual tabela cada um dos seis dígitos da esquerda usa, conforme o primeiro dígito. */
const PARIDADE = ['LLLLLL', 'LLGLGG', 'LLGGLG', 'LLGGGL', 'LGLLGG',
                  'LGGLLG', 'LGGGLL', 'LGLGLG', 'LGLGGL', 'LGGLGL'];

function digitoVerificador(doze) {
    let soma = 0;
    for (let i = 0; i < 12; i++) {
        soma += Number(doze[i]) * (i % 2 === 0 ? 1 : 3);
    }
    return (10 - (soma % 10)) % 10;
}

function codigoDoPedido(preVendaID) {
    const doze = String(preVendaID).padStart(12, '0');
    if (doze.length !== 12) {
        throw new Error(`preVendaID ${preVendaID} não cabe em 12 dígitos`);
    }
    return doze + digitoVerificador(doze);
}

/** Os 95 módulos do EAN-13: guarda, seis dígitos, guarda central, seis dígitos, guarda. */
function modulos(codigo) {
    const paridade = PARIDADE[Number(codigo[0])];
    let bits = '101';
    for (let i = 0; i < 6; i++) {
        const d = Number(codigo[i + 1]);
        bits += paridade[i] === 'L' ? L[d] : G[d];
    }
    bits += '01010';
    for (let i = 0; i < 6; i++) {
        bits += R[Number(codigo[i + 7])];
    }
    bits += '101';
    return bits;
}

// ---------------------------------------------------------------------------
// PNG
// ---------------------------------------------------------------------------

function crc32(buf) {
    let c = ~0;
    for (let i = 0; i < buf.length; i++) {
        c ^= buf[i];
        for (let k = 0; k < 8; k++) c = (c >>> 1) ^ (0xEDB88320 & -(c & 1));
    }
    return ~c >>> 0;
}

function pedaco(tipo, dados) {
    const tamanho = Buffer.alloc(4);
    tamanho.writeUInt32BE(dados.length);
    const corpo = Buffer.concat([Buffer.from(tipo, 'ascii'), dados]);
    const checagem = Buffer.alloc(4);
    checagem.writeUInt32BE(crc32(corpo));
    return Buffer.concat([tamanho, corpo, checagem]);
}

/** PNG em tons de cinza, 8 bits, sem filtro — o suficiente para barras. */
function escreverPNG(caminho, largura, altura, pixels) {
    const cabecalho = Buffer.alloc(13);
    cabecalho.writeUInt32BE(largura, 0);
    cabecalho.writeUInt32BE(altura, 4);
    cabecalho[8] = 8;  // bits por amostra
    cabecalho[9] = 0;  // tons de cinza
    cabecalho[10] = 0; // compressão padrão
    cabecalho[11] = 0; // filtro padrão
    cabecalho[12] = 0; // sem entrelaçamento

    const linhas = [];
    for (let y = 0; y < altura; y++) {
        linhas.push(Buffer.from([0]));
        linhas.push(pixels.subarray(y * largura, (y + 1) * largura));
    }

    fs.writeFileSync(caminho, Buffer.concat([
        Buffer.from([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]),
        pedaco('IHDR', cabecalho),
        pedaco('IDAT', zlib.deflateSync(Buffer.concat(linhas), {level: 9})),
        pedaco('IEND', Buffer.alloc(0))
    ]));
}

// ---------------------------------------------------------------------------
// Desenho
// ---------------------------------------------------------------------------

/**
 * Desenha as barras num retângulo branco.
 *
 * `MODULO` largo (8 px) e margem folgada porque a imagem vai ser lida pela câmera do
 * emulador, que enxerga muito pior que um leitor de verdade: barra fina vira cinza e o
 * decodificador desiste.
 */
const MODULO = 8;
const ALTURA_BARRAS = 260;
const MARGEM_X = 40;
const MARGEM_Y = 40;

function desenhar(codigo, caminho) {
    const bits = modulos(codigo);
    const largura = bits.length * MODULO + MARGEM_X * 2;
    const altura = ALTURA_BARRAS + MARGEM_Y * 2;
    const pixels = Buffer.alloc(largura * altura, 255);

    for (let i = 0; i < bits.length; i++) {
        if (bits[i] !== '1') continue;
        const x0 = MARGEM_X + i * MODULO;
        for (let y = MARGEM_Y; y < MARGEM_Y + ALTURA_BARRAS; y++) {
            pixels.fill(0, y * largura + x0, y * largura + x0 + MODULO);
        }
    }

    escreverPNG(caminho, largura, altura, pixels);
    return {largura, altura};
}

// ---------------------------------------------------------------------------

function main() {
    const preVendaID = process.argv[2];
    if (!preVendaID || !/^\d+$/.test(preVendaID)) {
        console.log('Uso: node gerar-ean13.js <preVendaID> [saida.png]');
        console.log('');
        console.log('O código gerado é o preVendaID com zeros à esquerda (12 dígitos) mais o');
        console.log('dígito verificador — exatamente o que o leitor do app espera.');
        process.exit(1);
    }

    const codigo = codigoDoPedido(preVendaID);
    const saida = process.argv[3]
        ? path.resolve(process.argv[3])
        : path.join(__dirname, `ean13-${preVendaID}.png`);

    const {largura, altura} = desenhar(codigo, saida);

    console.log(`pedido ................ ${preVendaID}`);
    console.log(`código EAN-13 ......... ${codigo}`);
    console.log(`dígito verificador .... ${codigo[12]}`);
    console.log(`o app vai ler ......... ${parseInt(codigo.slice(0, -1), 10)}`);
    console.log(`imagem ................ ${saida} (${largura}x${altura})`);
}

main();
