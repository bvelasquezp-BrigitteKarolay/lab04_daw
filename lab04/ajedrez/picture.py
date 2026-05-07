from colors import *
class Picture:
    def __init__(self, img):
        self.img = img
    def __eq__(self, other):
        return self.img == other.img
    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        """Devuelve el espejo vertical de la imagen"""
        vertical = []
        for fila in self.img:
            vertical.append(fila[::-1])
        return Picture(vertical)

    def horizontalMirror(self):
        """Devuelve el espejo horizontal de la imagen"""
        horizontal = self.img[::-1]
        return Picture(horizontal)

    def negative(self):
        """Devuelve el negativo de la imagen"""
        imagenInvertida = []
        for fila in self.img:
            nuevaFila = []
            for caracter in fila:
                nuevaFila.append(self._invColor(caracter))
            imagenInvertida.append("".join(nuevaFila))
        return Picture(imagenInvertida)

    def join(self, picture2):
        """
        Devuelve una nueva figura poniendo la figura del argumento
        al lado derecho de la figura actual
        """
        nuevaImagen = []
        for i in range(len(self.img)):
            nuevaImagen.append(self.img[i] + picture2.img[i])
        return Picture(nuevaImagen)
    
    def up(self, picture2):
        """
        Devuelve una nueva figura poniendo la figura recibida
        como argumento encima de la figura actual
        """
        return Picture(picture2.img + self.img)

    def under(self, picture2):
        """
        Devuelve una nueva figura poniendo la figura recibida
        como argumento sobre la figura actual
        """
        nuevaImagen = []
        for i in range(len(self.img)):
            linea = []
            for j in range(len(self.img[i])):
                if picture2.img[i][j] == " ":
                    linea.append(self.img[i][j])
                else:
                    linea.append(picture2.img[i][j])
            nuevaImagen.append("".join(linea))
        return Picture(nuevaImagen)

    def horizontalRepeat(self, n):
        """
        Devuelve una nueva figura repitiendo la figura actual
        al costado la cantidad de veces indicada por n
        """
        nuevaImagen = []
        for fila in self.img:
            nuevaImagen.append(fila * n)
        return Picture(nuevaImagen)

    def verticalRepeat(self, n):
        """
        Devuelve una nueva figura repitiendo la figura actual
        debajo la cantidad de veces indicada por n
        """
        nuevaImagen = []
        for i in range(n):
            for fila in self.img:
                nuevaImagen.append(fila)
        return Picture(nuevaImagen)

    # Extra
    def rotate(self):
        """
        Devuelve una figura rotada 90 grados en sentido horario
        """
        filas = len(self.img)
        columnas = len(self.img[0])
        nuevaImagen = []
        for j in range(columnas):
            nuevaFila = ""
            for i in range(filas - 1, -1, -1):
                nuevaFila += self.img[i][j]
            nuevaImagen.append(nuevaFila)
        return Picture(nuevaImagen)
    