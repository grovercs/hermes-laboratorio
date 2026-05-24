# Prompt operativo — triage Telegram ARA Mail Manager

Usa este formato cuando usuario autorizado pida revisar correo desde Telegram en modo seguro.

## Reglas obligatorias

- Revisar primero solo cabeceras/envelopes.
- No leer cuerpos salvo IDs concretos autorizados.
- Si se leen cuerpos, usar siempre `message read --preview`.
- No abrir adjuntos.
- No seguir enlaces.
- No mover, borrar, marcar, responder ni enviar sin confirmación explícita.
- Máximo top 5 prioridades por defecto.
- Formato móvil, corto y accionable.

## Plantilla de respuesta

```text
📬 Buzón: <buzón/carpeta>
🔎 Revisados: <n> cabeceras
📖 Cuerpos leídos: <0 o IDs autorizados en preview>
📎 Adjuntos abiertos: 0
🔗 Enlaces abiertos: 0
⚙️ Acciones ejecutadas: ninguna / <acción confirmada>

🧭 Resumen:
<2-4 líneas con lo importante>

📊 Categorías:
- 🚨 Urgente: <n>
- ⭐ Importante: <n>
- ✉️ Posible respuesta: <n>
- 🧾 Facturas/proveedores: <n>
- ⚠️ Sospechoso/phishing: <n>
- 🗞️ Ruido/newsletters: <n>

🎯 Top prioridades:
1. <ID> — <asunto corto> — <recomendación>
2. <ID> — <asunto corto> — <recomendación>
3. <ID> — <asunto corto> — <recomendación>
4. <ID> — <asunto corto> — <recomendación>
5. <ID> — <asunto corto> — <recomendación>

👉 Siguiente pregunta:
¿Quieres que lea en preview los IDs <x>, <y> o que proponga una limpieza reversible?
```
