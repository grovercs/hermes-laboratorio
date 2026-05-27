# Alta de buzón - Hotel L'Hostalet de Tossa

Fecha: 2026-05-27

## Empresa

Hotel L'Hostalet de Tossa

## Buzón

Correo: reservas@alojamientostossademar.com
Alias interno Himalaya/ARA: reservas-tossa
Proveedor: IONOS

## Objetivo

Añadir el buzón de reservas de Hotel L'Hostalet de Tossa al sistema ARA Mail Manager como segunda cuenta gestionable, sin modificar ni romper la cuenta existente de Vielha Computer.

## Estado final

Cuenta añadida en Himalaya:

    [accounts.reservas-tossa]

Backends configurados:

    IMAP
    SMTP

Cuenta por defecto mantenida:

    vielhacomputer

## Credenciales

La contraseña no se guarda en texto plano.

Se guardó en Windows Credential Manager con estos targets:

    himalaya:reservas-tossa:imap
    himalaya:reservas-tossa:smtp

También existieron/copias previas con el email completo:

    himalaya:reservas@alojamientostossademar.com:imap
    himalaya:reservas@alojamientostossademar.com:smtp

## Helpers creados

Se crearon helpers específicos para recuperar contraseña desde Windows Credential Manager:

    C:\Users\Usuario\.config\himalaya\get-imap-password-reservas-tossa.ps1
    C:\Users\Usuario\.config\himalaya\get-smtp-password-reservas-tossa.ps1

## Configuración Himalaya

La cuenta se añadió a:

    C:\Users\Usuario\.config\himalaya\config.toml

Bloque añadido:

    [accounts.reservas-tossa]
    email = "reservas@alojamientostossademar.com"
    display-name = "Hotel L'Hostalet de Tossa - Reservas"

    backend.type = "imap"
    backend.host = "imap.ionos.es"
    backend.port = 993
    backend.encryption.type = "tls"
    backend.login = "reservas@alojamientostossademar.com"
    backend.auth.type = "password"
    backend.auth.cmd = "powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:/Users/Usuario/.config/himalaya/get-imap-password-reservas-tossa.ps1"

    message.send.backend.type = "smtp"
    message.send.backend.host = "smtp.ionos.es"
    message.send.backend.port = 587
    message.send.backend.encryption.type = "start-tls"
    message.send.backend.login = "reservas@alojamientostossademar.com"
    message.send.backend.auth.type = "password"
    message.send.backend.auth.cmd = "powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:/Users/Usuario/.config/himalaya/get-smtp-password-reservas-tossa.ps1"

    folder.aliases.inbox = "INBOX"
    folder.aliases.sent = "Elementos enviados"

## Backup realizado

Antes de modificar Himalaya se creó backup:

    config.toml.backup-before-reservas-tossa-20260527-182053

## Pruebas realizadas

### Listado de carpetas

Comando:

    himalaya folder list --account reservas-tossa

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

    himalaya envelope list --account reservas-tossa --folder INBOX --page-size 5

Resultado:

    Se listaron 5 cabeceras del INBOX correctamente.

Conclusión:

    Lectura segura de envelopes/cabeceras OK.
    No se leyeron cuerpos completos.
    No se abrieron adjuntos.
    No se siguieron enlaces.
    No se envió ningún correo.

### Listado de cuentas

Comando:

    himalaya account list

Resultado:

    reservas-tossa: IMAP, SMTP
    vielhacomputer: IMAP, SMTP, default yes

Conclusión:

    reservas-tossa quedó configurada como segunda cuenta.
    vielhacomputer sigue siendo la cuenta por defecto.

## Pendiente

- Probar SMTP con un correo de prueba controlado.
- Crear carpeta ARA_Revisar_Basura en reservas-tossa si no existe.
- Probar con ARA/Gateway una instrucción mínima para listar cabeceras usando reservas-tossa.
- Documentar protocolo multi-buzón.
- Convertir el alta manual en script reutilizable tipo add-mailbox.ps1.

## Reglas de seguridad

- No enviar correos sin confirmación explícita.
- No borrar definitivamente.
- No abrir adjuntos.
- No seguir enlaces.
- No leer cuerpos salvo instrucción concreta.
- Usar siempre --account reservas-tossa para este buzón.

## Prueba SMTP

Fecha: 2026-05-27

Comando usado:

    himalaya message send --account reservas-tossa $msg

Resultado:

    Message successfully sent!

Verificación en enviados:

    himalaya envelope list --account reservas-tossa --folder "Elementos enviados" --page-size 5

Resultado:

    Apareció el correo "Prueba SMTP reservas-tossa" en Elementos enviados.

Conclusión:

    SMTP OK.
    Copia en enviados OK.

Nota:

    El mensaje de prueba apareció con fecha 1970-01-01 porque el raw message usado para la prueba manual no incluía cabecera Date.
    Para futuros envíos manuales raw conviene incluir cabecera Date o usar flujos de redacción/respuesta que generen cabeceras completas.
