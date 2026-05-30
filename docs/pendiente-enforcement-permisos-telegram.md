\# Pendiente: enforcement real de permisos Telegram



Proyecto: ARA Mail Manager / Hermes / Himalaya

Estado: pendiente crítico antes de autorizar usuarios no-owner en Telegram



\## Resumen



Actualmente existen dos capas relacionadas con Telegram:



1\. `TELEGRAM\_ALLOWED\_USERS`

2\. `mail-manager-lab/config/telegram-users.yaml`



Pero no cumplen la misma función.



\## Capa 1: TELEGRAM\_ALLOWED\_USERS



Archivo:



```text

C:\\Users\\Usuario\\AppData\\Local\\hermes\\.env

```



Variable:



```env

TELEGRAM\_ALLOWED\_USERS=...

```



Función actual:



\* Controla qué usuarios pueden hablar técnicamente con el bot de Telegram.

\* Si un usuario no está en esta lista, el Gateway no procesa su mensaje.

\* El usuario puede escribir al bot, pero ARA no responde.



Estado actual seguro:



```env

TELEGRAM\_ALLOWED\_USERS=solo Grover

```



\## Capa 2: telegram-users.yaml



Archivo local real:



```text

mail-manager-lab/config/telegram-users.yaml

```



Plantilla versionada:



```text

mail-manager-lab/config/telegram-users.example.yaml

```



Función prevista:



\* Definir usuarios autorizados.

\* Definir estado activo/inactivo.

\* Definir rol.

\* Definir organización.

\* Definir buzones permitidos.

\* Definir acciones permitidas.



Ejemplo previsto:



```text

telegram\_user\_id → usuario → estado → rol → organización → buzones permitidos → acciones permitidas

```



\## Hallazgo de la prueba con Sharon



Durante la prueba, se añadió temporalmente el Telegram ID de Sharon a `TELEGRAM\_ALLOWED\_USERS`.



Resultado observado:



\* Sharon pudo hablar con ARA.

\* ARA respondió desde el Telegram de Sharon.

\* ARA llegó a revisar correos de `administracion-vielha`.

\* Esto ocurrió aunque Sharon estaba marcada como `inactive` en `telegram-users.yaml`.



Conclusión:



```text

telegram-users.yaml todavía no se está aplicando técnicamente como barrera real.

```



\## Riesgo



No se debe añadir ningún usuario no-owner a `TELEGRAM\_ALLOWED\_USERS` hasta implementar una validación real de permisos.



Si se añade un usuario a `TELEGRAM\_ALLOWED\_USERS`, actualmente ese usuario puede llegar a pedir acciones a ARA sin que `telegram-users.yaml` lo bloquee técnicamente.



\## Estado actual recomendado



Mantener:



```env

TELEGRAM\_ALLOWED\_USERS=solo Grover

```



Mantener a usuarios como Sharon en `telegram-users.yaml` como:



```yaml

status: "inactive"

```



hasta que exista enforcement real.



\## Comportamiento deseado futuro



El comportamiento correcto debería ser:



1\. Usuario escribe al bot.

2\. Gateway deja pasar el mensaje solo hasta una capa de validación.

3\. ARA lee `telegram-users.yaml`.

4\. ARA comprueba:



&#x20;  \* Telegram ID.

&#x20;  \* Estado.

&#x20;  \* Rol.

&#x20;  \* Organización.

&#x20;  \* Buzones permitidos.

&#x20;  \* Acciones permitidas.

5\. Si el usuario está inactivo o no autorizado, ARA responde de forma profesional.

6\. Si el usuario está autorizado, ARA permite solo las acciones asignadas.



\## Respuesta deseada para usuario no autorizado



Ejemplo:



```text

Ahora mismo no puedo revisar ese buzón desde este Telegram.



Este usuario necesita autorización previa del administrador.

```



\## Regla crítica



Hasta implementar enforcement real:



```text

No añadir usuarios no-owner a TELEGRAM\_ALLOWED\_USERS.

```



\## Próximo trabajo técnico



Implementar una barrera previa que lea:



```text

mail-manager-lab/config/telegram-users.yaml

```



antes de permitir cualquier acción sobre correo.



La validación debe ocurrir antes de:



\* listar cabeceras,

\* leer previews,

\* abrir adjuntos,

\* seguir enlaces,

\* mover correos,

\* crear borradores,

\* enviar respuestas.



\## Nota de seguridad



La prueba con Sharon fue útil y confirmó el diseño pendiente, pero también demostró que la seguridad todavía depende de `TELEGRAM\_ALLOWED\_USERS`, no del YAML de permisos.



Por tanto, el sistema debe considerarse seguro solo mientras `TELEGRAM\_ALLOWED\_USERS` contenga únicamente usuarios completamente autorizados.



