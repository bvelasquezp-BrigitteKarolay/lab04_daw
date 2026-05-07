# Laboratorio 04: Ajedrez con Python

## Integrantes
- Karolay Valeria
- Jhonathan

---

## Descripción del proyecto

Este proyecto implementa la manipulación de imágenes tipo ASCII utilizando listas de strings en Python.  
Se trabaja con la clase `Picture`, que permite transformar y combinar figuras para construir representaciones como tableros y piezas de ajedrez.

El proyecto utiliza `pygame` para la visualización gráfica.

---

## Requisitos

- Python 3.x
- pip
- pygame

---

## Activación del entorno virtual (venv)

### Crear entorno virtual
```bash
python -m venv venv
````

### Activar en Windows

```bash
venv\Scripts\activate
```

### Activar en Linux / Mac

```bash
source venv/bin/activate
```

---

## Instalación de dependencias

Con el entorno virtual activado:

```bash
pip install pygame
```

---

## Ejecución del proyecto

### Ejecutar programa principal

```bash
python ajedrez/main.py
```

### Ejecutar ejercicios

```bash
python ajedrez/Ejercicio2a.py
python ajedrez/Ejercicio2b.py
python ajedrez/Ejercicio2c.py
python ajedrez/Ejercicio2d.py
```

---

## Notas

* Todas las figuras se construyen manipulando el atributo `img` de la clase `Picture`.
* Las transformaciones incluyen espejos, rotaciones, composición y repetición.
* La visualización se realiza mediante `pygame`.

---

## Conclusión

Este laboratorio permite comprender la construcción de figuras complejas a partir de estructuras simples, aplicando programación orientada a objetos y manipulación de datos en Python.

```

