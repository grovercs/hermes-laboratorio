# ARA Mail Manager — contexto operativo corto

Este documento sirve como contexto operativo breve para retomar trabajo de ARA Mail Manager sin depender de conversaciones largas ni compactaciones extensas.

## 1. Estado actual del proyecto

- Proyecto en fase de laboratorio/documentación operativa.
- ARA Mail Manager está planteado como asistente supervisado para clasificar, resumir y preparar trabajo sobre correo.
- El modo seguro de correo está documentado como comportamiento por defecto.
- El flujo real por Telegram ya fue probado con Himalaya sobre el buzón `info@vielhacomputer.com`.
- Las acciones con impacto externo siguen requiriendo confirmación explícita de Grover.
- Este repositorio (`hermes-laboratorio`) se usa como espacio seguro de documentación y respaldo operativo, sin secretos.

## 2. Rutas importantes

- ARA principal `HERMES_HOME`: `C:\Users\Usuario\AppData\Local\hermes`
- Hermes Agent: `C:\Users\Usuario\AppData\Local\hermes\hermes-agent`
- Repo laboratorio: `C:\proyectos\hermes-laboratorio`
- ARA Lab: `C:\proyectos\hermes\instances\ara-lab`

## 3. Arranque principal

Desde PowerShell:

```powershell
$env:HERMES_HOME = "C:\Users\Usuario\AppData\Local\hermes"
& "C:\Users\Usuario\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe"
```

## 4. Buzón actual probado

- Buzón: `info@vielhacomputer.com`
- Cuenta Himalaya: `vielhacomputer`
- Uso actual: IMAP / lectura, triage seguro y SMTP validado bajo supervisión.

## 5. Credential Manager + Himalaya

- Target en Windows Credential Manager: `himalaya:info@vielhacomputer.com`
- Helper local: `C:\Users\Usuario\.config\himalaya\get-imap-password.ps1`
- En la config de Himalaya se usa ruta con barras `/` para compatibilidad:
  - `C:/Users/Usuario/.config/himalaya/get-imap-password.ps1`
- No guardar contraseñas en texto plano en documentación, Git ni `config.toml`.

## 6. Reglas permanentes

Modo seguro de correo por defecto:

- No borrar definitivamente correos.
- No marcar correos como leídos/no leídos.
- No abrir adjuntos.
- No seguir enlaces.
- No responder ni enviar correos sin confirmación explícita.
- No mover correos sin confirmación explícita.
- No crear reglas automáticas sin confirmación explícita.
- No configurar ni usar SMTP/salida de correo sin confirmación explícita.
- Si Grover dice “borrar”, interpretar primero como propuesta reversible: mover a carpeta de revisión, no eliminar definitivamente.

## 7. Formato Telegram

Para triage de correo por Telegram:

- Formato móvil.
- Respuesta corta y accionable.
- Resumen primero.
- Usar emojis simples como separadores visuales.
- Máximo top 5 prioridades salvo que Grover pida detalle.
- Indicar siempre qué se revisó y qué no se tocó:
  - 📬 buzón
  - 🔎 revisados
  - 📖 cuerpos leídos
  - 📎 adjuntos
  - 🔗 enlaces
  - ⚙️ acciones
  - 🧭 resumen
  - 📊 categorías
  - 🎯 top prioridades
  - 👉 siguiente pregunta

## 8. Flujo real validado por Telegram

Flujo validado:

1. Listar cabeceras/envelopes de los últimos 20 correos del INBOX.
2. Clasificar sin leer cuerpos, sin abrir adjuntos y sin seguir enlaces.
3. Leer en preview solo IDs concretos autorizados por Grover.
4. Proponer acción reversible cuando hay phishing claro.
5. Ejecutar movimiento solo con confirmación explícita.
6. Verificar origen y destino después de la acción.

Caso validado:

- Se revisaron cabeceras de los últimos 20 correos.
- Se hizo preview seguro de IDs concretos autorizados.
- Se movieron los IDs `22448` y `22455` a `ARA_Revisar_Basura` con confirmación explícita.
- Verificación posterior en destino:
  - nuevo ID `3`: correo que antes era `22448`.
  - nuevo ID `4`: correo que antes era `22455`.

## 9. Flujo SMTP validado

Fecha: 2026-05-24

Se validó SMTP completo para el buzón `info@vielhacomputer.com` usando Himalaya e IONOS, siempre bajo confirmación explícita de Grover.

Resumen del hito:

- SMTP quedó configurado en Himalaya para la cuenta `vielhacomputer`.
- Se creó helper SMTP local sin secreto embebido.
- Se creó credencial separada en Windows Credential Manager para SMTP: `himalaya:info@vielhacomputer.com:smtp`.
- Primera prueba controlada: el correo llegó a `grovercs@gmail.com`, confirmando que SMTP funcionaba.
- La primera prueba falló al guardar copia en enviados porque faltaba alias de carpeta `sent`.
- Se corrigió añadiendo en `config.toml`:

```toml
folder.aliases.sent = "Elementos enviados"
```

- Segunda prueba controlada:
  - asunto: `Prueba ARA Mail Manager SMTP - enviados OK`
  - resultado: `Message successfully sent!`
  - código: `SEND_EXIT_CODE=0`
  - el correo llegó a `grovercs@gmail.com`
  - Himalaya guardó copia en `Elementos enviados` con ID `32`.

Límites respetados:

- No se respondieron correos reales.
- No se abrieron adjuntos.
- No se siguieron enlaces.
- No se mostraron secretos.
- Los envíos fueron pruebas controladas y confirmadas explícitamente.

## 10. Pendientes técnicos

Continuación documentada en `docs/ara-mail-manager-siguiente-fase.md`.

- No hay conexión/proveedor secundario validado.
- No hay selección automática de modelo según dificultad.
- Investigar modelos de mayor contexto en `ara-lab`.
- Investigar fallback de proveedor/modelo.
- Investigar configuración de compresión/contexto.

## 11. Regla de rendimiento

- Usar Telegram para tareas cortas, decisiones rápidas y triage operativo.
- Usar consola para documentación, Git y cambios de repo.
- Si una tarea tarda más de 90 segundos, dividirla en partes más pequeñas.
- Para tareas largas, crear documentos operativos cortos y reutilizables en `docs/`.
