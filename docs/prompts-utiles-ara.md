# Prompts útiles para ARA

Este documento contiene prompts listos para copiar y pegar al trabajar con ARA.

Objetivo: trabajar de forma clara, práctica y segura, evitando modificar archivos reales sin revisión previa y sin exponer secretos.

Regla general: no pegar contraseñas, tokens, claves API, archivos `.env`, `auth.json`, `config.yaml`, sesiones, logs privados ni credenciales en los prompts.

---

## 1. Revisar una carpeta sin modificar nada

```text
ARA, revisa la carpeta actual sin modificar nada.

Quiero que me digas:
1. En qué carpeta estás.
2. Qué archivos y carpetas principales ves.
3. Si parece un proyecto Git, Node, WordPress, Laravel, React/Vite u otro tipo.
4. Qué archivos importantes detectas.
5. Qué precauciones tomarías antes de tocar nada.

No crees, borres ni modifiques archivos.
```

---

## 2. Revisar estado Git antes de trabajar

```text
ARA, antes de trabajar en este proyecto, revisa el estado de Git.

Ejecuta:
1. pwd
2. git status
3. git branch --show-current
4. git remote -v

Después dime:
- En qué carpeta estamos.
- En qué rama estamos.
- Si hay cambios pendientes.
- Si hay archivos sin seguimiento.
- Si parece seguro continuar.

No modifiques archivos todavía.
```

---

## 3. Analizar un proyecto React/Vite

```text
ARA, analiza este proyecto React/Vite sin modificar nada.

Quiero que revises:
1. Estructura principal del proyecto.
2. package.json.
3. Scripts disponibles.
4. Carpeta src.
5. Componentes principales.
6. Si usa Supabase, Netlify, rutas, autenticación o variables de entorno.

No leas ni muestres valores de .env.
No modifiques archivos.
Al final, dame un resumen claro de cómo está organizado y qué pasos recomiendas antes de hacer cambios.
```

---

## 4. Analizar errores de `npm run build`

```text
ARA, necesito analizar un error de npm run build.

Primero revisa:
1. Carpeta actual.
2. git status.
3. package.json.

Después ejecuta:
npm run build

Si falla, explícame:
- Qué error aparece.
- En qué archivo o línea parece estar el problema.
- Por qué ocurre probablemente.
- Qué cambio recomiendas.

No modifiques archivos hasta explicarme el diagnóstico y pedirme confirmación.
```

---

## 5. Trabajar con Hotel Daily Control - Tossa

```text
ARA, vamos a trabajar en Hotel Daily Control - Tossa.

Ruta habitual del proyecto:
C:\Proyectos\antigravity\hoteles-tossa\hoteles-tossa-mvp\hoteles-tossa

Antes de tocar nada:
1. Confirma que estás en esa carpeta.
2. Ejecuta git status.
3. Revisa qué rama está activa.
4. Comprueba si hay cambios pendientes.

Después dime qué ves y espera mi confirmación antes de modificar archivos.

Recuerda:
- El proyecto es React/Vite.
- Normalmente se modifica src\App.jsx.
- Hay que ejecutar npm run build antes de subir cambios.
- Netlify despliega automáticamente desde GitHub.
- No tocar .env ni claves de Supabase.
```

---

## 6. Trabajar con WordPress / WooCommerce / Elementor

```text
ARA, necesito ayuda con un proyecto WordPress/WooCommerce/Elementor.

Antes de proponer cambios, ayúdame a revisar:
1. Qué problema concreto hay.
2. Si afecta a frontend, backend, plugin, tema, WooCommerce, Elementor o servidor.
3. Qué versión de WordPress/PHP/plugin podría estar relacionada.
4. Si conviene hacer copia de seguridad antes.

No propongas tocar base de datos ni archivos críticos sin advertirme.
No me pidas contraseñas ni credenciales.
Dame pasos seguros y prácticos para diagnosticar primero.
```

---

## 7. Revisar problemas SEO

```text
ARA, revisa este problema SEO de forma práctica.

Quiero que analices:
1. Página o sección afectada.
2. Títulos y metadescripciones.
3. Estructura H1/H2/H3.
4. Slugs y enlaces internos.
5. Indexación y sitemap si aplica.
6. Contenido duplicado o pobre.
7. Recomendaciones de mejora priorizadas.

No inventes datos.
Si necesitas que te pase una URL o texto, pídemelo.
Dame una lista de acciones concretas y ordenadas por impacto.
```

---

## 8. Crear documentación técnica

```text
ARA, crea documentación técnica clara sobre este tema/proyecto.

Estructúrala así:
1. Objetivo.
2. Situación actual.
3. Solución propuesta.
4. Requisitos.
5. Pasos de instalación o configuración.
6. Pruebas de funcionamiento.
7. Riesgos o precauciones.
8. Mantenimiento recomendado.

Usa un tono profesional, claro y fácil de entender.
No incluyas contraseñas, tokens, claves API ni credenciales.
Si falta información, marca los puntos como pendiente de confirmar.
```

---

## 9. Preparar presupuestos o informes técnicos

```text
ARA, ayúdame a preparar un presupuesto o informe técnico para un cliente.

Quiero que tenga esta estructura:
1. Introducción.
2. Necesidad detectada.
3. Solución propuesta.
4. Materiales o servicios incluidos.
5. Trabajos a realizar.
6. Ventajas para el cliente.
7. Condiciones o exclusiones.
8. Próximos pasos.

Usa tono profesional y convincente.
No inventes precios si no te los doy.
Si faltan datos, indícalos claramente como pendientes.
```

---

## 10. Trabajar con redes, MikroTik, UniFi y VPN

```text
ARA, necesito ayuda con redes, MikroTik, UniFi o VPN.

Primero ayúdame a ordenar la información:
1. Objetivo de la red.
2. Equipos implicados.
3. Rangos IP.
4. VLANs si existen.
5. WAN/Internet disponible.
6. VPN o acceso remoto.
7. Problema actual.
8. Pruebas realizadas.

No propongas cambios destructivos en firewall, NAT, rutas o VPN sin advertirme.
Antes de aplicar cambios reales, dame un plan paso a paso y cómo volver atrás si algo falla.
```

---

## 11. Revisar que no se suban secretos

```text
ARA, revisa que no se vayan a subir secretos antes de hacer commit o push.

Ejecuta:
1. git status
2. git diff --stat
3. git diff --name-only

Comprueba que no aparezcan:
- .env
- *.env
- auth.json
- config.yaml
- logs/
- sessions/
- pairing/
- memories/
- tokens
- claves API
- credenciales

No muestres valores sensibles si los encuentras.
Si detectas algo sospechoso, para y explícame qué archivo hay que excluir o revisar.
```

---

## 12. Hacer commit seguro

```text
ARA, quiero hacer un commit seguro.

Antes de hacer commit:
1. Ejecuta git status.
2. Muestra qué archivos han cambiado.
3. Revisa que no haya secretos ni archivos sensibles.
4. Muestra un resumen de git diff --stat.
5. Dime qué comando git add vas a usar.

No hagas commit hasta que yo confirme.
Cuando confirme, usa un mensaje de commit claro y concreto.
```

---

## 13. Hacer push solo con confirmación

```text
ARA, prepara el push pero no lo hagas todavía.

Antes de subir:
1. Ejecuta git status.
2. Confirma rama actual.
3. Confirma remoto origin.
4. Confirma último commit con git log --oneline -1.
5. Confirma que no hay archivos sensibles pendientes.

Después dime si está todo listo.
No ejecutes git push hasta que yo diga claramente: puedes hacer push.
```

---

## 14. Crear copia de seguridad segura

```text
ARA, quiero crear una copia de seguridad segura.

Antes de copiar nada:
1. Dime qué carpeta o archivo se va a copiar.
2. Dime dónde se guardará la copia.
3. Revisa si puede contener secretos.
4. Excluye .env, auth.json, config.yaml, logs, sessions, tokens, claves API y credenciales.
5. Si el backup se va a subir a GitHub, revisa primero .gitignore y git status.

No hagas la copia hasta explicar el plan y recibir confirmación si hay riesgo de datos sensibles.
```

---

## Prompt base para tareas delicadas

```text
ARA, esta tarea puede afectar a archivos reales.

Trabaja con protocolo seguro:
1. Confirma carpeta actual.
2. Ejecuta git status si hay Git.
3. No toques secretos ni credenciales.
4. Explica qué archivos vas a modificar.
5. Haz cambios pequeños.
6. Prueba build o tests si existen.
7. Muestra git diff antes de commit.
8. No hagas commit ni push sin mi confirmación.
9. Si hay errores, para y explica.
```
