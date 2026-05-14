# Reinicio y mantenimiento de ARA

Este documento resume qué hacer cuando ARA/Hermes se queda bloqueada, tarda demasiado o necesita una sesión limpia.

## Si ARA se queda bloqueada

1. Espera un poco si está ejecutando una tarea larga.
2. Si no responde o parece congelada, vuelve a la terminal donde está Hermes.
3. Intenta cancelar la operación actual con `Ctrl+C`.
4. Si Hermes vuelve al prompt, puedes seguir trabajando o escribir `/new` para empezar limpio.
5. Si la terminal queda inestable, cierra esa sesión y abre Hermes de nuevo.

## Cómo salir con Ctrl+C

En la terminal donde está ejecutándose Hermes:

```text
Ctrl+C
```

Usa `Ctrl+C` para interrumpir una operación bloqueada o salir de un proceso que no responde.

Si Hermes pregunta o vuelve al prompt, revisa la situación antes de lanzar otra tarea larga.

## Cómo reiniciar ARA desde `C:\proyectos\hermes`

1. Abre PowerShell o Windows Terminal.
2. Entra en el workspace local:

```powershell
cd C:\proyectos\hermes
```

3. Inicia Hermes/ARA:

```powershell
hermes
```

## Cuándo usar `/new`

Usa `/new` cuando quieras empezar una sesión limpia sin arrastrar demasiado contexto anterior.

Casos recomendados:

- La conversación ya es muy larga.
- ARA empieza a responder lento.
- Se ha cambiado de tema o de proyecto.
- Se han hecho cambios de configuración y quieres trabajar con contexto limpio.
- Después de un bloqueo o compactación problemática.

Comando dentro de Hermes:

```text
/new
```

## Si Telegram tarda mucho

Si ARA responde por Telegram pero tarda demasiado:

1. Espera unos minutos si la petición era larga.
2. Envía mensajes más cortos y concretos.
3. Evita pedir muchas acciones en un solo mensaje.
4. Si parece bloqueada, revisa Hermes en la terminal local.
5. Si hace falta, reinicia Hermes o el Gateway.
6. Para tareas grandes, pide primero un plan y luego ejecuta paso a paso.

## Cómo evitar conversaciones demasiado largas

Para reducir bloqueos y compactaciones lentas:

- Usa `/new` al cambiar de proyecto o tema.
- Divide tareas grandes en pasos pequeños.
- Evita mezclar diagnóstico, edición, Git y despliegue en una sola petición.
- Pide resúmenes breves antes de continuar.
- Cierra sesiones antiguas si ya no hacen falta.
- No pegues logs enormes salvo que sean necesarios; mejor pegar solo el error relevante.

## Comandos que usar con cuidado

Estos comandos pueden cerrar procesos importantes de golpe. Úsalos solo si sabes que Hermes, Gateway u otros procesos relacionados se han quedado bloqueados y no hay una forma más limpia de cerrarlos.

```powershell
taskkill /F /IM node.exe
taskkill /F /IM python.exe
```

Precauciones:

- `taskkill /F /IM node.exe` puede cerrar servidores Node, Vite, herramientas de desarrollo o procesos de otros proyectos.
- `taskkill /F /IM python.exe` puede cerrar Hermes, scripts Python, procesos de automatización o herramientas abiertas.
- Antes de usarlos, guarda trabajo pendiente.
- Si no estás seguro, pregunta antes o cierra solo la ventana concreta de la terminal bloqueada.

## No borrar configuración ni credenciales

No borrar, copiar, publicar ni subir a GitHub archivos de configuración o credenciales.

Especial cuidado con:

- `.env`
- `*.env`
- `config.yaml`
- `auth.json`
- tokens
- claves API
- contraseñas
- sesiones privadas
- logs con datos sensibles
- archivos de pairing o autenticación

Regla práctica: si un archivo puede contener secretos, no se muestra ni se sube.

## Ajustes realizados para evitar bloqueos por compactación

Fecha documentada: 2026-05-14

Ajustes realizados:

- `HERMES_STREAM_READ_TIMEOUT=1800` añadido en `.env`.
- `auxiliary.compression.timeout` cambiado de `120` a `600` en `config.yaml`.
- Backups creados en `C:\Users\Usuario\AppData\Local\hermes\backups-config`.
- Recordatorio: reiniciar Hermes después de modificar la configuración para que los cambios se apliquen correctamente.

Motivo:

- Evitar bloqueos cuando la compactación de contexto tarda más de 120 segundos.

Nota de seguridad:

- Este documento no incluye tokens, claves API, IDs privados ni credenciales.
