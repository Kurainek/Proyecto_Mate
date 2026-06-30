# Proyecto_Mate: Matemática Discreta - Ruta Óptima en Auto (India) 🚗
Proyecto de Matemática Discreta: Cálculo de ruta óptima entre ciudades mediante un grafo ponderado en Python.

**Integrante:** Bernardo Sandoval Cordova

## Descripción General del Proyecto
Este proyecto consiste en el diseño e implementación de una aplicación en Python para resolver un problema de camino mínimo utilizando la teoría de grafos. Se modeló una red de carreteras que conecta 15 de las ciudades más importantes de la India.

El problema se representa matemáticamente mediante un grafo ponderado no dirigido `G = (V, E, w)`:
* **Vértices (V):** Representan las 15 ciudades seleccionadas.
* **Aristas (E):** Representan 21 conexiones reales por carretera entre estas ciudades.
* **Pesos (w):** Corresponden a la distancia de conducción real en kilómetros entre cada par de ciudades conectadas.

Para encontrar la ruta óptima entre una ciudad de origen y una de destino, la aplicación implementa el **Algoritmo de Dijkstra**. Este algoritmo fue seleccionado por su alta eficiencia y exactitud para encontrar el camino más corto en grafos donde todos los pesos son valores positivos (como es el caso de las distancias físicas).

## Estructura del Repositorio
Para mantener el orden y facilitar la evaluación, el repositorio contiene los siguientes archivos fundamentales:

* `Proyecto.py`: Contiene el código fuente completo de la aplicación, incluyendo la definición del grafo, la implementación del algoritmo y la interfaz gráfica.
* `datos_grafo.csv`: Base de datos tabulada que detalla explícitamente las ciudades conectadas, las distancias en kilómetros y la fuente de donde se extrajo la información (Google Maps).
* `requirements.txt`: Archivo de texto con las dependencias necesarias para ejecutar el entorno del proyecto.
* `README.md`: Este documento, que explica la estructura, modelo y uso de la aplicación.

## Librerías y Requisitos
El proyecto está desarrollado en Python 3.12.1. Para su correcto funcionamiento, hace uso de las siguientes librerías:
* `networkx`: Motor principal del proyecto. Se utiliza para la creación de la estructura de datos del grafo, la manipulación de nodos/aristas y la ejecución interna del algoritmo de Dijkstra.
* `matplotlib`: Encargada de renderizar y mostrar visualmente el grafo matemático y la ruta calculada.
* `tkinter`: Librería nativa de Python utilizada para construir la Interfaz Gráfica de Usuario (GUI), permitiendo la interacción amigable con el programa.

## Instrucciones de Ejecución

Sigue estos pasos para iniciar la aplicación en tu entorno local de manera correcta:

1. **Clonar el repositorio:**
   Abre tu terminal y descarga el proyecto usando Git:
   ```bash
   git clone https://github.com/Kurainek/Proyecto_Mate.git
   cd Proyecto_Mate
## Instalar las dependencias:
Se recomienda utilizar un entorno virtual. Para instalar las librerías requeridas, ejecuta:

Bash
pip install -r requirements.txt
Iniciar la Aplicación:
Una vez instaladas las dependencias, ejecuta el archivo principal:

Bash
python Proyecto.py

## Guía de Uso de la Interfaz
Al ejecutar el programa, se abrirá una ventana con la red de ciudades dibujada en el panel derecho.

Dirígete al panel izquierdo llamado "CONFIGURACIÓN".

Selecciona una Ciudad de Origen y una Ciudad de Destino utilizando los menús desplegables.

Presiona el botón azul "Calcular Ruta Óptima".

En la sección RESULTADOS aparecerá un reporte detallado que incluye:

El recorrido paso a paso (nodo a nodo).

La distancia total a recorrer en kilómetros.

El tiempo estimado de viaje en automóvil (calculado en base a una velocidad promedio realista de 80 km/h).

Simultáneamente, en el mapa de la derecha, la ruta óptima calculada se trazará y resaltará en color negro, diferenciándose del resto de la red.