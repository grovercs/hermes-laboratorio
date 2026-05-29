# Alta de buzón - Administración Vielha Computer

Fecha: 2026-05-29

## Empresa

Vielha Computer

## Buzón

Correo: administracion@vielhacomputer.com
Alias interno Himalaya/ARA: administracion-vielha
Proveedor: IONOS

## Uso previsto

Buzón administrativo para:

    - facturas
    - proveedores
    - bancos
    - gestoría
    - documentación administrativa
    - avisos de servicios contratados

## Estado final

Cuenta añadida en Himalaya:

    [accounts.administracion-vielha]

Backends configurados:

    IMAP
    SMTP

## Credenciales

La contraseña no se guarda en texto plano.

Se guardó en Windows Credential Manager con estos targets:

    himalaya:administracion-vielha:imap
    himalaya:administracion-vielha:smtp

## Helpers creados

Se crearon helpers específicos para recuperar contraseña desde Windows Credential Manager:

    C:\Users\Usuario\.config\himalaya\get-imap-password-administracion-vielha.ps1
    C:\Users\Usuario\.config\himalaya\get-smtp-password-administracion-vielha.ps1

## Configuración Himalaya

La cuenta se añadió a:

    C:\Users\Usuario\.config\himalaya\config.toml

Bloque añadido:

    [accounts.administracion-vielha]
    email = "administracion@vielhacomputer.com"
    display-name = "Administración - Vielha Computer"

    backend.type = "imap"
    backend.host = "imap.ionos.es"
    backend.port = 993
    backend.encryption.type = "tls"
    backend.login = "administracion@vielhacomputer.com"
    backend.auth.type = "password"
    backend.auth.cmd = "powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:/Users/Usuario/.config/himalaya/get-imap-password-administracion-vielha.ps1"

    message.send.backend.type = "smtp"
    message.send.backend.host = "smtp.ionos.es"
    message.send.backend.port = 587
    message.send.backend.encryption.type = "start-tls"
    message.send.backend.login = "administracion@vielhacomputer.com"
    message.send.backend.auth.type = "password"
    message.send.backend.auth.cmd = "powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:/Users/Usuario/.config/himalaya/get-smtp-password-administracion-vielha.ps1"

    folder.aliases.inbox = "INBOX"
    folder.aliases.sent = "Elementos enviados"
    folder.aliases.trash = "Papelera"

## Backup realizado

Antes de modificar Himalaya se creó backup:

    config.toml.backup-before-administracion-vielha-20260529-170927

## Pruebas realizadas

### Listado de carpetas

Comando:

    himalaya folder list --account administracion-vielha

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

    himalaya envelope list --account administracion-vielha --folder INBOX --page-size 5

Resultado:

    Se listaron 5 cabeceras correctamente.

Conclusión:

    Lectura segura de envelopes/cabeceras OK.
    No se leyeron cuerpos completos.
    No se abrieron adjuntos.
    No se siguieron enlaces.

### Carpeta ARA_Revisar_Basura

Comando:

    himalaya folder add --account administracion-vielha ARA_Revisar_Basura

Resultado:

    Folder ARA_Revisar_Basura successfully created!

Conclusión:

    Carpeta de revisión reversible creada correctamente.

### Prueba SMTP

Comando:

    himalaya message send --account administracion-vielha $msg

Resultado:

    Message successfully sent!

Verificación en enviados:

    himalaya envelope list --account administracion-vielha --folder "Elementos enviados" --page-size 5

Resultado:

    Apareció el correo "Prueba SMTP administracion-vielha" en Elementos enviados.

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
- Usar siempre --account administracion-vielha para este buzón.
- Para correos sospechosos, mover a ARA_Revisar_Basura solo con confirmación explícita.
