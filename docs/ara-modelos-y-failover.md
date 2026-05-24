# ARA — modelos alternativos y plan de failover

Documento de laboratorio. No contiene secretos, API keys ni credenciales.

## 1. Objetivo

Evaluar modelos alternativos como segundo proveedor para ARA y definir un plan de failover para la instancia principal, usando `ara-lab` como entorno seguro de pruebas.

## 2. Contexto de partida

ARA principal funciona con:

- Modelo principal: `gpt-5.5`
- Proveedor: `openai-codex`
- Contexto operativo real: ~272K tokens
- Compresión activa, umbral: 0.75

Problema detectado: no hay proveedor secundario configurado en la instancia principal. Si `openai-codex` falla, ARA se queda sin modelo.

## 3. Entorno de pruebas: ara-lab

`ara-lab` es una instancia independiente de Hermes:

- Ruta: `C:\proyectos\hermes\instances\ara-lab`
- Separada de ARA principal. No comparte config ni secretos.
- Conectada a OpenRouter como proveedor para las pruebas.

Reglas de laboratorio durante todas las pruebas:

- No usar secretos reales de ARA principal.
- No modificar la instancia principal.
- No usar correo real, no usar Telegram real.
- No ejecutar acciones destructivas.
- Pedir confirmación antes de cualquier cambio sensible.

## 4. Modelos probados

### 4.1 Ollama local (máquina remota)

- Versión: Ollama 0.24.0
- Modelo: `qwen2.5-coder:1.5b`
- Latencia: respuesta rápida.
- Valoración: útil solo como auxiliar local para tareas pequeñas.
- Descartado como failover principal por capacidad limitada.

### 4.2 OpenRouter → Qwen

- Modelo: `qwen/qwen3.6-plus`
- Latencia: respuesta rápida.
- Pros: prudente, no inventa, fiable para instrucciones estrictas.
- Contras: redacción algo seca, menos adecuada para tareas comerciales o con tono cercano.

### 4.3 OpenRouter → DeepSeek

- Modelo: `deepseek/deepseek-v4-pro`
- Latencia: respuesta rápida.
- Pros: mejor redacción comercial, tono más natural y humano.
- Contras: puede inventar condiciones si no se le dan reglas estrictas. Con plantilla y reglas explícitas mejora notablemente.

## 5. Comparativa práctica

Prueba realizada: redacción de respuesta comercial simulada para un cliente que pregunta por fibra y línea móvil.

Modelo evaluado: `deepseek/deepseek-v4-pro` en `ara-lab`.

Comportamiento observado:

- Sin reglas estrictas ni plantilla: tendencia a añadir condiciones no confirmadas (ej. decir que la línea móvil no tiene permanencia).
- Con reglas explícitas + plantilla de referencia: respeta los datos, redacta con fluidez, tono natural de empresa local y no inventa.

Conclusión: DeepSeek rinde bien como failover comercial siempre que se use con un prompt bien estructurado y reglas explícitas.

## 6. Decisión recomendada

### 6.1 Instancia principal

Mantener ARA principal con `openai-codex` / `gpt-5.5`. No cambiar de proveedor principal ahora. El modelo actual funciona bien para el uso diario y un cambio sin pruebas exhaustivas es arriesgado.

### 6.2 Failover propuesto

Añadir a la configuración de ARA principal un segundo proveedor por OpenRouter:

- Modelo de failover: `deepseek/deepseek-v4-pro`
- Proveedor: OpenRouter
- Condición: solo se activa si el proveedor principal falla.

### 6.3 Modelos auxiliares

- Qwen (`qwen/qwen3.6-plus`): queda como alternativa prudente para tareas que requieran máxima fidelidad a instrucciones sin improvisación.
- Ollama local (`qwen2.5-coder:1.5b`): queda como auxiliar local, no como fallback principal.

## 7. Plan de aplicación segura

Orden propuesto para ARA principal:

1. Hacer backup completo de la configuración actual de ARA principal.
2. Probar el failover en `ara-lab` durante al menos una sesión completa de trabajo real simulado.
3. Si la prueba es satisfactoria, aplicar el failover en ARA principal.
4. Documentar el cambio en este mismo documento y en el contexto operativo.
5. Mantener siempre un plan de rollback documentado.

## 8. Qué NO hacer

- No cambiar el proveedor principal sin pruebas controladas.
- No copiar secretos de ARA principal a `ara-lab`.
- No aplicar failover en producción sin backup previo.
- No eliminar la configuración actual del proveedor principal.

## 9. Fecha de esta evaluación

2026-05-25 — Pruebas realizadas en `ara-lab` con OpenRouter, sesión de laboratorio supervisada.
