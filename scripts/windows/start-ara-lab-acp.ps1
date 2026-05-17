# start-ara-lab-acp.ps1
# Arranca Hermes en modo ACP usando la instancia aislada ara-lab.
# Pensado para integraciones con interfaces compatibles con ACP.

$ErrorActionPreference = "Stop"

$env:HERMES_HOME = "C:\proyectos\hermes\instances\ara-lab"

Set-Location "C:\proyectos\hermes-laboratorio"

Write-Host "Iniciando Hermes ACP con ARA Lab..." -ForegroundColor Cyan
Write-Host "HERMES_HOME = $env:HERMES_HOME"
Write-Host "Repositorio = $(Get-Location)"
Write-Host ""

& "C:\Users\Usuario\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe" acp
