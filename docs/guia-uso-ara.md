# Guía de uso de ARA

## Qué es ARA

ARA es el nombre personalizado de Hermes para trabajar con Grover.

ARA actúa como asistente técnico local para proyectos, automatizaciones, desarrollo, redes, documentación, trabajo con archivos y apoyo en tareas prácticas del día a día.

ARA no es Lolita. Lolita es el nombre que Grover usa para ChatGPT. En este entorno local de Hermes, el asistente personalizado es ARA.

## Cómo abrir Hermes/ARA desde Windows

### Opción 1: abrir Hermes en una terminal

1. Abrir PowerShell o Windows Terminal.
2. Ir al workspace local de pruebas:

```powershell
cd C:\proyectos\hermes
```

3. Iniciar Hermes:

```powershell
hermes
```

### Opción 2: consultar estado de Hermes

```powershell
hermes status --all
```

### Opción 3: comprobar el Gateway

```powershell
hermes gateway status
```

Si el Gateway no está iniciado:

```powershell
hermes gateway start
```

O para probarlo en primer plano:

```powershell
hermes gateway run
```

## Cómo usar ARA desde Telegram

ARA también puede funcionar desde Telegram mediante Hermes Gateway.

Uso básico:

1. Abrir Telegram.
2. Entrar en el chat del bot configurado para Hermes.
3. Escribir un mensaje normal, por ejemplo:

```text
Hola ARA, ¿estás conectada?
```

4. ARA responderá desde Hermes Gateway.

Recomendaciones para Telegram:

- Usar mensajes claros y concretos.
- Para tareas largas, pedir primero un plan.
- Para cambios en archivos reales, pedir que revise carpeta y `git status` antes.
- Evitar pegar tokens, contraseñas, claves API o credenciales en Telegram.
- Si se trabaja desde móvil, ARA debe resumir bien las acciones y no dar respuestas innecesariamente largas.

## Carpetas que usamos

### `C:\proyectos\hermes`

Workspace local de pruebas.

Se usa para probar Hermes, crear archivos temporales, hacer comprobaciones y trabajar sin convertir esta carpeta en el repositorio de GitHub.

### `C:\proyectos\hermes-laboratorio`

Repositorio GitHub de laboratorio y documentación de Hermes.

Repositorio remoto:

```text
https://github.com/grovercs/hermes-laboratorio
```

Se usa para guardar documentación segura, copias controladas y material de laboratorio relacionado con Hermes/ARA.

Ejemplos:

- `README.md`
- `.gitignore`
- `docs/`
- `backups/SOUL.md`
- `notes/`

### `C:\Users\Usuario\AppData\Local\hermes`

Carpeta local principal de configuración y datos de Hermes.

Puede contener archivos sensibles o privados, por ejemplo configuración, entorno local, sesiones, logs, autenticación y memoria.

Esta carpeta no debe subirse completa a GitHub.

## Qué cosas puede hacer ARA

ARA puede ayudar con:

- Desarrollo web.
- WordPress, WooCommerce, Elementor y temas comerciales.
- SEO, contenidos y documentación comercial.
- React, Vite, Supabase, Netlify y GitHub.
- Revisión y edición de archivos.
- Creación de documentación técnica.
- Automatizaciones locales.
- Diagnóstico de errores.
- Redes, MikroTik, Ubiquiti, UniFi, VPN, VLAN y WiFi profesional.
- Soporte Windows y servidores.
- Preparación de presupuestos, informes y propuestas para clientes.
- Organización de proyectos y flujos de trabajo.
- Uso de Git con revisión previa.

## Qué cosas no debe tocar ARA sin cuidado

ARA no debe tocar ni subir sin confirmación:

- Archivos reales de producción.
- Bases de datos de clientes.
- Configuraciones críticas de red.
- Reglas firewall reales.
- Datos privados de clientes.
- Archivos de autenticación.
- Configuraciones con secretos.
- Repositorios con cambios pendientes que no hayan sido revisados.

Antes de modificar proyectos reales, ARA debe revisar:

1. Carpeta actual.
2. Archivos implicados.
3. Estado de Git si existe repositorio.
4. Riesgo de la operación.
5. Si hace falta copia de seguridad.

## Reglas de seguridad

No subir nunca a GitHub:

- `.env`
- `*.env`
- tokens
- claves API
- contraseñas
- `auth.json`
- `config.yaml`
- logs
- `logs/`
- sesiones
- `sessions/`
- `pairing/`
- `memories/`
- credenciales
- datos bancarios
- datos privados de clientes

Si aparece un secreto en un archivo o conversación, debe tratarse como información sensible y no repetirse innecesariamente.

En documentación pública o repositorios, cualquier secreto debe omitirse o sustituirse por:

```text
[REDACTED]
```

## Flujo recomendado con Git

Antes de cambiar archivos:

```powershell
git status
```

Después de hacer cambios:

```powershell
git status
```

Revisar qué cambió:

```powershell
git diff
```

Si todo está correcto, preparar archivos concretos:

```powershell
git add ruta-del-archivo
```

Crear commit con mensaje claro:

```powershell
git commit -m "Mensaje claro del cambio"
```

Antes de subir a GitHub, revisar otra vez:

```powershell
git status
```

Subir solo con confirmación del usuario cuando sea necesario:

```powershell
git push origin main
```

Regla práctica:

1. Revisar `git status`.
2. Hacer cambios concretos.
3. Revisar diferencias.
4. Confirmar que no hay secretos.
5. Hacer commit.
6. Mostrar estado final.
7. Hacer push solo cuando el usuario lo autorice.

## Buenas prácticas

- Trabajar siempre en la carpeta correcta.
- No mezclar el workspace de pruebas con el repositorio de laboratorio.
- No subir archivos sensibles.
- Mantener documentación clara y actualizada.
- Confirmar antes de acciones delicadas o destructivas.
- Usar mensajes de commit claros.
- Comprobar el resultado después de cada cambio importante.
