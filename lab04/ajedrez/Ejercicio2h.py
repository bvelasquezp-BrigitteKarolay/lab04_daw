from interpreter import draw
from chessPictures import *

tablero = square.negative().up(square).join(square.up(square.negative())).horizontalRepeat(4).verticalRepeat(4)
fichas1 = rock.up(pawn).up(square.negative()).up(square).up(square.negative()).up(square).up(pawn.negative()).up(rock.negative())
fichas2 = knight.up(pawn).up(square).up(square.negative()).up(square).up(square.negative()).up(pawn.negative()).up(square.negative())
fichas3 = bishop.up(pawn).up(square.negative()).up(bishop).up(square.negative()).up(king.negative()).up(pawn.negative()).up(bishop.negative())
fichas4 = queen.up(pawn).up(square).up(square.negative()).up(square).up(square.negative()).up(pawn.negative()).up(queen.negative())
fichas5 = king.up(square).up(square.negative()).up(pawn).up(pawn.negative()).up(square).up(square.negative()).up(king.negative())
fichas6 = square.up(pawn).up(knight).up(square.negative()).up(square).up(square.negative()).up(pawn.negative()).up(bishop.negative())
fichas7 = square.negative().up(pawn).up(square.negative()).up(square).up(square.negative()).up(square).up(pawn.negative()).up(knight.negative())
fichas8 = rock.up(pawn).up(square).up(square.negative()).up(square).up(square.negative()).up(pawn.negative()).up(rock.negative())
fichasco = fichas1.join(fichas2).join(fichas3).join(fichas4).join(fichas5).join(fichas6).join(fichas7).join(fichas8)

draw(tablero.under(fichasco))