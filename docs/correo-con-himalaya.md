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

## Criterio inicial de clasificación de correos

### Prioridad alta

- Facturas de proveedores críticos: IONOS, Logalty, hosting, dominios, servicios cloud, telefonía y software importante.
- Pedidos enviados o incidencias de proveedores importantes: PcComponentes, mayoristas y hosting.
- Avisos de servicios críticos, pero siempre verificando desde portal oficial.

### Posible phishing / revisar con cuidado

- Correos de bancos enviados por remitentes extraños.
- DocuSign inesperados, especialmente en idiomas no habituales.
- Facebook Business Manager o cuentas publicitarias si no se esperaban.
- Asuntos genéricos tipo "Important Message" usando marcas sensibles como IONOS.
- Nunca abrir enlaces ni adjuntos directamente desde estos correos.

### Prioridad media

- Proveedores útiles para Vielha Computer: Prostcomputer, PcComponentes Resellers, Hispamicro, SWPanel y Ecomspain.
- Proveedores o plataformas relacionadas con WISP, redes, telecomunicaciones y hosting: DOWISP, SWPanel y conectividad.
- Webinars técnicos que puedan aportar valor al negocio.

### Prioridad baja

- Newsletters genéricas.
- Promociones repetidas.
- eBay y marketplaces salvo que haya una compra activa.
- Formación/comercial no urgente.
- Seguros u ofertas comerciales no solicitadas.

### Reglas de seguridad para clasificación

- Clasificar por cabeceras primero.
- No leer cuerpos sin autorización explícita.
- No abrir adjuntos sin autorización explícita.
- No mover, borrar, marcar como leído ni enviar nada.
- Para facturas o avisos críticos, recomendar revisar desde portal oficial.

## Próxima fase pendiente

- Decidir si se autoriza leer cuerpos de correos seleccionados.
- Alternativa segura: seguir trabajando solo con cabeceras/envelopes.
- Si se autoriza lectura de cuerpos, definir antes una regla estricta: leer solo IDs concretos, sin adjuntos, sin mover, sin borrar, sin marcar como leído y sin responder automáticamente.
- Método de contraseña migrado correctamente a Windows Credential Manager y probado con Himalaya.

---

## Estado actual: Himalaya con Windows Credential Manager

Fecha: 15/05/2026

Se ha configurado Himalaya para leer la contraseña IMAP desde Windows Credential Manager usando el target:

```text
himalaya:info@vielhacomputer.com
```

El archivo `config.toml` mantiene la autenticación mediante comando externo:

```text
C:\Users\Usuario\.config\himalaya\get-imap-password.ps1
```

Pruebas realizadas correctamente:

```powershell
himalaya folder list --account vielhacomputer
himalaya envelope list --account vielhacomputer --folder INBOX --page 1 --page-size 10
```

Resultado:
- Se listaron carpetas IMAP correctamente.
- Se listaron cabeceras/envelopes de INBOX correctamente.
- No se configuró SMTP.
- No se enviaron correos.
- No se leyeron cuerpos.
- No se abrieron adjuntos.
- No se movieron ni borraron mensajes.
- No se marcaron mensajes como leídos.
- No se guardó ninguna contraseña en texto plano dentro del repositorio.

Nota importante:
Al usar `New-StoredCredential`, no mostrar nunca el objeto completo en pantalla porque puede imprimir el campo `Password`.

Usar siempre `| Out-Null` al guardar la credencial.
