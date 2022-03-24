# Proyecto 1
Alumno: Alberto Espinosa Juárez

Programa Académico: Maestría en Ciencias de la Computación

## ¿Qué contiene el proyecto 1?
El proyecto 1 consiste de una biblioteca que se encuentra dentro de la carpeta "Proyecto_01" en ella se encuentran:
+ nodo.py Archivo que contiene la clase que define a un nodo y sus métodos
+ arista.py Archivo que contiene la clase que define a una arista y sus métodos
+ grafo.py Archivo que contiene la clase que define a un grafo y sus métodos, además, contiene los algortimos descritos para el proyecto 1
+ grafo2dot.py Archivo que hace la conversión o traducción a lenguaje DOT para hacerlo compatible con GraphViz y posteriormente abrirlo con el software de visualización de grafos Gephi
+ main.py Archivo que contiene la generación y guardado de cada uno de los 18 ejemplos para este proyecto 1 (3 de cada algoritmo)
+ Carpeta archivos_gv_e_imagenes Que contiene por subcarpetas los algortimos con sus correspondientes archivos .gv e imágenes
+ proyecto01_ipynb este archivo es un notebook en caso de quererlo replicar en Notebook

## Ejecución en local y en nube (Colab)
Para este proyecto realicé dos versiones
1. Ejecución en nube utilizando Google Colab. Para ejecutar el código se debe ir a la siguiente liga https://colab.research.google.com/drive/1pPVct7vIxeCeOwvTjumvnhrN7ooNv31g?usp=sharing y ejecutar todas las celdas (iniciando de arriba para abajo). No debería existir problema alguno
2. Ejecución en local. Si se clona el repositorio se puede ejecutar en local. Solo se pide leer antes el archivo grafo2dot pues es importante (solo en local).

## ¿Cómo veo la documentación?
Para revisar la documentación es necesario hacer uso del método *help(método)* que nos brindará información sobre cómo y qué hace un método.

**Ejemplo**

help(guardar_grafo)

**Desplegará información sobre el método guardar_grafo así como también de los parámetros que recibe**

## Resúmen del proyecto 1

### Modelo de malla
#### Malla 30 nodos (5x6)
![Grafo en malla de 30 nodos (5x6)][malla1]
#### Malla 100 nodos (10x10)
![Grafo en malla de 100 nodos (10x10)][malla2]
#### Malla 500 nodos (50x10)
![Grafo en malla de 500 nodos (50x10)][malla3]


[malla1]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/malla/malla_30.png "Malla 30"
[malla2]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/malla/malla_100.png "Malla 100"
[malla3]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/malla/malla_500.png "Malla 500"

### Modelo Erdos y Renyi
**Nota: Se utilizó la distribución Fruchterman para el modelo de Erdos y Renyi**

#### Erdos y Renyi 30 nodos 400 aristas
![Grafo erdos renyi 30 nodos y 400 aristas][erdos1]
#### Erdos y Renyi 100 nodos 1500 aristas
![Grafo erdos renyi 100 nodos y 1500 aristas][erdos2]
#### Erdos y Renyi 500 nodos y 4000 aristas
![Grafo erdos renyi 500 nodos y 4000 aristas][erdos3]

[erdos1]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/erdos_renyii/erdos_30_400.png
[erdos2]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/erdos_renyii/erdos_100_1500.png
[erdos3]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/erdos_renyii/erdos_500_4000.png

### Modelo Gilbert
#### Gilbert de 30 nodos y probabilidad de 0.7
![Gilbert 30 nodos][gilbert1]
#### Gilbert de 100 nodos y probabilidad de 0.6
![Gilbert 100 nodos][gilbert2]
#### Gilbert de 500 nodos y probabilidad de 0.04
![Gilbert 500 nodos][gilbert3]

[gilbert1]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/gilbert/gilbert_30_07.png
[gilbert2]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/gilbert/gilbert_100_06.png
[gilbert3]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/gilbert/gilbert_500_004.png

### Modelo geográfico
#### Geografico de 30 nodos y distancia 0.4
![geografico 30 nodos][geo1]
#### Geografico de 100 nodos y distancia 0.3
![geografico 100 nodos][geo2]
#### Geografico de 500 nodos y distancia 0.1
![geografico 500 nodos][geo3]

[geo1]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/geografico/geografico_30_04.png
[geo2]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/geografico/geografico_100_03.png
[geo3]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/geografico/geografico_500_01.png

### Modelo Barabási-Albert
#### Modelo Barabási-Albert 30 nodos y grado 5
![albert 30 nodos][albert1]
#### Modelo Barabási-Albert 100 nodos y grado 9
![albert 100 nodos][albert2]
### Modelo Barabási-Albert 500 nodos y grado 20
![aberto 500 nodos][albert3]

[albert1]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/babarasi/babarasi_30_05.png
[albert2]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/babarasi/babarasi_100_09.png
[albert3]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/babarasi/babarasi_500_20.png

### Modelo Dorogovtsev-Mendes
#### Modelo Dorogovtsev-Mendes 30 nodos
![Dorogovtsev-Mendes 30 nodos][mendes1]
#### Modelo Dorogovtsev-Mendes 100 nodos
![Dorogovtsev-Mendes 100 nodos][mendes2]
#### Modelo Dorogovtsev-Mendes 500 nodos
![Dorogovtsev-Mendes 500 nodos][mendes3]

[mendes1]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/dorogovtsev_mendes/dorogovtsev_mendes_30.png
[mendes2]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/dorogovtsev_mendes/dorogovtsev_mendes_100.png
[mendes3]: https://github.com/AlbertoEJ/ADA/blob/main/Proyecto_01/archivos_gv_e_imagenes/dorogovtsev_mendes/dorogovtsev_mendes_500.png
