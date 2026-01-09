## Proyecto Libere - Reto06 Amarillo
Este repositorio contiene el desarrollo íntegro del Reto 06, donde se realiza un flujo completo de análisis de datos, enriquecimiento mediante API, técnicas de clustering, modelado, scraping, NLP y creación de índices para uso en Kibana. El objetivo principal del proyecto es organizar y automatizar todo el proceso, asegurando trazabilidad, orden y correcta gestión de los datos transformados durante la ejecución.


## Descripción del Proyecto
El Reto 06 — Amarillo tiene como objetivo desarrollar un flujo completo de análisis y tratamiento de datos, desde su obtención y limpieza hasta el modelado, visualización, NLP y creación de índices para Kibana.

El proyecto incluye:
- Limpieza y preprocesamiento de datos
- Análisis exploratorio y visualización
- Segmentación de clientes mediante clustering
- Modelado predictivo con y sin PCA
- Enriquecimiento de datos mediante API
- Web scraping y NLP
- Exportación de resultados para análisis posterior

Se busca garantizar trazabilidad, modularidad y reproducibilidad en todo el flujo de trabajo.

------------------------------------------------------------------

## ESTRUCTURA DEL PROYECTO
```text
RETO_06_Amarillo/
│
├── .vscode/
├── Datos/
│   ├── Originales/
│   │   └── .gitkeep       # Para evitar carpeta vacía 
│   └── Transformados/
│       └── .gitkeep       # Carpeta de salida de todos los to_csv
│
├── Graficos/          # Carpeta para almacenar gráficos generados
├── config_files/
│   └── api_config.json    # CODIGO_API ,poder acceder API
├── packages/
│   └── Preprocesamiento/
│       └── funcion_limpieza.py # Funciones reutilizables 
│
├── 01- Limpieza_Final.ipynb
├── 02- Analisis_Exploratorio_Final.ipynb
├── 03- Clustering.ipynb
├── 03-Visualizacion.ipynb
├── 04- Análisis Clústeres.ipynb
├── 05- Api Reto 06.ipynb
├── 06.1- Modelado_Sin_PCA.ipynb
├── 06.2- Modelado_Con_PCA.ipynb
├── 07- Scraping.ipynb
├── 08.1- NLP_vitoria.ipynb
├── 08.2- NLP_Madrid.ipynb
├── 08.3- NLP_donosti.ipynb
├── 08.4- NLP_cordoba.ipynb
├── 09- KIBANA_indux.ipynb
│
├── Entorno_AMARILLO_R6.yml
├── RETO_06_Amarillo.code-workspace
├── README.md
├── .gitignore
└── desktop.ini
```
------------------------------------------------------------------

## Organizacion y Flujo de datos:
Carpetas de datos

Datos/Originales/:
Contiene los datasets en bruto. Nunca se modifican los archivos originales.
`.gitkeep` asegura que la carpeta se suba a GitHub aunque esté vacía.

Datos/Transformados/:
Carpeta de salida donde se guardan todos los archivos generados o transformados.
Todos los `to_csv()` del proyecto se dirigen a esta carpeta para mantener los datos originales intactos.
`.gitkeep` permite mantener la estructura en el repositorio.


## Configuracion de API
Para el acceso a la API, se utiliza config_files/codigo_api.json que contiene:
- CODIGO_API: Clave o contraseña para autenticación en la API
Esto centraliza las credenciales y evita exponerlas directamente en los notebooks o scripts.


# Instrucciones para instalar el entorno (R6_Amarillo):
Version pyhton utilizada : 3.12

1. Requisitos previos

Antes de crear el entorno, asegúrate de tener instalados los siguientes programas:
- **Anaconda**(gestor de entornos y paquetes de Python)
- **Git** (para controlar versiones y clonar repositorios)
- **Visual Studio Code** (editor de código recomendado)

Archivo Entorno_AMARILLO_R6.yml en la raíz del proyecto (define todas las dependencias necesarias)

2. Crear el entorno con Conda

2.1 Abre Anaconda Prompt o tu terminal preferida
2.2 Navega hasta la carpeta del proyecto donde se encuentra el archivo Entorno_AMARILLO_R6.yml:

    `cd ruta/a/RETO_06_Amarillo`

Ejecuta el siguiente comando para crear el entorno:
    `conda env create -f Entorno_AMARILLO_R6.yml`

3. Activar el entorno

Para empezar a usar el entorno, ejecuta:
    `conda activate reto06_Amarillo`

4. Crear el kernel para Jupyter / VS Code
Para poder usar el entorno dentro de Jupyter Notebook o VS Code, ejecuta:
    `python -m ipykernel install --user --name reto06_Amarillo --display-name "Python (reto06_Amarillo)"`
(--name define el nombre interno del kernel

--display-name define cómo aparecerá en Jupyter o VS Code)

5. Seleccionar el intérprete en Visual Studio Code
5.1 Abre el proyecto en VS Code (recomendado usando el archivo .code-workspace)
5.2 Abajo a la derecha, haz clic en “Seleccionar intérprete”
5.3 Elige Python (reto06_Amarillo)
5.4 Con esto, todos los notebooks y scripts ejecutarán Python usando el entorno correcto

------------------------------------------------------------------

FLUJO GENERAL DEL PROYECTO

- 1. Limpieza de datos → `01- Limpieza_Final.ipynb`
- 2. Análisis exploratorio y visualización → `02- Analisis_Exploratorio_Final.ipynb` y `03-Visualizacion.ipynb`

- 3. Clustering y análisis de clusters → `03-Clustering.ipynb` y `04- Análisis Clústeres.ipynb`

- 4. Consumo de API → `05- Api Reto 06.ipynb`

- 5. Modelado predictivo → `06.1- Modelado_Sin_PCA.ipynb` y `06.2- Modelado_Con_PCA.ipynb`

- 6. Web scraping y NLP → `07- Scraping.ipynb`, `08.1-08.4 NLP_*.ipynb`

- 7. Creación de índices para Kibana → `09- KIBANA_indux.ipynb`