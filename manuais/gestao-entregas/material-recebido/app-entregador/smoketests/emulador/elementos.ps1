# Lista os elementos da tela atual do emulador com o centro de cada um, para tocar
# por nome em vez de por pixel adivinhado.
#
# Le a arvore de acessibilidade via uiautomator. O app usa accessibilityLabel em boa
# parte dos controles, entao texto e content-desc bastam na maioria das telas.
#
# Uso:
#   .\elementos.ps1                 # so os clicaveis e os que tem texto
#   .\elementos.ps1 -Filtro FINAL   # so os que casam com o termo
#   .\elementos.ps1 -Tudo           # a arvore inteira

param(
    [string]$Filtro = '',
    [switch]$Tudo
)

$ErrorActionPreference = 'Stop'

$temp = Join-Path $env:TEMP 'ui-emulador.xml'
adb shell uiautomator dump /sdcard/_ui.xml | Out-Null
adb pull /sdcard/_ui.xml $temp | Out-Null
adb shell rm -f /sdcard/_ui.xml | Out-Null

[xml]$arvore = Get-Content $temp -Encoding UTF8

$linhas = @()
foreach ($no in $arvore.SelectNodes('//node')) {
    $texto = $no.text
    $desc = $no.'content-desc'
    $id = $no.'resource-id'
    $clicavel = $no.clickable -eq 'true'

    if (-not $Tudo) {
        if (-not $clicavel -and [string]::IsNullOrWhiteSpace($texto) -and [string]::IsNullOrWhiteSpace($desc)) {
            continue
        }
    }

    # bounds vem como "[esq,topo][dir,baixo]"
    if ($no.bounds -notmatch '\[(\d+),(\d+)\]\[(\d+),(\d+)\]') { continue }
    $x = [int](([int]$Matches[1] + [int]$Matches[3]) / 2)
    $y = [int](([int]$Matches[2] + [int]$Matches[4]) / 2)

    $rotulo = if ($texto) { $texto } elseif ($desc) { $desc } elseif ($id) { $id } else { $no.class }
    # Rotulo longo empurra as colunas de coordenada fora da tela; 58 e o que cabe.
    if ($rotulo.Length -gt 58) { $rotulo = $rotulo.Substring(0, 55) + '...' }

    $linhas += [pscustomobject]@{
        Rotulo   = $rotulo
        X        = $x
        Y        = $y
        Clicavel = if ($clicavel) { 'sim' } else { '' }
        Classe   = ($no.class -replace '^.*\.', '')
    }
}

if ($Filtro) {
    $linhas = $linhas | Where-Object { $_.Rotulo -like "*$Filtro*" }
}

$linhas | Format-Table -AutoSize -Wrap
Write-Host "`nToque com:  adb shell input tap X Y"
