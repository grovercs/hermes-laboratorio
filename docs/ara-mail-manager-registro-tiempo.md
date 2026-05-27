# ARA Mail Manager - Registro de tiempo

Registro de tiempo dedicado al diseño y creación de ARA Mail Manager.

## 2026-05-24

- Proyecto: ARA Mail Manager
- Objetivo general: crear una secretaria digital multi-buzón, supervisada por Grover, capaz de revisar correos, proponer respuestas en su estilo, aprender de correcciones y ser replicable para clientes.
- Estado inicial: diseño del sistema multi-buzón supervisado.
- Pendiente: definir arquitectura, scripts, permisos, flujo de aprendizaje de estilo y replicabilidad para clientes.
- Horas: pendiente de completar al cierre de la sesión
- Validación real por Telegram: se confirmó el flujo supervisado con Gateway activo para `info@vielhacomputer.com`: triage por cabeceras, preview autorizado de IDs concretos, propuesta de acción reversible, confirmación explícita y movimiento verificado a `ARA_Revisar_Basura`.
- Horas de esta validación: pendiente de cierre
- Validación SMTP completa: se configuró SMTP para `info@vielhacomputer.com` con IONOS, helper SMTP y credencial separada en Windows Credential Manager; tras corregir `folder.aliases.sent = "Elementos enviados"`, la segunda prueba terminó con `Message successfully sent!`, `SEND_EXIT_CODE=0`, llegada confirmada a `grovercs@gmail.com` y copia guardada en `Elementos enviados` con ID `32`.
- Horas de esta validación SMTP: pendiente de cierre

## 2026-05-25

- Proyecto: ARA Mail Manager / infraestructura ARA.
- Objetivo: probar modelos alternativos en `ara-lab` con OpenRouter y documentar la decisión de failover para ARA principal.
- Modelos probados:
  - Ollama local: `qwen2.5-coder:1.5b` — respuesta rápida, útil solo como auxiliar local, descartado como failover principal.
  - OpenRouter → Qwen: `qwen/qwen3.6-plus` — prudente y fiable, redacción algo seca.
  - OpenRouter → DeepSeek: `deepseek/deepseek-v4-pro` — mejor redacción comercial, requiere reglas estrictas para no inventar condiciones.
- Prueba práctica: redacción de respuesta comercial simulada (consulta de fibra y línea móvil). DeepSeek con plantilla y reglas explícitas rindió bien.
- Decisión: mantener `openai-codex`/`gpt-5.5` como proveedor principal en ARA; proponer `deepseek/deepseek-v4-pro` vía OpenRouter como failover; Qwen como alternativa prudente; Ollama como auxiliar local.
- Documento generado: `docs/ara-modelos-y-failover.md`.
- Contexto operativo actualizado con referencia al nuevo documento.
- Horas: pendiente de completar al cierre de la sesión

## 2026-05-27

- Proyecto: ARA Mail Manager / ARA principal.
- Objetivo: documentar incidente y resolución de Hermes/ARA principal tras el error `TypeError: 'NoneType' object is not iterable` con `openai-codex` / `gpt-5.5`.
- Estado inicial: el modelo llegaba a responder, pero Hermes terminaba mostrando error al finalizar la respuesta.
- Diagnóstico documentado: `openai-codex` tenía 2 credenciales; la credencial antigua `#1` estaba invalidada con `token_invalidated` / `401` y se eliminó, quedando solo `openai-codex-oauth-2`.
- Configuración verificada: `model.default: gpt-5.5`, `provider: openai-codex`, `context_length: 272000`, `fallback_providers: []`.
- `hermes doctor` detectó configuración antigua `v23`; se creó backup previo en `C:\Users\Usuario\AppData\Local\hermes\config.yaml.backup-before-doctor-fix-20260527-162018`.
- Acción aplicada fuera de este modo documentación: `hermes doctor --fix`, con migración correcta `v23` → `v24`.
- Validación posterior: la prueba `Responde solo: OK` respondió limpio sin error, y una segunda prueba confirmó funcionamiento normal de ARA principal tras la migración.
- Seguridad de esta sesión documental: no se tocó configuración real, no se modificó `.env`, no se abrieron correos, no se enviaron correos, no se hizo commit ni push.
- Horas: pendiente de completar al cierre de la sesión.

## Seguridad

Este registro no debe contener secretos, contraseñas, tokens, contenidos privados de correos ni credenciales.
