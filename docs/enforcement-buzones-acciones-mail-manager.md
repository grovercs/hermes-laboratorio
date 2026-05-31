# Enforcement de buzones y acciones en ARA Mail Manager

Proyecto: ARA Mail Manager / Hermes / Himalaya  
Estado: diseño pendiente antes de implementación

## Resumen

Ya existe una primera barrera real de seguridad para Telegram:

```text
¿Puede este Telegram hablar con ARA?
```

Esta barrera se aplica mediante:

```text
TELEGRAM_USERS_CONFIG
mail-manager-lab/config/telegram-users.yaml
```

Estado validado:

```text
Grover active → autorizado
Sharon inactive → bloqueada
Usuario desconocido → bloqueado
```

Ahora falta implementar la segunda barrera específica del Mail Manager:

```text
¿Qué buzones y acciones puede usar cada usuario autorizado?
```

Esta segunda barrera debe aplicarse antes de cualquier acción sobre correo.

## Objetivo

Evitar que un usuario activo en Telegram pueda acceder a buzones o ejecutar acciones que no tenga permitidas.

La validación esperada debe seguir esta cadena:

```text
telegram_user_id
→ usuario interno
→ status
→ organización
→ buzones permitidos
→ acciones permitidas
→ confirmación requerida
```

## Diferencia entre las dos barreras

### Barrera 1: acceso al bot

Pregunta:

```text
¿Puede este Telegram hablar con ARA?
```

Control actual:

```text
TELEGRAM_USERS_CONFIG
```

Archivo:

```text
mail-manager-lab/config/telegram-users.yaml
```

Resultado:

- usuarios `active` pueden hablar con ARA;
- usuarios `inactive` no llegan al agente;
- usuarios desconocidos no llegan al agente.

### Barrera 2: permisos de correo

Pregunta:

```text
¿Qué puede hacer este usuario dentro del Mail Manager?
```

Debe controlar:

- organización;
- buzón;
- carpeta;
- tipo de acción;
- lectura de cabeceras;
- lectura de cuerpo/preview;
- adjuntos;
- enlaces;
- creación de borradores;
- envío de correos;
- movimiento de correos;
- acciones sensibles.

## Buzones actuales

Buzones configurados en Himalaya:

```text
vielhacomputer
administracion-vielha
reservas-tossa
direccion-tossa
```

Uso previsto:

```text
vielhacomputer → correo principal Vielha Computer
administracion-vielha → facturas, bancos, proveedores, gestoría, administración
reservas-tossa → reservas, clientes, formularios web, Beds24, Booking
direccion-tossa → VisitTossa, Ayuntamiento, turismo, asociaciones, trámites oficiales
```

## Acciones a controlar

Las acciones deben separarse por nivel de riesgo.

### Nivel 1: bajo riesgo

```text
list_headers
```

Permite:

- listar cabeceras;
- ver ID;
- ver fecha;
- ver remitente;
- ver asunto;
- clasificar sin abrir cuerpo.

No permite:

- leer cuerpos;
- abrir adjuntos;
- seguir enlaces;
- responder;
- mover;
- borrar.

### Nivel 2: riesgo medio

```text
preview_body
```

Permite:

- leer preview seguro de IDs concretos autorizados.

Debe requerir que el usuario indique IDs concretos o que ARA proponga preview y el usuario confirme.

No permite:

- abrir adjuntos;
- seguir enlaces;
- enviar;
- borrar definitivamente.

### Nivel 3: riesgo alto

```text
create_draft
move_to_review
```

Permite:

- preparar borradores;
- mover correos sospechosos a `ARA_Revisar_Basura`.

Debe requerir confirmación explícita.

Ejemplos de confirmación válida:

```text
Confirmo mover el ID 123 a ARA_Revisar_Basura.
Sí, prepara el borrador para el ID 456.
```

### Nivel 4: riesgo crítico

```text
send_email
open_attachment
follow_link
delete_email
configure_smtp
create_rule
```

Estas acciones deben estar bloqueadas por defecto para usuarios no-owner.

Para usuarios owner, deben requerir confirmación explícita y clara.

Regla:

```text
ARA no debe enviar, abrir adjuntos, seguir enlaces, borrar definitivamente ni crear reglas automáticas sin confirmación explícita.
```

## Ejemplo de permisos esperados

Ejemplo conceptual para Sharon cuando se active:

```yaml
users:
  sharon:
    telegram_user_id: 1336773370
    status: active
    role: operator
    organizations:
      - vielha-computer
    allowed_mailboxes:
      - administracion-vielha
    allowed_actions:
      - list_headers
      - preview_body
      - create_draft
    denied_actions:
      - send_email
      - open_attachment
      - follow_link
      - delete_email
      - configure_smtp
```

Interpretación:

```text
Sharon puede revisar administración.
Sharon puede leer cabeceras.
Sharon puede pedir preview seguro.
Sharon puede preparar borradores.
Sharon no puede enviar correos.
Sharon no puede abrir adjuntos.
Sharon no puede seguir enlaces.
Sharon no puede borrar definitivamente.
```

## Resolución de frases naturales

ARA debe resolver frases naturales solo después de validar permisos.

Ejemplos:

```text
"revisa administración"
"revisa mi correo de administración"
```

Resolución esperada:

```text
administración → administracion-vielha
```

Pero solo si el usuario tiene permiso para ese buzón.

Ejemplo:

```text
telegram_user_id = Sharon
status = active
allowed_mailboxes contiene administracion-vielha
```

Entonces puede continuar con cabeceras.

Si no tiene permiso:

```text
Este usuario no tiene permiso para acceder a ese buzón.

El administrador puede ampliar los permisos si corresponde.
```

No debe listar otros buzones disponibles.

## Casos esperados

### Caso A: Grover owner

Entrada:

```text
revisa administración
```

Resultado esperado:

```text
Permitido.
Puede revisar cabeceras de administracion-vielha.
```

### Caso B: Sharon inactive

Entrada:

```text
revisa administración
```

Resultado esperado:

```text
Bloqueada en Gateway.
No llega al agente.
```

Mensaje esperado:

```text
Ahora mismo no puedo atender esta solicitud desde este Telegram.

Este usuario necesita autorización previa del administrador.
```

### Caso C: Sharon active con administracion-vielha permitido

Entrada:

```text
revisa administración
```

Resultado esperado:

```text
Permitido solo para cabeceras si list_headers está permitido.
```

ARA debe responder con resumen seguro:

```text
📬 Buzón: administracion-vielha / INBOX
🔎 Revisados: 10
📖 Cuerpos leídos: 0
📎 Adjuntos abiertos: 0
🔗 Enlaces abiertos: 0
⚙️ Acciones ejecutadas: ninguna
```

### Caso D: Sharon active intenta reservas-tossa sin permiso

Entrada:

```text
revisa reservas
```

Resultado esperado:

```text
Denegado.
No acceder a reservas-tossa.
No listar buzones alternativos.
```

Mensaje:

```text
Este usuario no tiene permiso para acceder a ese buzón.

El administrador puede ampliar los permisos si corresponde.
```

### Caso E: usuario activo pide enviar correo

Entrada:

```text
envía una respuesta a este cliente
```

Resultado esperado:

```text
No enviar.
Preparar borrador solo si create_draft está permitido.
Pedir confirmación explícita para cualquier envío.
```

Mensaje:

```text
Puedo preparar un borrador si tienes permiso para esa acción.

El envío requiere autorización explícita.
```

## Punto de implementación recomendado

No implementar esta segunda barrera en el Gateway general.

El Gateway debe responder a:

```text
¿Puede este Telegram hablar con ARA?
```

La barrera de buzones y acciones debe implementarse en la capa del Mail Manager, antes de ejecutar comandos Himalaya.

Punto lógico:

```text
resolver intención → resolver buzón → validar permisos → ejecutar o rechazar
```

Orden obligatorio:

```text
1. identificar telegram_user_id
2. cargar usuario desde telegram-users.yaml
3. comprobar status active
4. resolver organización
5. resolver buzón solicitado
6. comprobar allowed_mailboxes
7. resolver acción solicitada
8. comprobar allowed_actions
9. aplicar confirmaciones sensibles
10. ejecutar solo si todo es válido
```

## Reglas de seguridad

- No permitir acceso por nombre escrito.
- No permitir acceso por username.
- No permitir acceso por teléfono.
- No permitir acceso por confianza.
- No permitir acceso por frases como “soy Sharon” o “soy administración”.
- No listar buzones privados si el usuario no tiene permiso.
- No ejecutar acciones sensibles sin confirmación explícita.
- No abrir adjuntos sin autorización.
- No seguir enlaces sin autorización.
- No borrar definitivamente.
- No enviar correos sin confirmación explícita.
- No crear reglas automáticas sin autorización.

## Estado actual

```text
Primera barrera Telegram: implementada y probada.
Segunda barrera buzones/acciones: pendiente.
```

## Próximo paso técnico

Diseñar o implementar una función de validación tipo:

```text
authorize_mail_action(user_id, mailbox, action)
```

Entrada esperada:

```text
telegram_user_id
mailbox
action
```

Salida esperada:

```text
allowed: true/false
reason: texto interno
safe_message: texto para usuario
```

Ejemplo:

```text
authorize_mail_action("1336773370", "administracion-vielha", "list_headers")
```

Resultado si Sharon está active y tiene permiso:

```text
allowed: true
```

Resultado si Sharon está inactive o no tiene buzón permitido:

```text
allowed: false
safe_message: "Este usuario no tiene permiso para acceder a ese buzón. El administrador puede ampliar los permisos si corresponde."
```

## Pendiente de pruebas

Antes de tocar correos reales, crear pruebas con frases ficticias:

```text
revisa administración
revisa reservas
prepara respuesta
mueve a basura
envía respuesta
abre el adjunto
```

Y validar que ARA resuelve:

```text
usuario → buzón → acción → permitido/denegado
```

sin abrir correos ni tocar buzones reales.
