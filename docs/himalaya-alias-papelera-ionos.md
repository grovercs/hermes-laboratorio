# Mejora Himalaya - Alias Papelera IONOS

Fecha: 2026-05-29

## Contexto

Durante la prueba de guardado de borrador en `direccion-tossa`, se validó que:

    himalaya message save --account direccion-tossa --folder Borradores $draft

guardaba correctamente un mensaje en Borradores.

Al intentar borrar el borrador con:

    himalaya message delete --account direccion-tossa --folder Borradores 1

Himalaya falló con:

    destination folder does not exist

## Causa

Las cuentas IONOS tienen la carpeta de papelera llamada:

    Papelera

pero en `config.toml` no estaba definido el alias de trash.

## Solución aplicada

Se añadió en las tres cuentas Himalaya:

    folder.aliases.trash = "Papelera"

Cuentas afectadas:

    vielhacomputer
    reservas-tossa
    direccion-tossa

## Backup realizado

Antes de modificar la configuración se creó backup:

    config.toml.backup-before-trash-aliases-20260529-132409

## Validación

Comando:

    himalaya account list

Resultado:

    direccion-tossa: IMAP, SMTP
    reservas-tossa: IMAP, SMTP
    vielhacomputer: IMAP, SMTP, default yes

Comando:

    himalaya folder list --account direccion-tossa

Resultado:

    Borradores
    Elementos enviados
    INBOX
    Papelera
    Spam

Conclusión:

    Configuración OK.
    Alias trash añadido para cuentas IONOS.
    La cuenta direccion-tossa sigue funcionando correctamente.

## Nota operativa

Para mover un mensaje manualmente a Papelera se puede usar:

    himalaya message move --account direccion-tossa --folder Borradores Papelera 1

Para borrado reversible, preferir mover a Papelera antes que expurgar.

No usar expunge salvo confirmación explícita.
