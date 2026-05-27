# Hermes fallback nativo - ARA principal

Fecha: 2026-05-27

## Estado actual

ARA principal:
- HERMES_HOME: C:\Users\Usuario\AppData\Local\hermes
- Modelo principal: gpt-5.5
- Provider principal: openai-codex
- Config version: v24
- Auth openai-codex: logged in
- OpenRouter API: OK

Fallback configurado:
- Provider: openrouter
- Modelo: deepseek/deepseek-v4-pro
- Base URL: https://openrouter.ai/api/v1

## Comandos nativos usados

Ver ayuda:

    hermes fallback --help

Ver estado:

    hermes fallback list

Añadir fallback:

    hermes fallback add

Eliminar fallback:

    hermes fallback remove

Vaciar fallback:

    hermes fallback clear

## Procedimiento correcto

1. Establecer HERMES_HOME de ARA principal:

    $env:HERMES_HOME = "C:\Users\Usuario\AppData\Local\hermes"

2. Consultar ayuda:

    & "C:\Users\Usuario\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe" fallback --help

3. Consultar estado:

    & "C:\Users\Usuario\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe" fallback list

4. Crear backup antes de modificar config:

    Copy-Item "C:\Users\Usuario\AppData\Local\hermes\config.yaml" "C:\Users\Usuario\AppData\Local\hermes\config.yaml.backup-before-fallback-20260527-163949"

5. Añadir fallback con comando nativo:

    & "C:\Users\Usuario\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe" fallback add

Selecciones realizadas:
- Provider: OpenRouter
- Mantener API key existente
- Modelo: deepseek/deepseek-v4-pro

## Resultado verificado

Salida de hermes fallback list:

    Primary: gpt-5.5 (via openai-codex)

    Fallback chain (1 entry):
      1. deepseek/deepseek-v4-pro (via openrouter) [https://openrouter.ai/api/v1]

## Validaciones

Hermes doctor:
- Config version up to date: v24
- OpenAI Codex auth: logged in
- OpenRouter API: OK
- Sin errores críticos para Mail Manager

Pruebas CLI:
- "ARA principal funcionando."
- "segunda prueba OK"

Logs recientes:
- Las pruebas usaron provider=openai-codex
- Las pruebas usaron model=gpt-5.5
- El fallback quedó configurado pero no se activó en pruebas normales

## Aprendizaje

Antes de editar config.yaml a mano:
1. Ejecutar hermes <comando> --help
2. Buscar comandos nativos
3. Hacer backup
4. Aplicar con CLI
5. Verificar con doctor, fallback list y logs

No editar config.yaml manualmente salvo emergencia.
