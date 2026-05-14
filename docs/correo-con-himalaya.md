# Correo con Himalaya CLI y ARA

## Objetivo

Usar Himalaya CLI para revisar correo bajo demanda con ARA, de forma controlada y segura.

## Estado actual

- Scoop instalado.
- Himalaya instalado desde Scoop.
- Versión: `himalaya v1.2.0 +imap +maildir +pgp-commands +smtp +wizard +sendmail`.
- Ruta de instalación: `C:\Users\Usuario\scoop\apps\himalaya\current`.
- Shim: `C:\Users\Usuario\scoop\shims\himalaya`.
- Configuración IMAP de prueba creada localmente para la cuenta `vielhacomputer`.
- La configuración no contiene contraseña en texto plano.
- Script local `get-imap-password.ps1` creado sin secretos para leer la contraseña desde variable temporal.
- No hay SMTP configurado.
- No se han guardado credenciales en el repositorio.

## Reglas de seguridad

- Solo IMAP al principio.
- Nada de SMTP todavía.
- No enviar correos.
- No borrar correos.
- No mover correos.
- No marcar correos como leídos.
- No abrir adjuntos.
- No guardar credenciales en repositorios.
- No leer cuerpos completos salvo autorización explícita.

## Prueba realizada con cuenta `vielhacomputer`

- `himalaya folder list --account vielhacomputer` funcionó.
- Carpetas detectadas:
  - `Borradores`
  - `Elementos enviados`
  - `INBOX`
  - `Papelera`
  - `Spam`
- `himalaya envelope list --account vielhacomputer --folder INBOX --page 1 --page-size 10` funcionó.
- Se listaron 10 cabeceras/envelopes.
- No se leyeron cuerpos de correos.
- No se abrieron adjuntos.
- No se movió ningún correo.
- No se borró ningún correo.
- No se marcó ningún correo como leído.
- No se envió ningún correo.

## Resultado de clasificación inicial

Clasificación hecha solo con cabeceras, sin leer cuerpos ni adjuntos:

- Prioridad alta:
  - Factura de IONOS / 1&1.
- Prioridad media:
  - Boletines de Prostcomputer, por posible interés comercial/proveedor.
- Prioridad baja:
  - Resto de correos: newsletters, informativos o poco importantes.

## Próxima fase pendiente

- Decidir si se autoriza leer cuerpos de correos seleccionados.
- Alternativa segura: seguir trabajando solo con cabeceras/envelopes.
- Si se autoriza lectura de cuerpos, definir antes una regla estricta: leer solo IDs concretos, sin adjuntos, sin mover, sin borrar, sin marcar como leído y sin responder automáticamente.
- Decidir si en fase estable se migra el método de contraseña a Windows Credential Manager.
