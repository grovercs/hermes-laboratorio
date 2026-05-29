# Grover / ARA email reply drafting

Use this reference when Grover asks ARA to prepare a reply draft for a message reviewed through Himalaya.

## Safety boundary

- Draft only unless Grover explicitly says to send.
- Do not open attachments.
- Do not follow links.
- Do not move/delete/flag messages while drafting.
- If a body is needed, use `himalaya message read --preview <ID>` so the workflow remains preview-only.

## Drafting workflow

1. Confirm the message ID/folder if needed.
2. Read body only with `--preview` when Grover authorizes it.
3. Extract the practical request in 1-2 lines.
4. Check whether the original message already contains a long signature/legal footer.
5. If there is already a signature/footer, avoid repeating a full signature in the draft; use a short sign-off such as `Un saludo,` plus `Vielha Computer` or Grover's name if appropriate.
6. Produce a ready-to-copy draft, not a sent message.
7. If Grover then explicitly approves with wording like `envíalo`, send the already-reviewed draft using the intended account; report account, recipient and subject after success.

## Sending an approved reply draft

When the final action is an approved reply to a specific existing message:

1. Use `himalaya template reply --account <account> --folder <folder> <id> '<body>'` first to generate the reply template and capture the correct `To`, `Subject`, and `In-Reply-To` headers without opening attachments.
2. Review the generated headers/body for obvious mistakes before sending.
3. Pipe the final reviewed template to `himalaya template send --account <account>`.
4. If Himalaya reports success, say it was sent and include the account, recipient and subject. Do not claim attachments/links were opened unless they were.

For institutional cases where Grover chooses a different sender account (for example `direccion-tossa`) and says not to force a technical reply in the same thread, compose a new message from that account, keep `RE:` in the subject only for visible context, add any requested `Cc`, and do not include `In-Reply-To` unless Grover asks to thread it technically.

## Grover style for replies

- Spain Spanish by default, but if Grover requests Catalan, keep the same structure and tone in clear professional Catalan.
- Natural, close, professional, direct.
- Short sentences.
- Avoid generic AI phrasing such as “espero que este mensaje le encuentre bien”.
- Keep the structure simple: thanks, answer, next step, sign-off.
- When drafting replies about official listings, business relationships, accommodation categories, or administrative status, be prudent: do not assert legal/administrative categories that the recipient has not confirmed, but do state confirmed operational facts clearly. Example wording in Catalan: `les dades d’El Bergantí i L’Hostalet de Tossa, gestionats operativament des d’Alojamientos Tossa de Mar`.
- For Catalan replies from `reservas-tossa` or Alojamientos Tossa de Mar, prefer consistent polite plural forms when addressing institutions: `vostra resposta`, `us constin`, `podríeu`, `necessiteu`, `facilitar-vos`, `vostres indicacions`.
- For institutional or administrative communications involving public authorities, tourist directories, associations, federations, or official establishment data, recommend sending from `direccion-tossa` when configured, or at least copying direction/management. If only `reservas-tossa` is configured, prepare the text but warn before sending: `revisar si debe salir desde dirección`.
- In Alojamientos Tossa de Mar institutional drafts, state the operational fact once: `Des d’Alojamientos Tossa de Mar gestionem operativament El Bergantí i L’Hostalet de Tossa.` After that, avoid repeating the full formula; use cleaner later references like `aquests establiments` or `les dades d’aquests establiments`.
- When signing institutional Alojamientos Tossa de Mar drafts from direction, use `Direcció` / `Alojamientos Tossa de Mar`; for reservas-style drafts, use `Recepció` / `Alojamientos Tossa de Mar` when appropriate.
- For supplier/distributor information requests from Vielha Computer, prefer this concise style: say `Estamos revisando posibles proveedores`, ask to `ampliaseis un poco la información para trabajar como distribuidor o profesional`, request product types/brands, professional purchase conditions, volume discounts, usual delivery times, warranties/RMA, and updated PDF/Excel/online catalogue; close with `Con esta información podremos valorar si encaja con las necesidades de nuestros clientes. Quedamos pendientes.`

## Example pattern

```text
Hola,

Gracias por contactar con nosotros.

[Respuesta clara en frases cortas.]

Para poder avanzar, necesitamos:

- [dato 1]
- [dato 2]
- [dato 3]

Cuando nos envíe esta información, podremos revisarlo y prepararlo.

Quedamos atentos.

Un saludo,
Vielha Computer
```

## Common pitfall

Do not paste the original long legal footer into the draft unless Grover asks for a complete final email template including signature/legal text. In Telegram, keep the draft compact and copy-ready.
