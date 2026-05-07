# ♟️ Ajedrez con Pygame — Laboratorio 04

## Integrantes
- Karolay
- Valeria
- Jhonathan

---

## Descripción del proyecto

Este proyecto fue desarrollado como parte del **Laboratorio 04 de Python**. El objetivo principal fue trabajar con figuras de ajedrez representadas mediante estructuras de datos, aplicando programación orientada a objetos y transformaciones sobre imágenes usando la clase `Picture`.

Más que construir un ajedrez interactivo completo, el laboratorio se enfocó en **manipular figuras**, combinarlas, invertirlas, repetirlas y reflejarlas, para luego mostrarlas en pantalla con ayuda de `pygame` y del módulo `interpreter`.

También se trabajó con un **entorno virtual (`venv`)** para mantener ordenadas las dependencias del proyecto y facilitar su ejecución.

---

## Lo que se implementó

Durante el laboratorio se completaron e implementaron métodos importantes dentro de `picture.py`, entre ellos:

- `verticalMirror()`
- `horizontalMirror()`
- `negative()`
- `join()`
- `up()`
- `under()`
- `horizontalRepeat()`
- `verticalRepeat()`
- `rotate()` *(extra)*

Estos métodos permitieron construir distintas composiciones visuales a partir de piezas como:

- `knight`
- `queen`
- `pawn`
- `rock`
- `bishop`
- `king`
- `square`

---

## Idea general del laboratorio

La base del trabajo fue la clase `Picture`, que guarda una imagen como una lista de strings en el atributo `img`.  
A partir de esa representación interna, se fueron creando nuevas figuras aplicando transformaciones como:

- invertir colores,
- reflejar imágenes,
- unir figuras al costado,
- colocar una figura encima de otra,
- repetir patrones horizontal y verticalmente.

Eso permitió pasar de figuras simples a composiciones más complejas como tableros y aperturas de ajedrez.

---

## Estructura del proyecto

```bash
DAW_MAINN/
├── lab04/
│   ├── ajedrez/
│   │   ├── chessPictures.py
│   │   ├── colors.py
│   │   ├── picture.py
│   │   ├── interpreter.py
│   │   ├── pieces.py
│   │   ├── Ejercicio2a.py
│   │   ├── Ejercicio2b.py
│   │   ├── Ejercicio2c.py
│   │   ├── Ejercicio2d.py
│   │   ├── Ejercicio2e.py
│   │   ├── Ejercicio2f.py
│   │   ├── Ejercicio2g.py
│   │   ├── Ejercicio2h.py
│   │   ├── Ejercicio2i.py
│   │   └── main.py
│   ├── img/
│   └── venv/
└── README.md

```

## Requisitos
- Python 3.11 o superior compatible
- pip
- pygame
- entorno virtual venv
- Cómo ejecutar el proyecto
- 
# 1. Activar el entorno virtual

En Windows (PowerShell):

.\venv\Scripts\activate

En Git Bash:

source venv/Scripts/activate
# 2. Instalar dependencias

Si el proyecto usa requirements.txt:

pip install -r requirements.txt

Si solo necesitas instalar pygame:

pip install pygame
# 3. Ejecutar un ejercicio

Cada archivo Ejercicio2x.py se ejecuta por separado.

- python Ejercicio2a.py
- python Ejercicio2b.py
- python Ejercicio2c.py
- python Ejercicio2d.py
- python Ejercicio2e.py
- python Ejercicio2f.py
- python Ejercicio2g.py
- python Ejercicio2h.py
- python Ejercicio2i.py

## Métodos de Picture
# negative()

Convierte la figura en su negativo, cambiando cada color por su inverso.

# join()

Une dos figuras horizontalmente, una al lado de la otra.

# up()

Coloca una figura encima de otra.

# under()

Superpone una figura sobre otra, respetando los espacios vacíos.

# horizontalRepeat(n)

Repite una figura varias veces al costado.

# verticalRepeat(n)

Repite una figura varias veces hacia abajo.

# verticalMirror()

Invierte cada fila de la figura.

# horizontalMirror()

Invierte el orden de las filas de la figura.

## Ejercicios desarrollados

En el laboratorio se trabajaron ejercicios progresivos que permitieron comprobar el funcionamiento de los métodos implementados.

# Ejercicio 2.a: composición de caballos alternando colores.
# Ejercicio 2.b: uso de verticalMirror() sobre la composición de caballos.
# Ejercicio 2.c: repetición horizontal de la reina.
# Ejercicio 2.d: franja alternada de casillas.
# Ejercicio 2.e: variación del patrón anterior invirtiendo el orden.
# Ejercicio 2.f: construcción de una figura más grande con varias filas.
# Ejercicio 2.g: armado del tablero completo de ajedrez.
# Ejercicio 2.h: representación de la Apertura Italiana.
# Ejercicio 2.i: representación de la Apertura Escocesa.



## Video de demostración

https://drive.google.com/file/d/1P8eGzdGdpn36iFGAgrOZVLzTaP1Gjrxc/view?usp=sharing

Repositorio GitHub

## Repositorio del proyecto:
https://github.com/bvelasquezp-BrigitteKarolay/lab04_daw.git

## Conclusiones

Este laboratorio permitió comprender mejor cómo una imagen puede representarse internamente como una estructura de datos y cómo, a partir de esa base, se pueden construir nuevas figuras mediante programación.

También ayudó a reforzar el uso de clases, métodos, listas y ciclos en Python, además de la importancia de trabajar con un entorno virtual para evitar errores al instalar dependencias.

Finalmente, fue una práctica útil para desarrollar lógica paso a paso, ya que cada ejercicio se fue construyendo sobre el anterior hasta llegar a composiciones más completas como el tablero de ajedrez y las aperturas solicitadas.

## Referencias
https://www.w3schools.com/python/python_reference.asp
https://docs.python.org/3/tutorial/
https://virtualenv.pypa.io/en/latest/how-to/usage.html
https://www.geeksforgeeks.org/python/python-pip/
https://www.w3schools.com/python/python_lists.asp
https://edwardo2013.github.io/CCOM_labs_python/LABS/ciclos.html
https://www.w3schools.com/python/python_functions.asp
https://www.w3schools.com/python/python_classes.asp
https://www.geeksforgeeks.org/python/pygame-tutorial/



