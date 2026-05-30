@'

\# Enforcement real de permisos Telegram con TELEGRAM\_USERS\_CONFIG



Proyecto: ARA Mail Manager / Hermes / Himalaya  

Estado: aplicado y probado en instalación local de Hermes



\## Resumen



Se aplicó un parche local en Hermes Gateway para validar usuarios de Telegram usando:



```text

mail-manager-lab/config/telegram-users.yaml

```



La validación se realiza antes de que el mensaje llegue al agente ARA.



El Gateway autoriza únicamente usuarios con:



```text

telegram\_user\_id numérico + status: active

```



No autoriza por nombre, username, teléfono, rol ni frases en lenguaje natural.



\## Archivo modificado



El parche se aplicó fuera de este repo, en la instalación real de Hermes:



```text

C:\\Users\\Usuario\\AppData\\Local\\hermes\\hermes-agent\\gateway\\run.py

```



Estado observado en el repo de Hermes:



```text

M gateway/run.py

```



No se hizo commit en `hermes-agent` porque ese repo ya tenía muchos archivos modificados de origen.



\## Backups creados



```text

C:/Users/Usuario/AppData/Local/hermes/hermes-agent/gateway/run.py.bak-telegram-users-config-20260530-213720

```



```text

C:/Users/Usuario/AppData/Local/hermes/hermes-agent/gateway/run.py.bak-unauthorized-telegram-dm-message-20260530-214736

```



\## Variable activa en .env



En:



```text

C:\\Users\\Usuario\\AppData\\Local\\hermes\\.env

```



se añadió:



```env

TELEGRAM\_USERS\_CONFIG=C:/proyectos/hermes-laboratorio/mail-manager-lab/config/telegram-users.yaml

```



\## Cambios aplicados



1\. Se añadió un helper fail-closed para leer `TELEGRAM\_USERS\_CONFIG`.

2\. Se integró en `GatewayRunner.\_is\_user\_authorized()`.

3\. Solo añade al allowlist usuarios Telegram con `status: active`.

4\. Para Telegram DM no autorizado, el Gateway responde con mensaje fijo profesional.

5\. El mensaje no pasa al agente y no toca correos.



Mensaje para usuarios no autorizados:



```text

Ahora mismo no puedo atender esta solicitud desde este Telegram.



Este usuario necesita autorización previa del administrador.

```



\## Pruebas realizadas



\### Helper local



Comando ejecutado:



```powershell

$env:TELEGRAM\_USERS\_CONFIG = "C:/proyectos/hermes-laboratorio/mail-manager-lab/config/telegram-users.yaml"



\& "C:\\Users\\Usuario\\AppData\\Local\\hermes\\hermes-agent\\venv\\Scripts\\python.exe" -c "from gateway.run import \_telegram\_users\_config\_allowed\_ids; print(\_telegram\_users\_config\_allowed\_ids())"

```



Resultado:



```text

{'5703152430'}

```



Interpretación:



\- Grover aparece como activo.

\- Sharon no aparece porque está `inactive`.



\### Prueba Telegram



Resultado:



```text

Grover active → autorizado.

Sharon inactive → bloqueada antes de llegar al agente.

```



Sharon recibió:



```text

Ahora mismo no puedo atender esta solicitud desde este Telegram.



Este usuario necesita autorización previa del administrador.

```



El Gateway registró:



```text

WARNING gateway.run: Unauthorized user: 1336773370 (Sharon Silva) on telegram

```



\## Estado actual



```text

Gateway: funcionando

TELEGRAM\_USERS\_CONFIG: activo

Grover: active / owner / autorizado

Sharon: inactive / bloqueada

Mensaje profesional a no autorizados: funcionando

Correos: no se tocaron durante estas pruebas

```



\## Pendiente



Este parche solo responde a:



```text

¿Puede este Telegram hablar con ARA?

```



Todavía falta implementar:



```text

¿Qué buzones y acciones puede usar cada usuario autorizado?

```



Pendiente de enforcement por:



\- organización;

\- buzón;

\- acción;

\- confirmaciones sensibles;

\- adjuntos;

\- envío de respuestas;

\- movimiento a `ARA\_Revisar\_Basura`.



\## Rollback



Para desactivar este enforcement sin tocar código, comentar o quitar en `.env`:



```env

TELEGRAM\_USERS\_CONFIG=C:/proyectos/hermes-laboratorio/mail-manager-lab/config/telegram-users.yaml

```



y reiniciar Gateway.



Para revertir código, restaurar uno de los backups de `gateway/run.py`.

'@ | Set-Content -Path "docs\\enforcement-telegram-users-config.md" -Encoding UTF8

