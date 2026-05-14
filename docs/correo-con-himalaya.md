# Correo con Himalaya CLI y ARA

## Objetivo

Usar Himalaya CLI para revisar correo bajo demanda con ARA, de forma controlada y segura.

## Estado actual

- Scoop instalado.
- Himalaya instalado desde Scoop.
- Versión: `himalaya v1.2.0 +imap +maildir +pgp-commands +smtp +wizard +sendmail`.
- Ruta de instalación: `C:\Users\Usuario\scoop\apps\himalaya\current`.
- Shim: `C:\Users\Usuario\scoop\shims\himalaya`.
- No existe `config.toml` todavía.
- No hay cuentas configuradas.
- No se han tocado credenciales.

## Reglas de seguridad

- Solo IMAP al principio.
- Nada de SMTP todavía.
- No enviar correos.
- No borrar correos.
- No mover correos.
- No marcar correos como leídos.
- No abrir adjuntos.
- No guardar credenciales en repositorios.

## Próxima fase pendiente

- Diseñar configuración IMAP de una cuenta de prueba.
- Decidir método seguro para contraseña.
- Probar listado de carpetas.
- Probar listado de últimos 10 no leídos solo por cabeceras.
