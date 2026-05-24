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

## Seguridad

Este registro no debe contener secretos, contraseñas, tokens, contenidos privados de correos ni credenciales.
