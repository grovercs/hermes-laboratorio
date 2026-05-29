# Mejora Mail Manager - Carpeta ARA_Revisar_Basura

Fecha: 2026-05-29

## Contexto

La cuenta `vielhacomputer` ya tenía creada la carpeta:

    ARA_Revisar_Basura

Esta carpeta se usa como zona de revisión segura para correos sospechosos, basura, phishing o mensajes que ARA recomiende apartar sin borrar definitivamente.

Al revisar los nuevos buzones se comprobó que no existía en:

    reservas-tossa
    direccion-tossa

## Acción realizada

Se creó la carpeta `ARA_Revisar_Basura` en:

    reservas-tossa
    direccion-tossa

Comandos usados:

    himalaya folder add --account reservas-tossa ARA_Revisar_Basura
    himalaya folder add --account direccion-tossa ARA_Revisar_Basura

## Verificación

Comando:

    himalaya folder list --account reservas-tossa

Resultado:

    ARA_Revisar_Basura
    Borradores
    Elementos enviados
    INBOX
    Papelera
    Spam

Comando:

    himalaya folder list --account direccion-tossa

Resultado:

    ARA_Revisar_Basura
    Borradores
    Elementos enviados
    INBOX
    Papelera
    Spam

## Regla operativa

ARA puede recomendar mover correos sospechosos a `ARA_Revisar_Basura`, pero no debe moverlos sin confirmación explícita.

No borrar definitivamente.

No usar expunge salvo confirmación explícita.

## Uso previsto

Mover de forma reversible:

    - phishing probable
    - spam dudoso
    - boletines irrelevantes
    - falsos bancos/proveedores
    - correos sospechosos que Grover quiera revisar después

## Cuentas con carpeta creada

    vielhacomputer
    reservas-tossa
    direccion-tossa
