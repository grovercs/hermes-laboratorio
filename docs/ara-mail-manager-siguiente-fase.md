# ARA Mail Manager — siguiente fase operativa

Documento corto para continuar el trabajo después del contexto operativo inicial.

## 1. Punto de partida confirmado

- Repo laboratorio: `C:\proyectos\hermes-laboratorio`.
- Estado Git antes de este documento: `main` sincronizado con `origin/main`, sin cambios pendientes.
- Documento base leído: `docs/ara-mail-manager-contexto-operativo.md`.
- Buzón real validado: `info@vielhacomputer.com` mediante cuenta Himalaya `vielhacomputer`.
- Modo actual: IMAP / lectura y triage seguro bajo supervisión.
- No se han tocado secretos ni se ha leído contenido privado de correos para preparar esta fase.

## 2. Diagnóstico técnico no secreto

### ARA principal

Ruta de configuración esperada:

```text
C:\Users\Usuario\AppData\Local\hermes\config.yaml
```

Resumen no secreto observado:

- Modelo principal: `gpt-5.5`.
- Provider principal: `openai-codex`.
- Context length configurado: `272000`.
- Compresión habilitada.
- `compression.threshold`: `0.75`.
- `compression.target_ratio`: `0.2`.
- `auxiliary.compression.timeout`: `600`.
- `auxiliary.compression.context_length`: `272000`.
- `context.engine`: `compressor`.
- Delegación sin modelo/proveedor específico configurado; hereda por defecto si no se define otra cosa.

Interpretación práctica:

- La ventana real operativa de esta instalación se debe tratar como unos `272K` tokens, no como la ventana teórica de otro proveedor/modelo.
- Con `threshold` a `0.75`, la compresión debería activarse más tarde que con el valor anterior típico de `0.50`.
- El timeout de compresión ya está alto (`600`), útil para evitar bloqueos por resúmenes largos.

### ARA Lab

Ruta revisada:

```text
C:\proyectos\hermes\instances\ara-lab
```

Hallazgo no secreto:

- No aparece `config.yaml` en la raíz de `ara-lab`.
- Sí existen archivos de estado, logs, skills y `SOUL.md`.

Interpretación práctica:

- `ara-lab` existe como instancia/casa de Hermes, pero no tiene configuración de modelo/proveedor validada en un `config.yaml` propio.
- Antes de usar `ara-lab` para pruebas de modelos, fallback o automatización, hay que decidir si se inicializa una configuración propia o si se mantiene como laboratorio sin credenciales.
- No se deben copiar `.env`, `auth.json` ni secretos desde ARA principal sin un plan explícito.

## 3. Decisión recomendada para la siguiente fase

Siguiente fase recomendada: convertir el flujo probado en un protocolo operativo mínimo, antes de automatizar más.

Orden propuesto:

1. Mantener el buzón `vielhacomputer` como caso piloto.
2. Crear plantillas no secretas para:
   - perfil de buzón,
   - permisos,
   - carpetas seguras,
   - formato de triage Telegram,
   - registro de acciones aprobadas.
3. Definir comandos manuales validados, sin envolver todavía en scripts destructivos.
4. Probar una segunda sesión de triage solo por cabeceras.
5. Si Grover autoriza, probar preview de IDs concretos.
6. No configurar SMTP hasta que haya una fase separada y confirmada.

## 4. Estructura mínima sugerida dentro del laboratorio

Sin secretos:

```text
mail-manager-lab/
├── clients/
│   └── grover/
│       ├── mailboxes.example.yaml
│       ├── permissions.example.yaml
│       ├── folders.example.yaml
│       └── style_profile.example.md
├── prompts/
│   ├── triage-telegram.md
│   └── borrador-respuesta.md
└── audit/
    └── acciones-aprobadas.example.csv
```

Notas:

- Usar `.example.*` mientras sea documentación o plantilla.
- No guardar cuerpos completos de correos.
- No guardar direcciones privadas de clientes salvo las ya documentadas y autorizadas para el piloto.
- No guardar credenciales, tokens, contraseñas ni contenidos de `.env`.

## 5. Permisos piloto recomendados

Para `grover / vielhacomputer`:

Permitido por defecto:

- Listar carpetas.
- Listar cabeceras/envelopes.
- Clasificar por remitente, asunto, fecha y metadatos.
- Proponer acciones.

Permitido solo con confirmación explícita:

- Leer preview de IDs concretos con `--preview`.
- Mover correos a `ARA_Revisar_Basura`.
- Crear carpetas de revisión.
- Preparar borradores de respuesta.

Prohibido por defecto:

- Borrado definitivo.
- Cambiar flags leído/no leído.
- Abrir o descargar adjuntos.
- Seguir enlaces.
- Enviar correos.
- Configurar SMTP.
- Crear reglas automáticas.

## 6. Comandos manuales validados como referencia

Listar cabeceras:

```bash
himalaya envelope list --account vielhacomputer --folder INBOX --page 1 --page-size 20
```

Preview seguro de un ID autorizado:

```bash
himalaya message read --account vielhacomputer --folder INBOX --preview <ID>
```

Mover a revisión, solo tras confirmación explícita:

```bash
himalaya message move --account vielhacomputer --folder INBOX ARA_Revisar_Basura <ID1> <ID2>
```

Verificación posterior:

```bash
himalaya envelope list --account vielhacomputer --folder ARA_Revisar_Basura --page 1 --page-size 10
himalaya envelope list --account vielhacomputer --folder INBOX --page 1 --page-size 30
```

## 7. Checklist antes de cualquier acción real de correo

Antes de preview:

- Confirmar buzón.
- Confirmar carpeta origen.
- Confirmar IDs concretos.
- Confirmar que se usará `--preview`.
- Confirmar que no se abrirán adjuntos ni enlaces.

Antes de mover:

- Confirmar carpeta destino existente.
- Confirmar que los IDs siguen en la carpeta origen.
- Mostrar comando exacto.
- Esperar confirmación explícita final de Grover.
- Ejecutar solo los IDs confirmados.
- Relistar origen y destino.

Antes de responder/enviar:

- No ejecutar SMTP todavía.
- Preparar solo borrador visible.
- Pedir confirmación de texto final.
- Envío real queda fuera de fase actual.

## 8. Pendientes concretos

1. Decidir si crear la carpeta `mail-manager-lab/` con plantillas `.example.*`.
2. Definir formato exacto de `mailboxes.example.yaml`.
3. Definir formato exacto de `permissions.example.yaml`.
4. Definir formato de auditoría mínima sin datos sensibles.
5. Definir prompt estable de triage Telegram.
6. Decidir si `ara-lab` debe tener `config.yaml` propio o seguir sin configuración de proveedor.
7. Investigar fallback de proveedor/modelo solo después de resolver la separación de instancias.
8. Mantener SMTP fuera hasta orden explícita.

## 9. Siguiente paso recomendado

Crear las plantillas no secretas del punto 8, empezando por:

- `mail-manager-lab/clients/grover/mailboxes.example.yaml`
- `mail-manager-lab/clients/grover/permissions.example.yaml`
- `mail-manager-lab/clients/grover/folders.example.yaml`
- `mail-manager-lab/prompts/triage-telegram.md`
- `mail-manager-lab/audit/acciones-aprobadas.example.csv`

No crear scripts que muevan o borren correos todavía. Primero plantillas, después comandos manuales revisados, y solo al final automatización limitada.
