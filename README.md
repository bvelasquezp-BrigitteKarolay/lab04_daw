# Ajedrez con pygame
## Descripcion 
Este proyecto consiste en el desarrollo de una representacion de las distintas piezas que conforman el tablero de ajedrez implementada con Python y la libreria Pygame, que permite presentar el dibujo en pantalla.

Se uso el entornovirtual de python para manejar las dependencias del proyecto.

## Estructura del proyecto:
```
DAW_MAINN/
├── lab04/
│   ├── ajedrez/
│   │   ├── __pycache__/
│   │   ├── .gitignore
│   │   ├── chessPictures.py
│   │   ├── colors.py
│   │   ├── Ejercicio2a.py
│   │   ├── Ejercicio2b.py
│   │   ├── Ejercicio2c.py
│   │   ├── Ejercicio2d.py
│   │   ├── Ejercicio2e.py
│   │   ├── Ejercicio2f.py
│   │   ├── Ejercicio2g.py
│   │   ├── Ejercicio2h.py
│   │   ├── Ejercicio2i.py
│   │   ├── interpreter.py
│   │   ├── main.py
│   │   ├── picture.py
│   │   └── pieces.py
│   ├── img/
│   ├── python_basic/
│   ├── venv/
│   └── README.md
└── venv/
```
---
## Como ejecutar el proyecto
### Requisitos:
* python 3.13 o inferior
* pip acorde a la version de python
### Crear entorno virtual:
* Cree el entorno virtual con el siguiente comando:
```
python3 -m venv <nombre del entorno>
```
* copie la carpeta ```ajedrez``` y el archivo ```requirements.txt``` dentro de la carpeta creada
```
cp -rfv <ruta/a/ajetrez> <ruta/a/requirements.txt> <ruta/a/el/entorno>
```
---
### Iniciar entorno virutal
* Dentro de la carpeta de el entorno, nicie el entorno ejecutando (si esta en una distribucion de linux)
```
source bin/activate
```
* O caso este en windows
```
Scripts/activate
```
* Ahora la linea de comandos deberia ser precedida por el nombre de su entorno
```
(Nombre del entorno) Ususario@Maquina:
```
---
### Instalacion de dependencias y ejecucion
* Dento del entorno, ahora descarga instala las dependencias y paquetes del proyecto del requirements.txt con el siguiente comando 
```
pip install -r requirements.txt
```
* Ahora puedes ejecutar los ejercicios del directorio ajedrez directamente
```
python3 ajedrez/Ejercicio2X.py
```
