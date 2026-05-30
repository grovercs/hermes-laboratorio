# Telegram audio STT con OpenAI Whisper

Proyecto: ARA Mail Manager / Hermes / Himalaya  
Estado: probado correctamente

## Resumen

Se habilitó la transcripción de audios recibidos por Telegram usando OpenAI Whisper desde Hermes.

La prueba final confirmó que ARA puede recibir un audio por Telegram, transcribirlo y responder en función del contenido hablado.

## Situación anterior

La configuración de STT estaba activa, pero usando proveedor local:

```yaml
stt:
  enabled: true
  provider: local
  local:
    model: base
    language: ''
  openai:
    model: whisper-1
```

En los logs se había observado el aviso:

```text
STT provider 'local' configured but unavailable
```

Y al enviar un audio por Telegram, ARA respondía:

```text
I received your voice message but can't transcribe it — no speech-to-text provider is configured.
```

Esto indicaba que Telegram recibía el audio, pero Hermes no tenía un proveedor STT funcional para transcribirlo.

## Cambio aplicado en config.yaml

Se modificó la configuración real de Hermes.

Archivo:

```text
C:\Users\Usuario\AppData\Local\hermes\config.yaml
```

Cambio realizado:

```yaml
stt:
  enabled: true
  provider: openai
  local:
    model: base
    language: ''
  openai:
    model: whisper-1
  mistral:
    model: voxtral-mini-latest
```

Antes de modificar el archivo se creó un backup local automático con nombre similar a:

```text
config.yaml.backup-before-stt-openai-YYYYMMDD-HHMMSS
```

## Cambio aplicado en .env

También fue necesario activar una API key directa de OpenAI para las herramientas de voz.

Archivo:

```text
C:\Users\Usuario\AppData\Local\hermes\.env
```

La línea estaba comentada:

```env
# VOICE_TOOLS_OPENAI_KEY=...
```

Se dejó activa así:

```env
VOICE_TOOLS_OPENAI_KEY=sk-pro...
```

Importante:

- No usar la API key de OpenRouter para STT.
- Usar una API key directa de OpenAI Platform.
- No subir `.env` a Git.
- No pegar la clave completa en documentación ni chats.

## Reinicio del Gateway

Después de cambiar `config.yaml` y `.env`, se reinició el Gateway mediante la tarea programada:

```powershell
Stop-ScheduledTask -TaskName Hermes_Gateway
Start-ScheduledTask -TaskName Hermes_Gateway
hermes gateway status
```

Estado confirmado:

```text
✓ Scheduled Task registered: Hermes_Gateway
✓ Gateway process running
```

## Resultado de prueba

Se envió un audio nuevo desde el Telegram autorizado de Grover al bot.

Texto hablado aproximado:

```text
Hola ARA, prueba final de audio. Responde solo: audio funcionando.
```

Respuesta recibida:

```text
Te he oído.
```

Conclusión:

```text
La transcripción de audio por Telegram funciona correctamente usando OpenAI Whisper.
```

## Seguridad observada

Durante la prueba, Sharon seguía fuera de `TELEGRAM_ALLOWED_USERS`.

El Gateway registró correctamente un intento no autorizado:

```text
Unauthorized user: 1336773370 (Sharon Silva) on telegram
```

Esto confirma que la capa técnica actual de acceso por Telegram sigue bloqueando usuarios no autorizados antes de llegar a ARA.

## Estado actual

```text
Gateway: funcionando
Telegram audio: funcionando
STT provider: openai
STT model: whisper-1
VOICE_TOOLS_OPENAI_KEY: activa en .env
Usuarios permitidos en TELEGRAM_ALLOWED_USERS: solo Grover
telegram-users.yaml: pendiente de enforcement real
```

## Nota importante

El audio funciona para usuarios que ya están permitidos técnicamente por `TELEGRAM_ALLOWED_USERS`.

Esto no cambia el pendiente principal:

```text
telegram-users.yaml todavía no se aplica técnicamente como barrera real de permisos.
```

Hasta implementar enforcement real, no se deben añadir usuarios no-owner a `TELEGRAM_ALLOWED_USERS`.

## Próximo pendiente relacionado

Implementar enforcement real de permisos leyendo:

```text
mail-manager-lab/config/telegram-users.yaml
```

antes de permitir cualquier acción sobre correo, incluyendo solicitudes enviadas por texto o por audio.
