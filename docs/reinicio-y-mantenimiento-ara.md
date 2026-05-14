# Reinicio y mantenimiento de ARA

## Ajustes realizados para evitar bloqueos por compactación

Fecha del cambio: 2026-05-14

Ajustes documentados:

- `HERMES_STREAM_READ_TIMEOUT=1800` añadido en `.env`.
- `auxiliary.compression.timeout` cambiado de `120` a `600` en `config.yaml`.
- Backups creados en `C:\Users\Usuario\AppData\Local\hermes\backups-config`.
- Recordatorio: reiniciar Hermes después de modificar la configuración para que los cambios se apliquen correctamente.

Motivo:

- Evitar bloqueos cuando la compactación de contexto tarda más de 120 segundos.

Nota de seguridad:

- Este documento no incluye secretos ni valores sensibles.
