\# Telegram audio STT con OpenAI Whisper



Proyecto: ARA Mail Manager / Hermes / Himalaya  

Estado: probado correctamente



\## Resumen



Se habilitó la transcripción de audios recibidos por Telegram usando OpenAI Whisper desde Hermes.



La prueba final confirmó que ARA ya puede recibir un audio por Telegram, transcribirlo y responder en función del contenido hablado.



\## Situación anterior



La configuración de STT estaba activa, pero usando proveedor local:



```yaml

stt:

&#x20; enabled: true

&#x20; provider: local

&#x20; local:

&#x20;   model: base

&#x20;   language: ''

&#x20; openai:

&#x20;   model: whisper-1

