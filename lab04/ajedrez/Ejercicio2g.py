from interpreter import draw
from chessPictures import *

otros = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)
peones = pawn.horizontalRepeat(8)
campoabierto = square.negative().up(square).join(square.up(square.negative())).horizontalRepeat(4)

tablero = campoabierto.under(otros.up(peones)).up(campoabierto.verticalRepeat(2).up(campoabierto.under(peones.up(otros).negative())))
draw(tablero)