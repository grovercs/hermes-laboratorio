# Protocolo de trabajo seguro para proyectos reales

Este documento define el protocolo obligatorio que ARA debe seguir antes de tocar proyectos reales de Grover.

El objetivo es evitar pérdidas de trabajo, subidas accidentales de secretos, cambios destructivos o modificaciones en la carpeta equivocada.

## 1. Confirmar carpeta actual

Antes de modificar cualquier archivo, confirmar siempre la carpeta de trabajo.

En Windows/PowerShell, el usuario puede comprobarlo con:

```powershell
pwd
```

ARA debe asegurarse de estar dentro del proyecto correcto antes de escribir, borrar, copiar o ejecutar comandos.

Si la carpeta no coincide con el proyecto indicado, debe parar y pedir confirmación.

## 2. Ejecutar `git status`

Si el proyecto usa Git, ejecutar siempre:

```powershell
git status
```

Antes de tocar archivos, revisar:

- Rama actual.
- Cambios pendientes.
- Archivos modificados por el usuario.
- Archivos sin seguimiento.
- Si la rama está sincronizada con el remoto.

Si hay cambios previos que no son de ARA, no sobrescribirlos sin confirmación.

## 3. No tocar archivos sensibles

ARA no debe tocar, copiar, mostrar, subir ni modificar sin una razón clara y confirmación explícita:

- `.env`
- `*.env`
- `auth.json`
- `config.yaml`
- tokens
- claves API
- contraseñas
- credenciales
- datos bancarios
- datos privados de clientes
- logs con información sensible
- sesiones
- archivos de autenticación

Regla práctica:

Si un archivo puede contener secretos, no debe subirse a GitHub.

## 4. Hacer copia si no hay Git

Si el proyecto no tiene Git o no está claro que exista control de versiones, hacer o recomendar una copia antes de modificar archivos importantes.

Opciones:

- Copiar el archivo antes de editarlo.
- Copiar la carpeta del proyecto.
- Exportar base de datos si aplica.
- Crear backup desde el panel correspondiente si es WordPress u otra plataforma.

No hacer cambios destructivos en proyectos sin copia o control de versiones.

## 5. Explicar qué archivos se van a modificar

Antes de tocar archivos reales, ARA debe decir claramente:

- Qué archivo va a modificar.
- Qué parte o bloque va a cambiar.
- Qué objetivo tiene el cambio.
- Qué riesgo puede tener.
- Cómo se va a comprobar después.

Ejemplo:

```text
Voy a modificar src/App.jsx para ajustar el módulo de incidencias.
Después ejecutaré npm run build para comprobar que compila.
No tocaré .env ni configuración sensible.
```

## 6. Hacer cambios pequeños

Los cambios deben hacerse en bloques pequeños y controlados.

Evitar:

- Reescrituras grandes sin necesidad.
- Cambios masivos en muchos archivos a la vez.
- Reformateos innecesarios.
- Mezclar varias tareas distintas en el mismo cambio.

Preferir:

- Un objetivo claro por cambio.
- Pocos archivos modificados.
- Explicación breve de cada cambio.
- Verificación inmediata.

## 7. Probar build o tests si existen

Después de modificar código, ejecutar las pruebas adecuadas si existen.

Ejemplos:

```powershell
npm run build
```

```powershell
npm test
```

```powershell
python -m pytest
```

Si no hay tests o build definido, ARA debe indicarlo claramente y proponer una comprobación manual.

## 8. Mostrar `git diff` antes de commit

Antes de preparar un commit, revisar los cambios.

```powershell
git diff
```

También puede revisarse un resumen:

```powershell
git diff --stat
```

ARA debe confirmar que:

- Solo cambiaron los archivos esperados.
- No aparecen secretos.
- No se tocaron archivos sensibles.
- El cambio coincide con lo pedido.

## 9. Hacer commit solo con confirmación

ARA no debe hacer commit en proyectos reales si el usuario pidió confirmación previa o si la tarea es delicada.

Antes del commit, mostrar:

```powershell
git status
```

Y explicar qué se va a incluir.

Comando típico:

```powershell
git add ruta-del-archivo
```

```powershell
git commit -m "Mensaje claro del cambio"
```

El mensaje de commit debe ser claro y concreto.

## 10. Hacer push solo con confirmación

Subir a GitHub, Netlify, producción o cualquier remoto puede tener efectos reales.

Antes de hacer push, ARA debe:

1. Mostrar `git status`.
2. Confirmar la rama.
3. Confirmar el remoto.
4. Confirmar que no hay secretos.
5. Esperar autorización si el usuario la pidió o si el cambio afecta a producción.

Comando típico:

```powershell
git push origin main
```

## 11. Si hay errores, parar y explicar

Si aparece un error en cualquier paso, ARA debe parar y explicar:

- Qué ha ocurrido.
- Por qué puede estar pasando.
- Qué se ha modificado hasta ese momento.
- Qué queda pendiente.
- Cuál es el siguiente paso seguro.

No continuar encadenando comandos si el estado no está claro.

## Resumen rápido obligatorio

Antes de tocar proyectos reales:

1. Confirmar carpeta actual.
2. Ejecutar `git status`.
3. Revisar que no haya cambios del usuario sin proteger.
4. No tocar archivos sensibles.
5. Hacer backup si no hay Git.
6. Explicar qué archivos se van a modificar.
7. Hacer cambios pequeños.
8. Probar build o tests si existen.
9. Mostrar `git diff` antes de commit.
10. Hacer commit solo con confirmación.
11. Hacer push solo con confirmación.
12. Si hay errores, parar y explicar.
