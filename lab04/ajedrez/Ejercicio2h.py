from interpreter import draw
from chessPictures import *


# negras atras
fila8 = rock.negative() \
    .join(square) \
    .join(knight.negative()) \
    .join(queen.negative()) \
    .join(king.negative()) \
    .join(bishop.negative()) \
    .join(knight.negative()) \
    .join(rock.negative())

# peones negros
fila7 = pawn.negative() \
    .join(pawn.negative()) \
    .join(pawn.negative()) \
    .join(pawn.negative()) \
    .join(square) \
    .join(pawn.negative()) \
    .join(pawn.negative()) \
    .join(pawn.negative())

# caballo negro en c6
fila6 = square \
    .join(square) \
    .join(knight.negative()) \
    .join(square.horizontalRepeat(5))

# peon negro en e5
fila5 = square.horizontalRepeat(4) \
    .join(pawn.negative()) \
    .join(square.horizontalRepeat(3))

# alfil blanco en c4 y peon blanco en e4
fila4 = square.horizontalRepeat(2) \
    .join(bishop) \
    .join(square) \
    .join(pawn) \
    .join(square.horizontalRepeat(3))

# caballo blanco en f3
fila3 = square.horizontalRepeat(5) \
    .join(knight) \
    .join(square.horizontalRepeat(2))

# peones blancos
fila2 = pawn \
    .join(pawn) \
    .join(pawn) \
    .join(pawn) \
    .join(square) \
    .join(pawn) \
    .join(pawn) \
    .join(pawn)

# blancas atras
fila1 = rock \
    .join(knight) \
    .join(bishop) \
    .join(queen) \
    .join(king) \
    .join(square) \
    .join(square) \
    .join(rock)

figura = fila8 \
    .under(fila7) \
    .under(fila6) \
    .under(fila5) \
    .under(fila4) \
    .under(fila3) \
    .under(fila2) \
    .under(fila1)

draw(figura)