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

---

## Hallazgo: lectura preview desde Hermes/Git Bash con config temporal

Fecha: 16/05/2026

Durante una revisión autorizada de correos concretos se detectó una diferencia entre PowerShell normal y Hermes/Git Bash al ejecutar Himalaya en Windows.

### Problema detectado

Desde PowerShell normal funciona la ruta del helper con barras invertidas:

```text
C:\Users\Usuario\.config\himalaya\get-imap-password.ps1
```

Desde Hermes/Git Bash, esa misma ruta con barras invertidas puede romperse al pasar por las capas de shell y llegar a PowerShell sin separadores, provocando un error similar a:

```text
C:UsersUsuario.confighimalayaget-imap-password.ps1
```

### Solución segura probada

Se creó una configuración temporal de Himalaya sin secretos, sin modificar la configuración real, usando la ruta del helper en formato compatible con Git Bash:

```text
C:/Users/Usuario/.config/himalaya/get-imap-password.ps1
```

La línea usada en la config temporal fue:

```toml
backend.auth.cmd = "powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:/Users/Usuario/.config/himalaya/get-imap-password.ps1"
```

El patrón de lectura seguro fue:

```bash
himalaya --config .himalaya-temp-preview-vielhacomputer.toml message read --account vielhacomputer --folder INBOX --preview <ID>
```

### Resultado

- La config temporal con ruta `C:/Users/Usuario/.config/himalaya/get-imap-password.ps1` funcionó correctamente desde Hermes/Git Bash.
- La opción `--preview` permitió leer cuerpos de mensajes sin marcarlos como leídos.
- La config temporal fue borrada al final.
- No se modificó la config real de Himalaya.
- No se modificó `get-imap-password.ps1`.
- No se guardaron secretos.
- No se abrieron adjuntos.
- No se descargaron adjuntos.
- No se siguieron enlaces.
- No se movieron correos.
- No se borraron correos.
- No se marcaron correos como leídos/no leídos.
- No se enviaron correos.

### Regla operativa

Para leer cuerpos desde Hermes/Git Bash sin marcar correos como leídos:

1. Usar siempre `--preview`.
2. Usar IDs concretos autorizados por Grover.
3. Si la ruta del helper falla por barras invertidas, usar una config temporal sin secretos con ruta `C:/Users/Usuario/...`.
4. Borrar siempre la config temporal al final.
5. No abrir adjuntos, no seguir enlaces y no ejecutar acciones de impacto externo sin autorización explícita.

---

## Solución permanente aplicada: ruta del helper compatible con PowerShell y Hermes/Git Bash

Fecha: 16/05/2026

Se aplicó la solución permanente para que Himalaya use una ruta del helper compatible tanto con PowerShell normal como con Hermes/Git Bash.

### Backup creado

Antes de modificar la configuración real se creó este backup:

```text
C:\Users\Usuario\.config\himalaya\config.toml.backup-20260516-012630
```

### Config real modificada

Archivo modificado:

```text
C:\Users\Usuario\.config\himalaya\config.toml
```

### Único cambio realizado

La línea `backend.auth.cmd` ahora usa ruta con barras normales:

```text
C:/Users/Usuario/.config/himalaya/get-imap-password.ps1
```

Motivo: la ruta con barras invertidas funcionaba desde PowerShell normal, pero podía romperse desde Hermes/Git Bash al llegar a PowerShell sin separadores.

### Pruebas realizadas

```bash
himalaya folder list --account vielhacomputer
himalaya message read --account vielhacomputer --folder INBOX --preview 22395
```

### Resultado

Ambas pruebas funcionaron correctamente:

- `folder list` listó las carpetas IMAP de la cuenta `vielhacomputer`.
- `message read --preview 22395` leyó el cuerpo del correo en modo preview.

### Seguridad

Durante la prueba:

- No se abrieron adjuntos.
- No se descargaron adjuntos.
- No se siguieron enlaces.
- No se movieron correos.
- No se borraron correos.
- No se marcaron correos como leídos/no leídos.
- No se enviaron correos.

### Nota

Apareció el aviso no bloqueante:

```text
warning: Failed to set cwd to temp dir
```

El aviso no impidió que Himalaya funcionara correctamente.

---

## Prueba mínima de limpieza IMAP

Fecha: 16/05/2026

Se realizó una prueba mínima de limpieza por IMAP, sin SMTP, para validar el flujo de crear una carpeta de revisión y mover únicamente correos autorizados.

### Acciones ejecutadas

Se creó la carpeta de revisión:

```bash
himalaya folder add --account vielhacomputer ARA_Revisar_Basura
```

Se movieron solo los IDs autorizados `22418` y `22417` desde `INBOX` a `ARA_Revisar_Basura`:

```bash
himalaya message move --account vielhacomputer --folder INBOX ARA_Revisar_Basura 22418 22417
```

Después se listaron las carpetas:

```bash
himalaya folder list --account vielhacomputer
```

Se listaron las cabeceras de la carpeta destino:

```bash
himalaya envelope list --account vielhacomputer --folder ARA_Revisar_Basura --page 1 --page-size 10
```

Y se listaron los últimos 30 correos de `INBOX`:

```bash
himalaya envelope list --account vielhacomputer --folder INBOX --page 1 --page-size 30
```

### Resultado

- La carpeta `ARA_Revisar_Basura` se creó correctamente.
- Se movieron solo los IDs autorizados `22418` y `22417` desde `INBOX`.
- Los correos llegaron correctamente a `ARA_Revisar_Basura`.
- En la carpeta destino, Himalaya les asignó nuevos IDs relativos: `2` y `1`.
- Los IDs originales `22418` y `22417` ya no aparecen en los últimos 30 de `INBOX`.

### Seguridad

Durante la prueba:

- No se borró nada.
- No se marcó ningún correo como leído/no leído.
- No se abrieron adjuntos.
- No se descargaron adjuntos.
- No se siguieron enlaces.
- No se configuró SMTP.
- No se respondió ni se envió ningún correo.
- No se crearon reglas.
- No se movió ningún correo fuera de los IDs autorizados.

### Advertencia importante sobre IDs

Los IDs de Himalaya son relativos a la carpeta. Al mover un correo desde `INBOX` a otra carpeta, el mensaje puede recibir un ID distinto en la carpeta destino.

Regla operativa:

1. Confirmar siempre la carpeta origen.
2. Confirmar siempre los IDs actuales en esa carpeta antes de mover o borrar.
3. Usar siempre `--folder INBOX` cuando el origen sea `INBOX`.
4. Después de mover, listar la carpeta destino y la carpeta origen para verificar el resultado.
5. No borrar mensajes salvo autorización explícita y tras confirmar carpeta e IDs actuales.
