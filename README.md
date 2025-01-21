# Link Analyzer

![Link Analyzer Banner](https://via.placeholder.com/800x200.png?text=Link+Analyzer)

## ⭐ Proyecto Destacado: link_analizer

Este proyecto, creado por [x3089](https://github.com/x3089), es una herramienta de línea de comandos para analizar enlaces (URLs). Su objetivo es identificar posibles riesgos asociados con links, como phishing, malware o configuraciones de servidor sospechosas.

### Características principales:
1. **Análisis exhaustivo del enlace:**
   - Verifica el código de estado HTTP.
   - Inspecciona encabezados de respuesta HTTP.
   - Busca patrones maliciosos comunes.
2. **Sistema de clasificación de riesgos:**
   - **[92mSEGURO[0m**: El enlace no muestra signos de riesgo.
   - **[93mSOSPECHOSO[0m**: Indicios leves de posible riesgo.
   - **[91mCRÍTICO[0m**: El enlace tiene indicadores graves de ser malicioso.
3. **Fácil de usar:** Copia y pega cualquier enlace para obtener información detallada en segundos.

## Instalación

Sigue estos pasos para instalar y ejecutar Link Analyzer:

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/x3089/link_analyzer.git
   cd link_analyzer
   ```

2. **Configurar el entorno:**

   Es recomendable usar un entorno virtual:

   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. **Instalar las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

   Nota: El archivo `requirements.txt` contiene las librerías necesarias como `requests`.

4. **Ejecutar la herramienta:**

   ```bash
   python link_analyzer_tool.py
   ```

## Uso

1. Ejecuta el programa y pega el enlace que deseas analizar:

   ```plaintext
 █████  ███████ ████████ ██████   █████  
██   ██ ██         ██    ██   ██ ██   ██ 
███████ ███████    ██    ██████  ███████ 
██   ██      ██    ██    ██   ██ ██   ██ 
██   ██ ███████    ██    ██   ██ ██   ██ 
                                                                              
   PEGA EL LINK AQUI: (link por examinar)
   ```

2. Revisa la salida detallada, que incluirá:
   - **Código de estado HTTP.**
   - **Encabezados de respuesta.**
   - **Clasificación de riesgo (SEGURO, SOSPECHOSO, CRÍTICO).**

### Ejemplo:

```plaintext
[INFO] Análisis del link:
- Código HTTP: 403
- Encabezados de respuesta: {...}
[93m[SOSPECHOSO] El link devolvió un código HTTP indicando un posible problema del cliente.[0m
```

## Contribuciones

1. Realiza un fork del repositorio.
2. Crea una nueva rama:

   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```

3. Realiza tus cambios y envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---
**Hecho con ❤ por [x3089](https://github.com/x3089)**

