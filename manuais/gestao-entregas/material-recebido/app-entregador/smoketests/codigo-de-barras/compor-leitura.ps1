# Compõe a ilustração do capítulo 08: o código de barras dentro da faixa da câmera.
#
# Por que compor em vez de capturar: a câmera do emulador só enxerga a cena virtual (uma sala
# com TV), e não há como colocar a etiqueta do pedido na frente dela sem controlar o emulador
# pelo teclado. Então a captura da tela é real e apenas o conteúdo DA CÂMERA é sobreposto —
# a faixa de status, os textos e os botões são os do app, sem alteração.
#
# A movimentação correspondente é feita de verdade, pela rota `tentrega/lerCodigoBarras`,
# como está documentado no capítulo.
#
# Uso:
#   .\compor-leitura.ps1 -Captura ..\..\08-codigo-de-barras\prints\01-leitor-aberto.png `
#                        -CodigoBarras .\ean13-59487819.png `
#                        -Saida ..\..\08-codigo-de-barras\prints\02-codigo-na-faixa.png

param(
    [Parameter(Mandatory = $true)][string]$Captura,
    [Parameter(Mandatory = $true)][string]$CodigoBarras,
    [Parameter(Mandatory = $true)][string]$Saida
)

Add-Type -AssemblyName System.Drawing

$telaPath = (Resolve-Path $Captura).Path
$barrasPath = (Resolve-Path $CodigoBarras).Path

$tela = [System.Drawing.Image]::FromFile($telaPath)
$barras = [System.Drawing.Image]::FromFile($barrasPath)

# A faixa da câmera tem 130dp de altura (ver `cameraStrip` em BarcodeScannerModal.js) e fica
# no meio vertical da tela, entre as duas linhas vermelhas de 4dp.
$fatorAltura = 0.4219   # onde a faixa começa, em fração da altura da tela
$alturaFaixa = 0.1562   # altura da faixa, em fração da altura da tela
$bordaVermelha = [int]($tela.Width * 0.0097)

$faixaY = [int]($tela.Height * $fatorAltura)
$faixaH = [int]($tela.Height * $alturaFaixa)
$faixaX = $bordaVermelha
$faixaW = $tela.Width - ($bordaVermelha * 2)

$copia = New-Object System.Drawing.Bitmap $tela
$g = [System.Drawing.Graphics]::FromImage($copia)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic

# Fundo da etiqueta, ocupando a área que a câmera mostra.
$g.FillRectangle([System.Drawing.Brushes]::White, $faixaX, $faixaY, $faixaW, $faixaH)

# O código de barras, mantendo proporção, com folga em cima e embaixo.
$folga = [int]($faixaH * 0.10)
$alvoH = $faixaH - ($folga * 2)
$alvoW = [int]($barras.Width * ($alvoH / $barras.Height))
if ($alvoW -gt $faixaW) {
    $alvoW = $faixaW
    $alvoH = [int]($barras.Height * ($alvoW / $barras.Width))
}
$alvoX = $faixaX + [int](($faixaW - $alvoW) / 2)
$alvoY = $faixaY + [int](($faixaH - $alvoH) / 2)
$g.DrawImage($barras, $alvoX, $alvoY, $alvoW, $alvoH)

$g.Dispose()

$saidaPath = [System.IO.Path]::GetFullPath((Join-Path (Get-Location) $Saida))
$copia.Save($saidaPath, [System.Drawing.Imaging.ImageFormat]::Png)

$copia.Dispose()
$tela.Dispose()
$barras.Dispose()

Write-Host "OK  $saidaPath"
Write-Host "faixa da camera: x=$faixaX y=$faixaY $faixaW x $faixaH"
Write-Host "codigo desenhado: x=$alvoX y=$alvoY $alvoW x $alvoH"
