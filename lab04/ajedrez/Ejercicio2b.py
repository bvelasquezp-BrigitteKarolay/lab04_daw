from interpreter import draw
from chessPictures import *


dibujo = knight.join(knight.negative()).verticalMirror().up(knight.join(knight.negative()))
draw(dibujo)