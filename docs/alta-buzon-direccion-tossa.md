# Alta de buzón - Dirección Alojamientos Tossa de Mar

Fecha: 2026-05-29

## Empresa

Alojamientos Tossa de Mar

## Buzón

Correo: direccion@alojamientostossademar.com
Alias interno Himalaya/ARA: direccion-tossa
Proveedor: IONOS

## Uso previsto

Buzón institucional para:

    - VisitTossa
    - Ayuntamiento
    - Turismo
    - Federaciones
    - Asociaciones
    - Trámites oficiales
    - Gestiones administrativas de dirección

## Estado final

Cuenta añadida en Himalaya:

    [accounts.direccion-tossa]

Backends configurados:

    IMAP
    SMTP

## Credenciales

La contraseña no se guarda en texto plano.

Se guardó en Windows Credential Manager con estos targets:

    himalaya:direccion-tossa:imap
    himalaya:direccion-tossa:smtp

## Helpers creados

Se crearon helpers específicos para recuperar contraseña desde Windows Credential Manager:

    C:\Users\Usuario\.config\himalaya\get-imap-password-direccion-tossa.ps1
    C:\Users\Usuario\.config\himalaya\get-smtp-password-direccion-tossa.ps1

## Configuración Himalaya

La cuenta se añadió a:

    C:\Users\Usuario\.config\himalaya\config.toml

Bloque añadido:

    [accounts.direccion-tossa]
    email = "direccion@alojamientostossademar.com"
    display-name = "Dirección - Alojamientos Tossa de Mar"

    backend.type = "imap"
    backend.host = "imap.ionos.es"
    backend.port = 993
    backend.encryption.type = "tls"
    backend.login = "direccion@alojamientostossademar.com"
    backend.auth.type = "password"
    backend.auth.cmd = "powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:/Users/Usuario/.config/himalaya/get-imap-password-direccion-tossa.ps1"

    message.send.backend.type = "smtp"
    message.send.backend.host = "smtp.ionos.es"
    message.send.backend.port = 587
    message.send.backend.encryption.type = "start-tls"
    message.send.backend.login = "direccion@alojamientostossademar.com"
    message.send.backend.auth.type = "password"
    message.send.backend.auth.cmd = "powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:/Users/Usuario/.config/himalaya/get-smtp-password-direccion-tossa.ps1"

    folder.aliases.inbox = "INBOX"
    folder.aliases.sent = "Elementos enviados"

## Backup realizado

Antes de modificar Himalaya se creó backup:

    config.toml.backup-before-direccion-tossa-20260529-124308

## Pruebas realizadas

### Listado de carpetas

Comando:

    himalaya folder list --account direccion-tossa

Resultado:

    Borradores
    Elementos enviados
    INBOX
    Papelera
    Spam

Conclusión:

    IMAP OK

### Listado seguro de cabeceras

Comando:

    himalaya envelope list --account direccion-tossa --folder INBOX --page-size 5

Resultado:

    Se listó correctamente la cabecera del correo inicial de IONOS.

Conclusión:

    Lectura segura de envelopes/cabeceras OK.
    No se leyó cuerpo completo.
    No se abrieron adjuntos.
    No se siguieron enlaces.

### Prueba SMTP

Primer intento:

    Se intentó enviar un raw message con cabecera Date generada manualmente desde PowerShell.

Resultado:

    IONOS rechazó el mensaje con error 554 policy restrictions.

Conclusión:

    No usar cabecera Date manual generada desde PowerShell en pruebas raw.

Segundo intento:

    Se envió raw message sin cabecera Date manual.

Resultado:

    Message successfully sent!

Verificación en enviados:

    himalaya envelope list --account direccion-tossa --folder "Elementos enviados" --page-size 5

Resultado:

    Apareció el correo "Prueba SMTP direccion-tossa sin Date" en Elementos enviados.

Conclusión:

    SMTP OK.
    Copia en enviados OK.

Nota:

    El mensaje de prueba apareció con fecha 1970-01-01 porque el raw message usado para la prueba manual no incluía cabecera Date.
    Para futuros envíos manuales raw conviene evitar Date manual mal formada o usar flujos nativos de redacción/respuesta que generen cabeceras completas.

## Reglas de seguridad

- No enviar correos sin confirmación explícita.
- No borrar definitivamente.
- No abrir adjuntos.
- No seguir enlaces.
- No leer cuerpos salvo instrucción concreta.
- Usar siempre --account direccion-tossa para este buzón.

## Regla operativa

Para trámites oficiales o institucionales, ARA debe recomendar usar direccion-tossa o poner dirección en copia antes de enviar desde reservas-tossa.
