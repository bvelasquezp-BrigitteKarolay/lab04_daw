from interpreter import draw
from chessPictures import *


dibujo = knight.negative().join(knight).up(knight.join(knight.negative()))
draw(dibujo)