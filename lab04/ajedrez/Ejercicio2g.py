from interpreter import draw
from chessPictures import *

# tablero
fila1 = square.join(square.negative()).horizontalRepeat(4)
fila2 = square.negative().join(square).horizontalRepeat(4)

# piezas blancas
blancas = rock.join(knight) \
    .join(bishop) \
    .join(queen) \
    .join(king) \
    .join(bishop) \
    .join(knight) \
    .join(rock)

# peones blancos
peones_blancos = pawn.horizontalRepeat(8)

# piezas negras
negras = blancas.negative()

# peones negros
peones_negros = peones_blancos.negative()

figura = negras \
    .under(peones_negros) \
    .under(fila1) \
    .under(fila2) \
    .under(fila1) \
    .under(fila2) \
    .under(peones_blancos) \
    .under(blancas)

draw(figura)