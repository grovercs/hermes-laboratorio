# ARA Gateway Telegram - arranque automático en Windows

Propuesta segura para dejar el Gateway de Telegram de ARA arrancando automáticamente al iniciar Windows o al iniciar sesión del usuario `Usuario`.

## 1. Problema actual

Estado actual confirmado:

- El Gateway de Telegram funciona con la ARA principal.
- El Gateway está corriendo manualmente.
- `hermes gateway status` puede mostrar:

```text
Gateway is running
Running manually, not as a system service
```

Riesgo:

- Si se cierra la ventana, la sesión o el proceso manual, Telegram puede dejar de responder.
- Si Windows se reinicia, el Gateway no queda garantizado como arranque automático.
- Si se lanzan varios procesos manuales sin control, puede haber duplicados o comportamiento confuso.

## 2. Solución recomendada

La solución recomendada para el entorno Windows actual es crear una tarea programada de Windows que arranque el Gateway al iniciar sesión del usuario `Usuario`.

Ventajas:

- No requiere modificar el código de Hermes.
- No requiere guardar secretos nuevos.
- Puede usar la configuración principal ya existente.
- Permite arrancar automáticamente al login.
- Es fácil de revisar, pausar o eliminar desde el Programador de tareas.

Importante: esta documentación solo propone el diseño. No se crea la tarea todavía.

## 3. Alternativa futura: servicio Windows real

Como alternativa futura, se podría estudiar instalar el Gateway como servicio Windows real o mediante el mecanismo oficial de Hermes si queda validado en este entorno.

Ventajas posibles:

- Mejor integración con arranque del sistema.
- Gestión más clara de reinicios y recuperación.
- Menor dependencia de una sesión interactiva.

Riesgos o pendientes:

- Requiere más pruebas.
- Puede necesitar permisos de administrador.
- Hay que verificar cómo hereda `HERMES_HOME`.
- Hay que asegurar que no expone ni registra secretos.

## 4. HERMES_HOME correcto

La ARA principal debe usar explícitamente este HOME:

```text
C:\Users\Usuario\AppData\Local\hermes
```

Variable esperada:

```powershell
$env:HERMES_HOME = "C:\Users\Usuario\AppData\Local\hermes"
```

Motivo:

- Evita que Hermes use otro HOME por defecto.
- Asegura que se cargan configuración, sesiones, skills y estado de la ARA principal.
- Evita mezclar ARA principal con `ara-lab` u otras instancias.

## 5. Comando actual validado

Comando base validado para arrancar el Gateway:

```powershell
& "C:\Users\Usuario\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe" gateway run
```

En contexto de Hermes/Git Bash, el equivalente usado de forma segura fue:

```bash
HERMES_HOME='C:/Users/Usuario/AppData/Local/hermes' 'C:/Users/Usuario/AppData/Local/hermes/hermes-agent/venv/Scripts/hermes.exe' gateway run
```

Para una tarea programada de Windows, es preferible usar un script PowerShell claro y explícito.

## 6. Script propuesto: `start-ara-gateway.ps1`

Ruta propuesta del script:

```text
C:\Users\Usuario\AppData\Local\hermes\scripts\start-ara-gateway.ps1
```

Contenido propuesto:

```powershell
$ErrorActionPreference = "Stop"

$env:HERMES_HOME = "C:\Users\Usuario\AppData\Local\hermes"
$HermesExe = "C:\Users\Usuario\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe"

# Evitar duplicados: si el Gateway ya está corriendo, no arrancar otro.
$Status = & $HermesExe gateway status 2>&1
if ($LASTEXITCODE -eq 0 -and ($Status -match "Gateway is running")) {
    Write-Output "ARA Gateway ya está corriendo. No se arranca otro proceso."
    exit 0
}

Write-Output "Arrancando ARA Gateway con HERMES_HOME=$env:HERMES_HOME"
& $HermesExe gateway run
```

Notas:

- El script no contiene tokens ni secretos.
- Define `HERMES_HOME` explícitamente.
- Comprueba estado antes de arrancar para evitar duplicados.
- Mantiene el proceso en primer plano dentro de la tarea programada.

## 7. Tarea programada propuesta

Nombre sugerido:

```text
ARA Gateway Telegram
```

Disparador sugerido:

```text
Al iniciar sesión del usuario Usuario
```

Acción sugerida:

```text
Programa: powershell.exe
Argumentos: -NoProfile -ExecutionPolicy Bypass -File "C:\Users\Usuario\AppData\Local\hermes\scripts\start-ara-gateway.ps1"
```

Opciones recomendadas:

- Ejecutar solo para el usuario `Usuario`.
- Iniciar solo si hay red disponible, si la opción está disponible y resulta estable.
- Registrar salida en log local no versionado si se necesita diagnóstico.
- No guardar credenciales dentro del script.
- No usar rutas relativas.

## 8. Cómo verificar estado

Desde PowerShell:

```powershell
$env:HERMES_HOME = "C:\Users\Usuario\AppData\Local\hermes"
& "C:\Users\Usuario\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe" gateway status
```

Resultado esperado si está activo:

```text
Gateway is running
```

Si indica que corre manualmente o como tarea/servicio, revisar el contexto exacto antes de reiniciar nada.

## 9. Cómo detenerlo

Opciones seguras, de menor a mayor impacto:

1. Si está en una ventana visible, parar con `Ctrl+C` en esa ventana.
2. Si está gestionado por tarea programada, detener la tarea desde el Programador de tareas.
3. Usar el comando oficial de Hermes si está disponible y validado para este entorno:

```powershell
$env:HERMES_HOME = "C:\Users\Usuario\AppData\Local\hermes"
& "C:\Users\Usuario\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe" gateway stop
```

4. Como último recurso, cerrar el proceso concreto tras identificarlo bien.

Precaución: no usar comandos generales como matar todos los `python.exe` o todos los `node.exe` salvo emergencia, porque pueden cerrar otros proyectos o herramientas.

## 10. Riesgos y precauciones

### No duplicar procesos

Antes de arrancar el Gateway, comprobar estado:

```powershell
$env:HERMES_HOME = "C:\Users\Usuario\AppData\Local\hermes"
& "C:\Users\Usuario\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe" gateway status
```

Si ya está corriendo, no arrancar otro proceso.

### No mezclar instancias

Usar siempre:

```text
HERMES_HOME=C:\Users\Usuario\AppData\Local\hermes
```

No usar `C:\proyectos\hermes\instances\ara-lab` para el Gateway de Telegram principal salvo prueba explícita y separada.

### No tocar secretos

No documentar ni copiar:

- tokens de Telegram,
- `.env`,
- `auth.json`,
- claves API,
- credenciales,
- logs con datos privados,
- sesiones privadas.

### Smart App Control

Smart App Control fue desactivado porque bloqueaba `hermes.exe`. Si vuelve a bloquear ejecución, revisar primero política de Windows antes de cambiar configuración de Hermes.

### Logs

Si se añade logging al script, debe apuntar a una ruta local no versionada, por ejemplo:

```text
C:\Users\Usuario\AppData\Local\hermes\logs\ara-gateway-startup.log
```

No subir logs al repositorio.

## 11. Plan de implantación recomendado

Fase 1: documentación

- Mantener esta propuesta en el laboratorio.
- Revisar comandos y rutas.

Fase 2: script controlado

- Crear `start-ara-gateway.ps1` solo cuando Grover lo autorice.
- Probarlo manualmente.
- Verificar que no duplica procesos.

Fase 3: tarea programada

- Crear la tarea programada solo tras validar el script.
- Probar reinicio de sesión.
- Verificar con `gateway status`.
- Probar respuesta por Telegram.

Fase 4: mejora futura

- Evaluar instalación como servicio Windows real si la tarea programada no es suficiente.

## 12. Estado de esta propuesta

Fecha: 2026-05-24

Estado:

- Propuesta documentada.
- No se ha creado script real.
- No se ha creado tarea programada.
- No se ha modificado configuración real.
- No se ha reiniciado el Gateway.
- No se han tocado secretos.
