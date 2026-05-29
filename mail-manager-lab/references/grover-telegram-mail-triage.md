# Grover / ARA Telegram mail triage pattern

Use this when Grover asks ARA to review `info@vielhacomputer.com` or another authorized mailbox from Telegram.

## Default safety stance

Unless Grover explicitly authorizes a narrower action, do not:

- delete permanently,
- mark messages read or unread,
- open or download attachments,
- follow links,
- reply or send mail,
- create automatic rules,
- configure SMTP.

“Delete” or “clean up” should default to proposing a reversible move to a review folder, not permanent deletion.

## Telegram response format

Keep mobile responses short and actionable. Do not paste huge lists by default. Use simple emojis as section markers by default so the triage is scannable on Telegram/mobile.

Include:

- 📬 mailbox/folder reviewed,
- 🔎 number of messages reviewed,
- 📖 bodies read,
- 📎 attachments opened,
- 🔗 links opened,
- ⚙️ actions executed,
- 🧭 short executive summary,
- 📊 category counts,
- 🎯 top 5 priorities only,
- 👉 suggested next question.

For header-only reviews across any mailbox, use the multi-mailbox header review format:

1. Safety summary:
   - cuerpos leídos
   - adjuntos abiertos
   - enlaces abiertos
   - acciones ejecutadas
2. Global summary split into two sections to avoid double-counting:
   - Count by primary category:
     - total revisados
     - facturas
     - pagos/bancos
     - proveedores/marketing
     - alarmas/servicios
     - laboral/administrativo sensible
     - posible phishing
     - spam probable
     - otros/informativos principales
     - requieren acción prioritaria
   - Secondary labels detected:
     - informativo
     - seguridad
     - pago/servicio digital
     - oferta/producto
     - posible duplicado/corrección
     - any other useful label
3. Priority block:
   - prioridad alta
   - prioridad media
   - prioridad baja
4. Individual detail per email:
   - ID
   - fecha
   - remitente
   - asunto
   - tipo probable
   - riesgo
   - acción recomendada
5. Closing summary:
   - orden recomendado de actuación
   - reminder that no bodies were read, no attachments opened, no links followed, and no actions executed.

If categories overlap, assign one primary category for counting and add secondary labels separately to avoid confusing counts. Do not count the same email twice in primary categories. For example, TD SYNNEX can be primary `proveedores/marketing` and secondary `informativo`.

Then list each message with: ID, fecha, remitente, asunto, tipo probable, etiquetas secundarias if any, riesgo, acción recomendada. Do not read bodies, open attachments, follow links, or execute actions unless explicitly authorized.

Standard category markers:

- 🚨 urgente,
- ⭐ importante,
- ✉️ posible respuesta necesaria,
- 🧾 facturas/proveedores,
- ⚠️ posible phishing/sospechoso,
- 🗞️ ruido/newsletters.

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

1. List headers/envelopes first.
2. Classify from headers only.
3. Ask before previewing bodies unless the request explicitly names IDs for preview.
4. Preview only concrete authorized IDs with `message read --preview`.
5. Before moving mail, verify:
   - destination folder exists,
   - IDs still exist in the source folder,
   - exact command to run,
   - Grover’s final confirmation.
6. For `ARA_Revisar_Basura`, the validated move command shape is:

```bash
himalaya message move --account vielhacomputer --folder INBOX ARA_Revisar_Basura <ID1> <ID2>
```

7. After moving, list source and destination; report new destination IDs because Himalaya IDs are folder-relative.

## Common pitfall

Do not assume the generic destination-first/ID-first order from examples. For Grover’s validated Himalaya v1.2.0 workflow, use the proven order above: destination folder immediately after the source folder option, then message IDs.