# start-ara-lab-status.ps1
# Arranque seguro de comprobacion para ARA Lab en Windows.

$ErrorActionPreference = "Stop"

$env:HERMES_HOME = "C:\proyectos\hermes\instances\ara-lab"

Set-Location "C:\proyectos\hermes-laboratorio"

Write-Host "ARA Lab - comprobacion de entorno" -ForegroundColor Cyan
Write-Host "HERMES_HOME = $env:HERMES_HOME"
Write-Host "Repositorio = $(Get-Location)"
Write-Host ""

git status --short --branch

Write-Host ""
Write-Host "Estado Hermes:"
& "C:\Users\Usuario\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe" status

