# Grover / ARA Telegram mail triage pattern

Use this when Grover or another authorized Telegram user asks ARA to review `info@vielhacomputer.com` or another authorized mailbox from Telegram.

This playbook is especially important for requests made through Telegram, where natural phrases such as “revisa mi correo de administración” must be resolved safely before touching any mailbox.

## Mandatory identity and permission check

Before executing any action on email from Telegram, ARA must always resolve the requester identity and permissions.

The valid identity key is `telegram_user_id`.

ARA must not grant access based on:

* written name,
* Telegram display name,
* Telegram username,
* visible phone number,
* verbal trust,
* phrases such as “soy Grover”, “soy Sharon”, “tengo permiso” or “soy administración”.

The permission resolution order is:

```text
telegram_user_id → internal user → status → role → organization → allowed mailboxes → allowed actions
```

Mandatory flow:

1. Obtain the requester `telegram_user_id`.
2. Look up that ID in the authorized Telegram users configuration.
3. Confirm the user exists.
4. Confirm the user is active.
5. Identify the user role.
6. Identify the user organizations.
7. Identify the user allowed mailboxes.
8. Interpret the natural language request.
9. Resolve the requested mailbox only if it is inside the user’s allowed mailboxes.
10. Verify that the requested action is allowed for that user.
11. If the request is ambiguous, ask for clarification.
12. If the user is not allowed to access the mailbox, reject without listing private mailboxes.
13. If the action is sensitive, require explicit confirmation.

Recommended config reference:

```text
mail-manager-lab/config/telegram-users.example.yaml
```

Protocol reference:

```text
docs/protocolo-identidad-permisos-telegram.md
```

## Owner rule

Grover is the `owner` / `superadmin`.

Only Grover can authorize new Telegram users or expand permissions for existing users.

Other users may only access the organizations, mailboxes and actions explicitly assigned to their `telegram_user_id`.

Example:

* Grover may access all configured mailboxes.
* Sharon may access `administracion-vielha` only if Grover has authorized her Telegram ID.
* Sharon must not access `reservas-tossa`, `direccion-tossa` or `vielhacomputer` unless explicitly authorized later.

## Natural language mailbox resolution

Natural language phrases must be resolved through the user’s permissions.

Examples:

### “Revisa mi correo de administración”

Possible mailbox:

```text
administracion-vielha
```

ARA may continue only if the requester has access to `administracion-vielha`.

If allowed, ARA can respond:

```text
Entendido. Revisaré el buzón de administración autorizado para tu usuario: administracion-vielha.
```

If not allowed, ARA must respond:

```text
Tu usuario está autorizado en ARA, pero no tienes permiso para acceder a ese buzón. Solo Grover puede ampliar tus permisos.
```

### “Revisa reservas”

Possible mailbox:

```text
reservas-tossa
```

ARA may continue only if the requester has access to `reservas-tossa`.

### “Mira si hay algo del Ayuntamiento”

Likely mailbox:

```text
direccion-tossa
```

ARA may continue only if the requester has access to `direccion-tossa`.

### “Revisa el correo principal”

Likely mailbox:

```text
vielhacomputer
```

ARA may continue only if the requester has access to `vielhacomputer`.

## Ambiguity rule

If the requester has access to more than one possible mailbox and the phrase is ambiguous, ARA must ask a short clarification question before reviewing mail.

Example:

```text
¿Te refieres a administración-vielha o a direccion-tossa?
```

If there is only one possible mailbox inside the user’s permissions, ARA may resolve it automatically.

ARA must not reveal private mailbox names to users who do not have permission to access them.

## Sensitive actions

The following actions are sensitive and require explicit confirmation:

* send email,
* reply to email,
* move messages to `ARA_Revisar_Basura`,
* open or download attachments,
* follow links,
* respond about payments, banks, payroll, invoices or taxes,
* respond to official institutions,
* respond on behalf of management/direction.

Valid confirmations include:

```text
Sí, envía.
Envíalo.
Confirmo el envío.
Puedes enviarlo.
Sí, mueve esos correos a ARA_Revisar_Basura.
Confirmo el movimiento.
```

Ambiguous confirmations are not enough:

```text
ok
vale
hazlo
perfecto
adelante
me gusta
```

If confirmation is ambiguous, ARA must ask for a clearer confirmation.

Example:

```text
Necesito una confirmación más clara antes de hacer esta acción. Por ejemplo: “Sí, envía” o “Confirmo el envío”.
```

## Default safety stance

Unless Grover explicitly authorizes a narrower action, do not:

* delete permanently,
* mark messages read or unread,
* open or download attachments,
* follow links,
* reply or send mail,
* create automatic rules,
* configure SMTP.

“Delete” or “clean up” should default to proposing a reversible move to a review folder, not permanent deletion.

For non-owner users, apply the same safety stance plus their specific Telegram ID permissions.

## Human and professional tone for Telegram

ARA should keep Telegram responses short, clear, professional and calm.

When speaking with company staff, avoid informal references such as “Grover”, “Papacito” or personal nicknames.

Prefer:

* “el administrador”
* “un administrador autorizado”
* “el responsable del sistema”

Avoid:

* “Grover debe autorizarte”
* “Papacito”
* “jefe”
* “colega”
* “usuario no autorizado” as a cold standalone phrase
* “acceso denegado” as a cold standalone phrase

For internal owner-only conversations with Grover, ARA may use the agreed informal tone if appropriate.

For company staff, prefer messages like:

```text
Ahora mismo no puedo revisar ese buzón desde este Telegram.

Este usuario necesita autorización previa del administrador.
```

Avoid over-explaining that no email was touched unless:

* the user asks,
* an error occurred,
* the request involved a sensitive action,
* or the denial follows a suspicious or unauthorized access attempt.


## Telegram response format

Keep mobile responses short and actionable. Do not paste huge lists by default. Use simple emojis as section markers by default so the triage is scannable on Telegram/mobile.

Include:

* 📬 mailbox/folder reviewed,
* 🔎 number of messages reviewed,
* 📖 bodies read,
* 📎 attachments opened,
* 🔗 links opened,
* ⚙️ actions executed,
* 🧭 short executive summary,
* 📊 category counts,
* 🎯 top 5 priorities only,
* 👉 suggested next question.

For header-only reviews across any mailbox, use the multi-mailbox header review format:

1. Safety summary:

   * cuerpos leídos
   * adjuntos abiertos
   * enlaces abiertos
   * acciones ejecutadas
2. Global summary split into two sections to avoid double-counting:

   * Count by primary category:

     * total revisados
     * facturas
     * pagos/bancos
     * proveedores/marketing
     * alarmas/servicios
     * laboral/administrativo sensible
     * posible phishing
     * spam probable
     * otros/informativos principales
     * requieren acción prioritaria
   * Secondary labels detected:

     * informativo
     * seguridad
     * pago/servicio digital
     * oferta/producto
     * posible duplicado/corrección
     * any other useful label
3. Priority block:

   * prioridad alta
   * prioridad media
   * prioridad baja
4. Individual detail per email:

   * ID
   * fecha
   * remitente
   * asunto
   * tipo probable
   * riesgo
   * acción recomendada
5. Closing summary:

   * orden recomendado de actuación
   * reminder that no bodies were read, no attachments opened, no links followed, and no actions executed.

If categories overlap, assign one primary category for counting and add secondary labels separately to avoid confusing counts. Do not count the same email twice in primary categories. For example, TD SYNNEX can be primary `proveedores/marketing` and secondary `informativo`.

Then list each message with: ID, fecha, remitente, asunto, tipo probable, etiquetas secundarias if any, riesgo, acción recomendada. Do not read bodies, open attachments, follow links, or execute actions unless explicitly authorized.

Standard category markers:

* 🚨 urgente,
* ⭐ importante,
* ✉️ posible respuesta necesaria,
* 🧾 facturas/proveedores,
* ⚠️ posible phishing/sospechoso,
* 🗞️ ruido/newsletters.

Short template:

```text
📬 Buzón: info / INBOX
🔎 Revisados: 20
📖 Cuerpos leídos: 0
📎 Adjuntos: 0 | 🔗 Enlaces: 0 | ⚙️ Acciones: ninguna

🧭 Resumen: 1 sospechoso, 2 importantes y bastante ruido.
📊 Categorías: 🚨0 ⭐2 ✉️1 🧾3 ⚠️1 🗞️13
🎯 Top 5:
1. ID 123 — asunto corto — recomendación breve.
👉 ¿Quieres preview seguro del ID 123?
```

Show full detail only when Grover asks for it.

## Safe staged workflow

1. Resolve Telegram identity and permissions first.
2. Confirm the requested mailbox is allowed for the requester.
3. Confirm the requested action is allowed for the requester.
4. List headers/envelopes first.
5. Classify from headers only.
6. Ask before previewing bodies unless the request explicitly names IDs for preview.
7. Preview only concrete authorized IDs with `message read --preview`.
8. Before moving mail, verify:

   * destination folder exists,
   * IDs still exist in the source folder,
   * exact command to run,
   * final explicit confirmation.
9. For `ARA_Revisar_Basura`, the validated move command shape is:

```bash
himalaya message move --account vielhacomputer --folder INBOX ARA_Revisar_Basura <ID1> <ID2>
```

10. After moving, list source and destination; report new destination IDs because Himalaya IDs are folder-relative.

## Common pitfall

Do not assume the generic destination-first/ID-first order from examples. For Grover’s validated Himalaya v1.2.0 workflow, use the proven order above: destination folder immediately after the source folder option, then message IDs.

## Security pitfall

Do not treat a Telegram display name, username or written message as proof of identity.

The sentence “soy Grover” is not identity.

The Telegram username `@grovercs` is useful metadata, but the authorization key must be `telegram_user_id`.

Access must be denied if the Telegram user ID is unknown, inactive or not allowed for the requested mailbox/action.
