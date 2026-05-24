# ARA Mail Manager

Propuesta de diseño para ARA Mail Manager: sistema replicable para gestionar múltiples buzones propios o de clientes con supervisión humana.

## Visión

ARA Mail Manager no debe responder automáticamente. Su función es leer, interpretar, clasificar y preparar propuestas de respuesta. Grover, o el propietario autorizado del buzón, revisa, corrige o aprueba antes de cualquier acción con impacto externo.

El sistema debe aprender progresivamente el estilo de redacción a partir de correcciones aprobadas, manteniendo siempre una separación clara entre:

- núcleo común,
- configuración por cliente,
- credenciales seguras,
- histórico de decisiones aprobadas,
- borradores propuestos,
- acciones ejecutadas con confirmación.

## Principios de seguridad

1. No guardar contraseñas, tokens, claves API ni secretos en Git.
2. No guardar credenciales en texto plano.
3. En Windows local, usar Windows Credential Manager.
4. No enviar correos sin confirmación explícita.
5. No borrar definitivamente por defecto.
6. Para “borrar”, mover primero a una carpeta de revisión o Papelera.
7. No abrir adjuntos automáticamente.
8. No seguir enlaces automáticamente.
9. No crear reglas automáticas sin confirmación explícita.
10. Separar cada cliente o propietario para evitar mezcla de buzones, estilos y permisos.

## Alcance funcional

ARA Mail Manager debe permitir:

- Soportar varios buzones: IONOS, Gmail, Outlook u otro proveedor IMAP.
- Preguntar qué buzón se quiere supervisar antes de listar o revisar correos.
- Listar carpetas.
- Listar cabeceras o envelopes.
- Previsualizar correos de forma controlada.
- Clasificar correos por prioridad, tipo, riesgo o acción recomendada.
- Preparar respuestas en el estilo del propietario o cliente.
- Aprender del estilo a partir de correcciones aprobadas.
- Proponer movimientos a carpeta de revisión, Papelera u otras carpetas seguras.
- Registrar acciones propuestas y acciones aprobadas.
- Replicar la arquitectura para clientes sin mezclar datos.

## Estructura de carpetas propuesta

Estructura conceptual dentro del repositorio o producto ARA Mail Manager:

```text
ara-mail-manager/
├── core/
│   ├── imap_client.py
│   ├── mailbox_selector.py
│   ├── classifier.py
│   ├── draft_generator.py
│   ├── style_learner.py
│   ├── permission_policy.py
│   └── audit_log.py
├── clients/
│   ├── grover/
│   │   ├── mailboxes.yaml
│   │   ├── permissions.yaml
│   │   ├── style_profile.md
│   │   ├── folders.yaml
│   │   └── prompts/
│   │       ├── triage.md
│   │       └── reply_style.md
│   └── cliente-ejemplo/
│       ├── mailboxes.yaml
│       ├── permissions.yaml
│       ├── style_profile.md
│       ├── folders.yaml
│       └── prompts/
├── scripts/
│   ├── add-mailbox.ps1
│   ├── list-mailboxes.ps1
│   ├── check-mailbox.ps1
│   ├── preview-message.ps1
│   ├── propose-reply.ps1
│   ├── record-correction.ps1
│   └── move-to-review.ps1
├── docs/
│   ├── onboarding-cliente.md
│   ├── permisos.md
│   ├── seguridad.md
│   └── flujo-operativo.md
└── logs-locales-no-git/
```

Notas:

- `core/` contiene la lógica común reutilizable.
- `clients/<cliente>/` contiene configuración no secreta por cliente.
- Las credenciales no viven en `clients/`; se guardan en el gestor seguro del sistema.
- Los logs locales, previews temporales, borradores sensibles o exportaciones deben quedar fuera de Git.
- Cada cliente debe tener su propio perfil de estilo, permisos y buzones autorizados.

## Configuración por buzón

Ejemplo conceptual sin secretos:

```yaml
mailboxes:
  - id: vielhacomputer-ionos
    owner: Grover Castellon Suarez
    provider: ionos
    protocol: imap
    account_alias: vielhacomputer
    email: info@example.invalid
    credential_target: ara-mail-manager:vielhacomputer-ionos
    allowed_actions:
      - list_folders
      - list_envelopes
      - preview_message
      - propose_reply
      - move_to_review
    forbidden_actions:
      - send_without_confirmation
      - delete_permanently
      - open_attachments_without_confirmation
      - follow_links_without_confirmation
```

El campo `credential_target` identifica la entrada segura en Windows Credential Manager u otro backend equivalente. No debe contener la contraseña.

## Flujo de alta de nuevo buzón

1. Preguntar propietario o cliente.
2. Preguntar proveedor: IONOS, Gmail, Outlook u otro IMAP.
3. Preguntar dirección de correo o alias operativo.
4. Preguntar servidor IMAP, puerto y seguridad si no se detecta automáticamente.
5. Crear un identificador interno del buzón.
6. Crear entrada segura en Windows Credential Manager.
7. Guardar solo configuración no secreta en el perfil del cliente.
8. Probar conexión IMAP con acción mínima: listar carpetas.
9. Confirmar carpetas disponibles.
10. Definir carpeta de revisión para mensajes a limpiar.
11. Definir permisos iniciales.
12. Crear o revisar perfil de estilo del propietario.
13. Registrar el buzón como activo solo después de prueba correcta.

Ejemplo de target recomendado en Windows Credential Manager:

```text
ara-mail-manager:<cliente>:<buzon>
```

Ejemplo:

```text
ara-mail-manager:grover:vielhacomputer-ionos
```

Importante: al crear credenciales con `New-StoredCredential`, evitar imprimir el objeto completo. Usar `| Out-Null`.

## Flujo operativo diario

1. ARA pregunta qué buzón se quiere supervisar.
2. El usuario elige buzón o cliente.
3. ARA lista carpetas autorizadas.
4. ARA lista cabeceras o envelopes de la carpeta elegida.
5. ARA clasifica correos sin abrir adjuntos ni seguir enlaces.
6. Si hace falta, ARA pide permiso para previsualizar mensajes concretos.
7. ARA prepara propuestas:
   - responder,
   - archivar,
   - mover a revisión,
   - marcar como pendiente,
   - ignorar,
   - revisar desde portal oficial.
8. El usuario corrige, aprueba o rechaza.
9. ARA registra la decisión aprobada.
10. Si hay respuesta, ARA prepara borrador final.
11. El envío solo se ejecuta con confirmación explícita.

## Niveles de permisos

### Nivel 0: Solo lectura de estructura

Permitido:

- Listar buzones configurados.
- Listar carpetas.

Prohibido:

- Leer previews.
- Mover mensajes.
- Enviar.
- Borrar.
- Abrir adjuntos.

### Nivel 1: Triage por cabeceras

Permitido:

- Listar carpetas.
- Listar envelopes o cabeceras.
- Clasificar por remitente, asunto, fecha y metadatos disponibles.

Prohibido:

- Leer cuerpo completo salvo preview autorizado.
- Mover mensajes sin confirmación.
- Enviar.
- Borrar definitivamente.

### Nivel 2: Preview controlado

Permitido:

- Leer previews de mensajes concretos.
- Preparar resúmenes.
- Preparar propuestas de respuesta.

Prohibido:

- Abrir adjuntos.
- Seguir enlaces.
- Enviar sin confirmación.
- Borrar definitivamente.

### Nivel 3: Acciones reversibles confirmadas

Permitido con confirmación explícita:

- Mover a carpeta de revisión.
- Mover a Papelera.
- Archivar.
- Crear borrador local o propuesta de respuesta.

Prohibido por defecto:

- Borrado definitivo.
- Reglas automáticas.
- Envío sin confirmación final.

### Nivel 4: Envío confirmado

Permitido solo con confirmación explícita y mensaje final visible:

- Enviar respuesta aprobada.
- Reenviar correo aprobado.

Debe registrar:

- quién aprobó,
- cuándo se aprobó,
- buzón usado,
- destinatario,
- asunto,
- resumen del contenido enviado.

## Aprendizaje del estilo de redacción

ARA debe aprender de correcciones aprobadas, no de cualquier borrador provisional.

Flujo propuesto:

1. ARA genera una propuesta de respuesta.
2. Grover o el cliente corrige el texto.
3. El usuario marca la corrección como aprobada para aprendizaje.
4. ARA compara propuesta inicial y versión aprobada.
5. ARA extrae patrones de estilo:
   - saludo,
   - despedida,
   - nivel de formalidad,
   - longitud,
   - vocabulario habitual,
   - tono comercial o técnico,
   - frases recurrentes,
   - forma de pedir confirmación,
   - forma de explicar precios, plazos o incidencias.
6. ARA actualiza `style_profile.md` del cliente o propietario.
7. En siguientes borradores, ARA usa ese perfil como guía.

Ejemplo de perfil de estilo no secreto:

```markdown
# Perfil de estilo - Cliente ejemplo

## Tono
- Cercano, claro y profesional.
- Evitar tecnicismos si el destinatario no es técnico.

## Saludos habituales
- Hola,
- Buenos días,

## Despedidas habituales
- Un saludo,
- Gracias,

## Reglas
- No prometer plazos cerrados sin confirmación.
- Para incidencias técnicas, explicar primero el impacto y luego la solución.
```

No se deben guardar cuerpos completos de correos sensibles como “aprendizaje” salvo autorización y anonimización.

## Replicabilidad para clientes

Para replicar ARA Mail Manager en clientes:

1. Mantener un núcleo común sin datos de clientes.
2. Crear una carpeta o perfil por cliente.
3. Guardar solo configuración no secreta en Git o plantillas.
4. Guardar credenciales en el gestor seguro del entorno del cliente.
5. Definir permisos por cliente y por buzón.
6. Definir estilo de redacción por propietario.
7. Definir carpetas seguras:
   - revisión,
   - archivo,
   - papelera,
   - pendientes.
8. Definir protocolo de aprobación.
9. Registrar auditoría local de acciones aprobadas.
10. Preparar documentación de onboarding y soporte.

Plantilla mínima por cliente:

```text
clients/<cliente>/
├── mailboxes.yaml
├── permissions.yaml
├── style_profile.md
├── folders.yaml
└── prompts/
    ├── triage.md
    └── reply_style.md
```

## Scripts o comandos futuros necesarios

### Gestión de buzones

```powershell
.\scripts\add-mailbox.ps1 -Client grover -Mailbox vielhacomputer-ionos
.\scripts\list-mailboxes.ps1 -Client grover
.\scripts\check-mailbox.ps1 -Client grover -Mailbox vielhacomputer-ionos
```

### Revisión y triage

```powershell
.\scripts\list-folders.ps1 -Client grover -Mailbox vielhacomputer-ionos
.\scripts\list-envelopes.ps1 -Client grover -Mailbox vielhacomputer-ionos -Folder INBOX -PageSize 50
.\scripts\preview-message.ps1 -Client grover -Mailbox vielhacomputer-ionos -Folder INBOX -MessageId 12345
```

### Propuestas y aprendizaje

```powershell
.\scripts\propose-reply.ps1 -Client grover -Mailbox vielhacomputer-ionos -Folder INBOX -MessageId 12345
.\scripts\record-correction.ps1 -Client grover -DraftId draft-001 -ApprovedCorrection correction.md
.\scripts\update-style-profile.ps1 -Client grover
```

### Acciones reversibles

```powershell
.\scripts\move-to-review.ps1 -Client grover -Mailbox vielhacomputer-ionos -Folder INBOX -MessageId 12345
.\scripts\move-to-trash.ps1 -Client grover -Mailbox vielhacomputer-ionos -Folder INBOX -MessageId 12345
```

### Envío confirmado

```powershell
.\scripts\send-approved-reply.ps1 -Client grover -DraftId draft-001 -Confirm
```

Los comandos anteriores son propuesta futura. No implican que los scripts existan todavía ni que SMTP esté configurado.

## Integración IMAP propuesta

Para entorno local Windows, Himalaya CLI puede servir como primera capa operativa IMAP si se mantiene la configuración segura:

- autenticación mediante comando externo,
- contraseña en Windows Credential Manager,
- lectura con `--preview` cuando aplique,
- sin SMTP hasta autorización explícita,
- sin adjuntos ni enlaces automáticos.

A medio plazo, el núcleo común podría abstraer el proveedor con una interfaz propia:

```text
MailboxProvider
├── HimalayaProvider
├── GmailApiProvider
├── MicrosoftGraphProvider
└── GenericImapProvider
```

Así ARA Mail Manager puede empezar con IMAP/Himalaya y crecer hacia APIs oficiales si el cliente lo necesita.

## Auditoría mínima

Cada acción aprobada debería registrar:

- fecha y hora,
- cliente,
- buzón,
- carpeta origen,
- ID del mensaje en esa carpeta,
- acción propuesta,
- acción aprobada,
- usuario que aprobó,
- resultado,
- errores si los hubo.

No guardar contraseñas, tokens ni cuerpos completos sensibles en auditoría.

## Primera prueba real por Telegram

Fecha: 2026-05-24

Se validó un flujo real supervisado de ARA Mail Manager desde Telegram, con Gateway activo, usando el buzón autorizado `info@vielhacomputer.com` mediante la cuenta Himalaya `vielhacomputer`.

### Flujo validado

1. ARA respondió correctamente por Telegram con el Gateway activo.
2. ARA listó solo cabeceras/envelopes de los últimos 20 correos del `INBOX`.
3. En la primera fase no leyó cuerpos.
4. No abrió adjuntos.
5. No siguió enlaces.
6. No movió, borró, marcó ni respondió nada durante el triage inicial.
7. Con autorización explícita, ARA leyó en modo preview solo los IDs `22448`, `22455` y `22453`.
8. Clasificó:
   - `22448`: Santander falso, phishing casi seguro.
   - `22455`: AR24 falso, phishing muy probable.
   - `22453`: Naturgy sospechoso; no se movió.
9. ARA propuso una acción reversible para los dos phishing claros.
10. Grover corrigió la propuesta para usar la carpeta existente `ARA_Revisar_Basura` y el formato correcto ya probado de Himalaya.
11. Tras confirmación explícita de Grover, ARA movió solo los mensajes autorizados:

```bash
himalaya message move --account vielhacomputer --folder INBOX ARA_Revisar_Basura 22448 22455
```

12. ARA verificó que:
   - `22448` y `22455` ya no aparecían en `INBOX`.
   - ambos aparecían en `ARA_Revisar_Basura`.
   - los nuevos IDs relativos en la carpeta destino eran `3` para el Santander falso y `4` para el AR24 falso.

### Seguridad respetada

- No se borró definitivamente ningún correo.
- No se abrieron adjuntos.
- No se siguieron enlaces.
- No se respondió ningún correo.
- No se configuró SMTP.
- No se tocaron secretos.
- La acción ejecutada fue reversible: movimiento a carpeta de revisión existente.

### Lecciones operativas

- El flujo por Telegram es viable para triage supervisado real.
- La primera fase debe seguir siendo por cabeceras.
- El preview debe limitarse a IDs concretos autorizados.
- Para acciones reversibles, confirmar antes:
  1. carpeta destino existente,
  2. IDs actuales en carpeta origen,
  3. comando exacto,
  4. confirmación final de Grover.
- Después de mover, verificar siempre carpeta origen y destino, porque los IDs de Himalaya son relativos a cada carpeta.

## Estado inicial del proyecto

Fecha: 2026-05-24

Estado actual:

- Diseño del sistema multi-buzón supervisado.
- Sin modificación de configuración real.
- Sin apertura de correos reales.
- Sin acciones de correo ejecutadas.
- Sin secretos documentados.

Pendiente:

- Definir arquitectura técnica final.
- Definir formato definitivo de configuración por cliente.
- Definir scripts iniciales.
- Definir política exacta de permisos.
- Definir flujo de aprendizaje de estilo.
- Definir plantilla de onboarding para clientes.
- Definir estrategia de logs/auditoría sin datos sensibles.
