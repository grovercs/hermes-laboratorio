# Arquitectura para instancias Hermes separadas

## Objetivo

Este documento describe una arquitectura limpia para preparar varias instancias Hermes separadas, como "contenedores lógicos", sin tocar todavía la instalación real actual.

La idea principal es separar:

- Motor / binarios compartidos de Hermes.
- Datos, configuración, memoria, sesiones, skills, logs y credenciales de cada instancia.

Hermes soporta esta separación usando la variable de entorno `HERMES_HOME`.

## Estado actual

La instancia principal actual de ARA usa como HOME real de Hermes:

```text
C:\Users\Usuario\AppData\Local\hermes
```

El ejecutable compartido actual está en:

```text
C:\Users\Usuario\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe
```

Esta instalación actual mezcla en una misma raíz:

- Código y entorno de ejecución de Hermes.
- Configuración.
- Datos.
- Skills.
- Memoria.
- Sesiones.
- Logs.
- Credenciales.

Por seguridad, no conviene mover esta instalación todavía.

## HERMES_HOME

Hermes usa `HERMES_HOME` como ruta principal para localizar datos y configuración de una instancia.

Si `HERMES_HOME` apunta a una carpeta concreta, Hermes debe usar esa carpeta como HOME de la instancia.

Ejemplo conceptual:

```text
HERMES_HOME=C:\proyectos\hermes\instances\ara-lab
```

Entonces esa instancia debería usar sus propios archivos y carpetas bajo:

```text
C:\proyectos\hermes\instances\ara-lab
```

Si `HERMES_HOME` no está definido, Hermes puede usar el valor por defecto del usuario, normalmente equivalente a `~\.hermes`.

## Contenedores lógicos

La arquitectura propuesta consiste en usar el mismo motor Hermes, pero distintos `HERMES_HOME`.

Conceptualmente:

```text
Motor compartido:
C:\Users\Usuario\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe

Instancia ara-lab:
HERMES_HOME=C:\proyectos\hermes\instances\ara-lab

Instancia ara-correo:
HERMES_HOME=C:\proyectos\hermes\instances\ara-correo

Instancia ara-sistemas:
HERMES_HOME=C:\proyectos\hermes\instances\ara-sistemas

Instancia ara-main futura:
HERMES_HOME=C:\proyectos\hermes\instances\ara-main
```

Así cada instancia queda separada lógicamente, aunque todas llamen al mismo ejecutable.

## Estructura propuesta

Raíz propuesta:

```text
C:\proyectos\hermes\instances\
```

Instancias previstas:

```text
C:\proyectos\hermes\instances\ara-lab
C:\proyectos\hermes\instances\ara-correo
C:\proyectos\hermes\instances\ara-sistemas
C:\proyectos\hermes\instances\ara-main
```

Uso recomendado de cada una:

### ara-lab

Instancia de laboratorio.

Uso recomendado:

- Probar cambios.
- Probar Desktop/API Server.
- Probar configuraciones nuevas.
- Probar skills sin afectar ARA principal.
- Empezar sin secretos reales.

Esta debe ser la primera instancia nueva a crear.

### ara-correo

Instancia especializada en correo y triage.

Uso recomendado:

- Lectura controlada de correo.
- Reglas estrictas de seguridad.
- Sin SMTP salvo autorización explícita.
- Sin mover, borrar, marcar ni responder correos salvo orden concreta.

### ara-sistemas

Instancia para sistemas, redes, mantenimiento y soporte técnico.

Uso recomendado:

- Diagnóstico técnico.
- Documentación de redes/sistemas.
- Scripts y operaciones controladas.
- Aprobaciones manuales para acciones delicadas.

### ara-main

Instancia principal futura.

Recomendación actual:

- No migrarla todavía.
- Mantener de momento la instancia real actual en `C:\Users\Usuario\AppData\Local\hermes`.
- Valorar migrarla solo al final, cuando `ara-lab` haya demostrado que la arquitectura funciona.

## Archivos y carpetas propios de cada instancia

Cada instancia debe tener sus propios datos y configuración.

No se deben compartir sin plan:

```text
config.yaml
.env
auth.json
SOUL.md
skills\
sessions\
memories\
logs\
cron\
state.db
```

También pueden existir carpetas y archivos auxiliares por instancia, por ejemplo:

```text
cache\
pastes\
hooks\
pairing\
backups-config\
channel_directory.json
gateway_state.json
kanban.db
processes.json
```

Los archivos sensibles como `.env` y `auth.json` no deben copiarse entre instancias sin una revisión explícita y un motivo claro.

## Recursos que no deben compartirse sin plan

Cada instancia debe tener aislamiento no solo de archivos, sino también de recursos externos.

No se deben compartir sin diseño previo:

- Puertos locales.
- API Server de Hermes.
- Dashboard.
- Gateway.
- Telegram bot.
- Canales Telegram autorizados.
- Credenciales de proveedores LLM.
- Tokens OAuth.
- Claves API.
- Credenciales de correo.
- Cron jobs.
- Bases de datos de sesión o memoria.

Ejemplo de riesgo:

Si dos instancias intentan usar el mismo puerto de API Server o el mismo Telegram bot, pueden pisarse, responder desde la instancia incorrecta o mezclar sesiones.

## Riesgos de mover AppData ahora

No se recomienda mover todavía:

```text
C:\Users\Usuario\AppData\Local\hermes
```

Riesgos principales:

1. Es la instalación real actual de ARA.
2. Contiene el entorno de ejecución y el `venv` de Hermes.
3. Puede tener procesos activos asociados.
4. Contiene configuración real.
5. Contiene memoria, sesiones y estado actual.
6. Contiene `.env` y `auth.json`, que son sensibles.
7. Puede contener locks, PIDs, bases SQLite y archivos WAL/SHM en uso.
8. Copiar bases de datos con procesos activos puede dejar copias inconsistentes.
9. Cambiar rutas puede romper wrappers, gateway, dashboard o integraciones existentes.
10. Si `HERMES_HOME` no se propaga correctamente, un subproceso podría escribir en otra carpeta por error.

Conclusión:

La instalación actual debe tratarse como `ara-main actual` hasta tener una alternativa probada.

## Migración segura por fases

### Fase 1: Documentar

Crear y mantener esta documentación.

Objetivo:

- Dejar clara la arquitectura.
- Evitar cambios impulsivos sobre la instalación real.
- Tener una guía para futuras pruebas.

### Fase 2: Crear `ara-lab` vacío

Cuando se autorice explícitamente, crear solo:

```text
C:\proyectos\hermes\instances\ara-lab
```

Recomendaciones:

- No copiar `.env`.
- No copiar `auth.json`.
- No copiar sesiones.
- No copiar memoria real.
- No copiar bases de datos activas.
- Empezar como instancia limpia.

### Fase 3: Probar `HERMES_HOME`

Probar que Hermes puede arrancar usando:

```text
HERMES_HOME=C:\proyectos\hermes\instances\ara-lab
```

Verificar que los archivos nuevos se crean dentro de `ara-lab` y no en la instalación principal.

Comprobaciones futuras posibles:

```text
hermes config path
hermes config env-path
hermes status
```

Siempre usando el `HERMES_HOME` de `ara-lab`.

### Fase 4: Probar API Server/Desktop contra `ara-lab`

Solo después de verificar `ara-lab`:

- Probar API Server en puerto propio.
- Probar Hermes Desktop contra `ara-lab`, no contra ARA principal.
- Evitar credenciales reales al principio.
- Verificar logs, sesiones y cambios generados.

Si se usan puertos, asignarlos con cuidado para evitar conflicto con otras instancias.

### Fase 5: Crear `ara-correo` y `ara-sistemas`

Cuando `ara-lab` funcione correctamente:

- Crear `ara-correo` con configuración mínima y segura.
- Crear `ara-sistemas` con configuración orientada a soporte/sistemas.
- Mantener credenciales y permisos separados.
- Documentar diferencias entre instancias.

### Fase 6: Valorar migrar `ara-main`

Solo al final.

Condiciones previas recomendadas:

- `ara-lab` funciona.
- Se entiende bien cómo se propaga `HERMES_HOME`.
- Hay plan de backup.
- No hay procesos escribiendo en la instalación actual.
- Se sabe cómo volver atrás.
- Se han revisado gateway, dashboard, Telegram y cron.

Opción conservadora recomendada:

Mantener `C:\Users\Usuario\AppData\Local\hermes` como ARA principal actual y usar `C:\proyectos\hermes\instances\` solo para instancias nuevas.

## Recomendación actual

No mover la instalación actual.

Primer paso futuro recomendado:

Crear únicamente `ara-lab` vacío y probar `HERMES_HOME` sin secretos reales.

Hasta que esa prueba sea estable, la instancia principal debe seguir siendo:

```text
C:\Users\Usuario\AppData\Local\hermes
```

## Estado de seguridad de este documento

Este documento no contiene:

- Tokens.
- Claves API.
- Contraseñas.
- Contenido de `.env`.
- Contenido de `auth.json`.
- Credenciales de correo.
- Datos privados de clientes.

Solo describe rutas, arquitectura y fases de migración.
