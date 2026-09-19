# Captura a tela do emulador e grava com nome sequencial na pasta do capitulo.
#
# Existe porque `adb exec-out screencap -p > arquivo.png` CORROMPE o PNG no PowerShell:
# o operador de redirecionamento trata o binario como texto. O caminho valido e o de
# dois passos, screencap no /sdcard seguido de pull.
#
# Uso:
#   .\capturar.ps1 -Capitulo 01-primeiros-passos -Nome 02-login-vazio
#   .\capturar.ps1 -Capitulo 01-primeiros-passos -Nome 03-erro -Espera 2

param(
    [Parameter(Mandatory = $true)][string]$Capitulo,
    [Parameter(Mandatory = $true)][string]$Nome,
    [int]$Espera = 0
)

$ErrorActionPreference = 'Stop'

if ($Espera -gt 0) { Start-Sleep -Seconds $Espera }

$raiz = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$destinoPasta = Join-Path $raiz "$Capitulo\prints"
New-Item -ItemType Directory -Force -Path $destinoPasta | Out-Null

$destino = Join-Path $destinoPasta "$Nome.png"

adb shell screencap -p /sdcard/_cap.png | Out-Null
adb pull /sdcard/_cap.png $destino | Out-Null
adb shell rm -f /sdcard/_cap.png | Out-Null

$tamanho = (Get-Item $destino).Length
if ($tamanho -lt 10000) {
    throw "Captura suspeita: $destino tem apenas $tamanho bytes."
}

Write-Host "OK  $destino  ($([math]::Round($tamanho / 1024)) KB)"
