# TP4-Hough-Transformacion
# TP4 – Transformación de Hough en Visión por Computadora

Este proyecto forma parte del Trabajo Práctico N° 4 de la materia **Inteligencia Artificial** (Lic. en Informática, Universidad Siglo 21), cuyo objetivo es dotar a un sistema industrial automatizado de una autonomía mínima a través del procesamiento de imágenes.

##  Problemática

En una planta de montaje de motores, los brazos robotizados fallan ocasionalmente al colocar una pieza debido a desplazamientos mínimos del block del motor sobre la cinta transportadora. La solución debe ser simple, efectiva y autónoma.

##  Objetivo

Implementar prototipos funcionales utilizando la **Transformación de Hough** para detectar figuras geométricas (rectas y circunferencias) que permitan identificar la posición real de piezas y así corregir su montaje automáticamente.

##  Prototipos

### 1. Transformación de Hough para Rectas

- Generación manual de imagen con dos líneas diagonales.
- Implementación desde cero (sin OpenCV).
- Visualización del espacio de parámetros (acumulador).

 Ejemplos:

![Imagen de líneas](imagenes/imagen_rectas.png)  
![Acumulador de líneas](imagenes/acumulador_rectas.png)

### 2. Transformación de Hough para Circunferencias

- Dibujo manual de una circunferencia de radio conocido.
- Cálculo de su centro mediante votación en el acumulador.
- Resultados visuales del centro detectado.

 Ejemplos:

![Imagen con circunferencia](imagenes/imagen_circunferencia.png)  
![Acumulador de centros](imagenes/acumulador_circunferencia.png)

##  Informe

El repositorio incluye el informe final en PDF con justificación teórica, análisis de enfoques (búsqueda, redes neuronales y Hough), y recomendación fundamentada.

##  Lenguaje y herramientas

- Python 3.13
- Matplotlib
- NumPy

##  Restricciones del TP

- Sin uso de bibliotecas externas de visión (ej. OpenCV).
- Implementación desde cero para fines didácticos.
- Código auténtico y documentado.

## Autor

Julián Ottonello – Licenciatura en Informática – Universidad Siglo 21
